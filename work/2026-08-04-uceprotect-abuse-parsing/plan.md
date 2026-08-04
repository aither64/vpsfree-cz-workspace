# 2026-08-04-uceprotect-abuse-parsing

## Goal

Determine why RT ticket 93961, a MasterDC UCEPROTECT report for
`185.8.165.59`, did not create a vpsAdmin incident and produced no parser log.

## Affected repositories

- `vpsadmin`: mail retrieval, dispatch, and incident parser framework.
- `vpsfree-cz-configuration`: production parser configuration, fixtures, and
  production host/logging configuration.

The production Request Tracker installation is also in scope as an external,
non-repository system because it selects the recipients of abuse ticket
notifications before handing mail to Postfix.

## Approach

1. Trace the UCEPROTECT routing and parsing rules from production
   configuration into vpsAdmin's mail task.
2. Reproduce the supplied message, including the subject without an IP address.
3. Inspect production mail-task logs around ticket creation and later polls.
4. Separate parser behavior from upstream RT, mail delivery, filtering, and
   IMAP-folder behavior.
5. Trace RT 4.4.6's exact machine-generated-message and recipient-filtering
   behavior against the delivery headers and retained production history.

## Compatibility and deployment

This is a read-only investigation. No schema, persisted state, API, protocol,
configuration, mixed-version, deployment-ordering, or rollback change is
planned. Any follow-up fix must preserve processing of the existing `INBOX`
and `Junk` folders and avoid reprocessing previously consumed mail.

## Testing plan

- Run the focused MasterDC parser and incident routing specs.
- Reproduce ticket 93961 in memory from the prose UCEPROTECT fixture.
- Correlate RT's ticket timestamp with every production mail-processing run and
  search centralized logs for the ticket ID, provider case ID, IP, processing
  result, and parser warnings.
