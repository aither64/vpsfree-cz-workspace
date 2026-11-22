Selected package: /nix/store/qxclq96999l3ccs39mj5vw0m5k8hwllx-dev-workspace-0.2.0
Coordination catalog: sha256:34d1db44dbd7b835bdb33bf0f8979691c753db0a90f78c22d9080cfbf07319cf (/nix/store/qxclq96999l3ccs39mj5vw0m5k8hwllx-dev-workspace-0.2.0/share/dev-workspace/coordination.json)
# Resource claims and session notifications

The coordinator serializes integration into shared branches and reserves configured
machine targets for deployment. Sessions develop independently in their own worktrees. Repository
claims are short merge locks; machine claims are deployment reservations. Sessions
run commands, verify effects and explicitly release ownership. Queued requests
notify their waiting session when granted.

## Acquire resources

Use a schema-1 request with a fresh lowercase UUID `requestId`:

```json
{
  "schema": 1,
  "requestId": "11111111-1111-4111-8111-111111111111",
  "label": "Merge approved feature into master",
  "repositories": ["project"],
  "machines": []
}
```

Repositories must be registered to the session. Their canonical clones live in
`repos/<project>.git`; the reserved `workspace` registration uses the workspace
Git root. The coordinator validates the real common Git directory and canonical
SSH origin. A registration's optional `github` identity and any configured catalog
remote must agree with that origin. Repository names must be unambiguous.
Registering a repository does not require a catalog update or package rebuild.
Schema-1 machine names, IDs and aliases remain available for retained
operations through the compatibility catalog. New machine requests use schema 2
below. Supply at least one resource. The complete request fits 16 KiB; labels fit
512 bytes. Keep credentials out of labels and requests.

```sh
dev-session coordination acquire SESSION --as-is --request claim.json --json
dev-session coordination claim-status SESSION --as-is --id CLAIM_UUID --json
```

The command returns immediately with `held` or `waiting`. Run the shared mutation
only while the exact claim is `held`. Requests acquire all resources together;
a waiting request owns none of them. Earlier eligible conflicting requests have priority,
while disjoint resources can be used concurrently. A request blocked by held
resources cannot prevent their holder from acquiring other free resources. A queued grant sends a native
notification to the session's retained conversation. Read authoritative status
before acting on a notice. A notice supplies no merge or deployment approval.
Threadless sessions can use the local CLI but have no notification destination.

Aliases sharing a common Git directory and separate clones sharing a canonical
remote contend for the same repository. An explicit registered `default_branch`,
including `main`, remains authoritative; catalog defaults do not replace it.
Claims select resources, carry no target branch and grant no merge approval.
Queued requests retain their original resource keys and refuse changed mappings.

An exact request-ID retry returns its existing claim, including after release
or removal of the clone. Changed input or another owner refuses. Use a fresh ID for intentional new
ownership. A second claim does not implicitly reuse resources held by the same
owner. Request the complete set initially or use separate disjoint claims.

## Configured machine identity

A schema-2 machine request selects an exact machine from a registered configuration
repository and names an installed protocol-1 adapter:

```json
{
  "schema": 2,
  "requestId": "22222222-2222-4222-8222-222222222222",
  "label": "Deploy configured target",
  "repositories": [],
  "machines": [{
    "repository": "configuration",
    "selector": "region/machines/development",
    "adapter": "confctl"
  }]
}
```

Use the same `acquire`, `claim-status`, `cancel-claim` and `release` commands.
Machine acquisition alone does not reserve the configuration repository for a
merge. Ordinary new machines need no catalog entry or package rebuild.

The runtime reads machine metadata at the registered feature branch's exact
committed revision.
It supplies the canonical local repository path to the adapter; the request
cannot supply a path, revision or shared-label override. The resolver uses local
locked inputs without builds, remote fetching, lockfile writes or target probes.
A missing branch, flake or prepared input prevents admission. The runtime never
falls back to the default branch.

By default, identity is the canonical registered SSH repository origin and exact
configured machine name. Clones, registration aliases, workspaces and branches
therefore contend for the same target. Different repositories can each contain
`vps` without contending for the same lock. If configuration supplies
`metaConfig.labels.dev-workspace.lock-id`, its nonempty string value selects a
shared identity instead. Configure the same stable label wherever intentional
cross-repository overlap needs one lock. Names and labels must be nonempty,
case-sensitive UTF-8 strings of at most 256 bytes, without control characters or
surrounding whitespace. An explicit null or malformed label prevents resolution.

The visible identifier is
`machine:github.com/example/configuration:region/machines/development`.
Shared labels display as `machine:shared:LABEL`. Reserved delimiters and other
UTF-8 bytes are percent-encoded. Display text is not a claim input. Internal keys
hash the canonical structured identity; routing, hostnames, SSH addresses,
commits and local Git paths do not enter that identity. The coordinator does not
discover physical overlap between different logical identities.

New claims and waiting grants check each source pair, its canonical origin and
exact configured selector, against all held and waiting bindings and accepted
legacy aliases. The adapter ID must match, and the resources must be equivalent
under the package policy. A changed label or adapter cannot bypass an existing
hold or waiter by producing another key. Accepted legacy aliases retain this
requirement even without an active old claim. Terminal records retain no ownership.
A waiting request keeps its original structured binding; a newer commit with the
same mapping may be granted, while its initial source revision remains audit
evidence. An approved compatibility bridge makes namespaces contend without
transferring or rebinding a held claim.

Before an intended committed deployment batch, check its exact held typed binding
once:

```sh
dev-session coordination verify-machine SESSION --as-is --id CLAIM_UUID \
  --repository configuration \
  --selector region/machines/development --json
```

This read-only local check returns the claim ID, canonical resource, identifier
and current source revision. It grants no ownership, changes no record and
performs no deployment. Build, artifact, live-state and interruption checks still
follow the ordinary deployment procedure. Run them under the original claim and
release requirements.

## Execute and release

Independent feature work needs no repository claim. This includes edits, commits,
rebases, dependency updates, feature-branch pushes, hook preparation, builds,
tests, review and waiting for approval. A merge waiter can continue such work in
its own worktree. Git retains its ordinary file and ref locks.

Prepare the reviewed feature, clean target checkout, environment and hook trust
before requesting a merge lock. Obtain integration approval first. Acquire only
the repository being integrated, immediately before these steps:

1. Recheck the exact feature head, clean target checkout and current remote target.
2. Perform the approved fast-forward merge and required hooks.
3. Push normally and prove the resulting remote ref.
4. Release immediately, before CI monitoring, record updates, handoff or
   disposable checkout cleanup.

If the target moved, release and reconcile outside the claim. If a hook fails or
needs intervention, stop commands and inspect effects before release, then repair
and verify outside ownership. Git can exit zero after a failing post-merge hook;
inspect hook results before pushing. A rejected push or interrupted command needs
an actual ref check. Retain ownership for an uncertain shared mutation only while
actively reconciling its effects. Do not wait for operator input with a known-safe
repository held. Never hold merge locks during development, tests or review, and
do not reserve several repositories for a sequential integration batch.

Linked worktrees share Git configuration. Repository tools own configuration and
plugin trust; the coordinator never signs, changes trust or runs commands. A trust
mismatch returns to preparation and does not justify a development-wide claim.
Required hooks and signature checks remain enabled.

Machine reservations are separate: build and copy artifacts before ownership when
supported, then acquire only the physical machine near activation. Keep its
reservation until deployment verification and integration are complete under the
release rule below. Do not bundle repository claims into a deployment
reservation.

This is cooperative locking. Tools do not intercept arbitrary commands. The claim
certifies exclusive integration or deployment ownership, not command success.
Shared tracking writes use their short `dev-session-tracking.lock`; they do not
need a durable repository claim for independent session bookkeeping. Integration
from that same shared checkout takes the repository claim first, then tries the
tracking lock without waiting. If it is busy, release the claim and retry after
the writer finishes. Hold both only across the final target check, merge/hooks,
push and remote proof. Preserve unrelated dirty paths and index entries in the
shared checkout; disposable targets must be clean.

```sh
dev-session coordination release SESSION --as-is --id CLAIM_UUID --json
dev-session coordination cancel-claim SESSION --as-is --id CLAIM_UUID --json
```

Release settles a held claim. Cancellation settles a waiting request. Both are
owner-only and idempotent; cancellation cannot release held resources. Machine
ownership follows the deployment and integration rule below. Release grants no
merge approval. Session completion still follows its normal exact-head
integration requirements.

For workspace profile activation, hold a claim covering the package policy's
exact profile machine identity and run ordinary `workspace-host switch --source PATH` with
`DEV_WORKSPACE_CLAIM_ID=CLAIM_UUID` and the exact `DEV_SESSION_SLUG` and
`DEV_SESSION_WORKSPACE` identity. Workspace-host checks ownership under its
transition locks. Package compatibility, activation journals and forward recovery
remain workspace-host responsibilities.

## Machine retention

Promptly release each deployed physical machine once both conditions are met:

1. Deployment and its effects have been verified, with no unfinished or uncertain
   command effects.
2. Its complete deployed feature lineage is integrated into the approved remote
   default branches, including deployed dependencies.

The owning agent runs the normal release command without waiting for separate
UI acceptance or release direction. No background worker or timer is involved.
Failed or uncertain deployment and missing integration evidence keep the machine
held. Idle time and turn completion do not establish either condition.
Default-branch integration still needs separate explicit approval. A later
deployment requires fresh machine ownership.

Use existing rollout and review receipts for exact system/profile store paths,
complete source/input graphs, canonical repository/target mapping and machine
aliases, exact deployed and final intended feature heads, and fresh remote
ancestry evidence. Retain reviewed old/new base/head ranges, range-diff or
patch-equivalence evidence and migration lineage when history changes. Do not
describe a nonancestor deployed commit as literally merged. An independently
proven equivalent successor can establish integrated feature lineage; a
substantive successor requires a new verified deployment. Ordinary session
completion still requires every registered exact final feature head.

Before release, inspect authoritative status for the exact claim owned by this
session, reconcile unfinished or uncertain command effects, verify deployment
and integrated lineage, release that claim and verify its resulting state. The
cooperative owner-only, idempotent release API does not enforce these
prerequisites. Do not introduce release receipts or edit claim records to bypass
a missing condition. Keep short repository merge claims separate from machine
ownership. Release does not archive, delete, stop or clean a session; each
lifecycle action retains its separate authorization boundary.

## Interruption and lifecycle

Claims survive idle agents, disconnections and service restart. They have no
automatic expiry. The coordinator does not observe command execution or infer
completion. After interruption, inspect the original local and remote work,
stop anything still mutating the resources and reconcile effects. Release a
repository merge claim once its critical section is safe. A deployed machine
remains held until all machine-retention conditions are met. SSH or a client
process exiting does not permit release.

Held claims block lifecycle cleanup until their owner releases them. Lifecycle
fencing cancels waiting requests. Suspension retains ownership and waiting
requests, with no new grants while suspended. Status reads do not grant resources
or run recovery. The Operations page shows up to 128 claims, with up to eight repository and machine
names per claim; the CLI retains complete records. Machine
claims also appear in the session's Reservations tab.

The scheduler inventories validated ledger, claim and integration records once
per workspace pass after reconciling uncertain attempts. It verifies a session
only when that owner has claim work, a nonterminal job, an eligible background
continuation, a due notification or a due handoff reminder. Completed runs remain
eligible for reminders and notification delivery. Candidate records select work;
current generation, session incarnation, fences and action-time state still
govern every action under the existing admission locks. State changes wake the
scheduler; the five-second fallback covers lost wake signals.

## Storage and compatibility

The coordinator strictly reads bounded private `claims.json` envelopes in schemas
1 and 2 alongside the original ledger. The first typed request atomically writes envelope 2 while
preserving existing schema-1 rows. Typed rows freeze the resolved source binding
and identity. Exact request-ID replay returns that saved result before source
resolution, including after release or removal of its clone.
The existing admission mutex protects both old and new resource ownership.
Admission reserves a queued claim's future notification capacity in the ledger.
Notifications use the existing durable outbox; failed delivery retries without
changing or releasing claims. A released claim stays released even if an older
notification arrives later.

Packages advertise `share/dev-workspace/claim-contract.json`. Once claim records
exist, selecting a package without that capability refuses. Compatible selection
preserves live repository/machine mappings. The separate
`share/dev-workspace/repository-claim-contract.json` advertises support for
registered repositories outside the catalog. Every held or waiting repository
claim must retain its registered identity and common Git directory. A candidate
without that capability needs an explicit matching catalog entry for each active
repository; otherwise selection refuses. Released and canceled history does not
require the new capability. Retained machine mappings keep their existing catalog checks.

The separate `share/dev-workspace/machine-claim-contract.json` declares both claim
record schemas, identity version 1 and resolver protocol 1. Every schema-2 store
requires this reader capability, including released or canceled history. Reading
does not rewrite records. Never erase terminal rows or downgrade the envelope to
select a predecessor; recover forward with a compatible package.

`lib.mkPackage` accepts optional `machineIdentityConfig`. Its immutable
`share/dev-workspace/machine-identity-policy.json` contains schema 1,
`profileTarget` (one structured identity or null), and finite `legacyAliases`
entries of `{resource,identity}`. For an unchanged legacy configuration, packaging
derives the default policy from its catalog remotes and exact selectors, using
the runtime's identity derivation. The policy bridges known old keys;
it is not an inventory for new machines. Current and candidate profile identities
must remain equivalent, and a typed profile claim must match the configured
identity and current committed metadata. Initial upgrade uses the original
schema-1 profile-machine claim and its explicit bridge. Retained legacy catalog
and capability descriptors remain unchanged so predecessor hosts can admit that
first candidate. Typed requests start after selection.

Conflict and fairness comparisons normalize approved bridges across old/new
claims, legacy jobs and reservations without rewriting their keys or artifacts.
Candidate selection refuses a missing bridge or conflicting ownership and
preserves the original records. A bridge does not waive an adapter-ID change.
To preserve ownership across a deliberate origin, name or label change, retain a
stable shared label or configure an explicit reviewed compatibility bridge before
use. Recover with a compatible forward package; never delete records to bypass
compatibility checks.

New work uses `acquire`. Existing snapshots, jobs, integration journals,
reservations and uncertain effects retain their formats, recovery payloads and
original release requirements. Legacy jobs and reservations exclude conflicting
claims, including the same owner's legacy reservation. Retained preparation,
mechanical refresh and tracking publication acquire repository ownership around
their mutations. Collection preserves payloads in a claimed common Git directory. New claims cannot release
legacy reservations. A retained job may refresh its prepared snapshot by supplying
its exact `legacyJobId`; this does not permit submitting an independent new job.
Use the [retained workflow guide](coordination-legacy.md),
[integration guide](integration.md) and [operations guide](coordination-operations.md)
for those records.

Legacy automatic reservation release during lifecycle completion is implementation
behavior, not permission to archive, delete or release a deployed machine before
the retention conditions above. Existing journals and recovery contracts remain;
finishing work or preparing a handoff grants no lifecycle authorization.
# Coordination operations and recovery

For resource ownership, use the [claim guide](coordination.md) to acquire,
inspect, release or cancel a request. Claims survive disconnection and remain
held until released through the normal command. After interruption, reconcile
remaining local and remote effects. Release a repository claim after its safe merge critical
section. Promptly release each deployed physical machine once deployment and its
effects are verified and its complete deployed feature lineage is integrated,
as described in the [machine retention rule](coordination.md#machine-retention).
Do not wait for separate UI acceptance or release direction.
Existing snapshot-based operations keep the procedures below and the
[retained workflow guide](coordination-legacy.md).

The remaining sections describe legacy executor recovery. They do not start new
automatic workflows under a runtime with resource claims.

Read [the coordination contract](coordination.md) before operating its ledger.
The selected package installs both guides. Run `workspace-host coordination guide`
to read them from any checkout, including an unmerged deploy-first rollout.
Status reads do not reconcile, schedule or mutate anything. Use session commands
for exact owned operations; keep all recovery evidence and roots.

## Repository identity refusals

If acquisition refuses a repository identity, check the current session's
registration, `repos/<project>.git` and its single canonical SSH origin. Duplicate
names, unsafe projects and disagreement between `github`, origin or a configured
catalog remote require correction before a new request. Preserve an explicit
`main` default branch. Do not add a catalog entry merely to enable a normally
registered repository.

A queued mapping-change refusal leaves its original request waiting. Cancel it
and acquire a fresh request after reconciling the registration and clone. An
exact retry of a released request returns that receipt even if the clone was
removed. Package-compatibility refusals retain ownership: select a compatible
forward package instead of deleting claim records.

## Machine identity refusals

For a typed request, check its registered repository, exact feature branch,
canonical SSH origin, selector and installed adapter. Prepare missing local locked
inputs separately. Resolution does not fetch, build, inspect the machine or change
a lockfile. A new commit may keep the same machine identity; run `verify-machine`
once for the intended committed deployment batch.

A mapping or adapter change for an active source pair, or a changed queued binding,
leaves original ownership intact. Reconcile the configuration and retained work before canceling a
waiting request or acquiring a new one. Releasing a held claim still requires the
ordinary effect, verification and integration conditions. A compatibility bridge
restores conflict comparison; it cannot rebind a hold or authorize a different
source mapping. Preserve all records when a candidate reports bridge loss or a
collision, then select a corrected compatible package.

Schema-2 terminal claim history still requires the typed-reader capability.
Do not remove history or downgrade `claims.json` to pass selection. Existing
legacy reservations, exact attempts, immutable snapshots and forward recovery
remain authoritative. The machine policy and catalog are package configuration;
ordinary new machines do not need additions to either compatibility table.

## Agent waiting

If a claim remains `waiting` after the holder releases its resources, inspect
`workspace-host coordination status --json` for other holders and earlier
waiters. If neither explains the wait, check the user service log:

```sh
journalctl --user -u workspace-coordinator.service --since '10 minutes ago'
```

The coordinator logs source-resolution and admission refusals with the owning
session's slug. A waiting claim owns no resources; its status alone does not
distinguish contention from a refusal. Fix the reported source or mapping error
before retrying. Packed Git refs are scanned with bounded memory and have no
aggregate file-size limit. Preserve retained refs and claim records during
recovery.

Prepare and verify work independently. Request a machine only near the first
prepared deployment. Submit approved work, then continue other useful work.
Use the integration driver's `--background` mode when combining approved merges
and deployments. Background handoff verifies the caller's managed Codex identity and runs a cheap
Git preflight. Record the returned run ID and distinguish preparation from
submitted merge jobs. End the turn when no independent
work remains and the recipient is verified. The worker continues and sends a native message for action or
review. Read status when that message arrives and acknowledge its exact handoff event
and generation before handling the action. Renew the five-minute acknowledgement
while work continues. A delivered native message alone does not establish pickup.
For an external conversation, use `integration-resume --foreground` under an
attached observer, or explicitly select `--background --to-session-lead` to hand
responsibility to the retained managed lead. Individual submitted jobs also
run independently and retain their existing state notifications.

Do not keep a turn open to poll reservations or ask the user to restart it when
another session owns a resource. Pause/resume and generation recovery are described
in [background continuation](integration.md#background-continuation). A busy
resource never authorizes a deployment around its reservation.

On `needs_refresh`, refresh the branch or input baseline, resolve conflicts,
repeat the required verification and review, record any preserved approval proof,
and prepare a new snapshot. The coordinator does not decide conflict semantics.
Use a new request ID and current revision to refresh the unclaimed job.

## Interrupted execution

Read `dev-session coordination status` and identify the exact attempt. The
private attempt directory retains `request.json`, `phase.json`, `result.json` and
`worker.lock`; logs are diagnostic only. The systemd unit is
`workspace-operation-ATTEMPT.service`. A running worker refuses manual
reconciliation. A retained exited unit is distinct from a running process.

Run `reconcile` on the original job. Git recovery proves exact remote ancestry.
The coordinator launches safe reconciliation in independent
`workspace-reconcile-ATTEMPT.service` units after a worker exits. Network probes
and forward recovery never run in the scheduler. A stalled probe retains its
original claim; other resources and notification delivery can continue. Failed
probes wait at least 30 seconds before another attempt. State
changes wake it immediately; a five-second tick covers missed wake signals.
Unprovable effects stay blocked and require operator evidence.
A local fast-forward with a failed push stays in place and holds its claim until
the remote effect is resolved. Profile recovery can complete only the original
selected candidate and saved preparation. Machine recovery requires the adapter's
verified receipt and both live-system/profile identities. Ambiguous rollback or
partial publication keeps the reservation and claim. Do not replay activation or
use a fresh job to hide the original uncertainty.

Archive and deletion hold notifications and cancel queued operations before
cleanup. Coordination receipts bind each ordinary lifecycle journal to exact
owner incarnations. Legacy archive completion releases that owner's machine
reservations in the same ledger transaction that records lifecycle completion.
This implementation behavior grants no permission to archive or bypass the
machine retention rule. Verify deployment and its effects and the complete
integrated deployed lineage before releasing its exact session-owned claim.
Release does not authorize archiving, deleting, stopping or cleaning a session.
The reservation stays held during failed or interrupted cleanup. Retrying a
completed archive receipt can release a hold retained by a predecessor executor;
the exact owner binding must still match. Deployment history and recovery
artifacts remain available after release.

Revival freezes its archive association before tracking changes. It reconnects
the same owner without reacquiring reservations or resuming canceled jobs. A
recreated slug has no claim to the previous owner's resources. Running or
uncertain deployments require their original recovery before archival. Deletion
retains its existing deployed-ownership hold. Exceptional transfers remain
separate recovery operations; there is no force-release command.

## First reporting-startup upgrade

A predecessor whose host accepts only `agents.*` launch overrides cannot decode
the reporting startup plan. The reviewed candidate's narrowly scoped
`coordination candidate-prepare` and `candidate-reconcile` entries keep the
selected generation's ledger authority, actual managed owner, held machine
reservation and original attempt. They do not create bootstrap owners or grant
approval. Follow [team reporting upgrade and recovery](team-reporting-upgrade.md)
for exact source/profile-token proofs, ordinary submission and exited-attempt
recovery. Normal selected-generation reconciliation applies after selection.

## Reviewed rebase lineage

For each deployed nonancestor head, `finish.replacements` contains:

```json
{
  "repository": "example", "target": "refs/heads/master",
  "from": "DEPLOYED_SHA", "fromBase": "OLD_BASE_SHA",
  "to": "FINAL_SHA", "toBase": "NEW_BASE_SHA",
  "relation": "patch_equivalent", "approvalId": "UUID",
  "evidence": {"kind": "review", "path": "work/SESSION/lineage.json", "sha256": "HEX"}
}
```

The session review receipt binds `schema: 1`, `ownerId`, `reservationId`, this exact
tuple in `mapping`, `decision: "accepted"`, the independent `reviewer` identity and checksummed
`artifacts` for `range_diff`, `verification` and `migration_review`. Each artifact
has `kind`, `path` and `sha256`. The lead records the independently reviewed result
under the normal mandatory-review procedure; the receipt is not a reviewer
authentication service.

`patch_equivalent` requires matching ordered stable patch IDs for ordinary
nonmerge commits, retained range-diff evidence and reviewed migration behavior.
`reviewed_change` requires a new integration approval for the final prepared
snapshot, explicit deployed-state compatibility review and a later successful
deployment of the replacement. Both ranges must belong to the same owned
repository and configured target. The replacement must be its current exact
final head and already integrated. Unused, conflicting and intermediate mappings
refuse. Retain the original deployed source and artifact history.

## First installation and threadless maintenance

A pre-contract installed package cannot create managed coordination state.
Use the reviewed candidate's private `coordination-bootstrap` with explicit
source, registered workspace/session, exact predecessor profile token and request.
`--prepare` returns the retained source and a complete request containing the
machine snapshot and profile artifact. Preparation builds and copies outside
claims. Execute the returned request from the exact candidate, retaining the
returned source. It admits a threadless bootstrap owner and machine reservation,
then runs machine activation followed by profile activation in independent
services. An exact execution retry recovers the original jobs.

The bootstrap owner has no notification destination and cannot submit new
unattended work. Later `status`, `reconcile`, `cancel` and `finish` can select its
already retained UUID with `--bootstrap-owner OWNER`. The active tracking
incarnation must still match. The selector cannot create an owner, approve or
submit jobs, or waive integration and completion proofs. Archived owners must be
explicitly revived first.

Profile changes remain forward-only after selection. Preserve the supported
coordination contract when preparing a recovery package. System recovery follows
the configuration owner's deployment procedure. Neither recovery nor bootstrap
authorizes a reboot or default-branch integration.

## Suspension and resumption

`workspace-host suspend` refuses active mutation workers and holds queued work
and reservations. `workspace-host resume` restores services from the exact
selected generation before enabling claims and delivery. It preserves all queued
state and does not select a package or release a machine. If suspension fails
after holding the ledger, it restores services and the prior suspension flag;
failed compensation keeps suspension visible and requires `resume`.

## Capacity and retained evidence

Protocol stdout remains complete within its bound, normally 256 KiB. Prepared
Nix environment parsing has a separate 16 MiB bound; large Git diffs are hashed
as streams. Preparation and worker diagnostics retain at most 4 MiB per operation with an initial section
and a tail, and continue draining after the cap. Private logs use mode 0600 and
never prove an outcome. Ledger/portal errors are bounded UTF-8 text.

The ledger has a 16 MiB limit, with at least 2 MiB reserved for recovery and a
conservative budget for outstanding results and cancellation/completion writes.
Admission checks the prospective ledger, including the new records and receipt,
plus the remaining growth of every pending job, undelivered notification and
unreleased reservation. Notification allowances survive job completion. Worker
results, reasons and request receipts have 16 KiB encoded JSON bounds; deployment
history allows one unknown-to-applied disposition per attempt. Completion accounts
for actual coverage and contracts, integration proofs and both frontier projections.
Native notification options and receipts use the existing checksummed artifact
store. The ledger retains their identifiers and a bounded event envelope.
Persisted file limits include the trailing newline. A result, artifact or native
request must fit its complete file bound before publication.
Worker requests seal the current operation; refresh history and prior results
stay in the ledger. Admission checks the complete worker envelope before taking
a resource claim. An oversized snapshot returns `needs_refresh` without an
attempt, so its owner can reduce it and refresh the job.
Those recovery requests may use the reserve after normal admission fills, and
have a 16 KiB request bound. Existing request IDs remain idempotent at capacity. New preparation/admission requires
at least 1 GiB of free space. Capacity refusal preserves existing authority.
Compact artifacts, snapshots, request receipts and history remain available.
Disposable source/merge-target worktrees and their dedicated Nix roots are
collected once their final required reference ends. Never delete unresolved
reservations or receipts to make room. See [payload collection](#payload-collection).

A claim without `request.json` predates any worker launch but still requires
operator recovery; this release does not automatically redispatch it. Likewise,
`finish` retains full integration proofs even when deployment was canceled before
activation. Early release without integration is deferred; lifecycle abandonment
or separately reviewed exceptional recovery remains required.


## Payload collection

Inspect the global per-user coordination store with:

```sh
workspace-host coordination gc --dry-run --json
workspace-host coordination gc --apply --json
```

The default is a preview. `actions` identifies collectible worktrees and root
links, `removed` records successful removals, and `preserved` explains holds or
live references. `retry` means the ledger changed; rerun the same scan. Output
contains paths and reasons, not environment dumps or credentials.

The coordinator requests collection after ledger changes and every five minutes
through `workspace-coordination-gc.service`. It keeps deletion out of scheduling.
Collection preserves pending jobs, live worker locks/services, all unreleased
reservation recovery, unfinished integration journals, pending notification
artifacts and shared references. An operation succeeding does not retire a
reservation still held for deployment review. The selected workspace profile,
its predecessor and generations required by live work keep their package roots.

A preparation not submitted within 24 hours expires. A new preparation renews
its lease; status and collection previews do not. Older unused preparations and
unsealed interrupted payloads receive a 24-hour grace period at first applied
collection. Submitted snapshots stop independently pinning payloads after their
jobs/recovery obligations end. Fresh submission of an expired/consumed snapshot
without a live job reference requires preparation; an exact completed request
retry returns its saved receipt.

A `.keep` file, a native Git worktree lock, local changes, process references,
busy Git resources or unknown layouts preserve a payload. Collection uses Git
to remove registered worktrees; it does not delete user branches. Source
payload deletion is final, but original repository refs and compact evidence
remain available for a fresh preparation. Nix store paths are reclaimed only
by ordinary Nix GC.

`retention.json` is separate schema-1 bookkeeping for leases and interrupted
worktree removal. Existing ledger, snapshot and artifact formats are unchanged.
Collection shares generation admission with session creation. A separate payload
guard excludes new preparations, and package switches retain exclusive generation
admission. Routine collection does not prevent creating sessions;
legacy in-flight preparation commands also postpone collection. Deletion runs
outside ledger transactions. A changed ledger stops the current sweep, and
interrupted worktree removal resumes from its recorded exact path/common Git
directory. Do not hand-edit the bookkeeping to bypass a preservation reason.

Collection also takes each integration driver's existing lock without waiting.
A busy driver protects its own payloads and dependencies while the collector
continues with unrelated completed integrations. Shared retained sources also
remain protected while a legacy driver may still reuse an unrecorded head; unfinished journals retain hook dependencies
for their source heads between invocations. Once an integration is complete,
its registered, detached scratch worktrees below `integrations/<UUID>/` become
eligible. Collection verifies the recorded repository, workspace ownership,
cleanliness, process references and explicit holds. It preserves the compact
integration journal, feature branches and published history. Unknown files or
layouts survive for operator inspection.

Before removing integration scratch, the collector records its exact path,
common Git directory and HEAD in the journal's optional `payloadGcPending`
field. This is an admitted removal intent: retries continue deleting that exact
scratch checkout even if tracked files or `.git` have already disappeared.
The retained Git registration must still identify its original detached HEAD
and repository; a changed or missing registration preserves a surviving path.
If `.git` is already gone, Git cannot remove the surviving directory. The
collector finishes that admitted directory deletion, then asks Git to remove
its exact retained registration.
Do not reuse a checkout while its removal is pending. Process references and
`.keep` still postpone a retry, but remaining files are already admitted for
deletion rather than checked again for local changes. The field is removed
after completion.
Existing source retention bookkeeping is unchanged; older journal readers
preserve this additive field. An older collector leaves integration scratch and
this pending work untouched; resume collection with the newer runtime to finish.

Worker package roots also have a bounded lifetime. Notification roots are
released after their worker lock and service are idle. Pending messages and
their payload dependencies remain retained; the next dispatch roots its selected
package again. Background integration worker roots survive unfinished journals
and running services. Unknown root ownership or a mismatched package digest
prevents removal.

The collector prunes recognized workspace Nix profile generations through
`nix-env` under the existing profile-transition exclusion. It retains the
selected generation, one predecessor, all newer generations after a legacy
rollback, and package generations referenced by live operations, preparations or
recovery. It rechecks the selected profile identity before each removal and
does not change profile selection.
Other users' or system Nix profiles are outside this policy. Workspace package
switches are forward-only; retaining the predecessor supports diagnosis and
recovery evidence, not automatic workspace rollback.

The same sweep retires legacy positive-numeric symlinks immediately below
`state/codex/generations` when their targets are direct Nix-store outputs.
Preview reports them as `codex_generation_root` actions; apply unlinks those
roots, including roots for older running store executables. It preserves
`codex/current`, ordinary profiles and all other root families. Nix runtime
roots protect running executables and their dependency closures; see
[Codex dependency retention](codex-package.md#daemon-selection-and-dependency-retention).

Legacy Codex cleanup requires a valid current root and unchanged selected
workspace profile. The collector revalidates the profile identity, current
target and exact history link target before each unlink. Changed identities
refuse that mutation; an already absent history link is safe to retry. A valid
pending Codex transition skips only this cleanup and reports why; repeat the
ordinary switch/reconciliation to finish forward recovery, then collect again.
Malformed pending state refuses collection through the host's strict parser.
Symlinked history directories, unknown names, ordinary files and unrecognized
targets survive and appear in `preserved`. Collection never follows the history
directory through a symlink or recurses into it.

Use the preview/apply commands above after a successful switch or reconciliation,
or let the periodic sweep perform retirement. Repeated collection is harmless;
an older writer that recreated a numeric root leaves it eligible for a later
sweep. Existing package-generation admission excludes superseded writers from
new package operations. Retirement does not change profile selection, pending
records or launch provenance, and does not run store GC or restart daemons.

These policies release disposable references; they do not impose a byte limit
on active work. A live operation, held checkout, retained feature worktree or
running process can still keep an old closure. Nix GC decides when store paths
are reclaimable. Bulk archives included in a workspace Git input still multiply
its size until their copies and package roots become unreferenced.

### Storage inspection and explicit expiration

`workspace-host coordination gc --dry-run --json --sizes` reports allocated
payload bytes and preservation reasons. Adoption-grace rows include their expiry.
The preparations list reports saved lease deadlines.
Size reporting walks payload contents and is optional; routine collection avoids
that cost. Preview does not renew leases or write retention bookkeeping.

For a one-time cleanup, add `--expire-unused` to preview expiration of unused
preparation leases and orphan grace periods, then add `--apply` to perform it.
Queued jobs, live attempts, reservations, unfinished journals and explicit holds
still protect their dependencies. Expired unsubmitted requests need preparation
again; exact completed-request retries retain their saved receipt behavior.
Existing lease deadlines remain valid unless this explicit expiration is used.

Additional workspace checkouts omit work/ and archive/ through per-worktree Git
sparse checkout. Shared tracking stays in the complete registered workspace;
independent project repositories keep their normal layouts.
