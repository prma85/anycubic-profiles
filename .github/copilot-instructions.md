# Copilot Instructions - User 651589 Anycubic Profiles

Last updated: 2026-03-11

## Purpose

These instructions guide AI-assisted edits to custom Anycubic Slicer profiles in user/651589.

Primary objective:
- Preserve inheritance-driven architecture.
- Apply small, auditable overrides.
- Keep S1 and X behavior unified where intended.

## Read This First

Before editing profiles, read:
- ../copilot-instructions.md (high-level map)
- ../README.md (repository-level architecture)
- ../filament/README.md (filament strategy)
- ../process/README.md (process families and tuning rules)
- ../S1_VS_X_UNIFICATION.md (why filaments split and process can unify)

## Folder Responsibilities

- machine/: printer/nozzle hardware overlays
- filament/: material behavior calibration
- process/: quality/speed/use-case presets

Do not mix responsibilities between layers unless explicitly required.

## Naming and Structure Rules

### Process
- Base family: <name> @ AC Base
- 0.6 family: <name> @ AC 0.6mm
- 0.25 family: <name> @ AC 0.25mm
- Keep .json and .info pairs synchronized.

### Filament
- Keep existing KS1/KSX and nozzle suffix conventions.
- Do not collapse KS1 and KSX filament profiles into a single file.

### Machine
- Keep overrides minimal.
- Avoid duplicating system values unless intentional for lock-in.

## Compatibility Rules

For process profiles:
- Include Kobra X in compatible_printers for the same nozzle size.
- Keep S1 brass/hardened variants listed where used.

For filament profiles:
- Keep printer-specific compatibility due thermal/cooling differences.

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

For 0.6 profiles:
- Ensure support_bottom_z_distance >= effective layer height.

## Regular vs PETG Intent

PETG process variants intentionally diverge from regular profiles in bridge/support behavior and selected speeds.

When creating or editing PETG variants:
- Preserve explicit bridge tuning (for example, bridge_speed and bridge_flow).
- Preserve support release spacing where defined.
- Do not force PETG to match regular profile speeds blindly.

## Change Discipline

When editing JSON profiles:
- Keep IDs coherent and unique.
- Keep parent inheritance valid.
- Prefer removing redundant keys to rely on parent defaults.
- Avoid introducing unrelated formatting changes.

## Validation Checklist

After changes, verify:
- JSON syntax is valid.
- Name/filename/info alignment is correct.
- Inheritance targets exist.
- Compatibility lists match intended nozzle and printer scope.
- HQ/Optimal and PETG rules remain consistent.

## External Analysis Context

If preparing data for external AI analysis with zipped inputs:
- user.zip = custom overlays (user/651589/*)
- anycubic.zip = system defaults (system/Anycubic/*)
- Treat inherits in user.zip as references to files in anycubic.zip when parent is not present in user.zip.
