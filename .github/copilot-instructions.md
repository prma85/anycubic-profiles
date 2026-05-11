# Copilot Instructions - User 651589 Anycubic Profiles

Last updated: 2026-05-11

## Purpose

These instructions guide AI-assisted edits to custom Anycubic Slicer profiles in user/651589.

Primary objectives:
- Preserve inheritance-driven architecture.
- Apply small, auditable overrides.
- Keep S1 and X behavior unified where intended.

## Read This First

Before editing profiles, read:
- ../copilot-instructions.md (high-level map)
- ../README.md (repository architecture)
- ../filament/README.md (filament strategy)
- ../process/README.md (process families and tuning rules)

## Folder Responsibilities

- machine/: printer and nozzle hardware overlays
- filament/: material behavior calibration
- process/: quality, speed, and use-case presets

Do not mix responsibilities between layers unless explicitly required.

## Naming and Structure Rules

### Process
- Base family: <name> @ AC Base
- 0.6 family: <name> @ AC 0.6mm
- 0.25 family: <name> @ AC 0.25mm
- Keep .json and .info pairs synchronized.

### Filament
- **Naming:** All brand/material names MUST start with uppercase (ESun, IBOSS, IBoss, not ESun, IBoss, IBoss)
- Keep KS1 and KSX nozzle suffix conventions.
- Do not collapse KS1 and KSX filament profiles into one file.
- Use one-level user inheritance:
  - KS1 0.25, 0.6, 0.8 must inherit matching KS1 0.4.
  - KSX 0.25, 0.6, 0.8 must inherit matching KSX 0.4.
  - KSX must never inherit KS1 user filaments.
- **Nozzle transition rules (applied relative to 0.4mm parent values):**

  **PLA group** (Regular, Matte, Silk, Metal, Glow, Translucent, CF):
  | Parameter                  | 0.25mm  | 0.6mm   | 0.8mm   |
  |----------------------------|---------|---------|---------|
  | Pressure Advance           | ×1.5    | ×0.667  | ×0.333  |
  | Flow Ratio                 | +0.01   | −0.01   | −0.02   |
  | Retraction Length          | −0.2mm  | +0.2mm  | +0.4mm  |
  | Max Volumetric Speed       | cap 3   | ×1.2    | ×1.4    |
  | Nozzle Temp (all temp keys)| −5°C    | +5°C    | +10°C   |
  | Fan (max & min speed)      | −20pp   | +20pp   | +40pp   |
  - Matte subtype: apply extra −0.01 to flow ratio
  - Silk/Metal subtype: cap filament_retraction_speed at 30 mm/s for 0.6/0.8mm

  **PETG group** (Regular, High-Flow/Rapid, Translucent):
  | Parameter                  | 0.6mm   | 0.8mm   |
  |----------------------------|---------|---------|
  | Pressure Advance           | ×0.60   | ×0.30   |
  | Flow Ratio                 | −0.02   | −0.04   |
  | Retraction Length          | +0.4mm  | +0.8mm  |
  | Max Volumetric Speed       | ×1.25   | ×1.5    |
  | Nozzle Temp (all temp keys)| +10°C   | +15°C   |
  | Fan (max & min speed)      | +30pp   | +50pp   |
  - High-Flow subtype (Rapid, GF): multiply MVS result by additional ×1.2
  - Translucent subtype: set fan to 0%, set MVS to 0.4mm value ×0.7

  **TPU group** (95A, HS, High Speed):
  | Parameter                  | 0.6mm   | 0.8mm   |
  |----------------------------|---------|---------|
  | Pressure Advance           | ×0.50   | 0.000   |
  | Flow Ratio                 | no change| −0.01  |
  | Retraction Length          | keep    | keep    |
  | Max Volumetric Speed       | cap 5   | cap 7   |
  | Nozzle Temp (all temp keys)| +5°C    | +10°C   |
  | Fan (max & min speed)      | +20pp   | +40pp   |

  **Important:** "pp" = percentage points (absolute, not relative). All fan values clamped 0–100.
  Retraction: if the 0.4mm value is nil/absent, use 0.8mm as the baseline before applying the delta.
  Temperature: shift nozzle_temperature, nozzle_temperature_initial_layer, nozzle_temperature_HS,
    nozzle_temperature_initial_layer_HS, nozzle_temperature_range_high,
    nozzle_temperature_BRASS, nozzle_temperature_initial_layer_BRASS — all by the same delta.
    Do NOT change nozzle_temperature_range_low.

- **Temperature rules (Hardened Steel offset, within a single nozzle size):**
  - nozzle_temperature_BRASS = nozzle_temperature (base)
  - nozzle_temperature_initial_layer_BRASS = nozzle_temperature_initial_layer
  - nozzle_temperature_HS = base + 5 (PLA) or base + 10 (PETG)
  - nozzle_temperature_initial_layer_HS = initial + 5 (PLA) or initial + 10 (PETG)
  - Validate: nozzle_temperature_initial_layer_HS <= nozzle_temperature_range_high
  - Do NOT change range_low
- **Material restrictions by nozzle:**
  - 0.25mm: PLA only (no PETG, TPU, specialty)
  - 0.4mm: All materials (primary calibration)
  - 0.6mm: All materials
  - 0.8mm: PLA, PETG, TPU
- Keep child variants minimal:
  - Remove keys identical to inherited effective values.
  - Keep only intentional differences.
  - Never remove version.
- .info must be plain key-value with sync_info=create and aligned setting_id.
- Deltas must remain type-specific and printer-aware.
- filament_change_length must only be added or kept when justified by system transitions.

### Machine
- Keep machine overrides minimal.
- Avoid duplicating system values unless intentional for lock-in.

## Compatibility Rules

For process profiles:
- Include Kobra X in compatible_printers for the same nozzle size.
- Keep S1 brass and hardened variants listed where used.

For filament profiles:
- Keep printer-specific compatibility due thermal and cooling differences.

## 0.25 HQ vs Optimal Rule

For the five 0.25 pairs (0.06/0.08/0.10/0.12/0.14), HQ and Optimal should differ only on:
- default_acceleration
- outer_wall_acceleration
- outer_wall_speed
- inner_wall_acceleration
- inner_wall_speed
- gap_infill_speed
- internal_solid_infill_speed
- sparse_infill_speed

Any additional differences should be treated as regression unless explicitly requested.

## 0.6 Safety Rule

For 0.6 process profiles:
- Ensure support_bottom_z_distance >= effective layer height.

## Regular vs PETG Intent

PETG process variants intentionally diverge from regular profiles in bridge and support behavior.

When creating or editing PETG variants:
- Preserve explicit bridge tuning.
- Preserve support release spacing where defined.
- Do not force PETG to match regular profile speeds blindly.

## Change Discipline

When editing JSON profiles:
- Keep IDs coherent and unique.
- Keep inheritance targets valid.
- Prefer removing redundant keys to rely on parent defaults.
- Avoid unrelated formatting churn.

## Validation Checklist

After changes, verify:
- JSON syntax is valid.
- Name, filename, and info alignment are correct.
- Inheritance targets exist.
- Compatibility lists match intended nozzle and printer scope.
- HQ/Optimal and PETG rules remain consistent.
- For filament variants:
  - All non-0.4 variants inherit matching 0.4 parent.
  - BRASS and HS temperature key intent remains intact where required.
  - HS initial temperature does not exceed range high.
  - Keys identical to inherited values are removed except required metadata.

## External Analysis Context

If preparing data for external AI analysis with zipped inputs:
- user.zip = custom overlays (user/651589/*)
- anycubic.zip = system defaults (system/Anycubic/*)
- Resolve inherits in user.zip by checking user.zip first, then anycubic.zip.
