# HaveAPI 0.32.1 downstream integration

The requested follow-up is merged into both remote defaults:

- vpsfreecz/vpsadmin `master`: `097226b22edf8b59f80b5dfaa55265e9d0cac633`.
- vpsfreecz/vpsfree-cz-configuration `master`: `c040c14cdbacc07998700b524996a89306188d7f`.

The product selects all five HaveAPI gems at 0.32.1. The site hook supplies
`close_sso=1` only through HaveAPI's validated Switch user revoke path. The
API1/API2 operations page uses client ID `api.vpsfree.cz`, Switch user enabled,
SSO enabled and renewable_auto access tokens lasting 900 seconds. The services
channel selects the exact product commit; inherited WebUI70bd stays unchanged.

User approval was “merge” in reply to the explicit two-repository request.
Both ordinary fast-forward merges and nonforce SSH pushes passed, with actual
post-merge and pre-push hook child exits verified. Independent remote snapshots
showed the exact intended default heads and unchanged other heads. Both merge
claims were explicitly released and their released states verified. Sources and
targets remain clean; feature/recovery refs, private state and roots are retained.

The exact-head quick checks and final independent reviews remain accepted, with
NO MIGRATIONS. No deployment, production login, host build, or additional CI
campaign was performed. Original product0f observer89033 remains separately
owned by E2; this handoff does not infer its current outcome. This session stays
open and active; no lifecycle or cleanup action was performed.

[Approval](approval.json) · [Integrated receipts](integrated.json) ·
[Site procedure](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/c040c14cdbacc07998700b524996a89306188d7f/docs/operations/vpsadmin-documentation-oauth.md)

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/)
