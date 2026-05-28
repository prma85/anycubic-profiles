# Anycubic Custom Profiles - User 651589

Last updated: 2026-05-27

## Repository Purpose

This folder contains custom Anycubic Slicer Next overlays:
- machine/: hardware and nozzle machine overrides
- filament/: material and brand calibrations
- process/: print strategy profiles (quality, speed, use-case)

Design goal:
- Keep custom values where improvements are proven.
- Inherit from parent profiles for everything else.
- Keep process strategies reusable across Kobra S1 and Kobra X for the same nozzle size when practical.

## Documentation Map

- Main architecture and status: README.md
- Process details: process/README.md
- Filament details: filament/README.md
- Copilot instructions: .github/copilot-instructions.md
- External AI review prompt: AI_OPTIMIZATION_REVIEW_PROMPT.md

## Process Profile Status

Process library families:
- Base profiles (@ AC Base): 31 profiles, shared KS1+KX intent
- 0.6mm profiles (@ AC 0.6mm): 24 profiles
- 0.8mm profiles (@ AC 0.8mm): 2 profiles (Large Object family)
- 0.25mm profiles (@ AC 0.25mm): 13 profiles
- Named specialty: 6 profiles

### Quick Selection

Default profile: 0.20mm HQ @AC Base

| Use case | Profile |
|---|---|
| Balanced daily use | `0.20mm HQ @AC Base` |
| Best quality | `0.16mm HQ @ AC Base` or `0.12mm HQ @ AC Base` |
| Ultra-fine detail | `0.08mm HQ @ AC 0.25mm` |
| Fast draft | `0.28mm ExtraDraft @ AC Base` |
| TPU flexible | `0.20mm Optimal TPU @ AC Base` |
| Functional/strong | `Tools & Home Improvements @ AC Base` |
| Batch flexi parts (20–30 pieces) | `Batch Flexi @ AC Base` (0.12mm) or `Batch Flexi 0.16mm @ AC Base` |
| Large single object (60%+ plate) | `Large Object @ AC Base` / `@ AC 0.6mm` / `@ AC 0.8mm` |
| PETG quality | `0.20mm HQ PETG @ AC Base` |
| PETG speed / Rapid PETG | `0.20mm Optimal PETG @ AC Base` |
| PETG draft | `0.24mm Draft PETG @ AC Base` |
| ABS / ASA | `0.20mm ABS-ASA @ AC Base` (KS1 only) |
| Miniatures | `Miniatures @ AC Base` |

### 0.25 HQ vs Optimal Rule

HQ and Optimal should differ only on:
- default_acceleration
- outer_wall_acceleration
- outer_wall_speed
- inner_wall_acceleration
- inner_wall_speed
- gap_infill_speed
- internal_solid_infill_speed
- sparse_infill_speed

### PETG vs Regular Process Intent

PETG process variants intentionally diverge in bridge and support behavior. Preserve explicit PETG bridge tuning and support-release spacing unless a change is explicitly requested.

## Filament Strategy Summary

Filaments are printer and nozzle scoped because thermal and cooling behavior is hardware dependent.

Current model:
- KS1 0.4mm and KX 0.4mm are the base custom overlays for each printer family.
- 0.25mm, 0.6mm, and 0.8mm variants inherit from same-printer 0.4mm overlays.
- Standard PLA brands inherit from `Improved PLA @AC KS1/KX 0.4mm` rather than directly from the system parent, giving a deeper chain that carries calibrated retraction, z-hop, fan, and temperature settings.
- Variant files keep only keys that differ from their 0.4mm parent.
- Keep version in all filament profiles.

For full details and inventory, see filament/README.md.

## S1 vs X Strategy (Merged)

Core principle:
- Filaments remain split by printer and nozzle (KS1 vs KX).
- Processes are mostly shared by nozzle family through compatible_printers.

Why:
- Material behavior is strongly printer dependent (thermal path, cooling path, pressure behavior).
- Print intent profiles are more transferable between S1 and X for the same nozzle diameter.

When to break process unification:
- Repeatable platform-specific failures that cannot be fixed at machine or filament layer.
- Persistent support-release defects tied to one platform.
- Platform-specific resonance requiring process acceleration policy split.

## Machine Custom Settings vs System Defaults

Machine files are lightweight overlays, not full forks.
All KS1 machine profiles set `printer_flush_multiplier: 0.9` (system default 1.0 — reduced 10% for filament economy while remaining safe for multi-colour).

### Anycubic Kobra S1 0.2 nozzle - Brass
- max_layer_height: 0.14, min_layer_height: 0.04
- retraction_length: 0.4 (finer nozzle needs less retraction)
- printer_flush_multiplier: 0.9

### Anycubic Kobra S1 0.4 nozzle - Brass
- default_print_profile: 0.16mm Optimal
- max_layer_height: 0.32
- retraction_speed: 50, wipe_distance: 2
- printer_flush_multiplier: 0.9

### Anycubic Kobra S1 0.4 nozzle - Hardened Steel
- Same as 0.4 Brass + nozzle_type: hardened_steel

### Anycubic Kobra S1 0.6 nozzle - Brass / Hardened Steel
- z_hop: 0.6 (larger nozzle needs more clearance)
- retract_restart_extra: 0.06
- retraction_speed: 50
- printer_flush_multiplier: 0.9

### Anycubic Kobra S1 0.8 nozzle - Brass / Hardened Steel
- retract_lift_above: 0.5 (Brass) / 0.6 (HS)
- retract_restart_extra: 0.08
- retraction_speed: 60, wipe_distance: 2
- printer_flush_multiplier: 0.9

### Anycubic Kobra X 0.4 nozzle - Stainless Steel
- nozzle_type: stainless_steel
- No flush_multiplier override (inherits system default 1.0 — KX was working correctly)

## Numeric Tuning Validation Checklist (Merged)

Any numeric tuning proposal must pass all required gates before values are changed.

Required gate sequence:
1. Data integrity
2. Inheritance resolution
3. Scope discipline
4. Baseline behavior characterization
5. Constraint compliance
6. Comparative justification
7. Cross-profile consistency
8. Risk scoring and rollback plan
9. Test matrix proposal
10. Output contract

Mandatory failure conditions:
- unresolved inheritance chain
- missing effective baseline
- missing rule-check report
- protected family consistency regressions without rationale
- missing rollback plan

If any required gate fails, status must be: STOP - insufficient validation.

## How user and system work together

Custom files in user/651589 are overlays, while vendor defaults live under system/Anycubic.

Rule of thumb:
- If a key is absent in a custom profile, parent behavior applies.
- If a key is present, custom value overrides parent behavior.

This keeps maintenance manageable while preserving targeted custom tuning.
