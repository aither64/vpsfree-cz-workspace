# Review: node pool readiness and persistent NixOS development disks

Request: implement the accepted packaging plan, deploy the user profile, and
prove both devcluster providers can start/update/stop/restart with retained
container data. Keep branches unmerged. Password-reset session read-only; no
archive/delete/reset/merge or system deployment. Full context plan.md/state.md.

Workspace root: /home/aither/workspace/ai/vpsfree.cz
All project worktrees: worktrees/2026-09-11-devcluster-packaging-investigation/.
Organization vpsfree-dev-workspace delta base9e8783d68fdf40de04683e419d4f373bc27e3730
(already reviewed, CI passed and deployed) to19238ca67ad822b362ae60f0cf7e7b4b27d60397.
-9a1bd6f waits for ZFS import AND active osctld pool before node mutations; bounded
180-second outer process deadline with one second kill grace, read-only probes.
Actual remote heredoc tests simulate delayed osctld and permanently unready pool.
-19238ca requests persistent NixOS roots, rejects older OSVM before constructing
any VM, moves PID publication after construction, adds runner contract tests and
pins companion OS source for packaged smoke. Standalone OS provider retains old
interface compatibility. Docs state required input and configuration-update order.

vpsadminos delta base3eaf7b7320754715b38fc629e7f0ce23d13402cd to
e6c4c5cfa27ce3b139bba6475be80cfead4b8df4 (one functional commit, already pushed to
make the exact cross-repository test pin fetchable; automated branch CI started).
Adds NixosMachine preserve_root_disk:false constructor option/public reader.
Default test-driver fresh images retained. Opted-in callers reuse existing root,
prepare additional disks, and explicitly destroy/reset as before. Initial/root
replacement copies use same-directory Tempfile plus rename; partial copies do not
become retained roots. RSpec tests cover fresh default, retained data across new
machine instances, reset, additional disks and failed initial copy. Integration
API documentation accompanies the primitive. No osctld/kernel/module changes.

Workspace head1c534c2109dbb8d3920ef933fc770c63df90c17b, currently pins deployed9e8783d;
will receive only reviewed organization pin. vpsadmin8d0ccafd5b307115ddc4b1f24152ba30ed52e893
remains unchanged validation input. Generic runtimebcbaf825 and dependencies stay
unchanged. OS test-input dependencies unchanged; only its source revision moved.

Live evidence: final SSH readiness fixed No-route race, then refresh reached
osctl before its daemon socket existed. Manual refresh later passed. Full
vpsAdmin update on deployed9e8783d passed after changing only node transfer delay.
The restart also erased all services MySQL VPS rows while CT3 remained on node:
NixosMachine unconditionally deleted/re-copied services-root.img each start. This
is a real persistent-data failure within the accepted acceptance scope. Only
our disposable test state affected. Creating a fresh API VPS1 in the current
fixture DB for the eventual fixed-driver retention test; keep old orphanCT3 data.

Ownership/design: OSVM owns the generic machine disk policy; organization owns
persistent development-runner policy and pool refresh. Rejected provider-side
monkeypatch/subclass copies of protected disk-preparation internals. Keep normal
upstream tests fresh by default instead of changing their semantics. The new
keyword requires a newer OS input for vpsAdmin; no unsafe fallback to fresh roots.
Current password-reset recorded OS2166e593 lacks the new keyword and must be
updated/attached to this companion revision before a retry; do not mutate it.
Standalone OS-only clusters keep the previous6f9b2c755 minimum.

Compatibility/rollback: no schema/disk format/CLI/socket/lifecycle contract change
or production/clusterwide node update. Reuse existing complete images without
conversion. Older provider/OSVM combinations can wipe NixOS roots on restart;
document that unsafe rollback instead of claiming preserved data under old code.
A retained NixOS root must contain its direct-boot system closure. Run update in
the running VM before stopping/restarting with changed configuration. This option
is not an offline root-image migration or closure installer. Local operator is
trusted for host administration; remote/guest boundaries unchanged. Existing
nontransactional forced certificate replacement remains separate accepted work.
No credential replacement or force used live.

Quick verification: command suite11/139 passes; runner contract suite3/7 passes;
OSVM full RSpec111/0 failures; bash/ruby syntax and Nix formatting/diff checks pass.
OS precommit/commit-msg hooks pass after direct RuboCop forwarding correction.
Local libosctl native prerequisite compiled in the normal Nix environment; no
kernel compilation. Test-only socket fixture initially missing was corrected;
Minitest lacks mock library, so runner test uses scoped class replacement instead.

High risk (persisted disks, destructive older behavior, cross-project API and
startup). Four lanes general/architecture/scope/risk at gpt-5.6-sol xhigh. Read
mandatory-change-review SKILL.md and assigned lane reference. Review committed
series and local AGENTS.md directly, no subagents/live mutations/project edits.
Save review-persistence-<lane>.md here. Report severity, concrete file/line and
failure scenario; no findings if none, with residual limits. New code has not
been deployed or used in live VM startup. After review: final package/CI, deploy,
copy reviewed VM configuration while running, stop/start and assert API DB plus
container/host markers survive, then stop only our clusters and retain disks.
