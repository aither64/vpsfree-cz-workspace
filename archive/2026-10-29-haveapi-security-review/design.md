# Defensive security regression review design

## Scope

Audit the exact published HaveAPI range
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0..ae46cf27a9afb6558d386c293cec7231dd6c423d`
for introduced security regressions and, following the user's later scope
expansion, every confirmed pre-existing security bug found in the same reviewed
boundary. The five commits are reviewed as a whole, with unchanged code read
only where needed to establish reachability, policy, escaping, request lifetime,
cache lifetime, and base-versus-head behavior.

## Interfaces and files

Primary boundaries are the Ruby server's Rack/Sinatra documentation dispatch,
documentation renderers/templates/assets, OAuth and session/request identity
handling, metadata/authorization description filtering, parser/error envelopes,
and sample/client literal generation changed by the range. Repository-local
spec helpers and synthetic fixtures are the only execution interface.

Existing tracked repository files remain read-only. Confirmed evidence is added
only beneath the isolated checkout's `vulnerabilities/VULN-XX/`, one issue per
directory, with an executable local regression example and a report citing the
final exact source lines.

## Security invariants

- Documentation and API descriptions expose only resources, actions,
  parameters, and authentication information visible to the current requester.
- Requester identity, OAuth state/session data, rendered documentation, and
  cached descriptions cannot cross request, user, privilege, API instance, or
  origin boundaries.
- Hostile API metadata, sample data, descriptions, paths, parameters, and
  server responses cannot become executable HTML or JavaScript in the
  documentation UI.
- Dispatch and parser failures remain controlled protocol errors without policy
  bypass, sensitive disclosure, unsafe mutation, or request-process failure.
- Generated examples preserve literal values and escaping in each target
  language; formatting changes cannot silently change request semantics or
  create executable interpolation.
- Optional OAuth documentation behavior does not weaken authentication,
  authorization, redirect/origin checks, session isolation, or default-deny
  behavior.

## Investigation boundaries

For each changed path, trace attacker-controlled input to its final policy,
rendering, cache, parser, or generated-code sink. Compare against the base when
behavior is suspicious. Treat an exception or formatting error as a security
finding only when local execution demonstrates a relevant leak, bypass, unsafe
state change, persistent cross-request effect, executable injection, or
meaningful denial of service.

Do not inspect unrelated subsystems, another session's artifacts, live systems,
credentials, dependency updates, or framework redesign opportunities. Do not
apply fixes or alter existing source/spec files.

## Compatibility, deployment, and recovery

This is a read-only source and local-fixture review, so it introduces no API,
schema, persistent-state, deployment, or mixed-version change. The audited head
and base remain untouched. Recovery is limited to stopping and reconciling this
session's local test processes while retaining the registered worktree and
uncommitted evidence. No merge, deployment, release, or lifecycle action is in
scope, and the session stays open.

## Acceptance criteria

- Native provider/model/effort and exact session binding are recorded and match
  the request before source analysis.
- The isolated worktree resolves to the requested head and tree; the complete
  five-commit series descends from the requested base.
- Every requested security boundary is inspected, including the related
  unchanged code needed to decide reachability and introduced/pre-existing
  classification.
- Every confirmed finding has a locally successful, reproducible security PoC
  and a skill-compliant report under `vulnerabilities/`; unsupported leads are
  omitted from findings.
- Final reporting includes severity, exact source lines, prerequisites, impact,
  command/result, range classification, remediation, concrete coverage, and
  honest limits.
- Tracked source is clean and all owned check processes are reconciled at
  handoff.

## Checks

Quick checks verify repository identity, exact commit/tree/range/series, local
instructions, hooks, clean tracked source, and the declared Nix/Ruby entry
points. Targeted checks exercise suspicious paths with existing local helpers or
small synthetic fixtures. Potentially longer repository checks are run only
when they directly resolve a material lead, with a bounded target and stop
condition; no external or live request is permitted.

## Corrected-head re-audit boundary

The second pass compares direct parent
`ae46cf27a9afb6558d386c293cec7231dd6c423d` to corrected head
`ddf836fbb33ec6f920c3edfd9a4a53c2c2eb494b`, expected tree
`30efb19e02a756036771767745a9858fe968f95b`. It independently verifies that each
previously executable payload becomes one literal argv token without changing
the documented CLI/curl request semantics, and that the centralized quoting is
applied exactly once to all dynamic shell tokens. The adjacent CLI-help
formatter is in scope only to resolve the concrete copy/run injection lead; no
broad client audit is added.

Acceptance for this pass requires unchanged original PoCs to stop creating
markers, positive argv/JSON preservation checks for the fixed renderers, local
proof for any remaining/new issue, exact corrected source identity, clean
tracked source, and reconciled owned processes. A fix that merely prevents the
marker while corrupting the intended argument does not satisfy the invariant.

## Second corrected-head boundary

Compare `ddf836fbb33ec6f920c3edfd9a4a53c2c2eb494b` to final corrected head
`aee093cd3387c261570067e58b7f1e16029e3619`, while verifying its direct parent
`a3f522e509faaf9da34d9e87c7f7e9246c76bd6c`. Acceptance requires all original
VULN-01 through VULN-04 execution payloads to remain inert, exact CLI/curl argv
and request JSON, visibly preserved hostile response text, every physical
response line remaining a shell comment in the retained combined code block,
and the real Copy control preserving that same safe text. Any new finding still
requires its own locally triggered PoC and report.
