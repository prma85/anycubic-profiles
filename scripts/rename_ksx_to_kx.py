"""
Rename all KSX -> KX in user filament profiles.

Changes:
  - Filenames:  *KSX* -> *KX*  (both .json and .info)
  - Inside JSON:
      name, filament_settings_id, inherits: replace "@AC KSX" -> "@AC KX"
  - Inside .info:
      setting_id: replace "KSX" -> "KX"

Does NOT change:
  - compatible_printers machine names (e.g. "Anycubic Kobra X 0.4 nozzle")
    — these reference system profiles we don't own
  - Any content inside system/ directory
"""
import json, glob, os, re

FILAMENT_DIR = 'filament'
IDENTITY = {
    'filament_settings_id','filament_vendor','from','inherits',
    'is_custom_defined','name','version',
}


def rename_str(s):
    """Replace @AC KSX with @AC KX in a profile name/id string."""
    return s.replace('@AC KSX', '@AC KX')


def save_sorted(fpath, d):
    content  = sorted(k for k in d if k not in IDENTITY)
    identity = sorted(k for k in d if k in IDENTITY)
    ordered  = {k: d[k] for k in content + identity}
    with open(fpath, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(ordered, f, indent=4, ensure_ascii=False)
        f.write('\n')


json_files = sorted(glob.glob(f'{FILAMENT_DIR}/*KSX*.json'))
info_files = sorted(glob.glob(f'{FILAMENT_DIR}/*KSX*.info'))

print(f'JSON files to process: {len(json_files)}')
print(f'INFO files to process: {len(info_files)}')
print()

renamed_files = 0
updated_json  = 0

# ── Step 1: Update JSON content first (before renaming files) ────────────────
for fpath in json_files:
    with open(fpath, encoding='utf-8') as f:
        try:
            d = json.load(f)
        except Exception as e:
            print(f'  PARSE ERR {fpath}: {e}')
            continue

    changed = False

    # name
    old_name = d.get('name', '')
    new_name = rename_str(old_name)
    if new_name != old_name:
        d['name'] = new_name
        changed = True

    # filament_settings_id
    fsi = d.get('filament_settings_id', [])
    new_fsi = [rename_str(v) for v in fsi]
    if new_fsi != fsi:
        d['filament_settings_id'] = new_fsi
        changed = True

    # inherits
    old_inh = d.get('inherits', '')
    new_inh = rename_str(old_inh)
    if new_inh != old_inh:
        d['inherits'] = new_inh
        changed = True

    if changed:
        save_sorted(fpath, d)
        updated_json += 1

print(f'JSON files with content updated: {updated_json}')

# ── Step 2: Update INFO content ──────────────────────────────────────────────
updated_info = 0
for fpath in info_files:
    lines = []
    with open(fpath, encoding='utf-8') as f:
        raw = f.read()
    if 'KSX' not in raw:
        continue
    new_raw = raw.replace('KSX', 'KX')
    with open(fpath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(new_raw)
    updated_info += 1

print(f'INFO files with content updated: {updated_info}')

# ── Step 3: Rename files ──────────────────────────────────────────────────────
all_to_rename = sorted(
    glob.glob(f'{FILAMENT_DIR}/*KSX*.json') +
    glob.glob(f'{FILAMENT_DIR}/*KSX*.info')
)

for old_path in all_to_rename:
    new_path = old_path.replace('KSX', 'KX')
    if old_path != new_path:
        os.rename(old_path, new_path)
        renamed_files += 1

print(f'Files renamed: {renamed_files}')

# ── Verification ──────────────────────────────────────────────────────────────
remaining_ksx = (
    glob.glob(f'{FILAMENT_DIR}/*KSX*')
)
print(f'\nRemaining KSX files: {len(remaining_ksx)}')
if remaining_ksx:
    for f in remaining_ksx[:5]:
        print(f'  {f}')

# Check internal references still have KSX
ksx_internal = 0
for f in glob.glob(f'{FILAMENT_DIR}/*.json'):
    with open(f, encoding='utf-8') as fp:
        try: d = json.load(fp)
        except: continue
    name = d.get('name','')
    inh  = d.get('inherits','')
    fsi  = ' '.join(d.get('filament_settings_id',[]))
    if '@AC KSX' in name or '@AC KSX' in inh or '@AC KSX' in fsi:
        ksx_internal += 1
        print(f'  STILL HAS KSX: {f}')

print(f'JSON files with remaining @AC KSX references: {ksx_internal}')
print('\nDone.')
