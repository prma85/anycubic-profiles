# CLAUDE.md — user/651589 Repository

This is the authoritative Claude Code instruction file for the `user/651589` git repository.
The parent `CLAUDE.md` at the root AppData folder covers the overall program structure.
This file covers the **git-tracked repository** specifically.

## Repository Identity

- **Path:** `C:\Users\pandrade\AppData\Roaming\AnycubicSlicerNext\user\651589`
- **Purpose:** Custom filament, process, and machine profiles for Anycubic Kobra S1 and Kobra X
- **Slicer:** Anycubic Slicer Next (OrcaSlicer-based)
- **Git remote:** tracked; commit and push when asked

## Documentation Map

Read in this order before editing:

1. **`SKILLS.md`** — complete knowledge base: printer hardware, slicer architecture, filament logic, KS1 vs KX differences, troubleshooting patterns
2. **`.github/copilot-instructions.md`** — authoritative editing policy, validation gates, naming rules, nozzle transition tables
3. **`README.md`** — repository architecture, machine overlay notes, S1 vs X strategy
4. **`process/README.md`** or **`filament/README.md`** — domain-specific guidance


## Git Workflow

```bash
# Always run from user/651589 — this is the git root
git add <specific files>
git commit -m "Description"
git push
```

Never `git add .` — this can accidentally include gcode files, thumbnails, or logs.
Stage only the profiles that were intentionally changed.

## Three-Tier Architecture (Quick Reference)

```
Machine  →  Filament  →  Process
(hardware)  (material)  (strategy)
```

- **Machine:** `machine/` — nozzle type, retraction, acceleration limits
- **Filament:** `filament/` — temps, flow, PA, cooling — **printer-scoped, never merge KS1/KX**
- **Process:** `process/` — layer height, speeds, supports — **shared across S1+X per nozzle**

## Critical Rules (Never Violate)

- Never cross-inherit KS1 and KX filament families
- Never remove `version` from any profile
- Never modify files under `system/Anycubic/` (vendor defaults, not git-tracked)
- Never exceed layer height > 0.75 × nozzle diameter
- Hardened Steel temp: +5°C on HS keys for PLA, +10°C for PETG — never on range_low/range_high
- Profile `name` field must exactly match filename stem (slicer resolves `inherits` by this)
- `.info` files: `sync_info=create`, `user_id=` empty, `setting_id=<filename stem>`

## File Pair Rule

Every `.json` profile must have a matching `.info` file with aligned `setting_id`.
When creating new profiles, always create both files.

## Scope of This Repo

Only `user/651589/` is git-tracked. Do not commit:
- `system/Anycubic/` (vendor defaults)
- `log/` (slicer debug logs)
- `*.gcode` files
- Thumbnail or cache files
