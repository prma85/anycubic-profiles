# Anycubic Custom Profiles - User 651589

Last updated: 2026-03-12

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
- Copilot overview: copilot-instructions.md
- Copilot authoring rules: .github/copilot-instructions.md
- External AI review prompt: AI_OPTIMIZATION_REVIEW_PROMPT.md

## Process Profile Status

Process library families:
- Base profiles (@ AC Base): shared process intent
- 0.6mm profiles (@ AC 0.6mm): thicker-layer speed family
- 0.25mm profiles (@ AC 0.25mm): fine-detail family

Completed work:
- Added missing 0.4 base variants for Book Nook and Disney plates.
- Expanded 0.6 families, including 0.32 and 0.38 draft tiers.
- Added 0.25 HQ and Optimal profiles at 0.06, 0.08, 0.10, 0.12, 0.14.
- Normalized 0.25 HQ vs Optimal differences to a consistent 8-key pattern.

### Quick Selection

Default profile: 0.20mm Quite-HQ @ AC Base

- Balanced daily use: 0.20mm Quite-HQ @ AC Base
- Best quality: 0.16mm HQ @ AC Base or 0.12mm HQ @ AC Base
- Fast output: 0.24mm General PETG @ AC Base or 0.28mm ExtraDraft @ AC Base
- Tiny detail: 0.08mm HQ @ AC 0.25mm
- Flexible: 0.20mm Optimal TPU @ AC Base
- Functional and strong: Tools & Home Improvements @ AC Base

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
- KS1 0.4mm and KSX 0.4mm are the base custom overlays for each printer family.
- 0.25mm, 0.6mm, and 0.8mm variants inherit from same-printer 0.4mm overlays.
- Variant files keep only keys that differ from their 0.4mm parent.
- Keep version in all filament profiles.

For full details and inventory, see filament/README.md.

## S1 vs X Strategy (Merged)

Core principle:
- Filaments remain split by printer and nozzle (KS1 vs KSX).
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

### Anycubic Kobra S1 0.2 nozzle - Brass
- max_layer_height: 0.18 -> 0.14
- min_layer_height: 0.05 -> 0.04
- retraction_length: 0.8 -> 0.4

### Anycubic Kobra S1 0.4 nozzle - Brass
- default_print_profile: 0.20 Standard -> 0.16mm Optimal
- max_layer_height: 0.28 -> 0.32
- retraction_speed: 40 -> 50
- retract_restart_extra: 0 -> 0.04
- wipe_distance: 1 -> 2

### Anycubic Kobra S1 0.4 nozzle - Hardened Steel
- Same as 0.4 brass, plus nozzle_type: brass -> hardened_steel

### Anycubic Kobra S1 0.6 nozzle - Brass
- nozzle_type: hardened_steel -> brass
- retraction_length: 0.8 -> 1.0

### Anycubic Kobra S1 0.8 nozzle - Brass and Hardened Steel
- retraction_length: 0.8 -> 1.0

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
