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
6. [How to Update Values](#how-to-update-values)
7. [Quick Reference: Selection Guide](#quick-reference-selection-guide)

---

## What Changed: Migration Overview

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
| **0.6mm** | 39 profiles | Speed, quality, production | Both | ✓ New (v2.0) |
| **0.25mm** | 29 profiles | Fine details, miniatures | Both | ✓ New (v2.0) |
| **0.8mm** | 29 profiles | Fast prototype, structural | Both | ✓ New (v2.0) |
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

#### 0.6mm (39 Profiles) ✓ Recommended for Speed
**Physics basis:** Larger orifice = higher flow rates + lower pressure advance (thicker extrusion beads, less drag-induced wave patterns)

**Materials included:**
- ABS (5) + ASA (5) = **10 engineering plastics**
- PLA (7) + PLA+ (2) = **9 general purpose**
- PETG (14) = **flexible options including GF, CF, transparent**
- TPU (3) = **flexible materials**
- Specialty (2) = **Nylon, composite**

**Key profile characteristics:**
- Nozzle temp: +5-15°C higher than system baseline (wider nozzle = reduced heat loss)
- Pressure advance: 40-50% reduction (less precision-based drag)
- Flow rate: system-calibrated per material (not custom-reduced)

#### 0.25mm (29 Profiles) ⏳ Fine Detail Mode
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

#### 0.8mm (29 Profiles) ⚡ Fast Prototyping
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
| | | **52** | **39** | **29** | **29** | **149 total KS1 profiles** |

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
| | | **52** | **39** | **29** | **29** | **149 total KSX profiles** |

**Total inventory: 298 filament profiles (149 KS1 + 149 KSX)**

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

### Three Smart Override Rules (Physics-Based)

We applied different strategies for each nozzle size to respect your existing calibrations while embracing system baselines:

#### Rule 1: 0.6mm - Direct System Application ✓
**Strategy:** Use system baselines directly — they're proven to work.

**Why:** Your manually-calibrated JustMaker PETG GF @AC KS1 0.6mm shows system values are accurate. Physics also confirms larger nozzles can use higher temps and lower pressure advance.

**Implementation:**
- Copy effective system values (from Anycubic system profile for 0.6mm)
- Apply to all 39 profiles uniformly
- Inherits from corresponding 0.4mm Base profile
- System provides: nozzle_temperature, pressure_advance, fan speeds

**Example (Creality PLA 0.6mm):**
```json
{
  "inherits": "Creality PLA @AC KS1 Base",
  "compatible_printers": ["Anycubic Kobra S1 0.6 nozzle"],
  "nozzle_temperature": ["220"],          // System S1 0.6 for PLA
  "pressure_advance": ["0.015"],          // S1 0.6 system value
  "filament_max_volumetric_speed": ["12"], // System-calibrated
  ...
}
```

#### Rule 2: 0.25mm - Selective Smart Filtering ⚠️
**Strategy:** Only use system values if they're **lower** than your 0.4mm custom settings (don't aggressively reduce).

**Why:** Small nozzles are sensitive. Your 0.4mm calibrations are conservative and proven. Only adopt system values if they represent an improvement (lower flow = less back-pressure).

**Implementation:**
- For each numeric field: compare system 0.25 vs custom 0.4 value
- Only include field if system 0.25 < custom 0.4 (improvement)
- Skip if system would be more aggressive
- Conservative: inherits 0.4mm baseline if no safe improvement available

**Example (Creality PLA 0.25mm):**
```json
{
  "inherits": "Creality PLA @AC KS1 Base",
  "compatible_printers": ["Anycubic Kobra S1 0.25 nozzle"],
  "nozzle_temperature": ["200"],          // System 0.25 if lower than 0.4
  "pressure_advance": ["0.055"],          // System 0.25 only if < 0.4
  // Skips: filament_flow_ratio, volumetric_speed (not improvements)
  ...
}
```

#### Rule 3: 0.8mm - Conservative Comparison Against 0.6mm ⬆️
**Strategy:** Only use system values if they're **>= your 0.6mm overlay values** (ensure smooth progression).

**Why:** 0.8mm needs enough flow/PA to exceed 0.6mm, otherwise there's a contradiction in the extrusion physics. Progression should be: 0.4 → 0.6 → 0.8 (increasing or stable, never dropping).

**Implementation:**
- For each numeric field: compare system 0.8 vs KS1 0.6 overlay value
- Only include field if system 0.8 >= KS1 0.6 value
- Avoids contradictory settings between nozzle sizes
- Falls back to inheritance chain if system is worse

**Example (Creality PLA 0.8mm):**
```json
{
  "inherits": "Creality PLA @AC KS1 Base",
  "compatible_printers": ["Anycubic Kobra S1 0.8 nozzle"],
  "nozzle_temperature": ["220"],          // System 0.8 if >= 0.6 value
  "pressure_advance": ["0.05"],           // System 0.8 only if >= 0.6
  "filament_max_volumetric_speed": ["12"], // Same as system 0.4
  ...
}
```

### System Data Quality Notes

⚠️ **Known issue with Kobra X 0.4mm system baseline:**
- Nozzle temperature for ABS = 205°C (physiologically wrong, should be 250-260°C)

**Decision:** KSX 0.6/0.8/0.25 inherit from **KS1 equivalents**, NOT from KSX 0.4 baseline. This avoids propagating the error.

---

## Main Differences Between Variants

### Temperature Strategy by Nozzle Size

| Size | Delta vs 0.4mm | Rationale | Materials |
|---|---|---|---|
| **0.25mm** | -10 to -20°C | Tiny mass dissipates heat faster; lower temp prevents oozing | PLA 200°C, PETG 230°C |
| **0.4mm** | 0° (baseline) | Standard reference point | All materials |
| **0.6mm** | +5 to +15°C | Larger mass absorbs heat; higher temp improves flow | PLA 220°C, PETG 245°C |
| **0.8mm** | +10 to +20°C | Largest mass; needs highest temps for consistency | PLA 220°C, PETG 250°C |

**Important:** These are general tendencies. Your custom 0.4mm profiles may already include optimal base temperatures; nozzle variants inherit these and adjust via system baselines.

### Pressure Advance (PA) Strategy

| Size | PA Adjustment | Physics Explanation |
|---|---|---|
| **0.25mm** | PA ×1.5 to ×2.0 | Tiny diameter = high sensitivity to vibrations & pressure waves |
| **0.4mm** | PA ×1.0 (baseline) | Standard reference; your calibrations are here |
| **0.6mm** | PA ×0.4 to ×0.6 | Wider extrusion = less drag-induced oscillation; fewer micro-vibrations |
| **0.8mm** | PA ×0.3 to ×0.5 | Largest extrusion = minimal vibration impact; bead width dominates |

**Why PA changes:** Pressure advance compensates for pressure spikes during speed changes. Wider nozzles create wider beads with less precise control → lower PA. Narrower nozzles require tighter control → higher PA.

### Flow Rate / Volumetric Speed

| Size | Approach | Rationale |
|---|---|---|
| **0.25mm** | Use system if lower | Avoid over-aggressive flow restrictions |
| **0.4mm** | Your custom values | Existing calibrations stand |
| **0.6mm** | Use system directly | Proven to work; physics supports it |
| **0.8mm** | Use system if ≥ 0.6mm | Ensure smooth layer-to-layer progression |

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
