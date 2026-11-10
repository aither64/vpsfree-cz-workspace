# Final refresh review, 2026-11-02

One Important documentation finding; no Blocking findings or additional Advisory
findings. Scope is proportionate to the user's rebase and deployment-documentation
request. Address R1 before treating the refresh as accepted and proceeding under
the review workflow. The lead has agreed to the narrow wording correction, which
was not yet applied to the frozen reviewed head.

## R1: Configuration rollback does not necessarily revoke dedicated API access

- Severity: Important.
- Lanes: General; Risk and compatibility.
- File: `docs/operations/prometheus-query-access.md:325`, in conjunction with the
  new prior-generation rollback procedure at lines 262–271.
- Reviewed head: `d03e944a992d006e0eb0bf2400d182eb22c5a340`.
- Commit context: the unqualified sentence is inherited in proxy commit
  `46bddfcdb0b5e1bfcc95edc98f1f8aa1f4c5cd21`; the new operator rollback contract
  is added by `d03e944a992d006e0eb0bf2400d182eb22c5a340`.

The page says, "Configuration rollback removes dedicated API access." The new
procedure restores the operator's recorded previous deployed generation. The
user may already have deployed the previously published feature head
`d07b4251172020472b21e8830e92b023849d543f`; its proxy policy contains these same
dedicated routes. Rolling back to such a generation preserves the routes and
accepts the runtime credential. An operator relying on the sentence as assurance
that rollback removed access could leave that access active.

Make the condition explicit and preserve the following guidance about runtime
credential independence, revocation and recovery. The lead's accepted wording is:

> Configuration rollback removes the dedicated API only if the selected generation
> lacks those routes. A prior deployed generation may already include them;
> explicitly revoke the runtime credential if rollback must also remove access.

This requires a narrow prose correction, not a new mechanism or test framework.
The lead can inspect the exact amended diff and required hooks under the skill's
narrow-remediation policy; another full review is unnecessary for that correction.

## Identity, settings and reviewed range

Reviewer: retained independent `reviewer0`, purpose `review`, saved
`gpt-6.1-sol` / `xhigh`, `read_only` access. Same-session roster and thread
`01a15e5b-e473-79c1-9bee-3262c72c5792` verified. No setting override, fallback or
nested agent was used.

`dev-session current` from the bound session tracking directory printed
`2026-10-21-aitherdev-observability-access`. Both identity environment variables
were absent, consistent with the trusted developer binding. Rechecked before
writing this report.

- Repository/worktree: this session's `vpsfree-cz-configuration` worktree.
- New base: `c040c14cdbacc07998700b524996a89306188d7f`.
- Frozen final head: `d03e944a992d006e0eb0bf2400d182eb22c5a340`.
- Prior reviewed/published head: `d07b4251172020472b21e8830e92b023849d543f`.
- Old base: `38e7c837893695999e588a73f5d2a0088b8257b1`.
- Project HEAD matched the packet, with clean worktree and index.
- Overall risk remains High: authorization plus root-operated maintenance,
  secret provisioning, configuration rollback and changed dependency inputs.

Read the current mandatory-change-review skill and General, Scope and
proportionality, and Risk and compatibility references. Applied scope review first,
then operator correctness and compatibility. Read current workspace/repository
guidance and applicable procedures, the refresh packet, design/state/plan context,
complete series/final diff, range proof, documentation delta and refresh evidence.
Reused prior unaffected architecture conclusions from [review.md](review.md) and
[review-followup.md](review-followup.md).

## Scope and proportionality

The actual request is to rebase the registered configuration feature and include
deployment documentation specific to this repository. The new milestone changes
only the two existing operator pages: +152/-34 lines. No helper, system package,
application behavior, generic provisioning framework or new test infrastructure
was introduced. Reusable deployment and recovery steps belong in these linked
configuration-owned operations pages. Removing development-session orchestration
from them improves their usefulness to an operator.

The maintenance trap addresses a concrete risk: leaving ingestion stopped when
inventory, review or apply fails. The transient Python setup supplies an existing
recipe's undeclared runtime prerequisite using native Nix. Both are bounded parts
of the requested operator guidance. The change does not justify broader hardening,
a new deployment system or re-auditing unchanged feature components.

## General and operational assessment

The docs identify exactly `cz.vpsfree/containers/prg/int.log` and
`cz.vpsfree/containers/prg/proxy`. They retain previous local builds/closures before
building, use explicit names for dry activation and switch, and stop if the
previous deployed configuration has no matching retained local build. They do not
require monitor or aitherdev system deployment.

Inspected the checkout-pinned confctl source at revision
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`: CLI declarations accept both generation
listing switches and the documented deployment actions. `Cluster#find_generations`
resolves names through `Generation::BuildList`; remote profile numeric IDs are
not interchangeable with those local build names. Combined generation listing
can correlate local and remote entries by toplevel. No deployment or remote
generation command was executed by the reviewer.

The logger maintenance block installs cleanup before either stop. Its EXIT trap
captures the failure status, attempts ingestion and timer restart independently,
and returns failure if either restart fails. HUP/INT/TERM exit through cleanup.
It retains the private, exclusively created inventory and explicit operator
approval. The text requires a fresh inventory after ingestion resumes and gives
manual restart commands for failed cleanup or uncatchable termination. This is
appropriately described as attempted recovery rather than an outage-free
transaction. Existing metadata-helper refusal and partial-apply semantics remain
accurate.

The Python preparation derives the immutable nixpkgs revision from the selected
checkout, exports only a nonsecret reference, and checks remote Python/htpasswd
availability before generating the credential. The root flake's `nixpkgs` input
follows `nixpkgsStable`; the proxy selects the corresponding stable channel.
The credential recipe uses that same reference for transient remote Python.
The existing secret flow remains in memory/stdin and private staged files, with
no credential value in Git, Nix expressions, argv or environment. It preserves
the documented possible server/client mismatch on partial failure and its
recovery. This refresh adds no persistent Python package or replacement auth
mechanism.

Bounded SSH/HTTPS, human access, ingestion/exporter, new-host and ordinary rotation
acceptance remain documented. Destructive production probes are not prescribed.
The manual root-key entry is accurately described as user-owned and conditional
on whether it remains present. Apart from R1, no operator correctness or prose
finding was identified.

## Complete history, replay and migration conclusions

The complete base-to-head series has exactly three logical commits:

1. `5e15c92cb8a4cf42a6e97f9d2a447fef1734febf`: logger implementation/tests/docs.
2. `46bddfcdb0b5e1bfcc95edc98f1f8aa1f4c5cd21`: proxy implementation/tests/docs and
   shared registration.
3. `d03e944a992d006e0eb0bf2400d182eb22c5a340`: the subsequently requested operator
   deployment/recovery documentation milestone.

The third commit is a separately requested, independently reviewable deliverable,
not an obsolete iteration or fixup stream. Its separation from the previously
published implementation is justified.

Independently compared the actual range-diff: the logger replay is equal; the
proxy difference is only surrounding upstream MkDocs context. All implementation,
helper and fixture file contents are byte-identical to the prior reviewed head.
README and flake registration are identical too; MkDocs retains the intended
feature additions against its updated baseline. The replay tree is
`fc83f713cc326769c86547b6318ade731f6563f4`, matching the supplied native
reconstruction proof; final tree is
`a6c98ebe3389322b22ea9b7d1f4055d51b8d9758`. Actual Git diffs exactly match both
supplied full final diff (1,812 lines) and documentation milestone delta (269 lines).

No obsolete feature approach, transitional shim or redundant fixup remains in
the complete final series. The native per-action remote log creation properties
and legacy local-selector defaults still serve their distinct native contexts;
neither is an abandoned compatibility path.

There are no repeated dependency/channel/input/generated-artifact update streams
in this feature series. Upstream input changes arrive through the new base; the
feature commits do not select dependency revisions or change lockfiles against it.
There are no superseded feature pin updates requiring consolidation.

**No migrations.** No database/TSDB/log-format migration or transitional migration
lineage is introduced or rewritten. The explicit historical metadata procedure
retains its existing contract. The old feature was published and user rollout
since then is unknown: this review does not infer that it was never deployed or
externally used. Existing persisted permissions and runtime credentials remain
supported across the refresh; their recovery is independent of Git rebasing.

The unaffected architecture conclusion is reusable because implementation and
component interfaces are unchanged, and the new docs use existing native tools.
R1 is inside the supported rollback contract, not a request for optional redesign.

## Verification and acceptance limits

The packet records successful current-input quick derivations, required hooks,
shell/Python parsing, links, and synthetic cleanup success/failure/signal cases.
Reviewer independently inspected source, Git proofs, lock identity and the pinned
confctl implementation, using offline source-path evaluation only. No documented
runtime/deployment command, long test/build, live request or actual credential
operation was executed. No source, index, branch or lifecycle mutation was made;
only this report was written.

The upstream baseline changes nixpkgs and other inputs. Prior successful runtime
and host-build evidence remains valid for its old inputs, not proof for this
refresh. The lead's planned changed-input proxy integration, logger VM and exact
logger/proxy builds remain pending at this review checkpoint. Complete those
after the narrow R1 correction is inspected under the remediation policy.

User-owned deployment and its current state remain unverified. The operator must
identify the actual deployed generation, retain the matching rollback build,
inspect historical metadata/ACLs and required readers, and verify runtime secrets,
public TLS, live access, ingestion/exporter behavior and ordinary rotation as
applicable. Runtime revocation does not retroactively cancel executing requests;
open SSH sessions also need separate handling for immediate revocation. The
accepted ordinary-shell/unredacted-data and API resource-limit boundaries from
the earlier reviews remain unchanged.

The lead has accepted R1 and plans to amend only its wording, preserve credential
independence/recovery guidance, and verify the exact diff/hooks. No merge,
provisioning, deployment or session lifecycle action is authorized by this report.

Session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-21-aitherdev-observability-access/>.
