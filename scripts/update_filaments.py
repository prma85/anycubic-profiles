#!/usr/bin/env python3
"""
Comprehensive filament profile updater.

Pass 1 — root profiles (inherit from system):
  - cool_plate_temp: PETG→50, PLA initial_layer→40
  - MVS: KSX from reference table; KS1 corrected when clearly wrong

Pass 2 — nozzle variants (inherit from user 0.4mm):
  - MVS: recalculate from updated root using canonical scaling
         0.25mm: ×0.50 (cap at 3), 0.6mm: ×1.25, 0.8mm: ×1.50

Pass 3 — all profiles:
  - Format simplification: remove type/setting_id/filament_id/instantiation/bed_type
  - Remove keys that exactly match parent value
  - Sort alphabetically (content first, identity last)

Also: create EconoFil KSX profiles, fix cross-printer compat_printers
"""

import json, os, glob, sys
from datetime import datetime

REPO = "C:/Users/pandrade/AppData/Roaming/AnycubicSlicerNext/user/651589"
SYS  = "C:/Users/pandrade/AppData/Roaming/AnycubicSlicerNext/system/Anycubic/filament"
FILAMENT_DIR = f"{REPO}/filament"

IDENTITY_KEYS = {
    "filament_settings_id", "filament_vendor", "from",
    "inherits", "is_custom_defined", "name", "version",
}
DROP_ALWAYS = {
    "type", "setting_id", "filament_id", "instantiation",
    "filament_type", "bed_type", "filament_load_time", "filament_unload_time",
}

# ── MVS reference table [KSX, KS1] ──────────────────────────────────────────
MVS_TABLE = {
    "rapid_pla":        [23, 27],
    "rapid_plaplus":    [20, 24],
    "standard_pla":     [13, 16],
    "standard_plaplus": [16, 19],
    "pla_matte":        [14, 16],
    "translucent_pla":  [15, 17],
    "pla_silk":         [10, 12],
    "pla_galaxy":       [13, 15],
    "pla_glow":         [13, 15],
    "pla_cf":           [16, 19],
    "rapid_petg":       [18, 21],
    "standard_petg":    [13, 15],
    "translucent_petg": [11, 13],
    "petg_gf":          [11, 13],
    "petg_cf":          [12, 14],
    "tpu_standard":     [ 4,  5],
    "tpu_hs":           [ 8, 10],
}

NOZZLE_SCALE = {
    "0.25": 0.50,
    "0.6":  1.25,
    "0.8":  1.50,
}


def classify(name):
    """Return (category, printer) for a root profile name. None/None if unknown."""
    n = name.lower()
    if "@ac ksx" in n:
        printer = "KSX"
    elif "@ac ks1" in n:
        printer = "KS1"
    else:
        return None, None

    if any(x in n for x in ["rapid petg","petg hs","petg high speed","petg hf","tecbears rapid petg","improved petg hs"]):
        return "rapid_petg", printer
    if any(x in n for x in ["translucent petg","petg translucent"]):
        return "translucent_petg", printer
    if any(x in n for x in ["petg gf","petg glass","justmaker petg"]):
        return "petg_gf", printer
    if any(x in n for x in ["petg cf","petg carbon"]):
        return "petg_cf", printer
    if "petg" in n:
        return "standard_petg", printer
    if any(x in n for x in ["rapid pla+","pla+ 2.0","rapid pla +"]):
        return "rapid_plaplus", printer
    if any(x in n for x in ["pla cf","pla-cf"]):
        return "pla_cf", printer
    if any(x in n for x in ["silk dual","silk pla","pla silk"]):
        return "pla_silk", printer
    if any(x in n for x in ["matte pla","pla matte"]):
        return "pla_matte", printer
    if any(x in n for x in ["pla galaxy","galaxy pla","glitter","hyper pla galaxy"]):
        return "pla_galaxy", printer
    if any(x in n for x in ["pla glow","glow pla","glow in","polychrome glow"]):
        return "pla_glow", printer
    if any(x in n for x in ["translucent pla","pla translucent"]):
        return "translucent_pla", printer
    if any(x in n for x in ["pla metal","metal pla"]):
        return "pla_silk", printer
    if any(x in n for x in ["pla pro","pla+","plaplus"]):
        return "standard_plaplus", printer
    if "pla" in n:
        return "standard_pla", printer
    if any(x in n for x in ["tpu hs","tpu high speed","high speed tpu"]):
        return "tpu_hs", printer
    if "tpu" in n:
        return "tpu_standard", printer
    return None, printer


def nozzle_size_from_name(name):
    """Extract nozzle size string from profile name: '0.25', '0.4', '0.6', '0.8'."""
    for s in ["0.25mm", "0.4mm", "0.6mm", "0.8mm"]:
        if s in name:
            return s[:-2]  # strip 'mm'
    return None


def load_profiles(directory):
    """Load all JSON profiles from directory. Returns {name: (path, dict)}."""
    result = {}
    for fpath in sorted(glob.glob(f"{directory}/*.json")):
        with open(fpath, encoding="utf-8") as f:
            try:
                d = json.load(f)
            except Exception as e:
                print(f"  PARSE ERROR {os.path.basename(fpath)}: {e}", file=sys.stderr)
                continue
        name = d.get("name", os.path.basename(fpath).replace(".json",""))
        result[name] = (fpath, d)
    return result


def write_json(path, d):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, indent=4, ensure_ascii=False)
        f.write("\n")


def write_info(path, profile_name, sync="update"):
    info_path = path.replace(".json", ".info")
    existing = {}
    if os.path.exists(info_path):
        with open(info_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if " = " in line:
                    k, v = line.split(" = ", 1)
                    existing[k.strip()] = v.strip()
    existing["sync_info"] = sync
    existing.setdefault("user_id", "")
    existing["setting_id"] = profile_name
    with open(info_path, "w", encoding="utf-8", newline="\n") as f:
        for k, v in existing.items():
            f.write(f"{k} = {v}\n")


def simplify(d, system_parents, user_profiles_dict):
    """Return simplified dict (drop redundant/always-drop keys) and change list."""
    inherits = d.get("inherits", "")
    parent = system_parents.get(inherits)
    if parent is None:
        entry = user_profiles_dict.get(inherits)
        if entry:
            _, parent = entry

    new = {}
    changes = []

    for key, val in d.items():
        if key in DROP_ALWAYS:
            changes.append(f"  - REMOVE `{key}` = {json.dumps(val)} (header field)")
            continue
        if key in IDENTITY_KEYS:
            new[key] = val
            continue
        if parent and key in parent and parent[key] == val:
            changes.append(f"  - REMOVE `{key}` (matches parent: {json.dumps(val)})")
            continue
        new[key] = val

    # Sort: content keys alpha, then identity keys alpha
    content_keys = sorted(k for k in new if k not in IDENTITY_KEYS)
    identity_keys = sorted(k for k in new if k in IDENTITY_KEYS)
    ordered = {k: new[k] for k in content_keys + identity_keys}
    return ordered, changes


def apply_cool_plate(d, changes):
    """Fix cool_plate_temp for PETG (→50) and PLA initial_layer (→40)."""
    inherits = d.get("inherits", "")
    name = d.get("name", "")
    n = (name + " " + inherits).lower()

    is_petg = "petg" in n
    is_pla = not is_petg and "pla" in n

    if is_petg:
        for key in ("cool_plate_temp", "cool_plate_temp_initial_layer"):
            cur = d.get(key, [None])[0]
            if cur != "50":
                changes.append(f"  - SET `{key}` {cur!r} → '50'")
                d[key] = ["50"]

    elif is_pla:
        key = "cool_plate_temp_initial_layer"
        cur = d.get(key, [None])[0]
        if cur is not None and cur != "40":
            changes.append(f"  - SET `{key}` {cur!r} → '40'")
            d[key] = ["40"]
        elif cur is None:
            # Explicit set only if parent has wrong value (35)
            # Check if parent has 35
            parent_cpt = None
            inh = d.get("inherits","")
            sys_parent = system_parents.get(inh)
            if sys_parent:
                parent_cpt = sys_parent.get(key, [None])[0]
            if parent_cpt not in (None, "40"):
                changes.append(f"  - ADD `{key}` → '40' (parent has {parent_cpt!r})")
                d[key] = ["40"]


def apply_mvs_root(d, changes):
    """Update MVS in root profiles using reference table."""
    name = d.get("name", "")
    cat, printer = classify(name)
    if cat is None:
        return

    target = MVS_TABLE[cat][0 if printer == "KSX" else 1]
    cur = d.get("filament_max_volumetric_speed", [None])[0]
    cur_val = float(cur) if cur else None

    if printer == "KSX":
        # KSX: always apply table (not previously calibrated)
        if cur_val is None or abs(cur_val - target) > 0.5:
            changes.append(f"  - SET `filament_max_volumetric_speed` {cur!r} → '{target}' (KSX reference table)")
            d["filament_max_volumetric_speed"] = [str(target)]

    else:  # KS1: only update if clearly wrong
        if cur_val is None:
            changes.append(f"  - SET `filament_max_volumetric_speed` None → '{target}' (no existing override)")
            d["filament_max_volumetric_speed"] = [str(target)]
        elif cur_val < target * 0.65:
            changes.append(f"  - CORRECT `filament_max_volumetric_speed` {cur!r} → '{target}' (was < 65% of table reference {target})")
            d["filament_max_volumetric_speed"] = [str(target)]


def apply_mvs_variant(d, user_profiles_dict, changes):
    """Recalculate MVS for nozzle variants from their 0.4mm parent."""
    name = d.get("name", "")
    size = nozzle_size_from_name(name)
    if size not in NOZZLE_SCALE:
        return

    parent_name = d.get("inherits", "")
    if parent_name not in user_profiles_dict:
        return

    _, parent_d = user_profiles_dict[parent_name]
    parent_mvs_raw = parent_d.get("filament_max_volumetric_speed", [None])[0]
    if parent_mvs_raw is None:
        return

    parent_mvs = float(parent_mvs_raw)
    scale = NOZZLE_SCALE[size]
    target_raw = parent_mvs * scale
    target = round(target_raw, 1) if target_raw > 3 else 3  # 0.25mm cap at 3

    cur = d.get("filament_max_volumetric_speed", [None])[0]
    cur_val = float(cur) if cur else None

    if cur_val is None or abs(cur_val - target) > 0.5:
        changes.append(f"  - RECALC `filament_max_volumetric_speed` {cur!r} → '{target}' ({parent_mvs}×{scale})")
        d["filament_max_volumetric_speed"] = [str(target)]


def fix_explicit_wrong_cool_plate(d, changes):
    """Fix explicit wrong cool_plate_temp values in ANY profile (including variants)."""
    name = d.get("name", "")
    n = name.lower()
    is_petg = "petg" in n

    for key in ("cool_plate_temp", "cool_plate_temp_initial_layer"):
        cur = d.get(key, [None])[0]
        if cur is None:
            continue
        if is_petg and cur not in ("50", "0"):  # 0 means "not applicable"
            changes.append(f"  - FIX `{key}` {cur!r} → '50' (PETG wrong value)")
            d[key] = ["50"]
        elif not is_petg and cur == "35" and key == "cool_plate_temp_initial_layer":
            changes.append(f"  - FIX `{key}` '35' → '40' (PLA explicit wrong value)")
            d[key] = ["40"]


# ── EconoFil KSX creation ────────────────────────────────────────────────────
def create_econofil_ksx(user_profiles_dict, log):
    ks1_entry = user_profiles_dict.get("EconoFil PLA @AC KS1 0.4mm")
    if not ks1_entry:
        return
    _, ks1 = ks1_entry

    # 0.4mm KSX
    name_04 = "EconoFil PLA @AC KSX 0.4mm"
    path_04 = f"{FILAMENT_DIR}/EconoFil PLA @AC KSX 0.4mm.json"
    if not os.path.exists(path_04):
        # Build from KS1, adjust MVS for KSX (standard_pla = 13)
        cat, _ = classify(name_04)
        target_mvs = MVS_TABLE.get(cat or "standard_pla", [13,16])[0]
        d = {
            "cool_plate_temp_initial_layer": ["40"],
            "filament_cost": ks1.get("filament_cost", ["16"]),
            "filament_deretraction_speed": ks1.get("filament_deretraction_speed", ["0"]),
            "filament_max_volumetric_speed": [str(target_mvs)],
            "filament_retract_lift_below": ks1.get("filament_retract_lift_below", ["249"]),
            "filament_retract_restart_extra": ["0"],
            "filament_retract_when_changing_layer": ["1"],
            "filament_retraction_length": ks1.get("filament_retraction_length", ["0.8"]),
            "filament_retraction_minimum_travel": ks1.get("filament_retraction_minimum_travel", ["1"]),
            "filament_retraction_speed": ks1.get("filament_retraction_speed", ["40"]),
            "filament_wipe": ["1"],
            "filament_wipe_distance": ["1"],
            "filament_z_hop": ["0.4"],
            "hot_plate_temp": ks1.get("hot_plate_temp", ["60"]),
            "hot_plate_temp_initial_layer": ks1.get("hot_plate_temp_initial_layer", ["60"]),
            "nozzle_temperature": ks1.get("nozzle_temperature", ["200"]),
            "nozzle_temperature_BRASS": ks1.get("nozzle_temperature_BRASS", ["200"]),
            "nozzle_temperature_HS": ks1.get("nozzle_temperature_HS", ["205"]),
            "nozzle_temperature_initial_layer": ks1.get("nozzle_temperature_initial_layer", ["210"]),
            "nozzle_temperature_initial_layer_BRASS": ks1.get("nozzle_temperature_initial_layer_BRASS", ["210"]),
            "nozzle_temperature_initial_layer_HS": ks1.get("nozzle_temperature_initial_layer_HS", ["205"]),
            "nozzle_temperature_range_high": ks1.get("nozzle_temperature_range_high", ["210"]),
            "textured_plate_temp": ks1.get("textured_plate_temp", ["65"]),
            "textured_plate_temp_initial_layer": ks1.get("textured_plate_temp_initial_layer", ["65"]),
            "filament_settings_id": [name_04],
            "filament_vendor": ["Generic"],
            "from": "User",
            "inherits": "Anycubic PLA @Anycubic Kobra X 0.4 nozzle",
            "is_custom_defined": "0",
            "name": name_04,
            "version": "1.3.2602.11",
        }
        write_json(path_04, d)
        write_info(path_04, name_04, "create")
        log.append(f"\n### NEW: {name_04}")
        log.append(f"  Created KSX 0.4mm variant, MVS={target_mvs}, inherits Anycubic PLA @Anycubic Kobra X 0.4 nozzle")

    # Nozzle variants
    pa_base = float(ks1.get("pressure_advance", ["0.035"])[0]) if "pressure_advance" in ks1 else 0.035
    flow_base = float(ks1.get("filament_flow_ratio", ["0.98"])[0]) if "filament_flow_ratio" in ks1 else 0.98
    base_mvs = MVS_TABLE["standard_pla"][0]  # KSX

    nozzle_map = {
        "0.25mm": {
            "compat": ["Anycubic Kobra X 0.25 nozzle", "Anycubic Kobra X 0.25 nozzle - Brass",
                       "Anycubic Kobra X 0.25 nozzle - Hardened Steel"],
            "mvs": str(3),
            "pa": round(pa_base * 1.5, 3),
            "flow": round(flow_base + 0.01, 4),
        },
        "0.6mm": {
            "compat": ["Anycubic Kobra X 0.6 nozzle", "Anycubic Kobra X 0.6 nozzle - Brass",
                       "Anycubic Kobra X 0.6 nozzle - Hardened Steel"],
            "mvs": str(round(base_mvs * 1.25, 1)),
            "pa": round(pa_base * 0.667, 3),
            "flow": round(flow_base - 0.01, 4),
        },
        "0.8mm": {
            "compat": ["Anycubic Kobra X 0.8 nozzle", "Anycubic Kobra X 0.8 nozzle - Brass",
                       "Anycubic Kobra X 0.8 nozzle - Hardened Steel"],
            "mvs": str(round(base_mvs * 1.5, 1)),
            "pa": round(pa_base * 0.333, 3),
            "flow": round(flow_base - 0.02, 4),
        },
    }

    for size_key, info in nozzle_map.items():
        vname = f"EconoFil PLA @AC KSX {size_key}"
        vpath = f"{FILAMENT_DIR}/{vname}.json"
        if not os.path.exists(vpath):
            vd = {
                "compatible_printers": info["compat"],
                "filament_flow_ratio": [str(info["flow"])],
                "filament_max_volumetric_speed": [info["mvs"]],
                "pressure_advance": [str(info["pa"])],
                "filament_settings_id": [vname],
                "filament_vendor": ["Generic"],
                "from": "User",
                "inherits": name_04,
                "is_custom_defined": "0",
                "name": vname,
                "version": "1.3.2602.11",
            }
            write_json(vpath, vd)
            write_info(vpath, vname, "create")
            log.append(f"\n### NEW: {vname}")
            log.append(f"  Created nozzle variant MVS={info['mvs']}, PA={info['pa']}, flow={info['flow']}")


# ── Cross-printer compat fix ─────────────────────────────────────────────────
def fix_cross_printer(user_profiles_dict, log):
    fixes = {
        "EconoFil PLA @AC KS1 0.4mm": "Kobra X",
        "Elegoo Rapid PETG @AC KS1 0.4mm": "Kobra X",
    }
    for profile_name, remove_str in fixes.items():
        entry = user_profiles_dict.get(profile_name)
        if not entry:
            continue
        fpath, d = entry
        compat = d.get("compatible_printers", [])
        new_compat = [c for c in compat if remove_str not in c]
        if new_compat != compat:
            d["compatible_printers"] = new_compat
            log.append(f"\n### EDIT: {profile_name}")
            log.append(f"  - REMOVE '{remove_str}' from compatible_printers")
            log.append(f"    Before: {compat}")
            log.append(f"    After:  {new_compat}")
            write_json(fpath, d)
            write_info(fpath, profile_name)


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    global system_parents  # needed by apply_cool_plate
    system_parents = load_profiles(SYS)
    # system_parents dict: name → (path, dict)  but we just want name→dict
    system_parents = {name: d for name, (_, d) in load_profiles(SYS).items()}
    # Actually load_profiles returns (path, dict) tuples so fix that:
    sys_raw = {}
    for fpath in sorted(glob.glob(f"{SYS}/*.json")):
        with open(fpath, encoding="utf-8") as f:
            try:
                d = json.load(f)
            except:
                continue
        name = d.get("name","")
        sys_raw[name] = d
    system_parents = sys_raw

    user_profiles = load_profiles(FILAMENT_DIR)

    log = [f"# Filament Profile Changes — {datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]

    # ── Phase 0: fix cross-printer compat ────────────────────────────────────
    log.append("## Phase 0: Cross-printer compat_printers fixes")
    fix_cross_printer(user_profiles, log)

    # ── Phase 0b: create EconoFil KSX ────────────────────────────────────────
    log.append("\n## Phase 0b: Create EconoFil KSX profiles")
    create_econofil_ksx(user_profiles, log)

    # Reload after new files
    user_profiles = load_profiles(FILAMENT_DIR)

    # ── Phase 1: root profiles ────────────────────────────────────────────────
    log.append("\n## Phase 1: Root profile fixes (cool_plate + MVS)")
    for name, (fpath, d) in sorted(user_profiles.items()):
        inherits = d.get("inherits", "")
        if inherits not in system_parents:
            continue  # not a root profile
        changes = []
        apply_cool_plate(d, changes)
        apply_mvs_root(d, changes)
        if changes:
            log.append(f"\n### {name}")
            log.extend(changes)
            write_json(fpath, d)
            write_info(fpath, name)

    # Reload to pick up Phase 1 changes
    user_profiles = load_profiles(FILAMENT_DIR)

    # ── Phase 2: nozzle variants MVS + explicit cool_plate fixes ─────────────
    log.append("\n## Phase 2: Nozzle variant MVS recalculation + explicit cool_plate fixes")
    for name, (fpath, d) in sorted(user_profiles.items()):
        inherits = d.get("inherits", "")
        if inherits in system_parents:
            continue  # root profile, already done
        changes = []
        size = nozzle_size_from_name(name)
        if size in NOZZLE_SCALE:
            apply_mvs_variant(d, user_profiles, changes)
        fix_explicit_wrong_cool_plate(d, changes)
        if changes:
            log.append(f"\n### {name}")
            log.extend(changes)
            write_json(fpath, d)
            write_info(fpath, name)

    # Reload again after Phase 2
    user_profiles = load_profiles(FILAMENT_DIR)

    # ── Phase 3: format simplification of ALL profiles ────────────────────────
    log.append("\n## Phase 3: Format simplification (remove redundant/header keys)")
    for name, (fpath, d) in sorted(user_profiles.items()):
        simplified, changes = simplify(d, system_parents, user_profiles)
        if changes:
            log.append(f"\n### {name}")
            log.extend(changes)
            write_json(fpath, simplified)
            write_info(fpath, name)

    # ── Write change log ──────────────────────────────────────────────────────
    log_path = f"{REPO}/CHANGES.md"
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(log) + "\n")

    print(f"Done. {len(user_profiles)} profiles processed. See CHANGES.md")


if __name__ == "__main__":
    main()
