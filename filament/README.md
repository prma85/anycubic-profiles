# Filament Configuration Guide - User 651589

Last updated: 2026-05-11
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
| Max Volumetric Speed   | cap 3   | ×1.2   | ×1.4   |
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

