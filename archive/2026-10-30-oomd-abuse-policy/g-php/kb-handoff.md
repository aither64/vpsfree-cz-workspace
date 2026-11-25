# G-PHP final KB source delta

Exact owning source: backend `4db0de750500baffb16c7fbc0ac30a2aa198baa7`, tree
`63cc6814777d1435750dcf12901cef0e12aefc16`, parent `93dcd30d`.
Final owned file hashes: `committed-source-hashes.json`; raw scoped patch:
`committed-owned.patch`. This closes provisional source scope only. No capture,
pin, media, staging or production KB work is authorized or performed.

| Intent | Route / source | Landmark disposition | Geometry / visibility |
| --- | --- | --- | --- |
| VPS policy destination | `?page=adminvps&action=incidents&veid=ID`; `webui/pages/page_adminvps.php` + `forms/incident_policy.forms.php` | Old `vps.oom-details` retired; new `vps.incidents.page`, `.policy` | Dedicated page, all discovered policies including zero counts; details collapsed |
| Sidebar destination | `webui/forms/vps.forms.php` | New `vps.incidents.menu` replaces the old direct history entry | After OOM/configure OOM entries, before admin Report incident/Outages |
| Scoped limits | `forms/incident_policy.forms.php`; nested keyed API update | Old `vps.oom-settings` retired; new `vps.incidents.settings` | Two fields per policy; inherit beside Save clears only local draft |
| Shared permission | Same helper; ordinary VPS update | New `vps.incidents.permission` | One heading/section; shared permission and nonterminal action feedback retained |
| VPS list indicator | `forms/vps.forms.php` | Old `vps.oom-summary` column retired; new `vps.incidents.warning` link | No extra column; icon immediately before hostname in all network/rescue/normal branches; zero thresholds show no icon |
| VPS overview warning | `page_adminvps.php` + helper | Threshold link to new subpage | Perex after details title/submenu and before first VPS table; only reached warning/stop thresholds |
| Saved history | `forms/incidents.forms.php`, `pages/page_incidents.php` | Existing incident routes retained; policy-key filter and typed historical detail added | Retired policy keys retained, saved values remain dated history |

Unrelated disk/rescue/network/action warnings stay in their existing branches.
Current metadata and counts are generic; no source-specific policy assumption.
Actual production PHP/XTemplate with synthetic real HaveAPI responses produced
accepted CS/EN admin/member desktop/narrow views. Native locale fallback was fixed
in the local renderer and recorded; final CS views show actual Czech. The existing
1150px legacy viewport remains; this is no responsive redesign or canonical KB
media proof. Existing VPS list/detail crop and sidebar capture bindings need
assessment by the retained KB owner using this exact source, not an automatic
revival of the parked capacity/capture campaign.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
