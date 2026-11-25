# H review packet

## Final committed package

H is ready for lead acceptance. Both authorized Git windows are complete and
the backend window was explicitly returned to implementer1. No H source/index
work remains. Root owns final independent review and any later publication.

| Repository | H parent (M) | Final H head | Tree | Changed paths |
| --- | --- | --- | --- | --- |
| backend | `f746838ff7b5fd38fbb732197793244df18a5b05` | `4f391f06d42f27e5c48ee1bd0a25680be9fd51b0` | `8dbfe2121c83736f0d89430e7c677f402b8328a9` | 2 |
| site | `73b9dc657fcac4fce6c25a8873be4f35c908f736` | `dea33d0941efeb8ffc2cd3730631bcecfb342d5a` | `a5f36b7112883072b756ceb809c3f005bfbd60a0` | 24 |

The backend unpublished predecessor `19f22fca704a5e16b97ebdc18c7521218b0b76f8`
was ordinarily amended to include the requested footer consistency. It is not
a retained extra H commit. Normal backend pre-commit and commit-msg hooks passed
for both the original and final amendment; no hook was bypassed. The site
repository declares no hook framework; its normal commit passed. The site is
clean and both indexes were empty at return. G1's disjoint dirty backend sources
were preserved. No push, default integration, independent review launch, runtime
or deployment occurred. H contains no migrations, schema change, generated
clients or transitional compatibility/history stream.

Final source hashes match the committed H blobs. The exact scoped patches and
parents/heads/trees are recorded in `backend-commit-receipt.json`,
`site-commit-receipt.json`, `source-parity.json`, `backend-owned.patch` and
`site-owned.patch`. Existing 84 render comparisons, the affected 12 OOM reruns,
18 final footer checks, 43 rightmost-scroll proofs and final 77/393 + 60/197
template checkers cover their recorded inputs. `final-check-reuse.json` makes the
full site flake-check boundary explicit: 377 unchanged files and 16 H-only
CSS/footer updates subsequently covered by targeted render checks and the
normal final checker. Do not call the earlier flake snapshot the exact final
source. All 35 M template files remain unchanged.

Root's requested corrected representative screenshot is
`visual/vps_oom_report-cs-390-after.png`; the password, expiration and CPU
footer samples sit beside it. Compatibility and documentation placement remain
as described below. No additional project documentation is useful.

Owner: implementer4; styling-only package accepted visually by root.

Baseline site `d42ad451db702a4bf7982c3d94369c3e3d31d76a`; backend `4842e75b17df5453b0c5883dd5d54524bf69b8a2`. M commits precede H in each repository. Final parents/heads and hook outcomes are recorded above.

## Scope and affected paths

26 existing HTML variants changed: 24 site and two built-ins. No subject/plain/meta, locale, spec, renderer, API/schema/client, migration, recipient or runtime change belongs to H. The five incident families belong to M.

### site

- `templates/alert_admin_monthly_traffic_closed/email/en.html.erb`
- `templates/alert_admin_monthly_traffic_confirmed/email/en.html.erb`
- `templates/alert_admin_unpaid_cpu_closed/email/en.html.erb`
- `templates/alert_admin_unpaid_cpu_confirmed/email/en.html.erb`
- `templates/alert_admin_unpaid_data_flow_closed/email/en.html.erb`
- `templates/alert_admin_unpaid_data_flow_confirmed/email/en.html.erb`
- `templates/alert_user_outgoing_data_flow_closed/email/cs.html.erb`
- `templates/alert_user_outgoing_data_flow_closed/email/en.html.erb`
- `templates/alert_user_outgoing_data_flow_confirmed/email/cs.html.erb`
- `templates/alert_user_outgoing_data_flow_confirmed/email/en.html.erb`
- `templates/alert_user_paid_cpu_closed/email/cs.html.erb`
- `templates/alert_user_paid_cpu_closed/email/en.html.erb`
- `templates/alert_user_paid_cpu_confirmed/email/cs.html.erb`
- `templates/alert_user_paid_cpu_confirmed/email/en.html.erb`
- `templates/daily_report/email/en.html.erb`
- `templates/expiration_user_active/email/cs.html.erb`
- `templates/expiration_user_active/email/en.html.erb`
- `templates/password_recovery/email/cs.html.erb`
- `templates/password_recovery/email/en.html.erb`
- `templates/payments_overview/email/en.html.erb`
- `templates/snapshot_download_ready/email/cs.html.erb`
- `templates/snapshot_download_ready/email/en.html.erb`
- `templates/vps_oom_report/email/cs.html.erb`
- `templates/vps_oom_report/email/en.html.erb`

### backend

- `api/notification_templates/templates/password_recovery/email/cs.html.erb`
- `api/notification_templates/templates/password_recovery/email/en.html.erb`

## Evidence and limitations

[Draft and design rationale](draft.md) records parity, presentation choices and compatibility. Source ERB tokens and body interiors remain byte-identical; six preexisting IP-release cards remain byte-identical. Existing production builder and TimeZones rendered 84 baseline/final pairs. Browser text/link/image/anchor/cell parity passed all 84. Root requested a small OOM-table wrap correction; only twelve affected CS/EN pairs were rerun, preserving all unaffected evidence. Final OOM 390px samples retain whole action/link words and a 366px card. All43 overflowing dense daily tables reach rightmost cells after horizontal scroll; email clients that ignore scroll CSS retain visible ordinary tables as fallback. No hidden overflow is used.

Normal site flakecheck and checker pass on the retained393-file snapshot. Final OOM CSS changed two paths afterward: a fresh normal site checker passes all 77 templates / 393 files; the other 391 file hashes remain equal to the retained flakecheck snapshot. All35Mfiles remain equal there. Backend checker passes60 templates / 197 files; H backend two-file hashes unchanged. Current H hashes/source equality are recorded in `source-parity.json`; exact scope patches in `site-owned.patch`/`backend-owned.patch`; no expanded render campaign follows source-identical commit metadata.

H contains no migrations and adds no compatibility path or transitional history. Root owns whole-branch review across prior source, migrations and later G1 work. H commits must remain separate from M per the user instruction. No integration, push, independent review launch, runtime or deployment is authorized in this package.

No project documentation change is useful: existing template/check guidance remains valid. Rollback selects the prior template source and never rewrites saved MailLogs. Root owns any later template reconciliation and producer demonstration.

Next: lead acceptance and independent final affected-lane review when the combined deliverable is complete. Both H windows have returned.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/

## Final footer consistency correction

Root requested the exact IP-release footer style (`font-size:12px;color:#596773`)
on existing automated-notice paragraphs. H adds only that inline style to 16 site
and two built-in variants; no notice is added to the eight admin variants. The
six existing IP-release cards remain unchanged. Eighteen one-case representative
production-builder/DOM comparisons confirm the computed 12px and RGB(89,103,115)
style, exact text, links, images, anchors and data cells. Existing branch coverage
from the 84 pairs and affected 12 OOM pairs remains applicable because every ERB
block and body text is unchanged. The two normal template checkers pass on the
final sources. The retained full site flake-check receipt is earlier; changed
inputs are explicitly recorded as H-only CSS/footer changes rather than claiming
an exact final-source flake rerun.

Backend first committed `19f22fca704a5e16b97ebdc18c7521218b0b76f8`, then root
requested this footer consistency amendment while unpublished. The initial commit
window had already returned to implementer1, so H reacquired it explicitly from
implementer1 and root before the ordinary two-path amendment. No G1 index mutation
occurred before that handback. M remains the parent.

The initial backend API-shell commit attempt stopped before hooks because that
shell lacks the root Overcommit bundle. `nix develop .#vpsadmin` runs the normal
root hook environment; the successful initial commit and final amendment retain
all hooks. Existing lesson: [root and API shell distinction](../../../notes/vpsadmin/2026-09-15-plugin-rake-database.md).
