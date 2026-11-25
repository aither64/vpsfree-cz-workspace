# G3: declared site policy and generated clients

Owner: implementer3, retained Sol/xhigh/workspace_write. Root released G3;
architect0 owns the creation-time contract at the top of design.md. Old KB and
capacity work remains parked at accepted vendor import77f7421f.

## Current checkpoint

Final backend dependency is satisfied at `5aa1df7b51fc22c9d35a2d7f6aec889afa54b303`,
tree `63cc6814777d1435750dcf12901cef0e12aefc16`. Backend source/index stay frozen
under implementer1. The one export batch used two fresh fixture databases;
all three raw output files match byte for byte. Evidence is
[export-receipt.json](nov18-g3-client-sync/export-receipt.json).

| Input | SHA256 |
| --- | --- |
| Raw schema |997045d31c26e2dde0a9ddcadd842ce15e767b52b006bdb02731e5eb08de4f00|
| Source provenance |869db77e2f5a8dd29efb3cea0f854664bd9a441d21cee4d62d63d315e861c58d|
| Exporter lock |2e9a124eff7b80d6fd57cd0f03cb2809847c67cc7f1af6364911c3622d7242a0|

API7.0/protocol2.0/full-fixture/en/all six plugins:154 application resources,
527 actions and8915 parameters. Rust includes the separate authentication
resource/five actions in its155/532 inventory. Export durations49.280s/41.465s.
HaveAPI generator remains unchanged `1ef9b204ba45bb261d3334be5c555cc1856b713b`.
No configured policy keys become generated enums.

| Repository | Current head | Status |
| --- | --- | --- |
| Configuration |1efed32a70a91e8705be2ceeb6b7dac4ad19e10c|Published over fresh master15e3b9af; exactly two patch-equivalent files, accepted bytes unchanged; current Ruby3.4.12 scoped lint/syntax and normal hooks pass. Final parser evidence retained.|
| Go SDK |bd0d1d2f548c128f4fbc8657679450b7f998e181|693 generated files (+9/-0); projection4/4 and Go9/9 tests pass. Two consolidated purposes, tree-equal to checked source.|
| Rust SDK |e34ef441468b3e7579719ceb68d1b0b2cce8d101|697 generated files (+9/-0); provenance7/7, regeneration refusal10/10, format/shell/provenance/regeneration check0; focused compile/test6/6; clean two-purpose tree, exact equality to checked preconsolidation source.|
| TS SDK |3cb7cf838a607bbafab207307e11626e57cdec8c|686 generated files (+9/-0); all required checks pass; exact HTTPS artifact delivered to owner2. CI44210679888 success.|

Each full generated set comparison, including deletions, is retained at
`nov18-g3-client-sync/{go,rust,ts}-generated-set.json`; handwritten output is
preserved. Go's effective schema changes exactly the retained OAuth revocation
URL and hashes to `8d9c19f23981b644f894edcbbabf1b7f82c7016a68d37b0d034ed649c5c9b478`.
[Schema compatibility](nov18-g3-client-sync/schema-compatibility.json) records
three new resources/six actions, no action/resource removals, removal of the
obsolete VPS flat summary/write fields, runtime string key filter and removal
of the old Unknown filter. No generation/runtime/formatter/version changes.

TS packed source is `d9d6d53dd0a2fb3b736b912123731bc78d69289e`, separate from
its support delivery commit. Archive SHA256
`b00e1e457dec33419505a286cf3dd5c937aa982ab4b3e7e6fca1b0fdf47dee20`,345015B,
[portable HTTPS artifact](https://raw.githubusercontent.com/vpsfreecz/vpsadmin-typescript-client/3cb7cf838a607bbafab207307e11626e57cdec8c/development-artifacts/incident-escalation-sdk.tgz).
The exact retained archive passes ESM/strict types/executor consumer checks and
was downloaded independently with the same hash. Prior source05c/delivery3b98
and old artifact remain reachable through preservation refs and published
`2026-10-30-oomd-abuse-policy-g3-prior`. The final source equals preconsolidation
except for replacing the support artifacts. TS initial18-test batch found one
stale old schema digest; the corrected suite passes18/18. Original failure logs
remain retained; successful unaffected checks were reused.

The site declaration preserves key/source/labels/templates/global mode with
`limits warning:5,stop:10`, suppression false and no selector. Final parser
SHA256 `54f6f26f375330c23155dd7955c8238da3b50ba26231a26ebf13440f73cfce1b`
loads it successfully; this supersedes the earlier provisional parser result.
Actual generated Go scalar/null test confirms the accepted site README sentence.
Config source SHA256 `f3b4549ab502d40fe8bb72de6f4a22e1d9ec4dfdf8aa692ff5e25003a3df5e78`;
README SHA256 `d7d7daf487bd9368326b1e81f1852e21ff75d91425ca44c276260192f66c79ef`.
Historical accepted ce4 tree `eb5ba450085213bd75b769c3eda4b2fcd102f89b`, base5c67e6a. Final rebased tree `457391d83177a8ab7a5276078c2ba8ef15b4d6f5`, base15e3b9af. No owned pin/migration change; all upstream pins retained.

Root final wording pass accepted TS docs SHA1e2ed2d7, Go README SHAa63fa2be
and Rust development docs SHAf24535f2. All three explain actual methods,
capability checks, current facts versus saved evaluations and nullable fields.
Go explicitly documents scalar-null loss; Rust/TS preserve optional/null facts.
No new server availability/permissions or future applicability is inferred.

## Final Rust CI coverage

The ordinary feature push started run44211967472, attempt1, workflow389779539,
exact head `e34ef441468b3e7579719ceb68d1b0b2cce8d101`. It completed SUCCESS at
2026-11-18T01:00:21Z. The runtime observer start was explicitly refused before
registration; there was no monitor/native watcher to replace. Root supplied the
terminal observation, and the existing jobs and complete logs were read once.
[CI interpretation](nov18-g3-client-sync/rust-ci-result.json) binds those raw logs.

| Job | Coverage/result |
| --- | --- |
| client async | Pinned compiler all-targets:2 library+6 policy tests pass;1 real-server test intentionally ignored; examples compile; format/provenance7cases pass |
| client blocking | Pinned compiler all-targets/blocking:2 library+6 policy tests pass;2 real-server tests intentionally ignored; examples compile; format/provenance7cases pass |
| MSRV | Rust1.95 default and blocking each pass the same8cases;1/2 real-server tests intentionally ignored |
| regeneration | Exact saved-source generation check and10 source-refusal cases pass |
| documentation/package (blocking job) | all-feature documentation builds; package verification succeeds with708files, reported2.9MiB/179.6KiB compressed |

The two generated dead-code warnings remain. Cargo's declared package include
list excludes integration-test sources; the generated library package verifies.
No real-server fixture, production call, local duplicate compilation or CI rerun
was performed. Counts above describe each matrix execution, not unique tests.

## Compatibility and documentation routing

New generic policy calls require the final backend resources and permissions.
The prior unmerged flat policy fields and write contract are superseded; the
old `unknown` filter is removed. Typed policy keys remain runtime strings, and
no new call establishes runtime permission or future applicability. Older
released clients remain governed by their captured contract; capability checks
precede new calls. No registry release or consumer/default integration has been
performed. React uses the exact development artifact and still requires its
ordinary published-release prerequisite before integration.

Go keeps the existing scalar-null limitation; Rust uses `Option`, while TS
preserves optional/null output and explicit-null update inputs. The Go OAuth
projection is unchanged and proven to modify exactly one field. No client
rollback undoes a server action. Recover a generated snapshot by restoring its
raw input/provenance/tool locks and generated output together; retained prior
refs preserve the actual supported source/artifact boundary.

| Topic | Reader/class | Authoritative home | Evidence |
| --- | --- | --- | --- |
| Policy calls, optional output and capability handling | SDK consumers/reference | Go README development section; Rust/TS docs/development.md | Actual generated members and HTTP/prepared-request/strict-type tests; root wording hashes above |
| Site declaration, activation and recovery | Site operators/configuration reference | configs/vpsadmin/api/README.md | Final actual parser load and normal config hooks; no activation claim |
| Fixture export and SDK synchronization | Contributors/how-to | vpsAdmin docs/api-schema-export.md | Final backend source guide; retained export+fresh-repeat receipt |
| Exact heads, pin streams, archive delivery and execution | This initiative/individual evidence | This brief and nov18-g3-client-sync receipts | Complete old/new history, raw inputs, generated-set manifests and checks |

No migrations exist in these four G3 ranges. Backend migration/history proof is
owned by G1's final packet, rather than copied into SDK/config source docs.
Initial TS stale-digest failure, Go generator launch missing its Git executable
(before output), and Rust's missing pinned formatter (before output replacement)
remain in raw logs. Corrected native tool paths and substitution-only pinned
Rust tools resolved the environment failures without source or recipe changes.

## Remaining delivery

All intended G3 changes are committed and quick checks pass. Complete ranges
and preservation/consolidation proof are in
[final-history.json](nov18-g3-client-sync/final-history.json). Automatic Rust CI has completed successfully, including the full matrix and
MSRV checks. Root owns independent final review, pending the complete G2 package.
Existing exact Rust CI completed successfully; coverage is recorded below. No duplicate local matrix ran. Published registry
release remains required before React default integration; this development
artifact does not supply it. No registry publication/version bump/default merge,
deployment, runtime reset, capture, cleanup or lifecycle action is authorized.
Old KB/capacity work stays parked at accepted vendor77f7421f; ownership of KB
source/article candidates was returned separately. All evidence/roots remain.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/

## Current-default configuration reconciliation

Fresh SSH fetch and before/after remote reads establish default
`15e3b9af90276e41d19e6a33477add58e5f9a8c9`. Final feature head
`1efed32a70a91e8705be2ceeb6b7dac4ad19e10c`, tree
`457391d83177a8ab7a5276078c2ba8ef15b4d6f5`, contains one two-file purpose over
that exact default. `range-diff` reports `ce4fa64a = 1efed32a`; stable patch IDs
both equal `fe53bfc6be01d46a8dcf52bea3457414f244fcb5`. The two accepted file
hashes above are unchanged. Upstream locks/pins are inherited, with zero owned
changes to them. [Receipt](nov18-g3-client-sync/config-current-default.json)
binds source, toolchain, ordinary hooks and remote publication.

The first replay paused at the ordinary prepare-commit-message hook because the
current lock needed regexp_parser2.13.3. After the frozen bundle was prepared,
Git requested committing the already-staged replay; normal hooks passed, and
ordinary rebase continuation dropped the rescheduled identical patch. No reset,
hook bypass, conflict/source edit or contract change occurred. The current
upstream tool evaluation then identified Ruby3.4.12; old3.4.11 native gems could
not be reused, so an isolated frozen bundle under ignored `.gems` preserves the
old bundle. Current Ruby3.4.12 syntax, scoped RuboCop1file/0offenses and all normal
pre-commit/message hooks passed. The standalone one-file lint pass is in
`config-current-bundle.log` (exit0 in `config-current-bundle.exit`); the failed
`config-current-quick.log` remains historical failure evidence. The receipt binds
both scopes explicitly. All original failures remain in raw logs.

Prior `0be59e51` and accepted `ce4fa64a` have distinct preservation refs; none of
the existing refs were recreated or rewritten. The prior published0be source is
also retained at remote `2026-10-30-oomd-abuse-policy-g3-prior`. The new final
feature was published over SSH with explicit old0be lease and independently
verified remote equality; master stays15e3. No deployment/default integration.
`final-history.json` now stores exact existing ref/object arrays for all four
repositories, replacing the erroneous empty prefix-filter results. SDK source,
archive, refs and checks remain frozen.

## Configuration history provenance

Old range: `5c67e6a010462a850fb6258c486eeef4490c27d5..0be59e51d8473ca0b26b4a9cfe49ca3fe6818fcb`,
old tree `13e7fbe8761151ae54b7cb2f6da8abc207459382`.
New range: `5c67e6a010462a850fb6258c486eeef4490c27d5..ce4fa64a6b6c2a22afb6c7ede2124d5f9ef4e1f0`,
new tree `eb5ba450085213bd75b769c3eda4b2fcd102f89b`.
Both heads have the exact same direct parent. No fetch, rebase or merge occurred.
The existing feature commit was amended, consolidating its superseded callback
with the final declared-limit declaration and documentation into one logical
site-policy purpose. Old-to-new changes exactly the two assigned files. This is
an intended contract change, not patch/tree equivalence or ancestor continuity.
The old head is not an ancestor of the amended new head; retain any deployed
source evidence under its actual old identity. The preservation ref above keeps
that exact old head/tree reachable. Existing published/default refs were not
changed. No dependency/channel/input pin stream or migration changed here.
Final source compatibility and deployment remain separately gated; no claim that
the new head was deployed, literally merged or equivalent to a prior deployment.

Root clarified final export ownership: implementer3 runs the ordinary fixture
export after implementer1 hands off clean committed G1 core, G-mail and G-PHP
with required quick checks. No intermediate export or live database. Continue
automatically through final export and all client/artifact checks on that handoff.
Exporter determinism may be reused only for unchanged exporter/profile/tooling;
repeat from a fresh fixture database if those inputs changed or proof is absent.
