# Private PID namespace persistence-barrier review

Related source review before post-review native execution. This is not final
release readiness: required logging choice, exact consumer repins, assembled
package/resources, actual managed VM and live canaries remain outstanding.
User authorized implementation/deployment, but not default-branch integration.

## Outcome and finite scope

The accepted automatic New session feature keeps optional custom naming, dated
48-character slugs, deterministic fallback, durable identity/replay, upload
ownership and preparation recovery. Latest user chose model naming, disabled
file/network actions and immediate question rejection. Fixed gpt-5.5/low static
catalog child design was independently reviewed; its production/API/policy
code remains unchanged in this delta.

Latest native run at provider1be failed persistence after successful ordinary
inference/eligibility. Its snapshot owner was neither recorded control root nor
utility IDs; actual writer remains unattributed. Pinned source shows ordinary
turn completion does not join its memory pipeline/detached shell/MCP helpers.
Killing only leader groups cannot prove whole-home baseline quiescence. The
architect's accepted design.md supplements select a bounded fixture-only phase
correction, not a product process-management framework or a store exception.

Delta pid-boundary.diff changes only provider codex/ephemeral_integration_test.go
and main-owned docs/reference.md. Existing USER|NET|MOUNT clone/reexec gains PID;
Go test child is namespace init. Before native launch/signals require internal
marker, PID1/PPID0, distinct well-formed captured outer namespace, fresh private
proc with self=1 and matching init namespace. Proven owner rechecked before
every namespace-wide signal. No host fallback, process scans or marker-only kill.

Stop is serial: fence diagnostic generation, reject active utility, drain/hold
diagnosticMu so external helpers cannot start; guarded kill(-1,SIGKILL), finish
BOTH existing single Cmd.Wait owners through reusable cached results; then
Wait4(-1,WNOHANG|WALL) orphan drain. Only ECHILD proves empty; zero does not.
Unexpected direct waits/signals/reaps, missing ownership or fixed total2s
budget fail before restart/seed. No competing wildcard reaper or new init
service; private namespace init exit provides final containment on failure.

Original ordinary inference/eight eligibility controls remain before one stop/
join/restart. Keep original deny count fixed, exact same native profiles/home/
config/catalog, reopen same ordinary client options and persisted thread/read
only. Insert unchanged timestamp1 seeds once, verify exact seed fields, capture
one immutable persistence baseline. Fresh-MCP restart likewise uses persisted
read without starting ordinary writers. No reseeding/restoring/rebaseline,
changed seed age, separated utility home, ignored store/table or deadline/tool/
SQL/marker/egress weakening. Native logger remains strict and fails if retained
utility input/identity is found; pending user question is not consent.

New pure guard/wait tests are under ^TestEphemeralIntegration. Separate
^TestEphemeralNamespaceOwnershipIntegration$ is a post-review non-model native
control: two owned leaders, setsid descendant and adopted orphan, both direct
waits, positive adopted reaps, ECHILD, init survival, second start/stop cycle.
Internal TestEphemeralNamespaceOwnedHelper is not a standalone quick selector;
it fails absent private prerequisites. The full TestEphemeralProtocolIntegration
remains post-review, exact candidate/source/hash/ip/nft/sqlite prerequisites,
existing utility10s and fixture180s budgets. No actual new native pass exists.

## Committed series, consumers and compatibility

All four trees clean. Read branch-inventory.md and linked complete final/own
incoming diffs. Exact source checkpoint:

- codex-web base4c170393a96ed0a6ac2e43488d073f6fcab36132,
  headde874bc39553f8955cecdfaaeb4216959b40bd3c.
- dev-workspace base924c0ec28c41dd8b56aaf17f2212b302ca614899,
  head87eb917f50986d5206a08b3355837800a03e4529.
- vpsfree-dev-workspace base8f8d8ecf5031c40d3e4a4ee2e9425721fc035800,
  head2e3733ade1bac712f0b852d1960a681e5bca5076.
- workspace basea51fa51e2e2503ce658003f75b77a5be1ff6c042,
  head725db6717a82524776f1a687ae9ff96515168b79.

One provider owning helper/test/documentation unit introduces the final design;
obsolete incoming Luna/V8 and empty-file paths are folded away. New PID fixture
fix is folded there, pre-correction1be retained in backup. Runtime has focused
production units, separate dependency revision unit and separate managed
verification unit87eb. Earlier reviews and managed narrow socket correction
reconciliation are in static-profile-review.md/managed-child-review.md.

No new migrations. Exact externally consumed runtime4ef and extension399
remain ancestors and are unchanged; schema1/policy3 and maintenance/storage
lineage remain supported. New preparation version1 records are additive files.
No production/persistent/public API/CLI/native model/binary/policy/team/host
module changes by this delta; extra PID/proc prerequisite is explicit test only.
Existing shutdown/rollback contracts remain those recorded in plan/project docs.

Provider owns RunEphemeralTurn; runtime session_namer.go is direct consumer;
extension consumes runtime mkPackage, assembled workspace consumes extension.
Imports/pins/adapter code are in companion worktrees. Runtime still pins oldd371
in committed Go/flake files and uses an explicitly local temporary modfile for
source quick checks. This is a source checkpoint, not a coherent releasable
package; final dependency publication/repins/resources remain separate work.

## Documentation and quick evidence

Main reconciled provider reference.md namespace/baseline/control instructions,
applied vpsfree-user-facing-writing/humanizer guidance, inspected prose against
source. Other feature/operations docs from fixed source review remain unchanged.
Design rationale/individual execution limits are in design.md/state.md and
pid-boundary-report.md. Prepared managed-child-smoke.nix remains independently
reviewed, not executed. No code change is hidden in documentation.

Parent read full delta, gofmt and diff --check passed. Owning cached Nix supplies
Go1.26.7; TMPDIR=/tmp/GOWORK=off/-mod=readonly explicit. Command:

    go test -mod=readonly -tags=codex_integration -race ./codex \
      -run '^TestEphemeralIntegration' -count=1 -json

14 top-level groups/122 passing test/subtest events, zero failures/skips,2.827s;
raw /tmp/automatic-session-slugs-pid-boundary-quick.jsonl. This selector executes
no namespace/control/model/native fixture. Tagged file SHA:
fcd317b7aeb411e9f6ea840ac58146e4f34dc4e359989ceffeccfa1004c2120c.
Earlier fixed-profile schema/API/adapter checks remain qualified at their exact
heads; no unnecessary broader rerun for unchanged production code. No declared
hook framework; normal hooks not bypassed. All intended delta committed.

## Reviewer assignment and report

High risk: namespace-wide signal/reaping ownership, host process boundary and
whole-home persistence proof. Same independent retained reviewer0,
gpt-6.1-sol/xhigh/read_only, no fallback/override. Cover all affected lanes:
general; architecture/repetition; scope/proportionality; risk/compatibility.
Read mandatory-change-review skill and all corresponding references in full.
Inspect committed delta, design, tests, local AGENTS, complete series/final diff
and actual consumers. Assess the positive proof and fail-closed boundaries,
including no host-wide kill and no wildcard stealing direct Wait status.
Trusted local operator assumption applies; do not expand into hypothetical
compromised-operator filesystem containment.

Return findings ordered Blocking/Important/Advisory with lane/file/commit
references, concrete rationale and smallest correction. Explicitly conclude
whole-branch history/obsolete approaches and migration lineage, including no
migrations. Separate source conclusion from still-unexecuted native, package/VM
and logging gates. No tests, edits/fixes, Git/pins/lifecycle/deployment, nested
agents or requested rubber stamp. Report via report_to_lead/final; parent saves.
