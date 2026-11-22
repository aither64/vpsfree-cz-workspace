# Pi providers and portal message delivery

## Goal and scope

Propose Codex subscription support in Pi, provider selection per Pi worker, availability-only fallback, and faster message catch-up on tab switches. Codex keeps its per-session provider. Keep cybersecurity and other policy/access gates terminal; never switch providers or replay a blocked turn to work around a gate.

Separately investigate and fix the reported portal send failure: `Sending...` lasted more than 10 seconds before recovery actions appeared. Treat sending and tab catch-up as distinct paths until evidence links them. Do not operate the reported session or retry its message as part of diagnosis.

## Affected repositories

- `dev-workspace`: portal, Pi adapter/provider resolution, and durable submission handling.
- `codex-web`: only if the shared Codex adapter or client owns the verified defect.
- `vpsfree-cz-configuration` and the workspace selection: only as needed for an aitherdev rollout. Keep application deployment on the user profile and the host module contract in site configuration.

## Approach

1. Trace the reported send through browser, portal and runtime receipt boundaries. Fix the first proven cause. Keep the original request ID across uncertain outcomes and do not present durable queue acceptance as completed delivery.
2. Measure tab activation to latest message painted for Pi and check Codex. Prefer immediate catch-up on activation and reconnect over globally shortening a background poll. Keep scroll position, drafts and stream ordering intact.
3. Reuse supported account login and model discovery for the Pi provider picker. Inherit the session provider unless a worker has an explicit override. Bind model selection and credentials to the resolved provider; apply explicit changes at safe turn boundaries.
4. Consider optional fallback only for a positively identified availability problem, without duplicating an accepted turn or switching after output or tool execution. Policy, access, auth and unknown outcomes are not fallback triggers. Prove selection and fallback with distinct test providers before a live smoke test.

## Compatibility and deployment

Preserve retained session defaults and the receipt/retry contract. Confirm whether new stored settings can be read or ignored safely after rollback. Review and test the exact candidate before any aitherdev activation. Use `vpsfree-cz-configuration` for any necessary host-side change and the matching workspace profile for the portal runtime; record previous exact revisions. Deployment does not approve a merge.

## Documentation

Keep the current design and evidence here. Document lasting provider, delivery and compatibility behavior beside the owning runtime APIs; keep any site rollout evidence in session records.

## Testing plan

- Submission: trace click to durable receipt; exercise slow backend acceptance, lost response, retry with same ID, duplicate prevention, and failure reconciliation. Keep UI send status truthful. Use disposable sessions.
- Tabs: use an inactive Pi tab with intervening output, switch back, and measure catch-up. Repeat for Codex; test rapid switches and reconnect for ordering and deduplication.
- Provider: test legacy inheritance, distinct workers and credentials, safe provider/model changes on the same retained history, and negative fallback cases for denials, unknown outcomes and tool side effects. Verify account-entitled models rather than assuming Daybreak is available.
