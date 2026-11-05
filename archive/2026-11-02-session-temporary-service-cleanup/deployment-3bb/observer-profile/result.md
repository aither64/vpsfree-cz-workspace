# Profile/UI observer result

- Scope: read-only observation of deployment-3bb profile/UI status. Session identity matched the bound slug and workspace.
- Terminal record: `deployment-3bb/operation-status.json` reports `complete=true`, phase `deployment-and-selected-ui-verified-integration-pending`.
- Profile switch: exit 0 in 51.64 seconds; no remaining owned process group. See `deployment-3bb/profile/status.json`, `exit-status.txt`, and `command.log`.
- UI attempts 1–3 ended with exit 1 and no remaining process groups. Attempt 1 was recorded as stopping in NSS setup before portal HTTP. Attempt 4 ended with exit 0 in 33.92 seconds and no remaining process group. The terminal record reports verification on the actual selected profile at 1280 and 375 widths, badges `0/1/0`, accepted own readers, and strict TLS.
- UI evidence: `deployment-3bb/ui*/status.json` and associated `command.log` files; attempt 1 and attempt 2 also have `exit-status.txt`.
- Main records actual selected equality and authenticated health passed. Default integration is approved; session lifecycle is unauthorized. Machine remains held pending approved remote default lineage integration.
- No usability or acceptance decision is made by this observer.

Observer raw result: `observer-profile/result.json`.
