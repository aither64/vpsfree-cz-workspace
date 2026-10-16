# Provider failure diagnostics review packet

Status: completed committed deliverable; quick checks pass. Independent affected
final review is requested before long verification. No long checks authorized
by this packet alone.

## Outcome and scope

The final b8a6 local packaged recovery VM failed during provider switching, but
both original forward and compensation exceptions were replaced with generic
messages. A single fixture-only diagnostic used the exact original product and
passed with complete observation and no matching raises. The original failure
was not reproduced; its cause remains unproved. The accepted amendment fixes
that demonstrated loss of evidence and the VM's delayed failure reporting.

Architect-owned accepted brief: design.md, "Provider failure diagnostics
addendum, 2026-10-15". Investigation, causal limits and evidence comparisons:
recovery-check-investigation.md. Exact-package diagnostic evidence:
recovery-diagnostic/run/result.json, run/provenance.json and run/check.log.
Original failed evidence: runtime-amended-flake.log/status. Older passing package
evidence: runtime-integration-final.log/status. Preserve all original results.

Allowed amendment paths:

- libexec/workspace-codex-providers.rb
- test/workspace_host/codex_provider_test.rb
- nix/tests/session-recovery-boot.nix
- docs/codex-providers.md

Acceptance: bounded failure-only safe stderr records distinguish forward and
recovery errors, fixed local step and already-observed readiness facts. Unknown
or unavailable fields stay explicit. Diagnostic formatting/sink failure cannot
change compensation or state outcomes. Expected failure and reboot cases in the
original VM remain covered; unexpected terminal failure reaches the assertion
promptly, with bounded fixture evidence. No new probes, per-poll logs, product
TracePoint, general logging framework, speculative provider repair or changed
notification behavior.

## Review routing

Overall risk: high, because this code owns host process switching and recovery
and errors can contain secrets. General, architecture/repetition,
scope/proportionality, and risk/compatibility lanes apply to the amendment.
Retain reviewer0 with saved GPT-6.1 Sol/xhigh/read_only settings, after verifying
current same-session identity and eligibility. The completed substantive amendment is committed and quick checks pass.
Reviewer reads the
mandatory-change-review skill and all four lane references, directly, without
nested agents. Previously reviewed unchanged notification lanes need no rerun.

Inspect the complete current runtime feature series and migration provenance as
well as the affected patch. The existing one logical notification feature commit
b8a6be26a75347dcc9ec0fd1330dff886e47c93f stays intact. The new independently
reviewable provider-diagnostics behavior belongs in one separate logical commit;
no fixup or repeated dependency/pin stream should be retained. The exact completed head and evidence are recorded below.

## Compatibility and consumers

The provider implementation and owning guide are in dev-workspace, selected by
the workspace user profile and vpsfree-cz-configuration host module. Current
published runtime is b8a6be26a75347dcc9ec0fd1330dff886e47c93f; workspace is
e6aaa9c76ff3a0cb1d9dacca876c496e7e639b3f and configuration is
c4fb5da44733cb9a83e61428afe604a034b1946b. Those pins still select b8a6 while the
amendment is unpublished. Final downstream pin/history refresh remains separate.

Preserve ownership proof, locks, native/service order, readiness deadlines,
health retry, restart policy, terminal restoration and recovery fencing. No new
state field/schema, operation stage, receipt, API, protocol, stdout success
contract, external dependency or Codex pin is intended. Stderr diagnostics are
additive; older state and helpers remain compatible. No migrations. No version
of this amendment has been merged, released, deployed or externally consumed;
disposable diagnostics are evidence fixtures, not supported state predecessors.

User authorizes implementation, verification and coordinated aitherdev deployment
through vpsfree-cz-configuration. Default-branch merges, session lifecycle actions
and reservation release are not authorized. Foreign machine review ownership
must not be bypassed. Passing new diagnostics verification cannot establish the
cause or repair of the original failed b8a6 run.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/

## Exact completed packet and lead verification

Runtime base: ba8669b14536f72b559abc912bba8eac430111e4.
Existing feature: b8a6be26a75347dcc9ec0fd1330dff886e47c93f.
Final local head: bd60e37064ec4811a4686392bc9e83f0729ebcc1.
This is the feature's direct successor, with a clean registered runtime worktree.
The final diagnostics commit is unpublished; publication is held for review.

Complete series, both full commit messages/parents:
runtime-final-with-diagnostics-series.txt. Complete 40-path inventory/stat:
runtime-final-with-diagnostics-stat.txt. Full current branch diff:
runtime-final-with-diagnostics.patch (SHA256
ae4b2eb94b6257fed90007af0c9fd4ffbda0e8adfcd7f3d02680cbd77408e306).
Affected four-path delta: provider-diagnostics-final.patch (SHA256
f2ec11feb03cbfdad99f18e80550cb699494e72eff27d334cfb7dee97a93e91b).
Detailed quick commands, failure-path contracts and migration/history provenance:
provider-diagnostics-inventory.md and provider-diagnostics-freeze.json.
Lead independently verified exact head/parent/cleanliness, two-commit range,
four-path delta, all frozen artifact hashes and both byte-for-byte Git patches.

Lead full focused command, declared runtime environment:
`ruby test/workspace_host/codex_provider_test.rb`.
PASS20 cases,185 assertions,0failures/errors/skips,1.118786s,seed38199.
Evidence: provider-diagnostics-lead-ruby-final.log/status. Member independently
ran19cases/183assertions excluding only the unchanged real Unix-socket case
unavailable in its sandbox; the full lead run includes it. Source/test Ruby
syntax, Nix fixture parse, staged/final/full-branch diff checks pass per packet.
Only approved provider-guide wording changed after the final Ruby run; lead
checked the committed prose. Main-agent writing/Humanizer pass complete.

Full branch retains the previously independently reviewed initial notification
schema1/optional strict receipt lineage and no migration files. See
amended-final-inventory.md and amended-composition-review.md. The new diagnostics
commit changes no persistent state, dependencies/vendorHash, flake or Codex pin.
Review its proportionality and safe failure isolation as substantive new work;
do not treat the prior runtime review as reviewing this amendment. Explicit
whole-branch history/no-migration conclusion is required. Do not rerun unchanged
notification/provider-allowlist lanes or long checks merely for confirmation.

Documentation changed: docs/codex-providers.md, beside recovery instructions;
existing README provider-guide link remains the entry point. Temporary failure
logs, investigation rationale and individual rollout decisions stay in session
records. No own activation has occurred; no new state-consumer boundary exists.
