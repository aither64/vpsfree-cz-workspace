# NixOS stable channel update

Design owner: architect0. Package D sufficient brief amended 2026-11-18.
Packages A and B are released by the lead under the corrected one-time pin
contract below. Exact inventory results remain implementation evidence.

User correction, relayed by the lead: "i did NOT ask you to change the branch,
I asked you for a one-time update to release-26.05 to get this fix sooner."
This supersedes the initial interpretation that changed the tracking branch.
The resulting branch-selection commits were unpublished and unintegrated;
implementers are removing them from their own feature history. Final acceptance
requires the original flake URL and lock `original` tracking attributes intact.

## Scope and settled evidence

Update only the `nixos-stable` channel's `nixpkgs` role in the two requested
repositories once to exact published revision
`4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d` from `release-26.05`, while preserving
`nixos-26.05` tracking. Merge through the lead and report the systems that need
deployment for the nginx update. No deployment is requested. The final change
is generated `flake.lock` only; no handwritten application, stateVersion, module,
input URL, original ref, or unrelated dependency change belongs in these packages.

[Nixpkgs PR #589970](https://github.com/NixOS/nixpkgs/pull/589970) is merged into
`release-26.05`, at `1e6cf0d7cf5f5354d1bfd7105813dddb527851d4`, on
2026-11-18 at 16:03:46 UTC. The patch changes only nginx mainline/stable package
version and source hash: 1.31.8 → 1.31.9 and 1.30.6 → 1.30.7. Its parent PR
[#589961](https://github.com/NixOS/nixpkgs/pull/589961) is titled “Nginx Security
Updates”. Do not infer particular CVEs or unaffected configurations from this
title alone.

At investigation time, GitHub reported `release-26.05` tip
`4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d`. Comparing the PR merge to that tip
returned `ahead`, ahead_by 6, behind_by 0, and merge-base equal to the PR merge.
The implementers must bind this proof to the actual generated lock revision,
which must equal that exact SHA. Do not chase later branch movement. Source
inspection of the locked nginx package definitions supplies a second direct
check. The one-time locked revision comes from **release-26.05**; the original
tracking ref remains **nixos-26.05**. The release family remains 26.05.

## Packages and file ownership

| Package | Owner / files | Dependencies | Acceptance / evidence |
| --- | --- | --- | --- |
| A: vpsfree-cz-configuration channel | implementer0; this session's repository worktree; generated `flake.lock` only; package-a.md evidence | Corrected brief and lead release; no B dependency | Original flake and tracking identity, exact channel mapping, isolated final diff, locked fix inclusion, bounded evaluation and nginx-target inventory, exact base/head and checks |
| B: vpsadminos-org-configuration channel | implementer1; this session's repository worktree; generated `flake.lock` only; package-b.md evidence | Corrected brief and lead release; no A dependency | Same acceptance; account for fancyindex nginx overrides |
| D: design | architect0; this file only | Repository and upstream read-only inspection | Settled scope, channel mappings, compatibility and verification contract |

Implementers own diagnosis, their generated input updates, hooks, commits,
checks and evidence. They may clarify routine details directly with architect0
or each other using actual same-session addresses. Lead owns release,
acceptance, review decisions and authorized integration. Separate repositories
and evidence files permit parallel execution; no shared index or generated
output is needed. Architect does not edit application files or commit tracking.

## Channel update contract

| Repository | Channel / role | Root input | Preserved URL |
| --- | --- | --- | --- |
| vpsfree-cz-configuration | nixos-stable / nixpkgs | nixpkgsStable | `github:NixOS/nixpkgs/nixos-26.05` |
| vpsadminos-org-configuration | nixos-stable / nixpkgs | nixpkgs | `github:NixOS/nixpkgs/nixos-26.05` |

In the prepared worktree, reconcile any in-flight effects and remove only the
owned, unpublished commits implementing the superseded branch switch. Begin
from the original base flake and lock, including `original.ref = nixos-26.05`.
Confirm `confctl inputs channel ls` and input mapping using the repository's
pinned development shell. Use the exact channel-owned set command:

```sh
nix develop -c confctl inputs channel set --commit --no-changelog nixos-stable nixpkgs 4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d
```

Do not edit `flake.nix`, manually edit `flake.lock`, update all inputs, or pin an
unmerged PR. This set command is appropriate for the user's explicit one-time
selection of a published revision as well as ordinary feature pinning. Keep
the generated message and one final generated lock-only commit per repository.
No branch-switch commit or reversal belongs in final base-to-head history.
Use required hooks and the repository environment; no hook bypass.

Verified against pinned confctl's `lib/confctl/inputs/setter.rb`:
`Setter.run!` saves the selected root node's complete `original` attributes,
resolves an exact GitHub override URL, invokes Nix lock generation into a
temporary output, restores the saved `original` attributes in that generated
output, then renames it into place. Its commit lists only `flake.lock`. Therefore
start from the original lock, not a rejected branch-switch lock: the setter
preserves whichever original attributes it receives. The ordinary future
channel update remains tied to `nixos-26.05`.

Preserve `nixpkgsStaging`, `nixpkgsProduction`, `nixpkgsUnstable`, confctl,
vpsAdmin/vpsAdminOS, and all other direct inputs and follows edges in A. In B,
preserve `vpsadminos`, confctl and their independent nested inputs. A changed
lock node name is not an input identity: resolve `nodes.root.inputs` and follows
paths before comparing semantic identities. In particular, B's root `nixpkgs`
was node `nixpkgs_3` in inspected locks; `.nodes.nixpkgs` was unrelated.
Expected transitive effects caused by existing follows edges are allowed;
unrelated revisions or graph rewrites require diagnosis before acceptance.

## Compatibility and deployment/recovery invariants

This advances a same-release nixpkgs input once to obtain a published security
package update before `nixos-26.05` advances. It retains the channel's future
tracking behavior and carries other changes between old and new locked
revisions; do not describe the whole input diff as nginx-only. Existing
forward-only scheduled updates may defer until `nixos-26.05` catches up; no
workflow change is part of this request.

No local API/protocol/schema/state-format/module interface is changed. Existing
stateVersion and database version selections remain unchanged. No coordinated
node update or cross-repository ordering is introduced. Existing consumers of
the input through follows still receive its package set, so report the wider
channel consumer set separately from the nginx deployment subset. nginx's
version/hash fix introduces no configuration migration in this PR. Evaluated
configuration assertions must still hold.

No machine reservation, activation, restart, dry-activation, remote service
inspection or deployment is part of this task. Merge alone changes no running
system. Future rollout should follow each repository's ordinary machine
ownership/build/deployment procedure, start incrementally, and retain the old
system generation for rollback. These checks do not certify rollback of every
other package or persisted service state changed by a future whole-system
deployment; assess those effects before that deployment. Reverting the generated
lock is source recovery, not a rollback of a running machine. Session remains
open; integration does not authorize session cleanup or lifecycle actions.

## Smallest faithful verification

1. Quick checks: required hooks, `git diff --check`, channel/input inventory,
   semantic old/new lock diff, exact locked revision ancestry and locked nginx
   versions. Prove `flake.nix` byte identity with the original base and complete
   selected-node `original` equality (including nixos-26.05), unchanged follows
   and sibling identities, exact locked SHA above, and only `flake.lock` in the
   final changed-file list. All intended changes must be committed before any
   required final review. Whole-branch history must contain no superseded
   branch-switch commits.
2. Bounded evaluation: enumerate managed machine metadata and resolved role
   inputs; evaluate enabled nginx and actual package identity for changed-input
   consumers, including service-module enablement and custom nginx overrides.
   Evaluate selected machine derivation paths/assertions where available without
   realizing full systems. Scope to the channel change and inventory, not all
   unrelated checks exported by the flake. Record any evaluation error precisely.
3. No long build, VM test, fleet rebuild or deployment is required by this brief
   for the mechanical update. If evaluation exposes a real compatibility issue,
   stop at the failing component and agree the smallest faithful next check with
   the lead. Long/uncertain checks use the monitor procedure; unexpected local
   kernel builds stop for investigation. Do not expand scope to repair unrelated
   failures silently.

Lead applies the mandatory-review skill's mechanical-content exemption or final
review requirements to the completed diff, and retains whole-branch history and
no-migration accounting. Scheduled update workflows are not validation workflows
and must not be dispatched for this task. No new test suite or repository docs
are needed for this routine update; session evidence explains the decision.

## Identifying nginx deployment targets precisely

Use the evaluated configuration, not only `rg` or metadata service labels:

1. Read `confctl.machines`, `confctl.buildPlan`, `confctl.machineKeys` and
   `confctl.inputsInfo`. Select managed machines, then resolve each machine's
   `nixpkgs` role after ordered channels and per-machine overrides. Enumerate
   consumers of A's `nixpkgsStable` or B's `nixpkgs`; preserve exact confctl machine
   selectors and host aliases. Do not duplicate B's hosts from A's unmanaged
   `cluster/org.vpsadminos/cluster.nix` reference entries.
2. Evaluate the actual system modules with the locked confctl evaluator and
   original inputs. Read `config.services.nginx.enable` and, when true,
   `config.services.nginx.package.{name,version,drvPath,outPath,src}`. Record
   source tarball path/hash identity as available and module overrides. Packages
   installed separately from the service are not automatically active services;
   inspect the unit ExecStart/package if configuration redirects execution.
3. Tie the actual package source to nginxStable/nginxMainline in that machine's
   resolved nixpkgs input. Require the updated version and matching source
   identity, allowing modules such as fancyindex to change derivation paths.
   Mere channel membership, a version string alone, or `services.nginx.enable`
   alone cannot prove the selected executable contains this update. Compare old
   and new evaluated identities where needed to distinguish newly fixed targets
   from already-fixed or differently sourced nginx.
4. Emit three groups: configured nginx targets that receive this fix; other
   channel consumers; any nginx consumer whose independent package source leaves
   it outside this fix. State that this is desired-configuration evidence, not a
   claim about the currently deployed generation.

Both inspected repositories pin confctl
`ff5e017780a35fb97b549db2a51b570193867c3b`. Its `mk-confctl-outputs.nix`
contains `evalConfigFor` but does not export evaluated configs. A bounded
session-local probe may expose that existing value without changing repository
code: read the pinned evaluator source, verify a unique final-output insertion
anchor, add an output mapping `machinesWithKey` to
`(evalConfigFor m).evalConfig.config`, and import the instrumented expression
with the original `confDir`, inputs and channels. Keep all module inputs and
arguments unchanged; do not force its unused relative `moduleOptions` import
from a relocated probe. Save this disposable probe/evidence in the session,
never the configuration commits. An equivalent probe that exactly reproduces
the pinned evaluator's modules/specialArgs is acceptable. Verify the probe
against the actual pinned source before relying on its output.

Static B candidates are `org.vpsadminos/int.images`, `org.vpsadminos/int.iso`,
`org.vpsadminos/int.www`, and `org.vpsadminos/proxy`. Images and ISO select
`pkgs.nginx.override` with fancyindex; this preserves upstream nginx source but
must be checked in the evaluated package. A also enables nginx indirectly via
service modules (for example vpsAdmin frontends), so a source grep is only an
inventory cross-check. Final target lists belong in package evidence and lead's
report after evaluation, not a guessed deployment command here.

## Evidence and remaining work

Inspected workspace routing, team guide, documentation skill, repository
AGENTS/README where present, input definitions and locks, confctl input docs and
evaluator, and PR API/compare data. B has no tracked AGENTS/README/docs at the
inspected revision. Bare HEAD was older than origin/master; implementers own
fresh fetched bases and final evidence. No other session was used as a source.

No design blocker remains for the corrected A/B pin. Implementers supply final base/head,
changed paths, hook results, locked identities, bounded checks, exact inventory,
known gaps and no-migration/history conclusion. Lead records approved target
integration and remote final-head proof. No application documentation update is
useful: behavior and operating procedures are unchanged, and local guidance
places this update's verification evidence in session records.

## Current implementation brief: D5 / package C — forward-only no-update semantics

Recorded 2026-11-18 by architect0. This is the current development scope; the
preceding sections preserve the completed configuration pin's rationale and
evidence. User accepted the proposal and directed: “design it first and then
implement it.” The brief below is sufficient for lead release of package C.
No design blocker remains. Lead owns the pre-commit user-visible prose pass.

### Source and scope

Fresh fetched confctl default/base, confirmed by implementer0, is
`ff5e017780a35fb97b549db2a51b570193867c3b`. It is exactly the previously inspected
configuration-pinned revision, so there is no implementation baseline drift.
The bare repository's local master is older and is not the implementation base.
Read current default AGENTS, README, input guide, CLI/man definitions, transaction,
validator, graph resolver, result/commit composition, existing focused specs,
Rakefile, flake checks and CI routes.

Only confctl changes. No new flag, workflow workaround, lock-graph merge engine,
dependency solver, automatic retries, configuration-repository source updates,
version release, deployment or default-branch integration is included. The two
configuration repositories continue using the old behavior until a separately
authorized confctl pin update. Feature publication follows the workspace rules;
confctl integration needs its own explicit approval.

| Package | Owner and files | Dependencies | Acceptance |
| --- | --- | --- | --- |
| C: guarded update no-op semantics | implementer0; confctl source, focused specs, input docs/man/changelog, owned package-c.md evidence | This brief and lead release; prepared session worktree/environment; no other implementing owner | Behavior and transaction guarantees below, quick checks, one complete review packet and required independent review |

Expected source boundary: `lib/confctl/inputs/{forward_guard,guarded_update,updater,commit_message}.rb`,
`lib/confctl/cli/inputs/{update_result,root,channels,machines}.rb`; minimal
`lock_graph.rb` change only if needed to expose its existing resolution.
Specs belong in existing `spec/inputs/{forward_guard,guarded_update,commit_message,lock_graph}_spec.rb`
and `spec/confctl/cli/inputs_forward_only_spec.rb` as applicable. Update
`docs/flake-inputs.md`, the three `--forward-only` entries and strict-check wording
in `man/man8/confctl.8.md`, and `CHANGELOG.md` Unreleased. Generated man output
remains ignored under existing conventions. Do not regenerate the unrelated
module-option reference. No dependencies, Nix inputs or workflow edits are needed.

Implementer0 owns source/tests/docs, diagnosis, hooks, commits, evidence and review
fixes through completion. Architect0 owns this brief and routine clarification;
lead owns scope, acceptance, independent review and the before-commit prose
window. This is one package: source, CLI and tests share the same interfaces and
must not be split among overlapping owners.

### Behavior and compatibility contract

For `inputs update --forward-only`, including root, `--all`, channel and machine
forms:

| Candidate relation or defect | Outcome |
| --- | --- |
| Identical locked sources throughout attempted graph | Successful unchanged attempt |
| All changed existing revisions are descendants; graph otherwise valid | Accept complete candidate into temporary accumulated state |
| One or more behind revisions, with no other rejection or evidence error | Discard whole attempt; report unavailable forward update; continue |
| Divergence, changed source/extraction identity, removed reachable path, or changed locked metadata at equal SHA | Reject invocation, exit 3; install nothing |
| Missing/invalid ancestry, unsupported changed source, malformed graph/Nix result, cached-fetch fallback, unmatched selection or concurrent writer | Fail invocation, exit 1; install nothing |

“Behind” means Git ancestry, never timestamp or package-version comparison.
An attempted parent upgrade containing a behind nested dependency is skipped as
a whole; do not combine its new parent with hand-selected old children. A mixed
behind plus divergent/invalid candidate is a failure, not a skip. Equal SHA with
different locked hash/timestamp stays a rejection. Independent selected inputs
can advance even when another input is skipped.

`check-update` remains a strict validator of the two supplied locks: a behind
candidate still exits 3. The underlying `ForwardGuard` retains that meaning.
Unflagged updates, explicit `set`, ancestry/cache integrity and `--downgrade`
meaning remain unchanged. This intentionally changes the documented exit-3
contract for behind-only *update attempts*, not strict artifact validation.
Document the successful no-op/partial-update behavior and the distinction in the
existing docs and Unreleased changelog; introduce no alternate skip flag.

There is no persisted schema, generation format, API protocol or stateVersion
change. Old and new tools read the same locks; returning to the old binary restores
its behind-is-error behavior. Existing single-writer/mirror compatibility rules
still apply. Git ancestry retains commits, not their effects: later descendant
reverts are still outside this check, and divergent cherry-picks still reject.

### Settled result interfaces

Keep `ForwardGuard::Result`'s `status`, `changes`, `issues` and predicates. Add a
`rejections` array of structured values with fields `kind`, `path`, `old_rev`,
`new_rev`. Kinds are `behind`, `diverged`, `source_changed`,
`revision_metadata_changed`, `removed`. Existing human-readable `issues` remain
available for CLI diagnostics. Evidence errors retain status `error`; they cannot
be classified as skippable. Populate a structured record for every policy
rejection; never parse issue strings to recover its kind.

A helper such as `behind_only?` is true only for status `rejected`, a nonempty
rejections array, and every rejection kind `behind`. `success?` must remain false
for this validator result so `check-update` cannot accidentally accept rollback.
Preserve existing status priority: errors, then rejection, then updated/unchanged.

Guarded updater results keep `status`, `changed`, `changes`, `issues` and add
`skipped` (array; empty normally) and `updated_inputs` (original selected logical
names whose attempts accepted graph changes). A skipped entry contains
`input` (original canonical terminal target), `requested_inputs` (sorted original
names/aliases mapped to it), and the structured behind `rejections`. These records
describe skipped attempts, not a promise that no other accepted attempt touched
the same shared dependency. `changes` always describes the final installed graph
versus the initial baseline, never discarded candidates or temporary steps.

Use `unchanged`/`changed: false` with skipped diagnostics when all attempts leave
the original graph unchanged; no third success status is necessary. A mixed
accepted/skipped result is `updated`/`changed: true`. Failure results expose no
purported installed changes. Internal callback plumbing can accept the final
`updated_inputs` alongside `changes` so existing commit composition receives
accepted selected names, rather than claiming a skipped input was updated.
Keep that callback change local to GuardedUpdate/Updater and their tests.

### Deterministic resolution and transaction

1. Hold the existing cooperating-update process lock for the whole invocation.
   Take the existing clean tracked-checkout/lock/HEAD/index snapshot once.
2. Resolve every original selected logical input using the initial LockGraph.
   Group aliases by terminal path, deduplicate and lexically sort terminal paths;
   sort original alias names within each group. This order is independent of CLI
   selection order; a parent terminal path precedes its nested child.
3. Start a temporary accepted reference with the exact original lock bytes.
   Before each attempt, re-resolve **all original selected names** against the
   accumulated accepted graph. Each must still resolve to its original terminal
   path. Missing or redirected selections fail as a selection/evidence error
   before installation; do not silently update a new target or add work. Also
   check this invariant for an accepted candidate, including the last attempt.
4. Invoke the existing Nix update helper with a one-element canonical target
   array and distinct `--reference-lock-file`/`--output-lock-file` paths. Nix
   generates the entire candidate from the last accepted reference. Never
   update the real lock between attempts and never edit graph nodes manually.
5. Validate the complete reachable candidate graph against the accumulated
   reference using ForwardGuard. For updated success, retain the complete
   candidate as the next reference; for unchanged success, retain the previous
   reference bytes. For pure-behind rejection, retain the previous reference
   and record a skip. Every other rejection/error aborts the invocation.
6. After the finite pass, validate final accumulated graph strictly against the
   original baseline. A failure here is a failure, never a skip. Recheck the
   existing checkout snapshot even for an all-skipped/unchanged success.
   If unchanged, leave exact original lock bytes and do not commit. Otherwise
   compute final original→accepted changes, preserve mode, atomically rename
   once, mark installed and run the ordinary commit once when requested.

Complete-graph validation includes aliases, descendants, new/removed paths and
shared follows. No accepted step may regress a change accepted earlier; the
final check also binds the result to the initial pin. Do not carve a safe root
out of a rejected candidate. The guarantee is safe progress for independent
inputs, not maximal progress for interdependent inputs: an intertwined target
may conservatively skip in the deterministic pass. No search, replay or fixed
point iteration is required. A later accepted attempt may safely advance shared
state; summaries must use the final graph and label skip records as attempts.

Retain all existing failure/recovery semantics. Temporary files are cleaned on
ordinary failure/interruption before install. Nix errors and warnings cannot
fall back to an in-place update. A concurrent writer's changes are neither
overwritten nor rolled back. A commit-hook failure after the final install
continues to fail while leaving the validated candidate/hook effects for
diagnosis; do not pretend to roll back a hook transaction. Separate command
invocations remain separate transactions. Source rollback needs no data migration.

### CLI and documentation

Root, channel and machine forms must report skipped attempts explicitly, with
logical input and retained/candidate revisions or nested blocking path. Reuse
the shared UpdateResult helper for skip formatting instead of separate policy
implementations. Preserve channel/role and machine/role context where available.
Do not print the current unconditional `Updating ...` line as evidence that a
skipped input advanced. Report final accepted updates from final `changes`; an
all-skipped case may print `No changes.` after its skip explanation. Preserve
unguarded update/set output behavior and strict check-update diagnostics.

Commit revision summaries/changelogs remain selected-input-only and describe
original→final accepted values. Skipped attempted revisions never enter the
commit. If only descendants changed, retain existing generic selected-input
title behavior. Do not add operational receipts to confctl docs. Lead performs
the required user-facing prose pass on settled messages/docs before commit;
implementer may continue disjoint tests during that short owned prose window.

### Acceptance and checks

Quick phase, in confctl's `nix develop` environment, before final review:

- Focused RSpec for guard, guarded transaction, commit message, graph resolution
  and forward-only CLI; changed Ruby lint, required hooks and `git diff --check`.
- Regressions prove: behind-only success/no commit/exact bytes; equality;
  descendant catch-up; independent mixed skipped/accepted inputs with one final
  commit; parent-forward/nested-behind whole-attempt skip; aliases deduplicated;
  shared follows never regress; deterministic order and selected-path drift
  failure; strict `check-update` still returns 3 for a behind lock.
- Any divergence, metadata/source/removal rejection or evidence/Nix failure
  after earlier accepted temporary work leaves original lock/index/HEAD; mixed
  behind-plus-hard-error is not suppressed. Retain concurrent-writer,
  interruption, cached-response and post-install-hook-failure regression coverage.
- Verify candidates receive the previously accepted lock as their Nix reference,
  while rejected attempts never become later references. Include a small real
  Nix fixture exercising sequential reference/output-lock plumbing where the
  existing test harness permits it; keep provider/graph rules separately tested
  and avoid live upstream resolution in regression tests.
- Generate command manpages with `bundle exec rake md2man:man`; ensure generation
  succeeds without adding ignored output. Nixfmt is required for any changed
  Nix fixtures; if none change, record that no Nix formatting change was needed.

After all intended changes are committed and quick checks pass, lead invokes
mandatory independent review with complete base→head series, final diff, this
contract and explicit no-migration/history conclusion. After review, run full
`bundle exec rspec` and `bundle exec rubocop` before feature publication, reusing
already-passing identical results if those full checks completed in the quick
phase. Long/uncertain checks use the monitor procedure, not unowned background
jobs. Existing push CI covers Ruby versions, RuboCop and CI-tagged integration
tests; lead owns monitoring and any necessary failure response. No new workflow
or manual fleet/deployment test is required for this change. Stop unexpected
local kernel builds under the existing verification procedure.

Implementer evidence must identify exact base/head, changed files, check commands
and outcomes, fixtures' boundary/any gaps, final skip/error semantics, one-install
proof, docs checked/updated, and no persisted migration/release/deployment. Lead
owns plan/state and later approval-bound actions. Routine clarifications may
proceed directly; material contract deviations return to lead before execution.

## Current adoption brief: D6 / packages A2 and B2

Recorded 2026-11-18 by architect0 after package C was reviewed, tested and merged.
This section is the current scope. User's “yup, continue” follows the proposed
next step of updating confctl in both configuration repositories. Lead owns
that continuation's integration scope. Packages A2/B2 are sufficient for lead
release with no open design dependency. Earlier merged configuration and confctl
history remains intact.

### Exact source, ownership and command

Adopt published confctl master revision
`d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49` in both repositories. Both implementers
freshly verified that remote confctl/master equals this revision. Both inspected
flakes have the direct root declaration `confctl.url = "github:vpsfreecz/confctl"`;
no channel maps a role to this input. Therefore the documented root update is
the owning workflow, not a channel update:

```sh
nix develop -c confctl inputs update --commit confctl
```

Use the repository's pinned shell and hooks, keep the useful generated confctl
changelog/message, and verify the resulting lock selects the exact SHA above.
Do not edit flake URLs or lock JSON manually. Do not update all inputs. Do not
chase a later unrelated confctl head: if branch movement causes this command to
select another SHA, report it and reconcile the owned unmerged attempt before
using the existing root `inputs set --commit confctl <exact-SHA>` workflow to
produce the requested final pin. Preserve original input tracking metadata and
consolidate any unmerged attempt into one final adoption commit.

| Package | Owner / files | Initial current default | Acceptance |
| --- | --- | --- | --- |
| A2: vpsfree-cz-configuration confctl adoption | implementer0; generated `flake.lock` only; package-a2.md evidence | `828c390c7e1857f11522933977afd852634b85f8` | Exact confctl SHA, preserved nginx pin/tracking and graph, quick checks, one new logical commit |
| B2: vpsadminos-org-configuration confctl adoption | implementer1; generated `flake.lock` only; package-b2.md evidence | `72c18d811086dac8e16ec8c7ee6bf8e32ce62123` | Same acceptance |

The two repositories, indexes, generated output and evidence files are independent;
neither package depends on the other. Both implementers confirmed capacity and
workspace-write access, refreshed current defaults and prepared existing clean
session worktrees. Append new adoption commits after the existing merged pin
commits. Do not rebase, amend or consolidate previously merged history. If a
default advances, preserve it and recheck only the new adoption range. Architect
owns this brief; lead owns acceptance, tracking, history gate and merge coordination.

### Semantic lock invariants

Both root `confctl` edges currently resolve to node `confctl` locked at
`ff5e017780a35fb97b549db2a51b570193867c3b`. Its `original` object is
`{owner=vpsfreecz, repo=confctl, type=github}` with no explicit ref. Preserve it.
Its nested nixpkgs follows `confctl/vpsadminos/nixpkgs`, and its own vpsAdminOS
input is separate from the configuration's machine channels. Preserve these
edges and all nested locked identities.

The adopted confctl source changes no `flake.nix`, `flake.lock` or
`nix/flake/` files relative to its old pin. Expected configuration diff is
therefore only the resolved confctl node's `locked.rev`, `locked.narHash` and
`locked.lastModified`. Resolve semantic root/follows paths rather than relying
on incidental lock node numbering. Diagnose any unexpected node/edge/revision
change before accepting it; this package does not authorize transitive refreshes.

In particular, retain **exactly** the existing `nixos-stable` lock revision
`4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d`, its full source/hash/timestamp identity,
and complete `original` object tracking `nixos-26.05`. A resolves this through
root `nixpkgsStable`; B through root `nixpkgs` (currently node `nixpkgs_3`).
All root declarations, sibling identities and follows mappings must remain
unchanged. `flake.nix` and workflow files are byte-identical to the fresh base.

### Acceptance, verification and history

Use existing source evidence at exact `d8ab7d4`: independent final review, focused
and full RSpec/RuboCop, and successful Ruby matrix/CI integration documented in
package-c.md and the review receipts. Adoption does not justify repeating that
unchanged source suite, full machine inventory or system builds.

Required bounded checks for each package:

1. Generated final diff is `flake.lock` only; required hooks and `git diff
   --check` pass. Record exact fresh base and final new adoption head.
2. Compare parsed old/final lock graphs: exact requested confctl revision and
   only the three expected locked fields changed; original objects, follows,
   nested dependencies and all siblings identical. Prove flake/workflow byte
   equality and exact retained nginx pin/tracking.
3. Read-only resolution through the updated pinned environment confirms confctl
   points at the adopted source and existing channel mappings still evaluate
   (for example `confctl inputs ls --json confctl` and `confctl inputs channel ls`).
   If preparing the changed tool's shell/package takes over a minute, use the
   normal monitor workflow. Do not run a daily update or an actual inputs update
   as a smoke test: that would intentionally change additional pins.
4. Provide the new base→head series/diff and mechanical-history conclusion:
   one generated adoption commit, no superseded updates, no migration, and no
   rewriting of earlier merged commits. Lead applies the mandatory review skill's
   mechanical dependency exemption while retaining the whole-branch history
   gate and fresh approved integration proof.

No project documentation commit, workflow text change, version release,
deployment, machine reservation or lifecycle action is part of adoption. The
new updater becomes available when tools/workflows load the newly pinned shell;
it requires no system activation. Lock schema and persisted state are unchanged;
reverting the new confctl pin restores prior tooling behavior without a migration.
No ordering between A2/B2 is needed. Keep execution evidence in the owned package
records and existing session state; lead handles final remote heads and handoff.
