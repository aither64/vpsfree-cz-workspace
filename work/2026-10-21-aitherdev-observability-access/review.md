# Independent final review

No Blocking or Important findings. One Advisory finding below. The frozen
deliverable passes independent review for proceeding to the planned disposable
integration tests and affected-host builds. Those checks and deployment acceptance
are still pending; this report does not establish deployment readiness.

## Findings

### A1: Check both historical log reads independently

- Severity: Advisory.
- Lane: General, behavior and coverage.
- Commit: `7bd4be8d591bbf52492ed73fdab1140b8b1bf403`.
- File: `tests/log-reader-vm.py:51`.

The successful historical-access assertion runs remote archive `grep` followed by
messages archive `tail`, separated by `;`. The shell returns only the latter
command's status. A regression that leaves the historical remote directory or
archive unreadable can therefore pass this assertion when the messages archive
remains readable. The earlier negative read does not prove access after apply,
and the later ingestion/rotation checks use another host directory.

Use two checked SSH assertions, or join the commands with `&&`, so both reads must
succeed. Checking the expected marker in both archives would also make their
content assertions explicit. This is a focused test correction; inspection of
the reconciliation implementation did not identify a corresponding access defect.

## Identity and scope

Reviewer: retained `reviewer0`, purpose `review`, model `gpt-6.1-sol`, effort
`xhigh`, access `read_only`. The live same-session roster matches the thread-bound
identity `01a15e5b-e473-79c1-9bee-3262c72c5792`. No fallback or model/effort override.
The reviewer authored no implementation and used no nested agents.

`dev-session current`, run from the session tracking directory before inspection
and rechecked there before writing this report, printed
`2026-10-21-aitherdev-observability-access`. Both identity environment variables
were absent, consistent with the trusted workspace/thread binding.

Reviewed repository:
`worktrees/2026-10-21-aitherdev-observability-access/vpsfree-cz-configuration`.

- Base: `38e7c837893695999e588a73f5d2a0088b8257b1`.
- Head: `072f7e01f5000bfd43439c5ba27aee28cfe69b17`.
- Worktree and index: clean at review start; HEAD matched the frozen revision.
- Actual Git diff exactly matched all 1,630 lines of `final.diff`.
- Overall risk: High, because this introduces SSH/HTTP authorization, runtime
  credentials, root-operated file metadata changes, and rollback obligations.

Read the mandatory-change-review skill and all four lane references in full,
workspace/repository instructions and applicable procedure routes, plus the
packet, design, plan, state, complete final series and diff. Inspected surrounding
logger/proxy/monitor configuration, exporter ownership, administrator keys, flake
registration, fixtures and both operations guides. Pinned nixpkgs modules supplied
the actual nginx authentication and OpenSSH account/key contracts.

## Whole-branch history, streams and migrations

The complete base-to-head series contains exactly:

1. `7bd4be8d591bbf52492ed73fdab1140b8b1bf403`:
   `int.log: add unprivileged SSH log reader`.
2. `072f7e01f5000bfd43439c5ba27aee28cfe69b17`:
   `proxy: add dedicated Prometheus query access`.

The first commit contains the logger feature, its reconciliation helper, fixtures
and operations documentation. The second contains the independent HTTPS feature,
its fixture/docs, and shared flake/documentation registration. The ordering avoids
registering logger files before they exist. The split is coherent and independently
reviewable; tests and documentation accompany their owning behavior.

No obsolete unmerged approach, fixup commit, unused transition shim, or superseded
protocol remains in this complete series or final diff. The packet's earlier
unpublished commit identities are absent from the reviewed ancestry. Folding the
helper/rotation corrections into the owning logger commit was appropriate. No
released, merged, deployed or externally consumed intermediate version is claimed
by the packet, and none is needed to justify retaining an intermediate here.

There are no repeated dependency, channel, input or generated-artifact update
streams. No lockfile or dependency pin changes are present; the flake edits only
register checks. There are no redundant pin commits to consolidate.

**No migrations.** No database migration, TSDB conversion, log format conversion,
or transitional schema lineage is introduced. Consequently there are no migration
versions with merge/release/deployment/external-use provenance to preserve. The
explicit operator-run ownership/mode reconciliation is a metadata operation, with
its own inventory and recovery contract, and is not an activation-time migration.

## Lane assessments

### General

The implementation follows the accepted machine-key and dedicated-random-secret
design. It does not remove the user-owned manual root key, add source-IP auth,
change monitor raw-port access, introduce client mapping or add a custom wrapper.
Both features have fixtures derived from production configuration. The API fixture
uses permissive upstreams, so denied-request assertions test the proxy boundary
rather than depending on backend rejection. It covers both backend identities,
form bodies/query strings, credentials, method/path rejection, normalized paths,
limits, and authentication rotation on existing connections.

Logger coverage includes historical refusals, current/archive/new-host reads,
rotation, ingestion/exporter health, protected-file writes, effective SSH policy,
home key rejection, PTY and reverse-forwarding denial. A1 weakens one historical
read assertion. The remaining long checks have not yet established runtime success.

The guides are linked from README and MkDocs and describe reusable procedures,
security boundaries, preparation, failure recovery and rollback. They distinguish
prepared operations from live acceptance and keep the manual root-key removal
separate. Temporary verification/release evidence remains in session records.
No prose or documentation correctness issue requiring remediation was found.

### Architecture and repetition

The site configuration owns both access boundaries. Existing OpenSSH, rsyslog,
logrotate, nginx and curl mechanisms implement them; no runtime/provider API or
cross-project consumer contract changes. The current clients are the aitherdev
user's SSH/curl processes. Both monitor vhosts use one route/auth/limit generator
with separate upstream values, avoiding security-policy drift. Expected endpoint
lists in tests serve as independent contract assertions rather than a second
implementation of routing policy.

The logger helper owns one narrowly defined metadata operation. Descriptor-relative
opening, explicit scope, inode checks, ACL/mount/link refusals and a reviewed
inventory have a concrete operator-safety purpose. No unsafe duplicated security
rule, hidden extension interface or misplaced reusable component was found.

### Scope and proportionality

The account remains an ordinary unprivileged shell, as explicitly accepted. It is
not presented as a general filesystem or process sandbox. The implementation does
not add a generalized auth service, automatic secret deployment, database repair,
root-key management or speculative compatibility framework.

The helper's safety mechanisms are proportionate to root-operated historical
metadata changes. The inline provisioning example uses native tools and documented
operator inspection rather than introducing another installed subsystem. The
fixtures focus on owned authorization and permission behavior. No scope growth or
disproportionate abstraction requiring remediation was found.

### Risk and compatibility

The SSH Match block constrains key lookup to a root-managed file, public-key
authentication and the specified forwarding/PTY/tunnel/rc restrictions. A writable
home cannot supply unrestricted SSH keys. The account has only the reader group;
existing root/human key configuration is not edited. New remote directories/files
and logrotate replacements use root ownership with group read/traverse access.
Exporter pipe ownership and the existing ingestion/retention actions are preserved.

The helper refuses unsafe entry types, foreign owners/groups/filesystems, mounts,
hard links, ACLs and write/special bits. It compares the reviewed complete inventory
before mutation, revalidates identities during apply, and supports a no-op repeat
after a fully successful application. It deliberately requires quiesced root
writers. Partial application can require inspection and a fresh inventory; it is
not a transaction, as documented. No unprivileged write path into protected files
was identified inside that contract.

I investigated message-derived hostname traversal because rsyslog writes as root.
The pinned installed binary is rsyslog 8.2608.0 and contains its dynamic-filename
containment guard. Its [versioned upstream implementation](https://github.com/rsyslog/rsyslog/blob/v8.2608.0/tools/omfile.c)
derives the fixed directory prefix and rejects rendered paths outside it. This
configuration does not opt out. Together with the reconciled tree's protected
ownership and refusal of symlinks/mounts, the suspected lexical escape is not a
finding on this pinned revision. This is source/binary inspection, not a live probe.

Nixpkgs renders each non-null location `basicAuthFile` as active Basic auth with
that runtime file. Allowed API locations therefore replace the human password-file
selection without disabling authentication. Exact normalized locations plus raw
URI checks reject alternate path spellings; the rewrite stays in the same location,
preserves arguments/body and clears Authorization. The catch-all denies the new
prefix. Existing human routes retain their own auth. No source-IP or raw-port
bypass was introduced.

The fixed limit key is shared across both monitor vhosts and unauthenticated
requests, with the documented availability tradeoff. Limits apply to the dedicated
locations. Missing/wrong runtime credentials fail closed; no secret material is
generated by Nix. The provisioning example validates fixed destinations, generates
the secret in memory, uses stdin for hashing/SSH, and atomically replaces staged
files. Its possible server/client mismatch after failure and recovery are stated.

The two features can deploy independently. Old proxy configuration will not accept
the dedicated credential on human routes. No fleet-wide coordinated update or
persisted format compatibility layer is required. Credential and log metadata
changes persist independently of Nix generations; the guides correctly require
explicit revocation/recovery rather than assuming configuration rollback restores
them. Existing-reader preservation must precede permission rollout.

## Verification and residual limits

Reviewer performed read-only Git range/status/diff inspection, `git diff --check`,
quick Nix evaluation of the pinned tool/source and generated nginx configuration,
and AST parsing of the helper, both fixtures and both local/remote provisioning
programs. These checks passed. Inspected the pinned NixOS nginx/sshd/rsyslog/user
modules and the generated two-vhost nginx policy. No implementation, index, branch,
live service, credential or lifecycle mutation was performed; only this report
was written.

The packet records successful hooks, formatting, logger policy/syntax checks,
effective sshd Match policy, bounded helper checks and nginx syntax checks. Those
reported checks are not a substitute for the following pending verification:

- Run the planned disposable HTTP integration fixture, logger VM and affected-host
  builds after the lead handles A1. This review did not launch them.
- Live TLS/routing, runtime secret ownership/ACLs, actual historical log metadata,
  required pre-existing readers, ingestion and ordinary rotation need separately
  authorized deployment acceptance. No live service request or provisioning ran.
- The shell permits programs, home/tmp writes, outbound connections and ordinary
  log generation. OpenSSH forwarding restrictions do not turn it into a network
  sandbox. Logs and allowed metric/diagnostic data remain unredacted.
- An unauthenticated public client can exhaust the fixed API quota. Proxy read
  timeout is not a hard query CPU budget; these are accepted design limits.
- Runtime secret replacement is atomic per host/file, not a distributed
  transaction. New requests reauthenticate; executing requests and open SSH
  sessions require separate handling when immediate revocation is necessary.
- The user's manual machine-key grant for root remains until the user removes it.

The lead may verify a narrow A1 correction directly under the skill's remediation
policy. It need not rerun independent review for that assertion-only change.
No merge, deployment or lifecycle action is authorized by this review.

Session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-21-aitherdev-observability-access/>.
