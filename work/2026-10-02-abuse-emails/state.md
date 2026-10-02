---
lifecycle: active
---

# Abuse email parsing extension

## Current status

Phase: ready, awaiting merge approval for vpsfree-cz-configuration/master. The user
authorized "Implement the plan." All nine formats now extract one source/event,
perform one historical assignment lookup and preserve full readable content.
Implementation, local checks, independent review with its narrow fix, original
content/database checks and targeted API build are complete. Feature is pushed;
no merge, deployment or live replay authorized. Session stays open.

## Phase checklist

- [x] Verify binding/roster and lock all-nine/readable-content decisions.
- [x] Write approved durable design before source edits.
- [x] Simplify source/docs/tests; quick checks and lead writing audit pass.
- [x] Consolidate final feature history and prepare full review inventory.
- [x] Complete independent review and resolve findings.
- [x] Verify original content/persistence and targeted API build.
- [x] Capture final comparison, guarded feature push and CI inspection.
- [ ] Integration/deployment (future authorization).

## Ownership and exact revisions

Bound session: `2026-10-02-abuse-emails`, workspace
`/home/aither/workspace/ai/vpsfree.cz`. Current and both lead environment markers
match. Retained ready members: architect0 design GPT-6 Astra/xhigh/write;
implementer0 application gpt-6.1-sol/xhigh/write; reviewer0 independent review
gpt-6.1-sol/xhigh/read-only. No settings overrides or fallback. Lead owns
coordination, prose and acceptance; fresh catalog-policy Luna/low owns long runs.

Repository/worktree: vpsfree-cz-configuration at
`worktrees/2026-10-02-abuse-emails/vpsfree-cz-configuration`; branch
`2026-10-02-abuse-emails`. Current head
**`40289e3b3760eda1f55306d2547919aeb06bafe7`**, exact base/merge base
`b164a3b786cb82878f00f8ebd2a7825ee5254c15`.
One coherent feature commit, 19 files, 1426 additions/9 removals. Clean tree;
no migrations, schema/API/core/decoder/pin/node changes or obsolete branch paths.
Actual vpsadminServices pin: `a65a4dfeb92a59df4a80a737a20bcbf8558793ff`.

Old restrictive head `7cce4271be0bcd81a42c6784e12dff326e5d041f` is superseded,
unmerged/undeployed/unconsumed. Only local/remote feature refs contained it before
rewrite. Canonical SSH fetch reconfirmed master at the base and remote feature at
that old head before push. Guarded SSH force-with-lease succeeded; remote feature
now exactly `40289e3b`, remote master remains `b164a3b`. No master rewrite.
Initial plan/state/design commit: `20f6e451474b3af5b5747ae8f0f41e2b4dba9270`.

## Implemented contract and local evidence

Original subject without RT prefix, decoded human body/direct plain attachments,
and decoded LRob textual evidence without JSON/Base64 envelope. Earlier-owner,
repeated and other-IP content intentionally remains. No range/A-B-A checks,
record grammar/source extraction, filtering or generated summaries/counts.
Missing event owner has no current-owner fallback; Burina reports stay separate.
Unused text fields may repeat; optional JSON range values are ignored, while
JSON duplicate-key rejection remains a format boundary without a custom scanner.
Unchanged decoder schema checks still validate standard optional field types;
ignored JSON range extensions belong only to the adapter.

Expected and verified event instants on 2026-09-28 UTC:

| Ticket | detected_at |
| --- | --- |
| 95347 | 08:41:50 |
| 95348 | 08:44:40.114 |
| 95350 | 09:23:02 |
| 95351 | 09:29:00 |
| 95353 | 09:36:08 |
| 95355 | 10:32:52 |
| 95356 | 10:38:19 |
| 95360 | 11:46:46 |
| 95361 | 11:57:11.439254 |

Prepared pinned Nix environment: `bundle exec rake spec` passed 186 examples,
0 failures (seed 4071, about one second). The initial nine-file lint and final
two-changed-file lint both passed; other Ruby files were unchanged. Full diff whitespace passes. Normal Overcommit
Nixfmt/RuboCop and
SingleLineSubject/TrailingPeriod/TextWidth hooks pass without bypass.

Lead authored the owning README section through the writing skill; implementer
applied it verbatim. Lead reproduced Custom Visuals date-only remainder rejection;
member narrowed uniqueness to complete prefixes with acceptance/rejection tests.
Initial synthetic wrapper/invalid-byte mutations and lint failures were corrected
before final checks. No production RT semantics or decoder changes.

## Review and longer verification

[Independent review](simplification-review.md) and [full packet](simplification-review-packet.md)
cover all four mandatory lanes at high risk for untrusted parsing, tenant
attribution and persisted content. Reviewer0 inspected the entire one-commit
series at base `b164a3b` through `382c5fb` and concluded no obsolete history or migrations.
Its sole Important finding was Apache reports routed as syslog by a timezone note.
Member fixed format discrimination and the exact regression; lead inspected the
three-path delta and independently reran that example (1/0). Final fold `40289e3b`
contains only 29 additions/4 removals relative to reviewed `382c5fb`, with normal hooks
and clean/full whitespace. No contract expansion or lane rerun under skill step 9.
README clarified existing standard decoder checks without changing the decoder.

[Verification evidence](simplification-verification.md): fresh watcher
verify_abuse_preservation (Luna/low, fork none) completed the exact-head related
batch, exit 0 in 94 seconds. All nine original subject/content/time/one-lookup and
no-save comparisons passed. All nine isolated pinned-schema MariaDB save/reload
cases preserved exact text, subject, assignment and event time, including both
fractions at DATETIME precision 6. Real helper checks passed historical/current
owner, inclusive highest-ID boundary, accepted cross-range/A-B-A full content and
missing-owner no-fallback. Notifications/mailbox disabled; minimal models do not
test wider API callbacks or notification delivery.

Targeted API generation 2026-10-02--21-04-10 built successfully, all 19 affected
derivations. No deployment/kernel escalation. Parent inspected completed
status/evidence; no operation remains running. Production state is unverified.

Original EMLs/input metadata/harnesses remain private and outside version control.
Nine committed fixtures are synthetic. Prepared env avoids member home-cache
writes; read-only frozen Ruby/gem wrapper omits the writing shellHook. Strict
writable wrappers set PS1 before sourcing; shellHook must not be evaluated twice.

## Documentation, recovery and next action

[Plan](plan.md), [approved design](design.md); owning explanation:
configuration `configs/vpsadmin/api/README.md`. Earlier [proposal review](review.md),
[implementation review](implementation-review.md) and [verification](verification.md)
are explicitly marked historical for the superseded restrictive approach.

Final comparison captured base `b164a3b`/head `40289e3b`; source stays clean. GitHub
branch workflow query returned no runs. Only manual/scheduled daily update exists;
no applicable feature CI or superseded runs to cancel. Next: integrate/deploy only
after explicit user direction for the repository/target. No deployment or live
replay planned.

The mail task deletes fetched messages before parsing with EXECUTE=yes; rejected
mail is not automatically retained. Originals remain in RT. Recovery must inspect
existing incidents and partial persistence/notification outcomes before replay.
Rollback cannot retract incidents/notifications or restore deleted mail. Offline
checks do not establish actual production schema/version or mail-worker owner.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-abuse-emails/
