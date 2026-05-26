"""
Shows ONLY the differences between KS1 and KSX system parents.
Also shows what delta should be applied when copying KS1 Improved -> KSX Improved.
"""
import json, glob

SYS = 'C:/Users/pandrade/AppData/Roaming/AnycubicSlicerNext/system/Anycubic/filament'

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

sys_profiles = {}
for f in glob.glob(f'{SYS}/*.json'):
    with open(f, encoding='utf-8') as fp:
        try: d = json.load(fp)
        except: continue
    sys_profiles[d.get('name', '')] = d


def resolve(name, key, depth=0):
    if depth > 6: return None
    d = sys_profiles.get(name)
    if not d: return None
    v = d.get(key)
    if v is not None: return v[0] if isinstance(v, list) else v
    return resolve(d.get('inherits', ''), key, depth + 1)


SKIP = {
    'type','from','setting_id','filament_id','is_custom_defined','instantiation',
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
    'filament_retraction_distances_when_cut','pellet_flow_coefficient',
    'filament_adhesiveness_category',
}


for material, (ks1_name, ksx_name) in PAIRS.items():
    ks1_d = sys_profiles.get(ks1_name, {})
    ksx_d = sys_profiles.get(ksx_name, {})

    keys = sorted(set(list(ks1_d.keys()) + list(ksx_d.keys())) - SKIP)

    diffs = []
    for k in keys:
        ks1_r = resolve(ks1_name, k)
        ksx_r = resolve(ksx_name, k)
        ks1_s = str(ks1_r) if ks1_r is not None else 'nil'
        ksx_s = str(ksx_r) if ksx_r is not None else 'nil'
        if ks1_s != ksx_s:
            # Try to compute numeric delta
            try:
                delta = float(ksx_r) - float(ks1_r)
                delta_s = f'{"+" if delta >= 0 else ""}{delta:g}'
            except (TypeError, ValueError):
                delta_s = 'non-numeric'
            diffs.append((k, ks1_s, ksx_s, delta_s))

    print(f'\n{"=" * 90}')
    print(f'  {material}   ({len(diffs)} differences)')
    print(f'  KS1: {ks1_name}')
    print(f'  KSX: {ksx_name}')
    print(f'\n  {"Key":<55} {"KS1 resolved":>14} {"KSX resolved":>14}  {"Delta (KSX-KS1)"}')
    print(f'  {"-" * 85}')
    for k, ks1_s, ksx_s, delta_s in diffs:
        print(f'  {k:<55} {ks1_s:>14} {ksx_s:>14}  {delta_s}')
