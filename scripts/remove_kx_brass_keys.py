"""
Remove all BRASS-specific temperature and fan keys from KX filament profiles.
The Kobra X has a single machine profile with nozzle_type=hardened_steel.
There are no Brass machine variants for KX, so BRASS filament keys are never used.
"""
import json, glob, os

IDENTITY = {'filament_settings_id','filament_vendor','from','inherits',
            'is_custom_defined','name','version'}

BRASS_KEYS = {
    'nozzle_temperature_BRASS',
    'nozzle_temperature_initial_layer_BRASS',
    'fan_max_speed_BRASS',
    'fan_min_speed_BRASS',
    'fan_cooling_layer_time_BRASS',
    'slow_down_layer_time_BRASS',
    'nozzle_temperature_range_high_BRASS',
    'nozzle_temperature_range_low_BRASS',
}


def save_sorted(fpath, d):
    content  = sorted(k for k in d if k not in IDENTITY)
    identity = sorted(k for k in d if k in IDENTITY)
    ordered  = {k: d[k] for k in content + identity}
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


kx_files = sorted(glob.glob('filament/*@AC KX*.json'))
fixed = 0
for fpath in kx_files:
    with open(fpath, encoding='utf-8') as f:
        try:
            d = json.load(f)
        except Exception:
            continue
    name = d.get('name', '')
    removed = []
    for k in list(d.keys()):
        if k in BRASS_KEYS:
            del d[k]
            removed.append(k)
    if removed:
        save_sorted(fpath, d)
        update_info(fpath, name)
        fixed += 1

print(f'Cleaned BRASS keys from {fixed} KX profiles.')
print('Removed keys (across all profiles): nozzle_temperature_BRASS, '
      'nozzle_temperature_initial_layer_BRASS, fan_max_speed_BRASS, '
      'fan_min_speed_BRASS, fan_cooling_layer_time_BRASS, slow_down_layer_time_BRASS')
