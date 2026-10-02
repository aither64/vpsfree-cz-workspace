---
lifecycle: active
---

# Abuse email parsing extension

## Current status

Phase: investigation and proposal. User requested inspection and a suggested
solution. No application changes, incidents, deployment or integration performed.

## Phase checklist

- [x] Verify session identity and retained roster.
- [x] Inspect all nine external emails and existing parser routing.
- [x] Architect design and verification brief.
- [ ] Independent proposal review and lead reconciliation.
- [ ] Present recommended solution.
- [ ] Implementation, local checks and final branch review (future work).
- [ ] Deployment and integration (future work; separate authorization).

## Ownership and repositories

- Lead: investigation, coordination and final recommendation.
- `architect0`: design-purpose, ready, workspace-write; retained
  GPT-6 Astra/xhigh. Assigned a design-only brief.
- `reviewer0`: eligible independent review-purpose member, read-only;
  retained gpt-6.1-sol/xhigh, pending assignment.
- `implementer0`: workspace-write, retained gpt-6.1-sol/xhigh; unassigned
  because this turn requests a proposal.
- Configuration inspected read-only through `repos/vpsfree-cz-configuration.git`
  at `b6e650ad902482b4c4e66b5a89a4275bed92419e`; no branch or worktree.

## Evidence and current findings

`dev-session current` and both environment markers match
`2026-10-02-abuse-emails` in `/home/aither/workspace/ai/vpsfree.cz`.
All nine external EML files were MIME-decoded read-only. Inputs remain outside
version control. Configuration README, API README, provider parsers, handler
and existing parser specifications were inspected.

The samples include legacy X-ARF text attachments, inline provider.tools fields,
Fail2Ban SSH syslog messages, an LRob X-ARF v4 JSON attachment, and two prose
summaries. Current matching/date extraction excludes these variants. Burina
messages repeat earlier evidence and include a victim IP in later logs.

Expected proposed detection times (2026-09-28, UTC), by ticket:

| Ticket | Event time | Source of time |
| --- | --- | --- |
| 95347 | 08:41:50 | X-ARF report Date |
| 95348 | 08:44:40.114 | provider.tools Last seen |
| 95350 | 09:23:02 | Last SSH log event, explicit +0200 |
| 95351 | 09:29:00 | X-ARF JSON timestamp |
| 95353 | 09:36:08 | X-ARF report Date |
| 95355 | 10:32:52 | Last SSH log event, explicit +0200 |
| 95356 | 10:38:19 | Cisilino Last seen UTC |
| 95360 | 11:46:46 | Last SSH log event, explicit +0200 |
| 95361 | 11:57:11.439254 | Last SSH log event, explicit -0500 |

These are inspected proposal expectations, not results from executing the
existing parsers. The vpsAdmin base lookup was also inspected read-only:
assignment from_date/to_date cover the supplied event time. Range evidence must
remain inside the selected assignment interval.

## Documentation and next action

See [plan.md](plan.md) and [design.md](design.md). Architect findings agree with
lead inspection. Commit the initial substantive tracking bundle, and obtain
independent design review. No production behavior documentation changes are
needed before a solution is implemented.

## Risks and recovery

Wrong source selection or timezone inference could assign an incident to the
wrong owner. Repeated log evidence needs an explicit incident-granularity policy.
Existing `processed?` behavior does not guarantee creation or mail retention;
the repository README warns fetched mail is deleted under `EXECUTE=yes`
independently of parser success. No replay against a live mailbox is authorized.

## Cleanup

Leave the session open. No owned worktrees or generated artifacts to clean.
