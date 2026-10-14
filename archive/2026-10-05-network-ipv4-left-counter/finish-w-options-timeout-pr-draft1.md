A stalled shared capability OPTIONS request can leave free-IP suggestions loading past their existing timeout. This change applies one 12-second caller budget to capability discovery and address loading, settles errors so later locations progress, and prevents late requests/results after timeout or cancellation. Shared metadata remains available to other callers and retries retain the existing cache policy.

Extends REQ-050 and addresses #30. The existing unit and adopted EN/CS desktop/mobile browser scenarios cover the timeout, sharing, retry and manual-filter boundaries. Documentation records the per-query budget and the limit that retry may rejoin a still-pending shared lookup.

Verification: implementation is being frozen; exact-head hosted checks, browser evidence and independent review are pending. Synthetic fixtures do not certify a live API. No deployment is included.
