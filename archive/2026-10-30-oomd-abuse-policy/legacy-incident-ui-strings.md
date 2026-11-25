# Generic incident UI copy (2026-11-17)

Current wording for G1/G2 supersedes the earlier shared-incident table below.
Policy names/descriptions come from API metadata, including saved metadata in
history. They are not translated or guessed by policy key in either frontend.
Use the table only where the corresponding control/fact is actually shown;
it is not a list of paragraphs to place on the page. Root will read actual final
screens before commit. React terminology input is a65a4dfeb92a59df4a80a737a20bcbf8558793ff.

| English | Czech |
| --- | --- |
| Incidents | Incidenty |
| Incident history | Historie incidentů |
| View incidents | Zobrazit incidenty |
| Warning limit reached | Dosažen limit pro upozornění |
| Shutdown limit reached | Dosažen limit pro vypnutí |
| Warning limit | Limit pro upozornění |
| Shutdown limit | Limit pro vypnutí |
| Below limits | Pod limity |
| Approaching a limit | Blíží se limitu |
| Details | Podrobnosti |
| Last incident | Poslední incident |
| Last warning | Poslední upozornění |
| Last automatic shutdown | Poslední automatické vypnutí |
| Automatic shutdown | Automatické vypínání |
| Allow automatic shutdown | Povolit automatické vypínání |
| Use inherited limits | Použít výchozí limity |
| Leave a field empty to inherit its limit. | Prázdné pole použije výchozí limit. |
| Save | Uložit |
| Changes saved | Změny byly uloženy |
| Unable to save changes | Změny se nepodařilo uložit |
| Incident limits are misconfigured. | Limity incidentů nejsou správně nastavené. |
| Policy settings | Nastavení pravidla |
| Policy | Pravidlo |
| Limits | Limity |
| Limits must be positive integers or empty to inherit the policy limits. | Limity musí být kladná celá čísla. Prázdné pole použije výchozí limit. |

Use Czech ngettext forms for `Incidents in %d day` / `Incidents in %d days`: `Incidenty za %d den`, `Incidenty za %d dny`, `Incidenty za %d dní`.

The page/tab title replaces the large overview section. Show policy labels as
section headings; two compact count/limit rows are enough. Use actual period
values with existing plural handling. Threshold banners contain one short
threshold statement and the incidents link; they do not promise a future stop.
Avoid duplicating the same warning at both a section heading and every count row.

Keep optional history/timestamps inside Details. Label a warning according to
its actual saved meaning: if it only proves queued work, retain the existing
queued qualifier rather than presenting it as sent. Last automatic shutdown
means a confirmed physical outcome. Existing pending/failed/uncertain operation
feedback remains visible through normal UI conventions.

Each policy's two override fields share a form and nearby secondary inherit
control; Save writes the draft. Shared automatic-shutdown permission has its own
form once. Do not add prose describing inactive outcomes, hook mechanics, source
adapters or the old dynamic-limit absence. Preserve meaningful read/save/error/
uncertainty feedback. Actual error and confirmation strings receive root's final
pass with the implementation; the older table is not a requirement to retain them.

## Historical wording (superseded for G)

# Shared incident UI copy

Final common labels/help follow lead-owned mail-rework-copy.md. Unchanged statuses and count/cooldown help retain the accepted original translation. Registered type labels come escaped from the API.

| English source | Czech |
| --- | --- |
| Below limits | Pod limity |
| Approaching a limit | Blíží se limitu |
| Warning limit reached | Dosažen limit pro upozornění |
| Automatic shutdown limit reached | Dosažen limit pro automatické vypnutí |
| 7 days: %1$d/%2$d; 30 days: %3$d/%4$d | 7 dní: %1$d/%2$d; 30 dní: %3$d/%4$d |
| Automatic shutdown exempt | Výjimka z automatického vypínání |
| Automatic shutdown permission | Automatické vypínání |
| Allowed | povoleno |
| Exempt | Výjimka |
| Incidents in 7 days / warning limit | Incidenty za 7 dní / limit pro upozornění |
| Incidents in 30 days / automatic shutdown limit | Incidenty za 30 dní / limit pro automatické vypnutí |
| Observation only | Pouze sledování |
| Warnings only | Pouze upozornění |
| Warnings and automatic shutdown | Upozornění a automatické vypínání |
| Global mode | Globální režim |
| Automatic shutdown active | Automatické vypínání aktivní |
| Last incident | Poslední incident |
| Last warning queued | Poslední upozornění zařazené k odeslání |
| Last confirmed automatic shutdown | Poslední potvrzené automatické vypnutí |
| Incidents counted since ownership change | Incidenty počítané od změny vlastníka |
| No outstanding shutdown | Žádné nevyřízené vypnutí |
| Automatic shutdown pending | Automatické vypnutí čeká na dokončení |
| Automatic shutdown failed | Automatické vypnutí selhalo |
| Automatic shutdown outcome uncertain | Výsledek automatického vypnutí není známý |
| Outstanding shutdown | Nevyřízené vypnutí |
| Cooldown ends | Konec ochranné lhůty |
| Counts use rolling 7-day and 30-day periods. Another incident at or after the cooldown ends is required for another automatic shutdown; no shutdown is scheduled for the cooldown end. | Incidenty se počítají za posledních 7 a 30 dní. Další automatické vypnutí vyžaduje nový incident v okamžiku konce ochranné lhůty nebo později. Na konec lhůty není naplánované žádné vypnutí. |
| Warning limit override (7 days) | Vlastní limit pro upozornění (7 dní) |
| Automatic shutdown limit override (30 days) | Vlastní limit pro automatické vypnutí (30 dní) |
| Leave an override empty to inherit the global default. Effective limits are shown above. The shutdown limit must be at least the warning limit. | Prázdné pole přebírá globální výchozí limit. Výsledné limity jsou uvedené výše. Limit pro vypnutí musí být alespoň stejný jako limit pro upozornění. |
| Changes apply to new incidents. An operation already running may still finish. | Změny se vztahují na nové incidenty. Již probíhající operace může doběhnout. |
| Reset limits to defaults | Obnovit výchozí limity |
| Limits must be positive integers or empty to inherit defaults. | Limity musí být kladná celá čísla. Prázdná hodnota použije výchozí limit. |
| Select whether automatic shutdown is allowed. | Vyber, zda je povolené automatické vypínání. |
| Incident settings | Nastavení incidentů |
| Save incident settings | Uložit nastavení incidentů |
| Incident settings unavailable | Nastavení incidentů není dostupné |
| Incident settings saved | Nastavení incidentů bylo uloženo |
| Unable to save incident settings | Nepodařilo se uložit nastavení incidentů |
| Incident escalation | Opatření při opakovaných incidentech |
| Incident type | Typ incidentu |
| An exemption disables automatic shutdowns by vpsAdmin for repeated incidents. Incident collection and warnings remain active. | Výjimka vypíná automatická vypnutí ve vpsAdminu kvůli opakovaným incidentům. Sběr incidentů a upozornění zůstávají aktivní. |
| Automatic shutdown permission, the cooldown and any unfinished shutdown are shared across incident types for this VPS. | Povolení automatického vypínání, ochranná lhůta a dosud nedokončené vypnutí jsou společné pro všechny typy incidentů tohoto VPS. |
| The node's memory protection remains active. | Ochrana paměti na nodu zůstává aktivní. |
