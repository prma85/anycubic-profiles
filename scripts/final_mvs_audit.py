import json, glob, subprocess

SCALE = {'0.25mm': 0.50, '0.6mm': 1.25, '0.8mm': 1.50}

user_profiles = {}
for f in sorted(glob.glob('filament/*.json')):
    with open(f, encoding='utf-8') as fp:
        d = json.load(fp)
    user_profiles[d.get('name', '')] = (f.replace('\\', '/'), d)

sys_profiles = {}
for f in glob.glob('C:/Users/pandrade/AppData/Roaming/AnycubicSlicerNext/system/Anycubic/filament/*.json'):
    with open(f, encoding='utf-8') as fp:
        d = json.load(fp)
    sys_profiles[d.get('name', '')] = d


def resolve_mvs(name, up, sp, depth=0):
    if depth > 6:
        return None
    d = up[name][1] if name in up else sp.get(name)
    if not d:
        return None
    v = d.get('filament_max_volumetric_speed', [None])[0]
    if v is not None:
        return float(v)
    return resolve_mvs(d.get('inherits', ''), up, sp, depth + 1)


issues = []
for name, (fpath, d) in sorted(user_profiles.items()):
    size = next((s for s in SCALE if name.endswith(s)), None)
    if not size:
        continue
    parent_name = d.get('inherits', '')
    if parent_name not in user_profiles:
        continue
    _, pd = user_profiles[parent_name]
    if '@Anycubic Kobra' not in pd.get('inherits', ''):
        continue
    cur = d.get('filament_max_volumetric_speed', [None])[0]
    if not cur:
        continue

    old_v = None
    for base in ['fb2c04f', 'c6b6ec9', '75c5393']:
        r = subprocess.run(['git', 'show', base + ':' + fpath],
                           capture_output=True, text=True)
        if r.returncode == 0:
            try:
                old_d = json.loads(r.stdout)
                old_v = old_d.get('filament_max_volumetric_speed', [None])[0]
                break
            except Exception:
                pass

    parent_mvs = resolve_mvs(parent_name, user_profiles, sys_profiles)
    if not parent_mvs:
        continue
    raw = parent_mvs * SCALE[size]
    exp = 3 if (size == '0.25mm' and raw > 3) else round(raw, 1)
    exp_clean = int(exp) if exp == int(exp) else exp

    cur_f = float(cur)
    old_f = float(old_v) if old_v else None

    if old_v and abs(cur_f - old_f) > 0.05 and abs(cur_f - float(exp_clean)) > 0.15:
        issues.append((name, old_f, cur_f, exp_clean))

if issues:
    print(f'Unexplained changes ({len(issues)}):')
    for name, old, cur, exp in sorted(issues):
        print(f'  {name}: before={old}, now={cur}, formula={exp}')
else:
    print('CLEAN: no unexplained MVS changes found.')
    print('All differences are correct scaling or preserved hand-calibrations.')
