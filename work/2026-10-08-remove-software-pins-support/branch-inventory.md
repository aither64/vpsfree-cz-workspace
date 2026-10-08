# Confctl final branch inventory

Base: `1b56616eff41e760327f3a0dbed8875e4aa9dbec` (merged upstream Version 3.0.0).
Head: `cc40679d267165aecfa569128438bb55fe910268` (fixture correction folded; prior published head3be154b5).
Branch: `2026-10-08-remove-software-pins-support`.
Parent fetch succeeded; `origin/master` remains the exact base. No rebase needed.
Worktree/index clean; base-to-head whitespace check passed. Prior head `3be154b5` was published; the final corrected head is now published
after scoped independent review. No default integration.

## Complete series

```text
d72ff27a9b589ed0d2b0532db70f4e1b96b7373d Make confctl runtime exclusively flake-based
72eb424c430182c0563b3ecb7d4e5869a5c2721d Remove Nix pin evaluation and expose flake module options
85bb8717ca25aa84a01fb6f5ef4ce43e3283a5fb Make the flake example the sole configuration fixture
9d63ab4f30929043b8695225c0128029b188a985 Drop software-pin-only dependencies and CI setup
cc40679d267165aecfa569128438bb55fe910268 Document flake-only operation and preserved recovery state
```

Final diff: [published comparison](https://github.com/vpsfreecz/confctl/compare/1b56616eff41e760327f3a0dbed8875e4aa9dbec...cc40679d267165aecfa569128438bb55fe910268).
The complete local review capture is `confctl-final.diff`.
Diff summary: 126 files changed, 1896 insertions(+), 6991 deletions(-) (net removal 5,095 lines).

## Split and history disposition

1. Ruby runtime/backend/CLI removal, flake persistence policy and their regression
   specs stay together: pin classes and dispatch must disappear atomically from
   the recursive Ruby loader, while selection protections accompany persistence.
2. Nix deletion, shared option evaluator and its Rake/ModuleOptions/template
   consumers share the new output contract. Carrier optional metadata and its
   test assertion accompany removal of the pin-derived Nix metadata.
3. Whole example replacement and its fixture consumers move together, avoiding
   dual example paths. Hidden files, lock, nested machines and developer wrapper
   are preserved from the flake example; old pin files are deleted.
4. Pin-only dependencies/env setup and narrow CI trigger/action consistency are
   independently reviewable. flake.nix hunks were separated from output exports.
   No input or Ruby dependency lock refresh is mixed in.
5. Supported prose and generated references follow the final implementation.
   Main-agent writing pass and final Rake regeneration happened before commits.

The initial runtime commit was amended before publication for message width.
Its superseded object is outside the final series. No fixup/tidy commit or
superseded design was published. All implementation corrections were folded
into these first owning commits. No obsolete compatibility backend, adapter or
transitional migration is intentionally retained. Independent reviewer verified those conclusions from the complete series and
final diff; narrow corrections were reconciled under the review policy.

## Prior review remediation at 3be154b5

Independent all-lane/whole-history review completed at `18d8b4862a2523d629a534ea38d2ba92ef0209c8`.
Required fixes were directly inspected and tested under the narrow-fix policy:
actual current target/retention protection, correct stable owned declarations,
and init optional-channel delimiter. Fixes were folded into owning units1/2/5;
units3/4 are patch-identical. No fixup or transition remains in the final series.
Local capture `review-remediation.range-diff` records all five
units before/after; reviewed-to-final delta is exactly six files, +236/-117.
The generated reference changes only its 114 declaration labels. Prior remediation tree
`d2adc4f0f94e0f179652c1c12a8885e9bc5e318a` equals the checked pre-fold tree;
parent rechecked all five source hashes and generated-reference hash after fold.
Full66/0 and stable114-option evidence applies unchanged to the final head.
No new public output/design or compatibility contract was added, so no full
review rerun is required under skill steps8-9. The original independent whole-
history/migration conclusions remain recorded in review-report.md, with the
lead's focused reconciliation. Package and Nix RSpec builds and local smoke
passed; exact-head CI was pending at that prior checkpoint.

## Migration and use provenance

No database or persisted-state conversion migrations. Existing merged v3 flake
JSON and GC-root naming remain supported. No new format version or conversion
of old pin records is introduced; explicit pin/missing/unknown-mode and invalid
records remain untouched and unusable with the new tool. v3 upgrade instructions
are a supported historical procedure, not a new migration implementation.

The prior five-commit series ending at `3be154b5` was published on the feature
branch and has not been merged, released or deployed. External consumption is
not audited. No intermediate schema requires support. Existing v3
behavior at the base is merged/released; rollback compatibility with its flake
JSON is intentional. Production configuration migration status and third-party
netboot JSON readers remain unknown and need inventory before a later rollout.

## Fixture-source discovery correction

After full local rollback/carrier deployment passes and two initial lock
failures, exactly2fixture commands use explicit path: URLs before Git init.
Folded into unit3; original unit1/2 SHA unchanged,4/5 patches identical.
Local captures `fixture-remediation.diff` and `fixture-remediation.range-diff`
preserve the
exact two-line delta and complete five-unit history. Final head`cc40679d267165aecfa569128438bb55fe910268`,
tree08f33e1fe5613f7634ba69b38535fb3c35a3c0c9; checked pre-fold tree identical.
Quick66/0,95-file lint,2Nix format/extracted Ruby syntax and hooks passed.
No new API/boot/rollback/schema/migration behavior; scope remainsconfctl only.
[review-fixture-revision.md](review-fixture-revision.md) records the independent general-lane revision assessment scope;
[review-report.md](review-report.md) contains its completed conclusion.

## Final verification and readiness

Parent final check: local/published head cc40679d and tree08f33e1 agree, clean
source/index, complete whitespace check passed. Independent review has no open
findings. Full quick checks, package/smoke, final-head Ruby matrix/lint and all
four local VM suites passed. Remote VM workflow37766013754 remains queued;
no successful remote VM result is claimed. Ready, awaiting explicit approval to
integrate confctl into master. Session and feature refs remain open/retained.
