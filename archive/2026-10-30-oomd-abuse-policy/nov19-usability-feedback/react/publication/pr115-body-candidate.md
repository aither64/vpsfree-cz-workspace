Add separate Incident policies and Incident reports tabs for each VPS (REQ-051). Policies show API-supplied periods, counts, limits and actions. Reports show authorized saved policy matches, with links for active policies and retired-policy history. Notices identify their saved originating policy. Overview and list alerts appear when a threshold is reached, without per-row API requests.

Limit fields display effective numeric values and provide an independent Inherited/Custom choice for each field. Saving an unchanged inherited field preserves null; an explicit custom value stays custom even when it equals the default. Switching from custom to inherited leaves the value blank and pending until save and authoritative readback. Limits and shared shutdown permission save separately, preserving confirmation targets, preflight checks, drafts after errors and locks for uncertain results. Policy and shared details are visible directly.

The cached policy selector preserves retired keys and other report filters, and changing or clearing a selection resets pagination. Empty member results show that information is unavailable, because private policy outcomes may be hidden.

Verification at reviewed `25c8db48`:

- Independent review covered the complete three-commit series across all four high-risk review lanes and found no issues. The series contains no migrations.
- Application typing, 115 focused tests, and relevant lint, locale/plural, documentation and asset checks passed for their recorded inputs. The final browser test change passed E2E core typing; history consolidation preserved the checked inputs.
- All 12 existing synthetic desktop/mobile browser cases passed once, with no skips or retries. The session retains 16 captures, including four visually accepted policy/history views covering English admin desktop and Czech owner mobile.
- All five Nix targets passed: frontend, BFF, provenance, source contents and installed contents. Installed metadata identifies the full clean revision, and the package check covers 387 public assets. The x86_64 build passed with six optional WASI warnings.

Before merge, publish an SDK release containing the required members and replace the immutable development archive with that registry artifact in the manifest, lock and provenance. Browser checks use intercepted synthetic data. Live API authorization, engine execution, OAuth, SMTP and deployment acceptance remain separate; this revision has not been deployed.

[Nov19 change record](https://github.com/vpsfreecz/vpsadmin-webui/blob/25c8db48d087a1f77a9c1dae02c2cdcae0f4e098/docs/work-log/2026-11-19-incident-policy-usability.md) · [SDK provenance](https://github.com/vpsfreecz/vpsadmin-webui/blob/25c8db48d087a1f77a9c1dae02c2cdcae0f4e098/packages/vpsadmin-typescript-client-development.json) · [Current session evidence](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)

[Earlier committed G2 captures](https://github.com/vpsfreecz/vpsadmin-webui/blob/b1fb37b0de3af6ef2f6f9e5f4f73ea0296b19c89/docs/work-log/screenshots/2026-11-17-generic-incidents/README.md) retain their historical source labels. Current Nov19 captures are session artifacts.
