# Filament Configuration Guide - User 651589

Last updated: 2026-03-12
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

## Temperature and Delta Rules

- Apply HS +5 only to:
  - nozzle_temperature_HS
  - nozzle_temperature_initial_layer_HS
- Do not apply +5 to:
  - nozzle_temperature_range_low
  - nozzle_temperature_range_high
- Enforce thermal safety:
  - nozzle_temperature_initial_layer_HS <= nozzle_temperature_range_high

## Editing Workflow

1. Edit 0.4mm parent for shared material behavior.
2. Keep variant-only behavior in 0.25mm, 0.6mm, 0.8mm children.
3. Remove child keys identical to 0.4mm parent.
4. Validate inheritance targets and JSON syntax.
5. Refresh .info timestamps when bulk updates are made.

## Delta Audit Matrix (Merged)

Representative profiles were audited to confirm transition-driven behavior.

Scope:
- Printer context: KS1 variants (0.4mm, 0.6mm, 0.8mm, 0.25mm)
- System reference: Anycubic S1 and S1 Max profiles
- Keys checked: filament_flow_ratio, pressure_advance, filament_max_volumetric_speed, filament_change_length

Legend:
- Y = system transition contains a change for that key
- N = key exists but no system change
- NA = key not present in that system transition

| Profile                 | Family Ref        | User 0.4->0.6 (flow/PA/MVS/FCL) | System 0.4->0.6 | User 0.6->0.8 (flow/PA/MVS/FCL) | System 0.6->0.8 | User 0.4->0.25 (flow/PA/MVS/FCL) | System 0.4->0.25 |
| ----------------------- | ----------------- | ------------------------------- | --------------- | ------------------------------- | --------------- | -------------------------------- | ---------------- |
| Improved PETG           | Anycubic PETG     | +0.02 / -0.010 / -3 / add       | Y/Y/Y/Y         | 0 / +0.005 / 0 / keep           | N/Y/N/N         | 0 / -0.005 / lower / remove      | Y/Y/Y/NA         |
| Improved PLA            | Anycubic PLA      | n/a / n/a / n/a / add           | Y/Y/Y/Y         | n/a / n/a / n/a / keep          | Y/Y/Y/N         | n/a / n/a / n/a / remove         | Y/Y/Y/NA         |
| Improved PLA+           | Anycubic PLA+     | n/a / n/a / n/a / add           | Y/Y/Y/NA        | n/a / n/a / n/a / keep          | NA/NA/NA/NA     | n/a / n/a / n/a / remove         | Y/Y/Y/NA         |
| Anycubic ABS improved   | Anycubic ASA      | n/a / n/a / 0 / n/a             | Y/Y/Y/NA        | n/a / n/a / 0 / n/a             | Y/N/N/NA        | n/a / n/a / n/a / n/a            | Y/Y/Y/NA         |
| Overture High Speed TPU | Anycubic TPU      | 0 / +0.01 / 0 / remove          | N/Y/N/NA        | 0 / 0 / 0 / n/a                 | Y/Y/N/NA        | n/a / n/a / n/a / n/a            | Y/Y/Y/NA         |
| JustMaker PETG GF       | Anycubic PETG-CF  | +0.02 / -0.010 / n/a / add      | Y/Y/Y/NA        | 0 / +0.005 / n/a / keep         | NA/NA/NA/NA     | 0 / -0.005 / n/a / remove        | Y/Y/Y/NA         |
| Generic Silk PLA        | Anycubic PLA Silk | -0.02 / -0.020 / 0 / add        | Y/Y/Y/NA        | +0.02 / +0.035 / 0 / keep       | NA/NA/NA/NA     | 0 / 0 / lower / remove           | Y/Y/Y/NA         |
| eSun PLA-CF             | Anycubic PLA-CF   | n/a / -0.020 / 0 / add          | Y/Y/Y/NA        | n/a / +0.035 / 0 / keep         | NA/NA/NA/NA     | n/a / 0 / lower / remove         | Y/Y/Y/NA         |

Notes:
- n/a in user columns means key is not explicitly present and is inherited.
- add/keep/remove under FCL describes filament_change_length lifecycle.

## Validation Checklist

After filament edits, verify:
- JSON syntax parses successfully.
- Inheritance target exists.
- Profile IDs and info setting_id remain aligned.
- Compatibility matches printer and nozzle intent.
- Safety constraints remain valid.

