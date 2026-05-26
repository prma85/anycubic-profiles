import json, glob, subprocess

TEMP_KEYS = [
    'nozzle_temperature', 'nozzle_temperature_initial_layer',
    'nozzle_temperature_BRASS', 'nozzle_temperature_initial_layer_BRASS',
    'nozzle_temperature_HS', 'nozzle_temperature_initial_layer_HS',
]

sys_profiles = {}
for f in glob.glob('C:/Users/pandrade/AppData/Roaming/AnycubicSlicerNext/system/Anycubic/filament/*.json'):
    with open(f, encoding='utf-8') as fp:
        try:
            d = json.load(fp)
        except Exception:
            continue
    sys_profiles[d.get('name', '')] = d

renames = {
    'filament/ESun PETG Translucent @AC KS1 0.4mm.json':
        'filament/eSun PETG Translucent @AC KS1 0.4mm.json',
    'filament/ESun PETG Translucent @AC KSX 0.4mm.json':
        'filament/eSun PETG Translucent @AC KSX 0.4mm.json',
    'filament/IBoss Glitter PETG @AC KS1 0.4mm.json':
        'filament/iBoss Glitter PETG @AC KS1 0.4mm.json',
    'filament/IBoss Glitter PETG @AC KSX 0.4mm.json':
        'filament/iBoss Glitter PETG @AC KSX 0.4mm.json',
    'filament/TecBears Rapid PETG @AC KS1 0.4mm.json':
        'filament/TECBEARS Rapid PETG @AC KS1 0.4mm.json',
    'filament/TecBears Rapid PETG @AC KSX 0.4mm.json':
        'filament/TECBEARS Rapid PETG @AC KSX 0.4mm.json',
}

issues = []
ok = 0
for new_path, old_path in renames.items():
    git_path = old_path.replace('\\', '/')
    old_r = subprocess.run(['git', 'show', 'fb2c04f:' + git_path],
                           capture_output=True, text=True)
    if old_r.returncode != 0:
        print('SKIP (not in fb2c04f):', old_path)
        continue
    try:
        old_d = json.loads(old_r.stdout)
    except Exception as e:
        print('PARSE ERR:', e)
        continue

    with open(new_path, encoding='utf-8') as fp:
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
                ok += 1
            else:
                issues.append((name, k, old_v, par_v, '(inherited)', 'LOST'))
        elif str(cur_v) != str(old_v):
            issues.append((name, k, old_v, par_v, cur_v, 'CHANGED'))

print(f'Correctly simplified: {ok}')
print(f'Issues: {len(issues)}')
for name, k, old, par, cur, status in sorted(issues):
    flag = '***' if status == 'LOST' else '   '
    print(f'{flag} [{status}] {name}: {k}')
    print(f'       before={old!r}  parent={str(par)!r}  now={cur!r}')
