# Copilot Instructions — User 651589 Anycubic Profiles

Last updated: 2026-05-25

## Purpose

Authoritative editing policy for AI-assisted work on custom Anycubic Slicer profiles in `user/651589`.

For full slicer knowledge, printer differences, and material behaviour see **`../SKILLS.md`**.
For repository architecture and machine notes see **`../README.md`**.

---

## Documentation Map

| File | Purpose |
|------|---------|
| `SKILLS.md` | Complete knowledge base: hardware, filament logic, troubleshooting |
| `CLAUDE.md` | Claude Code instructions for this repository |
| `.github/copilot-instructions.md` | This file — editing policy and validation gates |
| `README.md` | Repository architecture, machine overrides, S1 vs X strategy |
| `filament/README.md` | Filament strategy, nozzle transition tables, inventory |
| `process/README.md` | Process families, HQ/Optimal rule, PETG intent |

---

## Primary Objectives

- Preserve inheritance-driven architecture — child files override only what differs
- Apply small, auditable overrides — no wholesale rewrites of parent content
- Keep KS1 and KX filament families strictly separate
- Keep process profiles shared between S1 and X for the same nozzle size

---

## Folder Responsibilities

- `machine/` — printer and nozzle hardware overlays only
- `filament/` — material behaviour calibration, printer-scoped
- `process/` — quality, speed, and use-case presets, nozzle-scoped

Do not mix responsibilities between layers.

---

## Naming Rules

### Filament
- Pattern: `[Brand] [Material] @AC [Printer]`
- For 0.25mm: `[Brand] [Material] @AC [Printer] 0.25mm`
- Examples: `Bambu PLA Matte @AC KX`, `Soleyin UF PLA @AC KS1`, `Bambu PLA Matte @AC KX 0.25mm`
- **Brand/material names MUST start with uppercase** (ESun not eSun, IBoss not iBOSS)
- KS1 and KX are separate — never merge into one file

### Process
- Base (0.4mm cross-printer): `[name] @ AC Base`
- 0.6mm: `[name] @ AC 0.6mm`
- 0.25mm: `[name] @ AC 0.25mm`

### Machine
- Pattern: `Anycubic [Model] [Nozzle] nozzle - [Material]`
- Example: `Anycubic Kobra S1 0.4 nozzle - Brass`

---

## Filament Inheritance Rules

```
KS1 system parent
    └── KS1 user profile  ← covers 0.4mm + 0.6mm + 0.8mm via compatible_printers
            └── KS1 user 0.25mm profile  ← inherits KS1 user profile

KX system parent
    └── KX user profile  ← covers 0.4mm + 0.6mm + 0.8mm via compatible_printers
            └── KX user 0.25mm profile  ← inherits KX user profile
```

- KX must **never** inherit from KS1 user profiles
- 0.25mm profiles keep only keys that differ from their parent (temp −5°C, MVS cap 3, retraction −0.2mm)
- `version` is always retained in every file

---

## Nozzle Transition Rules

**Research-backed finding (2026-07):** Nozzle diameter does not require changes to temperature, MVS, flow ratio, or pressure advance when max volumetric speed is held constant. At identical MVS, filament dwell time in the melt zone is determined only by MVS / filament_cross_section — both independent of nozzle orifice size. Anycubic's own KX system profiles confirm this: flow, MVS, and PA are identical across 0.4/0.6/0.8mm for every material; PETG temp is flat at 230°C across all nozzle sizes.

**Profile consolidation:** A single filament profile per material per printer covers 0.4mm, 0.6mm, and 0.8mm nozzles via `compatible_printers`. A separate 0.25mm profile is kept because it genuinely caps MVS and drops temp slightly.

### Deltas applied only at 0.25mm (vs 0.4mm parent)

| Parameter | 0.25mm |
|-----------|--------|
| Nozzle Temp (all keys) | −5°C |
| Max Volumetric Speed | cap 3 mm³/s |
| Retraction Length | −0.2mm |
| Flow Ratio | inherit (no change) |
| Pressure Advance | inherit (no change) |

### What does NOT change between 0.4/0.6/0.8mm

- Temperature: no change
- MVS: no change
- Flow ratio: no change
- Pressure advance: no change
- Retraction: inherit from parent (Anycubic uses nil for 0.6/0.8mm — same effect)
- Fan speeds: no systematic delta (0.8mm cooling behaviour is hotend/material-specific, not a rule)

**If retraction needs adjustment for a specific nozzle after empirical testing:** add it to the single multi-nozzle profile as an explicit override for that compatible_printers entry, or create a nozzle-specific variant only when empirically justified.

---

## Hardened Steel Temperature Rules (within a single nozzle size)

- `nozzle_temperature_BRASS` = base temperature
- `nozzle_temperature_initial_layer_BRASS` = initial layer temperature
- `nozzle_temperature_HS` = base + 5°C (PLA) or base + 10°C (PETG)
- `nozzle_temperature_initial_layer_HS` = initial + 5°C (PLA) or initial + 10°C (PETG)
- **Validate:** `nozzle_temperature_initial_layer_HS` ≤ `nozzle_temperature_range_high`
- **Never** change `nozzle_temperature_range_low`

---

## Cool Plate (Smooth PEI) Temperature Rules

System parent defaults are often wrong — explicit overrides are required:

| Material | `cool_plate_temp` | `cool_plate_temp_initial_layer` |
|----------|-------------------|---------------------------------|
| PLA/PLA+ | 35 (inherit — do not override) | **40** (must override explicitly) |
| PETG | **50** (must override) | **50** (must override) |
| TPU | 30 | 30 |

**PETG:** Bonds chemically to smooth PEI at 70°C+. Never inherit the system default (KX system parent has 70 — wrong). 50°C + glue stick is mandatory.

---

## KX Profile Derivation from KS1

When creating a KX profile based on a KS1 profile:
- **Apply** hardware-structural deltas: `additional_cooling_fan_speed=0`, `activate_air_filtration=0`, plate temp +5°C
- **Copy** calibration values: nozzle temps, MVS, retraction, fan speeds
- **Do not copy** `flow_ratio` and `pressure_advance` — let these inherit from the KX system parent
- **Do not copy** `adaptive_pressure_advance_model` — KX has its own PA characteristics

---

## Material Restrictions by Nozzle

- 0.25mm: PLA only
- 0.4mm: all materials
- 0.6mm: all materials
- 0.8mm: PLA, PETG, TPU only

---

## Process Profile Rules

- `compatible_printers` for 0.4mm base: include Kobra S1 (plain, Brass, Hardened Steel) and Kobra X
- HQ vs Optimal (0.25mm): must differ in exactly 8 keys — see `SKILLS.md` Section 9
- PETG process variants intentionally diverge in bridge and support — do not force to match regular

### Support Z distances

- `support_bottom_z_distance` = layer_height, capped at **0.20mm**
- `support_top_z_distance`:
  - **HQ profiles** = layer_height + 0.02mm
  - **Optimal / SD / Draft profiles** = layer_height + 0.05mm, capped at:
    - 0.30mm for 0.4mm and 0.25mm nozzle
    - 0.34mm for 0.6mm nozzle
    - 0.36mm for 0.8mm nozzle

| Layer | Bottom | Top HQ | Top Optimal/Draft (0.4mm) |
|---|---|---|---|
| 0.06mm | 0.06 | 0.08 | 0.11 |
| 0.08mm | 0.08 | 0.10 | 0.13 |
| 0.10mm | 0.10 | 0.12 | 0.15 |
| 0.12mm | 0.12 | 0.14 | 0.17 |
| 0.14mm | 0.14 | 0.16 | 0.19 |
| 0.16mm | 0.16 | 0.18 | 0.21 |
| 0.18mm | 0.18 | 0.20 | 0.23 |
| 0.20mm | 0.20 | 0.22 | 0.25 |
| 0.24mm+ | 0.20 (cap) | 0.26 | 0.29–0.30 (cap) |

PETG profiles deviate intentionally (larger gaps to prevent fusing) — do not force to match PLA.

### Acceleration

- **HQ** profiles: `default_acceleration: 4000`
- **Optimal / SD / Draft** profiles: `default_acceleration: 6500` — always set explicitly; system Standard parent inherits 10000 which exceeds Kobra X limit
- **HQ** profiles: `smooth_coefficient: 30` — reduces ringing from abrupt speed changes; system default 80 is too loose for slow HQ printing

### Bridge flow

- `bridge_flow: 1.2` on all PLA/TPU/ABS profiles — 1.4 caused failures on some filaments
- PETG profiles use `bridge_flow: 0.94` — do not change

---

## Machine Profile Rules

- Keep overrides minimal
- Avoid duplicating system values unless intentional for lock-in
- Do not modify `system/Anycubic/` files

---

## .info File Rules

Every `.json` profile must have a paired `.info`:
```
sync_info = create
user_id =
setting_id = <exact filename stem>
updated_time = <unix epoch>
```

---

## Change Discipline

- Keep child files minimal — remove keys that match parent exactly
- Keep IDs coherent: `name` = `filament_settings_id`/`print_settings_id` = filename stem = `.info` `setting_id`
- Prefer inheritance over duplication
- Stage only intentionally changed files in git commits
- Never commit gcode files

---

## Numeric Tuning Validation Gates

Any numeric tuning proposal must pass all gates before values are changed:

1. Data integrity — profile loads and resolves cleanly
2. Inheritance resolution — effective value confirmed at each level
3. Scope discipline — change applies only to intended profiles
4. Baseline behaviour characterization — current effective value documented
5. Constraint compliance — layer height, line width, volumetric limits checked
6. Comparative justification — rationale for new value vs baseline
7. Cross-profile consistency — related profiles checked for regressions
8. Risk scoring and rollback plan — impact assessment and revert path
9. Test matrix proposal — what to print and what to look for
10. Output contract — exactly which keys change, to what values, in which files

**Mandatory STOP conditions:** unresolved inheritance chain, missing effective baseline, missing rule-check report, protected family consistency regressions without rationale, missing rollback plan.

---

## Validation Checklist

After any change:
- [ ] JSON syntax valid
- [ ] `name` = filename stem exactly
- [ ] `filament_settings_id` / `print_settings_id` matches name
- [ ] `.info` exists with matching `setting_id`
- [ ] `inherits` target exists
- [ ] `compatible_printers` covers intended scope
- [ ] No keys duplicated from parent (except `version`)
- [ ] Hardened Steel temps correct
- [ ] `nozzle_temperature_initial_layer_HS` ≤ `nozzle_temperature_range_high`
- [ ] Layer height ≤ 0.75 × nozzle diameter
- [ ] `support_bottom_z_distance` = layer_height (capped 0.20)
- [ ] `support_top_z_distance` = HQ: layer+0.02; Optimal/Draft: layer+0.05 (cap 0.30/0.34/0.36 by nozzle)
- [ ] `default_acceleration`: HQ = 4000, Optimal/Draft = 6500 (never rely on inherited 10000)
- [ ] `smooth_coefficient: 30` present in all HQ profiles
- [ ] `bridge_flow: 1.2` on all non-PETG profiles
- [ ] For matte PLA: `close_fan_the_first_x_layers=4`, `full_fan_speed_layer=8`, `filament_z_hop=0.6`
