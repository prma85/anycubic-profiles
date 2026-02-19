# Anycubic Kobra S1 Slicer Configuration - Co-Pilot Context

**Last Updated:** February 2026

---

## SYSTEM INFORMATION

### Printer Hardware

- **Model:** Anycubic Kobra S1 (Combo edition)
- **Build Plate:** 220×220×250mm
- **Nozzle:** 0.4mm brass (default) or hardened steel
- **Hot End:** Standard Anycubic (OrcaSlice compatible)
- **Extruder:** Direct-drive with pressure advance calibration
- **Bed:** PEI spring steel with magnetic base (pre-installed)
- **Environment:** Office location (quiet operation preferred)

### Software Stack

- **Slicer:** Anycubic Slicer Next (OrcaSlice-based)
- **Configuration System:** JSON-based profiles with .info metadata
- **Config Location:** `C:\Users\pandrade\AppData\Roaming\AnycubicSlicerNext\user\651589\`
- **Folders:** `filament/`, `process/`, `machine/`

### Printer Compatibility

These profiles also work with:

- Anycubic Kobra 3
- Anycubic Kobra 2
- Anycubic Kobra X

---

## DEFAULT CONFIGURATION

### ⭐ PRIMARY PROFILE: `0.20mm Quit-HQ @AC KS1`

**Why this is the default:**

- **Quiet operation:** Optimized for office use (quiet-HQ profile name)
- **High quality:** Produces detailed, visually appealing prints
- **Reasonable speed:** Not the fastest, but efficient
- **Versatile:** Works well with most filaments
- **Balanced:** Perfect sweet spot between quality and speed

**Recommended filament:** Anycubic PLA (included) or any standard PLA

**Typical print times:**

- 50mm cube: ~25 minutes
- 100mm miniature: ~1.5-2 hours
- Average functional part (50-100mm): 30-90 minutes

### Secondary Recommendations

1. **For highest quality:** `0.16mm HQ @AC KS1` or `0.12mm HQ @AC KS1`
2. **For speed:** `0.20mm SD @AC KS1` or `0.24mm General PETG`
3. **For fastest prints:** `0.28mm General PETG`
4. **For flexible parts:** `0.20mm Optimal TPU`
5. **For miniatures (<8cm):** `Miniatures (0.08mm)`

---

## FILAMENT INVENTORY OVERVIEW

### Material Summary (by type)

| Material | Count | Best Profile                                   | Notes               |
| -------- | ----- | ---------------------------------------------- | ------------------- |
| PLA      | 10+   | `0.20mm Quit-HQ` or `0.16mm Optimal`           | Standard, versatile |
| PLA+     | 5+    | `0.20mm Quit-HQ` or `0.16mm Optimal PLA+`      | Better strength     |
| PETG     | 12+   | `0.20mm General PETG` or `0.24mm General PETG` | Durable, slower     |
| PETG HS  | 2     | `0.20mm General PETG` or `0.24mm General PETG` | Higher temps        |
| TPU      | 4+    | `0.20mm Optimal TPU`                           | Flexible, slow      |
| PLA Silk | 4     | `0.16mm Optimal Silk PLA`                      | Glossy finish       |
| PLA-CF   | 1     | `0.20mm PLA-CF`                                | Use hardened nozzle |
| Other    | 3+    | Check material-specific note                   | Specialty           |

**Total filaments configured:** 40+ brands/materials

### Top Brands by Profile Count

1. **Overture** (5+ filaments) - Excellent quality, well-tested
2. **Creality** (5+ filaments) - Good value, consistent
3. **Prusament** (5+ filaments) - Premium Prusa-brand options
4. **Improved @ AC KS1** (5) - Pre-optimized for this printer
5. Others: Elegoo, Polymaker, eSun, Sovol, JustMaker, etc.

### Special Considerations

- **Abrasive materials (PLA-CF, Glass-filled PETG):** Use hardened steel nozzle to prevent wear
- **TPU:** Requires slow printing (20-40 mm/s), no bed heating needed
- **PETG:** Requires careful bed leveling, slower outer wall speeds than PLA
- **Silk finishes:** Same settings as regular PLA but produces glossy appearance

---

## PROCESS PROFILES ORGANIZATION

### By Layer Height (8 height options)

**0.08mm** - Ultra-fine detail (2 profiles)

- HQ, Optimal
- Use for: Tiny miniatures, jewelry, engravings
- Print time: ~3-4x slower than 0.20mm

**0.12mm** - Fine detail (2 profiles)

- HQ, Optimal
- Use for: Small detailed models, precision parts
- Print time: ~2-3x slower than 0.20mm

**0.16mm** - Excellent detail (5 profiles)

- HQ, Optimal, High Quality (legacy), Optimal PLA+, Optimal Silk PLA
- Use for: Action figures (8cm+), detailed prints
- Print time: ~1.5x slower than 0.20mm

**0.20mm** - Standard/Recommended (8 profiles)

- **Quit-HQ** ⭐ DEFAULT, HQ PETG, General PETG, PLA-CF, SD, Optimal TPU, Optimal TPU (variant)
- Use for: General purpose, smallest recommended for most prints
- Print time: Baseline reference

**0.24mm** - Fast Production (2 profiles - newly merged)

- General PETG (merged from Draft + General PETG), Draft @AC KS1 (legacy)
- Use for: Faster prints, larger parts
- Print time: ~0.7x slower than 0.28mm

**0.28mm** - Very Fast (2 profiles - newly merged)

- General PETG (merged from Draft + General PETG), Draft @AC KS1 (legacy)
- Use for: Fastest prints, large parts
- Print time: ~0.6x baseline (0.20mm)

### Specialized Profiles (non-layer-height based)

- **Action Figures:** 3 profiles (PLA, Quality, Speed)
- **Miniatures:** 1 profile (0.08mm, ultra-fine)
- **Tools & Home Improvements:** 1 profile (structural, durable)
- **Vase:** 2 profiles (hollow mode, spiral mode)

### Quality Level Guidance

| Level       | Definition                   | Best For                  | Speed vs Quality             |
| ----------- | ---------------------------- | ------------------------- | ---------------------------- |
| **Draft**   | Speed-focused                | Prototypes, tests         | High speed, lower quality    |
| **SD**      | Good speed                   | Functional parts          | Fast, acceptable quality     |
| **General** | Balanced (material-specific) | Default for material type | Moderate speed, good quality |
| **Optimal** | Speed + quality balance      | Most prints               | Balanced - recommended       |
| **HQ**      | Quality-focused              | Detailed prints           | Slower, high quality         |
| **Quit-HQ** | Quality + silent             | ⭐ OFFICE USE DEFAULT     | Quality + quiet noise levels |

---

## QUICK REFERENCE TABLES

### Temperature Profiles (Quick Lookup)

| Filament            | Nozzle °C | Bed °C         | Special Notes                      |
| ------------------- | --------- | -------------- | ---------------------------------- |
| **PLA (all types)** | 200-220   | 60             | Standard, room temp OK             |
| **PLA+**            | 210-230   | 60             | Hotter than PLA, better strength   |
| **PETG**            | 230-250   | 70-80          | Careful bed leveling, slow walls   |
| **PETG HS**         | 240-260   | 75-85          | Even hotter, test 5°C increments   |
| **TPU**             | 200-220   | 20-30 optional | Print 20-40 mm/s, much slower      |
| **PLA Silk**        | 200-220   | 60             | Glossy finish, same as PLA temps   |
| **PLA-CF**          | 205-225   | 60             | **Hardened steel nozzle required** |

### Nozzle Selection Guide

**Brass (default):**

- ✅ PLA, PLA+, PETG, TPU, PLA Silk
- ❌ PLA-CF, Glass-filled PETG (wears quickly)
- Cost: Low, replaceable

**Hardened Steel:**

- ✅ All materials, especially PLA-CF, Glass-filled PETG
- ✅ Extended lifespan with abrasive materials
- ⚠️ Slightly lower heat transfer (may need +5°C)
- Cost: Higher, more durable

---

## IMPORTANT SETTINGS BY FILAMENT TYPE

### PLA Printing Tips

- Direct from spool usually works
- Minimal cooling needed
- Adjust: **+5°C if having stringing, -5°C if over-extruding**
- Supports: Standard tree support works well

### PETG Printing Tips

- **CRITICAL:** Ensure bed is perfectly level
- Clean build plate with IPA between prints
- Reduce nozzle temp by 5-10°C if seeing curled edges
- **Outer wall speed:** Keep 40-60 mm/s (slower than PLA!)
- Supports: Use tree supports, slightly longer contact
- **Moisture:** Can absorb humidity; store dry

### TPU Printing Tips

- **Print MUCH slower:** 20-40 mm/s (not 60+ mm/s)
- **No bed heating needed** (actually helps prevent sticking)
- **Enable:** Avoid Crossing Walls or use `0.20mm Optimal TPU - Avoid Crossing Walls Off`
- **Supports:** Use sparingly, clean easily
- **Moisture:** Highly hygroscopic; dry 4-6 hours at 80°C if stored

### High-Speed Materials (PETG HS)

- Same as regular PETG but 10-20°C hotter
- Test temperature in 5°C increments
- More prone to stringing (increase retraction)

---

## MERGED PROFILES NOTE

**NEW (February 2026):** The following profiles have been merged for better compatibility:

1. **`0.24mm PETG`** (NEW)
   - Merged from: `0.24mm Draft @AC KS1` + `0.24mm General PETG`
   - Combines: Quality focus of General PETG with pragmatic speed of Draft
   - Compatible with: All Kobra S1 variants (including Hardened Steel)
   - Replaces: Use instead of Draft @AC KS1 for better results

2. **`0.28mm PETG`** (NEW)
   - Merged from: `0.28mm Draft @AC KS1` + `0.28mm General PETG`
   - Combines: Quality focus of General PETG with speed of Draft
   - Compatible with: All Kobra S1 variants (including Hardened Steel)
   - Replaces: Use instead of Draft @AC KS1 for better results

**Why merged?** The Draft profiles are simpler/faster but less detailed. The General PETG profiles are optimized but verbose. The merged versions provide the best of both: complete configuration with balanced speed/quality trade-off.

**Legacy profiles still exist** but consider using the new unified PETG profiles instead.

---

## COMMON TASKS & QUICK SOLUTIONS

### "I want to print a new filament"

1. Check filament folder README by material type
2. Find your brand/type in categorization
3. Select from process folder: `0.20mm Quit-HQ` (default) or appropriate layer height
4. Test on small print first
5. Adjust nozzle temp ±5°C if needed

### "Prints are coming out fuzzy/stringing"

- Temperature too high by 5-10°C
- Try: Reduce nozzle temp by 5°C
- Alternative: Increase retraction (check specific profile)

### "First layer not sticking"

- Bed level likely off
- Clean bed with IPA (isopropyl alcohol)
- If PETG: Ensure bed is 70-80°C (not 60°C like PLA)
- Re-bed level using calibration print

### "Edges curling on large PETG prints"

- Normal PETG behavior; nozzle too hot
- Try: Reduce nozzle by 10°C
- Use: Brim on base or lower bed temp by 5°C
- Profile: Use `0.20mm Quit-HQ` for quieter operation

### "Need fastest print possible"

- Use: `0.28mm General PETG` with PETG filament
- Alternative: `0.24mm General PETG`
- Note: Quality will be acceptable but visible layers

### "Need highest quality/detail"

- Use: `0.12mm HQ` or `0.08mm HQ`
- Expect: 2-3x longer print time
- Best with: PLA or PLA+ (simpler than PETG)

### "Flexible part failing"

- Material: Use TPU only
- Profile: `0.20mm Optimal TPU`
- Speed: Drop further if needed (20-30 mm/s)
- Bed: Ensure no heating (room temp OK)

### "Adding new filament brand"

1. Create: `Brand Material.json` + `Brand Material.info`
2. Copy from similar filament (same material type)
3. Update: Nozzle/bed temps per manufacturer specs
4. Update: Brand/material in filament README.md
5. Test: Small print before production

---

## PRINTER CALIBRATION NOTES

### Bed Leveling (Critical!)

- Perform every 5-10 prints or if adhesion issues
- Use: Paper method or printer's auto-level if available
- Corners: Check all 4 + center
- Importance: More critical for PETG than PLA

### Pressure Advance (Already calibrated)

- PLA: ~0.03 (per filament profiles)
- PETG: ~0.04-0.05 (material dependent)
- Adjustable in: Individual filament .json files
- Purpose: Prevents under/over-extrusion at direction changes

### Nozzle Cleanliness

- Clean after every 3-5 prints or if oozing
- Method: Brass brush during heating, or cold pull when cool
- Prevent: Moisture in filament (store dry)

### Bed Adhesion Maintenance

- Clean with: IPA (isopropyl alcohol) on lint-free cloth
- Frequency: Every 3-5 prints
- Don't: Use soap/water (leaves residue)
- Bed wear: Self-leveling PEI spring steel; replace if worn

---

## FILE STRUCTURE OVERVIEW

```
651589/
├── README.md (Main guide - START HERE)
├── filament/
│   ├── README.md (Filament categorization by brand/material)
│   ├── *.json (40+ filament profiles)
│   ├── *.info (Metadata for each)
│   └── base/ (Base filament profiles)
├── process/
│   ├── *.json (45+ process profiles by layer height)
│   ├── *.info (Metadata for each)
│   ├── base/ (Base process profiles)
│   └── [NEW] 0.24mm PETG.* & 0.28mm PETG.* (Merged profiles)
├── machine/
│   ├── *.json (Nozzle/hotend configurations)
│   ├── *.info (Metadata)
│   └── base/ (Base machine profiles)
└── .git/ (Version control)
```

---

## COMMON MODIFICATIONS

### "I want to print faster"

**Adjust in process profile (.json):**

- Reduce `layer_height` (go from 0.20 to 0.24 or 0.28)
- Increase `outer_wall_speed`, `inner_wall_speed`, `sparse_infill_speed` by 10-20%
- Increase `travel_speed` (currently 400, max ~600)

### "I want better quality"

**Adjust in process profile (.json):**

- Increase `layer_height` (0.20 to 0.16, or 0.16 to 0.12)
- Decrease wall speeds by 10-20%
- Increase `top_shell_layers` and `bottom_shell_layers`
- Use wall generator `arachne` (more expensive, better walls)

### "My print is warping"

**For PETG specifically:**

- Reduce nozzle temp by 10°C
- Lower bed temp by 5°C
- Add brim to base
- Ensure bed is level

### "Need new material temperature"

**Update in filament profile (.json):**

- Find section with `temperature` or `filament_*_temperature`
- Note: Some values have `[0]` notation for multi-filament support
- Test in 5°C increments on small print

---

## FIRMWARE & VERSION INFO

- **Slicer Version:** Anycubic Slicer Next (OrcaSlice-based)
- **Profile Versions:** 1.3.2503.03 to 2.3.0.03 (work together fine)
- **JSON Format:** OrcaSlice-compatible
- **Last Config Update:** February 2026

---

## CONTACT/SUPPORT NOTES

- **Printer:** Anycubic Kobra S1 Combo
- **Nozzle:** 0.4mm (brass primary, hardened steel backup)
- **Configuration Owner:** Personal office setup
- **Maintenance:** Regular bed leveling, PEI plate cleaning
- **Filament Storage:** Dry boxes with desiccant (critical for PETG/TPU)

---

## QUICK DECISION TREE

```
START: I have a 3D model to print

Q1: Do you know the filament material?
├─ YES → Go to filament folder README, find your material type
├─ NO → Check physical filament spool for type (usually says PLA, PETG, etc.)

Q2: What's your priority?
├─ Quality → Use 0.16mm HQ or 0.12mm HQ (slower, beautiful results)
├─ Balance → Use 0.20mm Quit-HQ (DEFAULT - quality + quiet + speed)
├─ Speed → Use 0.24mm PETG or 0.28mm PETG (faster, still good quality)
├─ Flexible → Use 0.20mm Optimal TPU (if material is TPU)
├─ Miniatures → Use Miniatures 0.08mm or 0.12mm HQ (very detailed)

Q3: Do you have the filament configured?
├─ YES → Select filament, process, machine in slicer → SLICE → PRINT
├─ NO → Check filament folder for your brand → Add if missing

Q4: Is print quality acceptable?
├─ YES → You're done! Save settings for next time
├─ NO → Check Common Tasks section for issue (stranging, warping, etc.)
```

---

## NOTES FOR FUTURE UPGRADES

- All profiles are OrcaSlice-compatible
- New materials/brands can be added by copying + modifying existing profiles
- Configuration is version-controlled (git repo included)
- Profiles support multi-material printing (future expansion possible)
- Consider adding: PEEK, ASA, ABS, Nylon profiles as needed
- Machine compatibility: Profiles work across Kobra S1/2/3/X family
