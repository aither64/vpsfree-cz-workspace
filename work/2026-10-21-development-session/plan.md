# PHP session upload-progress mitigation

## Goal and scope

Disable `session.upload_progress.enabled` everywhere PHP is used in
`vpsfree-cz-configuration`, pending upstream fixes for the user-reported
CVE-2026-109618 and CVE-2026-109619. Verify advisory identifiers and mitigation
scope rather than asserting unverified coverage. Deliver a reviewed published
feature branch, exact machine inventory and a confctl deployment command.
Actual deployment and default-branch integration are outside this request.

## Owners and backlog

| Owner | Expected result | Acceptance / checks | Dependencies |
| --- | --- | --- | --- |
| architect0 | PHP inventory and design.md | Cover service modules, generated INI, all host mappings and confctl syntax; cite advisory evidence | None |
| implementer0 | Configuration execution package | Minimal complete patch, hooks/quick checks, focused commit, published branch | Design, initial tracking commit |
| implementer1 | Independent execution package from design | Own nonoverlapping files or verification/rollout evidence; report coverage and command | Design |
| reviewer0 | Independent final review | Committed final diff, complete history and migration conclusion; no unresolved material findings | All commits and quick checks |
| lead | Coordination, acceptance, tracking and handoff | Exact deploy command and limitations, stable session URL | Member reports |

## Approach and documentation

Architect traces PHP configuration entry points and writes the implementation
and verification brief. Implementers own source, technical comments/docs,
checks, commits and fixes; serialize Git and overlapping edits. A concise source
comment should explain temporary mitigation where useful. Keep individual
machine rollout steps, exact revisions and verification evidence in this session.

## Compatibility, deployment and recovery

Disabling PHP session upload progress may remove application upload-progress
reporting; ordinary uploads and sessions should remain functional. Confirm
actual service behavior and INI precedence in design. No schema, API, persisted
state or channel changes are intended. Apply through normal configuration
activation and PHP service restart/reload semantics; removing the setting before
upstream fixes would restore exposure. Mixed-version hosts remain exposed until
their own configuration is activated. Do not deploy or merge in this turn.

## Verification

Run repository hooks and focused syntax/configuration checks first, then final
independent review. Delegate required uncertain-duration builds to a fresh
Luna/low verification utility after review. Assess every PHP host and ensure no
runtime-specific setting overrides Off. Confirm the exact confctl selector and
build/deploy syntax against installed tool/repository guidance.
