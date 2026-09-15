# UCEPROTECT multi-report implementation

## Goal and scope

Implement the accepted multi-report parsing plan. Deployment and ticket replay are outside this request. The supplied email stays in upload storage outside version control.

## Affected repositories

- vpsfree-cz-configuration: MasterDc parser, parser specs, handler specs, and API configuration README.
- vpsadmin: inspected incident result, handler, send/reply chains and member notification template. The existing array contract supports the implementation; no API change is needed.

## Findings

Inspected configuration HEAD 94b6cca7. The decoded notice names 37.205.11.27 and 185.8.165.59. The prose matcher returns immediately after its first capture. The CSV parser uses CSV#find and optionally filters by one subject IP. Both paths can silently omit further entries. The pre-change tests covered only single-address cases.

The result and send chain already support multiple incidents belonging to different users. The notification template includes incident.text verbatim, so copying a complete multi-user report into every incident would disclose other entries. The configuration handler defaults matched parsers to processed=true, independently of completeness.

## Accepted implementation approach

1. Parse UCEPROTECT into report entries before writing records. Each entry contains a validated canonical IP, detection time, and evidence restricted to that entry.
2. For prose, parse complete explicit source-address lists following recognized notice labels, including comma-separated lists and wrapping. Do not scan arbitrary addresses from headers, URLs, signatures, or unrelated evidence. Support repeated recognized notice blocks. Use the message date where no event timestamp exists.
3. For CSV, parse all relevant tables and all real source rows; retain row timestamps and ignore the existing 0.0.0.0 sentinel. An IP in the subject is fallback/context, not a reason to discard explicitly reported body entries. Log subject/body contradictions and retain valid body entries; reject unsupported subject-only address lists for manual review.
4. Deduplicate repeated representations of the same event within the message, using canonical IP and event time. Preserve distinct timestamped events. Resolve each entry with find_ip_address_assignment at its own detection time; do not group by user or VPS.
5. Render a per-entry subject and body with shared provider context and only that IP's evidence. Generate a concise MasterDC/UCEPROTECT summary for multiple-entry prose lists. For CSV, project the selected IP and timestamp fields only; other raw fields stay in RT. Keep the original message in RT for operator review.
6. Process valid entries and reject malformed/unassigned entries individually, as explicitly selected by the user. Log each rejection with RT/message reference and source location plus a completion summary. Keep current matched-parser processed semantics and persistence exception behavior. Do not add automatic retries, batch atomicity, or cross-message deduplication. The mailbox task deletes fetched messages independently of processed?, so recovery is manual from RT.
7. Return the incident array through the existing handler. Preserve dry-run behavior and sender checks.

## Compatibility and deployment

Configuration-only change using the existing parser array contract and unchanged matched-parser handled semantics. No database migration, new persisted format, generated client, CLI, service protocol, Nix option, or coordinated node update is expected. The pinned vpsAdmin service revision c38839d5be62e9d40d055b23a84844e2037ba4db supports both old and new parser versions. Rollback can read all created incidents but restores the first-IP bug for future notices; it cannot retract notifications. Deploy the configuration parser after tests and required implementation review. Before replaying the supplied ticket, inspect its existing incident and deliberately process only the missing report to avoid notifying the first user twice.

## Documentation

Readers: parser maintainers and abuse operators. Updated configs/vpsadmin/api/README.md with report splitting, event-time ownership, evidence isolation, failure policy, and replay limitations, linked from the repository README. Rollout remains prepared only; see rollout.md.

## Testing plan

- Synthetic quoted-printable RT-wrapped two-IP notice modeled on the upload; keep the original .eml outside git.
- Two assignments with different user_id/vps_id values produce two incidents and correctly routed notifications.
- Multiple CSV rows/tables, individual timestamps, subject IP plus additional body entries, and sentinel rows.
- Duplicate entries, repeated blocks, line wrapping, IPv4/IPv6, punctuation, invalid tokens, unrelated header/signature addresses, and conflicting subject/body data.
- Historical assignment lookup and separate incidents even when both IPs belong to one user or VPS.
- No cross-entry details in incident subject/text.
- Invalid timestamps and missing assignments are logged while valid entries are processed; persistence failures propagate. Partial processing is explicit in diagnostics.
- Dry run returns the same proposed incidents without writes; existing single-report fixtures remain supported.

## Final decisions

- Only MasterDC UCEPROTECT changes; preserve SPFBL/SBL and unambiguous single-entry rendering.
- CSV is authoritative for an IP mentioned in both prose and CSV, including invalid CSV rows (no timestamp substitution through prose fallback).
- Subject IP is fallback only with no recognized body report. Contradictions are logged; valid body reports remain eligible.
- Multiple-entry incident text is generated from selected structured fields, never the full message. Sender checks remain unchanged.
- No database, API, mailbox, dependency pin, deployment, or replay changes.
- Verify focused specs, all config specs, lint, actual upload read-only dry run, then required four-lane xhigh review of committed work.

## Completion

Implemented, reviewed, merged and cleaned up at b6e650ad902482b4c4e66b5a89a4275bed92419e.
The user subsequently authorized default-branch integration and cleanup; exact
proofs and results are in state.md and rollout.md. Deployment/replay remain out
of scope. Feature refs and session records are retained.
