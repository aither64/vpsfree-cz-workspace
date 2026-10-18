# Portal recovery and display timing

The lead owns this bounded browser/API design. All implementation stays in
dev-workspace; workspace and configuration changes select its exact revision.

## Interfaces and invariants

Ordinary send attempts keep their saved IDs, text, attachments and context.
Add optional dismissed metadata to their browser storage codec. Dismiss hides
only the receipt and succeeds only after persistence; observed-message
acknowledgement remains responsible for removing retry identity. Retry uses the
existing message endpoint with retry=true and the same ID/attachments, follows
current execution eligibility, and is guarded against concurrent page retries.
Capture the thread and draft identities so delayed responses cannot clear a
different thread or revised text/uploads. Plan and queue recovery stay with
their existing owners. No automatic resend is introduced.

Index status adds loading=true only for a cold cache with no refresh failure.
New browsers distinguish that state from warning-bearing successful responses.
Use the shared controller for both transport and snapshot failures; success
means a healthy snapshot. Update snapshot data independently of warning grace,
preserving freshness and authoritative-inventory checks. Access errors remain
immediate; server reconciliation and its deadlines are unchanged.

Timestamp presentation is keyed by thread and stable transcript entry identity.
Exact observations survive later approximate/missing responses for that entry;
a new exact value replaces an old one. For entries without exact times, while
metadataPending is true, hide fallback time/date presentation until the shared
visible warning grace expires. Repeated reads do not restart the grace. Once
enrichment settles, show available estimates with their ~ marker or the existing
unavailable-time presentation. Apply consistent selection to footer and date
grouping, including older-page/repair/filter renders. Clear page-memory state on
thread changes and use the shared hide/resume timing semantics. Legacy servers
without metadataPending use their existing estimates immediately.

## Compatibility, deployment and recovery

No server receipt, persistent runtime, Codex or database migration. Optional
browser metadata and the additive index flag tolerate older clients/servers.
Old clients may show dismissed warnings again. Keep matching source pins and
the existing system-then-profile activation order. Reuse configuration's
coordinated aitherdev operations contract; recovery remains forward-only.

## Acceptance and verification

Exercise lost message responses with revised drafts, exact retries, attachments,
reloads, dismissal, storage errors, repeated clicks and thread changes. Fake
browser clocks cover loading/warning grace, repeated failed snapshots, recovery,
visibility, immediate auth errors and pending/exact/estimated timestamp
transitions across newest, older and repaired history. Run focused syntax/unit
checks before final review; run browser/package/CI/build verification afterward.
Deployment acceptance requires exact package identities, working portal access,
the three reported behaviors and retained Codex/tmux continuity.
