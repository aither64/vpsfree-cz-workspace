# Aitherdev provider rollout

## Scope and preparation

Authorized by "Implement the plan": deploy the provider catalog through the
configuration feature branch and the composed application through its user
profile. No default integration, forced interruption, session closure or native
Codex upgrade. Preserve existing global config/auth and subscription backups.

The initial catalog selects codex-lb to match existing routing. Subscription ID
is openai. Snajpa is http://172.16.106.12:2455/v1, with credentials referenced
only by /home/aither/.codex/aither-on-snajpa-codex-lb.token.

Pre-rollout native service PID 2615996 and portal PID 2832678 remain active.
Selected user package is
/nix/store/yb4mamskfrlzaz71ncp3363bhl4jc6hg-dev-workspace-0.2.0.
Its derivation source /nix/store/z12mvgjj11b22xb2j0qr687iwm2x1g28-source
matches the runtime base 1a27453c exactly (Git archive/no-index comparison).
Selecting the feature therefore preserves the current baseline behavior.
Current system is
/nix/store/apsqp7fvi89kjc0fxp7gijq03sr4jm3n-nixos-system-aitherdev-26.05.20261010.6fcc160.

Native remains 0.160.0, actual executable
/nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0/libexec/codex/bin/codex.
The provider implementation does not modify the native package selection.

## Remaining ordered checks

1. Pass isolated native routing/settings/compensation and real-worker VM checks.
2. Publish the final runtime; consolidate each downstream pin stream and verify
   extension/sibling/follows identities and check-dev-workspace-deployment.
3. Build the scoped aitherdev configuration and composed user package. Inspect
   dry activation, including service changes beyond the provider catalog.
4. Confirm current package generation, journals and live restart/adoption policy
   immediately before mutation. Preserve guest and active thread processes.
5. Deploy the matching host catalog/module and select the composed user profile
   with workspace-host switch. Refuse unsafe native restart; do not force it.
6. Check portal previews, active provider identity, sidebar data and switch/cancel
   admission. Verify both directions in a genuinely idle live window when one is
   available; isolated native proof covers both directions meanwhile.

## Recovery preparation

Retain system generations, selected user-package roots and feature refs.
Global Codex backups remain untouched. Provider recovery uses its native snapshot
and journal rather than overwriting histories or databases. Once private provider
state exists, package recovery must select a corrected package advertising the
matching schema and policy. A waiting request can be canceled. Applying or
recovery-required state reserves writes until the supported worker verifies
compensation. Terminal restoration notices require dev-session sync.

Execution results will be recorded here. No deployment has occurred yet.

## Verification results

Native routing at 0fd76973 passed in 46.44 seconds, log
/tmp/provider-native-0fd.log. The selected 0.160.0 executable retained IDs,
history prefixes, model, reasoning effort, sandbox/profile, latest idle policy
and tier updates, and the required MCP helper. Subscription-to-pool and reverse
inference reached exactly the expected endpoints (6 subscription, 3 pool calls).
Compensation used the same helper without performing inference.

The a13 fixture failure was an unscoped test activation after helper-owned
subscriptions disconnected. The native thread lifecycle explicitly unloads idle
threads without subscribers; the fixture now activates with retained settings.
Focused fixture compilation and native routing pass. Live services remain
unchanged. Real-worker VM recovery is running separately.

The first VM run failed at its unquoted cgroup path; shlex.quote preserves
systemd's literal backslash. The second run at da86d090 passed the host-module
VM and packaged suites, but the recovery VM waited after removal of a foreign
process. A read-only reproduction against the live Codex cgroup showed Ruby's
glob also interpreted the backslash: zero matches despite an existing path;
using a literal base finds its process file. The exact owned build was canceled
(exit 130), and its QEMU/build processes were confirmed stopped.

Runtime 084a659d keeps the cgroup root literal, with a passing descendant/PID
regression and improved phase diagnostics. Ruby provider checks pass (13 runs,
45 assertions), Nix parse/diff checks pass. Matching consolidated pins are
configuration a4ba33a5 and workspace 9533c364; extension/sibling/follows paths
are preserved. The exact composed contract passes at
/tmp/provider-deployment-contract-084a.log. Root SSH to the scoped host is
available and confirms the unchanged pre-rollout system generation.

Final prepared selection after the usage fixture correction:

- Runtime 42791ba5afb00b466f76c95bf807b9e6668e7d37; production source is identical
  to reviewed 084a659d except the disposable VM handler's usage response.
- Configuration 82ad72d0cef9af8065badb2590c279a5cb6a2b87 and workspace
  28167f33b48513e8f5efb10e603fdbc5f51c1988 select that exact runtime.
- Both pin streams are consolidated. The latest generated configuration message
  is unchanged byte-for-byte; original and locked workspace input identities
  agree. Extension, siblings and follows remain unchanged.
- Composed deployment contract: /tmp/provider-deployment-contract-4279.log.
- Quick real-helper fixture preflight verified both synthetic authenticated
  endpoints. Recovery/build batch uses a fresh watcher; current CI is
  https://github.com/aither64/dev-workspace/actions/runs/38325388272.

No deployment has occurred. Earlier revisions above are verification history.

## Configuration build and activation preparation

Final-head CI 38325388272 passed. Scoped `confctl build --yes
cz.vpsfree/machines/aitherdev` passed and produced generation
2026-10-13--02-20-31, system
/nix/store/qdwzchqcpbh3qiax45g0ll27ibn9aa7k-nixos-system-aitherdev-26.05.20261010.6fcc160.
The first build invocation stopped at its confirmation prompt with EOF before
building; the documented --yes option supplies the already authorized build
confirmation. No local kernel build occurred. Full stdout is retained at
/tmp/provider-config-build-4279-yes.log. Closure comparison adds only the provider
catalog; native Codex is unchanged.

The fresh watcher owns recovery VM and composed package checks. The parent owns
the concurrent scoped configuration build/dry-activation under the monitor
skill's visible fallback because the installed utility permits one concurrent
watcher. Scoped dry activation passed (exit 0), without reported service changes;
log /tmp/provider-config-dry-activate-4279.log. No system switch or profile
selection yet.
Live process-boundary inspection still shows original service PIDs and the
unrelated Python helper in the native cgroup. Portal/router contain only their
expected service processes and the portal's quota reader. Private config/auth/
token identities are unchanged and no package transition is pending.

Final recovery VM at 42791ba5 passed (exit 0), test script 417.23 seconds;
/tmp/provider-recovery-vm-4279.log. All four provider/reboot scenarios passed,
including the final lingering reboot in 58.98 seconds. Repeated recovery phase
assertions were temporary wait observations: compensation completed and the
test proceeded successfully. QEMU cleanup completed normally. Composed
workspace package build is now running at 28167f33 with locked inputs required.

## Executed rollout

Composed package build passed with --no-update-lock-file on 28167f33, yielding
/nix/store/9krkxik0ma49qwpn77c4238dxvd5pzw0-dev-workspace-0.2.0;
/tmp/provider-workspace-build-4279.log. Candidate native package is still
a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0. Candidate and predecessor
advertise livePackageSwitchPolicy 1; native launch package also advertises 1.
Provider schema and transition policy are 1. Saved exact comparisons now match
all four final published feature heads.

The parent launched the scoped system switch selecting the exact already-built
generation 2026-10-13--02-20-31. Its fresh Luna/low watcher observes separate
log/exit artifacts and has no deployment authority. System and application
mutations remain owned by the parent. Host log: /tmp/provider-host-switch-4279.log.
Application selection follows successful host activation and a repeated native
adoption/process preflight. No provider request has been submitted yet.

Host activation passed (exit 0), with 2/2 health checks passing. The exact tested
qdwzchqc system generation is now active. Installed catalog is a regular,
root-owned 0644 file and declares openai/codex-lb with initial codex-lb.
Repeated preflight retained native PID 2615996 and predecessor profile; portal
and router cgroups contained only expected service/quota-reader processes.
Private file identities remained unchanged. Parent launched stable
workspace-host switch against the verified workspace source;
/tmp/provider-profile-switch-4279.log. The watcher observes it without mutation
authority. Selection is still in progress; no provider request yet.

Application selection passed (exit 0) at profile generation 116. Protocol and
semantic checks passed with unchanged Codex 0.160.0. Native PID remains 2615996;
portal is 322255, router 322230 and provider worker 324030, all active. No package
transition remains pending. The unrelated native-cgroup Python process 3218417
and other guests were retained.

Live acceptance:

- Both previews passed: subscription returned one window; Snajpa returned
  metrics and two windows. Active provider stayed codex-lb. Public catalog
  contains only id/label/kind, never endpoints or token paths. Subscription reset
  controls are disabled while LB is active. Read-only log:
  /tmp/provider-live-previews-4279.log.
- Served HTML contains the active-provider label, preview select, separate
  Switch and Cancel controls. Served provider JS matches reviewed source.
- Owned request af828073-ac3d-418f-9d2b-1b5271feae11 targeted openai and remained
  waiting. The 15-second smoke deadline expired before the first inventory
  finished; /tmp/provider-live-switch-cancel-4279.log records that harness limit.
  Subsequent observation showed six blockers and a healthy worker. Exact API
  cancellation returned 202/canceled and preserved active codex-lb. The owned
  operation identity is retained privately in
  /tmp/provider-live-owned-switch-operation.json. No production cold resume or
  daemon restart occurred. Both actual routing directions are proved by isolated
  native execution; a live idle window was unavailable.
- Final private state is regular, owned by UID1000 and mode0600, with terminal
  canceled operation. Global config/auth/token fingerprints are unchanged; both
  backup directories remain. No token or fingerprint values were disclosed.

Rollout is verified and available for use. All feature branches remain published
and unmerged, awaiting separate integration direction. No archive, deletion,
forced interruption or unrelated process cancellation was performed. Earlier
prepared/no-deployment statements describe the checkpoints before this section.

## Cancellation feedback follow-up preparation

The user-reported stale cancellation banner is fixed in runtime7c07b540,
selected by configuration bfb1d89c and workspace33c0834d. Committed independent
review is complete; focused browser/status and corrected Go checks pass.
The composed deployment contract passes and generated pin streams remain
consolidated. Provider state/receipts/schema and native protocol are unchanged.

Before rollout: native 2615996, portal322255, router322230; selected user profile
116/9krkxik0 and systemqdwzchqc. No package transition pending. Snajpa remains
active and the retained verification operation remains canceled. Global config,
login and token identities match the prior private snapshot.

Build the composed user application and scoped system first. If the system
closure remains identical, retain the deployed host and only select the user
profile. Check candidate/predecessor/native launch compatibility and process
ownership before stable workspace-host switch. Confirm served asset versions,
source bytes and the retained live cancellation rendering as empty, with both
previews and unchanged native PID/provider. Do not submit another live switch
or erase receipts for this UI verification. Execution results follow below.

Composed build and exact-head CI 38366486448 passed. The final workspace rebase
is patch-equivalent and derivation-identical to the built da517c1b input.
Candidate application is mipb66x7; scoped host generation 2026-10-13--10-22-17
is l51k28cg. Closure comparison shows only confctl deployment metadata and its
aggregating store identities changed; the provider catalog is byte-identical.
Normalized activation scripts match. The parent will dry-activate and select
that tested metadata generation before updating the compatible user package.

Dry activation and exact host generation switch passed (exit 0), with 2/2 health
checks and no service changes. System l51k28cg is active. Native PID 2615996,
private identities and selected native command remain unchanged.

An additional candidate-path preflight failed because the unrooted --no-link
build output no longer existed. Journal evidence proves the pressure GC deleted
mipb66x7 at10:25:25CEST (08:25:25UTC), before the host switch, freeing2.6GiB.
The parent incorrectly continued to the next sequential tool call after that
assertion failure; the stable workspace-host switch was launched with the exact
locked source and now rebuilds the same candidate. No unsafe selection was
forced: that command owns guarded native/contract admission, and the earlier
inspection proved the identical derivation and native command. Repeated live
checks still show the same native process/private files. Future independent
build handoffs must retain an explicit temporary GC root and dependent tool
calls must stop on failed prerequisites. See the reusable notes below.

Profile operation log is /tmp/provider-cancel-profile-switch.log; its independent
exit file is /tmp/provider-cancel-profile-switch.exit. Fresh Luna/low observer
provider_cancel_rollout_watch owns only observation of this rollout batch.
The parent owns mutation, diagnosis and acceptance. No provider request is made.

A read-only dev-session URL lookup launched during the package build waited on
the transition lock. The parent terminated only that exact owned lookup
(PID1368932, exit 143); the profile build/native/portal were untouched. Repeat
the stable URL command after package selection from the selected generation.

## Cancellation follow-up executed and verified

Profile selection passed (exit 0) at generation 117, retaining native 0.160.0
PID 2615996. Protocol compatibility and semantic observation checks pass.
Application is /nix/store/mipb66x7d3w03rv94yialwzc08f819k9-dev-workspace-0.2.0;
selected system is l51k28cg at2026-10-13--10-22-17. Portal, router and provider
worker are active. No package transition remains pending. Rebuilt output was
rooted temporarily during guard checks; the selected profile now retains it,
so the owned /tmp/provider-cancel-candidate-root link was removed.

Read-only acceptance passed: subscription preview has one window, Snajpa
metrics/two windows are available, active provider remains codex-lb and public
catalog fields are limited to id/label/kind. Served HTML/assets match reviewed
app.js v37/provider module v2. The actual served module renders empty status
for the retained historical cancellation. Focused synthetic DOM tests prove
local confirmation, close/select clearing, polling and delayed-response behavior;
no real-browser visual check was performed. Private file identities and both
backups match; guests 3495839/3497034 remain alive. No new provider request was
submitted and no receipt erased. The stable URL was re-read after selection.

Current workspace final branch is 06a0a8a5 on 306548c3 after another unrelated
coordination-only master checkpoint. This post-deployment rebase is patch-
equivalent to source 33c0834d used for activation, and evaluates to the exact
same v3jkb98a derivation/output. Final contract/comparison pass; one pin remains.
All four published feature heads are ready, awaiting separate merge approval.

## Default integration after rollout

The user directed merge and excluded CI waiting. All four exact reviewed
feature heads were fast-forwarded into remote master and verified: client
5f15b929, runtime7c07b540, configurationbfb1d89c and workspace06a0a8a5.
Their full identities and pre-integration bases are in state.md. Deployment
remains generation117/mipb66x7 and hostl51k28cg; integration made no runtime
mutation. Feature refs/session/worktrees are retained. No additional CI wait
or archive was performed. The initiative is complete.
