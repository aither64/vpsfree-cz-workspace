Final review41cc50af — frozen c51c69b4

Important — R-pane-pid-41cc50af: the new post-maintenance fixture requires an unchanged pane process PID across intentional quiesce.

At c51c69b4, nix/tests/session-creation.nix:1046 compares the target pane's session/id/pid with the source pane. The actual owning quiesce at libexec/dev-session:9548–9552 uses tmux respawn-pane -k on that pane. This preserves its tmux pane identity while replacing the root process and therefore pane_pid. Successful ordinary quiesce and restoration can consequently fail this new assertion before the remaining acceptance cases. The existing observer contract at test/creation_transport.py:160–185 correctly preserves session/pane identity and proves replacement client/native/root identity without requiring a stable pane PID.

Minimal correction: remove only "pid" from the post-maintenance tuple at1046. Retain session/id, exact selected target native/root/socket/token proof, and the source client's PID/startTime absence assertion at1047–1048. The preflight comparison at1015 is a separate boundary without the intentional maintenance respawn and is not included in this finding. No production, helper, budget, permission or design change is needed. Main has accepted this finding and its narrow disposition; it remains present in the exact reviewed committed head. I did not review a remedy.

No Blocking findings or additional Important/Advisory findings.

Identity, settings and exact boundary

Before session records, actual dev-session current and both DEV_SESSION_SLUG/DEV_SESSION_WORKSPACE matched 2026-11-03-lead-wakeup-delivery and /home/aither/workspace/ai/vpsfree.cz. The live same-session roster identifies independent reviewer0, review purpose, ready, thread01a1a349-5cda-76c0-baf0-cc0765288adf, retained gpt-6.1-sol/xhigh/read_only. Installed full_access did not expand my review scope. Capacity was available; no model/effort override, fallback, nested reviewer or watcher was used.

Repository: git@github.com:aither64/dev-workspace.git.
R: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/dev-workspace.
Reviewed head: c51c69b4e0372c29b277bca35be26681e7c254d6.
Tree: dff6a95a9ba56cb8eb742810a5541d0258442256.
Affected: a57d3e6fa4768341ae1c83c5356a0ab4f06657bb..c51c69b4e0372c29b277bca35be26681e7c254d6.
Complete: 3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7..c51c69b4e0372c29b277bca35be26681e7c254d6.

I independently verified clean tracked/index state, head/tree, actual complete series/messages and final inventory, the complete full-index binary diff SHA256 bdc2e494295e92127015bbdec04fefaecfc11780b7004303280e174afded093f, and both affected source blobs against disk. All735 tracked working entries matched committed objects. Relative to a57, only the two assigned test files differ; all733 other tree entries match. The affected range is +203/-22; complete range is11 commits/100 paths/+19670/-183. Prior substantive source conclusions are reused only inside that proved unchanged boundary, not as a fresh broad native/SDK audit.

Guidance and lanes

Applied mandatory-change-review and all four full lane references; read/reused applicable workspace procedures, R AGENTS, current leading packet through its first historical boundary, current plan/state, and the two sufficient design briefs6798/6946. Overall branch risk remains HIGH for durable permission, Stop/startup authority and host transitions.

Scope/proportionality: I compared the supported pause/wait/interrupt/ordinary-activate/stable-resume contract, preservation and stopped-client restoration with the affected changes and retained full-branch growth. These two corrections address demonstrated fixture assumptions through existing seams: direct call-deadline proof and one public start+sync sequence for each of two exact proxy-created roots. They do not introduce another product subsystem, timeout inflation, private recovery writer or generalized framework. The duration concern supports the existing shortest next path after narrow remediation: main-owned normal publication and one original packaged CI, without an extra local preparation cycle. Rejected strict MCP/history/accounting/mail guarantees and automatic child restart remain rejected.

General: B's replacement of the whole-pause stopwatch matches the real pauseNative contract at maintenance_pause.go:132–172 and separate local result bookkeeping at175–185. The four-method test positively reaches the selected silent RPC, checks applicable timeout/uncertainty, exact steer/no-resume counts, a live original parent and persisted deadline/phase/cutover/activation/Stop/continuation/notice identities. Its submitting-ledger assertion uses the real pinned SDK conditional-steer:v1 JSON [cwd, sourceTurn, action] identity. The new callback test at maintenance_pause_test.go:632–659 directly brackets the configured500ms deadline, compares competing grace/allowance/parent deadlines and checks derived-context cancellation. Existing budgets and production bytes are unchanged. No finding in B.

C uses the ordinary public start then sync commands for the original before/after roots after restoring the source listener. Its record/status observations require existing Automatic permission, exact root/socket and source/proxy epoch, with no private writes or third-generation exception. It positively observes actual source clients before capture, retains creation/conversation/team/incarnation identities, requires the exact captured terminal intents and completed restoration, and positively observes target clients afterward. Participant-specific observer arguments are appropriately omitted for idle terminal-only roots. Original bodies and helper/budget boundaries remain intact except the assigned additions. R-pane-pid is the one unsupported assertion.

Architecture/repetition: both changes remain with their owning fixtures and use existing real client/store, public commands and managed-client observer. The small recovery observation/evidence helper does not duplicate permission-generation algorithms or create another restoration implementation. No concrete new drift or ownership defect found.

Risk/compatibility: the affected delta changes no production admission/Stop/native-readiness guard, permission serialization, RPC, persisted schema, package selection, authentication or timing default. Missing/foreign permission and ordinary held behavior remain governed by the previously reviewed production code. Positive target-client proof and old-client absence remain essential; journal/service completion alone is insufficient. This source assessment is not actual Go/native/systemd/VM composition proof.

Evidence assessment

Independently matched all131 B manifest artifacts and all168 C artifacts, their hashes/lengths, both terminal receipts/manifests, and all244 protected prior records. Inspected actual command/result/event logs, the isolated cap mutation, source snapshots and the ledger-oracle-only correction.

B receipt6fcd3ef73a8dae22d31045d0734c7a821ac998ad49f7c43932d90306c74fb6da:
- Initial aggregate naturally exited1/11.476s;11 top-level/8 subtests passed and the new steer ledger oracle failed.
- Only the oracle changed to the pinned SDK encoded tuple. The anchored affected steer naturally passed0/12.091s. Successful unique coverage is12 top-level/9 subtests, with no skips; this is not a green replay of the aggregate.
- The isolated source copy bypasses only the native-call cap. Its sole direct deadline test naturally failed1/17.655s at the new500ms bracket, with the captured deadline equal to the longer grace. The direct test remained byte-identical through the oracle correction; final production is unchanged.
- Original2s parent,500ms call,700ms recovery and1s grace are preserved. GOWORK=off explicitly disables the workspace; it is not an empty setting.

C receipt15c207b82eda570ae3f51ec69626d1c0e0376f57b5336e237f062ff5a4662631:
- Actual quick events establish5 top-level/24 subtests, no failures/skips, with Nix/Python syntax checks; natural0/10.201s.
- This checks existing permission/recovery components and syntax, not the new composed guest sequence.
- Accepted0113 Ruby source binding remains valid within its unchanged scope:26 unique successful methods/225 successful assertions plus host7/195 across qualified batches. The26/213 batch was25pass/1error and remains non-green; no passing aggregate replay or new Nix derivation acceptance is inferred.
- Both final affected blob hashes match checked/committed evidence. No tests or other checks were rerun by me.

Complete history, consolidation, streams and migrations

The final11-purpose series is:
e18a1e8d tracking-admission test;158124c5 durable utility delivery;0659be50 archive hydration diagnostics;f42e8f81 SDK selection;d1c97bf5 maintenance;87d2d14d creation ready-lock evidence;53e61720 creation diagnostics;7dd3a011 grace-transition fixture;2d54d2d8 native-identity/creation maintenance fixture;a7eb8deb bounded proxy timing;c51c69b4 auxiliary preset namespace.

Independent actual-Git comparisons establish:
- a57→7baf retains the first4 literal commits. The B correction is folded into c78f121e→d1c97bf5; all six later messages/stable patch IDs match. Seven paired tree deltas contain only the B test, with the same stable delta patch ID.
- 7baf→c51 retains the first8 literal commits. C is folded into d33d6557→2d54d2d8; both later messages/stable patch IDs match. Three paired tree deltas contain only the fixture, with stable delta850bcdcceefa51f04cddfa0cf1cc8293dc0a56ed.
- Exact a57 and7baf retention refs resolve correctly; earlier retained refs remain present. Neither a57 nor7baf is a literal ancestor of c51.

History conclusion: the corrections are coherently consolidated with their owning behavior. No obsolete approach, transient fixup chain or redundant follow-up history remains in the reviewed final series. Retained failed/published predecessors provide provenance and saved-owner references, not literal successor integration or runtime acceptance.

Stream conclusion: there is one logical SDK/input update, literal f42e8f81 selecting codex-web c3c2adb705f5ff6bb42c98bd44be3649fd93bedb. flake inputs, Go module/sums and selected vendor hash remain its final selection. The later nix/workspace-portal.nix edits install maintenance support/docs and do not create another SDK selection. No redundant pin/input stream or new native/catalog/model input update is introduced here.

Migration conclusion: no database migrations, seeds or format conversions in the complete inventory. The final branch still directly introduces private maintenance schema2 and preserves historical schema1 routing to its immutable SourcePackage owner before interpreting private semantics. The affected changes do not alter those bytes or touch old journals/owners. The source/state lineage is sound within the reviewed supported boundary; historical donor external consumption remains unknown. Equivalence does not prove merge, deployment, consumer adoption or backward execution by an arbitrary old package.

Disposition and remaining limits

Return R-pane-pid-41cc50af for the accepted minimal correction and focused main verification under step9. No further independent finding or broader design remedy is requested. I reviewed frozen c51 only and did not grant publication, runtime or lifecycle release.

Original a57 fast1c56/creation7b534 failures remain failures. Missing historical phase/response/recovery bytes prevent unique cause attribution; these corrections do not establish the old incident's exact production cause. No current local VM/native or original packaged composed success is established. Whole-VM/native, remaining R checks, W/C composition, authorized rollout and usability acceptance remain due; prior identity/tallies do not transfer automatically. Integration still requires its separate approval.

Review completed. All review capacity returned; no command effects, edit ownership or follow-up execution retained. I performed only read-only source/history/evidence work, with no tests, Nix, CI/network, Git mutation, runtime/recovery/profile/claim/integration/deployment/cleanup/lifecycle action. Session remains open; no next package assumed. Lead owns report persistence, finding reconciliation and subsequent allocation.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/
