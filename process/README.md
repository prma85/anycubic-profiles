# Process Profiles Guide

Last updated: 2026-03-11
Scope: `user/651589/process`

## Overview

This folder contains custom process profiles organized as inheritance overlays on top of Anycubic system defaults.

Current inventory:
- Total JSON profiles: 65
- Shared base family (`@ AC Base`): 26
- 0.6mm family (`@ AC 0.6mm` plus legacy `@ 0.6mm`): 26
- 0.25mm family (`@ AC 0.25mm`): 13

Core strategy:
- Keep geometry and nozzle-specific physics in system parents whenever possible.
- Keep custom files focused on intent (quality, speed, special use cases).
- Use explicit naming to make nozzle context obvious.

## Naming Pattern

### Base family (cross-printer process intent)
- Pattern: `<profile> @ AC Base`
- Example: `0.16mm HQ @ AC Base`

### 0.6mm family
- Pattern: `<profile> @ AC 0.6mm`
- Legacy names still present for compatibility: `<profile> @ 0.6mm`
- Example: `0.24mm Draft @ AC 0.6mm`

### 0.25mm family
- Pattern: `<profile> @ AC 0.25mm`
- Example: `0.10mm HQ @ AC 0.25mm`

## Compatibility Pattern

Process profiles are intentionally shared between S1 and X for the same nozzle size.

### 0.4mm compatible_printers
- `Anycubic Kobra S1 0.4 nozzle`
- `Anycubic Kobra S1 0.4 nozzle - Brass`
- `Anycubic Kobra S1 0.4 nozzle - Hardened Steel`
- `Anycubic Kobra X 0.4 nozzle`

### 0.6mm compatible_printers
- `Anycubic Kobra S1 0.6 nozzle`
- `Anycubic Kobra S1 0.6 nozzle - Brass`
- `Anycubic Kobra S1 0.6 nozzle - Hardened Steel`
- `Anycubic Kobra X 0.6 nozzle`

### 0.25mm compatible_printers
- `Anycubic Kobra S1 0.25 nozzle`
- `Anycubic Kobra S1 0.25 nozzle - Brass`
- `Anycubic Kobra S1 0.25 nozzle - Hardened Steel`
- `Anycubic Kobra X 0.25 nozzle`

## New and Expanded Profile Sets

## 0.4mm base migration (`@ AC Base`)
- Standardized naming for custom base profiles.
- Added missing shared 0.4 process variants:
  - `Book Nook @ AC Base`
  - `Disney plates @ AC Base`
- These inherit from `0.28mm Standard @Anycubic Kobra S1 0.4 nozzle` and intentionally remove direct layer geometry overrides.

## 0.6mm expansion (`@ AC 0.6mm`)
- Generated from mapped system standards:
  - `0.18` family from `0.18mm Standard @Anycubic Kobra S1 0.6 nozzle`
  - `0.20` family from `0.20mm Standard @Anycubic Kobra S1 0.6 nozzle`
  - `0.24` family from `0.24mm Standard @Anycubic Kobra S1 0.6 nozzle`
  - `0.30/0.32/0.38` family from `0.30mm Standard @Anycubic Kobra S1 0.6 nozzle`
- Added new drafts:
  - `0.32mm Draft @ AC 0.6mm`
  - `0.38mm Draft @ AC 0.6mm`
- Support Z-distance sanity enforced:
  - `support_bottom_z_distance >= effective layer height`

## 0.25mm HQ/Optimal family
Added HQ and Optimal variants at:
- `0.06mm`
- `0.08mm`
- `0.10mm`
- `0.12mm`
- `0.14mm`

All 5 HQ/Optimal pairs now follow the same difference pattern.

## HQ vs Optimal: Key Differences (0.25mm family)

Across all 0.25mm pairs, HQ vs Optimal differs in exactly 8 keys:
- `default_acceleration`
- `outer_wall_acceleration`
- `outer_wall_speed`
- `inner_wall_acceleration`
- `inner_wall_speed`
- `gap_infill_speed`
- `internal_solid_infill_speed`
- `sparse_infill_speed`

### Shared behavior
- HQ keeps slower/more conservative walls and acceleration for quality.
- Optimal pushes inner wall and infill throughput for print time reduction.

### Value pattern
For `0.06` and `0.08`:
- HQ `sparse_infill_speed=150` vs Optimal `450`

For `0.10`, `0.12`, `0.14`:
- HQ `sparse_infill_speed=200` vs Optimal `130`

This asymmetry is intentional and inherited from the selected system template families.

## Regular vs PETG Process Behavior

The PETG variants are not simple copies; they explicitly tune adhesion risk, support release, and bridging.

Representative deltas observed in current profiles:
- Bridges:
  - PETG sets explicit `bridge_speed=30`
  - PETG sets explicit `bridge_flow=0.94`
- Supports:
  - PETG generally increases `support_object_xy_distance` (e.g., `0.7 -> 1`)
  - PETG slightly increases support Z gaps in some 0.20 profiles (`0.30 -> 0.32`)
- Throughput:
  - PETG commonly lowers some infill/internal speeds vs regular profiles
  - Outer wall speed can be profile-family dependent and is not globally slower in every layer family

In short:
- Regular profiles prioritize broader speed/quality balance.
- PETG profiles prioritize stability and release behavior where PETG tends to string, fuse supports, or sag bridges.

## Extension Rules (How To Add More)

When adding a new custom process profile:

1. Choose the correct system parent by nozzle and layer family.
2. Keep naming consistent:
- Base: `@ AC Base`
- 0.6: `@ AC 0.6mm`
- 0.25: `@ AC 0.25mm`
3. Keep `compatible_printers` aligned to nozzle size and include Kobra X.
4. Remove unnecessary geometry/nozzle-layer keys if parent already defines them.
5. Validate support spacing for the effective layer height.
6. Generate matching `.info` file with aligned ID/name.

## Validation Checklist

Before accepting a new or edited process profile:
- JSON parses successfully.
- `name`, filename, and `.info` basename match.
- `print_settings_id` is unique and coherent.
- `inherits` points to an existing parent profile.
- `compatible_printers` covers both S1 and X for that nozzle size.
- For 0.6: `support_bottom_z_distance >= effective layer height`.
- HQ/Optimal pairs only differ where intended.

## Related Docs

- Main repository guide: `../README.md`
- Quick operator guide: `../QUICK_REFERENCE.md`
- Filament strategy: `../filament/README.md`
- S1 vs X unification note: `../S1_VS_X_UNIFICATION.md`
