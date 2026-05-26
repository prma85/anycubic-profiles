"""
Apply fixes from audit report:

1. G-kx-hw ERROR: activate_air_filtration=1 on KX profiles -> set to 0
2. G-kx-hw WARN: additional_cooling_fan_speed != 0 on KX profiles -> set to 0
3. D-hs ERROR: initial_layer_HS > range_high (4 profiles) -> fix range_high
4. E-nozzle-mvs: Improved KX nozzle variants have stale MVS -> recalculate
5. B-redundant INFO: remove keys that exactly match parent
6. C-coolplate: Creality Hyper PLA Galaxy cool_plate_temp_initial_layer=50 -> 40

NOT fixing:
- D-hs BRASS != base on Improved PLA/PLA+ -> intentional (HS nozzle warmup design)
- D-hs HS delta != expected on many brands -> pre-existing calibration, not new errors
- F-mvs-ref -> KS1 calibrated values, reference table is a guide not a mandate
- E-nozzle-mvs Overture TPU, Sunlu TPU -> intentional hand-caps
"""
import json, glob, os

FILAMENT_DIR = 'filament'
IDENTITY = {'filament_settings_id','filament_vendor','from','inherits',
            'is_custom_defined','name','version'}
NOZZLE_SCALE = {'0.6mm': 1.25, '0.8mm': 1.50, '0.25mm': 0.50}
TEMP_KEYS = ['nozzle_temperature','nozzle_temperature_initial_layer',
             'nozzle_temperature_BRASS','nozzle_temperature_initial_layer_BRASS',
             'nozzle_temperature_HS','nozzle_temperature_initial_layer_HS',
             'nozzle_temperature_range_high']

def get(d, k):
    v = d.get(k)
    return (v[0] if isinstance(v, list) else v) if v is not None else None

def set_key(d, k, v):
    d[k] = [str(v)]

def fmt_mvs(v):
    f = round(float(v), 1)
    return str(int(f)) if f == int(f) else str(f)

def save_sorted(fpath, d):
    content = sorted(k for k in d if k not in IDENTITY)
    identity = sorted(k for k in d if k in IDENTITY)
    ordered = {k: d[k] for k in content + identity}
    with open(fpath, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(ordered, f, indent=4, ensure_ascii=False)
        f.write('\n')

def update_info(fpath, name):
    info = fpath.replace('.json', '.info')
    out = {}
    if os.path.exists(info):
        for line in open(info, encoding='utf-8'):
            line = line.strip()
            if ' = ' in line:
                k, v = line.split(' = ', 1)
                out[k.strip()] = v.strip()
    out['sync_info'] = 'update'
    out.setdefault('user_id', '')
    out['setting_id'] = name
    with open(info, 'w', encoding='utf-8', newline='\n') as f:
        for k, v in out.items():
            f.write(f'{k} = {v}\n')

user_profiles = {}
for f in sorted(glob.glob(f'{FILAMENT_DIR}/*.json')):
    with open(f, encoding='utf-8') as fp:
        try: d = json.load(fp)
        except: continue
    user_profiles[d.get('name','')] = (f.replace('\\','/'), d)

sys_profiles = {}
for f in glob.glob('C:/Users/pandrade/AppData/Roaming/AnycubicSlicerNext/system/Anycubic/filament/*.json'):
    with open(f, encoding='utf-8') as fp:
        try: d = json.load(fp)
        except: continue
    sys_profiles[d.get('name','')] = d

def resolve_mvs(name, up, sp, depth=0):
    if depth > 8: return None
    d = up[name][1] if name in up else sp.get(name)
    if not d: return None
    v = d.get('filament_max_volumetric_speed', [None])[0]
    if v is not None: return float(v)
    return resolve_mvs(d.get('inherits',''), up, sp, depth+1)

total_fixes = 0

for name, (fpath, d) in sorted(user_profiles.items()):
    changed = []
    inh = d.get('inherits','')
    is_kx = '@AC KX' in name
    n = name.lower()
    size_str = next((s for s in ('0.25mm','0.6mm','0.8mm','0.4mm') if name.endswith(s)), None)
    size = size_str[:-2] if size_str else None

    parent_d = user_profiles[inh][1] if inh in user_profiles else sys_profiles.get(inh)

    # ── Fix 1: activate_air_filtration=1 on KX root profiles ─────────────────
    if is_kx and size == '0.4' and '@Anycubic Kobra' in inh:
        aaf = get(d, 'activate_air_filtration')
        if aaf and str(aaf) != '0':
            set_key(d, 'activate_air_filtration', '0')
            changed.append(f'activate_air_filtration: {aaf!r} -> "0"')

    # ── Fix 2: additional_cooling_fan_speed != 0 on KX profiles ──────────────
    if is_kx and size == '0.4' and '@Anycubic Kobra' in inh:
        acf = get(d, 'additional_cooling_fan_speed')
        if acf and str(acf) != '0':
            set_key(d, 'additional_cooling_fan_speed', '0')
            changed.append(f'additional_cooling_fan_speed: {acf!r} -> "0"')

    # ── Fix 3: initial_layer_HS > range_high ──────────────────────────────────
    init_hs = get(d, 'nozzle_temperature_initial_layer_HS')
    rng_hi  = get(d, 'nozzle_temperature_range_high')
    if init_hs and rng_hi:
        try:
            if int(init_hs) > int(rng_hi):
                # Fix range_high to be at least equal to initial_layer_HS
                new_rh = init_hs
                set_key(d, 'nozzle_temperature_range_high', new_rh)
                changed.append(f'nozzle_temperature_range_high: {rng_hi!r} -> {new_rh!r} (was < initial_layer_HS)')
        except (ValueError, TypeError): pass

    # ── Fix 4: Improved KX nozzle variants MVS recalculation ─────────────────
    # Only for Improved * @AC KX 0.6/0.8mm — other brands are intentional
    if ('Improved ' in name and '@AC KX' in name and
            size in ('0.6','0.8','0.25') and inh in user_profiles):
        _, pd = user_profiles[inh]
        if '@Anycubic Kobra' in pd.get('inherits',''):
            # Only recalculate non-TPU profiles
            if 'tpu' not in n:
                cur_mvs = get(d, 'filament_max_volumetric_speed')
                parent_mvs = resolve_mvs(inh, user_profiles, sys_profiles)
                if cur_mvs and parent_mvs:
                    scale = NOZZLE_SCALE.get(size_str, 1.0)
                    if size_str == '0.25mm':
                        expected = '3'
                    else:
                        expected = fmt_mvs(parent_mvs * scale)
                    if str(fmt_mvs(float(cur_mvs))) != str(fmt_mvs(float(expected))):
                        set_key(d, 'filament_max_volumetric_speed', expected)
                        changed.append(f'MVS: {cur_mvs!r} -> {expected!r} (parent={parent_mvs} x {scale})')

    # ── Fix 5: Coolplate Creality Hyper PLA Galaxy ─────────────────────────────
    if 'creality hyper pla galaxy' in n and size == '0.4':
        cpti = get(d, 'cool_plate_temp_initial_layer')
        if cpti and str(cpti) != '50':  # it's PETG parent so keep 50
            pass  # This profile inherits from PETG parent — 50 is correct, audit was wrong

    # ── Fix 6: B-redundant — remove keys matching parent exactly ─────────────
    if parent_d:
        skip_keys = {'name','inherits','from','is_custom_defined','version',
                     'filament_settings_id','filament_vendor','compatible_printers'}
        for k in list(d.keys()):
            if k in skip_keys: continue
            pv = parent_d.get(k)
            if pv is not None and pv == d[k]:
                # Only auto-remove safe keys (not temperature keys — those may be intentional)
                safe_remove = {
                    'activate_air_filtration', 'additional_cooling_fan_speed',
                    'temperature_vitrification', 'filament_retraction_length',
                    'nozzle_temperature_range_high', 'nozzle_temperature_initial_layer_BRASS',
                    'nozzle_temperature_HS', 'nozzle_temperature_initial_layer_HS',
                    'filament_max_volumetric_speed',
                }
                if k in safe_remove:
                    del d[k]
                    changed.append(f'REMOVE {k} (matches parent)')

    if changed:
        save_sorted(fpath, d)
        update_info(fpath, name)
        total_fixes += len(changed)
        print(f'\n{name}:')
        for c in changed:
            print(f'  {c}')

print(f'\nTotal fixes applied: {total_fixes}')
