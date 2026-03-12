# Anycubic Kobra S1/Kobra X - Quick Reference

Default profile: 0.20mm Quite-HQ @ AC Base

## Fast Selection

- Balanced daily use: 0.20mm Quite-HQ @ AC Base
- Best quality: 0.16mm HQ @ AC Base or 0.12mm HQ @ AC Base
- Fast output: 0.24mm General PETG @ AC Base or 0.28mm ExtraDraft @ AC Base
- Tiny detail: 0.08mm HQ @ AC 0.25mm
- Flexible: 0.20mm Optimal TPU @ AC Base
- Functional/strong: Tools & Home Improvements @ AC Base

## Process Families

- Base: @ AC Base
- 0.6: @ AC 0.6mm
- 0.25: @ AC 0.25mm

## 0.25 HQ vs Optimal (Quick Rule)

HQ and Optimal differ only on speed/acceleration-oriented keys:
- default_acceleration
- outer_wall_acceleration, outer_wall_speed
- inner_wall_acceleration, inner_wall_speed
- gap_infill_speed, internal_solid_infill_speed, sparse_infill_speed

## PETG vs Regular (Quick Rule)

PETG process variants generally add/adjust:
- explicit bridge tuning (bridge_speed, bridge_flow)
- support release spacing (support_object_xy_distance, support Z gaps)
- selected throughput reductions for stability

## Where to read details

- Main guide: README.md
- Process details: process/README.md
- Filament details: filament/README.md
- S1 vs X strategy: S1_VS_X_UNIFICATION.md
- Copilot overview: copilot-instructions.md
- Copilot authoring rules: .github/copilot-instructions.md
