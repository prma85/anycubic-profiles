"""Cascade corrected parent temps to nozzle variants."""
import json, glob, os

IDENTITY = {'filament_settings_id','filament_vendor','from','inherits','is_custom_defined','name','version'}
TEMP_KEYS = ['nozzle_temperature','nozzle_temperature_initial_layer',
             'nozzle_temperature_BRASS','nozzle_temperature_initial_layer_BRASS',
             'nozzle_temperature_HS','nozzle_temperature_initial_layer_HS',
             'nozzle_temperature_range_high']
PLA_DELTA  = {'0.25mm': -5, '0.6mm': 5, '0.8mm': 10}
PETG_DELTA = {'0.6mm': 10, '0.8mm': 15}

user_profiles = {}
for f in sorted(glob.glob('filament/*.json')):
    with open(f, encoding='utf-8') as fp:
        try:
            d = json.load(fp)
        except Exception:
            continue
    fp_clean = f.replace('\\', '/')
    user_profiles[d.get('name', '')] = (fp_clean, d)


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


TARGETS = [
    ('Improved PLA @AC KX 0.4mm',
     ['Improved PLA @AC KX 0.25mm', 'Improved PLA @AC KX 0.6mm', 'Improved PLA @AC KX 0.8mm'],
     PLA_DELTA),
    ('Improved PLA+ @AC KX 0.4mm',
     ['Improved PLA+ @AC KX 0.25mm', 'Improved PLA+ @AC KX 0.6mm', 'Improved PLA+ @AC KX 0.8mm'],
     PLA_DELTA),
    ('Improved PETG @AC KX 0.4mm',
     ['Improved PETG @AC KX 0.6mm', 'Improved PETG @AC KX 0.8mm'],
     PETG_DELTA),
    ('Improved PETG HS @AC KX 0.4mm',
     ['Improved PETG HS @AC KX 0.6mm', 'Improved PETG HS @AC KX 0.8mm'],
     PETG_DELTA),
    ('Improved PETG Translucent @AC KX 0.4mm',
     ['Improved PETG Translucent @AC KX 0.6mm', 'Improved PETG Translucent @AC KX 0.8mm'],
     PETG_DELTA),
    # KS1 PLA+ also got nozzle_temperature_HS correction
    ('Improved PLA+ @AC KS1 0.4mm',
     ['Improved PLA+ @AC KS1 0.25mm', 'Improved PLA+ @AC KS1 0.6mm', 'Improved PLA+ @AC KS1 0.8mm'],
     PLA_DELTA),
]

for parent_name, variants, delta_map in TARGETS:
    if parent_name not in user_profiles:
        continue
    _, parent_d = user_profiles[parent_name]
    for vname in variants:
        if vname not in user_profiles:
            continue
        vpath, vd = user_profiles[vname]
        size = next((s for s in ('0.25mm', '0.6mm', '0.8mm') if vname.endswith(s)), None)
        if not size or size not in delta_map:
            continue
        delta = delta_map[size]
        changed = []
        for tk in TEMP_KEYS:
            pv = parent_d.get(tk, [None])[0]
            if pv is None:
                continue
            expected = str(int(pv) + delta)
            cur = vd.get(tk, [None])[0]
            if str(cur) != expected:
                vd[tk] = [expected]
                changed.append(f'{tk}: {cur!r} -> {expected!r}')
        if changed:
            save_sorted(vpath, vd)
            update_info(vpath, vname)
            print(f'Updated {vname}: {len(changed)} keys')
            for c in changed:
                print(f'  {c}')

print('Done.')
