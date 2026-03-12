# Prompt for External AI Optimization Review

You are reviewing a custom Anycubic Slicer profile ecosystem. I am providing two zip files:

- user.zip: contents of user/651589 (my custom overlays)
- anycubic.zip: contents of system/Anycubic (vendor/system defaults)

## Critical mapping rule

When a profile in user.zip has an inherits field:

1. First try to resolve the parent profile inside user.zip.
2. If not found, resolve it inside anycubic.zip.
3. Evaluate effective behavior using the full inheritance chain.

Do not analyze custom files in isolation without resolving inheritance.

## What this repository contains

### 1) Machine customizations (user/651589/machine)

Machine profiles are intentionally lightweight overlays on top of system machine defaults.

Main explicit custom overrides include:
- 0.2 brass:
  - lower min/max layer range
  - lower retraction length
- 0.4 brass and hardened steel:
  - default profile changed to 0.16mm Optimal
  - max layer height increased (0.28 -> 0.32)
  - retraction speed increased (40 -> 50)
  - wipe distance increased (1 -> 2)
  - retract restart extra increased (0 -> 0.04)
  - hardened steel variant sets nozzle_type=hardened_steel
- 0.6/0.8 brass and hardened steel:
  - retraction length typically increased (0.8 -> 1.0)
  - 0.6 brass explicitly sets nozzle_type=brass

Please assess whether these machine deltas are still optimal and identify any conflicts with downstream filament/process assumptions.

### 2) Filament customizations (user/651589/filament)

Filament system is multi-nozzle and printer-aware.

High-level model:
- KS1 0.4 custom profiles are the primary source family.
- 0.25 / 0.6 / 0.8 variants exist with nozzle-specific tuning.
- KSX variants exist separately from KS1 due machine/cooling differences.

Please review:
- temperature and flow consistency across nozzle sizes
- pressure advance trends across 0.25 -> 0.4 -> 0.6 -> 0.8
- consistency between PLA, PLA+, PETG, TPU, ASA, ABS families
- suitability of current material coverage by nozzle size

Material families in custom library include (not exhaustive):
- PLA, PLA+, Silk PLA
- PETG (regular, transparent, reinforced variants)
- TPU
- ABS
- ASA
- Nylon and specialty materials

Brand coverage includes many vendor-specific profiles (Anycubic, Creality, Elegoo, Overture, Prusament, iBOSS, etc.).

### 3) Process customizations (user/651589/process)

Process families:
- @ AC Base (shared process intent)
- @ AC 0.6mm (0.6 nozzle family)
- @ AC 0.25mm (fine-detail family)

Recent key work:
- Base process naming migration to @ AC Base
- Added missing 0.4 base profiles for Book Nook and Disney plates
- Added broad 0.6 family, including 0.32 Draft and 0.38 Draft
- Added 0.25 HQ/Optimal profiles for: 0.06, 0.08, 0.10, 0.12, 0.14
- Normalized HQ-vs-Optimal differences for 0.25 families to an 8-key pattern

Expected HQ vs Optimal difference keys in 0.25 pairs:
- default_acceleration
- outer_wall_acceleration
- outer_wall_speed
- inner_wall_acceleration
- inner_wall_speed
- gap_infill_speed
- internal_solid_infill_speed
- sparse_infill_speed

Please verify that no unintended extra differences remain.

### 4) S1 vs X unification strategy

Intentional approach:
- Filaments are separated by printer/nozzle (KS1 vs KSX).
- Processes are shared across printers for same nozzle size via compatible_printers.

Please validate this architecture and identify where printer-specific process forks might be justified.

## Review tasks for you

Perform a deep optimization and consistency review:

1. Build an inheritance-resolved model of effective settings for machine + filament + process combinations.
2. Detect contradictions across layers (machine vs filament vs process).
3. Detect duplicated overrides that could be removed safely.
4. Detect risky settings (stringing, poor bridging, support fusion, over-acceleration, thermal instability).
5. Propose improvements per material family (PLA/PLA+/PETG/TPU/ABS/ASA/Nylon).
6. Propose improvements per nozzle size (0.25/0.4/0.6/0.8).
7. Propose improvements per use-case process family (HQ/Optimal/Draft/PETG-specialized/special-purpose).
8. Flag any naming, compatibility, or inheritance integrity issues.
9. Recommend a minimal-change plan and an aggressive-optimization plan.

## Output format I want

Please provide:

1. Executive summary (top risks + top wins)
2. Findings table with severity (critical, major, minor, opportunity)
3. Concrete patch suggestions (exact keys and values to change)
4. Validation plan (small test matrix first, then full matrix)
5. Prioritized implementation roadmap

## Important constraints

- Preserve current naming conventions unless there is a strong reason to change.
- Preserve inheritance-first architecture.
- Prefer reducing overrides rather than adding new hard-coded values.
- Explain trade-offs explicitly (quality, strength, speed, reliability).
- If suggesting value changes, cite why using both print physics and observed profile patterns.
