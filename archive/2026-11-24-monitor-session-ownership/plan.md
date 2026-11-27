# Runtime monitor ownership and Pi coverage

## Goal

Investigate why an active Codex session lead can receive an ownership refusal
from the runtime monitor before launch. Separately check whether Pi sessions
expose an equivalent monitor and can resume their exact lead on a result.
The original incident details are retained in the conversation, not in Git.

## Affected repositories

Start with `dev-workspace` (monitor service, backend adapters and installed skill).
Inspect `codex-web` and Codex as dependency boundaries; no change there without
source evidence. For the aitherdev rollout, also use `vpsfree-cz-configuration`
for the system pin and the `workspace` repository for the user-profile pin.
No vpsAdminOS changes or repeat of the reported check.

## Approach

Trace the Codex and Pi cases separately. Establish the serving package and
authenticated caller where available, then compare with the exact roster.
Distinguish known defects from conditions that could not be reconstructed.

## Decisions

Do not infer authority from working directory, environment alone, arguments,
or a model prompt. Do not test with the reported command or operation ID.
Preserve the roster, idempotent launches and exact-lead delivery.

## Compatibility and deployment

Retain old bindings and stored operations only where they remain verifiable.
Assess subprocess and resumed-conversation behavior before choosing a fix.
Follow-up request: deploy the Codex fix on aitherdev using
`vpsfree-cz-configuration`, merge it, and release aitherdev. The user confirmed
deployment, activation, merges into the three named `master` targets, and release.
Use a genuine live-package compatibility change to replace the frozen helper
through the existing managed updater. Keep the system-before-profile sequence,
verify the actual serving helper and live continuity, and release only after
deployment and integrated lineage are proven. Do not restart the affected session to reproduce or conceal the failure,
and do not adopt or rerun its workload. Pi parity remains out of scope.

The system is on D, but the profile switch refused before managed maintenance
because of one accepted, never-materialized Pi creation. The user authorized
only discard of that request, not a retry. [D5](design.md#d5--discard-one-never-materialized-pi-request-without-retrying-it)
uses an epoch-2 bridge from the selected source to preserve the request across
an initial compatible switch and retire it through its authenticated owner.
Keep the normal pins, live system and original claim unchanged for the bridge.
A separate dated workspace build output must reproduce the bridge from exact
inputs and carry its complete source patch. Its default-branch integration and
temporary selection require specific approval. After verified discard, switch to
the unchanged epoch-3 target with ordinary managed interruption and resume.

## Documentation

Record generalized evidence and limits in state/design. If a supported tool or
capability changes, update the runtime's owning docs and installed skill as needed.

## Testing plan

Use isolated adapter-to-monitor fixtures and disposable commands/state. Test
exact lead, retained member, foreign lead, stale caller and a valid thread binding
without shell variables. Separately test malformed inputs, unchanged ID retries,
exact-lead delivery, and Pi capability or fallback behavior supported by the
evidence. Review a committed candidate after quick checks and before longer checks.
For D5, prove exact-request refusal, writer exclusion, crash replay and no Pi
start or native effects in focused disposable tests. Use one stock disposable
source→bridge→target check after review to prove source preservation, the
serving bridge owner, the target's acceptance of the bridge's actual cancelled
record, and replacement of the serving helper without losing an unrelated root.
