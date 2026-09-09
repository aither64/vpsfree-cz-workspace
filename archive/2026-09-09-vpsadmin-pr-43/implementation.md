# PR 43 development branch

Status: merged after explicit user approval. At 2026-09-09 14:31:19 UTC,
master fast-forwarded from 41af23e20 to 19971f039 over SSH. GitHub recognized
PR #43 as merged. No merge commit was created and no deployment was performed.

[Review the merged changes](https://github.com/vpsfreecz/vpsadmin/compare/41af23e207478af2469e1d6423312930e720ba87...19971f039771500d5d0304610f91fe6f4af5fed3)
at `19971f039771500d5d0304610f91fe6f4af5fed3`, based on
`41af23e207478af2469e1d6423312930e720ba87`.

| Commit | Change |
| --- | --- |
| `ed8121659` | Original payment-period feature, rebased with its patch and author preserved. |
| `a22f37263` | API JSON dependency constrained below 3, with matching generated package metadata. |
| `19971f039` | Czech/English continuation-cursor description and five request regressions. |

The cursor description now explains using the previous page's last payment ID,
keeping the same filters, and receiving an empty page for an unavailable or
excluded cursor. Bilingual OPTIONS tests verify that its label, type and
validation are preserved and that another endpoint retains its inherited
description.

The JSON dependency fix resolves the API startup failure caused by JSON 3's
keyword-only parse options and ActiveSupport 8.1's positional options argument.
Only JSON changes version in the generated API package. Stored JSON needs no
conversion.

## Validation

- Payment requests: 25 examples, zero failures.
- Retained boundary probes: seven examples, zero failures, including tied
  timestamps, includes, timezone offsets, date bounds, counts and tenant scope.
- Migration up/down: one example, zero failures.
- Packaged-dependency API boot smoke: five examples, zero failures. The Nix
  package builds; JSON decode and ActiveRecord serialization probes pass.
- API locale regeneration/health, focused RuboCop and mandatory commit hooks
  pass. All four independent review lanes report no findings at this head.
- A fresh temporary integration checkout fast-forwarded without changing the
  approved head and passed all five API boot smoke examples (seed 29306).

| GitHub workflow | Result |
| --- | --- |
| [RuboCop](https://github.com/vpsfreecz/vpsadmin/actions/runs/34358367558) | Passed |
| [i18n health](https://github.com/vpsfreecz/vpsadmin/actions/runs/34358367595) | Passed |
| [API Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/34358367616) | Passed: 26 topic jobs and topic coverage |
| [API Migration Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/34358367602) | Passed |
| [VM integration CI](https://github.com/vpsfreecz/vpsadmin/actions/runs/34358367645) | Running; excluded from the approval gate by request |

The required workflows above passed on the exact merged head before approval.
Source/master pushes triggered further runs of the same commit; they remain
running or queued. The extra WebUI PHPUnit run also passed. Current-head runs
were retained, including VM integration, as requested.

## Review limits and completion

Production-scale index timing/query plans and dependent WebUI Next end-to-end
tests remain unverified. Some extra boundaries are covered by retained probes
rather than permanent project specs. These are recorded limits, with no
Blocking, Important or Advisory findings from the review lanes.

Future rollout must complete the API before clients use the date filters.
Disable such client behavior before API rollback, and retain the JSON fix or
use an earlier known-bootable artifact; this exact base packages incompatible
JSON 3. The index itself is reversible and preserves payment data.

The PR source branch was updated from 44cfb4357 to the approved 19971f039 using
an exact force-with-lease before the ordinary fast-forward push to master.
The development and PR source branches are retained. The temporary integration
worktree was removed; the clean feature worktree will be removed by the guarded
session archive workflow once this conversation is idle. No user action remains
for this merge.
