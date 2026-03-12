# Copilot Instructions - User 651589 Anycubic Profiles

Last updated: 2026-03-12

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
- Keep KS1 and KSX nozzle suffix conventions.
- Do not collapse KS1 and KSX filament profiles into one file.
- Use one-level user inheritance:
  - KS1 0.25, 0.6, 0.8 must inherit matching KS1 0.4.
  - KSX 0.25, 0.6, 0.8 must inherit matching KSX 0.4.
  - KSX must never inherit KS1 user filaments.
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
