# Network availability and IPv4 counter implementation

## Accepted finish plan (2026-10-08)

The user explicitly requested implementation of the revised finish plan.
[finish-session-plan.md](finish-session-plan.md) supersedes the nested runtime
acceptance route and the earlier acceptance of generic HTTP500 policy feedback.
Source tests/CI stay hosted. Local execution is limited to required runnable
package/guest preparation and the specifically selected direct-runtime/capture
acceptance, after committed independent review. Architect0 owns the design
append, implementer0 application edits, and the lead Git/pins/issue prose and
artifact acceptance. The preview remains running. No default integration,
installed activation, production KB writes or session lifecycle is included.

The OPTIONS timeout is a separately requested issue, not a W product change.
K will use one combined runtime/capture source lineage with the final V pin,
followed by the two approved PNGs and their validated provenance. Original
refs remain preserved; no unsupported new fixture is carried into old tooling.

## Accepted interface and network-counter refinement (2026-10-08)

User selected the grouped PHP network table and Available now counter semantics,
then explicitly requested the same number improvements in React and implementation.
Add admin-only Network available_to_users (registered, unowned, unassigned,
unreserved rows; zero if disabled) and owned_unassigned (owned, no interface,
including reserved/disabled rows). Count allocation units, not host expansion;
particular VPS use remains subject to location, purpose and quota. Existing
fields and public IPv4 counter remain unchanged; no migration or allocator edit.

PHP uses Network/Properties/IP usage/Actions columns with vertically labelled
information and counter tooltips. Remove routed-list Enabled column; disabled
rows use existing grey shading with a network-address tooltip, retaining details
and existing service actions. React retains network-list layout, replaces its
ambiguous Used/Assigned/Owned/Free statistics with Registered/Assigned/
Owned not assigned/Available to users, and shows only Network disabled in the
admin IP-list Flags group. Missing new fields display unknown, never old Free.

Architect0 owns the bounded design append; implementer0 owns V/W source and
regressions; root owns final bilingual copy, normal-hook commits/publication,
records and review. Preserve existing feature worktrees and current running
manual UI cluster until explicit supported refresh. No local CI/test suites;
use exact-head hosted evidence, independent committed review and manual UI
acceptance. Keep all default integration and production operations separate.

KB still selects only the two CS/EN networking/ip-address-list PNGs. Final
regeneration should show grey rows rather than the removed column. Canonical
configuration/KB pin reconciliation is dependent on final V/W publication, not
intermediate source drafts. Existing K runtime, D and E tooling remain untouched.


## Accepted portable KB tooling implementation (2026-10-07)

The user requested implementation of the standalone KB launcher plan after
confirming that vpsfree-kb-contracts must also work outside this workspace.
Keep one Linux/Nix repository-owned launcher and capture engine. Harden its
state identity, serialization, resource isolation, owned shutdown and recovery;
introduce explicit versioned connection descriptors and capture leases with
running-source verification before fixture writes. Ordinary --cluster use must
work without dev-session, workspace packages or an external checkout layout.

The optional workspace adapter belongs to vpsfree-dev-workspace. It delegates
to the same pinned KB engine and adds managed session/generation/provider
checks. Adapter source development is included; package activation or switching
is a distinct operation. Legacy capture state is recreated, never automatically
adopted or deleted. Keep existing network V/W/C/K feature heads unchanged while
developing the launcher in a separate same-session KB worktree and the adapter
in its own extension worktree. No PR management, default integration, production
KB writes or network retirement is included.

Architect0 owns the detailed design in design.md, implementer0 owns source and
tests, and the lead owns coordination, final prose and acceptance. Project
documentation owns the portable state/connection/recovery contract; the
extension links that contract and documents only managed integration. Quick
checks and normal-hook commits precede independent final whole-branch review;
isolated runtime and bilingual capture verification follow that gate through a
fresh watcher. Preserve exact source attribution and existing successful network
feature verification instead of rerunning unchanged tests.

Implementation inspection found that the selected generic dev-workspace public
provider dispatcher buffers output and supplies stdin EOF. The adapter's
full-lifetime capture handshake therefore needs one generic source correction:
stream only the `capture-lease` provider command under the existing generation
guard. Preserve other commands, catalog selection, inherited-authority stripping
and exit behavior. A dedicated generic feature worktree and exact extension
input pin join the source scope; no package activation is included. Architect0
owns the bounded transport/test clarification before those edits.

## Goal and authorization

Implement the final plan accepted in this conversation. The user requested
implementation on 2026-10-06, selected both configuration channels, and explicitly
confirmed that Network.role is sufficient for public/private classification.
No RFC1918/CIDR classification or filtering is part of this feature.

## Affected repositories

- vpsadmin: enabled state, allocation policy, counter, legacy UI, docs and tests.
- vpsadmin-webui: state/control and address selectors, translations and docs.
- vpsfree-cz-configuration: exact reviewed source pins for vpsadmin and
  vpsadmin-webui channels, deployment/recovery preparation.
- vpsfree-kb-contracts: required external documentation impact verification;
  revise only evidence required by the actual UI impact.

## Design and ownership

Architect0 reconciles [design.md](design.md) before substantive implementation.
Implementer0 owns source/configuration edits; lead owns coordination, review,
verification and final user-facing English/Czech copy. Reviewer0 remains
independent and receives final committed deliverables after quick checks.
Existing default-true inventory remains visible. Disabled pools prohibit new
use, including explicit IDs and owned detached reuse, while preserving existing
service, trusted assigned-address continuity, release and rollback. Counter is
unowned/unassigned/unreserved rows from enabled public_access IPv4 pools only.
Do not infer pool retirement from purpose, location or maintenance flags.

## Compatibility and deployment

Additive NOT NULL/default-true migration; omitted updates preserve state.
Expose admin-only write and readable status, with optional list filtering.
All writers must enforce policy before first disable; already admitted chains
may complete. Preserve existing routes and ownership; no coordinated node
upgrade is needed. Old API rollback ignores disabled state and is unsafe while
retired pools remain disabled. No production activation, database mutation,
network retirement, default-branch integration, or lifecycle action is included.

## Configuration and verification

Use confctl within the configuration dev shell to pin final published feature
SHAs through channels vpsadmin/role vpsadmin and vpsadmin-webui/role
vpsadmin-webui. Preserve generated commits and inspect lock changes.
Run relevant quick checks and hooks, then commit all source/UI/config/docs.
Inventory full branch history, final diffs and migration deployment provenance;
final independent review precedes long integration tests and affected-host builds.
Fresh verification watchers own long/uncertain runs. Correct substantive review
findings and run focused verification under the narrow-fix policy.

## Documentation

Keep lasting enabled/admission/continuity semantics and upgrade guidance with
vpsadmin, UI design/work log with vpsadmin-webui, rollout evidence in session
records, and required KB impact evidence under the external contract workflow.
Production KB writes require approval of exact staged changes. Preserve unrelated
shared workspace work and keep the session open after handoff.

## Independent dependency prerequisite found during CI

Current W CI fails its BFF production dependency audit before the required
quick/unit gates. Both the original 02ac0c7 base and final e4c49bcd lock
proxy-addr 2.0.7; network work changed neither package manifest nor lockfile.
Upstream GHSA-jqcg-44mw-7w3h identifies 2.0.8 as patched. Prepare this one
transitive dependency update in a separate W worktree/branch and review PR,
without bundling it into the network feature or changing the currently tested
W/C heads. Verify production audit and owning BFF/package checks. It is a
separate prerequisite for green CI/integration; no default merge or deployment
is authorized. All network runtime work continues at its recorded heads.

## User-requested workflow correction (2026-10-06)

Update workspace AGENTS.md and the Git procedure to make development branches
the ordinary deliverable, without creating or managing pull requests unless
the user explicitly asks or that repository's own instructions require them.
The vpsadmin-webui PR requirement remains local to vpsadmin-webui. Preserve
fast-forward-only default integration, explicit integration authorization,
independent source review, hooks and verification. Do not use GitHub merge
commits to integrate workspace projects. No change to existing application
branches, PR state, pins, package selection or deployments is part of this edit.

This bounded instructions-only change uses the registered workspace feature
worktree at the current shared master base 9b37d3900045f965ebc6581cec6c114d0064e696.
Implementer0 owns the edit; lead owns final wording and scope; reviewer0 performs
the independent final general-lane review after commit and existing quick
instruction checks. No migration or long build is needed.

## Accepted user-list visibility follow-up

User requested implementation after selecting “Keep owned IPs visible”.
Network Index for non-admins lists enabled networks only. IP Index applies
existing access permissions, then keeps enabled-network addresses, the caller's
owned addresses and currently assigned addresses they may access. Disabled free
inventory is hidden before count/pagination. Explicit filters cannot widen this
visibility. Admin inventory remains unchanged. Show and association permissions
remain independent of enumeration; assigned hosts/export endpoints and history
retain current access. No model-wide default scope, migration, new field, numeric
classification or allocation/counter change. Both UIs must retain owned/assigned
disabled addresses and included network details without client-side removal.

Architect0 reconciles the owning brief; implementer0 owns source/tests/docs and
prepared pin helpers. Lead owns final prose, review, checks and publication.
Refresh the vpsadmin configuration role and KB V revision to final source; W pin
changes only if W actually changes. Keep application/configuration/KB/dependency
changes in existing feature branches; do not create/manage PRs outside W, merge,
deploy, retire production networks or mutate lifecycle/package state.


## Follow-up after the accepted finish plan (user request, 2026-10-08)

Complete the HTTP action feedback, practical direct runtime campaign and two
selected legacy KB images first. Then investigate the shared OPTIONS discovery
timeout reported as vpsadmin-webui issue30, and implement a bounded correction
if warranted by the current contract and evidence. Use the retained architect
and implementer for new substantive W work, hosted exact-head verification,
and independent affected review. Preserve the current Wce review boundary until
that sequential follow-up starts. The user will review results in the morning;
this does not authorize default integration, production KB writes or local CI.


## Accepted continuation (2026-10-09)

Implement the approved final plan in order: exact K027/Eeea source gate; monitored ordinary-host public runtime proof; two genuine CS/EN networking/ip-address-list captures and strict export/visual/media/E acceptance; then separate W issue30 fix on current main and required hosted/independent review. Final canonical C selection follows accepted W. Finish with verified handoff, retain active session and branches, no further merge/deploy/activation/production KB or cleanup. Preserve incomplete G4/G6, their future sparse growth allowance and the running preview.


### Accepted finite runtime baseline after K68 isolation3 failure (2026-10-09)

Root accepts the architect proposal at design.md:4446. Use genuine published
7dc4d70830e535f4559bccfa668cf65cdce1de2d for one finite K-runtime-only upgrade
experiment. This preserves actual artifact/import/closure, disk, six-credential,
accounts and live-source assertions while dropping the unsupported K68 and
vpsAdmin-version-upgrade claim. No failed attempt is replayed or adopted.
The predecessor's single SSH scan can fail; a native failure ends the experiment.
The durable ordinary service and final-controller authenticated shutdown remain
required. Exact new K/E hosted checks and committed affected review precede
package construction and another real phase.

To avoid retaining another live pair, root separately accepts final G027 public
stop then proven reset of only failed isolation3 A/B, after bounded private
evidence retention and fresh named tuple/unit proof. A refusal halts that
sequence. No unit stop, manual unlink, force, process/group signal or cleanup of
G4/G6/preview is included. See finish-direct-runtime-baseline-source-acceptance1.json.


### Independent issue30 work during the runtime shutdown hold (2026-10-09)

The failed public A shutdown now blocks the next portable campaign. Root starts
the separately authorized React suggestion-timeout unit while architect0
resolves that operational boundary. This supersedes only the prior scheduling
requirement that runtime/media finish first. The issue30 technical brief and all
runtime/media acceptance gates remain intact; W cannot certify missing real
K/guest or PNG proof. The new registered dev/ip-suggestions-timeout worktree
starts from freshly fetched main7152729dcde326e00d16b5af0a46d0f60b431dbb,
with no overlapping open PR. Preserve merged availability history.

## Prospective shutdown and readiness refinement (2026-10-09)

The recorded isolation3 retirement failure established that a guest stop job
can outlast the runner's machine wait. Preserve the current incomplete runs;
future source cannot recover an ownerless receipt. Root accepted architect0's
bounded sections at design.md4710 and4866 for prospective implementation.
The same runner, tracker, listener and reapers retain ownership through slow
graceful shutdown, with one stop per started machine and no timeout-driven
kill/restart. One K readiness predicate governs status/connection/capture and
its selected E consumer. Caller and machine budgets remain distinct.

The genuine published7dc runtime experiment is conditional on two public-SSH
console-router-only drains after complete old readiness/source proof. Each
checks guest identity/closure and clean inactive service state under finite
guest/caller budgets. Its claim records that preparation, unchanged V and the
finite failure/no-replay limit. Final-code ordinary shutdown is verified without
the historical preparation. The selector-only packet stays preserved.

Implementer0 completes the independent W issue30 source unit first, then the
accepted K/E source owners. Root owns prose, functional commit splits, exact
K/E selectors and hosted gates. Committed affected independent review, immutable
packages and a new measured retained-resource admission precede any real phase.
No additional pair, old-run recovery, reset, activation, default integration or
production KB publication is granted by this refinement.

## Published shutdown boundary and issue30 checkpoint (2026-10-09)

Issue30 source, hosted CI/smoke, independent whole-branch review and twelve
synthetic browser states are accepted at Wcce68142. PR39 remains unmerged and
requires explicit integration approval. K3bb675f1/E5a12cf39 publish the accepted
shutdown/readiness and finite7dc source boundary, preserving logical history and
source graphs. The new late-child tests expose a main-thread-only descendant
reader; architect0 owns its source diagnosis and bounded proposal. New K/E
review and all real operations remain held pending correction and exact checks.
Retained failed campaigns, preview and capacity/recovery constraints are unchanged.

### Hosted source gate after the task-discovery repair

Publish the corrected K feature heads and observe the existing Check source
workflow. The unchanged Managed page runtime workflow also starts on cluster
changes; its VM test phase is outside this source gate and must wait for the
committed affected review. Stop only those automatic Managed runs proved to
belong to the newly published session feature heads before they enter the VM
phase; retain their native cancellation evidence. This is a review-gate control
of these owned CI runs, not a source change, default integration, guest cleanup
or permission to cancel another branch's work. Later integration verification
requires an explicit selected run after the review. Exact-head source checks,
E composition checks and their results remain separate.

The corrected selected pair is K29b17bf4/E2ec02952. The complete committed
inventory and prepared four-lane packet are `finish-task-discovery-review1-*`.
After exact source evidence and affected review, use
`finish-direct-runtime-operation-brief6.md` for the prospective finite7dc
experiment. It supersedes older operation briefs that selected K68 or charged
only two retained tank sets. All four failed/current retained disk sets and
their remaining sparse growth are part of fresh admission; no retirement or
GC saving is assumed. The two owned Managed runs were cancelled before VMs;
that cancellation supplies no integration pass.


## Direct notification remediation checkpoint (2026-10-09)

The completed affected four-lane review of K29b/E2ec found one Important caller-loss
path. The accepted narrow correction ensures notification after the first valid
shutdown latch even when replying fails. Its actual-peer regression requires a
native broken write and later public stop of the same one-shot drain. Root's
focused inspection reconciled the frozen controls and protected paths; this is
a direct step9 remediation within the assessed shutdown contract.

K09229a735be3887e8078e4c00216f8b63613dcf5 and E63948d784b6f15b22e562fc982a50351d4c0fba6
are normally consolidated and published. K retains its three logical owners and
E retains its two; the verifier/provider patches and unrelated graphs remain
unchanged. A fresh Luna/low utility collects exact replacement source checks.
No passing remediation, package admission or real campaign is inferred from
publication. The [current inventory](finish-stop-ack-step9-inventory.json) keeps
the original completed review separate from this correction. All existing real
campaign and media/capacity constraints remain; the active session endpoint and
separate merge/publication approvals are unchanged.

### Exact waiter-barrier follow-up (2026-10-09)

The previous K notification batch passed on the runtime ref and in E, but the
original K ref failed in an unchanged test's operation-lock probe. The probe
could contend with public nonblocking stop; the native waiter outcome was not
retained, so the exact interleaving remains inferred. A one-path test correction
now waits after the real authenticated acknowledgement and preserves public
stop, handoff authority, all five-second guards and effects assertions. It is
folded into owning K922e71e5, selected by E2c1d3e86. Their exact source checks
are watcher-owned. This is direct review-remediation verification, with no new
public boundary. No package/guest work is admitted yet.

Exact source gate cleared at K922e71e5/E2c1d3e86 by completed hosted checks and
focused step9 remediation verification. Prepare immutable packages and fresh
measured admission next; retain all four failed allocations and their growth.
See finish-stop-waiter-step9-acceptance.json. No real phase is admitted yet.

Fresh admission update: package construction completed for exact K922e71e5,
with all source blobs matched. Guest execution is blocked by current disk
capacity:166.55GiB free versus171.99GiB before builder headroom or unknown
remaining closure costs. No alternative mounted disk-backed filesystem was
found. Keep all four incomplete allocations and possible sparse growth.
Continue only after additional capacity or an owned campaign filesystem is
established and fresh receipts/kernel/cache/concurrency/monitor facts qualify.
No cleanup savings or another finite guest attempt is inferred.

2026-10-10 user correction: reduce the verification footprint; use focused smoke
if further reduction is not feasible. Separate the historical runtime upgrade
experiment from KB capture acceptance. Assess one current-source instance and
existing supported smaller settings before any further guest work. Preserve
truthful distinctions between package/source tests, live smoke and reproducible
canonical images. Do not invent a new broad test framework or cleanup authority.

## Selected smoke disposition (2026-10-10)

Following the user's resource-cost objection, choose the already supported
installed CLI/read/negative smoke instead of launching the full historical
upgrade/isolation campaign or qualifying guessed smaller guests. Architect0's
[bounded separation](design.md#separate-screenshot-operation-and-proportionate-smoke-fallback-2026-10-10)
requires no source/API/schema/provider change. Exact G922 smoke is completed in
[the native receipt](finish-installed-smoke1.json): two help commands, noncreating
absent status, missing connection refusal and missing-connection capture refusal.
No new VM, guest config or published image/result was created.

Accepted hosted/source/package and W issue30 browser evidence is retained.
Historical upgrade/isolation/continuity remains explicitly deferred and unfinished.
Fresh canonical CS/EN PHP images, live API/PHP observations, strict media and final
configuration selection remain pending; package smoke does not satisfy them.
The previous 172 GiB refusal belongs to the full campaign and this host's retained
obligations. One existing capture profile has 40 GiB new eventual output, but this
is an optional separately admitted operation, not the chosen smoke or a minimum.
No further capacity or lifecycle operation follows automatically from this handoff.

The active session retains failed campaigns, preview, branches and worktrees.
Default integration, production KB writes, deployment, activation and cleanup
remain outside this disposition. See [current handoff](finish-smoke-handoff1.md).
