# 2026-11-23-pi-message-delivery

## Goal

Implement the approved Pi message-delivery changes as lead of this new tracked session. Use the workspace procedures, create and commit plan and state before project commits or external changes, and use the retained team for design, implementation and final review. Own all three parts through published feature branches and verified tests. Do not merge or deploy, or change the reported live session.

1. Stop Pi workflow observation storms from contending with Send. The deployed dev-workspace f3bd843f, codex-web 3209aa7b fixture reproduced an empty question drain waiting for the exclusive session lock, discarding a fresh result and scheduling an extra observation. With 96 failed lead refreshes and 580 host inspections of that runtime in four minutes, prevent useless exclusive work and repeated display demand under failure/churn; preserve correct rechecks for real work and prioritize the foreground sender.
2. Save user input durably under the original client ID before waiting on Pi. Validate local identity, authorization, attachments and mode and acknowledge truthfully as Queued. Have the portal own safe delivery across tab closure, network loss and restart. Preserve exact native acceptance, selected target/settings, order and steer/follow-up semantics. Recheck before dispatch; do not replay an ambiguous native send. Distinguish queued, sent and actionable terminal failure. Existing retry:true with a missing native receipt returns Unknown. Reuse shared browser contracts and supported persistence where appropriate and protect legacy consumers, workers and receipts.
3. Remove full transcript reconstruction and hashing from worker identity/capability checks on Send while preserving real pre-effect verification, including behavior with retained workers. Measure p95 durable queue receipt <250ms and healthy Pi delivery <1s on long histories under representative team activity. Exercise restarts on both sides of dispatch, repeated ID, closed tab, live scope changes and background fairness using disposable fixtures. Record actual measurements and limits. Select remote and deployed-compatible bases deliberately. Require independent review and the applicable longer verification. Keep compact status and evidence in state.md for the initiating conversation.

## Affected repositories

- dev-workspace: Pi workflow observation, durable portal delivery and worker checks.
- codex-web: shared browser message delivery contracts where required. The architect
  will verify the precise boundary before releasing implementation.
- No configuration deployment or live package/session mutation is authorized.

## Approach

1. Retained architect0 investigates the three bounded problems and writes design.md
   with stable contracts, compatibility/recovery invariants and independent packages.
2. Select fresh remote bases deliberately against deployed dev-workspace f3bd843f
   and codex-web 3209aa7b. Record gaps; do not import unrelated peer work.
3. Retained implementer0 and implementer1 own complete packages, including source,
   tests, technical docs, quick checks, commits and review fixes. Sequence shared
   files and Git mutation windows explicitly.
4. Review the complete committed series with retained reviewer0 after quick checks,
   then execute applicable longer verification and disposable performance fixtures.
5. Publish feature branches and verify their exact remote heads and CI. Keep this
   session active and open; do not merge, deploy or alter the reported live session.

## Decisions

- Identity verified by dev-session current and both matching environment markers.
- Retain Full-team settings: Astra/xhigh design; Sol/xhigh implementation and review.
- Queued means durable local acceptance only. Preserve original client IDs, target,
  settings, ordering, steer/follow-up semantics and exact native acceptance evidence.
- Ambiguous native dispatch must never be replayed. Missing legacy retry receipts
  remain Unknown. Validate locally before queue receipt and recheck before effects.

## Compatibility and deployment

Assess old/new portal, shared browser, retained workers, receipts and persisted
queues together. Reuse supported persistence, preserve legacy consumers, document
state formats and rollback boundaries. Real pre-effect authorization and identity
checks remain mandatory. Deployment ordering is documentation only in this task.

## Documentation

Runtime maintainers and browser consumers need lasting queue, ambiguity, recovery
and capability semantics in the owning repositories. Keep temporary branch state,
actual measurements and test limits in this session's state and linked evidence.

## Testing plan

Quick checks cover focused Go/browser/Pi tests and required hooks. Independent final
review includes full history and migration provenance. Longer checks use disposable
state only: restart before/after dispatch, repeated ID, closed tab/network loss,
live authorization/target/settings changes, retained workers and background fairness.
Measure durable queue receipt p95 against 250ms and healthy Pi delivery against 1s
on long histories with representative team activity. Record sample sizes, actual
percentiles, fixture workload and limitations; no live session experiments.
