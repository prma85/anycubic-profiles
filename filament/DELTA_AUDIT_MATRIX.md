# Delta Audit Matrix (Representative Profiles)

This matrix validates that generated nozzle variants are transition-driven, not blanket-scaled.

Scope:

- Printer context: KS1 variants (`@AC KS1 Base`, `0.6mm`, `0.8mm`, `0.25mm`)
- System reference for transition presence: Anycubic S1 and S1 Max profiles
- Keys checked: `filament_flow_ratio`, `pressure_advance`, `filament_max_volumetric_speed`, `filament_change_length`

Legend:

- `Y` = system transition contains a change for that key
- `N` = system transition has key but no change
- `NA` = key not present in that system transition

## Matrix

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

- `n/a` in user columns means that key is not explicitly present in that user profile and therefore inherited from parent.
- `add/keep/remove` under FCL means `filament_change_length` was introduced, kept, or absent/removed in the destination profile.
- Matrix is representative and intended for architecture verification, not as a replacement for per-file numerical validation.

## Safety Checks (Current State)

- `nozzle_temperature_range_high` on generated `0.6mm`/`0.8mm`: PASS
- `nozzle_temperature_initial_layer_HS <= nozzle_temperature_range_high`: PASS
- `.info setting_id` aligned to `filament_settings_id`: PASS
