"""
Full filament profile audit against all documented rules.

Checks (by section):
  A. File format — no banned header keys, identity coherence
  B. Inheritance — target exists, no redundant keys matching parent
  C. Cool plate temperatures — PLA=40 initial, PETG=50/50
  D. Hardened Steel temps — BRASS=base, HS=base+delta, initial_HS <= range_high
  E. Nozzle variants — temp deltas correct, MVS scaling correct, 0.25mm capped at 3
  F. MVS reference table — 0.4mm root profiles within acceptable range of reference
  G. KX hardware rules — air_filtration=0, aux_fan=0 on KX
  H. Cross-printer contamination — no KX in KS1 compat, no KS1 in KX compat
  I. TPU caps — HS 0.6mm=5, HS 0.8mm=7 (hard caps, not scaling)

Outputs: AUDIT_REPORT.md with all findings grouped by severity.
"""
import json, glob, os

SYS = 'C:/Users/pandrade/AppData/Roaming/AnycubicSlicerNext/system/Anycubic/filament'
FILAMENT_DIR = 'filament'

# ── Reference data ────────────────────────────────────────────────────────────
BANNED_KEYS = {'type', 'setting_id', 'filament_id', 'instantiation',
               'filament_type', 'bed_type', 'filament_load_time', 'filament_unload_time'}

TEMP_KEYS = ['nozzle_temperature', 'nozzle_temperature_initial_layer',
             'nozzle_temperature_BRASS', 'nozzle_temperature_initial_layer_BRASS',
             'nozzle_temperature_HS', 'nozzle_temperature_initial_layer_HS',
             'nozzle_temperature_range_high']

# MVS reference table [KX, KS1] — tolerance ±2
MVS_REF = {
    'rapid_petg':       [18, 21],
    'standard_petg':    [13, 15],
    'translucent_petg': [11, 13],
    'petg_gf':          [11, 13],
    'petg_cf':          [12, 14],
    'rapid_plaplus':    [20, 24],
    'standard_plaplus': [16, 19],
    'standard_pla':     [13, 16],
    'pla_matte':        [14, 16],
    'translucent_pla':  [15, 17],
    'pla_silk':         [10, 12],
    'pla_galaxy':       [13, 15],
    'pla_glow':         [13, 15],
    'pla_cf':           [16, 19],
    'tpu_standard':     [ 4,  5],
    'tpu_hs':           [ 8, 10],
}
MVS_TOLERANCE = 2  # acceptable deviation from reference

NOZZLE_SCALE = {'0.6mm': 1.25, '0.8mm': 1.50, '0.25mm': 0.50}
PLA_TEMP_DELTA  = {'0.25mm': -5, '0.6mm': 5, '0.8mm': 10}
PETG_TEMP_DELTA = {'0.6mm': 10, '0.8mm': 15}
TPU_HS_CAPS = {'0.6mm': 5, '0.8mm': 7}


# ── Helpers ───────────────────────────────────────────────────────────────────
def get(d, k):
    v = d.get(k)
    return (v[0] if isinstance(v, list) else v) if v is not None else None

def fmt_mvs(v):
    f = round(float(v), 1)
    return int(f) if f == int(f) else f

def classify(name):
    n = name.lower()
    is_kx  = '@ac kx'  in n
    is_ks1 = '@ac ks1' in n
    printer = 'KX' if is_kx else ('KS1' if is_ks1 else None)
    if printer is None: return None, None
    if any(x in n for x in ['rapid petg','tecbears rapid petg','improved petg hs']): return 'rapid_petg', printer
    if any(x in n for x in ['translucent petg','petg translucent']): return 'translucent_petg', printer
    if any(x in n for x in ['petg gf','justmaker petg']): return 'petg_gf', printer
    if any(x in n for x in ['petg cf','petg carbon']): return 'petg_cf', printer
    if 'petg' in n: return 'standard_petg', printer
    if any(x in n for x in ['rapid pla+','pla+ 2.0']): return 'rapid_plaplus', printer
    if any(x in n for x in ['pla cf','pla-cf']): return 'pla_cf', printer
    if any(x in n for x in ['silk dual','silk pla','pla silk']): return 'pla_silk', printer
    if any(x in n for x in ['matte pla+','matte pla','pla matte','overture matte']): return 'pla_matte', printer
    if any(x in n for x in ['pla galaxy','galaxy pla','glitter','hyper pla galaxy']): return 'pla_galaxy', printer
    if any(x in n for x in ['pla glow','glow pla','glow in','polychrome glow']): return 'pla_glow', printer
    if any(x in n for x in ['translucent pla','pla translucent']): return 'translucent_pla', printer
    if any(x in n for x in ['pla metal','metal pla']): return 'pla_silk', printer
    if any(x in n for x in ['pla pro','pla+','plaplus']): return 'standard_plaplus', printer
    if 'pla' in n: return 'standard_pla', printer
    if any(x in n for x in ['tpu hs','tpu high speed','overture high speed tpu']): return 'tpu_hs', printer
    if 'tpu' in n: return 'tpu_standard', printer
    return None, printer

def nozzle_size(name):
    for s in ('0.25mm', '0.6mm', '0.8mm', '0.4mm'):
        if name.endswith(s): return s[:-2]
    return None


# ── Load profiles ─────────────────────────────────────────────────────────────
sys_profiles = {}
for f in glob.glob(f'{SYS}/*.json'):
    with open(f, encoding='utf-8') as fp:
        try: d = json.load(fp)
        except: continue
    sys_profiles[d.get('name','')] = d

user_profiles = {}
for f in sorted(glob.glob(f'{FILAMENT_DIR}/*.json')):
    with open(f, encoding='utf-8') as fp:
        try: d = json.load(fp)
        except Exception as e:
            continue
    name = d.get('name','')
    user_profiles[name] = (f.replace('\\','/'), d)

def resolve(name, key, depth=0):
    if depth > 8: return None
    d = user_profiles[name][1] if name in user_profiles else sys_profiles.get(name)
    if not d: return None
    v = get(d, key)
    if v is not None: return v
    return resolve(d.get('inherits',''), key, depth+1)


# ── Findings ──────────────────────────────────────────────────────────────────
findings = {'ERROR': [], 'WARN': [], 'INFO': []}

def E(profile, check, msg): findings['ERROR'].append((profile, check, msg))
def W(profile, check, msg): findings['WARN'].append((profile, check, msg))
def I(profile, check, msg): findings['INFO'].append((profile, check, msg))


# ── Run checks ────────────────────────────────────────────────────────────────
for name, (fpath, d) in sorted(user_profiles.items()):
    inh = d.get('inherits','')
    compat = d.get('compatible_printers', [])
    is_kx  = '@AC KX'  in name
    is_ks1 = '@AC KS1' in name
    n = name.lower()
    is_petg = 'petg' in n
    is_pla  = 'pla' in n and not is_petg
    is_tpu  = 'tpu' in n
    size = nozzle_size(name)

    # Parent dict
    parent_d = user_profiles[inh][1] if inh in user_profiles else sys_profiles.get(inh)

    # ── A. File format ────────────────────────────────────────────────────────
    for bk in BANNED_KEYS:
        if bk in d:
            W(name, 'A-format', f'banned key present: `{bk}` = {d[bk]!r}')

    info_path = fpath.replace('.json', '.info')
    if not os.path.exists(info_path):
        E(name, 'A-info', '.info file missing')
    else:
        info_sid = None
        for line in open(info_path, encoding='utf-8'):
            if line.strip().startswith('setting_id'):
                info_sid = line.split('=',1)[1].strip()
        if info_sid != name:
            E(name, 'A-info', f'.info setting_id mismatch: {info_sid!r} != {name!r}')

    stem = os.path.splitext(os.path.basename(fpath))[0]
    if stem != name:
        E(name, 'A-identity', f'name {name!r} != filename stem {stem!r}')

    fsi = get(d, 'filament_settings_id')
    if fsi and fsi != name:
        E(name, 'A-identity', f'filament_settings_id {fsi!r} != name {name!r}')

    # ── B. Inheritance ────────────────────────────────────────────────────────
    if inh and inh not in user_profiles and inh not in sys_profiles:
        E(name, 'B-inherit', f'inherits target not found: {inh!r}')

    if parent_d:
        for k, v in d.items():
            if k in BANNED_KEYS: continue
            if k in ('name','inherits','from','is_custom_defined','version',
                     'filament_settings_id','filament_vendor','compatible_printers'): continue
            pv = parent_d.get(k)
            if pv is not None and pv == v:
                I(name, 'B-redundant', f'key `{k}` = {v!r} matches parent exactly (can remove)')

    # ── C. Cool plate temps ───────────────────────────────────────────────────
    if size == '0.4' and '@Anycubic Kobra' in inh:  # root profiles only
        cpt  = get(d, 'cool_plate_temp')
        cpti = get(d, 'cool_plate_temp_initial_layer')
        if is_petg:
            if cpt != '50':
                E(name, 'C-coolplate', f'cool_plate_temp={cpt!r}, expected "50"')
            if cpti != '50':
                E(name, 'C-coolplate', f'cool_plate_temp_initial_layer={cpti!r}, expected "50"')
        elif is_pla:
            if cpti is not None and cpti != '40':
                W(name, 'C-coolplate', f'cool_plate_temp_initial_layer={cpti!r}, expected "40" or not set')

    # ── D. HS temperature rules ───────────────────────────────────────────────
    base_t  = resolve(name, 'nozzle_temperature')
    init_t  = resolve(name, 'nozzle_temperature_initial_layer')
    brass_t = resolve(name, 'nozzle_temperature_BRASS')
    init_br = resolve(name, 'nozzle_temperature_initial_layer_BRASS')
    hs_t    = resolve(name, 'nozzle_temperature_HS')
    init_hs = resolve(name, 'nozzle_temperature_initial_layer_HS')
    rng_hi  = resolve(name, 'nozzle_temperature_range_high')

    hs_delta = 10 if is_petg else 5
    try:
        if base_t and brass_t and int(brass_t) != int(base_t):
            W(name, 'D-hs', f'BRASS={brass_t} != base={base_t} (expected equal)')
        if init_t and init_br and int(init_br) != int(init_t):
            # Allow deliberate +5 first-layer warmup (e.g. Elegoo Rapid PETG KS1)
            delta = int(init_br) - int(init_t)
            if abs(delta) > 5:
                W(name, 'D-hs', f'initial_layer_BRASS={init_br} vs initial_layer={init_t} (delta={delta:+d})')
        if base_t and hs_t and int(hs_t) != int(base_t) + hs_delta:
            actual_delta = int(hs_t) - int(base_t)
            W(name, 'D-hs', f'nozzle_temperature_HS={hs_t} vs base={base_t}: delta={actual_delta:+d}, expected +{hs_delta}')
        if init_hs and rng_hi and int(init_hs) > int(rng_hi):
            E(name, 'D-hs', f'initial_layer_HS={init_hs} > range_high={rng_hi} (violates constraint)')
    except (TypeError, ValueError):
        pass  # nil values — skip

    # ── E. Nozzle variant rules ───────────────────────────────────────────────
    if size in ('0.25', '0.6', '0.8') and inh in user_profiles:
        _, pd = user_profiles[inh]
        if '@Anycubic Kobra' not in pd.get('inherits',''):
            pass  # only check direct 0.4mm children
        else:
            size_key = size + 'mm'
            # Temperature deltas
            is_tpu_var = 'tpu' in n
            if not is_tpu_var:
                delta_map = PETG_TEMP_DELTA if is_petg else PLA_TEMP_DELTA
                delta = delta_map.get(size_key)
                if delta is not None:
                    for tk in TEMP_KEYS:
                        if tk == 'nozzle_temperature_range_high': continue
                        pv = get(pd, tk)
                        cv = get(d, tk)
                        if pv is None or cv is None: continue
                        try:
                            expected = int(pv) + delta
                            if int(cv) != expected:
                                W(name, 'E-nozzle-temp',
                                  f'{tk}: got {cv}, expected {expected} (parent={pv}, delta={delta:+d})')
                        except (ValueError, TypeError): pass

            # MVS scaling
            cur_mvs = get(d, 'filament_max_volumetric_speed')
            if cur_mvs:
                parent_mvs_eff = resolve(inh, 'filament_max_volumetric_speed')
                if parent_mvs_eff:
                    scale = NOZZLE_SCALE.get(size_key, 1.0)
                    if size_key == '0.25mm':
                        expected_mvs = 3
                    else:
                        expected_mvs = fmt_mvs(float(parent_mvs_eff) * scale)

                    is_tpu_hs = any(x in n for x in ['tpu hs','tpu high speed','overture high speed tpu'])
                    if is_tpu_hs and size_key in TPU_HS_CAPS:
                        expected_mvs = TPU_HS_CAPS[size_key]

                    cur_f = float(cur_mvs)
                    exp_f = float(expected_mvs)
                    if abs(cur_f - exp_f) > 0.2:
                        W(name, 'E-nozzle-mvs',
                          f'MVS={cur_mvs}, expected {expected_mvs} (parent={parent_mvs_eff} × {scale})')

    # 0.25mm cap at 3
    if size == '0.25':
        mvs = get(d, 'filament_max_volumetric_speed')
        if mvs and float(mvs) > 3:
            E(name, 'E-025-cap', f'0.25mm MVS={mvs} exceeds cap of 3')

    # ── F. MVS reference table (0.4mm root profiles) ─────────────────────────
    if size == '0.4' and '@Anycubic Kobra' in inh:
        cat, printer = classify(name)
        if cat and printer:
            ref_idx = 0 if printer == 'KX' else 1
            ref = MVS_REF[cat][ref_idx]
            eff_mvs = resolve(name, 'filament_max_volumetric_speed')
            if eff_mvs:
                try:
                    diff = abs(float(eff_mvs) - ref)
                    if diff > MVS_TOLERANCE:
                        W(name, 'F-mvs-ref',
                          f'MVS={eff_mvs} vs reference={ref} (diff={diff:.1f} > tolerance={MVS_TOLERANCE})')
                except (ValueError, TypeError): pass

    # ── G. KX hardware rules (root profiles) ─────────────────────────────────
    if is_kx and size == '0.4' and '@Anycubic Kobra' in inh:
        aaf = resolve(name, 'activate_air_filtration')
        if aaf not in (None, '0', 0):
            E(name, 'G-kx-hw', f'activate_air_filtration={aaf!r} on KX profile (must be 0)')
        acf = resolve(name, 'additional_cooling_fan_speed')
        if acf not in (None, '0', 0):
            W(name, 'G-kx-hw', f'additional_cooling_fan_speed={acf!r} on KX profile (should be 0)')

    # ── H. Cross-printer contamination ───────────────────────────────────────
    if compat:
        has_ks1 = any('Kobra S1' in c for c in compat)
        has_kx  = any('Kobra X' in c for c in compat)
        if has_ks1 and has_kx:
            E(name, 'H-cross', f'compatible_printers lists both S1 and Kobra X')
        if is_ks1 and has_kx:
            E(name, 'H-cross', f'KS1 profile has Kobra X in compatible_printers')
        if is_kx and has_ks1:
            E(name, 'H-cross', f'KX profile has Kobra S1 in compatible_printers')


# ── Write report ──────────────────────────────────────────────────────────────
lines = ['# Full Filament Audit Report', f'Generated: 2026-05-25', '',
         f'Profiles checked: {len(user_profiles)}', '']

for level in ('ERROR', 'WARN', 'INFO'):
    items = findings[level]
    lines.append(f'## {level} ({len(items)})')
    lines.append('')
    if not items:
        lines.append(f'None.')
        lines.append('')
        continue

    # Group by check type
    by_check = {}
    for profile, check, msg in items:
        by_check.setdefault(check, []).append((profile, msg))

    for check, entries in sorted(by_check.items()):
        lines.append(f'### {check} ({len(entries)} issues)')
        lines.append('')
        lines.append('| Profile | Issue |')
        lines.append('|---------|-------|')
        for profile, msg in sorted(entries):
            lines.append(f'| {profile} | {msg} |')
        lines.append('')

with open('AUDIT_REPORT.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')

# Print summary to console
print(f'Profiles checked: {len(user_profiles)}')
for level in ('ERROR', 'WARN', 'INFO'):
    print(f'  {level}: {len(findings[level])}')
print()
for level in ('ERROR', 'WARN'):
    for profile, check, msg in sorted(findings[level]):
        print(f'  [{level}] [{check}] {profile}')
        print(f'         {msg}')
print()
print('Full report: AUDIT_REPORT.md')
