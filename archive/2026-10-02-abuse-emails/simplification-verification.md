# Whole-content replacement verification

Status: passed at exact final head
`40289e3b3760eda1f55306d2547919aeb06bafe7` after independent review and
focused remediation. Earlier checks in verification.md apply only to the
superseded restrictive contract.

## Acceptance checks

All nine private originals must produce one candidate with their original subject
minus RT prefix, complete normalized readable body/direct text attachments,
supported decoded LRob text evidence, expected UTC instant and fractions, and
exactly one assignment lookup for the reported source at that instant. No raw
JSON envelope is emitted. Dry runs must save nothing.

The independent content expectation reads the original MIME parts and evidence
without calling production rendering helpers. It follows agreed decoding,
line-ending/outer-whitespace normalization and existing duplicate-section rules.
Original messages, input metadata and verification scripts remain private and
outside version control.

## Disposable database and API configuration

The prepared MariaDB harness loads the exact ip_addresses,
ip_address_assignments and incident_reports declarations from the pinned API
schema. It invokes the configuration handler with the real historical lookup
and minimal persistence models. Notifications and mailbox access are disabled;
it does not test wider API callbacks or production configuration.

Check each original in dry-run and normal-save modes, reload persisted records
and compare exact subject, text, assignment and event instant. Check DATETIME(6)
fractional roundtrips, event owner versus a later current owner, inclusive
highest-ID boundary selection and one lookup. Missing event ownership must produce no incident or current-owner fallback.
Crossing assignment histories and
A/B/A reports must succeed with full content when the selected event has an owner.

After independent review, a fresh catalog-policy Luna/low watcher owns the related
DB and targeted int.api1 build batch. No node/kernel checks or deployment. It
retains logs/status and reports any unexpected kernel build for parent diagnosis.

## Executed evidence

Fresh watcher /root/verify_abuse_preservation, gpt-6-luna/low, fork none, pinned
catalog utility policy; no overrides/fallback, source edits, diagnosis or retry.
Single related batch `/tmp/abuse-emails-preservation-verification.sh` guarded the
exact head and clean tracked source. Exit0 in 94 seconds. Parent inspected the
status and bounded completed log; no running operation or kernel escalation.

All nine originals passed independent exact subject/text/time/one-lookup
comparisons with 0 saves. All nine normal-parser saves and reloads passed exact
subject/text/assignment/time comparisons. DATETIME precision 6 retained both
fractions. Real helper checks passed historical owner instead of current owner,
inclusive highest-ID boundary with complete earlier content, cross-range and
A/B/A acceptance with one event lookup, and missing event owner without fallback.
Notifications disabled; mailbox unused. Minimal models do not exercise wider API
callbacks or notification delivery. The disposable DB process exited through its
owned trap; private artifacts remain outside version control.

Targeted `confctl build --yes 'cz.vpsfree/vpsadmin/int.api1'` passed all 19 affected
derivations and built generation 2026-10-02--21-04-10. No deployment or node/kernel
suite. Logs/status remain private at `/tmp/abuse-emails-simplification-verification.log`
and `/tmp/abuse-emails-simplification-verification.status`.

Guarded SSH force-with-lease feature push passed against expected old `7cce4271`.
At feature-push time, remote feature was exactly `40289e3b` and master remained
`b164a3b`. GitHub branch runs
list returned `[]`; only manual/scheduled daily-update exists, with no applicable
feature CI or superseded runs to cancel. Final comparison captured exact base/
head and source worktree stays clean. Production versions/worker/schema remain
unverified; no live reports or mailbox operations performed.

## Default-branch integration

Under the user’s subsequent explicit merge direction, a fresh temporary checkout
fast-forwarded the unchanged final head onto master. Full RSpec passed again:
186 examples, 0 failures, seed 52091. Clean content was pushed normally over SSH;
remote master and feature both matched exact head `40289e3b`. No applicable CI runs
were returned for that commit. Only the operation-owned temporary checkout was
removed; feature worktree/refs and the session are retained. Deployment is owned
by the user and was not performed by the agent.
