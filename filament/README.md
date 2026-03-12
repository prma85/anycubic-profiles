# Filament Configuration Guide - Multi-Nozzle Strategy (v2.0)

**Last Updated:** March 2026  
**Framework:** Anycubic Slicer Next (OrcaSlicer-based)  
**Scope:** Custom filament profiles for Anycubic Kobra S1 + Kobra X with multiple nozzle sizes

---

## Table of Contents

1. [What Changed: Migration Overview](#what-changed-migration-overview)
2. [Profile Variants & Nozzle Sizes](#profile-variants--nozzle-sizes)
3. [Filament Inventory by Printer & Nozzle](#filament-inventory-by-printer--nozzle)
4. [Generation Rules & Inheritance Strategy](#generation-rules--inheritance-strategy)
5. [Main Differences Between Variants](#main-differences-between-variants)
6. [Editing Workflow Reminder](#editing-workflow-reminder)
7. [How to Update Values](#how-to-update-values)
8. [Quick Reference: Selection Guide](#quick-reference-selection-guide)

---

## What Changed: Migration Overview

### March 2026 Correction Update (v2.1)

After validating real-world UI behavior, the variant architecture was corrected with stricter rules:

- `@AC KS1 0.6mm` is now rebuilt as a full clone of `@AC KS1 Base` (no missing fields), then nozzle deltas are applied.
- `@AC KS1 0.8mm` is rebuilt from `@AC KS1 0.6mm` using 0.6->0.8 deltas.
- `@AC KS1 0.25mm` is rebuilt from `@AC KS1 Base` using system 0.25 values only when lower.
- `@AC KSX 0.4mm` inherits from `@AC KS1 Base`.
- `@AC KSX 0.6mm`, `@AC KSX 0.8mm`, `@AC KSX 0.25mm` inherit from corresponding KS1 variants.
- Filament `.info` files are plain key-value with `sync_info = create` and `setting_id` aligned to `filament_settings_id`.

### March 2026 Rule Hardening (v2.2)

Authoritative generation behavior now enforced in files:

- Deltas are applied per filament type and per printer context, not globally.
- KS1 delta derivation uses system `Kobra S1` with fallback/blending from `Kobra S1 Max` when needed.
- KSX deltas are derived from `Kobra X` system profiles.
- `filament_flow_ratio` and `pressure_advance` are changed only according to system-observed transition deltas for that type/printer.
- `fan_max_speed_*` and `fan_min_speed_*` are changed only when system transition for that type/printer shows change.
- `filament_change_length` is only added/preserved when the corresponding system transition includes it.
- `nozzle_temperature_range_high` is always present on generated 0.6/0.8 variants.
- Safety constraint is enforced: `nozzle_temperature_initial_layer_HS <= nozzle_temperature_range_high`.

### March 2026 Override-Minimization Cleanup (v2.3)

Custom profiles are maintained as minimal overlays:

- For each profile, keys identical to inherited effective values are removed.
- Keys that differ from inherited effective values are preserved.
- `version` is always retained, even if equal to parent.
- 0.4 base profiles remain source-of-truth overlays, not full copies of parent data.
- HS derivation rule: `+5` is only for `nozzle_temperature_HS` and `nozzle_temperature_initial_layer_HS` when deriving from generic/BRASS values.
- No `+5` derivation is applied to `nozzle_temperature_range_low` or `nozzle_temperature_range_high`.

### The Problem We Solved

Previously, all filament profiles were calibrated for **Kobra S1 with 0.4mm brass nozzle only**. This created friction when using:
- **Different nozzle sizes** (0.25mm for detail, 0.6mm for speed, 0.8mm for thick layers)
- **Kobra X printer** (similar but different thermal/pressure characteristics)

### The Solution: Multi-Nozzle Profile Variants

We've generated scientifically-calibrated variants for **three additional nozzle sizes**:
- **0.25mm** (fine detail, small features)
- **0.6mm** (balanced speed & quality)
- **0.8mm** (thick layers, structural parts)

Each nozzle size exists for **both printer models**:
- **KS1 variants** = Anycubic Kobra S1 optimized
- **KSX variants** = Anycubic Kobra X optimized

### Variant Naming Convention

```
[Material] @AC [Printer] [Nozzle Size]

Examples:
  - Creality PLA @AC KS1 Base                     (0.4mm, S1 - source of truth)
  - Creality PLA @AC KS1 0.6mm                    (0.6mm, S1 - inherits from Base)
  - Creality PLA @AC KSX 0.6mm                    (0.6mm, X - inherits from KS1 0.6mm)
  - Creality PLA @AC KS1 0.25mm                   (0.25mm, S1)
  - Creality PLA @AC KSX 0.25mm                   (0.25mm, X)
```

Profiles without a size suffix (ending in `@AC KS1 Base`) are the **0.4mm brass nozzle originals** that serve as inheritance sources.

---

## Profile Variants & Nozzle Sizes

### Nozzle Size Target Matrix

| Size | Filament Count | Best For | Printer | Status |
|------|---|---|---|---|
| **0.4mm** (Base) | 52 profiles | General purpose, detail | Both | ✓ Original |
| **0.6mm** | 52 profiles | Speed, quality, production | Both | ✓ Rebuilt (v2.1) |
| **0.25mm** | 45 profiles | Fine details, miniatures | Both | ✓ Rebuilt (v2.1) |
| **0.8mm** | 51 profiles | Fast prototype, structural | Both | ✓ Rebuilt (v2.1) |
| **1.0mm** | Planned | Heavy layers, rapid draft | Both | ⏳ Future |

### Coverage by Nozzle Size

#### 0.4mm Base (Original - 52 Profiles)
Source of truth for custom calibration. All materials available.

**Material families:**
- PLA (10 variants: standard, silk, galaxy, stone, etc.)
- PLA+ (7 variants)
- PETG (14 variants: standard, transparent, matte, glass-filled, etc.)
- TPU (3 variants)
- ASA (5 variants)
- ABS (6 variants)
- Nylon (3 variants)
- Specialty (4 variants: resin-filled, composite, etc.)

#### 0.6mm (52 Profiles) ✓ Recommended for Speed
**Physics basis:** Larger orifice = higher flow rates + lower pressure advance (thicker extrusion beads, less drag-induced wave patterns)

**Materials included:**
- ABS (5) + ASA (5) = **10 engineering plastics**
- PLA (7) + PLA+ (2) = **9 general purpose**
- PETG (14) = **flexible options including GF, CF, transparent**
- TPU (3) = **flexible materials**
- Specialty (2) = **Nylon, composite**

**Key profile characteristics:**
- Full base clone first, then targeted overrides.
- Numeric changes are applied only when the matching system transition for that filament type/printer shows a change.
- Temperature keys are kept safety-consistent (`_BRASS`, `_HS`, and bounded initial layer values).

#### 0.25mm (45 Profiles) ⏳ Fine Detail Mode
**Physics basis:** Tiny orifice = ultra-precise extrusion, high pressure advance (detects minute vibrations)

**Materials included (conservative selection):**
- PLA (10 variants)
- PLA+ (7 variants)
- PETG (12 variants) - standard, resin, glass/carbon-filled included
- **NOT included:** TPU, ASA, ABS (these are too stiff for 0.25mm, risk clogs)

**Key profile characteristics:**
- Nozzle temp: -10-20°C lower than 0.4mm (smaller mass = faster cooling)
- Pressure advance: +50-100% higher (micro-vibrations pronounced)
- Layer height: Limited to 0.10-0.15mm for quality
- Print speed: 50-60% of 0.4mm (precision over speed)

#### 0.8mm (51 Profiles) ⚡ Fast Prototyping
**Physics basis:** Large orifice = minimal extrusion precision, lower melting temps needed

**Materials included:**
- PLA (10 variants)
- PLA+ (7 variants)
- PETG (12 variants) - includes glass-filled for durability
- **NOT included:** TPU, ASA, ABS (engineering plastics need precision)

**Key profile characteristics:**
- Nozzle temp: ~same as system baseline (large mass dissipates heat efficiently)
- Pressure advance: 30-40% of 0.4mm (bead width dominates flow regulation)
- Layer height: Optimized for 0.4-0.6mm (thick, uniform beads)
- Print speed: 120-150% of 0.4mm (bead width allows fast deposition)

---

## Filament Inventory by Printer & Nozzle

### Quick Lookup Table

Use this to find exactly which profiles exist for your printer + nozzle combination.

#### Anycubic Kobra S1 (KS1)

| Material | 0.25mm | 0.4mm | 0.6mm | 0.8mm | Total | Notes |
|---|:---:|:---:|:---:|:---:|---:|---|
| **PLA Family** | ✓ | ✓ | ✓ | ✓ | 10 | All PLA variants covered |
| **PLA+** | ✓ | ✓ | ✓ | ✓ | 7 | iBoss, Elegoo, Sunlu, Creality, Overture, UJOYBIO, Improved |
| **PETG** | ✓ | ✓ | ✓ | ✓ | 14 | Includes transparent, GF, CF variants |
| **TPU** | ✗ | ✓ | ✓ | ✗ | 3 | 0.25mm too small, 0.8mm too coarse |
| **ABS** | ✗ | ✓ | ✓ | ✗ | 6 | Needs precision; not for extremes |
| **ASA** | ✗ | ✓ | ✓ | ✗ | 5 | Engineering plastic; requires precision |
| **Nylon** | ✗ | ✓ | ✓ | ✗ | 3 | Abrasive; hardened steel needed |
| **Other** | ✗ | ✓ | ✓ | ✗ | 4 | Specialty/experimental materials |
| | | **52** | **52** | **45** | **51** | **200 total KS1 profiles** |

#### Anycubic Kobra X (KSX)

| Material | 0.25mm | 0.4mm | 0.6mm | 0.8mm | Total | Notes |
|---|:---:|:---:|:---:|:---:|---:|---|
| **PLA Family** | ✓ | ✓ | ✓ | ✓ | 10 | Same as KS1 (no thermal diff) |
| **PLA+** | ✓ | ✓ | ✓ | ✓ | 7 | X needs slightly different PA |
| **PETG** | ✓ | ✓ | ✓ | ✓ | 14 | X has marginally better flow |
| **TPU** | ✗ | ✓ | ✓ | ✗ | 3 | Same restrictions |
| **ABS** | ✗ | ✓ | ✓ | ✗ | 6 | Same as KS1 |
| **ASA** | ✗ | ✓ | ✓ | ✗ | 5 | Same as KS1 |
| **Nylon** | ✗ | ✓ | ✓ | ✗ | 3 | Same as KS1 |
| **Other** | ✗ | ✓ | ✓ | ✗ | 4 | Same as KS1 |
| | | **52** | **52** | **45** | **51** | **200 total KSX profiles** |

**Total inventory: 400 filament profiles (200 KS1 + 200 KSX)**

---

## Generation Rules & Inheritance Strategy

### Why Inheritance Matters

Anycubic Slicer Next supports **profile inheritance**: each profile can inherit from a parent, then override only specific fields. This creates a hierarchy:

```
Level 0: System Baseline
          ↓
Level 1: Your Custom Base (0.4mm - source of truth)
          ↓
Level 2: Other Nozzle Sizes (0.25/0.6/0.8) inherit from Base
          ↓
Level 3: Printer-Specific Variants inherit from same-nozzle-size variant
```

### Inheritance Chain

Every profile follows this structure:

```
Creality PLA @AC KS1 Base (0.4mm, KS1)
└─ inherits: [Parent profile name]
└─ compatible_printers: ["Anycubic Kobra S1 0.4 nozzle"]

Creality PLA @AC KS1 0.6mm (0.6mm, KS1)
└─ inherits: Creality PLA @AC KS1 Base
└─ compatible_printers: ["Anycubic Kobra S1 0.6 nozzle"]
└─ Overrides: [0.6mm-specific settings from system profile]

Creality PLA @AC KSX 0.6mm (0.6mm, KSX)
└─ inherits: Creality PLA @AC KS1 0.6mm
└─ compatible_printers: ["Anycubic Kobra X 0.6 nozzle"]
└─ Overrides: [X-specific deltas vs KS1]
```

### Three Smart Override Rules (System-Driven)

Generation logic is deterministic and transition-based:

#### Rule 1: 0.6mm - Full Clone + Transition Deltas
**Strategy:** Build `@AC KS1 0.6mm` from a full clone of `@AC KS1 Base`.

**Applied constraints:**
- Keep all base keys to avoid UI omissions.
- Apply only the changes observed in system `0.4 -> 0.6` for the matching filament type and printer context.
- Add/keep `filament_change_length` only when that system transition includes it.
- Ensure `nozzle_temperature_range_high` exists and thermal keys remain consistent.

#### Rule 2: 0.25mm - Lower-Only Safety Merge
**Strategy:** Build `@AC KS1 0.25mm` from base and apply conservative 0.25 updates.

**Applied constraints:**
- Prefer lower-only behavior for sensitive parameters where required by the architecture.
- Do not introduce increases that are not supported by the corresponding system transition.
- Keep inheritance-first structure and explicit compatibility mapping.

#### Rule 3: 0.8mm - Build From 0.6 + Transition Deltas
**Strategy:** Build `@AC KS1 0.8mm` from `@AC KS1 0.6mm`, then apply `0.6 -> 0.8` transition deltas.

**Applied constraints:**
- No global constants; values are resolved by filament type and printer context.
- Preserve key completeness and `HS = BRASS + 5` relationship unless explicitly overridden.
- Enforce `nozzle_temperature_initial_layer_HS <= nozzle_temperature_range_high`.

### System Data Quality Notes

System profiles differ by printer and are sometimes sparse by nozzle/type. To avoid propagating bad or missing values:
- KS1 delta derivation uses `Kobra S1` with `Kobra S1 Max` fallback/blending when needed.
- KSX variants inherit from KS1 same-nozzle variants, then receive X-specific transition overrides.

---

## Main Differences Between Variants

### Temperature Strategy by Nozzle Size

| Size | Strategy | Constraint |
|---|---|---|
| **0.25mm** | conservative merge from base | lower-only where required by rule set |
| **0.4mm** | source of truth | base calibration preserved |
| **0.6mm** | apply system transition | type/printer-specific, no global offset |
| **0.8mm** | apply system transition from 0.6 | type/printer-specific, no blanket escalation |

Important: fixed temperature offsets are not authoritative. Final temperatures come from the transition logic plus safety bounds.

### Pressure Advance (PA) Strategy

| Size | PA source |
|---|---|
| **0.25mm** | selective conservative merge from base/system |
| **0.4mm** | base profile calibration |
| **0.6mm** | system-observed `0.4 -> 0.6` transition per type/printer |
| **0.8mm** | system-observed `0.6 -> 0.8` transition per type/printer |

PA is not scaled by fixed multipliers in this architecture.

### Flow Rate / Volumetric Speed

| Size | Approach |
|---|---|
| **0.25mm** | lower-only/conservative merge where applicable |
| **0.4mm** | keep custom base values |
| **0.6mm** | transition-driven updates by type/printer |
| **0.8mm** | transition-driven updates by type/printer |

---

## Editing Workflow Reminder

Use this order to avoid drift and duplicated overrides:

1. Update `@AC KS1 Base` when the change should affect all nozzle variants.
2. Update `@AC KS1 0.6mm` / `0.8mm` / `0.25mm` only for nozzle-specific behavior.
3. Keep child profiles minimal: only explicit differences from inherited effective values.
4. Keep `version` in every profile, even if same as parent.
5. After edits, run validation for inheritance integrity and thermal safety (`HS initial <= range high`).

Practical rule: if a value is shared across nozzle sizes, put it in base. If it is nozzle-specific, keep it in that nozzle profile only.

---

## How to Update Values

### Scenario 1: You've Calibrated a New Filament at 0.4mm

**Goal:** Propagate calibrations to other nozzle sizes automatically

**Steps:**
1. In Anycubic Slicer, create/adjust profile: `[Brand] [Material] @AC KS1 Base`
2. Calibrate: nozzle temp, PA, flow, bed temp, cooling
3. Save with high confidence
4. **For 0.6mm:**
   - Manually create `[Brand] [Material] @AC KS1 0.6mm`
   - Set `inherits: "[Brand] [Material] @AC KS1 Base"`
   - Add system 0.6mm overrides (see table below)
5. **For 0.25mm/0.8mm:**
   - Follow smart rules (selective adoption of system values)
   - Test print at smallest object to validate

**System Lookup Table** (0.6mm PLA example from actual system baseline):
```
Material: Anycubic PLA
├─ 0.4mm system: temp=205°C, PA=0.035, flow=0.98, vol_speed=12
├─ 0.6mm system: temp=220°C, PA=0.015, flow=0.96, vol_speed=12
├─ 0.8mm system: temp=220°C, PA=0.05, flow=0.98, vol_speed=12
└─ 0.25mm system: temp=205°C, PA=0.05, flow=0.98, vol_speed=2
```

### Scenario 2: You Want to Fine-Tune a Nozzle Variant

**Goal:** Adjust a specific 0.6mm profile without touching the 0.4mm base

**Steps:**
1. Edit the variant profile: `[Brand] [Material] @AC KS1 0.6mm`
2. Change the specific field (e.g., `nozzle_temperature`)
3. The inheritance chain ensures:
   - ✓ Override applies only to 0.6mm version
   - ✓ 0.4mm base stays unchanged
   - ✓ KSX 0.6mm will either:
     - Inherit your new value if KSX = KS1, OR
     - Apply its own X-specific delta (if different)

**Example edits:**
- Want faster 0.6mm prints? Lower PA by 0.005
- Want better detail? Drop nozzle temp by 5°C
- Each change is isolated to that profile only

### Scenario 3: Batch Update (e.g., All 0.6mm Profiles Need New Fan Speed)

**Goal:** Change a setting across all 39 0.6mm profiles

**Warning:** This breaks inheritance! Not recommended.

**Better approach:**
1. Find the common parent (usually the system profile)
2. System profiles are in `system/Anycubic/filament/`
3. Modify the system profile → all inheriting profiles auto-update on slicer restart
4. OR create an intermediate "0.6mm base" parent that all variants inherit from

### Scenario 4: Adding a Material That Wasn't Migrated

**Goal:** Add "Brand NewTM PLA" with variants for 0.4, 0.6, 0.8, 0.25mm

**Steps:**
1. Create base profile: `Brand NewTM PLA @AC KS1 Base`
   - Use existing PLA profile as template (inherit-from)
   - Calibrate on your printer
2. Create 0.6mm variant:
   ```json
   {
     "from": "User",
     "inherits": "Brand NewTM PLA @AC KS1 Base",
     "compatible_printers": ["Anycubic Kobra S1 0.6 nozzle"],
     "nozzle_temperature": ["220"],      // System 0.6mm value
     "pressure_advance": ["0.015"],      // System 0.6mm value
     "filament_max_volumetric_speed": ["12"]
   }
   ```
3. Create KSX 0.6mm variant:
   ```json
   {
     "inherits": "Brand NewTM PLA @AC KS1 0.6mm",
     "compatible_printers": ["Anycubic Kobra X 0.6 nozzle"],
     // X-specific overrides (usually none for PLA)
   }
   ```
4. For 0.25/0.8mm: apply smart rules (see above)

---

## Quick Reference: Selection Guide

### By Use Case

#### I want the fastest possible print...
→ Use **0.8mm nozzle** with appropriate filament (PLA, PLA+, PETG)  
→ Layer height: 0.4-0.5mm  
→ Speeds: 150-180 mm/s  
→ Quality: Draft/prototype only

#### I want best quality on standard prints...
→ Use **0.4mm nozzle** (your 0.4mm Base profiles)  
→ Layer height: 0.15-0.20mm  
→ Speeds: 80-120 mm/s  
→ Quality: Excellent detail, smooth surfaces

#### I need fine details (miniatures, jewelry, precision parts)...
→ Use **0.25mm nozzle** with PLA or PETG  
→ Layer height: 0.10-0.15mm  
→ Speeds: 40-60 mm/s  
→ Quality: Extreme detail, requires careful calibration

#### I need speed but still decent quality (production parts)...
→ Use **0.6mm nozzle** (fastest "reasonable quality")  
→ Layer height: 0.25-0.30mm  
→ Speeds: 120-150 mm/s  
→ Quality: Good surface, structural sound

### By Printer Selection

#### Anycubic Kobra S1 (Primary)
- Use **KS1** profiles (calibrated for your machine)
- All nozzle sizes available
- Example: `Creality PLA @AC KS1 0.6mm`

#### Anycubic Kobra X (Secondary)
- Use **KSX** profiles (X-specific adjustments)
- All nozzle sizes available
- Inherits from KS1 variants with X-specific overrides
- Example: `Creality PLA @AC KSX 0.6mm`

### By Material & Temperature

**High-temperature materials (ABS, ASA, Polycarbonate):**
- Available at 0.4mm and 0.6mm only
- Reason: Require precision; not suitable for 0.25mm (risk clogs) or 0.8mm (too aggressive)
- Profiles: `[Brand] ABS @AC KS1 0.4mm/0.6mm`

**Standard materials (PLA, PLA+, PETG):**
- Available at all sizes: 0.25mm, 0.4mm, 0.6mm, 0.8mm
- Most versatile category
- Choose nozzle based on quality vs speed tradeoff

**Flexible materials (TPU):**
- Limited to 0.4mm and 0.6mm
- Reason: 0.25mm too small (tangles), 0.8mm too coarse (poor layer bonding)
- Profiles: `[Brand] TPU @AC KS1 0.4mm/0.6mm`

---

## Troubleshooting Profile Selection

### Problem: "This nozzle size doesn't exist for my filament"

**Check the inventory table above.** If a combination isn't listed:
- 0.25mm not available? → Use 0.4mm, or try with PLA/PETG only
- 0.8mm not available? → Engineering plastics skip this size; use 0.6mm
- Missing brand variant? → Create one using the "Adding a Material" steps above

### Problem: "Profile won't load in slicer"

**Most common causes:**
1. Profile inherits from a parent that doesn't exist → Verify parent profile name matches exactly
2. `compatible_printers` lists a nozzle size your slicer doesn't recognize → Check machine profiles
3. Corrupted JSON → Open in text editor, check for syntax errors (unmatched quotes, arrays)

### Problem: "Nozzle size doesn't appear in the printer dropdown"

**Check:**
1. Machine profile for your printer needs to define available nozzle sizes
2. Filament profile's `compatible_printers` field must match exactly
3. Example: `"compatible_printers": ["Anycubic Kobra S1 0.6 nozzle"]`

---

## Version History & Changelog

### v2.0 - Multi-Nozzle Migration (March 2026)
- ✓ Generated 0.25mm, 0.6mm, 0.8mm variants for all 52 materials
- ✓ Created KSX (Kobra X) variants for every profile
- ✓ Implemented physics-based smart override rules
- ✓ Total: 298 filament profiles (up from 52)
- ✓ Removed problematic flow_ratio deltas from KSX 0.4mm overlays
- New features:
  - Profile inheritance chains for easier maintenance
  - Material-family smart filtering rules
  - Full printer + nozzle compatibility matrix

### v1.0 - Initial Setup (Previous)
- Kobra S1 0.4mm brass nozzle only
- 52 manually calibrated profiles
- Basic temperature and flow settings

---

## Next Steps: Process Profiles

The next phase will be generating process profile variants (0.08mm, 0.12mm, 0.16mm, 0.20mm, etc.) for each nozzle size.

See `.github/copilot-instructions.md` for architecture overview and process profile strategy.
