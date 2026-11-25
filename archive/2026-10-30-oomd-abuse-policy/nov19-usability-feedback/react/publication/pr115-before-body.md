Add separate Incident policies and Incident reports tabs to VPS detail. Policies come from API metadata. Current policy facts and saved report evaluations show Period / Incidents / Limit / Action for warning and VPS-stop windows. Reports show authorized saved matches, link active policies to their VPS section and keep filtered history links for retired policies. Notices identify the policy that produced them. Lists make no per-row API calls.

Per-policy limits can inherit their defaults and save independently of the shared shutdown permission. Writes retain confirmed targets, fresh preflight, durable locks after uncertain results and authoritative readback. Capability checks handle older APIs. Overview and list alerts appear only when a threshold is reached (REQ-051).

Verification at `6b14ae5e`:

- The complete three-commit series passed all four independent review lanes with no findings. There are no migrations.
- Application and E2E type checks against the final SDK passed, along with 88 focused tests cumulatively, relevant lint/audits, documentation and asset checks. The original diagnostic failures remain recorded separately.
- The five Nix targets passed: frontend, BFF, provenance, source contents and installed contents. Both build metadata files match the full commit with `dirty=false`; the installed-content check covered 387 public assets.
- All 12 existing synthetic browser cases passed without retries or skips. The session retains 16 captures. Four representative policy/history views passed visual review: English administrator on desktop and Czech owner on mobile.

The SDK dependency is still an immutable development archive. Before merge, the manifest, lock and provenance must select a published registry SDK containing the required members. Browser checks used intercepted synthetic data; live API authorization, engine execution, OAuth, SMTP and deployment acceptance remain separate. The completed Nix build is recorded, although most outputs are no longer resident locally. Deployment of this revision remains unverified.

[Nov18 change record](https://github.com/vpsfreecz/vpsadmin-webui/blob/6b14ae5e1702ee8c137605d3512c123c9a24b582/docs/work-log/2026-11-18-incident-policy-explanations.md) · [SDK provenance](https://github.com/vpsfreecz/vpsadmin-webui/blob/6b14ae5e1702ee8c137605d3512c123c9a24b582/packages/vpsadmin-typescript-client-development.json) · [Current session evidence](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)

[Earlier committed G2 captures](https://github.com/vpsfreecz/vpsadmin-webui/blob/b1fb37b0de3af6ef2f6f9e5f4f73ea0296b19c89/docs/work-log/screenshots/2026-11-17-generic-incidents/README.md) retain their historical source labels. The current Nov18 captures are in the session evidence.
