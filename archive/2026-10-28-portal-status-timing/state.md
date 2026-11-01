---
lifecycle: complete
---

# Current status

User approval on October 29: “so if it looks good, let's merge it and release
aitherdev”. Scope is the four registered deliverables into their configured
master branches: codex-web, dev-workspace, vpsfree-cz-configuration and workspace.
This authorizes integration and release after verified deployed-lineage evidence;
it does not authorize archival. The later explicit instruction “all right,
let's delete the backups” authorized removal of the two retained migration homes.

- Phase: complete, including the subsequently requested fresh live creation test.
  Automatic naming, initialization, completed reply and private-home persistence
  passed; its thread and rollout are absent from stock state.
- Migration accepted October 29 at 13:27:47 CET; 2724 portal histories passed
  native reads, with 4360 stock threads retained separately. Codex 0.165, portal
  and tmux remain healthy on the verified deployed system/profile.
- The original confctl attempt was accepted as turn
  01a187a1-6581-7071-959c-20dca7142893; fresh transcript paging confirms that exact
  turn remains present and idle. Never resend the accepted message again.
- Browser renders timing for both reported sessions. Autostart retains its idle
  execution hold. Historical timing remains approximate for unobserved periods.
- Final live acceptance: read-only tmux attach/detach succeeded for this
  initiative; native conversation and naming sockets initialize and read config,
  both selecting private portal SQLite storage. Naming has no loaded threads.
  Existing exact-native naming/provider tests and successful live stock DeepSeek
  probe cover unchanged binary/provider behavior; no optional new naming canary
  or dormant-session execution is needed for release.
- Remote master proofs: codex-web f6f4a187, dev-workspace cc0d452a,
  configuration 584691d9, workspace 5fc7000f8. Workspace deployed head 1cb755a3
  has an independently reviewed patch-equivalent successor 5fc7000f8; both
  evaluate to deployed derivation 13wf9a0j. See integration-lineage-review-result.md.
- Dependency ancestry: unchanged extension 767dfd58 equals upstream master;
  llm-agents 91ff550f is an ancestor of upstream main (fresh GitHub comparison).
- Machine claim 0f7f1a64-cb9b-480b-bdf1-345e77f1374a was released and its released
  state verified at 12:57:26 UTC. All four short merge claims are released.
- Codex-web post-merge CI 40877082705 passed on exact f6f4a187. Runtime CI
  40877149430 passed on exact cc0d452a: fast, archive, creation and host all
  succeeded. Workspace/configuration define no runs for these heads. No
  superseded workspace feature workflow needed cancellation.
- Authorized backup cleanup completed: both retained old-home directories
  removed, reclaiming 34,361,597,952 bytes (about 32 GiB). About 88 GiB is now
  free. Live home identities, portal health and the test conversation passed
  post-cleanup checks. Logs/journals and feature refs/worktrees are retained.
  No archival requested.

The following investigation checkpoints are historical; the current summary
above supersedes their pre-deployment status.

See [design.md](design.md) for the implementation and verification brief.
All feature branches are `2026-10-28-portal-status-timing`, under the same
`worktrees/<slug>/` group: dev-workspace, codex-web, vpsfree-cz-configuration,
and workspace. The configuration checkout hook initially lacked ambient Ruby
gems; registration exists, so repair within its Nix shell without recreating it.

Detailed evidence and the exact retry identity are in [diagnosis.md](diagnosis.md).
The user's October 29 clarification resolves the interface question: stock CLI
need not access portal threads; existing portal tmux clients provide terminal
access. No deployment has been made. A connection-scoped
unsubscribe of the idle confctl thread returned
`notSubscribed`, confirming it cannot release another connection's ownership.

Latest read-only checks: system stock CLI is 0.165.0; workspace service remains
0.164.0. Their processes held 14 and 47 thread-writer locks respectively. Both
reported thread locks still belonged to the managed stock daemon. Both target
threads were idle when subsequently queried. The event that first opened them
in that daemon is not proven; do not claim the user manually opened them there.
The runtime currently derives its Codex home from inherited CODEX_HOME or
~/.codex; its tmux clients already use the workspace's explicit remote socket.

Application changes are in progress; live services have not been changed. No retained team was created; team list
reports no lead thread for this tracking-only shell initiative. The shared index
was empty and shared master matched origin/master before the initial checkpoint.
Unrelated workspace changes are preserved.

## Evidence

- `workspace-host status`: selected package
  `/nix/store/7wqvb8wdy58x94nh24k0kqnagqldfhvi-dev-workspace-0.2.0`.
- Autostart thread: `01a163b4-e2c6-7081-b9cb-e7a0e78eab4b`.
- Confctl thread: `01a14bb2-e3ad-7922-a5c9-bc1d07d5cbb8`.
- Portal Unix socket reads avoid the ambient curl trust-store mismatch with the
  internal CA; no credentials are needed for this local operator endpoint.
- User explicitly permits retrying `yes go ahead` after repair.

## Phase checklist

- [x] Initial investigation and scope.
- [x] Root cause established and implementation design accepted.
- [x] Runtime isolation, upgrade and migration implementation.
- [x] Applicable checks and independent review.
- [x] Host deployment and system/provider acceptance.
- [x] Portal home migration and profile switch; automatic acceptance.
- [x] Live health, private storage and both timing displays verified.
- [x] Authorized original message retry verified.
- [x] Terminal attach and both live native backends verified.
- [x] All four approved remote master integrations.
- [x] aitherdev and short repository claims released.
- [x] Final post-merge runtime CI and completion records.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-portal-status-timing/

## Implementation checkpoint (October 29)

- codex-web published head: ba8dfdd27daa7ab3f4350f7a2627984b6b7f84cf.
  Strict 0.163 and prompted 0.164 contracts remain; 0.165 adds a native fixture,
  upgrade fixture and exact source provenance. Full 0.165 catalog adds only Terra;
  derived Luna remains 62680 bytes with the existing digest.
- Exact 0.165 native SHA-256: 647b0157e6472a793e0a0bd45bc44ef8ade673b6d8f3db4118260acda4976652.
  The llm-agents package keeps its daemon Nix-store patch and chatgpt recursion
  limit insertion. Upstream adds native state migration 62 (attached parent).
  Both 0.164/0.165 source trees have temporary initiative-owned indirect GC roots.
- dev-workspace private home propagation and native storage launch identity are
  committed and published at 8c597b6f5c3b10ca8d9193f2da7ef4cc3a4b21a5.
  Naming/package prerequisites select 0.165. The fresh vendor derivation passed.
- Quick evidence: codex-web full Go unit suite, tagged version-probe tests,
  exact binary schema/client corpus and all 55 config restrictions passed.
  Runtime local protocol and focused naming tests passed. Initial host suite had
  two stale-home assertions and five long Unix socket path failures. Corrected
  assertions and TMPDIR=/tmp: focused 23 tests/742 assertions passed. Use the
  aggregator test/workspace_host_test.rb; individual shard files omit fixtures.
- Configuration worktree registration is complete. Overcommit installed through
  nix develop; no hook bypass used. Workspace feature worktree is also registered.
- Fresh independent ChatGPT login completed in the private portal home; credentials
  were not copied or printed. Existing stock login remains untouched.
- Initial read-only inventory: 7074 native rows, 507 registered/retained roots and
  members, 2723 portal-owned threads including dependencies, 4351 stock rows,
  no shared ancestor dependencies and no missing portal rollout. A missing
  historical test member is explicitly state=removed and excluded by the same
  retained-member rule as runtime; preserve its old native row in stock.
  Portal rollouts total about 13.27 billion bytes. Inventory still needs recovery
  and archived prompt references before final cutover. Current free space ~98 GiB.
- One-time inventory code/JSON and schema fixtures are untracked operational
  artifacts. Preserve the final reviewed migration source in Markdown or another
  durable permitted location before execution; do not rely on untracked archive
  retention. No migration, deployment, live resend or master merge has occurred.

Recovery/archived-prompt references increased explicit inventory seeds to 660;
the closure remains 2723 portal and 4351 stock threads, with no missing owned
rows/rollouts or shared dependencies. Completed provider snapshots contain eight
historical original rollout paths; they are evidence, not active recovery state.
Active provider state currently says applied. Recheck final transition readiness.

Fresh vendor derivation jndaqzn3gqjpcis944g8q36dgcrj4jcx produced
sha256-XEvzpQbsCzcHzhTdqghrjhGmiqna25MPU2b/wGJekqA=; runtime now uses that hash.
The discovery build failed as expected against a fake hash. Final build remains.
Configuration functional edit selects a private copy of the portal codex-lb token;
stock codex-ds continues using its stock key path.

## Final implementation evidence

- Runtime: 8c597b6f5c3b10ca8d9193f2da7ef4cc3a4b21a5 (published).
- Configuration: dcb5982fd4325d57cda79693fa4da27c7a955413 (published).
- Workspace composition: 5deaee4fcf6692f617e346aa84ab3f95f52c3bfd (published).
- Full runtime Go unit suite passed; focused native-client tests passed (2 tests,
  12 assertions). Earlier unrelated host socket-path fixture failures were fixed
  by TMPDIR=/tmp; corrected home expectations passed the focused host batch.
- Final composition check passes and preserves extension
  767dfd587e346168e1443e65ccdb67ce748f3fe3. System llm-agents was already the
  frozen 91ff550f revision, so its channel command made no redundant commit.
- Seven synthetic migration tests passed in about three seconds: exact schema
  and history preservation, untouched source, unknown stock records, missing
  portal history, low space, unknown schemas, atomic exchange recovery preserving
  new writes, wrong directory identity and live open-file exclusion (some cases
  share a test). Root /proc inspection uses existing SSH access to 172.16.106.40;
  ambient sudo needs a password and is not used by the operation.
- Latest inventory: 7075 indexed, 661 seeds, 2724 portal, 4351 stock; no missing
  portal history or shared dependencies. Existing missing stock rollouts stay
  unchanged. Portal rollouts total 13,275,356,461 bytes. Free disk is
  97,049,088,000 bytes (90.4 GiB); repeat capacity admission after final builds.
- Four portal shell snapshots contain old-home entries only in PATH. They do
  not set CODEX_HOME/SQLite storage; retain snapshot bytes and native history.
- One-time source, recovery behavior and deployment preparation are preserved
  in [rollout.md](rollout.md). It is not installed by any project package.
- Current session has no retained lead/team. The installed catalog digest is
  495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7.
  Mandatory review fallback is delegated/reviewer: gpt-6.1-sol, xhigh,
  read-only review instructions, effective full-access execution. No roster changes.

## Review remediation and final pins (October 29)

The independent Sol/xhigh review in [final-review.md](final-review.md) found two
blocking recovery/concurrency gaps and stale VM fixture homes. The fixture paths
are corrected. The detached runner now starts the failed selected hook before
ordinary switch admission and watches source writes through copying/publication.
A durable source metadata fingerprint protects recovery across observer loss.
SQLite's derived SHM reader-lock file is excluded; WAL/database/rollout writes
remain observed. Read-only WAL sidecar preparation precedes observation.
Fifteen synthetic fixtures pass, including short-lived rollout and WAL writers,
normal WAL reading, interruption before/between exchanges and selected-hook retry.
Operational source is committed at 5e267d26a; it has not been executed live.

Final published revisions:
- codex-web: f6f4a187509b3bebfc81585c535be856eaab0d04.
- dev-workspace: 7d1163585a51da684be0f5cdd500a64822165839.
- configuration: c92408739d53d0e5198710723d89d8189f0f4d99.
- workspace: 277833e8f9d8a45a502afca02b5df527da9440f0.

Fresh vendor derivation returned
sha256-2aYEuOcFTjdecQu/GEP2i2sLlYi5eMnDxpKb2nyU7Mw=; final runtime uses it.
The composition check passes for these pins and the unchanged extension.
Configuration's repeated runtime pin updates are consolidated into one generated
commit. Workspace rebase onto 5e267d26a is patch-equivalent (`range-diff =`).
Codex-web CI 40852873773 passes. Its earlier failure was an asynchronous WebCrypto
upload-recovery test timing out after 50 immediate spins; the focused test fix
uses a 5-second deadline with 2ms scheduling intervals. Runtime CI 40848346561
passed fast/package but failed creation/archive due to stale fixture homes.
Corrected final runtime CI 40854716525 is running. No failed checks were blindly
rerun and no obsolete active runs remained to cancel at the last query.

Independent follow-up [review-remediation-result.md](review-remediation-result.md)
accepted the observation/recovery design and final branch history/pins, but found
that unconditional chmod on reacquired source locks changed ctime. The narrow
fix leaves existing 0600 lock metadata unchanged. The outer-runner fixture now
fails after publication intent/before exchange, reacquires real locks, starts the
selected hook and completes without losing source or new writes. All 15 fixtures
pass (8.3 seconds). This requested narrow fix is verified directly under review
skill step 9; no new design or additional review lane is introduced. Blocking
findings are resolved; native/package verification may proceed.

Native batch: namespace ownership control passed. Prompted fixture refused the
mutable checkout catalog before protocol execution, as its immutable-resource
contract requires. Corrected the probe to the exact final codex-web Nix input
resource (same 62680-byte catalog and hash), then rerun only the failed/unexecuted
checks. This was verification setup, not a product failure. Final builds were
not started by the failed batch. The explicit PATH-alias warning is native's
known /tmp helper restriction; it did not fail the version/ownership checks.

Exact native checks passed in 91 seconds after correcting the immutable catalog
probe path: prompted 0.165 protocol, 0.164-to-0.165 state upgrade/resume/fork and
native provider routing. Namespace ownership had already passed. Detailed output
is native-final-immutable.log. Final workspace head is now
20916892cbcf2c1e51ebfb72b7bc09851bb7b00c after a patch-equivalent rebase onto
abe635989; other reviewed heads are unchanged. Six checksummed operational files
are prepared under the private maintenance directory, with interpreter/library
GC roots; no config, journal or migration service has been launched yet.

Final acceptance preparation found a separate cause for the timing label. The
autostart session's recovery API reports `idle` with executionHeld=true; its
activity API already returns historical timings. Browser app.js unconditionally
skipped that read for a held conversation, and an existing test explicitly
expected the label. A bounded follow-up runtime commit
cc0d452a0653a112c8a013492c1734d9554bb909 permits cold activity reads only after
recovery verifies idle and refreshes at that transition. Execution holds remain;
the existing actual HTTP/browser fixture now asserts native resume/send/queue
effects stay absent until explicit original input. Focused recovery/retained-input
Go checks passed (4.7 seconds), JavaScript syntax and diff whitespace checks pass.
This corrects the original display report alongside the separate writer conflict.
Its review, real browser check and refreshed consumer/package pins remain.

Host preflight found protected same-UID /proc entries also affect native process
classification. It now uses the existing root SSH inspection path, fixed to
aither UID1000, like the descriptor scan. A disposable copied executable fixture
proves embedded-CLI classification. Sixteen fixtures pass. The broader process
scan found stock CLI clients (0.158/0.160/0.164/0.165) still using the shared home.
The runner now waits for stock clients before draining either backend; the user
has been asked to exit these clients. Portal --remote tmux clients remain ordinary
switch-owned. The post-drain scan still refuses every source native process.
This avoids an unnecessary outage/refusal and never kills user CLI clients.

## Final reviewed artifacts and admission (October 29)

Independent final operational review: [final-ops-review-result.md](final-ops-review-result.md),
Sol/xhigh, same reviewer as prior rounds; no findings. All prior blocking findings
resolved. Whole-branch history, consolidated pin streams and migration lineage
accepted for these final published heads:

- codex-web: f6f4a187509b3bebfc81585c535be856eaab0d04.
- runtime: cc0d452a0653a112c8a013492c1734d9554bb909.
- configuration: 584691d9b96ce1555a5787a0a1d999eeb528811f.
- workspace: 1cb755a3d2f8729c3c42beda86cc492a14dd22f3, based on cf92beac0.

The workspace rebase from c2511ea73 is patch-equivalent (range-diff `=`), also
independently verified. Final Nix derivation is identical before and after rebase:
`/nix/store/13wf9a0jd1lhrwf6vdf9dvllwyhpapk5-dev-workspace-0.2.0.drv`.
The built application is
`/nix/store/d0wikyzpr7qk1w2c2zbqgj97qz1m58qn-dev-workspace-0.2.0`.
Final composed lock check passes. Nix reports a dirty sparse Git source, but
Git status/index/diff are clean and the exact evaluated derivation matches the
successful build. No application input changed in the rebase.

Browser/native final checks passed. The last seven-minute browser/build batch
is `timing-browser-build.log`; system generation is `2026-10-29--11-47-30`,
with target `/nix/store/fczhh0f76j8sy2awv7skrv2rp59vr7lg-nixos-system-aitherdev-26.05.20261026.718f670`.
Fresh preflight inventory: 7081 native rows, 2724 portal, 4357 stock, no shared
ancestors or missing portal rows/rollouts. Stock retains preexisting missing
historical rollouts. Source is 34.67 GB; free disk is 96.87 GB, sufficient for
source copy plus 8 GiB scratch and 20 GiB reserve. The six private operation
copies now match the reviewed cf92beac0 fenced source and hashes. No config,
journal, migration hook or live selection has yet been created.

## Deployed host and detached operation (October 29, 11:59 local)

Runtime CI 40858490632 passed at cc0d452a (22m26s); fast, creation and archive
passed, host was skipped. This completes the requested final CI observation.
Machine claim 0f7f1a64-cb9b-480b-bdf1-345e77f1374a is held by this initiative.
Configuration 584691d9 deployed through confctl generation 2026-10-29--11-47-30
with a successful separate dry activation followed by a no-reboot switch and
configured auto-rollback preserved. Both /run/current-system and the system
profile resolve to the exact built fczhh0f76j8sy2awv7skrv2rp59vr7lg output.
System health and firewall checks passed. Stock CLI is 0.165.0. The single
strict-config DeepSeek request returned CODEX_UPDATE_OK (8.5 seconds), log
live-provider-check.log. Temporary empty request cwd is
/tmp/portal-codex-provider-20261028-e1E3SH.

The detached user unit portal-codex-home-migration-20261028.service is running
(PID 142031 at launch), invocation 25bfa463a64247a694160f8ff4fa5cc2.
Private config binds reviewed workspace 1cb755a3 and application d0wikyzpr7.
The journal reports waiting-for-idle with the remaining stock CLI and active
threads. No home exchange, profile switch or message resend has occurred yet.
User-manager linger is enabled, so the job survives terminal/logout.
The portal and native services remain healthy on their old profile pending cutover.
The unit has unlimited start/stop timeout, SendSIGKILL=no and Restart=no.

The operation itself performs inventory conservation, all portal-thread reads,
private native-home/binary checks, activity reads and same-ID message retry.
A failed operation retains its journal and backups; recover the exact operation
under rollout.md. Manual live browser/tmux/provider/naming acceptance remains
pending even after its phase becomes accepted. Do not call the portal repair
complete until those results are available. The machine reservation remains
held until verified deployment and integrated deployed lineage; no merge or
release has been performed.

## First live failure and bounded recovery (October 29)

The first unit exited at 12:11 local with forward-recovery-required. It selected
the correct application package but never entered the publication hook. The second
quiescence pass uses the selected new helper's private Codex home against the
still-running old backend. The archived retained lead-policy-canary proof refused
its .codex rollout path. This is a migration ordering/context error, not history
loss or an active-writer conflict. Old native remains PID156049; pending target
and claim remain intact. The portal service is inactive until recovery.

Operational adapter and its exact packaged-host fixture are retained in rollout.md
at 867320a0e. No product/source pin, runtime schema or Nix output changed. A live
read-only source process/home/marker proof passed, and the exact formerly failing
require-execution-idle call passed with .codex context, without resume/send.
Six adapter fixtures/21 assertions and 16 existing partition fixtures pass.
User-installed Minitest6 hid Ruby's bundled mock helper and loaded duplicate plugins;
explicit bundled GEM_HOME/GEM_PATH plus MT_NO_PLUGINS=1 yields the expected six
actual tests. Do not count the earlier zero-test exit as verification.

The same reviewer completed [selected-recovery-review-result.md](selected-recovery-review-result.md)
with no findings across all four lanes. Refreshed only changed private sources
from reviewed 867320a0e and verified all eight checksums. The original failed
unit was restarted at 12:25:47 local, same config/journal/claim. It is running
with phase waiting-for-idle, error null, one active native thread and reopened
stock CLI PID307640. Previous failure is preserved in lastFailure. No new home
publication or message delivery has happened yet. Stop neither user CLI nor
old native manually; the reviewed operation owns the transition after idle.

## Second failure and actual-input rehearsal (October 29)

The second attempt failed at 12:29 local before the publication hook. The raw
Ruby adapter had bypassed the package shell wrappers, selecting ambient Python
without jsonschema in nested activation. Shell launcher migration-host.sh now
preserves both installed wrapper environments byte-for-byte except final
dispatch, with bundled Ruby. Reviewed operational source is 0560c7569; the same
reviewer found no findings in launcher-recovery-review-result.md. Both exact
old/new native checks passed through the real corrected launcher; all six adapter
cases/21 assertions and 16 partition cases pass. A read-only process scan from a
transient user service also passed with the hook's actual service environment.

Actual-input rehearsal is /tmp/portal-home-rehearsal-9vp15v4q, owned by this
initiative, with command rehearse-native-home.py and log native-home-rehearsal.log.
It reads original files/SQLite in read-only mode, copies portal rollouts and
splits both actual database partitions into disposable storage, then starts
0.165 on those copies and cold-reads every portal thread. No credentials are
copied and no live services/threads are changed. Success removes only its own
rehearsal directory. Failure preserves that directory for diagnosis. Fresh watcher
launch was unavailable in this turn; explicit parent monitoring fallback is in
use. Do not mistake its copied test state for published production migration.

Actual-input rehearsal passed in about nine minutes (12:44:41–12:53:36 local),
exit 0. All2724 portal rollouts were checksum-copied, both partitions of all five
actual databases passed schema/content/integrity/relation checks, and exact 0.165
cold-read all 2724 portal threads at their rewritten paths. Loaded-thread set
remained empty and owned native exited 0. Portal history retained 865987 items and
17878 turns; stock retained 420278 items and 4345 turns. Existing stock queued rows
were preserved. Evidence: native-home-rehearsal.log/json; private disposable
/tmp/portal-home-rehearsal-9vp15v4q was removed on success. Free disk returned to 88 GiB.

Final read-only preflight installed inotify coverage for 3286 source directories;
root descriptor inventory found only the known old portal native, current stock
CLI and its managed daemon holding source data. No unrelated writer was found.
All nine private operation sources match reviewed 0560c7569 and the shell launcher
has mode 0700. Restarted the exact original unit after these checks; retained
config/journal/source/profile/claim unchanged. Still no production home exchange
or original-message resend at the restart boundary. The actual copy/validation
can take roughly 10–15 minutes after idle; do not confuse copying with an error.

Terminal observation before recovery: retained tmux panes are alive in shells.
Do not indiscriminately sync every dormant session; normal attach/sync and recovery
holds govern terminal startup. Browser/tmux/provider/naming live acceptance still
follows successful migration. The earlier failed switch may have left previously
quiesced terminal clients requiring normal dev-session sync after cutover.

## Integration and release evidence (October 29)

The four complete final series and diffs match accepted independent review;
no obsolete unmerged approach or redundant pin stream remains. The bounded
independent lineage review used /root/integration_lineage_review at installed
Sol/xhigh, replacing the unavailable earlier reviewer. No findings.

| Repository | Target | Exact integrated final head |
| --- | --- | --- |
| codex-web | master | f6f4a187509b3bebfc81585c535be856eaab0d04 |
| dev-workspace | master | cc0d452a0653a112c8a013492c1734d9554bb909 |
| vpsfree-cz-configuration | master | 584691d9b96ce1555a5787a0a1d999eeb528811f |
| workspace | master | 5fc7000f8a5fd1aa1f60c9731cbbb4b8c59a2e13 |

All integrations used fresh target checks, ordinary fast-forward merges, enabled
hooks and SSH pushes, then exact remote-ref confirmation. Configuration's Nix
shell passed Nixfmt/RuboCop hook preparation and its merge hook completed without
failure. Workspace merge held its repository claim and nonblocking tracking
lock, preserved all unrelated changes and staged nothing. The rebased feature
was published with an exact force-with-lease before integration; its predecessor
remains retained in deployment evidence. Saved repository comparisons precede
integration. No branch refs were removed.

The same exact system and profile paths remain deployed. Migration unit exited 0,
journal is accepted/published/error=null, and no uncertain deployment remains.
The original accepted receipt is retained in acceptance.json. The live send ledger
has retired that attempt since completion; this is not a reason to retry it.
The native transcript page independently exposes its exact accepted turn.

All machine-retention conditions were satisfied before releasing aitherdev. A
new deployment requires a new claim. Waiting for the post-merge runtime CI does
not retain machine ownership because exact source CI already passed and this
integration changed no deployed code. The watcher tool was unavailable, so the
parent monitors that existing run with bounded output under the skill fallback.

The deployed nonancestor workspace head is additionally retained under local
refs/deployments/2026-10-28-portal-status-timing/workspace at 1cb755a3d2f8729c3c42beda86cc492a14dd22f3, so ordinary reflog expiry cannot discard its lineage.
No optional fresh-session smoke test is required after the existing packaged
creation checks and completed live acceptance; none was launched.

## Final completion

Post-merge workflows completed successfully:
- https://github.com/aither64/codex-web/actions/runs/40877082705
- https://github.com/aither64/dev-workspace/actions/runs/40877149430

The runtime run reports success for fast, archive, creation and host at exact
cc0d452a0653a112c8a013492c1734d9554bb909. Parent watcher exited 0 and no owned
verification process remains running. All registered exact final feature heads
are integrated and no required work remains. State is complete; the session is
not archived. Branches, feature worktrees, original-home backups and original
operation evidence remain retained. Routine tracking updates remain local under
the existing daily checkpoint cadence; no additional tracking commit was made.

## Fresh live creation acceptance requested

User asked whether a new session had actually been created and verified to save
under the workspace Codex home. Earlier checks did not exercise fresh live
creation; acknowledged that gap. Run one normal portal preparation request with
automatic naming, installed solo preset and one no-tools marker reply. Keep its
request ID stable, inspect its exact thread/database/history paths and prove no
same ID exists in stock state. This is ordinary session creation, not deployment;
aitherdev remains released. Do not delete/archive the new session without user
authorization. No product edit or new independent review is needed for this test.

## Fresh live creation result: passed (October 29, 18:08 CET)

Normal portal POST /sessions returned 202 for request
3ac62d57-0a64-406e-8291-2dd7b245f02b, using automatic naming and the installed
solo preset. The ordinary preparation/initialization reached ready without a
retry and created 2026-10-29-portal-storage-smoke-test. Lead model was
 gpt-6.1-sol, provider openai. Its only turn completed with the exact assistant
reply PORTAL_STORAGE_SMOKE_OK and returned to idle; no tools or extra work.

- Thread: 01a188a2-8d9b-7683-aaca-2309465aae3b.
- Turn: 01a188a2-9523-7a12-81c9-9101fd5131da.
- One row in /home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz/state_5.sqlite.
- Zero matching rows in /home/aither/.codex/state_5.sqlite.
- Persisted rollout: /home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz/sessions/2026/10/29/rollout-2026-10-29T18-08-36-01a188a2-8d9b-7683-aaca-2309465aae3b.jsonl.
- Parsed assistant reply is present in that rollout; stock-home counterpart absent.
- Read-only portal transcript paging independently returns the completed reply.

Raw evidence: fresh-creation-{request,acceptance,status,thread,storage}.json.
The new test session is retained for user inspection:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-29-portal-storage-smoke-test/
No archival/deletion, package switch, deployment or new machine claim occurred.
This replaces the earlier acceptance limitation concerning fresh live creation.
No remaining required work.

## Disk-retention clarification

Read-only disk check after the fresh-session smoke test: active stock ~/.codex
uses about 16 GiB; active workspace Codex home uses about 17 GiB. The migration
copied and partitioned the source, validated the copies, then atomically exchanged
directories. The original shared source remains at private operation
partition/stock and uses about 32 GiB. The original prepared private login/config
home remains at partition/portal and uses about 30 MiB. Thus live conversation
partitions are separate, while pre-migration data is duplicated in the retained
source backup. Current filesystem free space is about 56 GiB. No backup deletion
was requested or performed. Removing the retained backups would reclaim about
32 GiB; any later cleanup must verify the exact operation and live directory
identities rather than interpreting stock/portal staging names as active homes.

## Authorized migration backup cleanup: complete

User explicitly instructed: “all right, let's delete the backups”. Removed only
partition/stock and partition/portal under the private migration operation root.
Before deletion, held the original runner/publication locks, confirmed the unit
inactive and hook absent, checked accepted journal/acceptance, and matched both
backup and live directory device/inode identities to the publication record.
The privileged read-only descriptor scan found no backup data in use.

The removed directories occupied 34,361,597,952 allocated bytes (about 32 GiB).
Available bytes increased from 59,567,017,984 to 93,928,587,264; df reports 88 GiB
available. Both live homes retained their original post-publication identities.
Portal/native/tmux services remain active; health returns HTTP 200 and the fresh
smoke-test conversation and rollout remain present. Journal, acceptance,
verification and switch logs were retained. The private backup-cleanup.json
records exact removed paths/identities and successful completion. The original
migration backup is no longer available; do not rerun its completed cutover or
attempt a shared-home rollback. No service restart, deployment, session removal,
branch deletion or new reservation was performed. No remaining cleanup work.
