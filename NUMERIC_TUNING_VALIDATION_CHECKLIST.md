# Numeric Tuning Validation Checklist (Mandatory)

Last updated: 2026-03-12
Scope: Any proposal that changes numeric values in machine, filament, or process profiles.

## Zero-Bypass Rule

No numeric tuning proposal is allowed unless every required gate below is marked PASS with evidence.
If any required gate fails, output must be: STOP - insufficient validation.

## Required Inputs

- user.zip (custom overlays from user/651589)
- anycubic.zip (system defaults from system/Anycubic)

## Gate 1 - Data Integrity (Required)

- [ ] PASS: All JSON files parse successfully.
- [ ] PASS: No duplicate IDs in equivalent scope (for example print_settings_id or filament_settings_id where applicable).
- [ ] PASS: Filename, profile name, and matching .info metadata are consistent.

Evidence required:
- List of parser result counts (total checked, failures).
- Duplicate ID report (or explicit none found).
- List of mismatched name/file/info entries (or explicit none found).

## Gate 2 - Inheritance Resolution (Required)

- [ ] PASS: Every profile inheritance chain resolves completely.
- [ ] PASS: Resolution rule applied correctly:
  1) resolve in user.zip first
  2) if missing, resolve in anycubic.zip
- [ ] PASS: Effective final values can be computed for each proposed target profile.

Evidence required:
- For each target profile, provide full inheritance chain.
- Mark each parent source as user.zip or anycubic.zip.

## Gate 3 - Scope Discipline (Required)

- [ ] PASS: Proposed numeric changes are only in requested scope (machine, filament, and/or process as requested).
- [ ] PASS: No unrelated non-numeric changes are bundled.
- [ ] PASS: No naming or compatibility edits unless explicitly requested and justified.

Evidence required:
- File list with changed keys only.
- Confirmation that no unrelated files/keys are touched.

## Gate 4 - Baseline Behavior Characterization (Required)

- [ ] PASS: Baseline metrics are documented before proposing new numbers.
- [ ] PASS: Each target profile has at least one baseline configuration row with effective values.
- [ ] PASS: Baseline includes machine + filament + process stack, not isolated profile snippets.

Evidence required:
- Table per target profile including at minimum:
  - effective layer height
  - key speed/acceleration values
  - bridge/support critical values
  - temperature/flow/PA values when filament is involved

## Gate 5 - Constraint Compliance (Required)

- [ ] PASS: All project hard rules remain valid after proposed changes.
- [ ] PASS: No known safety/consistency rule is violated.

Mandatory checks (minimum):
- [ ] 0.6 process rule: support_bottom_z_distance >= effective layer height
- [ ] 0.25 HQ vs Optimal rule: only approved 8-key delta pattern (unless explicitly changing the rule)
- [ ] PETG profile intent preserved (bridge/support-release behavior not accidentally removed)
- [ ] compatible_printers still matches intended nozzle/printer family

Evidence required:
- Rule check report with pass/fail per profile.
- Explicit list of any exceptions and rationale.

## Gate 6 - Comparative Justification (Required)

- [ ] PASS: Every proposed numeric change has a reason tied to print physics and current profile patterns.
- [ ] PASS: Each change compares old value vs new value vs parent/system context.
- [ ] PASS: Trade-offs are explicitly stated (quality, speed, strength, reliability, support release, stringing risk).

Evidence required:
- Delta table with columns:
  - file
  - key
  - old effective value
  - proposed value
  - reference (parent/system/observed pattern)
  - expected impact
  - risk

## Gate 7 - Cross-Profile Consistency (Required)

- [ ] PASS: Similar profile families remain internally consistent.
- [ ] PASS: No orphan numeric style appears in a single profile without reason.

Minimum family checks:
- [ ] 0.25 HQ/Optimal pairs
- [ ] PETG families vs regular families at same layer group
- [ ] 0.6 family ladder (0.18/0.20/0.24/0.30/0.32/0.38 where applicable)

Evidence required:
- Consistency diff summary by family.
- Any intentional deviations flagged with justification.

## Gate 8 - Risk Scoring and Rollback Plan (Required)

- [ ] PASS: Each proposal has risk category: low, medium, or high.
- [ ] PASS: A rollback path is defined per changed file.
- [ ] PASS: Changes are grouped into staged batches (not one large unbounded patch).

Evidence required:
- Risk table per change batch.
- Rollback instructions by file group.

## Gate 9 - Test Matrix Proposal (Required)

- [ ] PASS: A minimal validation print matrix is defined before final recommendation.
- [ ] PASS: Matrix covers at least one representative model for quality, bridging, support release, and throughput.
- [ ] PASS: Success criteria are numeric and observable (not subjective only).

Minimum matrix dimensions:
- [ ] Nozzle sizes impacted (for example 0.25/0.4/0.6/0.8)
- [ ] Materials impacted (for example PLA, PETG, TPU)
- [ ] Profile families impacted (HQ/Optimal/Draft/PETG-specialized)

Evidence required:
- Test plan table with:
  - profile stack
  - model type
  - print objective
  - measurable pass criteria

## Gate 10 - Output Contract (Required)

Before suggesting any numeric value changes, the AI must produce this exact section order:

1. Validation summary (PASS/FAIL per gate)
2. Blocking issues (if any)
3. Safe-to-change scope
4. Proposed numeric deltas (only if all required gates pass)
5. Test matrix
6. Rollback plan

If any required gate fails:
- Do not propose numbers.
- Provide only remediation steps to reach PASS.

## Mandatory Failure Conditions

Any one of the following forces STOP:
- unresolved inheritance chain
- missing effective-value baseline
- missing rule check report
- inconsistency introduced in protected family patterns without explicit rationale
- missing rollback plan

## Reviewer Sign-Off Section

- Reviewer/Agent:
- Date:
- Requested scope:
- Gate result summary:
- Final status: PASS FOR NUMERIC PROPOSAL or STOP - INSUFFICIENT VALIDATION
