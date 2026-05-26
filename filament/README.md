# Filament Configuration Guide - User 651589

Last updated: 2026-05-25
Framework: Anycubic Slicer Next (OrcaSlicer-based)
Scope: Custom filament profiles for Anycubic Kobra S1 and Anycubic Kobra X

## Architecture Summary

Filaments are printer-scoped and nozzle-scoped.

Current inheritance model:
- KS1 0.4mm and KSX 0.4mm are custom overlay parents per material.
- KS1 0.25mm, 0.6mm, 0.8mm inherit from matching KS1 0.4mm.
- KSX 0.25mm, 0.6mm, 0.8mm inherit from matching KSX 0.4mm.
- Non-0.4 variants keep only keys that differ from their 0.4 parent.
- version is always retained.

This one-level user inheritance model was tested and confirmed to load correctly in the slicer UI.

## Naming Convention

[Material] @AC [Printer] [Nozzle Size]

Examples:
- Creality PLA @AC KS1 0.4mm
- Creality PLA @AC KS1 0.6mm
- Creality PLA @AC KSX 0.4mm
- Creality PLA @AC KSX 0.8mm

## Inventory Snapshot

Nozzle-family counts currently present:
- 0.4mm: 104
- 0.25mm: 90
- 0.6mm: 104
- 0.8mm: 102

## Key Rules

1. Keep KS1 and KSX separate.
2. Do not collapse printer families into one profile.
3. Keep .json and .info pairs synchronized.
4. Keep filament_settings_id, setting_id, and filename aligned.
5. Keep profile overrides minimal and intentional.
6. Never remove version.

## Nozzle Transition Rules

All non-0.4mm variants are derived from the matching 0.4mm parent by applying these deltas.
Rationale: larger nozzles extrude more plastic per unit time — the heater needs to be hotter to keep the melt fluid, the larger bead needs more cooling to solidify cleanly, wider orifices reduce pressure buildup (lower PA needed), and the larger melt reservoir increases oozing risk (more retraction). (Based on Prusa nozzle guide, Polymaker retraction wiki, Flashforge nozzle size guide.)

### PLA group (Regular, Matte, Silk, Metal, Glow, Translucent, CF)

| Parameter              | 0.25mm  | 0.6mm  | 0.8mm  |
|------------------------|---------|--------|--------|
| Pressure Advance       | ×1.5    | ×0.667 | ×0.333 |
| Flow Ratio             | +0.01   | −0.01  | −0.02  |
| Retraction Length      | −0.2mm  | +0.2mm | +0.4mm |
| Max Volumetric Speed   | cap 3   | ×1.25  | ×1.50  |
| All Nozzle Temp keys   | −5°C    | +5°C   | +10°C  |
| Fan Speed (max & min)  | −20pp   | +20pp  | +40pp  |

Subtype overrides (stacked on top of the table above):
- **Matte:** extra −0.01 flow (matte particles expand more)
- **Silk/Metal:** cap `filament_retraction_speed` at 30 mm/s for 0.6/0.8mm — these break if retracted too fast when cold
- **Translucent:** fan −10% extra, MVS −20% extra

### PETG group (Regular, High-Flow/Rapid, Translucent)

| Parameter              | 0.6mm   | 0.8mm  |
|------------------------|---------|--------|
| Pressure Advance       | ×0.60   | ×0.30  |
| Flow Ratio             | −0.02   | −0.04  |
| Retraction Length      | +0.4mm  | +0.8mm |
| Max Volumetric Speed   | ×1.25   | ×1.5   |
| All Nozzle Temp keys   | +10°C   | +15°C  |
| Fan Speed (max & min)  | +30pp   | +50pp  |

Subtype overrides:
- **High-Flow (Rapid, GF):** MVS result ×1.2
- **Translucent:** fan = 0%, MVS = 0.4mm value ×0.7

### TPU group (95A, HS, High Speed)

| Parameter              | 0.6mm  | 0.8mm  |
|------------------------|--------|--------|
| Pressure Advance       | ×0.50  | 0.000  |
| Flow Ratio             | none   | −0.01  |
| Retraction Length      | keep   | keep   |
| Max Volumetric Speed   | cap 5  | cap 7  |
| All Nozzle Temp keys   | +5°C   | +10°C  |
| Fan Speed (max & min)  | +20pp  | +40pp  |

Note: TPU is extruder-grip limited — even on 0.8mm nozzle, keep print speed ≤ 40–50 mm/s on the Kobra S1.

### Application notes

- "pp" = percentage points absolute (e.g. 40% + 20pp = 60%); fan clamped 0–100
- If 0.4mm retraction is nil/absent, use 0.8 mm as the baseline before applying the delta
- Temperature: shift all of `nozzle_temperature`, `nozzle_temperature_initial_layer`, `nozzle_temperature_HS`, `nozzle_temperature_initial_layer_HS`, `nozzle_temperature_range_high`, `nozzle_temperature_BRASS`, `nozzle_temperature_initial_layer_BRASS` — **never** change `nozzle_temperature_range_low`
- Round PA to 3 decimal places; flow ratio to 4 decimal places

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
- `fan_max_speed: 10`, `fan_min_speed: 5` — must be explicitly set; KSX system parent wrongly inherits 100/80
- `activate_air_filtration: 1` (KS1 only — KSX has no filtration hardware, parent defaults to 0)
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

| Filament Type             | KSX (mm³/s) | KS1 (mm³/s) |
|---------------------------|:-----------:|:-----------:|
| Rapid PLA / High Flow     | 23          | 27          |
| Rapid PLA+ / PLA+ 2.0     | 20          | 24          |
| Standard PLA+             | 16          | 19          |
| Standard PLA              | 13          | 16          |
| Matte PLA                 | 14          | 16          |
| Translucent PLA           | 15          | 17          |
| Silk / Dual Colour PLA    | 10          | 12          |
| Galaxy / Glitter PLA      | 13          | 15          |
| Glow in Dark PLA          | 13          | 15          |
| Carbon Fibre PLA (CF)     | 16          | 19          |
| Rapid PETG / HF / HS      | 18          | 21          |
| Standard PETG             | 13          | 15          |
| Translucent PETG          | 11          | 13          |
| PETG GF (Glass Fibre)     | 11          | 13          |
| PETG CF (Carbon Fibre)    | 12          | 14          |
| TPU Standard 95A          | 4           | 5           |
| TPU High Speed            | 8           | 10          |

**KSX note:** KSX profiles were not individually calibrated — values above are applied as reference baselines. KS1 values reflect actual calibration runs.

## Nozzle MVS Scaling Rules

When deriving nozzle variants from the 0.4mm parent MVS:

| Nozzle  | Multiplier | Notes |
|---------|-----------|-------|
| 0.25mm  | ×0.50     | **Always cap at 3 mm³/s** regardless of calculation |
| 0.4mm   | ×1.00     | baseline |
| 0.6mm   | ×1.25     | reduced wall friction |
| 0.8mm   | ×1.50     | much less back-pressure |

Physics: larger nozzle orifice → less wall friction → higher achievable flow. But thermal capacity limits still apply — the multipliers assume the same hotend.

## Profile Format Rules (slicer-compatible simplified format)

As of 2026-05-25 all profiles use the simplified format that matches what the slicer generates when editing through the UI:

1. **No header fields** — drop `type`, `setting_id`, `filament_id`, `instantiation`, `filament_type`, `bed_type`
2. **No redundant keys** — any key with the exact same value as the parent is removed
3. **Alphabetical order** — content keys (a–z), then identity keys (a–z): `filament_settings_id`, `filament_vendor`, `from`, `inherits`, `is_custom_defined`, `name`, `version`
4. `compatible_printers` is only present when it differs from parent

## Editing Workflow

1. Edit 0.4mm parent for shared material behavior.
2. Derive 0.25mm/0.6mm/0.8mm variants by applying the delta tables above.
3. Remove child keys identical to 0.4mm parent (keep only intentional differences).
4. Validate inheritance targets and JSON syntax.
5. Refresh .info timestamps when bulk updates are made.

## Validation Checklist

After filament edits, verify:
- JSON syntax parses successfully.
- Inheritance target exists.
- Profile IDs and info setting_id remain aligned.
- Compatibility matches printer and nozzle intent.
- Safety constraints remain valid.

