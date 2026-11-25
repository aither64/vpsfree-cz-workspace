# Legacy PHP presentation — bounded KB impact

Package297e5723, exact committed backend `51b79d2058ab4588b73a123aaff7a5a65ee610fe`,
tree `3313179196e1b204d39300a79adbc4f4ed03c07b`, parent3d9f4057. All10committed
blob hashes in `committed-source-hashes.json` equal accepted `source-hashes.json`.
This inventory
does not change KB source/contracts/pins, certify runtime/media, or allocate a capture.

| Intent/control | Source and destination | Disposition |
| --- | --- | --- |
| VPS policies | `webui/forms/incident_policy.forms.php` → `vps.incidents.menu`; `?page=adminvps&action=incidents&veid=ID` | Preserve policy intent and existing `vps.incidents.open` path; labels become Incident policies / Pravidla incidentů. Landmark declaration moves from vps.forms.php into the shared sidebar helper; refresh source/related fingerprint after final commit. |
| VPS reports | Same helper → new `vps.incident-reports.menu`; original `?page=incidents&action=list&list=1&vps=ID&return=ENCODED_CURRENT_URI` | Add separate report-list control/path binding, retaining Incident reports / Incidenty. Existing Back target uses the return value. Do not repurpose the policies ID. |
| Policy page | Retained `vps.incidents.page`, `.policy`, `.settings`, `.permission`; anchors `incident-policy-KEY` | Title labels change; two explicit Period/Incidents/Limit/Action rows replace ambiguous ratios. Current creation-time membership/action-dependency explanation and supplied mode appear above/within policies. Forms and shared permission remain unchanged. |
| Saved report | `?page=incidents&action=show&id=ID`; new `incident-report.policies`, `.policy`, `.policy-diagnostics` | Successful saved matched-policy tables are separate from current policy settings and admin diagnostics. Links use an authorized included VPS only; active keys target the anchor, retired keys retain exact policy-filtered history. No new member diagnostic/failure section. |
| Notice origin | Existing report detail/list | Explicit originating saved label; detail-only optional links. No hidden trigger lookup or per-list-row policy query. |
| Threshold alert | Retained `vps.incidents.warning` list icon; existing overview perex | Triggers and warning/stop precedence unchanged. Text names the reached action; link now says Incident policies. No numeric ratio, table or extra API request is added to compact alerts. |

The VPS sidebar insertion is immediately after OOM report controls and before the
admin-only Report incident entry. Reports and policies now occupy separate rows.
The original policy IDs keep their meaning; none is removed or reused for reports.
No route is renamed.

Review CS `navody:vps:incidenty` and EN `manuals:vps:incidents` to distinguish the
reports list from policies/settings, and review annotations that currently bind
`vps.incidents.open`. Existing global Incident reports translation remains Incidenty.

Reassess both languages of the retained screenshot concepts:

- `getting-started/vps-details`: sidebar adds one row and changes the policy label;
  visible detail sidebar geometry is directly affected. The warning remains above
  the first ordinary detail table, below the VPS heading, only at a reached threshold.
- `getting-started/vps-list` and `restore-backups/playground-vps-list`: no new list
  column or row count is introduced. Existing threshold icon stays at the hostname;
  zero-count VPSes have no icon. Final-source crop/fixture assessment remains with
  the separately allocated KB owner, including its policy DSL update. Scope is
  now bound to exact51b79d2source; no capture/media certificate is implied.

The focused suite proves zero icon behavior, reached-warning/stop precedence,
navigation URLs and independent period facts. The browser source additionally
checks an actual visible list row before negative old-summary assertions, a
zero-count newly created VPS, and the fixture's beta-warning reached VPS.
The browser scenario has not run on this package.

The six offline previews use actual PHP/XTemplate and real gettext with synthetic
HaveAPI responses. At390px the existing legacy viewport still lays out at1150px;
the package does not redesign responsiveness. These previews are review material,
not canonical KB media or a live-backend certificate. Exact source revision,
running closure, bilingual capture regeneration and production publication remain
separate follow-up obligations.
