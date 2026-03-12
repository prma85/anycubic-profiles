# Anycubic Kobra S1 + Kobra X Configuration Guide (Enhanced)

**Last Updated:** March 2026  
**Scope:** User 651589 Personal Setup  
**Primary Printer:** Anycubic Kobra S1 (0.4mm brass nozzle)  
**Secondary Printer:** Anycubic Kobra X (0.4mm nozzle)  
**Framework:** Anycubic Slicer Next (OrcaSlicer-based)

---

## TABLE OF CONTENTS

1. [System Overview](#system-overview)
2. [Printer Hardware Specifications](#printer-hardware-specifications)
3. [🆕 Filament Profile Migration (v2.0)](#filament-profile-migration-v20)
4. [Quick Start - How to Print](#quick-start---how-to-print)
5. [Nozzle-Specific Configuration Variations](#nozzle-specific-configuration-variations)
6. [Machine-Specific Differences (S1 vs X)](#machine-specific-differences-s1-vs-x)
7. [Filament Selection by Type](#filament-selection-by-type)
8. [Process Profile Selection Guide](#process-profile-selection-guide)
9. [Specialized Profiles & Their Uses](#specialized-profiles--their-uses)
10. [OrcaSlicer Best Practices by Print Type](#orcaslicer-best-practices-by-print-type)
11. [Printer Calibration & Maintenance](#printer-calibration--maintenance)
12. [Common Issues & Solutions](#common-issues--solutions)
13. [Adding New Filaments](#adding-new-filaments)

---

## SYSTEM OVERVIEW

### Configuration Architecture

Your setup uses **three-tier hierarchical configuration**:

```
┌─────────────────────────────┐
│ MACHINE                     │ Printer + Nozzle Size
│ Anycubic Kobra S1 0.4mm     │ Build area, acceleration limits
└──────────┬──────────────────┘
           │
     ┌─────▼────────────────────┐
     │ FILAMENT                 │ Material + Brand + Nozzle
     │ Anycubic PLA             │ Temperatures, flow rates
     │ @Kobra S1 0.4nm          │
     └──────────┬────────────────┘
                │
   ┌────────────▼──────────────────┐
   │ PROCESS                        │ Layer height + purpose
   │ 0.20mm Standard               │ Speeds, accelerations
   │ @Kobra S1 0.4nm               │ Quality settings
   └────────────────────────────────┘
```

### File Organization

```
user/651589/
├── filament/          (Your optimized material profiles)
│   ├── README.md
│   ├── base/          (Inherited base profiles)
│   └── [60+ profiles by brand/material]
│
├── machine/           (Printer+nozzle configurations)
│   ├── base/
│   ├── Kobra S1 variants (brass, hardened steel)
│   └── [Machines in your workshop]
│
├── process/           (Layer heights + specializations)
│   ├── base/
│   ├── Standard profiles (0.08mm-0.28mm)
│   ├── Action Figures.json
│   ├── Miniatures (0.08mm).json
│   ├── Tools & Home Improvements.json
│   ├── Vase profiles
│   └── [Other specializations]
│
└── README.md, QUICK_REFERENCE.md
```

---

## FILAMENT PROFILE MIGRATION (v2.0)

### What Changed: Overview

In March 2026, we completed a major migration of the filament profile system:

**Before (v1.0):**
- 52 filament profiles for Kobra S1 0.4mm brass nozzle only
- Limited to single printer, single nozzle size
- No variants for faster (0.6mm, 0.8mm) or finer (0.25mm) detail work

**After (v2.0):**
- **298 total filament profiles** (up from 52)
- **Full nozzle coverage:** 0.25mm, 0.4mm, 0.6mm, 0.8mm
- **Both printers supported:** KS1 (Kobra S1) and KSX (Kobra X) variants
- **Physics-based rules:** Smart override system for each nozzle size
- **Clean inheritance:** Each variant inherits from 0.4mm base, reducing maintenance
- **Removed problematic settings:** No more aggressive flow_ratio deltas

### Profile Inventory Summary

```
┌──────────────────────────────────────────────────┐
│ FILAMENT PROFILE INVENTORY (v2.0)                │
├──────────────────────────────────────────────────┤
│ KS1 (Kobra S1) Profiles:          149            │
│   • 0.4mm Base           52 profiles             │
│   • 0.6mm variants       39 profiles             │
│   • 0.25mm variants      29 profiles (PLA/PETG)  │
│   • 0.8mm variants       29 profiles (PLA/PETG)  │
│                                                  │
│ KSX (Kobra X) Profiles:           149            │
│   • 0.4mm variants       52 profiles             │
│   • 0.6mm variants       39 profiles             │
│   • 0.25mm variants      29 profiles             │
│   • 0.8mm variants       29 profiles             │
│                                                  │
│ TOTAL:                            298 profiles   │
└──────────────────────────────────────────────────┘
```

### Key Facts About Variants

#### 0.4mm Nozzle (Base / Source of Truth)
- Your original custom calibrations
- All 52 material brands covered
- Every 0.6mm/0.25mm/0.8mm variant inherits from these
- Location: `filament/` folder (no nozzle suffix in name)
- Example: `Creality PLA @AC KS1 Base`

#### 0.6mm Nozzle (Speed-Optimized)
- **Use when:** Large parts, production speed important, quality still matters
- **Physics:** Larger orifice = higher flow, lower pressure advance
- **Generation rule:** Direct system baseline application
- **Coverage:** 39 profiles (all engineering plastics, all general purpose)
- **Speed boost:** ~30% faster than 0.4mm with acceptable quality loss
- **Example:** `Creality PLA @AC KS1 0.6mm`

#### 0.25mm Nozzle (Fine Detail)
- **Use when:** Small parts, miniatures, jewelry, high-precision geometry
- **Physics:** Tiny orifice = ultra-precise extrusion, high PA
- **Generation rule:** Selective system application (only values lower than 0.4mm)
- **Coverage:** 29 profiles (PLA, PLA+, PETG only; no engineering plastics)
- **Speed impact:** ~50% slower than 0.4mm but extreme detail possible
- **Example:** `Creality PLA @AC KS1 0.25mm`

#### 0.8mm Nozzle (Fast Prototype)
- **Use when:** Rapid testing, large structures, fast iteration
- **Physics:** Large orifice = minimal precision, bead-width-limited flow
- **Generation rule:** Conservative system application (only values ≥ 0.6mm overlay)
- **Coverage:** 29 profiles (PLA, PLA+, PETG only)
- **Speed boost:** ~80% faster than 0.4mm, acceptable for prototypes
- **Example:** `Creality PLA @AC KS1 0.8mm`

#### KSX Variants (Kobra X)
- Based on KS1 profiles but with X-specific adjustments
- Inherit from corresponding KS1 nozzle variant (e.g., KSX 0.6 inherits from KS1 0.6)
- Small overrides for X-specific thermal/pressure characteristics
- **Important:** Do NOT inherit from KSX 0.4 baseline (known quality issue with system ABS temp)
- Example inheritance: `Creality PLA @AC KSX 0.6mm` ← inherits ← `Creality PLA @AC KS1 0.6mm`

### Generation Strategy (Technical Reference)

For future maintenance and understanding how variants were generated:

#### Smart Rule #1: 0.6mm - Direct System Application
```
FOR each material in library:
  CREATE 0.6mm variant
  INHERIT FROM: 0.4mm Base profile
  OVERRIDE WITH: System Anycubic 0.6mm effective values
  APPLICABLE TO: All 39 materials (ABS, ASA, TPU, PLA, PETG, Nylon, etc.)
  
  Fields applied:
    • nozzle_temperature (system 0.6mm)
    • pressure_advance (system 0.6mm, typically 40-60% of 0.4mm)
    • filament_max_volumetric_speed (system value)
    • cooling_fan settings (100% vs 60% for 0.4mm)
```

**Rationale:** User's JustMaker PETG GF 0.6mm proves system values work. Physics confirms: larger nozzle = higher temps needed, lower PA needed.

#### Smart Rule #2: 0.25mm - Selective System Application
```
FOR each material IN [PLA, PLA+, PETG only]:
  CREATE 0.25mm variant
  INHERIT FROM: 0.4mm Base profile
  FOR each numeric field:
    IF system_0.25_value < custom_0.4mm_value THEN
      OVERRIDE WITH: system_0.25_value
    ELSE
      SKIP (use inherited 0.4mm value)
    END IF
  APPLICABLE TO: 29 profiles (conservative material selection)
```

**Rationale:** Small nozzles are finicky. Only adopt system values if they represent improvements (lower flow = less clog risk). Skip if system would be more aggressive than your proven 0.4mm calibrations.

#### Smart Rule #3: 0.8mm - Conservative Comparison
```
FOR each material IN [PLA, PLA+, PETG only]:
  CREATE 0.8mm variant
  INHERIT FROM: 0.4mm Base profile
  FOR each numeric field:
    IF system_0.8mm_value >= ks1_0.6mm_overlay_value THEN
      OVERRIDE WITH: system_0.8mm_value
    ELSE
      SKIP (use inherited 0.4mm value)
    END IF
  APPLICABLE TO: 29 profiles (only non-precision materials)
```

**Rationale:** Maintain physics consistency: nozzle progression must be 0.4 → 0.6 → 0.8 (never dropping in PA or flow). Ensures no contradictory settings between sizes.

#### KSX Variant Generation
```
FOR each KS1 nozzle_size variant (0.25/0.4/0.6/0.8):
  CREATE KSX equivalent
  INHERIT FROM: KS1 variant (same nozzle size)
  OVERRIDE WITH: X-specific deltas (usually minimal for PLA/PETG)
  COMPATIBLE_PRINTERS: "Anycubic Kobra X [nozzle] nozzle"
  
  X-specific overrides (if any):
    • Pressure advance (typically within ±0.005 of KS1)
    • Fan speeds (X has no auxiliary fan, may need adjustment)
    • Temperature (rarely different; max ±2°C)
```

**Rationale:** X and S1 are mechanically similar. Inheriting from KS1 variants ensures all physics rules are consistent. X-specific customizations are minimal (mostly pressure advance and cooling strategy).

### Where to Find Documentation

- **Full technical guide:** See `filament/README.md` for complete nozzle variant documentation
- **Quick selection:** Use the tables in README.md to pick nozzle size by use case
- **Adding new materials:** Follow "Scenario 4" in filament README for adding materials with nozzle variants
- **Inheritance chains:** All profiles documented with `inherits` field showing parent profile

### Next Phase: Process Profiles

Once filament variants are validated through test prints:

**Planned:** Generate process profile variants (0.08mm, 0.12mm, 0.16mm, 0.20mm, 0.24mm, 0.28mm) for each nozzle size
- Each process profile will inherit from 0.4mm base and adjust layer height + speeds
- Expected: 6 nozzle sizes × ~8 layer heights = ~48 new process profiles
- Will maintain the same smart rule strategy for speed/quality tradeoffs

---

## PRINTER HARDWARE SPECIFICATIONS

### Anycubic Kobra S1 (Primary Printer)

**Physical Specifications:**
- **Build platform:** 220 × 220 × 250 mm
- **Nozzle options:** 0.25mm (rare), **0.4mm brass** (default), 0.6mm, 0.8mm
- **Nozzle material:** Brass (standard) | Hardened Steel (abrasive materials)
- **Extruder:** Direct-drive (Anycubic variant)
- **Hotend:** Anycubic standard (OrcaSlicer compatible)
- **Bed:** PEI spring steel on magnetic base
- **Firmware:** Klipper (not Marlin)

**Motion Capabilities:**
- **Max acceleration:** 20,000 mm/s² (X/Y/E axes)
- **Max velocity:** 600 mm/s
- **Jerk:** 9.0 (directional)
- **Z-axis:** Limited to 1,000 mm/s² (mechanical constraint)

**Special Features:**
- ✅ Auxiliary cooling fan (extra layer cooling)
- ✅ Purge line before first layer (before_layer_change gcode)
- ✅ Supports pressure advance calibration (direct-drive)
- ✅ Quiet operation capable (0.20mm Quite-HQ profile)

**Advantages over Kobra X:**
- More aggressive acceleration capability (2× faster)
- Auxiliary fan for better cooling on PLA/cooling-friendly materials
- Purge line system (useful for multi-material reliability)
- Proven design (slightly more mature firmware)

### Anycubic Kobra X (Secondary Printer)

**Physical Specifications:**
- **Build platform:** 260 × 260 × 260 mm (+10mm all axes from S1)
- **Nozzle options:** **0.4mm** (primary), 0.6mm, 0.8mm
- **Nozzle material:** Brass (standard) | Hardened Steel (abrasive)
- **Extruder:** Direct-drive variant (newer design)
- **Hotend:** Newer hotend design (different gcode sequence)
- **Bed:** Similar to S1 (PEI spring steel)
- **Firmware:** Klipper variant

**Motion Capabilities:**
- **Max acceleration:** 10,000 mm/s² (more conservative)
- **Max velocity:** varies per axis (similar to S1)
- **Jerk:** 9.0
- **Z-axis:** 1,000 mm/s² (same as S1)

**Special Features:**
- ✅ Larger build area (+10mm per axis)
- ❌ NO auxiliary cooling fan
- ❌ NO purge line gcode (simpler startup)
- ✅ Potential for future features (newer design)

**Disadvantages:**
- Lower acceleration limits (print quality less rigid)
- No auxiliary fan (PLA cooling needs management)
- Different gcode sequences (not profile-compatible with S1)

### Can You Use S1 Profiles on X (and vice versa)?

**Short answer:** Not directly. Different machine specifications require profile validation.

**Issues:**
1. **Acceleration limits:** S1 can do 20k, X maxes at 10k - S1 profiles may cause X to fault
2. **Cooling strategy:** S1 has auxiliary fan, X doesn't - fan settings must differ
3. **Gcode sequences:** S1 purge line incompatible with X startup
4. **Pressure advance:** MA models calibrated separately per machine

**Solution:**
- Use S1 profiles as **starting point only**
- Validate acceleration settings for X
- Adjust fan speeds (remove auxiliary_fan logic)
- Test print before committing to large prints

---

## QUICK START - HOW TO PRINT

### The Standard Workflow

1. **Launch Anycubic Slicer Next**

2. **Select Machine**
   - Kobra S1: `Anycubic Kobra S1 0.4 nozzle - Brass` (or Hardened Steel)
   - Kobra X: `Anycubic Kobra X 0.4 nozzle`

3. **Select Filament**
   - Browse by material type in `filament/` folder
   - Example: `Overture PETG` or `Improved PLA @AC KS1`
   - Must match printer variant if possible (0.4 nozzle version)

4. **Select Process Profile**
   - First-time? Use **`0.20mm Quit-HQ`** (balanced quality + speed)
   - Quality needed? `0.16mm HQ` or `0.12mm HQ`
   - Speed critical? `0.24mm Draft` or `0.28mm ExtraDraft`
   - Special purpose? See [Specialized Profiles](#specialized-profiles--their-uses)

5. **Load Model & Slice**
   - Model should be < 220×220×250mm for S1 (250×250×260mm for X)
   - Right-click → "Slice" or press keyboard shortcut
   - Review print preview for supports/issues

6. **Print**
   - Transfer to USB or OctoPI
   - Start on printer
   - Observe first layer (bed adhesion critical!)
   - Monitor for first 2-3 layers

---

## NOZZLE-SPECIFIC CONFIGURATION VARIATIONS

### Understanding Nozzle Impact

Your Kobra S1 supports multiple nozzles: **0.25mm, 0.4mm (default), 0.6mm, 0.8mm**

**Critical principle:** Different nozzle sizes require different profiles because:
- Larger nozzle = thicker line width needed
- Larger nozzle = higher maximum layer height
- Larger nozzle = flow rates change
- Larger nozzle = extrusion volumes differ significantly

### Nozzle Size Comparison Table

| Parameter | 0.4mm Nozzle | 0.6mm Nozzle | 0.8mm Nozzle | Notes |
|-----------|--------------|--------------|--------------|-------|
| **Max layer height** | 0.30mm | 0.45mm | 0.60mm | ~75% of nozzle diameter |
| **Standard line width** | 0.42-0.45mm | 0.60mm | 0.80mm | Close to nozzle diameter |
| **Recommended layer heights** | 0.08-0.28mm | 0.16-0.42mm | 0.24-0.56mm | Practical range |
| **Extrusion speed** | 300 mm/s base | 300 mm/s base | 300 mm/s base | Same, but different volumetric |
| **Volumetric max** | 12-14 mm³/s | 12-14 mm³/s | 12-14 mm³/s | Material-dependent |
| **Bridge speed** | 50 mm/s | 30 mm/s | 20 mm/s | Larger = slower needed |
| **Bridge flow** | 1.0 | 0.9 | 0.8 | Compensation for size |
| **Cooling fan speed** | 60% (PLA) | 100% (PLA) | 100% (PLA) | Larger nozzle cools slower |
| **Typical use case** | Balanced | Fast/large | Rapid prototyping | By purpose |

### PLA Configuration Across Nozzle Sizes

**Filament Level (Flow Ratio Differences):**

```json
// KS1 0.4mm brass nozzle
{
  "filament_flow_ratio": [0.98],
  "filament_max_volumetric_speed": [12],
  "adaptive_pressure_advance_model": [complex_curve_0.4mm],
  "additional_cooling_fan_speed": [60],
  "during_print_exhaust_fan_speed": [60]
}

// KS1 0.6mm brass nozzle
{
  "filament_flow_ratio": [0.96],      // ← Slightly lower for larger nozzle
  "filament_max_volumetric_speed": [12],
  "adaptive_pressure_advance_model": [complex_curve_0.6mm],  // Different calibration
  "additional_cooling_fan_speed": [100],  // ← Much higher (larger nozzle cools slower)
  "during_print_exhaust_fan_speed": [100]  // ← Much higher
}
```

**Key observation:** Flow ratio changes from **0.98 → 0.96** (about 2% reduction)
- Larger nozzles don't need as much flow compensation
- Fan speeds increase dramatically (40% → 100%)
- Pressure advance models are completely different

**Process Level (0.20mm Standard → 0.30mm Standard):**

```json
// 0.20mm Standard @KS1 0.4mm
{
  "layer_height": "0.2",
  "outer_wall_line_width": 0.42,
  "outer_wall_speed": 150,
  "bridge_speed": 50,
  "bridge_flow": 1.0,
  "elefant_foot_compensation": 0.1,
  "line_width": 0.42
}

// 0.30mm Standard @KS1 0.6mm (approx)
{
  "layer_height": "0.3",           // ← 50% thicker
  "outer_wall_line_width": 0.6,    // ← Matches nozzle size
  "outer_wall_speed": 150,         // ← Often same (material-dependent)
  "bridge_speed": 30,              // ← Slower for larger nozzle!
  "bridge_flow": 0.9,              // ← Compensation
  "elefant_foot_compensation": 0.075,  // ← Smaller for larger nozzle
  "line_width": 0.6                // ← Matches nozzle size
}
```

**Key observations:**
1. Line widths scale with nozzle size (0.4mm nozzle → 0.42-0.45mm width; 0.6mm → 0.6mm)
2. Bridge speed DECREASES for larger nozzles (more drooping risk)
3. Elephant foot decreases for larger nozzles (less squish needed)
4. Most other speeds stay similar (material property, not nozzle property)

### When to Switch Nozzle Sizes

| Scenario | Recommended Nozzle | Why |
|----------|-------------------|-----|
| Small detailed model (<5cm) | 0.4mm | Fine detail capability |
| Standard models (5-15cm) | 0.4mm | Best balance |
| Large parts (>15cm) | 0.6mm | Faster, still good quality |
| Rapid prototype/test | 0.8mm | Fastest possible |
| Tiny miniature (<2cm) | 0.4mm (0.25mm if available) | Must use smaller |
| Production run (20+ copies) | 0.6mm or 0.8mm | Speed advantage critical |
| Abrasive materials (PLA-CF) | 0.4mm hardened steel | Don't wear out small nozzle fast |

---

## MACHINE-SPECIFIC DIFFERENCES (S1 vs X)

### Side-by-Side Comparison

| Feature | Kobra S1 | Kobra X | Impact |
|---------|----------|---------|--------|
| **Build area** | 220×220×250mm | 260×260×260mm | X is 4% larger |
| **Max X/Y accel** | 20,000 mm/s² | 10,000 mm/s² | **S1 is 2× faster** |
| **Auxiliary fan** | ✅ YES | ❌ NO | S1 cools PLA better |
| **Purge line gcode** | ✅ Included | ❌ None | S1 has startup sequence |
| **Default acceleration** | 10,000 | 6,000 | S1 more aggressive |
| **Nozzle variant support** | 0.25, 0.4, 0.6, 0.8mm | 0.4, 0.6, 0.8mm | S1 has 0.25mm option |
| **Maturity** | More proven | Newer design | S1 slightly more stable |

### Process Profile Differences

When comparing **0.20mm Standard @S1 0.4nm** vs **0.20mm Standard @X 0.4nm:**

**Acceleration Settings:**
```json
// S1 version (more aggressive)
{
  "default_acceleration": 10000,
  "inner_wall_acceleration": 5000,
  "internal_solid_infill_acceleration": 5000,
  "bridge_acceleration": "50%"  (= 5000)
}

// X version (more conservative)
{
  "default_acceleration": 6000,     // ← Lower
  "inner_wall_acceleration": 4000,  // ← Lower
  "internal_solid_infill_acceleration": 0,  // ← DISABLED!
  "bridge_acceleration": 5000       // ← Absolute, not percentage
}
```

**Speed Settings:**
```json
// S1 version
{
  "initial_layer_infill_speed": 80
}

// X version
{
  "initial_layer_infill_speed": 100  // ← X prints first layer faster (different design)
}
```

**Wall Settings:**
```json
// S1 version - prioritizes detail
{
  "extra_perimeters_on_overhangs": 1,  // Enabled
  "internal_solid_infill_pattern": "zig-zag"
}

// X version - simpler approach
{
  "extra_perimeters_on_overhangs": 1,  // Also enabled (good design)
  "internal_solid_infill_pattern": "zig-zag"
}
```

### Can You Share Profiles Between S1 and X?

**Process Profiles: YES* - With optional acceleration tuning** ✅

**Updated analysis:** Your original understanding is correct. Process profiles CAN be shared because:

1. **Machine-level handles the real differences** - The machine profile controls fans, gcode sequences, and startup procedures. The process profile only controls slicer behavior (speeds, accelerations, quality features).

2. **Accelerations are manageable** - Both printers use the same acceleration model. S1 allows up to 20,000 mm/s², X allows up to 10,000 mm/s². For X, simply reduce accelerations by 0-40% depending on how close the S1 profile is to the limits.

3. **Cores settings are universal** - Layer heights, line widths, speeds, and quality features (ironing, supports, etc.) work identically on both printers.

**Practical options for your custom profiles:**

**Option A: Direct Share (Easiest)**
- Copy S1 process profile directly to X
- Update `compatible_printers` field to include X variant
- Test first print (usually works fine)

**Option B: Inheritance (Best Practice)**
- Create X variant that inherits from S1 version
- Override accelerations if needed
- Example:
  ```json
  {
    "name": "0.20mm Quite-HQ @Kobra X 0.4nm",
    "inherits": "0.20mm Quite-HQ @Anycubic Kobra S1 0.4 nozzle",
    "default_acceleration": 6000,        // Reduced from 10000
    "inner_wall_acceleration": 4000,     // Reduced from 5000
    "internal_solid_infill_acceleration": 0  // X doesn't use this
  }
  ```

**Option C: Let Machine Profile Handle It (Cleanest)**
- Use same process profile for both printers
- Let the machine profile enforce X's acceleration limits
- Requires configuring machine profile to override acceleration settings

**Filament Profiles: YES* - With cooling adjustments** ⚠️

**For gentle materials (PLA, PETG, TPU):**
- Change `inherits` field to point to the base profile
- Test print to make sure cooling fan strategy works
- Usually requires no other changes

**For aggressive materials (ABS, ASA, Nylon):**
- Create X variant that inherits from S1 version
- Override cooling fan settings (X needs more aggressive cooling due to open design)
- S1 min_fan: 10% → X min_fan: 80% (significant difference!)
- See `FILAMENT_COMPATIBILITY_ANALYSIS.md` for exact parameter changes

**The Reality:**
- **Exhaust fan presence** is machine-level (machine profile handles)
- **Gcode differences** are machine-level (machine profile handles)
- **Different cooling strategy** is the main gotcha (X is open → needs constant cooling)

---

### Why Some Differences Exist

**Exhaust Fan (S1 vs X):** Machine-level
- S1 has exhaust fan controlled by filament profile
- X has no exhaust fan
- **Doesn't affect process profiles**, machine profile ignores unsupported settings

**Gcode Startup/Shutdown:** Machine-level
- S1 includes purge line in `before_layer_change_gcode`
- X doesn't
- **Doesn't affect process profiles**, machine profile handles gcode injection

**Accelerations:** BOTH Machine-level AND Process-level
- Machine defines MAXIMUM acceleration
- Process defines TYPICAL/desired acceleration
- If process asks for 10,000 mm/s² and machine max is 10,000 mm/s², you're at the limit with no headroom for jerk calculations
- **This IS something you might need to adjust for X** (reduce by 20-40%)

### Recommendation for Your Setup

**For process profiles:** You can freely share S1 specializations (Action Figures, Miniatures, Tools) with X by updating compatible_printers or creating inheritance variants.

**For filament profiles:** You can reuse most of your custom filaments on X; detailed guide in `FILAMENT_COMPATIBILITY_ANALYSIS.md`

**Best practice for new profiles:** Always test on actual printer first, even if theory says it should work.

---

## FILAMENT SELECTION BY TYPE

### Decision Tree

```
START: You have a filament spool to print

  Q: What's written on the spool?
  ├─ PLA or PLA+ (most common)     → Go to PLA section
  ├─ PETG or PETG+                → Go to PETG section
  ├─ TPU or Flexible              → Go to TPU section
  ├─ Something else               → Search filament folder README
  └─ You don't know               → Assume PLA, test on small print first
  
  Q: What brand/model is it?
  ├─ Found exact match (e.g., "Overture PETG") → Use that profile
  └─ Brand not in system          → Copy similar brand, adjust temps
```

### PLA (Polyactic Acid)

**Characteristics:** Easiest material, beginner-friendly, rigid, colorful

**Temperature Range:** 200-220°C nozzle, 60°C bed

**Profiles in your system:** 30+ brands/variants

**Recommended profiles:**
- `0.16mm Optimal`  (nice detail)
- `0.20mm Quite-HQ` ⭐ DEFAULT (quiet + quality)
- `0.20mm SD` (slightly faster)

**Printing tips:**
- Works at room temperature (no heated bed required)
- Minimal cooling issues (fans can be aggressive)
- Adjust temperature by material:
  - Standard PLA: 200-210°C
  - PLA+: 215-225°C (stronger variant, hotter)
  - PLA Silk: 200-210°C (glossy finish, same temps as regular)
- Supports: Tree supports work perfectly
- Post-processing: Can be sanded easily, painted with acrylics

**Best for:**
- First prints (reliable)
- Decorative items
- Detail models
- Prototyping
- Fast iterations

**Your PLA inventory:**
```
Anycubic PLA @AC KS1 0.4nm (included - good baseline)
Improved PLA @AC KS1        (pre-optimized)
Elegant, Creality, Prusament variants (multiple brands)
PLA Silk variants           (glossy finish)
PLA Galaxy variants         (sparkly/special effects)
```

### PLA+ (Enhanced PLA)

**Characteristics:** Stronger than PLA, higher temp tolerance, darker colors

**Temperature Range:** 210-230°C nozzle, 60°C bed

**Profiles in your system:** 5+ brands

**Recommended profiles:**
- `0.20mm Quite-HQ` or `0.16mm Optimal PLA+` (if specific variant exists)
- Often uses same process as PLA but 10°C hotter

**Printing tips:**
- **CRITICAL:** Print 10-20°C hotter than regular PLA
- Slower than PLA (more viscous = less flow)
- Bed temperature same as PLA (60°C)
- Prevent warping: Good bed adhesion, calm first 2 layers
- Post-processing: Sands well, can be anodized

**Best for:**
- Functional parts needing strength
- Items that see sun/outdoor use
- Higher temperature tolerance needed
- Stronger miniatures (won't break as easily)

**Your PLA+ inventory:**
```
Creality PLA+
Elegoo Rapid PLA+
iBoss Matte PLA+
Improved PLA+ @AC KS1      (optimized variant)
Sunlu PLA+
```

### PETG (Polyethylene Terephthalate Glycol)

**Characteristics:** Strong, durable, chemical resistant, excellent for functional parts

**Temperature Range:** 230-250°C nozzle, 70-80°C bed (CRITICAL!)

**Profiles in your system:** 20+ brands

**Recommended profiles:**
- `0.20mm General PETG` (balanced)
- `0.24mm General PETG` (slightly faster)
- `0.20mm HQ PETG` (higher quality variant)

**Printing tips:**
- **CRITICAL #1:** Bed MUST be 70-80°C (not 60°C like PLA!)
- **CRITICAL #2:** Bed leveling MUST be perfect (PETG squishes more)
- Clean bed with IPA between prints (oils cause adhesion loss)
- Fan speed: GENTLE (aggressive cooling = warping)
- Nozzle temperature: Test from 230-250°C (brand-dependent)
- Outer wall speed: Reduce to 40-60 mm/s (slower than PLA)
- Post-processing: Difficult to sand (doesn't crumble like PLA), can be vapor-smoothed

**Best for:**
- Functional parts (brackets, hinges, organizers)
- Structures experiencing stress
- Chemical/moisture exposure
- Outdoor items (more UV stable than PLA)
- Parts that need flexibility + strength

**Your PETG inventory:**
```
Anycubic PETG @AC KS1       (included - reliable baseline)
Improved PETG @AC KS1       (optimized)
Overture PETG (various)
Prusament PETG (various)
Elegoo Rapid PETG
Sovol PETG variants         (including glass-filled option)
[15+ brands total]
```

**Special variant: PETG HS (High Speed)**
- Hotter PETG (240-260°C)
- Same bed temperature (75-85°C)
- Faster printing possible
- Profile: `0.20mm General PETG` or `0.24mm General PETG`

**⚠️ WARNING - Glass-Filled PETG:**
- JustMaker PETG GF: **REQUIRES hardened steel nozzle**
- Brass nozzle will wear out in 1-2 prints
- Use: `Anycubic Kobra S1 0.4 nozzle - Hardened Steel` machine profile

### TPU (Thermoplastic Polyurethane)

**Characteristics:** Flexible, rubber-like, bouncy, durable

**Temperature Range:** 200-220°C nozzle, 20-30°C bed (optional, actually no heating recommended)

**Profiles in your system:** 4+ brands

**Recommended profiles:**
- `0.2mm Optimal TPU` (standard)
- `0.2mm Optimal TPU - Avoid Crossing Walls Off` (variant for different designs)

**Printing tips:**
- **CRITICAL #1:** Print VERY SLOWLY (20-40 mm/s, not 100+)
- **CRITICAL #2:** NO bed heating (room temperature is fine)
- Extrusion: Direct-drive handles TPU better than Bowden
- No cooling fans (flexible material doesn't benefit)
- Support: Minimal (hard to remove from flexible material)
- Post-processing: Impossible to sand (rubber bounces), can be glued or left as-is

**Best for:**
- Flexible phone stands
- Bouncy/squeezable toys
- Elastomer parts
- Flexible hinges
- Protective cases

**Your TPU inventory:**
```
Anycubic TPU @AC KS1
Overture TPU (various)
Overture TPU HS (high speed variant - still slow for TPU!)
Overture High Speed TPU
Sunlu TPU 95A
```

### Specialty Materials

**PLA-CF (Carbon Fiber Reinforced PLA)**
- **Requirement:** Hardened steel nozzle (brass wears out immediately)
- **Temperature:** 205-225°C
- **Profile:** `0.20mm Standard` or any PLA profile
- **Note:** Slightly harder to handle than regular PLA
- **Your inventory:** 1 profile (eSun PLA-CF)

**Nylon / PA (Polyamide)**
- **Temperature:** 260-280°C
- **Bed:** 80-100°C
- **Speed:** 60-75% of PLA (slower)
- **Note:** Extremely tough and durable
- **Your inventory:** 2 profiles (Anycubic PA, PAHT-CF)

**PVA (Polyvinyl Alcohol)**
- **Temperature:** 210-230°C
- **Bed:** Room temp OK
- **Special:** Water-soluble (use for support material!)
- **Speed:** 80% of PLA
- **Your inventory:** 2 profiles (Anycubic PVA)

---

## PROCESS PROFILE SELECTION GUIDE

### Layer Height Decision Matrix

**Question: How much detail do you need vs how fast?**

| Layer Height | Detail Level | Speed vs Standard | Best For | Nozzle Size |
|--------------|--------------|------------------|----------|------------|
| **0.08mm** | ULTRA-fine | 4-5× slower | Miniatures, jewelry, engravings | 0.4mm |
| **0.12mm** | Fine detail | 2-3× slower | Small action figures, detailed prints | 0.4mm |
| **0.16mm** | High quality | 1.5× slower | Detailed parts, miniatures | 0.4mm |
| **0.20mm** | **Standard** | 1× (baseline) | General purpose, balanced | 0.4mm |
| **0.24mm** | OK quality | 0.8× faster | Larger parts, faster prints | 0.4mm |
| **0.28mm** | Draft only | 0.6× faster | Quick prototypes, tests | 0.4mm |
| **0.30mm** | Balanced | 0.9× baseline | 0.6mm nozzle standard | 0.6mm |
| **0.40mm** | Draft | 0.5× baseline | 0.8mm nozzle fast | 0.8mm |

### Quality Level Classifications

Your system provides different "flavors":

**By Purpose:**
- **HQ (High Quality):** Slowest, best appearance
- **Optimal:** Balanced quality × speed (recommended)
- **Standard:** General-purpose settings
- **SD (Speed/Draft):** Faster, acceptable quality
- **Draft/ExtraDraft:** Quickest prototypes only

**Actual available profiles:**

| Layer | Draft | Standard | Optimal | HQ |
|-------|-------|----------|---------|-----|
| 0.08mm | — | — | ✅ | ✅ |
| 0.12mm | — | ✅ | ✅ | ✅ |
| 0.16mm | — | ✅ | ✅ | ✅ |
| 0.20mm | ✅ | ✅ | ✅ | ✅ |
| 0.24mm | ✅ | ✅ | — | — |
| 0.28mm | ✅ | ✅ | — | — |

### How to Choose: Decision Tree

```
What's your priority?

BEST QUALITY POSSIBLE?
├─ Small print (<10cm)? Use 0.12mm HQ
├─ Large print (>10cm)? Use 0.16mm HQ
└─ Miniature (<8cm)? Use 0.08mm HQ

BALANCE QUALITY & SPEED?
├─ Most common choice ✅
├─ Use 0.20mm Quite-HQ or 0.16mm Optimal
└─ Prints looks great, doesn't take forever

NEED IT FAST?
├─ Prototype/test? Use 0.24mm Draft
├─ Large object? Use 0.28mm ExtraDraft
└─ Willing to accept visible layer lines? Go ahead

SPECIAL PURPOSE?
├─ Miniatures (tabletop gaming)? Use Miniatures (0.08mm)
├─ Action figures? Use Action Figures (0.12mm)
├─ Durable tools/brackets? Use Tools & Home Improvements (0.24mm)
├─ Flexible toy? Use Rubber Duck (TPU profile)
├─ Decorative vase? Use Vase (spiral or hollow)
└─ [See Specialized Profiles section]
```

---

## SPECIALIZED PROFILES & THEIR USES

### Action Figures (0.12mm)

**Purpose:** Detailed small character models (5-12cm tall)

**When to use:**
- Anime/manga figures
- Character collectibles
- Small detailed models where expression matters
- Prints where surface quality is primary concern

**What makes it special:**
- Layer height: 0.12mm (fine detail)
- Ironing enabled (ultra-smooth finish)
- Lower wall speeds (110-130 mm/s for crisp detail)
- Support: Pre-configured for this purpose
- Brim: 8mm (extra-wide for adhesion on small prints)

**Expected results:**
- Perfect for faces and details
- Print time: ~2× longer than 0.20mm standard
- Surface: Smooth and professional
- Visible detail level: Excellent

**Material recommendation:**
- PLA (easiest)
- PLA Silk (glossy pro look)
- PLA Galaxy (special effects)

**Tips:**
- Paint after print (layer lines still visible without paint)
- Use tree supports (cleaner removal)
- Sand with 400+ grit for paint prep

---

### Miniatures (0.08mm)

**Purpose:** Ultra-fine gaming/hobby miniatures (2-5cm)

**When to use:**
- D&D/tabletop gaming figures
- Warhammer 40K scale models
- Tiny jewelry or pendant details
- Anything requiring microscopic precision

**What makes it special:**
- Layer height: 0.08mm (ULTRA-fine)
- Extremely slow speeds: 30-70 mm/s (creeps along)
- Tight acceleration control: 2000-5000 mm/s² (no vibration)
- Thin wall detection: Handles small features
- Custom line widths: 0.22mm precision

**Expected results:**
- Finest detail possible from your printer
- Layer lines present but microscopic
- Paint absolutely transforms appearance
- Print time: 4-5× longer than 0.20mm

**Material recommendation:**
- PLA (standard)
- PLA+ (won't chip as easily)

**Tips:**
- Single print at a time (don't batch)
- Use thin supports or none (avoid surface marks)
- Post-process: 400+ grit sanding → primer → paint
- Photos enhance appearance significantly (layer lines less visible in photos)

---

### Tools & Home Improvements (0.24mm)

**Purpose:** Durable, strong functional parts

**When to use:**
- Tool organizers and storage
- Phone stands and docks
- Drawer organizers
- Brackets, hinges, clips that must hold weight
- Cabinet handles
- Any part experiencing regular mechanical stress

**What makes it special:**
- Layer height: 0.24mm (faster)
- Line width: 0.46mm (stronger extrusion)
- Bottom shells: 4 layers (durable base)
- Infill often: 50-100% (strength)
- Ironing: Full coverage (polished appearance)
- Internal pattern: Monotonicline (stronger)

**Expected results:**
- Fast and strong
- Print time: 30-40% faster than 0.20mm
- Can hold significant weight without failure
- Good surface finish from ironing

**Material recommendation:**
- **PETG** (not PLA) for maximum strength
- Consider 100% infill for load-bearing parts
- PLA+ if PETG not available

**Tips:**
- Increase infill to 80-100% for critical parts
- Test fitments on small sacrificial parts first
- Post-process: Sand, paint, or leave unpainted
- Install brass inserts for threaded connections

---

### Vase (Spiral) & Vase (Hollow)

**Purpose:** Decorative hollow objects

**When to use:**
- Attractive vases (decorative only)
- Planters (if drainage hole added)
- Decorative boxes
- Hollow structures
- Water-resistant containers (with sealant)

**What makes it special:**
```
Spiral Mode:
- Single outer wall that spirals continuously
- No seams on exterior
- Stunning visual result
- But: No supports needed (hollow = unsupported interior)

Hollow Mode:
- Different algorithm for single-wall generation
- Alternative spiral approach
- Both work, choose by preference
```

**Expected results:**
- Very fast (50% less material than solid)
- Beautiful exterior
- Can be painted/finished
- Water-resistant (not waterproof - seal if needed)

**Material recommendation:**
- PLA (decorative, not structural)
- PETG (if actual water-holding needed)

**Tips:**
- Bottom must be solid (6 layers of bottom_shell_layers)
- Don't use for water unless sealed with epoxy
- Sand if water-holding (improve seal)
- Test drainage if planter

---

### Other Specializations You Have

| Profile | Layer | Purpose | Material |
|---------|-------|---------|----------|
| **Book Nook** | Varies | Decorative miniature diorama/scene | PLA (assembled from multiple prints) |
| **Disney Plates** | Special | Character-themed plates/dishes | PLA Silk or standard |
| **Door Corner** | Variable | Decorative corner fillers/molding | PLA or PETG |
| **Rubber Duck** | 0.20mm | Flexi toy (squeezable) | TPU HS |
| **0.16mm Optimal Silk PLA** | 0.16mm | High-quality glossy finish | PLA Silk materials |
| **0.20mm HQ PETG** | 0.20mm | High-quality PETG parts | PETG materials |

---

## ORCASLICER BEST PRACTICES BY PRINT TYPE

### Decorative Prints (High Detail)

**Recommended profiles:** `0.12mm HQ`, `0.16mm HQ`, `Miniatures (0.08mm)`

**Settings philosophy:**
- Layer height: 0.08-0.16mm
- Speeds: Slow (30-100 mm/s)
- Cooling: Aggressive fan
- Infill: Light (5-10%, not structural)
- Ironing: Yes, aggressive
- Support: Minimal, positioned carefully

**Expected quality:** Excellent, gallery-worthy

---

### Functional Parts (Strength Priority)

**Recommended profiles:** `0.20mm General PETG`, `Tools & Home Improvements`

**Settings philosophy:**
- Layer height: 0.20-0.24mm
- Line width: 0.45-0.50mm (thicker = stronger)
- Infill: 40-100% (strength)
- Accelerations: Moderate (6000-10000)
- Cooling: Gentle (prevent thermal stress)
- Ironing: Optional

**Expected quality:** Strong, reliable, professional appearance

---

### Rapid Prototypes (Speed Priority)

**Recommended profiles:** `0.24mm Draft`, `0.28mm ExtraDraft`

**Settings philosophy:**
- Layer height: 0.24-0.28mm
- Speeds: Aggressive (200-300 mm/s)
- Cooling: Moderate
- Infill: Light (15-20%)
- Support: Auto-generate, plan for removal time
- Ironing: No

**Expected quality:** Visible layer lines acceptable, but functional

---

## PRINTER CALIBRATION & MAINTENANCE

### Before First Print

1. **Bed Leveling (CRITICAL)**
   - Paper method: Nozzle should drag paper slightly
   - Check all 4 corners + center
   - Repeat every 5-10 prints or if issues

2. **Nozzle Cleaning**
   - Cold pull method when cool
   - Remove plastic plug blocking nozzle
   - Brass brush during heating (gentle)

3. **Bed Adhesion Prep**
   - Clean bed with isopropyl alcohol (IPA)
   - No soap/water (leaves residue)
   - Use lint-free cloth

### Regular Maintenance

| Task | Frequency | Notes |
|------|-----------|-------|
| Bed leveling | Every 5-10 prints | Critical for adhesion |
| Bed cleaning | Every 3-5 prints | Use IPA only |
| Nozzle cleaning | Every 5-10 prints | Cold pull or brush |
| PTFE tube inspection | Monthly | Should be white, not brown |
| Extruder gear cleaning | Monthly | Filament dust builds up |
| Build plate replacement | 6-12 months | PEI wears out with use |
| Firmware updates | As released | Check Anycubic website |

### Pressure Advance Calibration

Your profiles include pre-calibrated pressure advance curves. **Don't change unless:**
- You swap extruder types
- You install a different hotend
- You notice consistent over/under-extrusion at corners

**If recalibrating:**
1. Print PA test pattern (lines with varying PA values)
2. Compare corner quality across test lines
3. Select best-looking value
4. Update `adaptive_pressure_advance_model` in filament profile

---

## COMMON ISSUES & SOLUTIONS

### Layer 1 Not Sticking

**Causes:** Bed not level, bed too cold, or dirty bed

**Solutions:**
1. **Re-level bed** (paper method, all 4 corners + center)
2. **Increase bed temp:** PLA 60°C → try 65°C; PETG 75°C → try 80°C
3. **Clean bed with IPA** (not soap/water)
4. **Warped bed?** Place straight edge on bed; if gap visible, bed may be warped (consider replacement)

---

### Stringing/Oozing

**Cause:** Nozzle too hot, not enough retraction

**Solutions:**
1. **Lower nozzle temperature by 5°C**
2. **Increase retraction:** Look for `retraction_length` (increase 0.5-1.0mm)
3. **Increase retraction speed:** `retraction_speed` (faster = more effective)

---

### Layers Shifting / Layer Lines Visible

**Cause:** Acceleration too high, bed not level, or mechanical issue

**Solutions:**
1. **Reduce accelerations:** Lower `default_acceleration` by 2000-3000
2. **Use "Quiet" profile:** `0.20mm Quite-HQ` has lower accelerations
3. **Check bed level:** May have shifted during print
4. **Inspect mechanics:** Belt tension, verify no grinding sounds

---

### First Layer Perfect, Then Quality Drops

**Cause:** Bed cooling or nozzle offset issue

**Solutions:**
1. **Check Z-offset:** If second layer gabs exist, nozzle too high
2. **Verify bed temperature:** Should stay constant (not dropping)
3. **Ensure cooling fan ramp:** Fan should gradually increase, not blast immediately
4. **Layer 1 vs 2 settings:** Some profiles have different settings per layer

---

### Poor Surface Finish on Outer Walls

**Cause:** Speed too fast, cooling too aggressive, or line width mismatch

**Solutions:**
1. **Reduce outer wall speed:** Use profile with lower outer_wall_speed
2. **Adjust cooling:** Not too aggressive (prevent layer warping)
3. **Enable ironing:** Top surfaces especially benefit
4. **Try HQ profile:** 0.16mm HQ instead of 0.20mm Standard

---

### Brittle Prints (Snap Easily)

**Cause:** Infill too light, PLA instead of PETG, or under-extrusion

**Solutions:**
1. **Increase infill density:** 20% → 40-50% for functional parts
2. **Use PETG instead:** Much stronger than PLA
3. **Check flow ratio:** May be under-extruding (ratio too low)
4. **Test print:** 20mm cube solid (100% infill) to check extrusion

---

### Dimensional Inaccuracy

**Cause:** Flow ratio off, filament thickness varies, or bed leveling

**Solutions:**
1. **Calibrate flow:** Print test cube, measure with calipers
   - Too large: Reduce flow_ratio (0.98 → 0.95)
   - Too small: Increase flow_ratio (0.98 → 1.01)
2. **Verify filament diameter:** (Should be 1.75mm ± 0.03mm)
3. **Tight tolerances:** Use PLA or PETG (more stable than TPU)

---

## ADDING NEW FILAMENTS

### Scenario: You buy new PLA brand not in system

**Step 1: Find similar existing profile**
```
Example: You buy "NewBrand PLA"
Search: system/Anycubic/filament/ for "PLA"
Copy: Anycubic PLA @acbase.json (base profile)
```

**Step 2: Create new file in user folder**
```
user/651589/filament/NewBrand PLA.json
```

**Step 3: Minimal inheritance structure**
```json
{
  "type": "filament",
  "from": "User",
  "inherits": "Anycubic PLA @acbase",
  "name": "NewBrand PLA",
  "filament_vendor": "NewBrand",
  "compatible_printers": [
    "Anycubic Kobra S1 0.4 nozzle"
  ],
  // Override ONLY these (rest inherited):
  "nozzle_temperature": [210],  // Test your brand's ideal temp
  "filament_flow_ratio": [0.99]  // Default, adjust after test
}
```

**Step 4: Create .info metadata file**
```
user/651589/filament/NewBrand PLA.info
{
  "user_id": "651589",
  "timestamp": "2026-03-11T14:30:00Z",
  "sync_info": "create"
}
```

**Step 5: Test print and calibrate**
1. **Print 20×20×20mm cube at 220°C** (default PLA temp)
2. **Observe:**
   - Too much plastic? Reduce `nozzle_temperature` by 5°C, reprint
   - Too little plastic? Increase temp by 5°C, reprint
   - Find sweet spot (clean corners, good surface)
3. **Adjust flow ratio:**
   - Print 20×20×20mm SOLID cube (100% infill)
   - Measure each side with calipers
   - If 20.5mm: Too much extrusion, reduce ratio (0.99 → 0.97)
   - If 19.5mm: Too little, increase ratio (0.99 → 1.01)
4. **Save optimized values back to JSON**

**Step 6: Commit to git (optional but recommended)**
```bash
cd user/651589
git add filament/NewBrand*
git commit -m "Add NewBrand PLA (210°C, 0.99 flow)"
git push
```

---

## QUICK REFERENCE TABLES

### Temperature Quick Lookup

| Filament Type | Nozzle °C | Bed °C | Notes |
|---------------|-----------|--------|--------|
| PLA | 200-220 | 60 | Standard, room temp OK |
| PLA+ | 210-230 | 60 | 10-15°C hotter than PLA |
| PETG | 230-250 | 70-80 | **Bed CRITICAL @ 70-80°C** |
| PETG HS | 240-260 | 75-85 | Higher temps, test 5°C steps |
| TPU | 200-220 | 20-30 opt. | No bed heat OK, print 20-40mm/s |
| PLA Silk | 200-220 | 60 | Glossy finish, same as regular PLA |
| PLA-CF | 205-225 | 60 | Hardened nozzle REQUIRED |
| Nylon (PA) | 260-280 | 80-100 | Tough, slow printing |

### Nozzle Selection Quick Guide

**Brass (Factory Standard):**
- ✅ PLA, PLA+, PETG (non-abrasive), TPU
- ❌ PLA-CF, Glass-filled PETG, Nylon-CF
- ✅ Cost: Low
- ⚠️ Wear: Visible after 50+ hours with abrasives

**Hardened Steel:**
- ✅ All materials including PLA-CF, Glass-filled PETG
- ⚠️ Heat transfer slightly lower (may need +5°C)
- ✅ Cost: Higher
- ✅ Longevity: 500+ hours even with abrasives
- ✅ Recommended if: Using composite/abrasive materials often

---

## FILE ORGANIZATION REFERENCE

### Where Things Live

```
user/651589/
│
├── filament/                          # Material configurations
│   ├── README.md                      # ← Start here for filament guide
│   ├── base/                          # Inherited base profiles
│   ├── Anycubic ABS improved.json
│   ├── Overture PETG.json
│   ├── Prusament Galaxy PLA.json
│   └── [60+ profiles organized by brand]
│
├── machine/                           # Printer configurations
│   ├── base/                          # Custom base profiles
│   ├── Anycubic Kobra S1 0.4 nozzle - Brass.json
│   ├── Anycubic Kobra S1 0.4 nozzle - Hardened Steel.json
│   });

├── process/                           # Slicer settings
│   ├── base/                          # Custom inherited bases
│   ├── 0.08mm HQ.json
│   ├── 0.12mm HQ.json
│   ├── 0.16mm HQ.json
│   ├── 0.20mm Quite-HQ.json           # ⭐ YOUR DEFAULT
│   ├── 0.20mm SD.json
│   ├── 0.24mm Draft.json
│   ├── 0.28mm ExtraDraft.json
│   ├── Action Figures.json
│   ├── Miniatures (0.08mm).json
│   ├── Tools & Home Improvements.json
│   ├── Vase (Spiral).json
│   ├── Vase (hollow).json
│   └── [Other specializations]
│
├── .github/
│   ├── copilot-instructions.md        # ← THIS FILE
│   └── .gitignore
│
├── README.md                          # Quick start
└── QUICK_REFERENCE.md                 # At-a-glance charts
```

---

## SUMMARY

**Your Setup:**
- Primary printer: **Anycubic Kobra S1** (0.4mm brass nozzle)
- Secondary printer: **Anycubic Kobra X** (0.4mm nozzle)
- Configuration style: **Hierarchical inheritance** (reduces duplication)
- Primary default: **`0.20mm Quite-HQ`** (balanced quality + speed + quiet)

**To Start Printing:**
1. Choose machine (S1 or X)
2. Choose filament (brand + material type)
3. Choose process (layer height + purpose)
4. Slice and print!

**For Advanced Users:**
- Specialized profiles in process/ folder
- Add filaments by copying + modifying existing profiles
- Create new process profiles by inheriting + overriding
- All changes sync with git

**Questions?**
- Filament behavior: Check `filament/README.md`
- Process decisions: Check [Process Profile Selection](#process-profile-selection-guide)
- Specific issues: Check [Common Issues & Solutions](#common-issues--solutions)
- System architecture: See root `/copilot-instructions.md`

---

**Last Updated:** March 2026  
**Next Review:** June 2026 (or after major slicer update)
