"""
Audit all nozzle variant MVS values against their expected value
(parent 0.4mm effective MVS * canonical scale factor).
Reports: wrong value, correct value, and what needs fixing.
Also reports the Generic PLA Miniatures special case.
"""
import json, glob

SCALE = {'0.25mm': 0.50, '0.6mm': 1.25, '0.8mm': 1.50}
# TPU caps override scaling
TPU_CAPS = {'0.6mm': {'standard': 5, 'hs': 5}, '0.8mm': {'standard': 7, 'hs': 7}}

def load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def fmt(v):
    if v is None: return None
    f = round(float(v), 1)
    return int(f) if f == int(f) else f

def resolve_mvs(name, up, sp, depth=0):
    if depth > 6: return None
    d = up[name][1] if name in up else sp.get(name)
    if not d: return None
    v = d.get('filament_max_volumetric_speed', [None])[0]
    if v is not None: return float(v)
    return resolve_mvs(d.get('inherits', ''), up, sp, depth + 1)

user_profiles = {}
for f in sorted(glob.glob('filament/*.json')):
    d = load(f)
    user_profiles[d.get('name', '')] = (f, d)

sys_profiles = {}
for f in glob.glob('C:/Users/pandrade/AppData/Roaming/AnycubicSlicerNext/system/Anycubic/filament/*.json'):
    d = load(f)
    sys_profiles[d.get('name', '')] = d

wrong = []     # (name, fpath, cur, expected, parent_mvs, size)
correct = []

for name, (fpath, d) in sorted(user_profiles.items()):
    size = next((s for s in SCALE if name.endswith(s)), None)
    if not size:
        continue

    parent_name = d.get('inherits', '')
    if parent_name not in user_profiles:
        continue  # inherits from system — not a nozzle variant
    _, pd = user_profiles[parent_name]
    if '@Anycubic Kobra' not in pd.get('inherits', ''):
        continue  # parent is not a 0.4mm root profile

    cur = d.get('filament_max_volumetric_speed', [None])[0]
    if cur is None:
        continue  # inheriting — skip

    n = name.lower()
    is_tpu = 'tpu' in n
    is_miniatures = 'miniatures' in n

    parent_mvs = resolve_mvs(parent_name, user_profiles, sys_profiles)
    if parent_mvs is None:
        continue

    # Determine expected value
    if is_miniatures:
        # Miniatures: slow specialty — expected scales normally from 0.4mm
        raw = parent_mvs * SCALE[size]
        expected = 3 if size == '0.25mm' else fmt(raw)
    elif is_tpu:
        # TPU: hard caps regardless of base
        is_hs = any(x in n for x in ['hs', 'high speed', 'overture high'])
        caps = TPU_CAPS.get(size, {})
        if size == '0.25mm':
            expected = 3
        elif is_hs:
            expected = caps['hs']
        else:
            expected = caps['standard']
    else:
        raw = parent_mvs * SCALE[size]
        expected = 3 if (size == '0.25mm' and raw > 3) else fmt(raw)

    if fmt(float(cur)) != expected:
        wrong.append((name, fpath, float(cur), expected, parent_mvs, size))
    else:
        correct.append(name)

print(f'Correct: {len(correct)}')
print(f'Wrong:   {len(wrong)}')
print()
print(f'{"Profile":<55} {"Size":<7} {"Base":>6} {"Got":>6} {"Expected":>8}')
print('-' * 90)
for name, fpath, cur, exp, base, size in sorted(wrong):
    flag = '  '
    if 'miniatures' in name.lower(): flag = '**'
    print(f'{flag} {name:<53} {size:<7} {base:>6} {cur:>6} {exp:>8}')
