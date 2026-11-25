# Changed legacy PHP copy for root review

Root-approved source copy (package297e5723): `webui/forms/incident_policy.forms.php` and `webui/forms/incidents.forms.php`.
The current policy page preserves `vps.incidents.menu`/`.page`; the restored reports
entry has `vps.incident-reports.menu`. Current and saved facts use separate tables.

| English | Czech | Context |
| --- | --- | --- |
| Incident policies | Pravidla incidentů | Sidebar, page title, live policy links; root supplied |
| Period / Incidents / Limit / Action | Období / Počet incidentů / Limit / Akce | Two supplied-period rows; root supplied |
| Warning / VPS stop | Upozornění / Vypnutí VPS | Action categories and saved decision; root supplied |
| Each policy counts reports that matched it when they were created. Sending a warning or stopping the VPS also depends on the policy and VPS settings. | Každé pravidlo počítá hlášení, která mu při vytvoření odpovídala. Odeslání upozornění i vypnutí VPS závisí také na nastavení pravidla a VPS. | Current policy page, above the individual policies |
| These counts and limits were saved when this report was evaluated. | Počty a limity byly uloženy při vyhodnocení tohoto hlášení. | Member-visible saved matched policies in report detail |
| Mode | Režim | Supplied effective mode; existing observe/notify/enforce labels retained |
| Other policy evaluations | Ostatní vyhodnocení pravidel | Admin diagnostics only; separate from successful matched policies |
| Matched | Shoda s pravidlem | Saved nullable match result in admin diagnostics; existing Yes/No/Unknown values |
| Error stage / Error class | Fáze chyby / Třída chyby | Safe API diagnostic fields, admin only; no error message |

Existing `Incident reports` → `Incidenty`, return behavior, mail-state qualifiers,
warning/stop precedence, shared permission and unknown-limit text remain intact.
`%d day` plural forms already exist. Contextual gettext entries keep the new
column/action translations separate from global `Incidents` → `Incidenty` and
`Warning` → `Varování`; only a scoped extractor keyword is added.

The first focused actual PHP/XTemplate/client suite passed16tests/113assertions.
Final exact-copy assertions pass17tests/122assertions; synthetic actual renders
also check both complete approved EN/CS paragraphs. Final scoped gettext health
passed. Live API/browser execution is held for owner1 and final independent review.
