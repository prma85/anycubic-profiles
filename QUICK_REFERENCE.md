# Anycubic Kobra S1 - Quick Reference Card

**Printer:** Anycubic Kobra S1 | **Nozzle:** 0.4mm Brass | **Default:** `0.20mm Quit-HQ @AC KS1`

---

## 🚀 QUICK START (3 Steps)

1. **Pick Filament** → Check `filament/README.md` or select by brand/material
2. **Pick Process** → Use `0.20mm Quit-HQ` (default) OR choose by goal below
3. **Slice & Print** → Adjust nozzle temp ±5°C if needed based on results

---

## 📝 SELECT PROFILE BY GOAL

| Goal                     | Profile                        | Speed  | Quality    | Time     |
| ------------------------ | ------------------------------ | ------ | ---------- | -------- |
| 🎯 **Balanced (BEST)**   | `0.20mm Quit-HQ`               | ⚡⚡   | ⭐⭐⭐⭐   | 1x       |
| 👁️ **Maximum Detail**    | `0.16mm HQ` or `0.12mm HQ`     | ⚡     | ⭐⭐⭐⭐⭐ | 1.5-2x   |
| 🏃 **Fast Print**        | `0.24mm PETG` or `0.28mm PETG` | ⚡⚡⚡ | ⭐⭐⭐     | 0.6-0.7x |
| 🔷 **Tiny Miniatures**   | `Miniatures (0.08mm)`          | ⚡     | ⭐⭐⭐⭐⭐ | 3-4x     |
| ⚙️ **Strong/Functional** | `Tools & Home Improvements`    | ⚡⚡   | ⭐⭐⭐     | 1x       |
| 🪜 **Flexible (TPU)**    | `0.20mm Optimal TPU`           | ⚡     | ⭐⭐⭐     | 2x       |
| 🎨 **Shiny Finish**      | `0.16mm Optimal Silk PLA`      | ⚡⚡   | ⭐⭐⭐⭐   | 1.5x     |

---

## 🌡️ TEMPERATURE BY MATERIAL (Nozzle / Bed)

| Material | Temp          | Bed         | Notes                   |
| -------- | ------------- | ----------- | ----------------------- |
| PLA      | 200-220°C     | 60°C        | Standard, versatile     |
| PLA+     | 210-230°C     | 60°C        | Run hotter than PLA     |
| **PETG** | **230-250°C** | **70-80°C** | **Slow outer walls!**   |
| PETG HS  | 240-260°C     | 75-85°C     | Even hotter             |
| TPU      | 200-220°C     | 20-30°C     | Print 20-40 mm/s        |
| PLA Silk | 200-220°C     | 60°C        | Glossy finish           |
| PLA-CF   | 205-225°C     | 60°C        | **Use hardened nozzle** |

---

## 🔧 NOZZLE SELECTION

🔵 **Brass** (Default)

- ✅ All standard prints: PLA, PLA+, PETG, TPU, Silk
- ❌ Avoid: Carbon fiber (PLA-CF), Glass-filled PETG
- Cost: Low

🟡 **Hardened Steel** (For Abrasives)

- ✅ PLA-CF, Glass-filled PETG
- ⚠️ May need +5°C hotter
- Cost: Higher, lasts longer

---

## ⚠️ COMMON ISSUES

| Problem                  | Cause           | Solution                        |
| ------------------------ | --------------- | ------------------------------- |
| **Stringing**            | Temp too high   | -5°C or more retraction         |
| **Under-extrusion**      | Nozzle too cool | +5°C                            |
| **First layer issues**   | Bed not level   | Re-level bed + clean with IPA   |
| **Curling edges (PETG)** | Nozzle too hot  | -10°C or lower bed by 5°C       |
| **Warping**              | PETG specific   | Level bed, use brim, lower temp |
| **TPU not printing**     | Too fast        | Reduce to 20-30 mm/s            |

---

## 🎁 FILAMENT BY TYPE (Quick Pick)

**PLA:** Creality, Overture, Polymaker, Prusament, Generic
**PLA+:** Creality, Elegoo, Overture, Sunlu
**PETG:** Creality, Overture, Prusament, Sovol, AzureFilm
**Silk:** Geetech, Generic, iBOSS, JustMaker
**TPU:** Overture, Sovol (requires slow printing)

_See `filament/README.md` for complete list of 40+ options_

---

## 📦 PROFILE LAYERS (Organization)

**By Height:**

- `0.08-0.12mm` → Ultra-fine detail
- `0.16mm` → Excellent detail (action figures)
- `0.20mm` → **Standard (default here!)**
- `0.24-0.28mm` → Fast production

**By Purpose:**

- Quit-HQ → Office use (⭐ DEFAULT)
- HQ → High quality
- Optimal → Balanced
- General → Material-specific
- Draft → Speed focused

---

## 🛎️ BEFORE YOU PRINT

✅ Bed leveled? (Do every 5-10 prints)
✅ Filament dry? (Especially PETG, TPU)
✅ Build plate clean? (IPA + lint-free cloth)
✅ Temperature set correctly? (Check material table above)
✅ Nozzle clean? (Brush if needed)

---

## 📞 SETTINGS TO ADJUST IF NEEDED

**Nozzle Temperature:** ±5°C (test on small print first)
**Bed Temperature:** ±5°C (for adhesion)
**Print Speed:** Only if profile feels wrong (check issue table)
**Retraction:** Only in filament-specific profile

---

## 💾 YOUR SETUP

| Item      | Value                      | Notes                       |
| --------- | -------------------------- | --------------------------- |
| Printer   | Anycubic Kobra S1          | + Kobra 3/2/X compatible    |
| Nozzle    | 0.4mm Brass                | Have hardened steel backup  |
| Bed       | PEI Spring Steel 220×250mm | Self-leveling               |
| Slicer    | Anycubic Slicer Next       | OrcaSlice-based             |
| Location  | Office                     | Quiet-HQ default preferred  |
| Filaments | 40+ profiles               | 8 material types, 17 brands |
| Processes | 45+ profiles               | 8 layer heights + specialty |

---

## 🔗 WHERE TO FIND THINGS

| Need               | File/Folder          |
| ------------------ | -------------------- |
| Main guide         | `README.md`          |
| Pick filament      | `filament/README.md` |
| AI assistant notes | `COPILOT_CONTEXT.md` |
| Filament profiles  | `filament/*.json`    |
| Process profiles   | `process/*.json`     |
| Machine configs    | `machine/*.json`     |

---

## 🆘 NEED HELP?

1. **Issue?** → See "COMMON ISSUES" table above
2. **Pick filament?** → Read `filament/README.md`
3. **Pick profile?** → Use "SELECT PROFILE BY GOAL" above or `README.md`
4. **Need detail?** → Read main `README.md` or `COPILOT_CONTEXT.md`
5. **New filament?** → Copy similar filament + adjust temps

---

## ✅ MERGED PROFILES (New!)

**0.24mm PETG** - Unified from Draft + General PETG

- ✅ Better than Draft (more optimized)
- ✅ Better than General (faster)
- ✅ Use for: Fast PETG printing with quality

**0.28mm PETG** - Unified from Draft + General PETG

- ✅ Use for: Fastest PETG prints
- ✅ Still maintains acceptable quality

---

**Printer Ready! Print confidently with 40+ filaments and 45+ processes configured.** 🎉
