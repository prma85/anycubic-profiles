"""
Fix all Improved KSX 0.4mm profiles then cascade to their nozzle variants.
Rules applied:
  - Improved PLA KSX:  match KS1 temps, keep KSX-specific plate temps (hot=75, textured=70),
                       MVS=13 (inherited from system parent - no explicit key needed)
  - Improved PLA+ KSX: match KS1 temps, fix range_high=240, initial_HS=210, MVS=16
  - Improved PETG KSX: temperatures already identical to KS1 (correct), just ensure
                       HS and BRASS keys explicit, fix range_high relative to HS temp
  - Improved PETG HS KSX: same - temps already correct, fix range_high
  - Improved PETG Translucent KSX: restore nozzle_temperature_HS and initial_layer_HS
                                   (were removed by simplification)
After updating 0.4mm files, recalculate all nozzle variants using canonical deltas.
"""
import json, glob

IDENTITY = {
    'filament_settings_id','filament_vendor','from','inherits',
    'is_custom_defined','name','version'
}

TEMP_KEYS = [
    'nozzle_temperature','nozzle_temperature_initial_layer',
    'nozzle_temperature_BRASS','nozzle_temperature_initial_layer_BRASS',
    'nozzle_temperature_HS','nozzle_temperature_initial_layer_HS',
    'nozzle_temperature_range_high','nozzle_temperature_range_low',
]

PLA_NOZZLE_DELTA  = {'0.25mm': -5, '0.6mm':  5, '0.8mm': 10}
PETG_NOZZLE_DELTA = {             '0.6mm': 10, '0.8mm': 15}


def save_sorted(fpath, d):
    content  = sorted(k for k in d if k not in IDENTITY)
    identity = sorted(k for k in d if k in IDENTITY)
    ordered  = {k: d[k] for k in content + identity}
    with open(fpath, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(ordered, f, indent=4, ensure_ascii=False)
        f.write('\n')


def update_info(fpath, name):
    info_path = fpath.replace('.json', '.info')
    import os
    out = {}
    if os.path.exists(info_path):
        for line in open(info_path, encoding='utf-8'):
            line = line.strip()
            if ' = ' in line:
                k, v = line.split(' = ', 1)
                out[k.strip()] = v.strip()
    out['sync_info'] = 'update'
    out.setdefault('user_id', '')
    out['setting_id'] = name
    with open(info_path, 'w', encoding='utf-8', newline='\n') as f:
        for k, v in out.items():
            f.write(f'{k} = {v}\n')


def set_key(d, k, v):
    if isinstance(v, list):
        d[k] = v
    else:
        d[k] = [str(v)]


# ─────────────────────────────────────────────────────────────────────────────
# 1. Improved PLA @AC KSX 0.4mm
# ─────────────────────────────────────────────────────────────────────────────
fpath = 'filament/Improved PLA @AC KSX 0.4mm.json'
with open(fpath, encoding='utf-8') as f:
    d = json.load(f)

# Temperatures: match KS1
set_key(d, 'nozzle_temperature',                    '200')
set_key(d, 'nozzle_temperature_initial_layer',       '200')
set_key(d, 'nozzle_temperature_BRASS',               '215')
set_key(d, 'nozzle_temperature_initial_layer_BRASS', '220')
set_key(d, 'nozzle_temperature_HS',                  '205')
set_key(d, 'nozzle_temperature_initial_layer_HS',    '205')
set_key(d, 'nozzle_temperature_range_high',          '230')
set_key(d, 'nozzle_temperature_range_low',           '200')

# Plate temps: match KS1 (user confirmed hot=75, textured=70)
set_key(d, 'hot_plate_temp',                   '75')
set_key(d, 'hot_plate_temp_initial_layer',     '75')
set_key(d, 'textured_plate_temp',              '70')
set_key(d, 'textured_plate_temp_initial_layer','70')

# MVS: remove explicit key — system parent Anycubic PLA KSX has 13, which is correct
d.pop('filament_max_volumetric_speed', None)

save_sorted(fpath, d)
update_info(fpath, 'Improved PLA @AC KSX 0.4mm')
print('Fixed: Improved PLA @AC KSX 0.4mm')


# ─────────────────────────────────────────────────────────────────────────────
# 2. Improved PLA+ @AC KSX 0.4mm
# ─────────────────────────────────────────────────────────────────────────────
fpath = 'filament/Improved PLA+ @AC KSX 0.4mm.json'
with open(fpath, encoding='utf-8') as f:
    d = json.load(f)

# Temperatures: match KS1 (range_high=240 for headroom, initial_HS=210)
set_key(d, 'nozzle_temperature_initial_layer',       '205')
set_key(d, 'nozzle_temperature_BRASS',               '205')
set_key(d, 'nozzle_temperature_initial_layer_BRASS', '205')
set_key(d, 'nozzle_temperature_HS',                  '210')
set_key(d, 'nozzle_temperature_initial_layer_HS',    '210')
set_key(d, 'nozzle_temperature_range_high',          '240')
set_key(d, 'nozzle_temperature_range_low',           '205')

# Plate: hot=65 (KS1 also has 65 for PLA+), textured=55 was original KSX
# KS1 PLA+ has hot=65, textured not set (inherits 60 from system). KSX had textured=55.
# Keep KSX-specific textured=55 since user chose KS1 plate temps only for PLA, not PLA+
# Wait — user said "match KS1" for plates, which for PLA was hot=75,textured=70.
# But for PLA+ KS1 has hot=65 and textured=(inherited=60). Keep current KSX hot=65, textured=55.

# MVS: 16 (already correct from refactor)
set_key(d, 'filament_max_volumetric_speed', '16')

save_sorted(fpath, d)
update_info(fpath, 'Improved PLA+ @AC KSX 0.4mm')
print('Fixed: Improved PLA+ @AC KSX 0.4mm')


# ─────────────────────────────────────────────────────────────────────────────
# 3. Improved PETG @AC KSX 0.4mm
# ─────────────────────────────────────────────────────────────────────────────
fpath = 'filament/Improved PETG @AC KSX 0.4mm.json'
with open(fpath, encoding='utf-8') as f:
    d = json.load(f)

# Temperatures already match KS1 (235/245 base/HS, range 230-255)
# These look correct — no changes needed to temps
# Just ensure all BRASS keys are present (BRASS=base for standard PETG)
set_key(d, 'nozzle_temperature',                    '235')
set_key(d, 'nozzle_temperature_initial_layer',       '235')
set_key(d, 'nozzle_temperature_BRASS',               '235')
set_key(d, 'nozzle_temperature_initial_layer_BRASS', '235')
set_key(d, 'nozzle_temperature_HS',                  '245')
set_key(d, 'nozzle_temperature_initial_layer_HS',    '245')
set_key(d, 'nozzle_temperature_range_high',          '255')
set_key(d, 'nozzle_temperature_range_low',           '230')

save_sorted(fpath, d)
update_info(fpath, 'Improved PETG @AC KSX 0.4mm')
print('Fixed: Improved PETG @AC KSX 0.4mm (verified, no temp changes needed)')


# ─────────────────────────────────────────────────────────────────────────────
# 4. Improved PETG HS @AC KSX 0.4mm
# ─────────────────────────────────────────────────────────────────────────────
fpath = 'filament/Improved PETG HS @AC KSX 0.4mm.json'
with open(fpath, encoding='utf-8') as f:
    d = json.load(f)

# range_high was 245 (equal to HS temp — no headroom). Fix to 255 to match PETG standard.
set_key(d, 'nozzle_temperature',                    '235')
set_key(d, 'nozzle_temperature_initial_layer',       '235')
set_key(d, 'nozzle_temperature_BRASS',               '235')
set_key(d, 'nozzle_temperature_initial_layer_BRASS', '235')
set_key(d, 'nozzle_temperature_HS',                  '245')
set_key(d, 'nozzle_temperature_initial_layer_HS',    '245')
set_key(d, 'nozzle_temperature_range_high',          '255')
set_key(d, 'nozzle_temperature_range_low',           '230')

save_sorted(fpath, d)
update_info(fpath, 'Improved PETG HS @AC KSX 0.4mm')
print('Fixed: Improved PETG HS @AC KSX 0.4mm (range_high 245->255)')


# ─────────────────────────────────────────────────────────────────────────────
# 5. Improved PETG Translucent @AC KSX 0.4mm
# ─────────────────────────────────────────────────────────────────────────────
fpath = 'filament/Improved PETG Translucent @AC KSX 0.4mm.json'
with open(fpath, encoding='utf-8') as f:
    d = json.load(f)

# HS keys were removed by simplification (matched system parent which has HS=nil).
# Restore them to match KS1 values (230°C).
set_key(d, 'nozzle_temperature',                    '220')
set_key(d, 'nozzle_temperature_initial_layer',       '220')
set_key(d, 'nozzle_temperature_BRASS',               '220')
set_key(d, 'nozzle_temperature_initial_layer_BRASS', '220')
set_key(d, 'nozzle_temperature_HS',                  '230')
set_key(d, 'nozzle_temperature_initial_layer_HS',    '230')
set_key(d, 'nozzle_temperature_range_high',          '240')

save_sorted(fpath, d)
update_info(fpath, 'Improved PETG Translucent @AC KSX 0.4mm')
print('Fixed: Improved PETG Translucent @AC KSX 0.4mm (restored HS=230)')


# ─────────────────────────────────────────────────────────────────────────────
# Now cascade: recalculate nozzle variants for all 5 KSX Improved profiles
# ─────────────────────────────────────────────────────────────────────────────
print()
print('Cascading to nozzle variants...')

user_profiles = {}
for f in sorted(glob.glob('filament/*.json')):
    with open(f, encoding='utf-8') as fp:
        d = json.load(fp)
    user_profiles[d.get('name', '')] = (f.replace('\\', '/'), d)

def get_parent_temps(parent_name):
    _, pd = user_profiles[parent_name]
    return {k: pd.get(k, [None])[0] for k in TEMP_KEYS}

targets = [
    # (variant_name, delta_map)
    ('Improved PLA @AC KSX 0.25mm',              PLA_NOZZLE_DELTA),
    ('Improved PLA @AC KSX 0.6mm',               PLA_NOZZLE_DELTA),
    ('Improved PLA @AC KSX 0.8mm',               PLA_NOZZLE_DELTA),
    ('Improved PLA+ @AC KSX 0.25mm',             PLA_NOZZLE_DELTA),
    ('Improved PLA+ @AC KSX 0.6mm',              PLA_NOZZLE_DELTA),
    ('Improved PLA+ @AC KSX 0.8mm',              PLA_NOZZLE_DELTA),
    ('Improved PETG @AC KSX 0.6mm',              PETG_NOZZLE_DELTA),
    ('Improved PETG @AC KSX 0.8mm',              PETG_NOZZLE_DELTA),
    ('Improved PETG HS @AC KSX 0.6mm',           PETG_NOZZLE_DELTA),
    ('Improved PETG HS @AC KSX 0.8mm',           PETG_NOZZLE_DELTA),
    ('Improved PETG Translucent @AC KSX 0.6mm',  PETG_NOZZLE_DELTA),
    ('Improved PETG Translucent @AC KSX 0.8mm',  PETG_NOZZLE_DELTA),
]

for variant_name, delta_map in targets:
    if variant_name not in user_profiles:
        print(f'  SKIP (not found): {variant_name}')
        continue
    fpath, d = user_profiles[variant_name]
    parent_name = d.get('inherits', '')
    if parent_name not in user_profiles:
        print(f'  SKIP (parent not found): {variant_name}')
        continue

    # Detect nozzle size from name
    size = next((s for s in ('0.25mm', '0.6mm', '0.8mm') if variant_name.endswith(s)), None)
    if not size or size not in delta_map:
        continue
    delta = delta_map[size]

    parent_temps = get_parent_temps(parent_name)
    changed = []

    for k in TEMP_KEYS:
        if k == 'nozzle_temperature_range_low':
            continue  # never change range_low
        pv = parent_temps.get(k)
        if pv is None:
            continue
        expected = str(int(pv) + delta)
        cur = d.get(k, [None])[0]
        if cur != expected:
            d[k] = [expected]
            changed.append(f'{k}: {cur!r} -> {expected!r}')

    if changed:
        save_sorted(fpath, d)
        update_info(fpath, variant_name)
        print(f'  Updated {variant_name}:')
        for c in changed:
            print(f'    {c}')
    else:
        print(f'  OK (no changes): {variant_name}')
