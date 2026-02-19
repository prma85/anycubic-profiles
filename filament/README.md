# Filament Configurations

This folder contains optimized filament profiles for the **Anycubic Kobra S1 (0.4mm brass nozzle)** running **Anycubic Slicer Next** (OrcaSlice-based).

Each filament profile includes:

- Nozzle and bed temperature settings (optimized for the specific material and brand)
- Material-specific extrusion rates and flow adjustments
- Pressure advance settings for consistent extrusion
- Vitrification temperature (for proper cooldown)

---

## Quick Selection Guide

### By Material Type

**Choose this if you know your material type and want all available options.**

#### 🔵 **PLA** (Polyactic Acid) - General Purpose, Beginner-Friendly

Default temperature: 200-220°C | Bed: 60°C

- Creality PLA (various types)
- Eleego Metal PLA
- Geetech PLA (silk and standard)
- Generic PLA variants
- iBOSS Silk PLA
- Improved PLA @AC KS1
- JustMaker Silk PLA
- Polymaker PLA
- Prusament Galaxy PLA

**Recommended Process Profiles:** `0.16mm Optimal`, `0.20mm Quit-HQ`, `0.20mm SD`

---

#### 🟢 **PLA+** (Enhanced PLA) - Better Strength and Temperature Resistance

Default temperature: 210-230°C | Bed: 60°C

- Creality PLA+
- Elegoo Rapid PLA+
- iBoss Matte PLA+
- Improved PLA+ @AC KS1
- Overture PLA Pro
- Sunlu PLA+
- UJOYBIO PLA+

**Recommended Process Profiles:** `0.16mm Optimal PLA+`, `0.20mm Quit-HQ`

**Note:** PLA+ prints hotter and may require 5-10°C higher nozzle temperature than standard PLA.

---

#### 🔴 **PETG** (Polyethylene Terephthalate Glycol) - Strong, Durable

Default temperature: 230-250°C | Bed: 70-80°C

- AzureFilm PETG
- Creality CR-PETG
- Creality PETG
- Elegoo Rapid PETG
- eSun Transparent PETG
- Geetech PETG (includes glass-filled variant)
- iBOSS Glitter PETG
- IEMAI Clear PETG
- Improved PETG @AC KS1
- JustMaker PETG GF
- Overture PETG
- Prusament PETG (standard, transparent, matte)
- Sovol PETG (standard, translucent gradient)
- TECBEARS Rapid PETG

**Recommended Process Profiles:** `0.20mm General PETG`, `0.24mm General PETG`, `0.28mm General PETG`

**Note:** Use hardened steel nozzle for glass-filled variants (JustMaker PETG GF). PETG requires careful bed leveling.

---

#### 🟠 **PETG HS/Hyper** (High Speed PETG) - Faster PETG Printing

Default temperature: 240-260°C | Bed: 75-85°C

- Creality Hyper PLA Galaxy
- Improved PETG HS @AC KS1

**Recommended Process Profiles:** `0.20mm General PETG`, `0.24mm General PETG`

**Note:** "Hyper" or "High Speed" variants need higher temperatures than standard PETG. Test temperature first on a small print.

---

#### 🟡 **TPU** (Thermoplastic Polyurethane) - Flexible, Rubber-like

Default temperature: 200-220°C | Bed: 20-30°C (optional)

- Overture High Speed TPU
- Overture TPU HS
- Overture TPU (95A durometer)
- Sovol TPU HS

**Recommended Process Profiles:** `0.20mm Optimal TPU`, `0.20mm Optimal TPU - Avoid Crossing Walls Off`

**Important Notes:**

- Print MUCH slower (20-40 mm/s)
- No bed heating required (cold bed recommended to prevent sticking issues)
- May require special handling or direct drive setup
- Use liberal supports
- Avoid crossing walls when possible

---

#### ⚫ **Specialty Materials**

**PLA Silk** (Glossy Finish PLA)

- Geetech PLA Silk
- Generic Silk PLA
- iBOSS Silk PLA
- JustMaker Silk PLA
- Recommended Process: `0.16mm Optimal Silk PLA`, `0.20mm Quit-HQ`
- Temperature: 200-220°C (same as PLA)

**PLA-CF** (Carbon Fiber Reinforced PLA)

- eSun PLA-CF
- Recommended Process: `0.20mm PLA-CF`
- Temperature: 205-225°C
- **Use hardened steel nozzle** (brass will wear quickly)

---

### By Brand

**Choose this if you have a specific brand/manufacturer and want to see all their variants.**

#### **AzureFilm**

- AzureFilm PETG

#### **Creality**

- Creality CR-PETG
- Creality Hyper PLA Galaxy
- Creality PETG
- Creality PLA+

#### **Eleego**

- Eleego Metal PLA

#### **Elegoo**

- Elegoo Rapid PETG
- Elegoo Rapid PLA+

#### **eSun**

- eSun PLA-CF (requires hardened steel nozzle)
- eSun Transparent PETG

#### **Geetech**

- Geetech PLA Silk
- Geetech PETG (includes GF variant)

#### **Generic**

- Generic PLA Miniatures
- Generic Silk PLA

#### **iBOSS**

- iBOSS Glitter PETG
- iBoss Matte PLA+
- iBOSS Silk PLA

#### **IEMAI**

- IEMAI Clear PETG

#### **Improved** (Anycubic Slicer Optimization)

- Improved PETG @ AC KS1 0.4 nozzle
- Improved PETG HS @ AC KS1 0.4 nozzle
- Improved PETG Translucent @ AC KS1 0.4 nozzle
- Improved PLA @AC KS1 0.4 nozzle
- Improved PLA+ @AC KS1 0.4 nozzle

#### **JustMaker**

- JustMaker PETG GF (glass-filled, use hardened nozzle)
- JustMaker Silk PLA

#### **Overture**

- Overture High Speed TPU
- Overture PETG
- Overture PLA Pro
- Overture TPU HS
- Overture TPU (95A)

#### **Polymaker**

- Polymaker PLA
- Polymaker PLA Pro

#### **Prusament** (Prusa Research)

- Prusament Galaxy PETG
- Prusament Galaxy PLA
- Prusament Matte PETG
- Prusament PETG
- Prusament Transparent PETG

#### **Sovol**

- Sovol TPU HS
- Sovol Translucent Gradient PETG

#### **Sunlu**

- Sunlu PLA+
- Sunlu TPU 95a

#### **TECBEARS**

- TECBEARS Rapid PETG

#### **UJOYBIO**

- UJOYBIO PLA+

---

## How to Use Filament Profiles

### 1. **Find Your Filament**

First, locate your filament file in this folder by brand or material type.

### 2. **Select in Slicer**

In Anycubic Slicer Next:

1. Load your 3D model
2. Select **Filament** → Choose your filament profile
3. Select **Process** → Choose appropriate layer height profile
4. Select **Machine** → Choose your nozzle type (Brass by default, Hardened Steel for abrasive materials)

### 3. **Adjust if Needed**

Most profiles are pre-optimized, but you may need to adjust:

- **Nozzle Temperature:** ±5-10°C based on ambient temperature and print results
- **Bed Temperature:** ±5°C if you're having adhesion/warping issues
- **Flow Rate:** If prints are over/under-extruded (check first layers on large prints)

---

## Temperature Guidelines by Material

| Material     | Nozzle Temp | Bed Temp         | Notes                                     |
| ------------ | ----------- | ---------------- | ----------------------------------------- |
| **PLA**      | 200-220°C   | 60°C             | Standard temp, reduce if stringing/oozing |
| **PLA+**     | 210-230°C   | 60°C             | Runs hotter, better layer adhesion        |
| **PETG**     | 230-250°C   | 70-80°C          | Steep temp curve, test 5°C increments     |
| **PETG HS**  | 240-260°C   | 75-85°C          | Requires significantly higher temps       |
| **TPU**      | 200-220°C   | 20-30°C optional | Print much slower, no heating needed      |
| **PLA Silk** | 200-220°C   | 60°C             | Same as PLA, beautiful glossy finish      |
| **PLA-CF**   | 205-225°C   | 60°C             | Abrasive, use hardened steel nozzle       |

---

## Nozzle Type Selection

### 🔵 Brass Nozzle (Default)

- Standard, general-purpose
- Good thermal transfer
- Affordable
- Dies quickly with abrasive materials
- **Use for:** PLA, PLA+, PETG, TPU, Silk PLA (most prints)

### 🔧 Hardened Steel Nozzle (Specialty)

- Extremely durable
- Slightly lower heat transfer (may need +5°C)
- Better for abrasive filaments
- More expensive
- **Use for:** PLA-CF, glass-filled PETG (JustMaker PETG GF)

---

## Storage & Handling Tips

- **Keep filament dry:** Store in sealed containers with desiccant packs
- **Temperature:** Room temperature, away from sunlight
- **Humidity:** <15% RH ideal (use dehydrator if filament has absorbed moisture)
- **TPU special care:** Can be hygroscopic; dry before use or print may fail
- **PETG hygroscopic:** Can absorb moisture; dry at 80°C for 4-6 hours if stored long

---

## Troubleshooting by Material

### **PLA Issues**

- **Stringing:** Usually temp too high. Reduce by 5°C or increase retraction.
- **Warping:** Normal for large prints at room temp; use brim on large bases.
- **Poor layer adhesion:** Usually not an issue; increase bed temp to 65°C if needed.

### **PETG Issues**

- **Warping:** Most common. Ensure bed is precisely level; clean with IPA.
- **Stringy:** Temperature too high. Reduce 5°C, increase retraction.
- **Curled edges:** Use brim, print slower outer walls, reduce nozzle temp.
- **Oozing:** Temp or retraction setting; try "Quit-HQ" profile for better settings.

### **TPU Issues**

- **Failing to print:** Usually nozzle pressure too high. Print at 20-30 mm/s outer wall.
- **Stringing:** Normal for TPU; increase retraction or enable "Avoid Crossing Walls."
- **Clogging:** Moisture in filament. Dry before use.
- **Not sticking:** Cold bed intentionally; ensure first layer is working despite.

---

## Profile Version Info

- All filament profiles inherit from base Anycubic configurations
- Specific optimizations added for Kobra S1 (0.4mm brass nozzle)
- Compatible with Kobra 3, Kobra 2, and Kobra X (check "compatible_printers" in .json)
- Version timestamps indicate last update time

---

## Adding New Filaments

When adding a new filament:

1. Create two files: `Brand Material.json` and `Brand Material.info`
2. Use an existing filament as a template
3. Update temperatures based on manufacturer specs
4. Test on small prints first
5. Document in this README under the appropriate material type and brand

---

## References

- Default nozzle height: 0.4mm (brass or hardened steel)
- Default bed size: 220x220x250mm (Kobra S1)
- Hot end: Standard Anycubic (compatible with OrcaSlice profiles)
- Slicer: Anycubic Slicer Next v1.3+/2.3+
