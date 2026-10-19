# Creation handoff correction

Lead-owned bounded design, using xhigh effort. Scope is the generic runtime's
Ruby acceptance boundary and its creation status page; native Codex is unchanged.

The live failed schema-3 receipts have valid direct-team/root shapes and include
`request.provider = codex-lb`. Direct request validation rejects the field before
any creation journal is published. `start` also fails to pass its provider into
the existing receipt preparation method. Plan requests additionally serialize
`destinationSettings`, absent from the same strict Ruby allowlist.

Keep schemas and strict readers. Forward `provider` from start into receipt
validation; compare the CLI's provider intent with the saved request for all
creation kinds, and validate its optional syntax with the existing helper.
Accept provider in direct new/plan receipts, plus optional boolean
destinationSettings for plans only. Do not reopen retired virtual-team creation.
No new binding fields or migrations: the accepted receipt plus the creation/fork
journal already own identity and provider intent. No duplicate effects on retry.

The creation renderer will assign text only when it changes, particularly errors,
and share a single error display helper across polling/retry/name failures.
A separate Copy error action uses the existing accessible copy-button component.
Polling remains live, including retries from another tab; unchanged responses
must not replace the selected text node. Bump the creation asset URL.

Quick checks: a Go-serialized current receipt consumed by real Ruby receipt
preparation for standalone/direct new/plan/fork and inherited/explicit providers;
Ruby start checks prove forwarding, full direct initialization/retry and negative
provider identities; real browser selection during repeated polling and copy.
Tests must fail on the existing code first. Final review precedes long package
checks; use the approved coordinator for publication/deployment and retain exact
rollback/provenance. Existing failed requests remain user-owned; verify the saved
receipt read-only against the candidate, leaving retry to its user.

Compatibility: old receipts without provider remain valid; optional plan flags
retain their type and kind checks. Corrected readers accept existing failed
receipts unchanged. No on-disk/schema or App Server contract changes. Old packages
retain their known refusal for explicit provider/team creations; do not claim
that rollback repairs those requests. Current forward-only provider transition
fences continue to apply. Acceptance requires unchanged provider settings and
stock binary, real handoff regressions, stable browser selection, deployment and
live read-only verification. Aitherdev release follows accepted verification.
