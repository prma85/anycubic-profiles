# Copilot General View (User 651589)

Last updated: 2026-03-12

This file is the entry point for AI assistants working in this repository scope.

## Internal Docs Index

- Authoritative editing policy: .github/copilot-instructions.md
- Repository architecture: README.md
- Process strategy and profile matrix: process/README.md
- Filament strategy and nozzle matrix: filament/README.md
- External AI review context: AI_OPTIMIZATION_REVIEW_PROMPT.md

## Practical Navigation

1. Start at .github/copilot-instructions.md for hard rules.
2. Open README.md for architecture, machine notes, and merged quick guidance.
3. Open process/README.md or filament/README.md depending on requested change.
4. For AI review task framing, open AI_OPTIMIZATION_REVIEW_PROMPT.md.

## Current Filament Inheritance Model

- 0.4mm profiles are the editable parent overlays per material and printer family.
- 0.25mm, 0.6mm, and 0.8mm profiles inherit from matching 0.4mm parents.
- Variant files should keep only keys that differ from 0.4mm.
- KSX variants must stay inside KSX family; do not inherit KS1 user filament files.
