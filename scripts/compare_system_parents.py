"""
Compare KS1 vs KSX system parent profiles for each material.
Shows every field that differs between the two printers,
and every field that is the same.
This drives how KSX Improved profiles should differ from KS1 Improved profiles.
"""
import json, glob

SYS = 'C:/Users/pandrade/AppData/Roaming/AnycubicSlicerNext/system/Anycubic/filament'

# Map material -> (ks1_parent_name, ksx_parent_name)
PAIRS = {
    'PLA': (
        'Anycubic PLA @Anycubic Kobra S1 0.4 nozzle',
        'Anycubic PLA @Anycubic Kobra X 0.4 nozzle',
    ),
    'PLA+': (
        'Anycubic PLA+ @Anycubic Kobra S1 0.4 nozzle',
        'Anycubic PLA+ @Anycubic Kobra X 0.4 nozzle',
    ),
    'PETG': (
        'Anycubic PETG @Anycubic Kobra S1 0.4 nozzle',
        'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
    ),
}

# Load all system profiles
sys_profiles = {}
for f in glob.glob(f'{SYS}/*.json'):
    with open(f, encoding='utf-8') as fp:
        try:
            d = json.load(fp)
        except Exception:
            continue
    sys_profiles[d.get('name', '')] = d


def resolve(name, key, depth=0):
    """Resolve a key through the inheritance chain."""
    if depth > 6:
        return None
    d = sys_profiles.get(name)
    if not d:
        return None
    v = d.get(key)
    if v is not None:
        return v[0] if isinstance(v, list) else v
    return resolve(d.get('inherits', ''), key, depth + 1)


def all_keys_for_pair(ks1_name, ksx_name):
    """Collect all keys present in either profile (including inherited)."""
    keys = set()
    for name in (ks1_name, ksx_name):
        d = sys_profiles.get(name, {})
        keys.update(d.keys())
    # Filter to meaningful settings (skip meta/identity)
    skip = {'type','from','setting_id','filament_id','is_custom_defined','instantiation',
            'name','inherits','version','filament_settings_id','filament_vendor',
            'filament_type','compatible_printers','compatible_printers_condition',
            'compatible_prints','compatible_prints_condition','default_filament_colour',
            'filament_diameter','filament_notes','filament_shrink','filament_shrinkage_compensation_z',
            'filament_soluble','filament_is_support','filament_ramming_parameters',
            'adaptive_pressure_advance','adaptive_pressure_advance_bridges',
            'adaptive_pressure_advance_model','adaptive_pressure_advance_overhangs',
            'filament_multitool_ramming','filament_multitool_ramming_flow',
            'filament_multitool_ramming_volume','filament_toolchange_delay',
            'filament_loading_speed','filament_loading_speed_start',
            'filament_unloading_speed','filament_unloading_speed_start',
            'filament_cooling_final_speed','filament_cooling_initial_speed',
            'filament_cooling_moves','filament_stamping_distance',
            'filament_stamping_loading_speed','filament_long_retractions_when_cut',
            'filament_retraction_distances_when_cut',
            'pellet_flow_coefficient','filament_adhesiveness_category',
            }
    return sorted(k for k in keys if k not in skip)


print('=' * 110)
print('SYSTEM PARENT COMPARISON: KS1 vs KSX')
print('Shows every field. DIFF marks where values differ between printers.')
print('=' * 110)

for material, (ks1_name, ksx_name) in PAIRS.items():
    ks1_d = sys_profiles.get(ks1_name, {})
    ksx_d = sys_profiles.get(ksx_name, {})

    print(f'\n{"=" * 110}')
    print(f'  MATERIAL: {material}')
    print(f'  KS1 parent: {ks1_name}  (inherits: {ks1_d.get("inherits","")})')
    print(f'  KSX parent: {ksx_name}  (inherits: {ksx_d.get("inherits","")})')
    print(f'\n  {"Key":<50} {"KS1 (explicit)":>18} {"KSX (explicit)":>18}  {"Resolved KS1":>14} {"Resolved KSX":>14}  {"STATUS"}')
    print(f'  {"-" * 105}')

    keys = all_keys_for_pair(ks1_name, ksx_name)

    same = []
    different = []
    for k in keys:
        ks1_exp = ks1_d.get(k)
        ksx_exp = ksx_d.get(k)
        ks1_v = ks1_exp[0] if isinstance(ks1_exp, list) else ks1_exp
        ksx_v = ksx_exp[0] if isinstance(ksx_exp, list) else ksx_exp
        ks1_r = resolve(ks1_name, k)
        ksx_r = resolve(ksx_name, k)
        ks1_exp_s = str(ks1_v) if ks1_v is not None else '-'
        ksx_exp_s = str(ksx_v) if ksx_v is not None else '-'
        ks1_r_s = str(ks1_r) if ks1_r is not None else '-'
        ksx_r_s = str(ksx_r) if ksx_r is not None else '-'

        if ks1_r_s != ksx_r_s:
            different.append((k, ks1_exp_s, ksx_exp_s, ks1_r_s, ksx_r_s))
        else:
            same.append((k, ks1_exp_s, ksx_exp_s, ks1_r_s, ksx_r_s))

    print(f'\n  --- DIFFERENCES ({len(different)}) ---')
    for k, e1, e2, r1, r2 in different:
        print(f'  {k:<50} {e1:>18} {e2:>18}  {r1:>14} {r2:>14}  DIFF')

    print(f'\n  --- SAME ({len(same)}) ---')
    for k, e1, e2, r1, r2 in same:
        print(f'  {k:<50} {e1:>18} {e2:>18}  {r1:>14} {r2:>14}')
