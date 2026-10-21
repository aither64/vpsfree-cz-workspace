# 2026-10-21-aitherdev-observability-access

## Goal

I'd like to update vpsfree-cz-configuration, so that aitherdev would have read-only access to log.int.prg.vpsfree.cz (afaik currently it has access to its root user, I'd rather use an unprivileged user). secondly, I'd like aitherdev to have access to prometheus instances in vpsfree-cz-configuration, so that codex on aitherdev could access prometheus metrics. suggest a solution.

## Affected repositories

- `vpsfree-cz-configuration`: read-only investigation of SSH log access,
  aitherdev networking and Prometheus services. No project edits in this phase.

## Approach

Produce a repository-grounded proposal before implementation. Architect0 owns
investigation and `design.md`; lead owns scope, acceptance and user communication.
Keep changes limited to this session's planning records. Do not deploy or merge.

Backlog:

| Owner | Result | Acceptance | Dependencies/checks |
| --- | --- | --- | --- |
| architect0 | Current access inventory and proposed design | Explain root removal, log read scope, all Prometheus query paths and mutation restrictions | Canonical configuration source and official upstream documentation |
| lead | Assess proposal and present recommendation | Concrete tradeoffs, rollout, remaining decisions and evidence | Architect report; inspect cited evidence |
| implementer0 / implementer1 | Reserved for subsequent execution packages | No implementation requested in proposal phase | User direction after proposal |

## Decisions

- Request is for a suggested solution; implementation and operations are deferred.
- Preserve retained team settings. Architect0 is ready with workspace-write access.
- No automatic independent review for investigation and planning records alone.

## Compatibility and deployment

Design must cover existing administrator access, key ownership, filesystem/log
rotation permissions, network exposure, Prometheus read versus mutation routes,
mixed configuration revisions, deployment order and rollback. No schema or
data migration is expected; confirm during investigation. Production unchanged.

## Documentation

Readers are the user and future implementers/operators. Proposed design and
evidence belong in this session. Lasting operational documentation would belong
in the configuration repository alongside any later implementation.

## Testing plan

This phase uses source inspection only. Proposed acceptance checks must verify
log readability across rotation, denied writes/privilege escalation, denied
root authentication by aitherdev's key, successful PromQL queries, and denied
management/write endpoints. No long tests or builds are authorized by this plan.
