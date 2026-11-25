# OOM incident email copy brief

Lead-owned wording under vpsfree-user-facing-writing, 2026-10-30. Copy for the
implementation, with placeholder names mapped to the architect's mail contract.
This is a wording brief, not rendered mail or an activation instruction.
Use the templates repository's exact greetings, signatures and automated notices.
Show VPS ID/hostname, 7-day/30-day incident counts and effective limits, plus the
relevant incident link(s). Keep the word "policy" out of member mail.

## English warning

Subject: `[vpsFree.cz] Action required: repeated resource incidents on VPS {id}`

Your VPS {id} {hostname} has repeatedly triggered our resource protection system.

This resource pressure affects other VPS on the same node and may disrupt their
services. Please review your VPS's memory usage and service configuration. A
common cause is a web server or application spawning more worker processes than
the available memory can support. Reducing the maximum number of workers may
resolve the problem.

If your workload needs more memory, you can increase your VPS's memory through a
membership expansion:

https://kb.vpsfree.org/information/membership_fees#what_the_membership_fee_is_composed_of

When automatic stops are effective, include:

Please address this to prevent further incidents. If a new incident brings the
total to {stop_limit} or more within 30 days, your VPS will be stopped automatically.
If you start it again and incidents continue while it remains at or above this
limit, it will be stopped again, at most once per 24 hours.

When automatic stops are suppressed, include only:

Please address this to prevent further incidents.

## Czech warning

Subject: `[vpsFree.cz] Je potřeba zásah: opakované incidenty ve VPS {id}`

VPS {id} {hostname} opakovaně vyvolává zásahy systému ochrany před nadměrnou zátěží.

Taková zátěž ovlivňuje ostatní VPS na stejném nodu a může narušit provoz jejich
služeb. Zkontroluj prosím využití paměti a nastavení služeb ve VPS. Častou příčinou
je webový server nebo aplikace, která spouští více pracovních procesů, než kolik
dostupná paměť zvládne. Problém může vyřešit snížení maximálního počtu těchto procesů.

Pokud aplikace potřebují více paměti, můžeš paměť VPS navýšit rozšířením členství:

https://kb.vpsfree.cz/informace/platby#z_ceho_se_sklada_clensky_poplatek

When automatic stops are effective, include:

Vyřeš prosím příčinu, aby nedocházelo k dalším incidentům. Pokud nový incident
zvýší jejich počet za posledních 30 dní na {stop_limit} nebo více, VPS se automaticky
vypne. Pokud VPS znovu spustíš a incidenty budou pokračovat, dokud jejich počet
zůstává na tomto limitu nebo nad ním, VPS se znovu vypne, nejvýše jednou za 24 hodin.

When automatic stops are suppressed, include only:

Vyřeš prosím příčinu, aby nedocházelo k dalším incidentům.

## Stopped email

English subject: `[vpsFree.cz] VPS {id} stopped after repeated resource incidents`

English opening: Your VPS {id} {hostname} was stopped after repeated resource incidents.

Czech subject: `[vpsFree.cz] VPS {id} se vypnulo kvůli opakovaným incidentům`

Czech opening: VPS {id} {hostname} se vypnulo kvůli opakovaným incidentům.

Reuse the matching language's shared-impact, memory/configuration and expansion
paragraphs above. Follow with:

English:

The automatic stop also disabled autostart. You can start the VPS again in
vpsAdmin to adjust its configuration. If another incident occurs while the total remains at or above
{stop_limit} within the last 30 days, it will be stopped again, at most once per
24 hours. Once the total falls below this limit, the usual limits apply again.

Czech:

Při tomto vypnutí se také zakázalo automatické spouštění VPS. VPS můžeš znovu
spustit ve vpsAdminu a upravit jeho nastavení. Pokud dojde k dalšímu incidentu a jejich počet za posledních
30 dní zůstane na {stop_limit} nebo výše, VPS se znovu vypne, nejvýše jednou za
24 hodin. Jakmile počet incidentů klesne pod tento limit, opět platí běžné limity.

The stopped template is sent only after confirmed stop success. Backend and
template owners must reconcile timing/settings changes so no promised future
action contradicts the effective exemption or mode at the point of sending.
