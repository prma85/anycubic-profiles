"""
Restore KSX-specific calibrated keys that were present in the old profile
but missing from the new rebuilt profile because they weren't in KS1 Improved.

Strategy:
  - Keys to always drop (old-format header fields): bed_type, filament_load_time,
    filament_unload_time (already removed in bc0f044 refactor — correct)
  - Keys to restore from old KSX: everything else that was explicit in old KSX
    but is now inherited (and where the effective inherited value differs from
    what the old profile had)
  - Exception: filament_adhesiveness_category — was 0 explicit, now inherited 100.
    Check what the old KSX system parent gives and decide.
"""
import json, glob, subprocess

BASE_COMMITS = ['75c5393', 'c6b6ec9', 'fb2c04f']
IDENTITY = {
    'filament_settings_id','filament_vendor','from','inherits','is_custom_defined',
    'name','version',
}
# Fields we intentionally dropped in the refactor — do NOT restore
ALWAYS_DROP = {
    'bed_type','filament_load_time','filament_unload_time',
    'type','setting_id','filament_id','instantiation','filament_type',
    'compatible_printers',
    # filament_adhesiveness_category: was 0 explicitly, KSX sys has 100.
    # The slicer added this field later — 0 was the old default before the field existed.
    # The inherited 100 from KSX system is the correct current value. Drop.
    'filament_adhesiveness_category',
}

SYS = 'C:/Users/pandrade/AppData/Roaming/AnycubicSlicerNext/system/Anycubic/filament'
SP = {}
for f in glob.glob(f'{SYS}/*.json'):
    with open(f, encoding='utf-8') as fp:
        try: d = json.load(fp)
        except: continue
    SP[d.get('name','')] = d

def resolve_sys(name, key, depth=0):
    if depth > 8: return None
    d = SP.get(name)
    if not d: return None
    v = d.get(key)
    if v is not None: return v[0] if isinstance(v, list) else v
    return resolve_sys(d.get('inherits',''), key, depth+1)

def save_sorted(fpath, d):
    content  = sorted(k for k in d if k not in IDENTITY)
    identity = sorted(k for k in d if k in IDENTITY)
    ordered  = {k: d[k] for k in content + identity}
    with open(fpath, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(ordered, f, indent=4, ensure_ascii=False)
        f.write('\n')

def update_info(fpath, name):
    import os
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

ksx_files = sorted(f for f in glob.glob('filament/Improved * @AC KSX 0.4mm.json'))
KSX_SYS_PARENTS = {
    'Improved PLA @AC KSX 0.4mm':              'Anycubic PLA @Anycubic Kobra X 0.4 nozzle',
    'Improved PLA+ @AC KSX 0.4mm':             'Anycubic PLA+ @Anycubic Kobra X 0.4 nozzle',
    'Improved PETG @AC KSX 0.4mm':             'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
    'Improved PETG HS @AC KSX 0.4mm':          'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
    'Improved PETG Translucent @AC KSX 0.4mm': 'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
}

for fpath in ksx_files:
    git_path = fpath.replace('\\', '/')

    old_ksx = {}
    for c in BASE_COMMITS:
        r = subprocess.run(['git', 'show', c + ':' + git_path],
                           capture_output=True, text=True)
        if r.returncode == 0:
            try:
                old_ksx = json.loads(r.stdout)
                break
            except Exception:
                pass
    if not old_ksx:
        print(f'SKIP (no history): {fpath}')
        continue

    ks1_path = fpath.replace('@AC KSX', '@AC KS1')
    try:
        with open(ks1_path, encoding='utf-8') as f:
            ks1 = json.load(f)
    except Exception:
        print(f'SKIP (no KS1): {fpath}')
        continue

    with open(fpath, encoding='utf-8') as f:
        cur = json.load(f)

    name = cur.get('name', '')
    sys_parent = KSX_SYS_PARENTS.get(name, '')
    restored = []

    for k, raw in old_ksx.items():
        if k in ALWAYS_DROP or k in IDENTITY:
            continue
        if k in ks1:
            continue  # already handled by rebuild script

        old_v = raw[0] if isinstance(raw, list) else raw
        cur_v_raw = cur.get(k)
        cur_v = (cur_v_raw[0] if isinstance(cur_v_raw, list) else cur_v_raw) if cur_v_raw else None

        # Inherited value from KSX system parent
        sys_v = resolve_sys(sys_parent, k)

        if cur_v is not None:
            # Already present — check if it matches old value
            if str(cur_v) == str(old_v):
                continue  # fine
            else:
                # Restore old value (it was changed)
                cur[k] = raw if isinstance(raw, list) else [str(old_v)]
                restored.append(f'  RESTORE {k}: {cur_v!r} -> {old_v!r}')
        else:
            # Currently inherited — should we restore?
            if sys_v is not None and str(sys_v) == str(old_v):
                # Inherited value matches old explicit — no need to restore
                continue
            else:
                # Inherited value differs from what we had — restore
                cur[k] = raw if isinstance(raw, list) else [str(old_v)]
                restored.append(f'  RESTORE {k}: (was inherited={sys_v!r}) -> {old_v!r}')

    if restored:
        save_sorted(fpath, cur)
        update_info(fpath, name)
        print(f'\n{name}:')
        for line in restored:
            print(line)
    else:
        print(f'{name}: nothing to restore')

print('\nDone.')
