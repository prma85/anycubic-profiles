"""
Check and correct Improved KX 0.4mm temperature values.

Method:
  For each temperature key:
    1. Get the KS1 calibrated value (explicit in Improved KS1 profile)
    2. Get the KS1 calibrated base temp (nozzle_temperature)
    3. delta_from_base = ks1_cal - ks1_base  (the intended offset)
    4. Apply to KX base temp: expected_kx = kx_base + delta_from_base

  Additionally apply system-level delta where both systems have numeric values:
    sys_delta = kx_sys - ks1_sys  (only when neither is nil)
    expected_kx = ks1_cal + sys_delta  (for plate temps, range, etc.)

  For keys where KS1 sys is nil (BRASS/HS keys on KS1):
    Use delta_from_base approach.
  For keys where both systems have values:
    Use absolute system delta approach.

  range_high: apply -10 system delta (KX sys range_high = KS1 sys range_high - 10 consistently)
"""
import json, glob, os

SYS = 'C:/Users/pandrade/AppData/Roaming/AnycubicSlicerNext/system/Anycubic/filament'
sp = {}
for f in glob.glob(f'{SYS}/*.json'):
    with open(f, encoding='utf-8') as fp:
        try:
            d = json.load(fp)
        except Exception:
            continue
    sp[d.get('name', '')] = d

user_profiles = {}
for f in sorted(glob.glob('filament/*.json')):
    with open(f, encoding='utf-8') as fp:
        try:
            d = json.load(fp)
        except Exception:
            continue
    user_profiles[d.get('name', '')] = (f.replace('\\', '/'), d)


def resolve_sys(name, key, depth=0):
    if depth > 6:
        return None
    d = sp.get(name)
    if not d:
        return None
    v = d.get(key)
    if v is not None:
        return v[0] if isinstance(v, list) else v
    return resolve_sys(d.get('inherits', ''), key, depth + 1)


TEMP_KEYS = [
    'nozzle_temperature',
    'nozzle_temperature_initial_layer',
    'nozzle_temperature_BRASS',
    'nozzle_temperature_initial_layer_BRASS',
    'nozzle_temperature_HS',
    'nozzle_temperature_initial_layer_HS',
    'nozzle_temperature_range_high',
]
IDENTITY = {'filament_settings_id','filament_vendor','from','inherits',
            'is_custom_defined','name','version'}

MATERIAL_MAP = {
    'Improved PLA @AC KX 0.4mm': (
        'Improved PLA @AC KS1 0.4mm',
        'Anycubic PLA @Anycubic Kobra S1 0.4 nozzle',
        'Anycubic PLA @Anycubic Kobra X 0.4 nozzle',
    ),
    'Improved PLA+ @AC KX 0.4mm': (
        'Improved PLA+ @AC KS1 0.4mm',
        'Anycubic PLA+ @Anycubic Kobra S1 0.4 nozzle',
        'Anycubic PLA+ @Anycubic Kobra X 0.4 nozzle',
    ),
    'Improved PETG @AC KX 0.4mm': (
        'Improved PETG @AC KS1 0.4mm',
        'Anycubic PETG @Anycubic Kobra S1 0.4 nozzle',
        'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
    ),
    'Improved PETG HS @AC KX 0.4mm': (
        'Improved PETG HS @AC KS1 0.4mm',
        'Anycubic PETG @Anycubic Kobra S1 0.4 nozzle',
        'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
    ),
    'Improved PETG Translucent @AC KX 0.4mm': (
        'Improved PETG Translucent @AC KS1 0.4mm',
        'Anycubic PETG @Anycubic Kobra S1 0.4 nozzle',
        'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
    ),
}


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


all_corrections = {}

for kx_name, (ks1_name, ks1_sys_name, kx_sys_name) in MATERIAL_MAP.items():
    _, ks1_d = user_profiles[ks1_name]
    fpath, kx_d = user_profiles[kx_name]

    # Get calibrated base temps from KS1
    ks1_base = ks1_d.get('nozzle_temperature', [None])[0]
    kx_base  = kx_d.get('nozzle_temperature', [None])[0]
    if ks1_base is None:
        # KS1 inherits base — get from system parent
        ks1_base = resolve_sys(ks1_sys_name, 'nozzle_temperature')
    if kx_base is None:
        kx_base = resolve_sys(kx_sys_name, 'nozzle_temperature')

    corrections = {}

    print(f'\n{"=" * 100}')
    print(f'  {kx_name}  (KS1 base={ks1_base}, KX base={kx_base})')
    print(f'  {"Key":<45} {"KS1-cal":>8} {"KS1-base-delta":>15} {"Expected KX":>12} {"Current KX":>12}  Status')
    print(f'  {"-" * 95}')

    for k in TEMP_KEYS:
        ks1_cal   = ks1_d.get(k, [None])[0]
        ks1_sys_v = resolve_sys(ks1_sys_name, k)
        kx_sys_v  = resolve_sys(kx_sys_name, k)
        kx_cur    = kx_d.get(k, [None])[0]

        if ks1_cal is None:
            continue  # KS1 doesn't have it explicitly — skip (will inherit)

        try:
            ks1_base_int = int(ks1_base)
            ks1_cal_int  = int(ks1_cal)
            kx_base_int  = int(kx_base)
        except (TypeError, ValueError):
            continue

        # Compute expected KX value:
        # Case 1: Both sys parents have numeric values for this key
        #         Use absolute delta: expected = ks1_cal + (kx_sys - ks1_sys)
        # Case 2: KS1 sys is nil (key doesn't exist in KS1 sys)
        #         Use delta-from-base: expected = kx_base + (ks1_cal - ks1_base)
        # Case 3: range_high — use absolute sys delta (-10 consistently)

        if ks1_sys_v is not None and kx_sys_v is not None:
            try:
                sys_delta = int(kx_sys_v) - int(ks1_sys_v)
                expected = str(ks1_cal_int + sys_delta)
                method = f'sys_delta={sys_delta:+d}'
            except (TypeError, ValueError):
                expected = ks1_cal
                method = 'copy'
        else:
            # KS1 sys nil — use delta from base
            delta_from_base = ks1_cal_int - ks1_base_int
            expected = str(kx_base_int + delta_from_base)
            method = f'base+{delta_from_base:+d}'

        cur_str = str(kx_cur) if kx_cur else '(inherited)'
        if str(kx_cur) == expected:
            status = 'OK'
        elif kx_cur is None:
            # Currently inherited — check if inherited value == expected
            # Resolve what KX would inherit
            inherited_v = resolve_sys(kx_sys_name, k)
            if str(inherited_v) == expected:
                status = f'OK (inherited={inherited_v})'
            else:
                status = f'NEEDS SET -> {expected}'
                corrections[k] = expected
        else:
            status = f'WRONG -> {expected}'
            corrections[k] = expected

        print(f'  {k:<45} {str(ks1_cal):>8} {method:>15} {str(expected):>12} {cur_str:>12}  {status}')

    if corrections:
        all_corrections[kx_name] = (fpath, kx_d, corrections)
        print(f'\n  -> {len(corrections)} corrections needed')

# Apply corrections
if all_corrections:
    print(f'\n\n{"=" * 60}')
    print('Applying corrections...')
    for kx_name, (fpath, d, corrections) in all_corrections.items():
        print(f'\n  {kx_name}:')
        for k, v in corrections.items():
            old = d.get(k, [None])[0]
            d[k] = [v]
            print(f'    {k}: {old!r} -> {v!r}')
        save_sorted(fpath, d)
        update_info(fpath, kx_name)
    print('\nDone.')
else:
    print('\n\nAll values correct — no changes needed.')
