# Filament Configuration Guide - User 651589

Last updated: 2026-07-28
Framework: Anycubic Slicer Next (OrcaSlicer-based)
Scope: Custom filament profiles for Anycubic Kobra S1 and Anycubic Kobra X

## Architecture Summary

Filaments are printer-scoped. One profile per material per printer covers 0.4mm, 0.6mm, and 0.8mm nozzles via `compatible_printers`. A separate 0.25mm child profile captures the only genuine nozzle-size dependency.

Current inheritance model:
- KS1 and KX each have one base profile per material (no nozzle suffix for 0.4/0.6/0.8).
- 0.25mm inherits from the matching multi-nozzle parent and carries only its deltas.
- **Brand PLA profiles** inherit from `Improved PLA @AC KS1/KX` (not directly from system parent).
- **Brand PLA+ profiles** inherit from `Improved PLA+ @AC KS1/KX`.
- `EconoFil PLA` inherits from `Improved PLA` directly (already correct parent).
- **PLA Translucent profiles** inherit from `Improved PLA Translucent @AC KS1/KX`.
- **Brand PETG Translucent profiles** (Prusament, ESun, Sovol, IEMAI) inherit from `Improved PETG Translucent @AC KS1/KX` (not directly from system parent).
- Specialty PLA (Matte, Silk, Galaxy, Metal, Glow) retain system specialty parents with explicit bed temp overrides.
- 0.25mm variants keep only keys that differ from their multi-nozzle parent.
- version is always retained.

This inheritance model was tested and confirmed to load correctly in the slicer UI.

## Naming Convention

Multi-nozzle profile (covers 0.4mm + 0.6mm + 0.8mm): `[Material] @AC [Printer]`
0.25mm child profile: `[Material] @AC [Printer] 0.25mm`

Examples:
- Creality PLA @AC KS1
- Creality PLA @AC KS1 0.25mm
- Creality PLA @AC KX
- Creality PLA @AC KX 0.25mm

## Inventory Snapshot

Profile counts currently present:
- Multi-nozzle (0.4/0.6/0.8mm): 104
- 0.25mm: 90

## Key Rules

1. Keep KS1 and KX separate.
2. Do not collapse printer families into one profile.
3. Keep .json and .info pairs synchronized.
4. Keep filament_settings_id, setting_id, and filename aligned.
5. Keep profile overrides minimal and intentional.
6. Never remove version.

## Nozzle Transition Rules (updated 2026-07-28)

Research finding: nozzle diameter does not require changes to temperature, MVS, flow ratio, or pressure advance when max volumetric speed is held constant. Filament dwell time in the melt zone depends on MVS / filament_cross_section — both independent of nozzle orifice size. Anycubic's own KX system profiles confirm this: flow, MVS, and PA are flat across 0.4/0.6/0.8mm; PETG temperature is identical at 230°C across all nozzle sizes.

**Profile structure:** One profile per material per printer covers 0.4mm + 0.6mm + 0.8mm via compatible_printers. A separate 0.25mm profile captures the only genuine nozzle-size dependency.

### 0.25mm deltas (vs the multi-nozzle parent profile)

| Parameter | 0.25mm |
|-----------|--------|
| Nozzle Temp (all keys) | −5°C |
| Max Volumetric Speed | cap 3 mm³/s |
| Retraction Length | −0.2mm |
| Flow Ratio | inherit (no change) |
| Pressure Advance | inherit (no change) |

Temperature delta shifts all of: `nozzle_temperature`, `nozzle_temperature_initial_layer`, `nozzle_temperature_HS`, `nozzle_temperature_initial_layer_HS`, `nozzle_temperature_range_high`, `nozzle_temperature_BRASS`, `nozzle_temperature_initial_layer_BRASS` — **never** change `nozzle_temperature_range_low`.

### 0.6mm and 0.8mm

No changes from the multi-nozzle parent profile values. These nozzle sizes are covered by the same profile file via compatible_printers.

## Bed Temperature Rules by Printer and Plate Type

### KS1 (CoreXY, high-speed, 600mm/s+) — differentiated by surface and layer

| Material | Smooth plate (PEO) first layer | Smooth plate other layers | Textured PEI first layer | Textured PEI other layers |
|---|---|---|---|---|
| PLA / PLA+ standard | 60°C | 55°C | 65°C | 60°C |
| PLA Matte / Silk / Galaxy | 60°C | 55°C | 65°C | 60°C |
| PLA Metal / Glow (filled) | 65°C | 60°C | 65°C | 60°C |
| PETG | 75–80°C | 70°C | 75–80°C | 70°C |
| TPU | 30°C | 30°C | 30°C | 30°C |

JSON keys: `hot_plate_temp_initial_layer` / `hot_plate_temp` (smooth), `textured_plate_temp_initial_layer` / `textured_plate_temp` (textured).

KS1 uses higher textured first-layer temp to lock filament into the texture ridges against the high-speed toolhead departing quickly. CoreXY edge-of-bed is ~10°C cooler than centre — the 5°C first-layer boost compensates.

### KX (Bedslinger, i3 Cartesian, 450mm/s) — flat temperature

| Material | All plate types, all layers |
|---|---|
| PLA / PLA+ standard | 60°C |
| PLA Matte / Silk / Galaxy | 60°C |
| PLA Metal / Glow (filled) | first layer 65°C, others 60°C |
| PETG | 70–75°C |
| TPU | 35°C |

KX uses flat 60°C because bedslinger thermal cycling during oscillation requires consistent bed heat. No first-layer/other-layer differentiation needed on smooth plate. Filled materials still get 65°C first layer to compensate particle heatsinks.

### EconoFil PLA (calibrated reference profile, 2026-07-01)

EconoFil is the calibrated reference for economic-tier PLA. Values below are the multi-nozzle profile anchors (apply unchanged to 0.4mm, 0.6mm, and 0.8mm). The 0.25mm child applies the standard 0.25mm deltas.

**KS1 0.4mm (brass nozzle)**:
- `nozzle_temperature`: 210°C, `nozzle_temperature_initial_layer_BRASS`: 220°C (first layer needs +10°C for PEI adhesion)
- `nozzle_temperature_HS`: 215°C (+5°C HS delta)
- `filament_flow_ratio`: 0.99, `pressure_advance`: 0.04, `filament_max_volumetric_speed`: 12
- Retraction: length 0.8, speed 40, deretraction 0, no wipe, no layer-change retract

**KX 0.4mm (hardened steel nozzle)**:
- `nozzle_temperature`: 210°C (this IS the HS print temp — the +5°C bump is baked in vs KS1's brass print value 205°C, since KX prints via HS keys)
- `filament_flow_ratio`: 0.99, `pressure_advance`: 0.025, `filament_max_volumetric_speed`: 12
- Retraction: length 1.2, speed 45, deretraction 30, z_hop_types "Slope Lift" (HS strings more; needs more aggressive retraction)

**Bed temps** (both printers): textured 65/70, hot 60-65/65, cool 45/45

### Improved PLA+ nozzle temperatures (KS1 calibrated, raised to KS1 high-speed spec)

- BRASS: 225°C all layers, HS: 230°C all layers
- `nozzle_temperature_range_high`: 240°C, `nozzle_temperature_range_low`: 225°C

(PLA+ at 205°C was calibrated for bedslingers — KS1 at 600mm/s needs 225°C minimum to maintain melt quality.)

## Improved Profile Baseline (2026-07-01)

Improved profiles act as the parent overlay for third-party filament of each material tier. When adding a new brand, inherit from `Improved [material] @AC [printer] 0.4mm` and only override truly brand-specific keys (density, cost, calibration deltas).

### Bed temperatures by material family

| Family | Textured (body/init) | Smooth PEI (body/init) | Cool plate (body/init) |
|---|---|---|---|
| PLA / PLA+ / PLA Silk Dual / PLA Translucent | 65 / 70 | 65 / 65 | 45 / 45 |
| PETG / PETG HS / PETG Translucent | (inherit 75) | (inherit 75) | 55 / 60 |

**PLA rationale**: textured init +5°C above body for reliable first-layer bond (validated against EconoFil calibration where 65°C init detached, 70°C held).
**PETG rationale**: leave hot/textured inheriting from Anycubic parent (75°C — correct for PETG). Cool plate 55/60 explicit because system defaults are wrong for PETG.

### PLA-family retraction pattern (EconoFil-calibrated)

Applied to Improved PLA, PLA+, PLA Silk Dual, PLA Translucent. The multi-nozzle parent carries the 0.4mm retraction anchor; the 0.25mm child applies −0.2mm retraction delta. PLA Silk Dual keeps `filament_z_hop_types: "Spiral Lift"` (multi-color needs spiral for color-swap wipe reduction) — all others use "Slope Lift".

| Key | KS1 (brass) | KX (HS) |
|---|---|---|
| `filament_retraction_length` | 0.8 | 1.2 |
| `filament_retraction_speed` | 40 | 45 |
| `filament_deretraction_speed` | 0 | 30 |
| `filament_retract_when_changing_layer` | 0 | 0 |
| `filament_retraction_minimum_travel` | 1 | 1 |
| `filament_wipe` | 0 | 0 |
| `filament_z_hop` | 0.4 | 0.4 |

KX values are more aggressive because HS nozzle strings more than brass at equivalent print temp.

### PETG-family retraction

PETG retraction is material-specific and left untouched by the Improved baseline — PETG runs cooler and wetter than PLA, needs slower/lower-magnitude retraction (deret 25, ret_spd 30). Only spurious "0" values are corrected (removed to allow parent inheritance).

## Hardened Steel Temperature Rules (within a single nozzle size)

- `nozzle_temperature_BRASS` = base temperature
- `nozzle_temperature_initial_layer_BRASS` = initial layer temperature
- `nozzle_temperature_HS` = base + 5°C (PLA) or base + 10°C (PETG)
- `nozzle_temperature_initial_layer_HS` = initial + 5°C (PLA) or initial + 10°C (PETG)
- Validate: `nozzle_temperature_initial_layer_HS` ≤ `nozzle_temperature_range_high`
- Do NOT change `nozzle_temperature_range_low`

## ABS / ASA Group Rules

ABS and ASA require special handling not covered by the PLA/PETG/TPU transition tables.

### Required settings (all ABS/ASA profiles)
- `fan_max_speed: 10`, `fan_min_speed: 5` — must be explicitly set; KX system parent wrongly inherits 100/80
- `activate_air_filtration: 1` (KS1 only — KX has no filtration hardware, parent defaults to 0)
- `activate_chamber_temp_control: 1`, `chamber_temperature: 55`
- `dont_slow_down_outer_wall: 1`

### Temperature baseline (Anycubic ABS improved)
- `nozzle_temperature: 255`, `nozzle_temperature_initial_layer: 255`
- `nozzle_temperature_HS: 260`, `nozzle_temperature_initial_layer_HS: 260` (+5°C HS rule applies)
- `hot_plate_temp: 105`, `hot_plate_temp_initial_layer: 105`

### Nozzle availability
- 0.4mm, 0.6mm, 0.8mm only — no 0.25mm for ABS/ASA

---

## Matte PLA Adhesion Rules

Matte PLA has lower inter-layer adhesion and is more vulnerable to early thermal contraction than regular PLA. All matte profiles must include:

- `close_fan_the_first_x_layers: 4` — no fan for first 4 layers prevents thermal shock detach
- `full_fan_speed_layer: 8` — gradual ramp from layer 4 to 8 instead of instant full fan
- `filament_z_hop: 0.6` — matte leaves larger ooze blobs on travel; 0.4mm is insufficient clearance
- `fan_max_speed: 80`, `fan_min_speed: 60` — matte surface degrades with over-cooling (vs 100/100 regular PLA)
- `fan_cooling_layer_time: 80` — shorter threshold (vs 100 for regular PLA)

These are validated against the Bambu A1 profile source and community OrcaSlicer practice. The fan reduction is intentional — matte pigment cools faster and over-cooling causes surface roughness.

---

## Cool Plate (Smooth PEI) Temperature Rules

The cool plate requires explicit temperature overrides — system parent values are often wrong.

| Material  | cool_plate_temp | cool_plate_temp_initial_layer | Notes |
|-----------|-----------------|-------------------------------|-------|
| PLA/PLA+  | (inherit 35)    | **40**                        | Must override initial layer to 40 |
| PETG      | **50**          | **50**                        | Both fields must be explicitly 50. Never use bare PEI — glue stick mandatory as release agent |
| TPU       | 30              | 30                            | Light adhesion for flexible parts |
| ABS/ASA   | (not applicable — use hot plate / textured plate) | | |

**PETG cool plate warning:** PETG bonds chemically to smooth PEI. At 70°C+ the bond becomes permanent and will tear the surface on removal. 50°C + glue stick is the safe combination.

## Reference MVS Table (0.4mm nozzle)

Calibrated baselines for high-speed Klipper printers (Kobra S1 has ~15% higher flow capacity than Kobra X due to better hotend thermistors/heater).

| Filament Type             | KX (mm³/s) | KS1 (mm³/s) |
|---------------------------|:-----------:|:-----------:|
| Rapid PLA / High Flow     | 23          | 27          |
| Rapid PLA+ / PLA+ 2.0     | 20          | 24          |
| Standard PLA+             | 16          | 19          |
| Standard PLA              | 13          | 16          |
| Matte PLA                 | 14          | 16          |
| Translucent PLA           | 8           | 8           |
| Silk / Dual Colour PLA    | 10          | 12          |
| Galaxy / Glitter PLA      | 13          | 15          |
| Glow in Dark PLA          | 13          | 15          |
| Carbon Fibre PLA (CF)     | 16          | 19          |
| Rapid PETG / HF / HS      | 18          | 21          |
| Standard PETG             | 13          | 15          |
| Translucent PETG          | 5           | 5           |
| PETG GF (Glass Fibre)     | 11          | 13          |
| PETG CF (Carbon Fibre)    | 12          | 14          |
| TPU Standard 95A          | 4           | 5           |
| TPU High Speed            | 8           | 10          |

**KX note:** KX values are reference baselines (not individually calibrated). KS1 values reflect actual calibration runs — do not change KS1 MVS without test print evidence.

*Translucent MVS values are clarity-mode caps. These profiles trade throughput for optical clarity (fan=0%, low speed, high temp). Standard translucent at normal speeds would use the previous 15/17 and 11/13 values.*

## Translucent Clarity Profile Rules

Translucent filaments require a fundamentally different approach from opaque materials. The goal is a single optical block, not fast throughput. Source: Bambu wiki on transparent PETG printing.

### Why fan=0%
Cooling fan freezes the extruded bead before it can fully flatten and fuse with the previous layer, trapping micro-bubbles. At 0% fan, layers melt into each other forming one continuous mass.

### PLA Translucent settings (Improved PLA Translucent base)
| Parameter | Value |
|---|---|
| `nozzle_temperature` (body) | 230°C (Brass) |
| `nozzle_temperature_initial_layer` | 235°C (Brass) |
| `nozzle_temperature_HS` / `_initial_layer_HS` | +5°C on each |
| `fan_max_speed` / `fan_min_speed` | 0% (all nozzle types) |
| `filament_flow_ratio` | 1.01 |
| `filament_max_volumetric_speed` | 8 mm³/s (flat across all nozzle sizes) |

### PETG Translucent settings (Improved PETG Translucent base)
| Parameter | KS1 value | KX value |
|---|---|---|
| `nozzle_temperature` (body, 0.4mm Brass) | 260°C | 252°C |
| `nozzle_temperature_initial_layer` | 260°C | 252°C |
| `nozzle_temperature_HS` / `_initial_layer_HS` | +10°C | +10°C |
| `fan_max_speed` / `fan_min_speed` | 0% | 0% |
| `filament_max_volumetric_speed` | 5 mm³/s (flat across all nozzle sizes) | 5 mm³/s (flat across all nozzle sizes) |

KX runs ~8°C cooler than KS1 to prevent heat-creep in the multi-channel ACE toolhead at slow print speeds.

### Nozzle size and translucent variants
Translucent profiles use the same temperature and MVS values for 0.4mm, 0.6mm, and 0.8mm nozzles. The 0.25mm child inherits the standard 0.25mm deltas (−5°C, MVS cap 3 mm³/s, −0.2mm retraction).

### Brand profiles
All brand PETG translucent profiles (Prusament, ESun, Sovol, IEMAI) inherit from `Improved PETG Translucent @AC KS1/KX 0.4mm`. Brands with their own calibrated temps (Sovol 235°C, IEMAI 250°C) keep explicit temp overrides in their profiles.

## Nozzle MVS Rules (updated 2026-07-28)

MVS is flat across 0.4mm, 0.6mm, and 0.8mm nozzles — no multipliers apply. Dwell time in the melt zone is determined by MVS / filament_cross_section, which is independent of nozzle orifice size at constant MVS.

The only adjustment is for 0.25mm: MVS is capped at 3 mm³/s regardless of the parent profile value (fine nozzle throughput constraint, not a thermal limit).

## Profile Format Rules (slicer-compatible simplified format)

As of 2026-05-25 all profiles use the simplified format that matches what the slicer generates when editing through the UI:

1. **No header fields** — drop `type`, `setting_id`, `filament_id`, `instantiation`, `filament_type`, `bed_type`
2. **No redundant keys** — any key with the exact same value as the parent is removed
3. **Alphabetical order** — content keys (a–z), then identity keys (a–z): `filament_settings_id`, `filament_vendor`, `from`, `inherits`, `is_custom_defined`, `name`, `version`
4. `compatible_printers` is only present when it differs from parent

## Editing Workflow

1. Edit the multi-nozzle parent (no nozzle suffix) for all shared material behavior — this covers 0.4mm, 0.6mm, and 0.8mm nozzles.
2. If a 0.25mm child exists, verify it contains only: −5°C temp, MVS cap 3 mm³/s, −0.2mm retraction length. Remove any other keys that now match the parent.
3. Validate inheritance targets and JSON syntax.
4. Refresh .info timestamps when bulk updates are made.

## Validation Checklist

After filament edits, verify:
- JSON syntax parses successfully.
- Inheritance target exists.
- Profile IDs and info setting_id remain aligned.
- Compatibility matches printer and nozzle intent.
- Safety constraints remain valid.

