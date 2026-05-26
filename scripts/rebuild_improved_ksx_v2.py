"""
Rebuild Improved KSX 0.4mm profiles using a curated delta table derived
from the system parent comparison, applied only where the delta makes sense.

Delta application rules:
  - FAN speeds/times: apply delta (open printer differs structurally)
  - PLATE temperatures: apply delta (KSX bed calibration differs)
  - activate_air_filtration / additional_cooling_fan_speed: always KSX=0 (no hardware)
  - MVS, flow_ratio, pressure_advance: copy KS1 Improved value directly
    (these are calibration values, not printer-structural differences;
     KSX was never independently calibrated — use KS1 as the reference)
  - Nozzle temperatures: copy KS1 Improved (same filament, same melt requirements;
    KSX system parent diffs are due to different system profile generation,
    not actual calibrated printer differences)
  - filament_cost, filament_density: copy KS1 Improved (brand-specific, not printer)
  - cool_plate_temp: take from Improved KS1 directly (we already fixed these to 50/40)
  - PETG-specific: nozzle_temperature_BRASS/HS on KSX system = same as base (230)
    because KSX parent explicitly sets them. Take KS1 Improved values for these.

Hardware-structural fields where KSX genuinely differs:
  - activate_air_filtration, additional_cooling_fan_speed: always 0 for KSX
  - fan_max_speed_BRASS, fan_max_speed_HS, fan_min_speed_BRASS, fan_min_speed_HS:
      apply delta (open printer needs less fan)
  - fan_cooling_layer_time_BRASS, fan_cooling_layer_time_HS: apply delta
  - slow_down_layer_time (PETG): apply delta (-2 from system comparison)
  - overhang_fan_threshold (PETG): KSX system uses 50%, KS1 uses 10% — take KSX value
  - Retraction fields: KSX system has nil for many (let inherit) vs KS1 explicit values
    Decision: keep explicit values from KS1 Improved (they were calibrated, not defaults)
"""
import json, glob

SYS = 'C:/Users/pandrade/AppData/Roaming/AnycubicSlicerNext/system/Anycubic/filament'
FILAMENT_DIR = 'filament'

IDENTITY = {
    'filament_settings_id','filament_vendor','from','inherits',
    'is_custom_defined','name','version',
}

TEMP_KEYS = [
    'nozzle_temperature','nozzle_temperature_initial_layer',
    'nozzle_temperature_BRASS','nozzle_temperature_initial_layer_BRASS',
    'nozzle_temperature_HS','nozzle_temperature_initial_layer_HS',
    'nozzle_temperature_range_high',
]
PLA_NOZZLE_DELTA  = {'0.25mm': -5, '0.6mm':  5, '0.8mm': 10}
PETG_NOZZLE_DELTA = {             '0.6mm': 10, '0.8mm': 15}


def load_sys():
    sp = {}
    for f in glob.glob(f'{SYS}/*.json'):
        with open(f, encoding='utf-8') as fp:
            try: d = json.load(fp)
            except: continue
        sp[d.get('name', '')] = d
    return sp

def load_user():
    up = {}
    for f in sorted(glob.glob(f'{FILAMENT_DIR}/*.json')):
        with open(f, encoding='utf-8') as fp:
            try: d = json.load(fp)
            except: continue
        up[d.get('name', '')] = (f.replace('\\', '/'), d)
    return up

def resolve_sys(name, key, sp, depth=0):
    if depth > 8: return None
    d = sp.get(name)
    if not d: return None
    v = d.get(key)
    if v is not None: return v[0] if isinstance(v, list) else v
    return resolve_sys(d.get('inherits', ''), key, sp, depth + 1)

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

def get(d, k):
    v = d.get(k)
    if v is None: return None
    return v[0] if isinstance(v, list) else v

def setkv(d, k, v):
    d[k] = [str(v)]

def numeric_delta(ks1_v, ks1_sys, ksx_sys):
    """Return (delta, new_value_str) for a field with known numeric delta."""
    try:
        delta = float(str(ksx_sys)) - float(str(ks1_sys))
        new_v = float(str(ks1_v)) + delta
        new_v = int(new_v) if new_v == int(new_v) else round(new_v, 4)
        return delta, str(new_v)
    except (TypeError, ValueError):
        return None, str(ks1_v)


SP = load_sys()
UP = load_user()

# ─────────────────────────────────────────────────────────────────────────────
# Fan speed delta keys: always apply system-derived delta
# These are genuinely different because KSX is open (less cooling needed)
# ─────────────────────────────────────────────────────────────────────────────
FAN_DELTA_KEYS = {
    'fan_max_speed', 'fan_min_speed',
    'fan_max_speed_BRASS', 'fan_min_speed_BRASS',
    'fan_max_speed_HS', 'fan_min_speed_HS',
    'fan_cooling_layer_time', 'fan_cooling_layer_time_BRASS', 'fan_cooling_layer_time_HS',
    'full_fan_speed_layer',
    'close_fan_the_first_x_layers',
    'enable_overhang_bridge_fan',
    'overhang_fan_speed', 'overhang_fan_threshold',
}
# Plate temp delta keys: KSX bed runs at different target (apply delta)
PLATE_DELTA_KEYS = {
    'hot_plate_temp', 'hot_plate_temp_initial_layer',
    'textured_plate_temp', 'textured_plate_temp_initial_layer',
}
# Always KSX=0 (hardware not present)
HARDWARE_ZERO = {'activate_air_filtration', 'additional_cooling_fan_speed'}
# Copy KS1 Improved directly (calibration data, not printer-structural)
COPY_FROM_KS1 = {
    'nozzle_temperature', 'nozzle_temperature_initial_layer',
    'nozzle_temperature_BRASS', 'nozzle_temperature_initial_layer_BRASS',
    'nozzle_temperature_HS', 'nozzle_temperature_initial_layer_HS',
    'nozzle_temperature_range_high', 'nozzle_temperature_range_low',
    'filament_max_volumetric_speed', 'filament_flow_ratio', 'pressure_advance',
    'filament_cost', 'filament_density',
    'cool_plate_temp', 'cool_plate_temp_initial_layer',
    # Retraction / motion: keep KS1 calibration
    'filament_retraction_length', 'filament_retraction_speed',
    'filament_retraction_minimum_travel', 'filament_deretraction_speed',
    'filament_retract_before_wipe', 'filament_retract_lift_below',
    'filament_retract_lift_enforce', 'filament_retract_restart_extra',
    'filament_retract_when_changing_layer',
    'filament_z_hop', 'filament_z_hop_types',
    'filament_wipe', 'filament_wipe_distance',
    # Thermal
    'idle_temperature', 'temperature_vitrification', 'slow_down_layer_time',
    'slow_down_min_speed', 'slow_down_for_layer_cooling',
    'reduce_fan_stop_start_freq', 'fan_cooling_layer_time',
    'dont_slow_down_outer_wall',
    # Purge / misc
    'filament_minimal_purge_on_wipe_tower', 'filament_start_gcode',
    'filament_end_gcode',
    # Per-nozzle material overrides from KS1 profiles
    'activate_chamber_temp_control', 'chamber_temperature',
    'during_print_exhaust_fan_speed', 'complete_print_exhaust_fan_speed',
    'adaptive_pressure_advance_model',
    'fan_cooling_layer_time_HS', 'fan_max_speed_HS', 'fan_min_speed_HS',
    'slow_down_layer_time_HS',
    # Cost/vendor fields
    'filament_cost',
}

MATERIALS = {
    'PLA': {
        'ks1': 'Improved PLA @AC KS1 0.4mm',
        'ksx': 'Improved PLA @AC KSX 0.4mm',
        'ks1_sys': 'Anycubic PLA @Anycubic Kobra S1 0.4 nozzle',
        'ksx_sys': 'Anycubic PLA @Anycubic Kobra X 0.4 nozzle',
        'ksx_inherits': 'Anycubic PLA @Anycubic Kobra X 0.4 nozzle',
        'nozzle_delta': PLA_NOZZLE_DELTA,
        'variants': ['Improved PLA @AC KSX 0.25mm',
                     'Improved PLA @AC KSX 0.6mm', 'Improved PLA @AC KSX 0.8mm'],
    },
    'PLA+': {
        'ks1': 'Improved PLA+ @AC KS1 0.4mm',
        'ksx': 'Improved PLA+ @AC KSX 0.4mm',
        'ks1_sys': 'Anycubic PLA+ @Anycubic Kobra S1 0.4 nozzle',
        'ksx_sys': 'Anycubic PLA+ @Anycubic Kobra X 0.4 nozzle',
        'ksx_inherits': 'Anycubic PLA+ @Anycubic Kobra X 0.4 nozzle',
        'nozzle_delta': PLA_NOZZLE_DELTA,
        'variants': ['Improved PLA+ @AC KSX 0.25mm',
                     'Improved PLA+ @AC KSX 0.6mm', 'Improved PLA+ @AC KSX 0.8mm'],
    },
    'PETG': {
        'ks1': 'Improved PETG @AC KS1 0.4mm',
        'ksx': 'Improved PETG @AC KSX 0.4mm',
        'ks1_sys': 'Anycubic PETG @Anycubic Kobra S1 0.4 nozzle',
        'ksx_sys': 'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
        'ksx_inherits': 'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
        'nozzle_delta': PETG_NOZZLE_DELTA,
        'variants': ['Improved PETG @AC KSX 0.6mm', 'Improved PETG @AC KSX 0.8mm'],
    },
    'PETG HS': {
        'ks1': 'Improved PETG HS @AC KS1 0.4mm',
        'ksx': 'Improved PETG HS @AC KSX 0.4mm',
        'ks1_sys': 'Anycubic PETG @Anycubic Kobra S1 0.4 nozzle',
        'ksx_sys': 'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
        'ksx_inherits': 'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
        'nozzle_delta': PETG_NOZZLE_DELTA,
        'variants': ['Improved PETG HS @AC KSX 0.6mm', 'Improved PETG HS @AC KSX 0.8mm'],
    },
    'PETG Translucent': {
        'ks1': 'Improved PETG Translucent @AC KS1 0.4mm',
        'ksx': 'Improved PETG Translucent @AC KSX 0.4mm',
        'ks1_sys': 'Anycubic PETG @Anycubic Kobra S1 0.4 nozzle',
        'ksx_sys': 'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
        'ksx_inherits': 'Anycubic PETG @Anycubic Kobra X 0.4 nozzle',
        'nozzle_delta': PETG_NOZZLE_DELTA,
        'variants': ['Improved PETG Translucent @AC KSX 0.6mm',
                     'Improved PETG Translucent @AC KSX 0.8mm'],
    },
}

SKIP_ENTIRELY = IDENTITY | {
    'type','setting_id','filament_id','instantiation','filament_type',
    'bed_type','compatible_printers',
}

for mat, cfg in MATERIALS.items():
    print(f'\n{"=" * 70}')
    print(f'  Building: {cfg["ksx"]}')

    _, ks1_d = UP[cfg['ks1']]
    ksx_fpath, _ = UP[cfg['ksx']]

    new_ksx = {}
    # Process every key in KS1 Improved
    for k, raw in ks1_d.items():
        if k in SKIP_ENTIRELY:
            continue
        ks1_v = raw[0] if isinstance(raw, list) else raw

        if k in HARDWARE_ZERO:
            setkv(new_ksx, k, '0')
            continue

        if k in COPY_FROM_KS1:
            setkv(new_ksx, k, ks1_v)
            continue

        if k in PLATE_DELTA_KEYS:
            ks1_sys = resolve_sys(cfg['ks1_sys'], k, SP)
            ksx_sys = resolve_sys(cfg['ksx_sys'], k, SP)
            _, new_v = numeric_delta(ks1_v, ks1_sys, ksx_sys)
            setkv(new_ksx, k, new_v)
            if str(new_v) != str(ks1_v):
                print(f'  PLATE_DELTA {k}: {ks1_v} -> {new_v}')
            continue

        if k in FAN_DELTA_KEYS:
            ks1_sys = resolve_sys(cfg['ks1_sys'], k, SP)
            ksx_sys = resolve_sys(cfg['ksx_sys'], k, SP)
            if ks1_sys is not None and ksx_sys is not None:
                _, new_v = numeric_delta(ks1_v, ks1_sys, ksx_sys)
                setkv(new_ksx, k, new_v)
                if str(new_v) != str(ks1_v):
                    print(f'  FAN_DELTA {k}: {ks1_v} -> {new_v}')
            else:
                setkv(new_ksx, k, ks1_v)
            continue

        # Anything else not categorised: copy from KS1
        setkv(new_ksx, k, ks1_v)

    # Identity
    new_ksx['filament_settings_id'] = [cfg['ksx']]
    new_ksx['filament_vendor']      = ks1_d.get('filament_vendor', ['Generic'])
    new_ksx['from']                 = 'User'
    new_ksx['inherits']             = cfg['ksx_inherits']
    new_ksx['is_custom_defined']    = '0'
    new_ksx['name']                 = cfg['ksx']
    new_ksx['version']              = ks1_d.get('version', '1.3.2602.11')

    save_sorted(ksx_fpath, new_ksx)
    update_info(ksx_fpath, cfg['ksx'])
    print(f'  -> Written: {ksx_fpath}')

    # ── Cascade to nozzle variants ────────────────────────────────────────────
    with open(ksx_fpath, encoding='utf-8') as f:
        parent_d = json.load(f)

    for variant_name in cfg['variants']:
        if variant_name not in UP:
            print(f'    SKIP: {variant_name}')
            continue
        v_fpath, v_d = UP[variant_name]
        size = next((s for s in ('0.25mm','0.6mm','0.8mm') if variant_name.endswith(s)), None)
        if not size or size not in cfg['nozzle_delta']:
            continue
        delta = cfg['nozzle_delta'][size]
        changed = []
        for tk in TEMP_KEYS:
            pv = get(parent_d, tk)
            if pv is None: continue
            try: expected = str(int(pv) + delta)
            except: continue
            cur = get(v_d, tk)
            if str(cur) != expected:
                setkv(v_d, tk, expected)
                changed.append(f'{tk}: {cur!r} -> {expected!r}')
        if changed:
            save_sorted(v_fpath, v_d)
            update_info(v_fpath, variant_name)
            print(f'    Updated variant {variant_name}: {len(changed)} temp keys')
        else:
            print(f'    OK: {variant_name}')

print('\nDone.')
