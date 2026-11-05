# Final independent review

## Findings

No Blocking findings. Three Important findings require a fix or an explicit
recorded decision before proceeding. These conclusions apply to the exact
committed ranges below, not to subsequent fixes or deployment pins.

### R1 — Important — Retired registrations permit an unsafe predecessor transition

Lane: risk/compatibility. Runtime commit `85760a7a` and core `08a0df82`.

`libexec/workspace-session-services.rb:181-195` decides that fully retired
registrations require no service capability. However, its call to `load_state`
first requires a current `work/SLUG` or `archive/SLUG` tracking directory
(`:143-170`). `libexec/workspace-host:3010` consequently admits a package without
either new capability after the last service retires.

The admitted predecessor at `c2182254` supports deleting that session. Its
`preserve_removed_state!` moves tracking into private removal recovery, and
`finalize_removal!` clears the removal journal. It knows neither new registration
file, so both remain at their original paths. On the next forward activation,
the candidate's `require_no_unfinished_lifecycle_operations!` calls the new
requirements inventory; `tracking_owner` finds zero ordinary tracking roots and
raises `ambiguous service tracking identity`. Preparation, candidate activation,
and other host operations using this inventory now refuse. Retrying delete
cannot resume its already completed journal. Reusing the slug instead produces
an identity mismatch. This is a normal allowed lifecycle sequence, without local
filesystem attacks or live services left to protect.

The host tests cover a stationary retired fixture only, and the exact predecessor
Store/Policy fixture covers parsing/inactivity, not predecessor deletion. The lead
confirmed that no other evidence covers this sequence.

Smallest recommended fix: require matching service capabilities while any
registration evidence remains, including fully retired records; keep the
never-registered path free of this gate. Document the persistent compatibility
boundary and update both preparation/activation tests. Do not add speculative
reconciliation for historical deletion state. An alternative is a narrowly
defined, durable retirement/evidence transition that demonstrably survives the
real predecessor's delete and subsequent forward activation; that alternative
needs its own focused compatibility review and proof.

### R2 — Important — First conversation creation strands a threadless service registry

Lane: risk/compatibility, with general correctness. Runtime core `08a0df82`.

`libexec/workspace-session-services.rb:279-283` permits managed launches in an
ordinary threadless session: `require_ordinary_manifest_ready!` explicitly accepts
that state. The service marker records `retained_thread_id: null`. Existing
documented behavior then permits an explicit `dev-session start` with an initial
request to create that tracking-only session's first conversation
(`docs/dev-sessions.md:58`; `libexec/dev-session:1195-1208`). That start path does
not check or transition registered-service ownership before publishing the root.

After successful start, every registry load compares the new root with the saved
null root and raises `service session identity changed`
(`workspace-session-services.rb:168-170`). The same tracking directory and session
now cannot list or stop their services, archive, delete, or pass host package
checks. A valid running service can be stranded by an ordinary supported command.
Retiring the service before start does not solve the retained-marker mismatch.
The new rootless automatic-archive fixture does not exercise first conversation
creation.

Smallest acceptable boundary: reject first-root creation under the existing
session/creation locks before creating its journal or native root whenever that
creation would invalidate retained service evidence. Give an actionable error
and document that the conversation must be created before service registration.
Keep ordinary threadless launch/archive support. A supported same-directory,
first-root transition is also possible, but must bind the existing creation
journal and update ownership durably across interruption; do not generally
accept changed roots or silently rewrite ownership during reads. Test both live
and fully retired registration cases, no side effects on refusal, and continued
stop/archive/delete usability. Inspect the affected contract after any design
change.

### R3 — Important — Existing navigation test still requires the removed sidebar anchor

Lane: general, verification. UI commit `fac02494`.

`portal/internal/web/coordination_test.go:46`, in
`TestOperationsNavigationDoesNotReadOrEmbedStatus`, still requires literal
`href="#reservations"` in the session page. The changed
`portal/internal/web/templates/session.html:29` and `:78` replace that sidebar
anchor with the Resources parent and a Reservations button. No template now
contains the required anchor. This test will fail in the full Go/package suite.

The final smoke regex `^Test(Service|Resource|InitialLifecycleReceipt)` excludes
this existing `TestOperations...` test, so the reported passing smoke does not
resolve the failure. This finding is established by inspecting the test and
template; the reviewer did not run tests.

Update the existing assertion to verify the Resources parent and nested
Reservations navigation, retaining its no-embedded-coordination-status,
observation-identity, and Operations-order assertions. Run that named quick test
before the long package campaign.

## Reviewed identity, scope and method

Reviewer: retained `reviewer0`, thread
`01a19ca7-8da1-7e63-852f-72d8332c553a`, `gpt-6.1-sol`, `xhigh`, `read_only`,
purpose `review`; no override, fallback, nested agent, or substantive authorship.
`dev-session current` printed exactly
`2026-11-02-session-temporary-service-cleanup` from its tracking directory. Both
environment markers were absent, and the exact trusted developer binding matched
the workspace `/home/aither/workspace/ai/vpsfree.cz`. The live same-session roster
confirmed the retained settings.

This is the mandatory final review of completed committed substantive work.
Overall risk is High: persisted ownership, native process/cgroup shutdown,
destructive file-removal order, receipts/recovery, package compatibility. Read the
mandatory-change-review skill and all four references in full: general,
architecture/repetition, scope/proportionality, risk/compatibility. Consulted
workspace procedures, runtime AGENTS, owning documentation, plan/state/design,
review packet, source history/diffs, adjacent lifecycle/creation/host/cache code,
tests, and submitted quick-check receipts.

Scope/proportionality was assessed before detailed hardening. The recorded user
amendments authorize managed registered services and Resources/Team counts;
unregistered discovery, adoption and migration gates remain excluded. The
46-file, 3,749-insertion runtime delivery includes extensive tests and the new
779-line Ruby owner; this is substantive lifecycle work rather than a small UI
edit. The same-day record shows delivered independent UI, core and integration
milestones and completed quick checks, rather than only planning churn. No
additional subsystem is needed to resolve these findings.

The conventional transient-user-unit approach fits the requested boundary.
Systemd owns stop escalation and cgroups; there is no PID/port scanner,
resource-plugin framework or terminal-lifetime dependency. The first-registration
marker and prelude have concrete loss-detection and pre-prune ordering purposes.
One Ruby owner validates/writes private state; host checks use that owner. Go
consumes the allowlisted public service projection and has a bounded subordinate
prelude reader for its existing lifecycle receipt machinery. Resources reuse the
existing cache, detail refresh and coordination ownership readers. No separate
architecture/repetition or scope finding was established.

The trusted local operator assumption was preserved. Inspection covered ordinary
I/O failures, concurrency, exact workspace/root/incarnation, remote input
validation, escaping, secret-safe projections and recovery. No hostile-local-
operator containment, unregistered-service inspection or additional service
controls/proxy/links are requested.

## Whole-series, consolidation and migration conclusion

Runtime repository/target: `git@github.com:aither64/dev-workspace.git`, `master`.
Reviewed complete range
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79..85760a7a673f3ec072c7c16dc88006e89214d448`;
head tree `26177eafea54f4427af09b87daad1540ac3e5feb`. Independently inventoried:

1. `fac02494b5b41d0d4a6f299f083e67f4ea3a799e` — Resources navigation/counts.
2. `08a0df822b4a01cef25207ba663df861b2b4006d` — registered service owner/lifecycle.
3. `85760a7a673f3ec072c7c16dc88006e89214d448` — dependent portal/package integration.

Workspace repository/target:
`git@github.com:aither64/vpsfree-cz-workspace.git`, `master`. Complete reviewed
feature range
`ef09cf555332afebafb276e3ae54cc1f5ea6012c..c474bcc55b04459dd936d2e4d8bea358b2b84184`:
one `workspace: require managed launches for temporary services` commit, two
instruction files, 20 insertions/one deletion. Reviewed its full diff and commit
message. It does not expand lifecycle authorization.

The three runtime commits have distinct reviewable purposes. Supporting tests
and docs belong with their behaviors; dependent integration follows the owner.
I found no obsolete approach, fixup series or transitional compatibility path
remaining in these committed ranges. The abandoned extra activity dimension and
unconsumed draft schema rescue are absent. The test-only predecessor fixture
matches the exact predecessor source prefix plus its module closing line, after
removing its two attribution comments; it is not a runtime compatibility engine.

There are **no database migrations**. New local service schema 1 is introduced
directly. Per the packet's explicit provenance, no predecessor service schema or
intermediate feature version was merged, released, deployed, or externally
consumed. No transitional migration remains. Existing ordinary archive/removal/
revival journal schemas and saved policies were not changed. This clean migration
lineage does not cure R1/R2's lifecycle compatibility defects.

There are **no repeated dependency/channel/input/generated update streams** in
the reviewed ranges, and therefore no redundant pin commits to consolidate at
this stage. Runtime `flake.nix`/`flake.lock` are unchanged; independently checked
lock SHA256 `fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955`.
Workspace and configuration still select runtime `c2182254`; the extension at
`e4e7e95ed39bf514b33f8f8ae61ba9868de060ae` composes the generic runtime rather
than duplicating this feature. Configuration remains unchanged at
`c040c14cdbacc07998700b524996a89306188d7f`. Mechanical pins have not been created or
reviewed. Final complete streams/input graphs and any rewritten ranges still
need the promised explicit history/migration conclusion before branch readiness.

## Verification limits and disposition

Inspected `runtime-final-smoke.log` and its exact-head receipt: Ruby service
21 tests/243 assertions, host 4/59, complete cluster/session Go checks, focused web
checks, JS syntax and 16 browser-unit tests passed at the submitted head. The
earlier broader 130-test Ruby result precedes final source corrections and is
only evidence for its recorded snapshot. R3 demonstrates why the focused smoke
does not establish full-suite success.

No reviewer builds, tests, native service operations, source publication,
deployment, claims, lifecycle commands or application edits were performed.
Only this permitted report artifact was written. Real systemd/cgroup, packaged
CLI layout and tools, full browser/navigation behavior, package/host contracts,
extended lifecycle VM and CI remain unverified at the final head. In particular,
fake-manager success is not native TERM/KILL, descendant or unload proof.

Disposition: reconcile R1–R3, commit their owning fixes with focused quick
verification, then continue the required long verification workflow. Narrow
refusal/test corrections can be inspected directly without repeating unaffected
lanes. A new ownership transition or changed public compatibility design needs
only its affected lane checked by this retained reviewer. This review grants no
deployment, default-branch integration, archive/delete/stop or session-close
approval and does not declare the branch ready for use.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
