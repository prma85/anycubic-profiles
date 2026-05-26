import json, glob, subprocess

BASE_COMMITS = ['75c5393', 'c6b6ec9', 'fb2c04f']
IDENTITY = {
    'filament_settings_id','filament_vendor','from','inherits','is_custom_defined',
    'name','version','type','setting_id','filament_id','instantiation',
    'filament_type','compatible_printers',
}

ksx_files = sorted(f for f in glob.glob('filament/Improved * @AC KSX 0.4mm.json'))

all_missing = {}  # fpath -> {key: old_value}

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
        cur_ksx = json.load(f)

    name = cur_ksx.get('name', '')
    old_only = {}
    for k, v in old_ksx.items():
        if k in IDENTITY:
            continue
        if k in ks1:
            continue  # KS1 has it — script handled it
        if not v:
            continue
        old_only[k] = v

    if old_only:
        print(f'\n{name}:')
        missing = {}
        for k, v in sorted(old_only.items()):
            cur_v = cur_ksx.get(k)
            val_str = str(v[0] if isinstance(v, list) else v)
            if len(val_str) > 50:
                val_str = val_str[:50] + '...'
            if cur_v is None:
                status = 'LOST (now inherited)'
                missing[k] = v
            else:
                cur_str = str(cur_v[0] if isinstance(cur_v, list) else cur_v)
                if cur_str == str(v[0] if isinstance(v, list) else v):
                    status = 'OK (preserved)'
                else:
                    status = f'CHANGED -> {cur_str}'
                    missing[k] = v
            print(f'  {k:<50} was: {val_str:<35} {status}')
        all_missing[fpath] = missing

print(f'\n\nSummary: {len(all_missing)} profiles have lost/changed KSX-specific keys')
