# Kobra S1 vs Kobra X Unification Strategy

Last updated: 2026-03-11

## Why this document exists

Your custom setup uses two similar printers (Kobra S1 and Kobra X) but does not treat all profile layers the same way.

- Filaments stay separated by printer/nozzle family.
- Process profiles are mostly unified by nozzle family.

This is intentional and based on where behavior differences matter most.

## Core principle

- Material physics and cooling behavior are strongly printer-dependent.
- Print intent (HQ, Optimal, Draft, PETG support strategy) is mostly transferable between S1 and X for same nozzle diameter.

Therefore:
- Split filament profiles by printer/nozzle.
- Share process profiles across printers with nozzle-matched compatible_printers.

## Key S1 vs X machine-level differences (system defaults)

Representative differences from Anycubic Kobra S1 0.4 nozzle vs Anycubic Kobra X 0.4 nozzle:

- Motion envelope and aggressiveness:
  - S1 has significantly higher acceleration limits in defaults.
  - X defaults are more conservative in acceleration/speeds.
- Cooling path:
  - S1 enables auxiliary fan in machine defaults.
  - X disables auxiliary fan.
- Startup/toolchange/end G-code:
  - S1 and X use different machine G-code templates.
- Extruder/kinematic guard values:
  - Several jerk/speed/clearance-related defaults differ.

These differences justify machine and filament separation.

## Why filament profiles are separated

Filament profiles contain parameters that directly interact with printer-specific thermal and flow behavior:
- nozzle temperature curves
- pressure advance behavior
- cooling behavior assumptions
- max volumetric flow behavior

Even small platform/cooling differences can shift optimal values, so KS1 and KSX filament families remain separate.

## Why process profiles can be unified

Process profiles mostly encode print intent:
- layer-family choice
- wall/infill speed posture
- quality vs throughput trade-offs
- support/bridge strategy for model classes

By keeping process overlays inheritance-first and nozzle-scoped, you can safely share them across S1 and X while machine + filament layers absorb hardware/material-specific behavior.

## How unification is implemented

### Process level
- 0.4 base process profiles include both S1 and X 0.4 entries.
- 0.6 process profiles include both S1 and X 0.6 entries.
- 0.25 process profiles include both S1 and X 0.25 entries.

### Filament level
- KS1 and KSX variants remain distinct.
- Inheritance is used to reduce duplication while preserving printer deltas.

## Benefits of this split approach

- Less profile sprawl in process layer.
- Better safety in material-specific tuning.
- Easier maintenance because each layer has a clear responsibility.
- Faster onboarding for future edits and AI-assisted optimization.

## When to break unification

Create printer-specific process forks only if a repeatable issue appears that cannot be solved in machine/filament layers, for example:
- persistent overhang failures only on one printer with multiple materials
- repeatable support-release defects tied to one platform kinematics
- platform-specific resonance that requires process acceleration policy differences
