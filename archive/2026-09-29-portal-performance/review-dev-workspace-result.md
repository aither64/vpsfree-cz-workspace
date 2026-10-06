# Dev workspace mandatory review result

## Review identity

- Reviewer: retained `reviewer0`, GPT-6 Sol, xhigh, read-only.
- Reviewed range: `3b570f0a8b75d809a2753177590158e9dc4639f1..9e25870d143f28c2e37763a5e6fd526dad1c9df5`, plus the exact pushed `codex-web` dependency at `f16fcff6fa9a5476545c98b50ecf1c2db04bf602`.
- Risk and lanes: high risk; general, architecture and repetition, scope and proportionality, and risk and compatibility.
- Scope: all three committed `dev-workspace` changes, their exact dependency pin, and archive/session behavior. This was a pre-push review, not the final whole-chain readiness gate.

## Findings

1. **Important:** an older page already in flight can restore obsolete entries after a same-thread rollout replacement. The pinned history model replaces rows without advancing `repairVersion`, so the portal accepts the stale response. The reviewer reproduced old entries reappearing with `gap: false`.
2. **Advisory:** the supported mixed-version pairing of a cached new portal script with an older `codex-web` asset rebuilds the transcript on legacy refresh without preserving disclosure state or scroll position. That path lacks a browser regression.

## Positive conclusions and residual risks

- The archive lock order, exclusive final checks, fail-closed observer, receipt scheduling, separate refresh lanes, shared helper use, exact pins, commit split, and visible copy showed no further finding.
- Portal unit contracts and whitespace checks passed during review.
- There are no migrations in the reviewed diff.
- Live browser races, exact cursor behavior, archive contention, metadata rebuild CPU, and the latency target remain verification gaps.

## Reconciliation

- Both findings are accepted. The Important race must be fixed and covered before push.
- The Advisory gap will also receive a focused mixed-version regression, with behavior corrected if the reproduction confirms state loss.
- `implementer0` owns the focused corrections and checks. A narrow rerun of affected lanes is required before push.

## Corrections

- `codex-web` local successor `d210d3f7cc93981d0ab163b1fcf0718f9587f47e` advances the shared history generation after full transcript replacement, so older paged and legacy reads are rejected. Focused regressions pass.
- `dev-workspace` local head `9b54f7b46cd37fdd36679e619616ebd995f43be6` preserves disclosure and scroll state on the supported newer-portal/older-asset fallback. Focused regressions pass.
- Both worktrees are clean. Neither correction is pushed; the exact downstream pin still names `f16fcff6` until the shared correction passes review.

## Focused rerun

- Reviewer: the same retained `reviewer0`, Sol/xhigh, read-only.
- The Important stale-read finding is resolved. Paged and legacy full replacements advance `repairVersion`, and the delayed older-page reproduction is rejected.
- No new Blocking or Important finding arose.
- The mixed-version Advisory is only partly resolved. Disclosure and scroll state survive while entry keys remain stable, but a sliding legacy recent-turn window changes fallback keys; real new output then cannot trigger the **New output** indicator. This compatibility edge remains assigned for correction and regression coverage.
- Exact pin regeneration, live browser races, rollout latency, archive contention, and metadata CPU remain open.

## Advisory correction

- `dev-workspace` local head `67246cf25a40ad5029121b75c99f24434bf86d36` gives legacy fallback rows stable keys and compares bounded recent-turn windows for additions or updates.
- The focused regression slides turns 1–20 to 2–21 and confirms that disclosure and the scroll anchor remain stable, the new turn is reported as changed, and removal alone does not report new output.
- Browser/unit contracts, Node syntax checks, and `git diff --check` pass. Narrow reviewer confirmation remains pending.

## Final pre-push confirmation

- The remaining mixed-version Advisory is resolved at `67246cf25a40ad5029121b75c99f24434bf86d36`.
- Stable legacy fallback identities preserve retained disclosure and scroll position as the bounded window slides. Added or updated entries drive **New output** when appropriate; removal alone does not.
- The reviewer found no false identity collision in the exercised entry shapes, hidden change, or paged-path regression. Focused browser and paging contracts, an additional identity reproduction, and `git diff --check` passed.
- No Blocking, Important, or Advisory finding remains from the pre-push review. Exact dependency pin regeneration and live rollout checks remain required; final whole-chain readiness is separate.

## Exact pin

- `dev-workspace` commit `87430b813cb0e0017e844711e60f4b34a7c32513` pins reviewed and pushed `codex-web` revision `d210d3f7cc93981d0ab163b1fcf0718f9587f47e` in Nix and Go metadata.
- The Go pseudo-version is `v0.0.0-20260929193321-d210d3f7cc93`; module and go.mod sums were resolved through the Go proxy.
- Nix metadata records `lastModified` 1790710401 and `sha256-jp6nOqpINJIzj9iKWqkmWDlSefRRZ7uTLM6y0BuiZns=`. Fake-hash discovery produced vendor hash `sha256-XCmaphXVXVvhnV3oU1UnreAw01qEoyBGB1bbb8Y9dSg=`.
- Nix syntax, lock JSON, Go module metadata, exact sums, the revision assertion, and diff checks pass. A focused dependency-coherence review remains pending before push.

## Pin review

- No Blocking or Important finding arose. The reviewer independently recomputed both Go checksums and confirmed the pseudo-version timestamp, short revision, Nix source metadata, discovered vendor hash, commit scope, and absence of stale `f16` pins.
- **Advisory:** the existing revision guard uses a textual grep that can match the expected version in a comment or overlook a `replace` directive selecting another module. The committed `go.mod` has neither issue, so the current pin is coherent, but the guard should parse the selected module rather than accept text coincidence.
- The Advisory is accepted and assigned for a focused guard correction before push. Full package build and final whole-chain readiness remain separate.

## Pin guard correction

- `dev-workspace` local head `9d48fc795de12f7725b0995d336c323c474c25e0` replaces textual grep with a parsed `go mod edit -json` check of the selected module version and replacements.
- Focused fixtures accept the exact required pin, reject a comment-only coincidence, reject wildcard and version-specific `codex-web` replacements, and allow unrelated replacements.
- Nix and shell syntax, the focused fixture, exact pin/vendor-hash preservation, and diff checks pass. Narrow reviewer confirmation remains pending.

## Pin guard rerun

- The comment-only and effective-replacement bypasses are resolved. The exact pin and vendor hash remain unchanged; shell syntax, Nix parsing, and diff checks pass.
- **Advisory:** the parsed guard still accepts any 14-digit pseudo-version timestamp with the expected short revision. The reviewer reproduced acceptance of `v0.0.0-20200101000000-d210d3f7cc93`, so the requested exact version is not yet enforced. The fixture also needs this case and an explicit unrelated-module replacement case.
- The Advisory is accepted and assigned for correction before push.

## Exact-version correction

- `dev-workspace` local head `9db7bc844a0332b7e00d21536c3bebf835928ece` derives the expected Go pseudo-version from the pinned flake input's `lastModifiedDate` and 12-character revision, then requires that full selected version.
- The fixture rejects the reviewer’s wrong-timestamp/same-revision value and explicitly accepts an unrelated-module replacement while retaining all earlier comment and effective-replacement cases.
- Nix and shell syntax, focused fixtures, lock-derived version equivalence, exact pin/vendor-hash preservation, and diff checks pass. Narrow reviewer confirmation remains pending.

## Final pin confirmation

- No finding remains. The guard compares Go's parsed selected requirement with the full pseudo-version derived from the pinned flake input.
- The reviewer confirmed the wrong-timestamp case fails, an unrelated replacement passes, and the earlier comment and effective-replacement cases still fail.
- Fixtures cover those cases; shell syntax, Nix parsing, independent checker runs, exact pin/vendor-hash preservation, and diff checks pass.
- The complete `dev-workspace` branch has passed its pre-push review. Full package build, live acceptance, and final whole-chain readiness remain separate gates.
