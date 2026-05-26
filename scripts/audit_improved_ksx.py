import json, glob, subprocess

files_to_check = [
    'filament/Improved PLA @AC KSX 0.4mm.json',
    'filament/Improved PLA+ @AC KSX 0.4mm.json',
    'filament/Improved PETG @AC KSX 0.4mm.json',
    'filament/Improved PETG HS @AC KSX 0.4mm.json',
    'filament/Improved PETG Translucent @AC KSX 0.4mm.json',
]

KEYS = [
    'nozzle_temperature',
    'nozzle_temperature_initial_layer',
    'nozzle_temperature_BRASS',
    'nozzle_temperature_initial_layer_BRASS',
    'nozzle_temperature_HS',
    'nozzle_temperature_initial_layer_HS',
    'nozzle_temperature_range_high',
    'nozzle_temperature_range_low',
    'filament_max_volumetric_speed',
    'filament_flow_ratio',
    'pressure_advance',
    'hot_plate_temp',
    'hot_plate_temp_initial_layer',
    'textured_plate_temp',
    'textured_plate_temp_initial_layer',
    'cool_plate_temp',
    'cool_plate_temp_initial_layer',
    'fan_max_speed',
    'fan_min_speed',
]

COMMITS = ['75c5393', 'c6b6ec9', 'fb2c04f', 'HEAD']

for fpath in files_to_check:
    print(f"\n{'='*90}")
    print(f"  {fpath.split('/')[-1]}")
    print(f"  {'Key':<45} {'75c5393':>12} {'c6b6ec9':>12} {'fb2c04f':>12} {'HEAD':>12}")
    print(f"  {'-'*85}")
    all_vals = {}
    for c in COMMITS:
        if c == 'HEAD':
            try:
                with open(fpath, encoding='utf-8') as f:
                    d = json.load(f)
            except Exception:
                d = {}
        else:
            git_path = fpath.replace('\\', '/')
            r = subprocess.run(['git', 'show', c + ':' + git_path],
                               capture_output=True, text=True)
            if r.returncode != 0:
                d = {}
            else:
                try:
                    d = json.loads(r.stdout)
                except Exception:
                    d = {}
        for k in KEYS:
            raw = d.get(k)
            v = raw[0] if isinstance(raw, list) else raw
            all_vals.setdefault(k, {})[c] = v

    for k in KEYS:
        row = all_vals[k]
        vals = [str(row.get(c) if row.get(c) is not None else '-') for c in COMMITS]
        changed = ' <--' if vals[0] != vals[3] and vals[0] != '?' else ''
        print(f"  {k:<45} {vals[0]:>12} {vals[1]:>12} {vals[2]:>12} {vals[3]:>12}{changed}")
