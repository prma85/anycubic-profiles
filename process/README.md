# Process Profiles Guide

Last updated: 2026-06-02
Scope: `user/651589/process`

## Overview

Custom process profiles organised as inheritance overlays on top of Anycubic system defaults.

Current inventory:
- Total JSON profiles: 86
- Base family (`@ AC Base`): 37
- 0.6mm family (`@ AC 0.6mm`): 27
- 0.8mm family (`@ AC 0.8mm`): 2 (Large Object only)
- 0.25mm family (`@ AC 0.25mm`): 13
- Other/named specialty: 9

Core strategy:
- Inherit geometry and nozzle physics from system parents.
- Custom files encode intent (quality, speed, use-case), not hardware.
- Process profiles are shared between KS1 and KX via `compatible_printers`.
- Where KX needs different process behaviour, a KX-specific profile inherits the base and overrides only what differs.

## Naming Pattern

| Family | Pattern | Example |
|---|---|---|
| 0.4mm cross-printer | `<profile> @ AC Base` | `0.16mm HQ @ AC Base` |
| 0.6mm nozzle | `<profile> @ AC 0.6mm` | `0.24mm Draft @ AC 0.6mm` |
| 0.8mm nozzle | `<profile> @ AC 0.8mm` | `Large Object @ AC 0.8mm` |
| 0.25mm nozzle | `<profile> @ AC 0.25mm` | `0.10mm HQ @ AC 0.25mm` |
| Named specialty | `<Use Case> @ AC <family>` | `Batch Flexi @ AC Base` |

## Compatibility Pattern

All process profiles list both S1 and X for the same nozzle size.

### 0.4mm `compatible_printers`
```json
["Anycubic Kobra S1 0.4 nozzle",
 "Anycubic Kobra S1 0.4 nozzle - Brass",
 "Anycubic Kobra S1 0.4 nozzle - Hardened Steel",
 "Anycubic Kobra X 0.4 nozzle",
 "Anycubic Kobra X 0.4 nozzle - Stainless Steel"]
```

### 0.6mm `compatible_printers`
```json
["Anycubic Kobra S1 0.6 nozzle",
 "Anycubic Kobra S1 0.6 nozzle - Brass",
 "Anycubic Kobra S1 0.6 nozzle - Hardened Steel"]
```
*(KX 0.6mm added when a KX-specific 0.6mm profile is created)*

### 0.25mm `compatible_printers`
```json
["Anycubic Kobra S1 0.25 nozzle",
 "Anycubic Kobra S1 0.25 nozzle - Brass",
 "Anycubic Kobra S1 0.25 nozzle - Hardened Steel"]
```

## Profile Families

### Standard layer height families (0.4mm nozzle)

| Layer | Profile name | Use case |
|---|---|---|
| 0.06–0.14mm | `0.XXmm HQ/Optimal @ AC 0.25mm` | Ultra-fine 0.25mm nozzle detail |
| 0.08mm | `0.08mm HQ/Optimal @ AC Base` | Extreme detail, 0.4mm nozzle |
| 0.12mm | `0.12mm HQ/Optimal @ AC Base` | High detail |
| 0.16mm | `0.16mm HQ @ AC Base` | Daily quality |
| 0.16mm | `0.16mm Optimal @ AC Base` | Daily quality, faster |
| 0.16mm | `0.16mm Optimal Silk PLA @ AC Base` | Silk PLA speed |
| 0.20mm | `0.20mm HQ @AC Base` | Standard balanced |
| 0.20mm | `0.20mm SD @ AC Base` | Standard + lower density |
| 0.24mm | `0.24mm HQ @ AC Base` | Fast quality |
| 0.24mm | `0.24mm Draft @ AC Base` | Draft speed |
| 0.28mm | `0.28mm ExtraDraft @ AC Base` | Draft max |

### PETG profiles — HQ / Optimal / Draft pattern

**Design principle:** Speeds are set high. The filament's `filament_max_volumetric_speed` automatically caps the actual speed. Regular PETG (MVS 10–12) will be slower than Rapid PETG (MVS 18–21) on the same Optimal profile — no separate profile needed per filament brand.

**0.4mm nozzle:**

| Layer | Profile | Outer | Inner | Intent |
|---|---|---|---|---|
| 0.16mm | `0.16mm HQ PETG @ AC Base` | 80 | 150 | Quality |
| 0.16mm | `0.16mm Optimal PETG @ AC Base` | 150 | 200 | Fast, MVS-capped |
| 0.20mm | `0.20mm HQ PETG @ AC Base` | 60 | 100 | Quality/slow |
| 0.20mm | `0.20mm Optimal PETG @ AC Base` | 150 | 200 | Fast — daily driver for Rapid PETG |
| 0.24mm | `0.24mm HQ PETG @ AC Base` | 50 | 70 | Quality/slow |
| 0.24mm | `0.24mm Draft PETG @ AC Base` | 200 | 300 | Max throughput |
| 0.28mm | `0.28mm HQ PETG @ AC Base` | 60 | 90 | Quality/slow |
| 0.28mm | `0.28mm Draft PETG @ AC Base` | 200 | 300 | Max throughput |
| 0.28mm | `0.28mm PETG @AC KS1` | inherit | inherit | Minimal wrapper |
| 0.28mm | `0.28mm PETG (strong) @AC KS1` | 100 | 150 | Max walls/shells |

**0.6mm nozzle:**

| Layer | Profile | Outer | Inner | Intent |
|---|---|---|---|---|
| 0.18mm | `0.18mm HQ PETG @ AC 0.6mm` | 80 | 150 | Quality |
| 0.18mm | `0.18mm Optimal PETG @ AC 0.6mm` | 150 | 200 | Fast |
| 0.20mm | `0.20mm HQ PETG @ AC 0.6mm` | 60 | 110 | Quality |
| 0.20mm | `0.20mm Optimal PETG @ AC 0.6mm` | 150 | 200 | Fast |
| 0.24mm | `0.24mm HQ PETG @ AC 0.6mm` | 80 | 120 | Quality |
| 0.24mm | `0.24mm Draft PETG @ AC 0.6mm` | 200 | 350 | Max throughput |

PETG profiles use: jerk=6, `bridge_flow: 0.94`, `bridge_speed: 30`, `support_object_xy_distance: 0.7–1.0`, support z-distances 0.24–0.30mm (larger than PLA to prevent PETG fusing to part), `overhang_reverse: 1`, `wipe_before_external_loop: 1`.

### TPU profiles (0.4mm nozzle)

| Profile | Notes |
|---|---|
| `0.20mm Optimal TPU @ AC Base` | Standard TPU, reduce_crossing_wall off |
| `0.20mm Optimal TPU - Avoid Crossing Walls Off @ AC Base` | TPU without wall avoidance |

### Specialty / use-case profiles

| Profile | Inherits | Purpose |
|---|---|---|
| `Batch Flexi @ AC Base` | 0.12mm Standard | 20–30 flexi/articulated PLA parts simultaneously (0.12mm, 0.5mm walls, no support, gyroid, slow_down_layers=4) |
| `Batch Flexi 0.16mm @ AC Base` | Batch Flexi @ AC Base | Same as above at 0.16mm, slightly faster |
| `Large Object @ AC Base` | 0.16mm Standard | Single print covering 60%+ of plate (outer brim, slow first layer, variable layer height base) |
| `Large Object @ AC 0.6mm` | Large Object @ AC Base | Large objects, 0.6mm nozzle, 0.24mm layer |
| `Large Object @ AC 0.8mm` | Large Object @ AC Base | Large objects, 0.8mm nozzle, 0.32mm layer |
| `Action Figures @ AC Base` | 0.12mm Standard | Detailed figures with ironing |
| `Miniatures @ AC Base` | 0.08mm Standard | Ultra-detail 0.08mm, fine line widths |
| `Custom Pokeballs @ AC Base` | 0.08mm Standard | Spherical multi-colour models |
| `Goffy Figures` | 0.12mm Standard | Figure quality at moderate speed |
| `Book Nook @ AC Base/0.6mm` | 0.28mm Standard | Large decorative scenes |
| `Disney plates @ AC Base/0.6mm` | 0.28mm Standard | Flat plate art |
| `Rubber Duck @ AC Base/0.25mm/0.6mm` | 0.08mm Standard | Multi-colour toy with exclude_object |
| `Layered Art` | — | Layered colour art |
| `Vase (Spiral) @ AC Base/0.6mm` | — | Single-perimeter spiral mode |
| `Vase (hollow) @ AC Base/0.6mm` | — | Hollow vase with minimal shell |
| `0.10mm Translucent Vase @ AC Base` | `Vase (Spiral) @ AC Base` | Glass-clarity hollow objects — 18mm/s, fan=0% implied by filament, vase/spiral mode |
| `0.10mm Translucent Solid @ AC Base` | `0.20mm Optimal PETG @ AC Base` | Glass-clarity solid objects — 18mm/s, 100% alignedrectilinear infill, 0 top/bottom shells, +4% flow |

## Universal Settings Applied to All Profiles

These are explicit in every non-excluded profile (not relying on system defaults):

| Setting | Value | Why |
|---|---|---|
| `reduce_crossing_wall` | `1` | Routes travel along walls instead of over infill — prevents nozzle hitting infill peaks |
| `reduce_infill_retraction` | `0` | Retracts before all infill travel — prevents ooze blobs that nozzle clips |
| `max_travel_detour_distance` | `300` | Caps detour search at 300mm for consistent travel pathfinding |
| `seam_gap` | `10%` | Consistent seam closure across all profiles |
| `wipe_on_loops` | `1` | Wipes nozzle tip before each outer wall (excluded: 0.06/0.08mm fine detail) |

## Support Settings (updated 2026-06-17)

All support-enabled profiles (non-TPU, non-vase, non-flexi) use:

| Setting | Value | Rationale |
|---|---|---|
| `support_interface_top_layers` | `3` | Dense separation surface for clean removal |
| `support_interface_bottom_layers` | `2` or `3` | Match top layers — explicit, not -1 |
| `support_interface_spacing` | `0.5mm` | Standard spacing; 0.2mm was too dense and caused adhesion |
| `support_interface_pattern` | `rectilinear_interlaced` | Alternating perpendicular layers, no gaps |
| `support_interface_speed` | `40mm/s` (0.4mm), `45` (0.6mm), `50` (0.8mm) | Slow = flat interface, no curl; primary anti-adhesion mechanism |
| `support_speed` | `120` (0.4mm), `150` (0.6mm), `180` (0.8mm) | Body scaffolding can be fast |
| `bridge_flow` | `1.2` | Tested safe across all filament types (1.4 caused failures on some materials) |

**Z-distance rule** (proportional to layer height, capped):

- `support_bottom_z_distance` = layer_height, capped at **0.20mm**
- `support_top_z_distance`:
  - **HQ profiles** = same as bottom (= layer_height, capped 0.20)
  - **Optimal / SD / Draft profiles** = bottom + 0.02mm

| Layer | Bottom (all) | Top HQ | Top Optimal/Draft |
|---|---|---|---|
| 0.06mm | 0.06 | 0.06 | 0.08 |
| 0.08mm | 0.08 | 0.08 | 0.10 |
| 0.10mm | 0.10 | 0.10 | 0.12 |
| 0.12mm | 0.12 | 0.12 | 0.14 |
| 0.14mm | 0.14 | 0.14 | 0.16 |
| 0.16mm | 0.16 | 0.16 | 0.18 |
| 0.18mm (0.6mm nozzle) | 0.18 | 0.18 | 0.20 |
| 0.20mm | 0.20 | 0.20 | 0.22 |
| 0.24mm+ | **0.20** (capped) | **0.20** | **0.22** |

Rationale: bottom_z = layer_height means the support contacts at exactly one layer thickness — the minimum that prevents bonding while ensuring the first bridging layer lands on a stable surface. The +0.02 on top for Optimal/Draft accounts for slightly higher print speeds that can cause minor drooping.

PETG profiles intentionally deviate — they need larger z-gaps (0.16–0.20) to prevent PETG fusing to the support. Do not force PETG to match PLA values.

## HQ vs Optimal vs Draft

**PLA (0.25mm family):** Exactly 8 keys differ between HQ and Optimal:
`default_acceleration`, `outer_wall_acceleration`, `outer_wall_speed`,
`inner_wall_acceleration`, `inner_wall_speed`,
`gap_infill_speed`, `internal_solid_infill_speed`, `sparse_infill_speed`

**Acceleration rules:**
- **HQ profiles** — `default_acceleration: 4000`, `outer_wall_acceleration: 2000`. Low to avoid ringing at slow outer wall speeds.
- **Optimal / SD / Draft profiles** — `default_acceleration: 6500`. This is the Kobra X maximum; the S1 can go higher but profiles are shared, so 6500 is the ceiling. System Standard parents default to 10000 — always override explicitly.
- `smooth_coefficient: 30` on all HQ profiles (system default 80 causes visible layer marks at speed transitions on slow HQ prints; 30 ramps speed changes more gradually).

**PETG family:**
- **HQ** — quality/slow: outer 60–80, inner 70–150, `top_surface_speed` 45–60. Conservative acceleration (2000 outer, 4000 default).
- **Optimal** — fast, MVS-capped: outer 150, inner 200, infill 300. `default_acceleration: 6500`. With regular PETG (MVS 10–12) the slicer auto-caps speeds to ~120mm/s. With Rapid PETG (MVS 18–21) speeds are fully unleashed.
- **Draft** (0.24mm+) — max throughput: outer 200, inner 300–350. `default_acceleration: 6500`. Always MVS-capped regardless of filament.

**ABS/ASA family:**
- `0.20mm ABS-ASA @ AC Base` — slow speeds (outer 70, inner 110), jerk 6, accel 3500, 4 walls, 5 shells. KS1 only.
- `0.24mm ABS-ASA @ AC 0.6mm`, `0.32mm ABS-ASA @ AC 0.8mm` — same philosophy at larger nozzle sizes.

## Bambu Studio Migration (future)

Process profiles will need re-parenting to BBL equivalents when porting to BambuStudio.
See `../SKILLS.md` section 7 for the full migration guide including:
- Re-parenting map (KS1 → P1P/P1S, KX → A1)
- Keys to remove, change, and keep
- Process parent naming in BambuStudio
- Specialty profile handling for Batch Flexi and Large Object

The new specialty profiles (`Batch Flexi`, `Large Object`) should map to P1P/P1S process parents at the matching layer height, keeping all custom keys unchanged. BambuStudio supports `inherits` so the same overlay approach works.

## Validation Checklist

Before accepting any new or edited process profile:
- JSON parses successfully
- `name`, filename, and `.info` basename match
- `print_settings_id` is unique and coherent
- `inherits` points to an existing parent
- `compatible_printers` covers both S1 and X for that nozzle size
- `support_bottom_z_distance` = layer_height (capped 0.20)
- `support_top_z_distance` = layer_height for HQ, layer_height+0.02 for Optimal/Draft (both capped 0.20/0.22)
- `support_interface_spacing` is `0.5` (standard; 0.2mm was too dense)
- `reduce_crossing_wall: 1`, `reduce_infill_retraction: 0`, `max_travel_detour_distance: 300` present
- `seam_gap: 10%` and `wipe_on_loops: 1` present (except 0.06/0.08mm fine detail profiles)
- Matching `.info` file exists with aligned `setting_id`
