---
lifecycle: complete
---
# Current status

Phase: complete. Automatic overview/file counts and the Linux preview speedup
are deployed and merged. Final feature CI passed; master package/host/archive
checks passed, while creation exposed an unchanged fork-settings race documented
in [counts-ci-failure-analysis.md](counts-ci-failure-analysis.md). That separate
baseline issue remains unresolved; this delivery does not claim entirely green
master CI. No remaining work, commands, claims or blockers for the repository
review scope. Refresh an existing browser tab to load the new UI.

- [x] Diagnose Git overload and portal latency; implement initial delivery.
- [x] Review, verify, deploy and merge initial delivery; master CI passed.
- [x] Restore automatic overview and collapsed-file counts; review and verify.
- [x] Deploy automatic counts and verify NFS/Linux totals agree.
- [x] Diagnose remaining Linux preview timeout; add full Git index hashes.
- [x] Consolidate final history/pins, focused checks and independent review.
- [x] Final package/system build (556 seconds, complete checks).
- [x] Collect final feature/master CI and reconcile the baseline-only failure.
- [x] Deploy final sources; verify live counts, previews and service continuity.
- [x] Merge exact approved heads, release claims and remove merge scratch.
- [x] Complete final CI and consolidated tracking; preserve the open session.

## Final CI and completion

Feature [run 43272216960](https://github.com/aither64/dev-workspace/actions/runs/43272216960),
attempt 1, exact db4b0fa6, passed archive/fast/creation; host was skipped by normal
feature policy. Authoritative duration: 17:42:13–18:26:18 UTC (44m05s).
counts-final-feature-ci.json contains complete job/run evidence. Watcher
01a1d0e9-efa9-7783-a23d-1a327f452cb8 and launcher 53871 exited 0 and are joined;
its report accounts for all owned command/cell sessions. No work remains running.

Master [run 43275677127](https://github.com/aither64/dev-workspace/actions/runs/43275677127),
attempt 1, same exact head, passed fast/package, host and archive. Creation failed
on the pre-existing fork effort-selection race. Full logs, unchanged-source
comparison, actual form/POST values and scope decision are recorded in
counts-ci-failure-analysis.md. Feature creation passing on the same revision
without a retry corroborates intermittency; it does not fix or erase the failed
master run. No workflow retries/cancellations or source edits followed it.
Parent master watch 54967 exited 1 and is joined. Its authoritative final status
is counts-final-master-ci.json.

Fresh SSH fetch/proof before completion returned the exact final head on each
remote master. Shared workspace remains master; its index is clean before the
owned tracking commit. All feature/deployed-predecessor refs are retained;
merge scratch and extra candidate roots are removed. Backend/public health still
passes at completion. No session archival/deletion or unrelated changes.

## Final delivery evidence

Final build watcher 01a1d0df-a172-7953-abd0-5ace25670a7f and parent launcher
92714 exited successfully, no surviving owned cells/sessions. Full batch took
556 seconds; counts-final-build.log/.exit and watcher result retain proof.
Generation 2026-11-12--18-56-10 built and activated system
/nix/store/lgqf1fy2km8d3jhdkwvqip35aazlylpi-nixos-system-aitherdev-26.05.20261026.718f670.
Current system and system profile match. Workspace profile/portal executable:
/nix/store/s0g8bym5k588czihviybr5822xr4xr0x-dev-workspace-0.2.0.
Copy/dry, no-reboot system switch and normal profile switch all exited 0.
Parent command sessions 56966, 97194 and 72620 are joined. No recovery needed
for this final deployment. Portal PID 304578; ordinary native PID 1309145 and
its November 8 start time are unchanged. Backend health, public HTTPS expected
401, ordinary and naming model/list RPCs passed. Exact evidence is in
counts-final-health.json and counts-final-native-health.json.

The unchanged verify-counts-live.py now passes completely. Results in
counts-live-verification.json bind each frozen pair, counts and timings:
- NFS vpsadmin: 2 files, +349/-4, summary 49.1 ms.
- NFS vpsadminos advanced to 1cb9bbc2: 16 files, +4905/-38, summary 49.8 ms.
- Linux 39a86775..ec577bc1: 3,223 files, +61686/-31047, summary 1,702.3 ms.
- Linux fs/nfs/client.c exact preview: 814.6 ms, +25/-4 matching independent counts.
All overview totals equal complete per-file sums. Repeated count responses match;
Linux repeated read took 25.2 ms. Host timings are measurements, not guarantees.

Each final reviewed base-to-head series was rechecked against the final review:
one coherent commit per branch, no migrations or redundant pin history.
All three exact final heads below were fast-forwarded and pushed over SSH to
remote master, with required hooks retained. Fresh remote equality proofs are
counts-{runtime,configuration,workspace}-remote-proof.txt. Configuration claim
waited six seconds; held status was confirmed while Nix still prepared its shell,
before its fresh checks and Git merge. Shared workspace integration held both
its repository claim and the nonblocking tracking lock, staged nothing and
preserved 2,378 unrelated/owned dirty entries. Detached merge worktrees were
removed normally after claim release. Feature and deployed-predecessor refs
remain. Owned candidate roots were removed after profile selection; installed
profile/generations retain required packages.

All final merge claims are released: runtime 5966b0c2-e1a2-41c6-8df5-084f69fa9ce2,
configuration 5faed448-cd54-4e63-851f-a013c1902c9f, workspace
f080ba8a-c153-4080-b315-9c50ed85fe9c. Machine
faad7680-b349-4d27-8876-e23e5ab55893 was released at 18:05:38 UTC, revision 3,
after verified final effects and complete exact integrated lineage. No archive,
delete or branch removal was requested or performed.

Final feature CI 43272216960 was observed by fresh Luna/low CLI utility
01a1d0e9-efa9-7783-a23d-1a327f452cb8 (launcher 53871), selected chlcbgg2 policy;
explicit full access/approval never verified. Master CI 43275677127 is the same
exact runtime db4b0fa6 and includes the normal host job. The one-utility limit was
occupied, so parent used bounded direct gh run watch monitoring (session 54967,
counts-final-master-ci-watch.log/.exit). No retries or cancellations. Workspace
has no GitHub workflows; configuration's sole workflow is schedule/manual only.

## Final automatic-count correction

| Repository | Review/integration base | Final head |
| --- | --- | --- |
| dev-workspace | 02881b401955ff0db71bb74f6fb84f6e475a7879 | db4b0fa62633b925e1917ec880737e1776f82cc8 |
| workspace | 42c76e8cb61e0d2063a3d25b4b448e66abee523f | 3bdad4b138a346482e98be906660f8526020835b |
| vpsfree-cz-configuration | 5dcde1ce5210a42e4499dbf1b6badbd1f0aa326c | 55b83513b863c704c845e65e956b8230482f173e |

All final heads are committed and published. One commit per branch; no migrations,
obsolete approaches or repeated pin commits. Final comparisons were captured.
Both consumers select runtime db4b0fa6/NAR
sha256-oikFACN3yLS8JwMk/p5NzQ7kzjaH53H97AYmb2mm7sQ=. Extension 0c7168f3, native
Codex 0.165.0, sibling inputs/follows and user-profile ownership are unchanged.

The earlier reviewed/deployed correction heads 4dd6c757, bf0574e49 and f74dd69e
are retained by local refs ending -counts-deployed. They were never merged.
The final runtime retains their complete tree except the --full-index flag and
its explanatory comment; this avoids expensive abbreviation searches in exact
blob diffs. Measured frozen Linux preview: 3.61 seconds before, 0.161 after,
identical hunks. Existing Nix diff/content tests pass (0.673 seconds).
Final deployment-contract check and all range diff checks pass. Full final
redeployment subsequently passed; the earlier nonancestor SHAs are not described
as literally merged.

Independent reviewer /root/counts_final_review, retained gpt-6.1-sol/xhigh,
reviewed all four lanes with no findings. High risk for deployment/API composition.
Original counts review is counts-final-review.md; final series and deployed
lineage are bound by counts-final-review-r2.md. Updated packet:
counts-review-packet.md. Prior documentation conclusions remain valid; the
internal Git flag needs only its adjacent rationale comment.

Original correction quick Go/JS/Playwright checks passed (browser 7.3 seconds).
All 16 Ruby-check derivations matched earlier successful checks exactly.
Composed package/system batch passed in 581.641 seconds; package check 5m24s.
First attempt selected a nonexistent consumer output; corrected to declared
.#default without source edits. Watcher omitted separate log/exit artifacts;
parent reconciled original successful tool transcript and realized roots in
counts-build-reconciliation.json. No rerun. Earlier correction feature CI
43265715007, attempt 1, passed fast/archive/creation; host skipped by policy.
Watcher thread 01a1d0ce-ea77-7443-a46e-eca45d5b979c and launcher 43472 are joined,
no remaining operations. Full authoritative result: counts-feature-ci-result.json.

Final build watcher (completed; see final delivery evidence): fresh Luna/low, selected chlcbgg2 catalog
f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d, utility
 dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569. Native thread
01a1d0df-a172-7953-abd0-5ace25670a7f, launcher 92714, explicit danger-full-access
and approval never verified. It owns /tmp/portal-counts-final-build.sh;
counts-final-build.log/.exit and watcher transcript/result hold evidence.
Final feature CI: 43272216960, attempt 1, exact db4b0fa6, passed.
No superseded running CI remained after force-push (predecessor had succeeded).

## Earlier correction deployment (superseded)

System and profile both select
/nix/store/zlwdk1fyv5nqprz16hgd5rxbcqhzwrfs-nixos-system-aitherdev-26.05.20261026.718f670,
generation 2026-11-12--18-25-23. Workspace profile and portal executable select
/nix/store/chlcbgg2i86n7pahydlfvbghnhifiv2x-dev-workspace-0.2.0.
Copy/dry/no-reboot system activation passed. First profile switch exited 1
because repository registration/local Git proof changed during activation;
selected forward package retained. Retried the same ordinary source switch,
which completed with exit 0 (counts-profile-switch-recovery.log/.exit).
No lock/journal edits or process signals. Backend health and public HTTPS pass;
public unauthenticated response is 401 (local curl used --insecure because the
internal CA is absent). Ordinary Codex PID 1309145 remained continuous from
November 8; ordinary and naming model/list RPCs pass. Portal PID 138755.

NFS vpsadmin: 2 files, +349/-4. NFS vpsadminos: 15 files, +4311/-37.
Linux frozen 39a86775..ec577bc1: 3,223 files, +61686/-31047. Summary and per-file
counts agree and repeat through cache. The first live script failed only its
additional Linux content comparison because that preview hit the pre-existing
four-second Git timeout; counts remained valid, including client.c +25/-4.
Direct tree numstat independently confirmed +25/-4 in 0.158 seconds. The final live
script subsequently passed unchanged after deploying the full-index fix.

At this earlier checkpoint, held machine claim: faad7680-b349-4d27-8876-e23e5ab55893, revision 2.
verify-machine passed again for final configuration 55b83513.
The then-unacquired merge requests were: runtime 5966b0c2-e1a2-41c6-8df5-084f69fa9ce2;
workspace f080ba8a-c153-4080-b315-9c50ed85fe9c; configuration
5faed448-cd54-4e63-851f-a013c1902c9f. Detached merge targets were prepared at 02881b40 and 5dcde1ce. The final
integrations used the short claims and shared tracking lock, then removed those
scratch targets and released ownership as documented above. Unrelated shared
files/index, feature refs and this open initiative remain preserved.

## Authorization and ownership

User, November 12: "you can deploy aitherdev using vpsfree-cz-configuration.
merge after verification". Scope: aitherdev system/profile and remote master
integration of dev-workspace, workspace and vpsfree-cz-configuration.
During the blocked system switch the user directed: "well the portal is offline
right now, so you have to fix it". The recovery is recorded below and in
[rollout.md](rollout.md). No reboot, session archival or branch deletion.

This conversation created the initiative with --no-attach/--no-codex on November
10; current and identity environment were absent. It remains our original
threadless initiative. No retained roster exists; team list reports no valid
lead thread. Lead owns application work; independent reviewers and verification
utilities use installed catalog fallbacks. Initial tracking commit: d58f2bfb1.

## Initial delivery source and remote proof

All repositories use branch 2026-11-10-portal-linux-review-performance in
worktrees/2026-11-10-portal-linux-review-performance/<project>.

| Repository | Final base | Exact final head, proved on remote master |
| --- | --- | --- |
| dev-workspace | 6587c4c1cedabee95bcc52f4667e7d33e3a82859 | 02881b401955ff0db71bb74f6fb84f6e475a7879 |
| workspace | 05ad6ab3e430ac69ec20d94a481843a7e1f57124 | 42c76e8cb61e0d2063a3d25b4b448e66abee523f |
| vpsfree-cz-configuration | dda57166bd8bb6d85a74decdd05a8810933bdecc | 5dcde1ce5210a42e4499dbf1b6badbd1f0aa326c |

Each series has one coherent commit, no migrations, obsolete approaches or
repeated pin streams. Final comparisons were saved before integration. Ordinary
fast-forward merges and SSH pushes passed with hooks enabled; fresh ls-remote
proved each exact remote head. Workspace integration held its repository claim
and the nonblocking shared tracking lock, preserved unrelated files/index, and
staged nothing. Configuration merge/push used its declared Nix shell. Detached
merge checkouts were removed normally; feature refs/worktrees remain.

## Initial delivery review and verification

- [Application review](final-review.md): /root/portal_final_review,
  gpt-6.1-sol/xhigh, installed fallback because no roster exists. High
  compatibility risk; general, architecture, scope and risk lanes. Reviewed the
  complete branch; no migrations/obsolete history/repeated streams. Important
  summary suspend/resume and legacy 5,000/5,001-record boundary findings were
  fixed, focused-tested and folded into 02881b40 under narrow-remediation rules.
- Targeted Go/JS and live-browser regression passed in Nix. Full repository Go
  suite 16.1s, web suite 251.5s, browser regression, flake checks and package
  build passed at 02881b40. /root/portal_verification joined session 97048,
  exit 0, about 15m45s; verification.log/verification.exit retain evidence.
- Feature [Check run 42805944135](https://github.com/aither64/dev-workspace/actions/runs/42805944135),
  attempt 1, exact 02881b40: fast, archive and creation passed; host skipped by
  normal branch policy. No retry. Earlier CLI watcher returned incomplete with
  an unfinished watch handle; parent reconciled processes and exact API result,
  then joined watch session 86406. No remaining operation from that batch.
- [Composition/history review](deployment-review.md): /root/deployment_review,
  gpt-6.1-sol/xhigh catalog fallback; original reviewer no longer live. All four
  lanes. Sole Important finding was workspace baseline advancement. Rebased
  290a659de on 2ffa0b1c to 42c76e8cb on 05ad6ab3; range-diff proved equal patch,
  final contract/diff checks passed, retaining review under its explicit narrow
  repair conclusion. No old workspace revision was deployed.
- Both locks select runtime 02881b40 and NAR
  sha256-TLsZCYeW4bPgcA/QAEkyjZDizq7sko4KPyVyt3PRdRA=. Extension
  0c7168f352f6d4f11c46368e702b9356d81012c6, sibling inputs, follows and native
  Codex inputs unchanged. Deployment checker, deployment-contract and
  tracking-source checks passed. No system-installed application was added.
- Composed package build passed. Initial confctl build ended at its interactive
  prompt, before activation; corrected system-only `confctl build --yes`
  passed in 129s under fresh Luna/low /root/system_build. Both batches joined.
  Copy-only, dry-activate, no-reboot switch and guarded profile switch passed.

## Initial deployment and recovery

System and system profile:
/nix/store/1gcqjfy0r9f2b6l6cczn9m30vn54najm-nixos-system-aitherdev-26.05.20261026.718f670.
Configuration generation: 2026-11-12--16-28-33.
Workspace profile and active portal executable:
/nix/store/a0nhkz2khja7qp17vw5fh1p8327i10iw-dev-workspace-0.2.0.
Package derivation: ph14qm33lqkzlxlsgwda74pxpfzmlkv6.
Portal PID 3304698; naming child 3304966. Ordinary Codex remained PID 1309145
throughout, using the unchanged 0.165.0 package. Both native/naming model RPCs,
backend health and public HTTPS checks pass. Public unauthenticated request
returns expected 401; local curl lacks the internal CA, so that credential-free
transport check used --insecure. No authentication data was exposed.

System activation stopped nginx at 16:32:35 CET before blocking on user-unit
reconciliation. Backend health alone did not prove public availability; the
initial report was corrected. Thirty-two foreign `team assign --message-stdin`
wrappers were waiting on terminal input, holding shared transition locks for
hours. After the user's restoration direction, each exact command/start identity,
TTY, lack of children and wait state was rechecked, then only those wrappers
received PID-specific SIGTERM via pidfds. No agent/daemon/process group was
killed; no lock or journal was edited. Nginx was started and the original
confctl operation completed normally, retaining auto-rollback. System/profile
paths match; both health checks passed. Parent session 82986 and all original
SSH/auto-rollback/switch processes finished. /root/deployment_wait joined its
own observer work; exit 0, total 19m43s including the blocked interval.

Pressure GC had deleted the unrooted --no-link candidate at 16:33:57 CET.
Ordinary profile selection rebuilt the same source and passed its packaged
checks/protocol compatibility; no source edits or bypass flags. Profile command
25312 and CLI watcher launcher 7704 exited 0. Watcher thread
01a1d077-c476-71a1-869b-91ed8eae36f0 was Luna/low, danger-full-access, approval
never; launch policy verified. Logs retain the expected /tmp PATH-alias warning.

## Linux acceptance

Live history initially failed because full commit resolution took 4–5 seconds,
exceeding the unchanged four-second Git budget. The clone held 29,130 packs but
its November 10 multi-pack index covered only three. One foreground
`git multi-pack-index write`, with lazy fetch/auto-maintenance disabled, succeeded
in under a minute. It changed only the object index: no fetch, repack, expiration,
object deletion or branch change. Observed RSS about 1.9 GiB, with 67 GiB available.
New index covers all packs; commit lookup took 165.6 ms. linux-midx-write.exit is 0.

Current live Linux range: 39a867754a8a743765a458e87d3a46ce26990f83 to
ec577bc14bb1a4212a52caf6af829978cd287aae, which advanced since the earlier
benchmark. History 567.8 ms; deferred summary 984.4 ms; 3,223 metadata records
334.3 ms, pending counts and no eager preview. fs/nfs/client.c content/diff
succeeded in 4,212.5 ms with 25 additions/4 deletions. Both content hashes and
request timings are in live-repository-verification.json. This is a warm host
measurement, not a cold-cache latency guarantee.
Earlier candidate benchmark at head 94b072af9c091c2638716e313c7d2aa8dc9be74d
returned 4,162 records in 245.6 ms and selected content in 419.8 ms.

## Initial claims and completed CI

All released after required effect/remote proof:

- Runtime merge: d0589727-4a66-46f9-8388-bdde026b8d9f.
- Configuration merge: 4f8ef03b-e2fc-4f94-b19a-cb58c20976cc.
- Workspace merge: 1db9145c-f36e-4309-8e4c-78bf5b1abb4c.
- Machine: ac205ec4-2d6d-4551-8adb-58e493865e89, released 16:09:26 UTC,
  revision 3, after complete verified deployment and exact integrated lineage.

Master [Check run 43255030699](https://github.com/aither64/dev-workspace/actions/runs/43255030699),
attempt 1, exact 02881b40, passed all four jobs. Fresh CLI watcher thread
01a1d083-6b29-7a40-a820-a96322225700 completed observation; parent launcher session
61638 was joined with exit 0. No watch process remains. Selected a0nhkz2 package policy: Luna/low, full_access,
danger-full-access, approval never, utility dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569;
catalog SHA256 527918949048890e311178d620a30706d74abd3d5f4687335112aca4d4966a0c.
Runtime monitor API unavailable for this threadless initiative. No workflow
retry/cancellation. CLI's expired ancillary connector auth does not affect the
codex-lb model; credentials were not changed.

## Documentation and limits

Initial README and dev-workspace/docs/workspace-portal.md explained pending counts,
exact-content renames, no implicit fetch, deferred summaries and link/rollback
limits. vpsfree-user-facing-writing and English humanizer were applied directly.
New metadata file IDs need the new portal; rollback preserves saved comparison
revisions but cannot resolve those IDs in old code. No persisted-format migration.
The existing 5,000-file cap, browser editor retention and explicit missing-object
preparation remain stage-2 work. No automatic maintenance was enabled.

Operational lessons: [deployment blockers](../../notes/cross-project/2026-11-12-portal-deployment-blockers.md).
Raw logs are untracked/disposable. Preserve branch refs and this open initiative;
completion does not authorize archival. The automatic-count correction below
supersedes content-only counting; larger pagination/editor-retention work remains
outside this delivery.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-portal-linux-review-performance/


## Final master CI disposition

Run 43275677127, attempt 1, db4b0fa6, completed 18:20:42 UTC with failure.
Fast/package, host and archive jobs passed. Creation job 131383300700 failed
because the unchanged fork form submitted medium after high was selected.
counts-ci-failure-analysis.md records actual form/POST evidence, unchanged-source
provenance and the background refresh overwrite path. This pre-existing fork
settings issue is outside the delivered repository-review scope; retain the red
result and do not rerun blindly or describe it as fixed. Parent watch session
54967 exited 1 and was joined; full authoritative final status is
counts-final-master-ci.json. Feature watcher 53871 also completed and was joined, as recorded above.
