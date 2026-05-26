import json, glob, subprocess

TEMP_KEYS = [
    'nozzle_temperature',
    'nozzle_temperature_initial_layer',
    'nozzle_temperature_BRASS',
    'nozzle_temperature_initial_layer_BRASS',
    'nozzle_temperature_HS',
    'nozzle_temperature_initial_layer_HS',
]

sys_profiles = {}
for f in glob.glob('C:/Users/pandrade/AppData/Roaming/AnycubicSlicerNext/system/Anycubic/filament/*.json'):
    with open(f, encoding='utf-8') as fp:
        try:
            d = json.load(fp)
        except Exception:
            continue
    sys_profiles[d.get('name', '')] = d

issues = []
ok_simplified = 0

all_files = sorted(glob.glob('filament/*.json'))
petg_04mm = [f for f in all_files if 'petg' in f.lower() and '0.4mm' in f.lower()]
petg_04mm = [f.replace('\\', '/') for f in petg_04mm]

for fpath in petg_04mm:
    old_r = subprocess.run(['git', 'show', 'fb2c04f:' + fpath], capture_output=True, text=True)
    if old_r.returncode != 0:
        print('SKIP (new file):', fpath)
        continue
    try:
        old_d = json.loads(old_r.stdout)
    except Exception as e:
        print('PARSE ERR:', fpath, e)
        continue

    with open(fpath, encoding='utf-8') as fp:
        cur_d = json.load(fp)

    name = cur_d.get('name', '')
    parent_name = cur_d.get('inherits', '')
    pd = sys_profiles.get(parent_name, {})

    for k in TEMP_KEYS:
        old_v = old_d.get(k, [None])[0]
        cur_v = cur_d.get(k, [None])[0]
        par_v = pd.get(k, [None])[0]
        if old_v is None:
            continue
        if cur_v is None:
            if str(par_v) == str(old_v):
                ok_simplified += 1
            else:
                issues.append((name, k, old_v, par_v, '(inherited)', 'LOST'))
        elif str(cur_v) != str(old_v):
            issues.append((name, k, old_v, par_v, cur_v, 'CHANGED'))

print(f'Correctly simplified (old==parent, now inherited): {ok_simplified}')
print(f'Issues found: {len(issues)}')
print()
for name, k, old, par, cur, status in sorted(issues):
    flag = '***' if status == 'LOST' else '   '
    print(f'{flag} [{status}] {name}')
    print(f'       {k}: before={old!r}  parent={str(par)!r}  now={cur!r}')
