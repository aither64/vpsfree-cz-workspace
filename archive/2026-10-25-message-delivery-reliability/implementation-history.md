---
lifecycle: active
---

# Message delivery reliability

Delivery fixes and the orphan-backup review correction are committed and checked.
The runtime has been refreshed onto the exact newly deployed archive-policy-3
baseline ec53874b. A separate creation admission race is corrected and its focused
Go/Ruby tests pass, including source replacement and worker cancellation. Affected
review, final candidate checks and activation remain. No live migration, machine
claim or original-attempt repair has occurred. No default-branch merge is authorized.

- [x] Reproduce the deadline race and establish the pre-transmission boundary.
- [x] Implement transactional storage, recovery, browser retries and plan lifetime.
- [x] Pass library Go/browser and focused portal/archive/profile checks.
- [x] Finish matching runtime/configuration/workspace pins and publish branches.
- [x] Independent final branch review and resolve findings.
- [ ] Packaged and applicable native/lifecycle verification.
- [ ] Claim aitherdev, activate, verify continuity and delivery.
- [ ] Revalidate and recover the exact stuck attempt without duplicate submission.
- [ ] Integrate only after explicit repository/target approval; release machine
  ownership only under the installed retention policy.

## Ownership and worktrees

Tracking was enabled by the user after the initial no-tracking implementation.
The failed `dev-session start --no-codex` performed no tracking creation: existing
feature worktrees required an explicit manifest. These new records describe the
current work directly. `CODEX_THREAD_ID` and native `thread/read` independently
identify current conversation `01a17206-ed6f-78b3-b410-c7d6015b6777`, its workspace
CWD and the registered vpsfree-cz socket. No conversation or roster is replaced.

All four worktrees use branch `2026-10-25-message-delivery-reliability` under
`worktrees/2026-10-25-message-delivery-reliability/`. The shared workspace remains
on master and contains unrelated changes that must be preserved.

| Repository | Initial base | Current status |
| --- | --- | --- |
| codex-web | 872c7ad3962f9fa9b17358244e27f3e3fac59fc5 | Published final library 7c84dc4d29566d99d7935627920dd653565aa379 |
| dev-workspace | 10bb047513c82d1310e8fcaa797e8772f948dd8a | Published 9bf4282185f9440eb9257d71d03636a353ee1282 |
| vpsfree-cz-configuration | d12a77374b18e15fe7600f95307114e2e1882828 | Published 59ade10f2c8b14de54303528e66e1538572d6a4d |
| workspace | b1b86b2b8a075666ccdef7f9d254047be972508a | Published db59ca58df9b649c01aeca7a5303bde270b53db2, rebased onto current shared master |

## Verification and evidence

Full library Go tests passed (codex about 22 seconds); browser retry/generic
contracts passed. Focused migration tests passed after atomic schema bootstrap.
Portal checks against the published library passed for plan dispatch, service
lifetime, typed outcomes, archive recovery, shipped browser assets and versions.
Ruby compatibility checks passed again (2 runs, 34 assertions). Native Codex
remains 0.163.0. Final composed-lock validation passed. Library CI on 7c84dc4
passed. Runtime CI on 9bf42821 failed three isolated test fixtures before VM execution; see [CI addendum](review-ci-addendum.md). Parent is correcting those fixtures, with no application changes.

Independent reviewer: `/root/message_delivery_final_review`, standalone
`gpt-6.1-sol`/`xhigh`, read-only, selected from the installed default team's review
role because the verified live roster is null. Catalog digest
`840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`.
Risk: high (persistent state, delivery boundaries, package compatibility and
forward recovery). Lanes: general, architecture, scope, risk. All intended
deliverables were committed and quick checks passed before assignment. See
[review packet](review-packet.md); report pending in `review.md`.

The library bootstrap correction was folded into its owning backend commit, and
the runtime pin refresh into its one dependency commit. No superseded migration
or repeated pin remains. No intermediate source was deployed or externally
consumed; disposable checks used an earlier published source. The workspace
feature retains pre-existing shared-master coordination ancestry, as identified
in the review packet. Initial tracking commit is `01c06f60`; it was not pushed
separately to default because shared master already contained unrelated local
coordination commits. It is preserved in the published workspace feature ancestry.

Logs are currently under `/tmp/message-delivery-reliability-2026-10-25/`; retain
compact evidence in this directory before handoff. Initial failures were diagnosed:
Unix socket fixture path length (set TMPDIR inside Nix), a missing TryLock method
(implemented), typed uncertainty expectations (updated), missing scheduler asset
embedding (fixed), and dependency timestamp timezone (corrected to UTC).

Final vendor hash for runtime:
`sha256-S1+JRkfIWOqNf9wS73W1vJPMzUMhQ1UnWZtQzaXKCO0=`.
Library vendor hash: `sha256-/NKkY+lT/h0ctIdTIkPgEn214M10xd95unGGNgyfK34=`.

The selected profile remains
`/nix/store/8ph05i3nps8xi1jfs450b16aysc16nvg-dev-workspace-0.2.0`.
No live migration, state repair or deployment has occurred. See [plan](plan.md)
and [design](design.md) for compatibility, acceptance and original recovery identity.

## Review resolution

[Independent review](review.md) found no Blocking issues and sound complete
history/migration lineage. The Important generic attachment-free retry finding
was fixed by retaining the original empty attachment list instead of consulting
newer composer uploads. A mounted-browser regression failed before the fix
(`calls: 1`) and passed afterward with the same UUID, no attachments, and the
newer draft/upload preserved. The Advisory SQLite timing identity omission is
fixed for single-attempt scopes. Focused browser/storage/deadline tests pass.

The three CI fixture corrections also pass their focused checks. Trailing
whitespace identified by review is removed. These are narrow corrections inside
the reviewed design, so mandatory-review step 9 applies without a redundant
reviewer rerun. They are folded into their owning commits. Exact final dependency
and downstream pin refreshes are being consolidated; preserve the original
review's ranges and record final comparisons before readiness. No migration,
public contract or deployment boundary changed.

## Post-review verification

Fresh utility `/root/post_review_checks` (`gpt-6-luna`/`low`, full access) ran
three independent operations and returned ownership with none still running.
Full portal Go suite passed against final library 0d17f1e (about 2m46s); four
pinned native App Server contracts passed (about 35s, native Go result 21.8s).
Logs/status: `/tmp/message-delivery-reliability-2026-10-25/post-review-{portal,native}.{log,exit}`.
The intentional fake-hash bootstrap produced final runtime vendor hash
`sha256-OBJxJ7v8o2Y+DOhzIGyt1bB7dC6N7lhj+eI49pfHUdY=`. No kernel build or live
service mutation occurred. Final dependency and downstream pins are being folded
into their one owning update per stream before package/profile builds.

## Final candidate heads

See [exact final heads](final-heads.json) and the retained review/final range-diffs.
All four feature worktrees are clean and base-to-head whitespace checks pass.
Library: 0d17f1e347c4592f5a4159ef384106ad287275a2; runtime:
ace4e0e9762ca40444e8bd7284462034646226e0; configuration:
e054fb5e0da070cfeda291362e975e028e89062d; workspace:
7baae084e2c101d40b49933aa87c904c0baa415e. Each retains one final pin update;
configuration preserves the final generated confctl message while consolidating
the superseded pin. Native Codex, extension and sibling inputs remain unchanged.
Library CI on 0d17f1e is green. Runtime CI 40182797562 and candidate builds are
owned by fresh native utility thread 01a17285-57c2-7782-9590-0d58db3f1531,
verified from native startup: gpt-6-luna/low, approval never, danger-full-access.
The completed review's Important/Advisory remediations are narrow, tested and
folded into the owning commits; no new schema or compatibility path is introduced.

Prepared original-attempt recovery follows the review's exact-row/claim and
backup requirements. Disposable SQLite verification passed dry-run, exact update,
consistent backup, unrelated-row preservation and stale/newer-claim refusal.
The script does not send a message and has not touched live state. Actual recovery
still requires current native acceptance proof, compatible activation and held
machine ownership. Backups will remain outside the portal Files tree.

## Reboot refinement and first candidate results

Before activation, parent found that the socket-adjacent legacy path lives under
`/run`: ready validation would fail after reboot removed the fence, and its old
source-adjacent backup was volatile. No live state has been migrated. The design
now keeps source backups beside the persistent database and reconstructs missing
fences from the committed ready journal under predecessor locks. Interrupted
committed import accepts an absent volatile source only with its verified durable
backup. Present changed files still fail closed. Five restart/refusal cases pass,
including preservation of the unresolved receipt. This material recovery refinement
requires affected independent review before acceptance.

The prior native utility finished with no local operation remaining. Its profile
build passed at 7baae084, producing
`/nix/store/1v2q9xrmr27r3g8ishgyk9p917haq7f3-dev-workspace-0.2.0`; it was NOT
activated and will be superseded. Configuration build stopped at its ordinary
`Continue? [y/N]` prompt (EOF); the authorized repeat needs `confctl build --yes`.
CI 40182797562 had a passing fast/package job, but creation failed when a fork's
source slug lock was held by another dev-session command. Captured browser body
and terminal receipt show `another dev-session command is changing
2026-10-25-explicit`, before fork initialization; no missing diagnostic or silent
message failure. The nonblocking Ruby source lock predates this change. Preserve
that evidence and inspect the unchanged lock call path before accepting a later
run. Full failed logs remain in /tmp/message-delivery-reliability-2026-10-25/.

An attempted message to the native CLI watcher to stop superseded builds was
refused by native thread/resume because it had an active writer; no cancellation
occurred. It subsequently completed its own batch normally. No live system/profile
or original attempt was touched.


Affected review uses fresh standalone native reviewer
`01a172a0-e739-7563-85b4-f3c8fc7f0ef2`, verified at launch as
`gpt-6.1-sol/xhigh`, approval never, full access with the catalog's read-only
reviewer developer instructions. Retained original reviewer identity was confirmed
from native metadata (`01a1726d-f645-71e0-8bde-29ffeb7deff5`, parent this thread,
`/root/message_delivery_final_review`, same saved model/effort). The available
native send API refused its continuation: direct app-server input is forbidden
for multi-agent v2 subagents. A standalone fallback records that communication
failure instead of bypassing it or self-reviewing. Original review is preserved;
reboot-review.md will cover the material recovery refinement and final heads.

Final refined candidate heads are in reboot-heads.json. Runtime is 48476400,
library f391c5e; configuration 229b8e9f and workspace 136caa22 retain one final
pin update each. Composed-lock validation passes. Full refined library Go tests
passed (~22.7 seconds), and focused published-dependency portal checks passed
(~5 seconds web, ~0.24 seconds archive). Runtime vendor hash is
`sha256-+F3Buoebm/FQbvQguBF3rFmBgP3zewF0QecyB3wFOrs=`.
The fresh hash watcher initially mistook its role and attempted forbidden nested
delegation without launching the build; an explicit same-operation clarification
made it run the assigned build itself (19 seconds, expected fake-hash failure,
actual hash above). No check was blindly rerun.


Native pre-deployment history probe initially conflated presentation metadata
pending with paging completeness and trimmed plan text before hashing. The
runtime plan digest hashes exact bytes. The probe is corrected to keep those
fields separate and hash exact text. It sent no input and changed no receipts.
Native MCP independently reports the target not loaded and its latest turn
interrupted; the paged read's status projection is not sufficient evidence of
current execution. Use current exact history plus the original pre-transmission
error, never missing history alone, for any recovery.


## Affected review and orphan-backup resolution

The fresh independent reviewer completed all four affected lanes and whole-branch
history review; see reboot-review.md. Actual independent identity is native thread
01a172a0-e739-7563-85b4-f3c8fc7f0ef2 (its default standalone agent path is /root,
not this lead's native identity). History/pin consolidation and migration lineage
are sound. One Blocking risk finding confirmed the explicit pre-commit orphan
question: an unreferenced durable backup could be ignored after /run disappeared.

The requested narrow correction is implemented: when no predecessor is present,
empty-phase initialization scans only for this database's backup-name prefix and
refuses an empty import if evidence remains. It does not guess or import a backup.
The regression reconstructs the post-backup/pre-commit crash, removes volatile
sources, and verifies refusal, intact backup bytes, no predecessor fences and no
ready empty journal. It fails against f391c5e using a Go overlay, while the fixed
full library suite passes (codex ~23.1 seconds). No other finding remains. The
prescribed guard and regression fit mandatory-review step 9, so another reviewer
confirmation turn is unnecessary. The correction is folded into the backend
commit and final metadata/pin refreshes will be consolidated again.


## Managed coordination handoff

The initial manual manifest binding to external investigation thread
01a17206-ed6f-78b3-b410-c7d6015b6777 was invalid for portal ownership: that chat's
CWD is the workspace root, while a session conversation must use its tracking
directory. The new session page correctly refused conversation access, and sync
reported no managed tmux session. No machine claim or deployment used that binding.
The owned manifest is now honestly threadless with explicit complete scope. Commit
this ordinary baseline, then use the supported initializer to create a managed
coordination-only conversation under the correct session directory. It must not
edit or implement work. This is a genuine authority handoff needed by deployment,
not adoption of another initiative or a fabricated ownership record. Preserve
all existing feature worktrees, branches, native conversations and team settings.


## Current baseline refresh

Managed owner is now initialized successfully at native thread
01a172c4-ca9f-7c70-b3e5-b1290a0568eb. Portal conversation lookup works; live
roster is null, so lead retains design/implementation and independent review
uses the retained standalone reviewer. The prior manual root-CWD binding was
never used for a claim or deployment.

Exact selected runtime source matches ec53874b6eea73bf65099cf19aa1a4bc5a3336aa
by Git blob identity against /nix/store/61cgny1cyg3mrpi2g75yfdvhklxjbm7a-source.
Runtime feature now 101a1850253e7cb17f89c8e01f7d11a1b0860948, four focused commits
above ec53874b. Rebase was conflict-free. Configuration refresh uses the matching
deployed 2d33a9ca baseline. Workspace refresh preserves the already deployed
compact tracking/storage behavior through exact cherry-picks of 7f94bfa79 and
eda0d9944 onto shared master, replacing the superseded runtime pin with one final
update. These inherited changes were not designed by this initiative.

Creation CI failed twice at nonblocking source EX acquisition, before native fork.
The exact historical holder is unknown. Shared browser queue reconciliation uses
this lock; controlled real Go/Ruby tests identify an external SH holder and prove
the same refusal. Accepted source-bound workers now wait at both source stages
without destination locks, recheck identity, retain the existing deadline and
process-group cancellation, and keep ordinary CLI admission nonblocking. Focused
test passes (~4.7s) for both stages, unchanged/replaced source, cancellation and
journal recovery. No schema or API change. See design.md for the bounded brief.

An initial workspace lock update matched no URL and remained running. A corrected update overlapped it, causing the first to fail at Git index.lock.
Both processes are finished; the successful final update changed only the intended
runtime/library nodes. Composed-lock validation passes. No lock was manually removed.
