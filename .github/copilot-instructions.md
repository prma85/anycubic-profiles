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
- Pattern: `[Brand] [Material] @AC [Printer] [Nozzle]`
- Examples: `Elegoo PLA @AC KS1 0.4mm`, `Bambu PLA Matte @AC KX 0.4mm`
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
    └── KS1 user 0.4mm (editable parent overlay)
            ├── KS1 user 0.25mm  ← inherits KS1 0.4mm
            ├── KS1 user 0.6mm   ← inherits KS1 0.4mm
            └── KS1 user 0.8mm   ← inherits KS1 0.4mm

KX system parent
    └── KX user 0.4mm (editable parent overlay)
            ├── KX user 0.25mm  ← inherits KX 0.4mm
            ├── KX user 0.6mm   ← inherits KX 0.4mm
            └── KX user 0.8mm   ← inherits KX 0.4mm
```

Deeper chain for standard PLA brands:
```
System parent
    └── Improved PLA @AC KS1/KX 0.4mm  ← calibrated user base
            └── [Brand] PLA @AC KS1/KX 0.4mm  ← brand overlay
                    ├── [Brand] PLA @AC KS1/KX 0.25mm
                    ├── [Brand] PLA @AC KS1/KX 0.6mm
                    └── [Brand] PLA @AC KS1/KX 0.8mm
```

- KX must **never** inherit from KS1 user profiles
- Non-0.4mm variants keep only keys that differ from their 0.4mm parent
- `version` is always retained in every file

---

## Nozzle Transition Rules

Applied relative to the 0.4mm parent of the same material+printer. Full tables in `SKILLS.md` Section 4.

**PLA group** (Regular, Matte, Silk, Metal, Glow, Translucent, CF):

| Parameter | 0.25mm | 0.6mm | 0.8mm |
|-----------|--------|-------|-------|
| Pressure Advance | ×1.5 | ×0.667 | ×0.333 |
| Flow Ratio | +0.01 | −0.01 | −0.02 |
| Retraction Length | −0.2mm | +0.2mm | +0.4mm |
| Max Volumetric Speed | ×0.50, cap 3 | ×1.25 | ×1.50 |
| Nozzle Temp (all keys) | −5°C | +5°C | +10°C |
| Fan Speed (max & min) | −20pp | +20pp | +40pp |

Subtype: Matte adds extra −0.01 flow. Silk/Metal cap retraction speed at 30 mm/s for 0.6/0.8mm.

**PETG group** (Regular, High-Flow/Rapid, Translucent):

| Parameter | 0.6mm | 0.8mm |
|-----------|-------|-------|
| Pressure Advance | ×0.60 | ×0.30 |
| Flow Ratio | −0.02 | −0.04 |
| Retraction Length | +0.4mm | +0.8mm |
| Max Volumetric Speed | ×1.25 | ×1.5 |
| Nozzle Temp (all keys) | +10°C | +15°C |
| Fan Speed (max & min) | +30pp | +50pp |

**TPU group** (95A, HS, High Speed):

| Parameter | 0.6mm | 0.8mm |
|-----------|-------|-------|
| Pressure Advance | ×0.50 | 0.000 |
| Flow Ratio | none | −0.01 |
| Retraction Length | keep | keep |
| Max Volumetric Speed | cap 5 | cap 7 |
| Nozzle Temp (all keys) | +5°C | +10°C |
| Fan Speed (max & min) | +20pp | +40pp |

**Application notes:**
- "pp" = percentage points absolute; fan clamped 0–100
- Temperature delta shifts ALL of: `nozzle_temperature`, `nozzle_temperature_initial_layer`, `nozzle_temperature_HS`, `nozzle_temperature_initial_layer_HS`, `nozzle_temperature_range_high`, `nozzle_temperature_BRASS`, `nozzle_temperature_initial_layer_BRASS` — **never** `nozzle_temperature_range_low`
- Round PA to 3 dp; flow ratio to 4 dp
- If 0.4mm retraction is nil/absent, use 0.8mm as baseline before delta

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
- 0.6mm safety rule: `support_bottom_z_distance` ≥ effective layer height
- HQ vs Optimal (0.25mm): must differ in exactly 8 keys — see `SKILLS.md` Section 9
- PETG process variants intentionally diverge in bridge and support — do not force to match regular

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
- [ ] For 0.6mm process: `support_bottom_z_distance` ≥ layer height
- [ ] For matte PLA: `close_fan_the_first_x_layers=4`, `full_fan_speed_layer=8`, `filament_z_hop=0.6`
