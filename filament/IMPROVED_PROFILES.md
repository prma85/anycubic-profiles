# Improved Profiles — Reference & Best Practices

**Purpose:** The "Improved" profiles are calibrated default layers that sit between the
Anycubic system profiles and brand-specific user profiles. They serve as the best-known
settings for each material family on each printer and are the fallback for any new filament
that doesn't have its own calibrated profile.

**Inheritance chain (post v1.4.1.02 flat model):**
```
Anycubic system profile
    └── Improved [material] @AC [printer] 0.4mm   ← calibrated base
            ├── Improved [material] @AC [printer] 0.25mm
            ├── Improved [material] @AC [printer] 0.6mm
            └── Improved [material] @AC [printer] 0.8mm
```

Brand profiles inherit directly from the system now (inheritance flattened for v1.4.1.02
compatibility), but the Improved profile values are the canonical reference for what any
brand profile in that family should look like.

---

## Temperature Model

### KS1 (Kobra S1)
KS1 profiles use the **BRASS suffix as the operating default**. The bare `nozzle_temperature`
field is not the primary reference on KS1 — use `nozzle_temperature_BRASS` as the baseline.

- `nozzle_temperature_BRASS` = brass nozzle operating temp
- `nozzle_temperature_HS` = BRASS + 5°C (PLA) or BRASS + 10°C (PETG)
- `nozzle_temperature_initial_layer_BRASS` = first layer temp (same or +5°C)
- `nozzle_temperature_initial_layer_HS` = BRASS_initial + 5°C (PLA) or +10°C (PETG)

### KX (Kobra X)
KX profiles use **no BRASS suffix** — the bare `nozzle_temperature` is used by HS nozzles
as their effective operating temp. Setting `nozzle_temperature` too low directly hurts HS
nozzle performance.

- `nozzle_temperature` = operating temp (used by both brass and HS on KX)
- `nozzle_temperature_HS` = `nozzle_temperature` + 5°C (PLA) or +10°C (PETG)
- `nozzle_temperature_initial_layer` = first layer temp
- `nozzle_temperature_initial_layer_HS` = `nozzle_temperature_initial_layer` + 5°C (PLA)

**Critical rule:** `nozzle_temperature_HS` must NEVER be lower than `nozzle_temperature`.
`nozzle_temperature_initial_layer_HS` must NEVER be lower than `nozzle_temperature_initial_layer`.
Hardened steel has lower thermal conductivity — it always needs more heat, not less.

---

## Improved PLA — Canonical Values

System parent effective temps: `nozzle_temperature` = 205°C, `initial_layer` = 215°C (both printers).

### KS1
| Nozzle | Temp (BRASS) | Initial (BRASS) | Temp (HS) | Initial (HS) | Flow  | MVS | Retract | PA    | Fan max/min |
|--------|-------------|-----------------|-----------|--------------|-------|-----|---------|-------|-------------|
| 0.25mm | 195         | 195             | 200       | 200          | 0.99  | 3   | 0.6mm   | 0.053 | 80/80       |
| 0.4mm  | (inherit)   | (inherit)       | (inherit) | (inherit)    | (inh) | 16  | 0.8mm   | (inh) | 100/60      |
| 0.6mm  | 205         | 205             | 210       | 210          | 0.97  | 20  | 1.0mm   | 0.023 | 100/100     |
| 0.8mm  | 210         | 210             | 215       | 215          | 0.96  | 24  | 1.2mm   | 0.012 | 100/100     |

### KX
| Nozzle | Temp  | Initial | Temp (HS) | Initial (HS) | Flow  | MVS | Retract | PA    | Fan max/min |
|--------|-------|---------|-----------|--------------|-------|-----|---------|-------|-------------|
| 0.25mm | 200   | 210     | 205       | 215          | 0.99  | 3   | 0.6mm   | 0.053 | 80/60       |
| 0.4mm  | (inh) | (inh)   | (inh)     | (inh)        | (inh) | 16  | (inh)   | (inh) | (inh)       |
| 0.6mm  | 210   | 220     | 215       | 225          | 0.97  | 20  | 1.0mm   | 0.023 | 100/100     |
| 0.8mm  | 215   | 225     | 220       | 230          | 0.96  | 24  | 1.2mm   | 0.012 | 100/100     |

*Note: 0.4mm KX inherits everything from system (Anycubic PLA @Anycubic Kobra X 0.4 nozzle).*

---

## Improved PLA+ — Canonical Values

System parent temps (KS1): `nozzle_temperature` = 205°C, `initial` = 215°C.
System parent temps (KX): same.

### KS1
| Nozzle | Temp (BRASS) | Initial (BRASS) | Temp (HS) | Initial (HS) | Flow  | MVS  | Retract | PA    | Fan max/min |
|--------|-------------|-----------------|-----------|--------------|-------|------|---------|-------|-------------|
| 0.25mm | 200         | 200             | 205       | 205          | 0.97  | 3    | 0.6mm   | 0.060 | 80/80       |
| 0.4mm  | (inherit)   | (inherit)       | (inherit) | (inherit)    | 0.96  | 19   | (inh)   | (inh) | 100/60      |
| 0.6mm  | 210         | 210             | 215       | 215          | 0.95  | 23.8 | 1.0mm   | 0.027 | 100/100     |
| 0.8mm  | 215         | 215             | 220       | 220          | 0.94  | 28.5 | 1.2mm   | 0.013 | 100/100     |

### KX
| Nozzle | Temp  | Initial | Temp (HS) | Initial (HS) | Flow  | MVS  | Retract | PA    | Fan max/min |
|--------|-------|---------|-----------|--------------|-------|------|---------|-------|-------------|
| 0.25mm | 200   | 210     | 205       | 215          | 0.97  | 3    | 0.6mm   | 0.060 | 80/60       |
| 0.4mm  | (inh) | (inh)   | (inh)     | (inh)        | 0.96  | 19   | (inh)   | (inh) | (inh)       |
| 0.6mm  | 210   | 220     | 215       | 225          | 0.95  | 23.8 | 1.0mm   | 0.027 | 100/100     |
| 0.8mm  | 215   | 225     | 220       | 230          | 0.94  | 28.5 | 1.2mm   | 0.013 | 100/100     |

---

## Improved PLA Translucent — Canonical Values

High temps + zero fan for optical clarity. Same values on KS1 and KX.

| Nozzle | Temp (BRASS) | Initial (BRASS) | Temp (HS) | Initial (HS) | Flow  | MVS | Fan |
|--------|-------------|-----------------|-----------|--------------|-------|-----|-----|
| 0.4mm  | 230         | 235             | 235       | 240          | 1.01  | 8   | 0%  |
| 0.6mm  | 235         | 240             | 240       | 245          | 1.00  | 10  | 0%  |
| 0.8mm  | 240         | 245             | 245       | 250          | 0.99  | 12  | 0%  |

---

## Improved PETG — Canonical Values

PETG HS rule: `nozzle_temperature_HS` = BRASS + 10°C.

### KS1
| Nozzle | Temp (BRASS) | Initial (BRASS) | Temp (HS) | Initial (HS) | Flow  | MVS  | Retract | PA    | Fan max/min |
|--------|-------------|-----------------|-----------|--------------|-------|------|---------|-------|-------------|
| 0.4mm  | 235         | 235             | 245       | 245          | 0.95  | 10   | (inh)   | 0.064 | 40/–        |
| 0.6mm  | 245         | 245             | 255       | 255          | 0.93  | 12.5 | 1.2mm   | 0.038 | 70/60       |
| 0.8mm  | 250         | 250             | 260       | 260          | 0.91  | 15   | 1.6mm   | 0.019 | 90/80       |

### KX
| Nozzle | Temp  | Initial | Temp (HS) | Initial (HS) | Flow  | MVS  | Retract | PA    | Fan max/min |
|--------|-------|---------|-----------|--------------|-------|------|---------|-------|-------------|
| 0.4mm  | 235   | 235     | 245       | 245          | 0.95  | 10   | 0.8mm   | 0.064 | 30/–        |
| 0.6mm  | 245   | 245     | 255       | 255          | 0.93  | 12.5 | 1.2mm   | 0.038 | 100/45      |
| 0.8mm  | 250   | 250     | 260       | 260          | 0.91  | 15   | 1.6mm   | 0.019 | 100/65      |

---

## Improved PETG HS (High Speed / Rapid) — Canonical Values

Higher flow ratio than regular PETG; same temperatures.

### KS1
| Nozzle | Temp (BRASS) | Temp (HS) | Flow  | MVS  | Retract | PA    | Fan max/min |
|--------|-------------|-----------|-------|------|---------|-------|-------------|
| 0.4mm  | 235         | 245       | 0.98  | 18   | (inh)   | 0.064 | 40/–        |
| 0.6mm  | 245         | 255       | 0.96  | 22.5 | 1.2mm   | 0.038 | 70/60       |
| 0.8mm  | 250         | 260       | 0.94  | 27   | 1.6mm   | 0.019 | 90/80       |

### KX
| Nozzle | Temp  | Temp (HS) | Flow  | MVS  | Retract | PA    | Fan max/min |
|--------|-------|-----------|-------|------|---------|-------|-------------|
| 0.4mm  | 235   | 245       | 0.98  | 18   | 0.8mm   | 0.064 | 30/–        |
| 0.6mm  | 245   | 255       | 0.96  | 22.5 | 1.2mm   | 0.038 | 100/45      |
| 0.8mm  | 250   | 260       | 0.94  | 27   | 1.6mm   | 0.019 | 100/65      |

---

## Improved PETG Translucent — Canonical Values

Very high temps + zero fan for clarity. Different KS1/KX baselines because of printer differences.

| Nozzle | KS1 BRASS | KS1 HS | KX Temp | KX HS | Flow  | MVS  | Fan |
|--------|-----------|--------|---------|-------|-------|------|-----|
| 0.4mm  | 260       | 270    | 252     | 262   | (inh) | 5    | 0%  |
| 0.6mm  | 270       | 280    | 262     | 272   | 0.94  | 6.25 | 0%  |
| 0.8mm  | 275       | 285    | 267     | 277   | 0.92  | 7.5  | 0%  |

---

## Rules for Adding New Profiles

1. **Do not set temperatures below the system parent** — if you have no specific calibration
   for a new brand, do not set temperature at all and let inheritance provide the system default.

2. **Never invert HS vs base** — `nozzle_temperature_HS` (KX) or `nozzle_temperature_BRASS + 5`
   (KS1) must always be higher than the base/BRASS value. Hardened steel always needs more heat.

3. **Use the Improved profile values as the floor** — brand-specific overrides should be at or
   above these values, never below, unless the brand's filament specifically prints at lower temps
   (in which case document the reason in a comment or git commit).

4. **Nozzle deltas are relative to the 0.4mm profile**:
   - 0.25mm: −5°C from 0.4mm effective temp
   - 0.6mm: +5°C from 0.4mm effective temp
   - 0.8mm: +10°C from 0.4mm effective temp
   - HS offset: +5°C (PLA) or +10°C (PETG) at every nozzle size

5. **On KX, setting `nozzle_temperature` overrides both brass AND HS nozzle behavior** because
   the KX system profile structure uses the bare field for both. Only set it if you have a
   confirmed calibration value ≥ the system default (205°C for PLA, 205°C for PLA+).

---

## Common Errors to Avoid

| Error | Symptom | Fix |
|-------|---------|-----|
| `nozzle_temperature_HS` < `nozzle_temperature_BRASS` | HS nozzle under-extrudes, jams | Set HS = BRASS + 5 (PLA) or +10 (PETG) |
| `nozzle_temperature` < system default on KX | All nozzle types too cold on KX | Remove the override or use ≥ system value |
| Propagating wrong parent temps via flatten | Entire brand family runs too cold | Audit child profiles after any parent edit |
| Setting initial_layer_HS < initial_layer | First layer adhesion fails with HS | initial_layer_HS = initial_layer + delta |
