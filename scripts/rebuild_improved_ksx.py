"""
Rebuild all Improved KSX 0.4mm profiles by taking the KS1 Improved values
and applying the deltas derived from the system parent comparison.

Method:
  For each key K in Improved KS1:
    ksx_improved[K] = ks1_improved[K] + (ksx_sys[K] - ks1_sys[K])
    i.e. if KSX system sets fan_min_speed 20pp lower than KS1 system,
    then KSX Improved sets fan_min_speed 20pp lower than KS1 Improved.

Keys that only exist in one system parent are applied as-is from the KSX system.
After building 0.4mm, cascade to nozzle variants using the standard delta tables.
"""
import json, glob

SYS = 'C:/Users/pandrade/AppData/Roaming/AnycubicSlicerNext/system/Anycubic/filament'
FILAMENT_DIR = 'filament'

IDENTITY = {
    'filament_settings_id','filament_vendor','from','inherits',
    'is_custom_defined','name','version',
}

# Keys we never copy from KS1 to KSX (printer-hardware-specific, always from KSX system)
HARDWARE_ONLY = {
    'activate_air_filtration',  # KSX=0 always (no filtration hardware)
    'additional_cooling_fan_speed',  # KSX=0 always (no aux fan)
}

# Temperature delta tables for nozzle variants (relative to 0.4mm of same printer)
PLA_NOZZLE_DELTA  = {'0.25mm': -5, '0.6mm':  5, '0.8mm': 10}
PETG_NOZZLE_DELTA = {             '0.6mm': 10, '0.8mm': 15}
TEMP_KEYS = [
    'nozzle_temperature', 'nozzle_temperature_initial_layer',
    'nozzle_temperature_BRASS', 'nozzle_temperature_initial_layer_BRASS',
    'nozzle_temperature_HS', 'nozzle_temperature_initial_layer_HS',
    'nozzle_temperature_range_high',
]


# ── helpers ───────────────────────────────────────────────────────────────────
def load_all_system():
    sp = {}
    for f in glob.glob(f'{SYS}/*.json'):
        with open(f, encoding='utf-8') as fp:
            try: d = json.load(fp)
            except: continue
        sp[d.get('name', '')] = d
    return sp

def load_all_user():
    up = {}
    for f in sorted(glob.glob(f'{FILAMENT_DIR}/*.json')):
        with open(f, encoding='utf-8') as fp:
            try: d = json.load(fp)
            except: continue
        up[d.get('name', '')] = (f.replace('\\', '/'), d)
    return up

def resolve_sys(name, key, sp, depth=0):
    if depth > 8: return None
    d = sp.get(name)
    if not d: return None
    v = d.get(key)
    if v is not None: return v[0] if isinstance(v, list) else v
    return resolve_sys(d.get('inherits', ''), key, sp, depth + 1)

def is_numeric(v):
    if v is None: return False
    try: float(str(v).rstrip('%')); return True
    except: return False

def apply_delta(ks1_val, delta):
    """Add numeric delta to a value (handles int and float)."""
    try:
        f1 = float(str(ks1_val).rstrip('%'))
        result = f1 + delta
        # Keep as int if both operands produced integer result
        if result == int(result):
            return str(int(result))
        return str(round(result, 4))
    except:
        return str(ks1_val)

def save_sorted(fpath, d):
    content  = sorted(k for k in d if k not in IDENTITY)
    identity = sorted(k for k in d if k in IDENTITY)
    ordered  = {k: d[k] for k in content + identity}
    with open(fpath, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(ordered, f, indent=4, ensure_ascii=False)
        f.write('\n')

def update_info(fpath, name):
    import os
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


# ── main logic ────────────────────────────────────────────────────────────────
SP = load_all_system()
UP = load_all_user()

MATERIALS = {
    'PLA': {
        'ks1_improved': 'Improved PLA @AC KS1 0.4mm',
        'ksx_improved': 'Improved PLA @AC KSX 0.4mm',
        'ks1_sys':      'Anycubic PLA @Anycubic Kobra S1 0.4 nozzle',
        'ksx_sys':      'Anycubic PLA @Anycubic Kobra X 0.4 nozzle',
        'ksx_inherits': 'Anycubic PLA @Anycubic Kobra X 0.4 nozzle',
        'nozzle_delta': PLA_NOZZLE_DELTA,
        'variants': [
            'Improved PLA @AC KSX 0.25mm',
            'Improved PLA @AC KSX 0.6mm',
            'Improved PLA @AC KSX 0.8mm',
        ],
    },
    'PLA+': {
        'ks1_improved': 'Improved PLA+ @AC KS1 0.4mm',
        'ksx_improved': 'Improved PLA+ @AC KSX 0.4mm',
        'ks1_sys':      'Anycubic PLA+ @Anycubic Kobra S1 0.4 nozzle',
        'ksx_sys':      'Anycubic PLA+ @Anycubic Kobra X 0.4 nozzle',
        'ksx_inherits': 'Anycubic PLA+ @Anycubic Kobra X 0.4 nozzle',
        'nozzle_delta': PLA_NOZZLE_DELTA,
        'variants': [
            'Improved PLA+ @AC KSX 0.25mm',
            'Improved PLA+ @AC KSX 0.6mm',
            'Improved PLA+ @AC KSX 0.8mm',
        ],
    },
    'PETG': {
        'ks1_improved': 'Improved PETG @AC KS1 0.4mm',
        'ksx_improved': 'Improved PETG @AC KSX 0.4mm',
        'ks1_sys':      'Anycubic PETG @Anycubic Kobra S1 0.4 nozzle',
        'ksx_sys':      'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
        'ksx_inherits': 'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
        'nozzle_delta': PETG_NOZZLE_DELTA,
        'variants': [
            'Improved PETG @AC KSX 0.6mm',
            'Improved PETG @AC KSX 0.8mm',
        ],
    },
    'PETG HS': {
        'ks1_improved': 'Improved PETG HS @AC KS1 0.4mm',
        'ksx_improved': 'Improved PETG HS @AC KSX 0.4mm',
        'ks1_sys':      'Anycubic PETG @Anycubic Kobra S1 0.4 nozzle',
        'ksx_sys':      'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
        'ksx_inherits': 'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
        'nozzle_delta': PETG_NOZZLE_DELTA,
        'variants': [
            'Improved PETG HS @AC KSX 0.6mm',
            'Improved PETG HS @AC KSX 0.8mm',
        ],
    },
    'PETG Translucent': {
        'ks1_improved': 'Improved PETG Translucent @AC KS1 0.4mm',
        'ksx_improved': 'Improved PETG Translucent @AC KSX 0.4mm',
        'ks1_sys':      'Anycubic PETG @Anycubic Kobra S1 0.4 nozzle',
        'ksx_sys':      'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
        'ksx_inherits': 'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
        'nozzle_delta': PETG_NOZZLE_DELTA,
        'variants': [
            'Improved PETG Translucent @AC KSX 0.6mm',
            'Improved PETG Translucent @AC KSX 0.8mm',
        ],
    },
}

SKIP_KEYS = IDENTITY | {
    'type','setting_id','filament_id','instantiation','filament_type','bed_type',
    'compatible_printers',
}

for mat, cfg in MATERIALS.items():
    print(f'\n{"=" * 70}')
    print(f'  Building: {cfg["ksx_improved"]}')

    _, ks1_imp = UP[cfg['ks1_improved']]
    ksx_fpath, ksx_imp = UP[cfg['ksx_improved']]

    # Collect all content keys from KS1 Improved
    all_keys = set(k for k in ks1_imp if k not in SKIP_KEYS)
    # Also include any keys currently in KSX Improved that aren't in KS1
    all_keys |= set(k for k in ksx_imp if k not in SKIP_KEYS)

    new_ksx = {}

    for k in all_keys:
        # Hardware-only: always take from KSX system (not KS1)
        if k in HARDWARE_ONLY:
            ksx_sys_val = resolve_sys(cfg['ksx_sys'], k, SP)
            if ksx_sys_val is not None:
                new_ksx[k] = [str(ksx_sys_val)]
                print(f'  HARDWARE {k}: {ksx_sys_val}')
            continue

        ks1_val = ks1_imp.get(k, [None])[0] if ks1_imp.get(k) else None
        if ks1_val is None:
            # Key not in KS1 Improved — skip (don't carry KSX-only quirks forward)
            continue

        # Compute delta from system parents
        ks1_sys_val = resolve_sys(cfg['ks1_sys'], k, SP)
        ksx_sys_val = resolve_sys(cfg['ksx_sys'], k, SP)

        if ks1_sys_val is None and ksx_sys_val is None:
            # No system reference — copy KS1 value directly
            new_ksx[k] = [str(ks1_val)]
        elif is_numeric(ks1_sys_val) and is_numeric(ksx_sys_val):
            delta = float(str(ksx_sys_val).rstrip('%')) - float(str(ks1_sys_val).rstrip('%'))
            if delta == 0:
                new_ksx[k] = [str(ks1_val)]
            else:
                new_val = apply_delta(ks1_val, delta)
                new_ksx[k] = [new_val]
                print(f'  DELTA {k}: {ks1_val} + {delta:+g} = {new_val}  '
                      f'(sys: {ks1_sys_val} -> {ksx_sys_val})')
        else:
            # Non-numeric or one side is nil — check if KSX sys has a different value
            if ksx_sys_val is not None and str(ksx_sys_val) != str(ks1_sys_val or ''):
                # KSX system overrides this key differently — apply KSX system value
                # but keep the KS1 Improved intent by using ksx_sys as reference
                new_ksx[k] = [str(ksx_sys_val)]
                print(f'  SYS_OVERRIDE {k}: {ks1_val} -> {ksx_sys_val}  '
                      f'(ks1_sys={ks1_sys_val})')
            else:
                # Same in both sys, or only KS1 sys has it — copy KS1 Improved
                new_ksx[k] = [str(ks1_val)]

    # Identity fields
    new_ksx['filament_settings_id'] = [cfg['ksx_improved']]
    new_ksx['filament_vendor']      = ksx_imp.get('filament_vendor', ['Generic'])
    new_ksx['from']                 = 'User'
    new_ksx['inherits']             = cfg['ksx_inherits']
    new_ksx['is_custom_defined']    = '0'
    new_ksx['name']                 = cfg['ksx_improved']
    new_ksx['version']              = ksx_imp.get('version', '1.3.2602.11')

    save_sorted(ksx_fpath, new_ksx)
    update_info(ksx_fpath, cfg['ksx_improved'])
    print(f'  -> Written: {ksx_fpath}')

    # ── Cascade to nozzle variants ────────────────────────────────────────────
    # Reload updated 0.4mm
    with open(ksx_fpath, encoding='utf-8') as f:
        parent_d = json.load(f)

    for variant_name in cfg['variants']:
        if variant_name not in UP:
            print(f'    SKIP variant (not found): {variant_name}')
            continue
        v_fpath, v_d = UP[variant_name]
        size = next((s for s in ('0.25mm','0.6mm','0.8mm') if variant_name.endswith(s)), None)
        delta_map = cfg['nozzle_delta']
        if not size or size not in delta_map:
            continue
        delta = delta_map[size]
        changed = []
        for tk in TEMP_KEYS:
            pv = parent_d.get(tk, [None])[0]
            if pv is None: continue
            expected = str(int(pv) + delta)
            cur = v_d.get(tk, [None])[0]
            if cur != expected:
                v_d[tk] = [expected]
                changed.append(f'{tk}: {cur!r} -> {expected!r}')
        if changed:
            save_sorted(v_fpath, v_d)
            update_info(v_fpath, variant_name)
            print(f'    Updated variant {variant_name}: {len(changed)} temp keys')
            for c in changed: print(f'      {c}')
        else:
            print(f'    OK (no changes): {variant_name}')

print('\nDone.')
