# Affected final review: deployed archive baseline

No Blocking or Important findings. Proceed to the prepared final artifact
verification. This supplements the unchanged [original review](review.md) and
[settings-baseline review](review-successor.md); it does not claim deployment
success or authorize integration. The user's direction is **deploy only; leave
the branches unmerged**. No lifecycle action is authorized.

Retained `reviewer0`, thread `01a182d1-b79b-7060-a7dc-f20d38733788`, reviewed
independently at saved `gpt-6.1-sol` / `xhigh`, `read_only`, purpose `review`.
Session command and roster reverified; both environment markers absent and the
trusted binding matches. Applied affected general/history, scope and
risk/compatibility/lifecycle review, reusing unchanged source/architecture
inspection under the mandatory skill's affected-lane rules. No nested review,
application edits, tests, lifecycle mutations, claims, merges or deployment.

## Changed baseline and safety boundary

Inspected all four files in `2caa9419..76c9ad4f` (+312/-37), the complete archive
helper, its command caller, managed retry cancellation and relevant tests/docs.
`QuiesceExplicitArchive` retains the managed interrupt wrapper. Proven native
descendants instead use the underlying native interrupt without enrolling them
in managed retry admission. The private shared helper retains prompt/receipt
capture, queue deletion only after durable capture, goal pause and idle wait.

`archive_explicit.go:275` rechecks the child's native parent before mutation;
`nativeArchiveParent` also checks exact returned thread identity and working
directory. Ancestry, rather than a shared directory alone, establishes ownership.
Discovery still stops parents before descendants, resamples concurrent spawns
and retires deepest children first. Managed roots and retained members continue
to use retry cancellation and refuse uncertain automatic submissions. This is a
bounded correction to an existing archive boundary, not a new Files capability.

The new command test covers root/member parents, foreign children, changed
parent/directory/ID, held prompts, lost interrupt replies and uncertain managed
submissions. The descendant test exercises active native turns, rejects managed
admission and checks concurrent-spawn/retirement order. Recovery documentation
matches those boundaries. No concrete correctness or compatibility defect found.
These are disposable synthetic tests, not evidence of an actual archive run.

All four inherited changed files match selected immutable runtime source
`/nix/store/f8ww1pcp5v9jb4icybcz5j26w9k19fbp-source`. Its immutable composition
lock selects `76c9ad4f`, consistent with the exact live/profile/system receipt in
[rollout-preparation.md](rollout-preparation.md). Preserve that deployed fix.

## Equivalence, complete history and pins

Runtime task range:
`76c9ad4fbd877992464d2a7f2a1a2fe60db043b1..dd445cb0627f93375f1378af6b59d30ef8b34875`.
Independent range-diff against reviewed `2caa9419..6a1bfad8` is `=`. All 14 task
files are byte-identical, including full app.js, assets, API, tests and docs.
Native/dependency/module and persisted runtime-contract files are unchanged.
The baseline addition itself is substantive, not an equivalence claim.

The full historical eight-commit series from `4a002f52` is `cc106266`,
`e9153e61`, `d0a9c5f6`, `fd9128a1`, `2beb55e2`, `2caa9419`, `76c9ad4f`,
`dd445cb0`. Earlier reports cover unchanged predecessors; this review covers the
new archive commit and interactions. No obsolete task approach, fixup or
transitional implementation remains. Fresh SSH remote proof confirms `master`
at `76c9ad4f` and feature at `dd445cb0`: current target delta is one Files commit.

Workspace task range:
`4a3a9bd39fd244de49665853535fc87d5e8373e5..10344897ad051dd68ec3adfc21f949e7cc52ec47`.
From remote `9d35428a8c8f82bf5f51aaf3adf23d2b338542f0`, inventoried two inherited
shared-master tracking archive commits (`4357d3cc`, `4a3a9bd3`) and the single
final pin. Peer record bodies were not opened or claimed as reviewed. The task
changes only flake.nix/lock (+5/-5). Configuration range:
`7c999104833e8cf2dd8ac779a9e8e51876fb7d85..c8e9701614fdb3735d086f7591a29cdfe1e4d453`,
one generated channel update (+3/-3) with truthful `76c9ad4f → dd445cb0` history.
Fresh SSH proof confirms both feature and target heads above.

Each task pin stream contains one final consolidated update; superseded pins
are absent and old ranges remain in receipts. Independent semantic lock checks
found only each intended runtime node changed, with all other nodes, edges,
follows, extension and native selections preserved. Both select the exact final
runtime and `sha256-5tPigdC6kl1wC4e8eaoo8XoPJnUnu9Yyb1caS0+Glpk=`. No redundant
pin updates or obsolete migration history remain.

**No database migrations.** This refresh changes no archive journal, held-prompt,
retry or manifest format. Earlier inherited communication schema-1 state,
reporting policy 2, communication policy 1 and browser drop persistence remain
supported; the whole historical runtime is not persistence-neutral. Retain its
existing recovery contracts and forward package-recovery boundary.

## Remaining verification

Inspected the passing focused quick-check and hook/contract receipts. Reviewer
ran read-only source/history/lock/whitespace comparisons. Independently confirmed
the candidate and selected-live recursive metadata contain identical Ruby
aggregate derivations with 16 direct inputs, and identical native derivations.
The Ruby aggregate output is absent locally; metadata equivalence does not
establish output availability or new candidate success.

Next: materialize/root the prepared composed package, deployment contract and
exact host output, check exact-head CI and run the unchanged-asset native smoke.
Use the composed full Go/Ruby/protocol/browser check coverage; no duplicate
generic runtime campaign or optional hardening is requested. Preserve exact
artifact and graph receipts before lead-owned guarded activation. Keep all
branches unmerged and this session open. Machine retention follows the selected
policy while deployed lineage remains unintegrated; this review supplies no
merge or release permission.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-files-tab-limit-diagnosis/>
