# Coordinating shared resources

The selected user-profile runtime provides
[resource claims and notifications](https://github.com/aither64/dev-workspace/blob/master/docs/coordination.md).
Sessions acquire repository or machine ownership, run their own commands,
verify effects and explicitly release. Read `workspace-host coordination guide`
before using it. A predecessor without claims retains its installed job workflow.

## Session workflow

Complete implementation, history consolidation, checks and independent review.
Obtain the user's explicit direction for the affected repository/target or
machine/actions. Deployment approval never grants merge approval.

Develop independently in session-owned worktrees. Edits, commits, rebases,
dependency updates, feature pushes, hook preparation, tests and review take no
repository claim. Prepare the clean target checkout and its dependencies first;
obtain merge approval before requesting ownership. Repository tools own hook
trust and ordinary Git locking. Keep hooks and signatures enabled.

Use `workspace-host coordination acquire SESSION --as-is --request FILE` with a
UUID `requestId`, `label`, and `repositories`/`machines` arrays. Schema 1 remains
available for repository claims and legacy catalog machines. New machine requests
use schema 2 and exact targets from a session's registered configuration repository,
as described below.
Supply at least one registered repository or configured machine. The request
atomically returns `held` or `waiting`. A waiter owns no resources; the coordinator
notifies its retained conversation when the complete request is granted. End the
turn when only waiting remains. Read `claim-status` before acting on any notice.
A notice neither authorizes work nor proves command completion.

Run the shared merge or deployment only while its claim is held. Independent
feature commands remain available during a merge wait. Follow the runtime's
[machine retention and release policy](#machine-retention) and the configuration
repository's operations guide.
Use `release SESSION --as-is --id UUID` after the applicable release requirements
are met, or `cancel-claim` for an unneeded waiting request. Retrying the exact
acquire request returns the same claim even after release; a new attempt needs
a new UUID. Request all resources
together or keep separate claims disjoint to avoid waiting on your own ownership.

Claims do not expire when an agent becomes idle or disconnected. After an
interruption, inspect effects and stop remaining local/remote mutations before
considering release. Repository locks follow the short merge procedure below;
deployed machines follow the retention rule below. Held claims block lifecycle
cleanup until explicitly released. Session completion still requires exact final
heads integrated and all work finished. Existing legacy reservations keep their
original completion requirements. Never release another session's resources or
edit records.

The Operations page shows owners and waiters; machine claims also appear in the
session Reservations tab. This is cooperative locking. Ordinary project tools do
not intercept arbitrary commands. Participating sessions must acquire the required
resources before mutation and keep ownership until the work is safe to release.

## Machine claims

Use the repository's exact configured `Machine.name`, including an FQDN when that
is its configured name. The default logical identity combines the canonical Git
origin with that name; it does not inspect the OS hostname, DNS, SSH target or
physical machine. Clones, worktrees and local repository aliases with the same
canonical origin and configured name contend for the same lock. Use a unique
configured target name when several machines have the same OS hostname.

For this workspace's host, a machine request has this form:

```json
{"schema":2,"requestId":"11111111-1111-4111-8111-111111111111","label":"Deploy workspace host","repositories":[],"machines":[{"repository":"vpsfree-cz-configuration","selector":"cz.vpsfree/machines/aitherdev","adapter":"confctl"}]}
```

The runtime resolves metadata from the registered repository's committed feature
head through the installed adapter. Commit configuration changes and prepare any
missing locked inputs before acquiring ownership. Resolution evaluates local
configuration metadata without building or copying a system or contacting the
machine. Ordinary new targets need no workspace package or catalog update.

The default identifier for this target is
`machine:github.com/vpsfreecz/vpsfree-cz-configuration:cz.vpsfree/machines/aitherdev`.
Identifiers use single colons and percent-encode reserved characters; the runtime
stores structured identity fields rather than parsing this display string.

Configurations that intentionally refer to the same target through different
repositories can set the same `labels."dev-workspace.lock-id"` value. It replaces
the repository/name identity with one shared logical ID. Values must be valid
UTF-8, contain 1–256 bytes, and have no control characters or leading or trailing
whitespace. An absent label uses the default identity; the resolver rejects null,
empty or malformed labels. Coordination does not detect accidental physical
overlap between different logical identities. Changing an origin, configured name
or shared ID changes the lock namespace. Preserve a stable ID or an explicit
compatibility bridge while active ownership or accepted legacy aliases depend on
the old mapping. Held ownership never silently follows a changed identity.
Terminal history alone does not retain ownership, but still requires a package
that can read schema-2 records.

Before an intended committed deployment batch, verify its current mapping once:

```sh
workspace-host coordination verify-machine SESSION --as-is --id UUID \
  --repository vpsfree-cz-configuration --selector cz.vpsfree/machines/aitherdev --json
```

This read-only check requires an owning held claim and the same current logical
mapping. It does not grant ownership or replace deployment, artifact or recovery
checks. Repeat it for a new intended batch rather than before every confctl command.

`config/coordination.nix` retains the old `aitherdev` name, ID and aliases only for
predecessor packages and retained operations. `config/machine-identity.nix` sets
the profile target to the repository/name identity above and bridges the exact old
resource `machine:vpsfree:aitherdev` to it. Keep this finite compatibility policy;
do not add ordinary new machines to the legacy catalog.

For the first upgrade from the old selected package, acquire its existing schema-1
hold with `machines: ["aitherdev"]`. Deploy the authorized system first, then use
the ordinary user-profile switch under that same hold. The new candidate must
recognize the old resource through the bridge. Use schema-2 machine requests only
after the new package is selected. Missing bridges or unresolved ownership refuse
the switch; never release or rewrite evidence merely to make it pass.

## Machine retention

The runtime's [machine retention and release policy](https://github.com/aither64/dev-workspace/blob/master/docs/coordination.md#machine-retention)
defines when the owner must release a deployed machine.
Use `workspace-host coordination guide` to read the selected package's version.
Release the deployed machine promptly after verifying deployment effects and
integrating its complete deployed lineage into the approved remote defaults.
Follow-up UI review can continue afterward. Failed or uncertain effects and
missing integration proof keep ownership held until the original recovery
procedure reconciles them. Deployment approval alone does not approve integration.

## Git and deployment

Acquire one repository only for the final target/feature/cleanliness checks,
ordinary fast-forward merge and hooks, non-force SSH push and remote verification.
Release immediately before CI, records, artifact registration or checkout cleanup.
Do not hold multiple repositories while integrating them sequentially. Stale
baselines or hook intervention return to unlocked preparation once commands stop
and effects are known. Reconcile uncertain shared mutations before release.

The shared workspace stays on master. Preserve unrelated files/index changes and
use its short `dev-session-tracking.lock` for shared tracking writes; independent
bookkeeping does not need a durable repository claim. Shared-checkout integration
acquires the repository claim first and then tries that tracking lock without
waiting; if busy, release the claim and retry after the writer finishes. Hold both
through the fresh target check, merge/hooks, push and remote proof. Preserve
unrelated dirty paths and index entries; disposable target checkouts must be clean.
A resource claim is metadata, not an acquired OS file lock. Keep machine reservations separate from merge claims;
build and copy artifacts before reserving a machine when supported.

Use confctl channels for inputs. Preserve the direct nested runtime override,
extension selection and matching configuration runtime. Run
`bin/check-dev-workspace-deployment` against final locks. The application stays
in its user profile. For ordinary `workspace-host switch --source PATH`, hold the
configured machine claim and pass `DEV_WORKSPACE_CLAIM_ID` plus the exact session
environment identity. Workspace-host owns compatibility, activation journals and
forward recovery. The configuration repository's operations guide owns concrete
machine deployment steps. Runtime selection and default-branch integration retain
their applicable explicit authorization gates.

## Retained operations

Existing snapshot-based jobs, integrations, deployment history, reservations and
uncertain attempts keep their original recovery procedures. New claims cannot
release their reservations or replace evidence. A retained job's preparation
supplies its exact `legacyJobId`; integrations resume by their original ID.
Never submit a replacement job to hide an uncertain effect. Legacy bootstrap
operations retain their dated recovery procedures. The generic package installs
the retained integration guide alongside current coordination/recovery guides.

Legacy lifecycle completion can automatically release reservations as part of
its existing implementation. Follow the runtime's
[operations and recovery guide](https://github.com/aither64/dev-workspace/blob/master/docs/coordination-operations.md)
for retained operations. Finishing work, releasing a claim or preparing a handoff
does not authorize archiving, deleting, stopping or cleaning a session.
