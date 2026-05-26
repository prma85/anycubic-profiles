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
skipped_new = []

BASE_COMMITS = ['fb2c04f', 'c6b6ec9', '80e8c43']

all_files = sorted(glob.glob('filament/*.json'))
petg_04mm = []
for f in all_files:
    fl = f.lower()
    if 'petg' in fl and '0.4mm' in fl:
        petg_04mm.append(f.replace('\\', '/'))

for fpath in petg_04mm:
    old_d = None
    for base in BASE_COMMITS:
        r = subprocess.run(['git', 'show', base + ':' + fpath], capture_output=True, text=True)
        if r.returncode == 0:
            try:
                old_d = json.loads(r.stdout)
                break
            except Exception:
                pass
    if old_d is None:
        skipped_new.append(fpath)
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

print(f'Profiles checked: {len(petg_04mm) - len(skipped_new)}')
print(f'Skipped (brand new, no base commit): {len(skipped_new)}')
print(f'Correctly simplified (old==parent): {ok_simplified}')
print(f'Issues: {len(issues)}')
print()
for name, k, old, par, cur, status in sorted(issues):
    flag = '***' if status == 'LOST' else '   '
    print(f'{flag} [{status}] {name}')
    print(f'       {k}: before={old!r}  parent={str(par)!r}  now={cur!r}')

if skipped_new:
    print('\nBrand-new files (no base):')
    for f in skipped_new:
        print(f'  {f}')
