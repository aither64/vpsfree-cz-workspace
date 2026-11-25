# Synthetic OOM notification previews

Synthetic user/VPS only. Exact pinned vpsAdmin9fc0648 TemplateBuilder and TimeZones; Europe/Prague.
Decision counts are fixed; overridden thresholds test current effective limits.

## vps_oom_warning en; enforcement=true; limits=5/10

```text
[vpsFree.cz] Action required: repeated resource incidents on VPS 12345

Hi example-member,

Your VPS 12345 example.vpsfree.cz has repeatedly triggered our resource protection system.

  Incidents in the last 7 days: 5 (warning limit: 5)
  Incidents in the last 30 days: 8 (stop limit: 10)
  Incident time: 2026-10-30 16:20:00 CET

This resource pressure affects other VPS on the same node and may disrupt their
services. Please review your VPS's memory usage and service configuration. A
common cause is a web server or application spawning more worker processes than
the available memory can support. Reducing the maximum number of workers may
resolve the problem.

If your workload needs more memory, you can increase your VPS's memory through a
membership expansion:

  https://kb.vpsfree.org/information/membership_fees#what_the_membership_fee_is_composed_of

Please address this to prevent further incidents.
If a new incident brings the total to 10 or more within 30 days, your VPS
will be stopped automatically. If you start it again and incidents continue while
it remains at or above this limit, it will be stopped again, at most once per
24 hours.

Incident history in vpsAdmin:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

More information about these incidents:

  https://kb.vpsfree.org/manuals/vps/incidents#oomd

Best regards,

vpsFree.cz team

(This is an automated mail from vpsAdmin, your reply will be sent to our support)
```

## vps_oom_warning en; enforcement=true; limits=6/15

```text
[vpsFree.cz] Action required: repeated resource incidents on VPS 12345

Hi example-member,

Your VPS 12345 example.vpsfree.cz has repeatedly triggered our resource protection system.

  Incidents in the last 7 days: 5 (warning limit: 6)
  Incidents in the last 30 days: 8 (stop limit: 15)
  Incident time: 2026-10-30 16:20:00 CET

This resource pressure affects other VPS on the same node and may disrupt their
services. Please review your VPS's memory usage and service configuration. A
common cause is a web server or application spawning more worker processes than
the available memory can support. Reducing the maximum number of workers may
resolve the problem.

If your workload needs more memory, you can increase your VPS's memory through a
membership expansion:

  https://kb.vpsfree.org/information/membership_fees#what_the_membership_fee_is_composed_of

Please address this to prevent further incidents.
If a new incident brings the total to 15 or more within 30 days, your VPS
will be stopped automatically. If you start it again and incidents continue while
it remains at or above this limit, it will be stopped again, at most once per
24 hours.

Incident history in vpsAdmin:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

More information about these incidents:

  https://kb.vpsfree.org/manuals/vps/incidents#oomd

Best regards,

vpsFree.cz team

(This is an automated mail from vpsAdmin, your reply will be sent to our support)
```

## vps_oom_warning en; enforcement=false; limits=5/10

```text
[vpsFree.cz] Action required: repeated resource incidents on VPS 12345

Hi example-member,

Your VPS 12345 example.vpsfree.cz has repeatedly triggered our resource protection system.

  Incidents in the last 7 days: 5 (warning limit: 5)
  Incidents in the last 30 days: 8 (stop limit: 10)
  Incident time: 2026-10-30 16:20:00 CET

This resource pressure affects other VPS on the same node and may disrupt their
services. Please review your VPS's memory usage and service configuration. A
common cause is a web server or application spawning more worker processes than
the available memory can support. Reducing the maximum number of workers may
resolve the problem.

If your workload needs more memory, you can increase your VPS's memory through a
membership expansion:

  https://kb.vpsfree.org/information/membership_fees#what_the_membership_fee_is_composed_of

Please address this to prevent further incidents.

Incident history in vpsAdmin:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

More information about these incidents:

  https://kb.vpsfree.org/manuals/vps/incidents#oomd

Best regards,

vpsFree.cz team

(This is an automated mail from vpsAdmin, your reply will be sent to our support)
```

## vps_oom_warning en; enforcement=false; limits=6/15

```text
[vpsFree.cz] Action required: repeated resource incidents on VPS 12345

Hi example-member,

Your VPS 12345 example.vpsfree.cz has repeatedly triggered our resource protection system.

  Incidents in the last 7 days: 5 (warning limit: 6)
  Incidents in the last 30 days: 8 (stop limit: 15)
  Incident time: 2026-10-30 16:20:00 CET

This resource pressure affects other VPS on the same node and may disrupt their
services. Please review your VPS's memory usage and service configuration. A
common cause is a web server or application spawning more worker processes than
the available memory can support. Reducing the maximum number of workers may
resolve the problem.

If your workload needs more memory, you can increase your VPS's memory through a
membership expansion:

  https://kb.vpsfree.org/information/membership_fees#what_the_membership_fee_is_composed_of

Please address this to prevent further incidents.

Incident history in vpsAdmin:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

More information about these incidents:

  https://kb.vpsfree.org/manuals/vps/incidents#oomd

Best regards,

vpsFree.cz team

(This is an automated mail from vpsAdmin, your reply will be sent to our support)
```

## vps_oom_warning cs; enforcement=true; limits=5/10

```text
[vpsFree.cz] Je potřeba zásah: opakované incidenty ve VPS 12345

Ahoj example-member,

VPS 12345 example.vpsfree.cz opakovaně vyvolává zásahy systému ochrany před nadměrnou zátěží.

  Incidenty za posledních 7 dní: 5 (limit upozornění: 5)
  Incidenty za posledních 30 dní: 8 (limit vypnutí: 10)
  Čas incidentu: 2026-10-30 16:20:00 CET

Taková zátěž ovlivňuje ostatní VPS na stejném nodu a může narušit provoz jejich
služeb. Zkontroluj prosím využití paměti a nastavení služeb ve VPS. Častou příčinou
je webový server nebo aplikace, která spouští více pracovních procesů, než kolik
dostupná paměť zvládne. Problém může vyřešit snížení maximálního počtu těchto procesů.

Pokud aplikace potřebují více paměti, můžeš paměť VPS navýšit rozšířením členství:

  https://kb.vpsfree.cz/informace/platby#z_ceho_se_sklada_clensky_poplatek

Vyřeš prosím příčinu, aby nedocházelo k dalším incidentům.
Pokud nový incident zvýší jejich počet za posledních 30 dní na 10 nebo více,
VPS se automaticky vypne. Pokud VPS znovu spustíš a incidenty budou pokračovat,
dokud jejich počet zůstává na tomto limitu nebo nad ním, VPS se znovu vypne,
nejvýše jednou za 24 hodin.

Přehled incidentů ve vpsAdminu:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

Více informací o těchto incidentech:

  https://kb.vpsfree.cz/navody/vps/incidenty#oomd

S pozdravem

tým vpsFree.cz

(Tento mail automaticky rozesílá vpsAdmin, Tvoje odpověď se zašle na naši podporu)
```

## vps_oom_warning cs; enforcement=true; limits=6/15

```text
[vpsFree.cz] Je potřeba zásah: opakované incidenty ve VPS 12345

Ahoj example-member,

VPS 12345 example.vpsfree.cz opakovaně vyvolává zásahy systému ochrany před nadměrnou zátěží.

  Incidenty za posledních 7 dní: 5 (limit upozornění: 6)
  Incidenty za posledních 30 dní: 8 (limit vypnutí: 15)
  Čas incidentu: 2026-10-30 16:20:00 CET

Taková zátěž ovlivňuje ostatní VPS na stejném nodu a může narušit provoz jejich
služeb. Zkontroluj prosím využití paměti a nastavení služeb ve VPS. Častou příčinou
je webový server nebo aplikace, která spouští více pracovních procesů, než kolik
dostupná paměť zvládne. Problém může vyřešit snížení maximálního počtu těchto procesů.

Pokud aplikace potřebují více paměti, můžeš paměť VPS navýšit rozšířením členství:

  https://kb.vpsfree.cz/informace/platby#z_ceho_se_sklada_clensky_poplatek

Vyřeš prosím příčinu, aby nedocházelo k dalším incidentům.
Pokud nový incident zvýší jejich počet za posledních 30 dní na 15 nebo více,
VPS se automaticky vypne. Pokud VPS znovu spustíš a incidenty budou pokračovat,
dokud jejich počet zůstává na tomto limitu nebo nad ním, VPS se znovu vypne,
nejvýše jednou za 24 hodin.

Přehled incidentů ve vpsAdminu:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

Více informací o těchto incidentech:

  https://kb.vpsfree.cz/navody/vps/incidenty#oomd

S pozdravem

tým vpsFree.cz

(Tento mail automaticky rozesílá vpsAdmin, Tvoje odpověď se zašle na naši podporu)
```

## vps_oom_warning cs; enforcement=false; limits=5/10

```text
[vpsFree.cz] Je potřeba zásah: opakované incidenty ve VPS 12345

Ahoj example-member,

VPS 12345 example.vpsfree.cz opakovaně vyvolává zásahy systému ochrany před nadměrnou zátěží.

  Incidenty za posledních 7 dní: 5 (limit upozornění: 5)
  Incidenty za posledních 30 dní: 8 (limit vypnutí: 10)
  Čas incidentu: 2026-10-30 16:20:00 CET

Taková zátěž ovlivňuje ostatní VPS na stejném nodu a může narušit provoz jejich
služeb. Zkontroluj prosím využití paměti a nastavení služeb ve VPS. Častou příčinou
je webový server nebo aplikace, která spouští více pracovních procesů, než kolik
dostupná paměť zvládne. Problém může vyřešit snížení maximálního počtu těchto procesů.

Pokud aplikace potřebují více paměti, můžeš paměť VPS navýšit rozšířením členství:

  https://kb.vpsfree.cz/informace/platby#z_ceho_se_sklada_clensky_poplatek

Vyřeš prosím příčinu, aby nedocházelo k dalším incidentům.

Přehled incidentů ve vpsAdminu:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

Více informací o těchto incidentech:

  https://kb.vpsfree.cz/navody/vps/incidenty#oomd

S pozdravem

tým vpsFree.cz

(Tento mail automaticky rozesílá vpsAdmin, Tvoje odpověď se zašle na naši podporu)
```

## vps_oom_warning cs; enforcement=false; limits=6/15

```text
[vpsFree.cz] Je potřeba zásah: opakované incidenty ve VPS 12345

Ahoj example-member,

VPS 12345 example.vpsfree.cz opakovaně vyvolává zásahy systému ochrany před nadměrnou zátěží.

  Incidenty za posledních 7 dní: 5 (limit upozornění: 6)
  Incidenty za posledních 30 dní: 8 (limit vypnutí: 15)
  Čas incidentu: 2026-10-30 16:20:00 CET

Taková zátěž ovlivňuje ostatní VPS na stejném nodu a může narušit provoz jejich
služeb. Zkontroluj prosím využití paměti a nastavení služeb ve VPS. Častou příčinou
je webový server nebo aplikace, která spouští více pracovních procesů, než kolik
dostupná paměť zvládne. Problém může vyřešit snížení maximálního počtu těchto procesů.

Pokud aplikace potřebují více paměti, můžeš paměť VPS navýšit rozšířením členství:

  https://kb.vpsfree.cz/informace/platby#z_ceho_se_sklada_clensky_poplatek

Vyřeš prosím příčinu, aby nedocházelo k dalším incidentům.

Přehled incidentů ve vpsAdminu:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

Více informací o těchto incidentech:

  https://kb.vpsfree.cz/navody/vps/incidenty#oomd

S pozdravem

tým vpsFree.cz

(Tento mail automaticky rozesílá vpsAdmin, Tvoje odpověď se zašle na naši podporu)
```

## vps_oom_stopped en; enforcement=true; limits=5/10

```text
[vpsFree.cz] VPS 12345 stopped after repeated resource incidents

Hi example-member,

Your VPS 12345 example.vpsfree.cz was stopped after repeated resource incidents.

  Incidents in the last 7 days: 7 (warning limit: 5)
  Incidents in the last 30 days: 12 (stop limit: 10)
  Incident time: 2026-10-30 16:20:00 CET
  Stopped at: 2026-10-30 16:23:00 CET

This resource pressure affects other VPS on the same node and may disrupt their
services. Please review your VPS's memory usage and service configuration. A
common cause is a web server or application spawning more worker processes than
the available memory can support. Reducing the maximum number of workers may
resolve the problem.

If your workload needs more memory, you can increase your VPS's memory through a
membership expansion:

  https://kb.vpsfree.org/information/membership_fees#what_the_membership_fee_is_composed_of

The automatic stop also disabled autostart. You can start the VPS again in
vpsAdmin to adjust its configuration.
If another incident occurs while the total remains at or above 10 within the last
30 days, it will be stopped again, at most once per 24 hours. Once the total
falls below this limit, the usual limits apply again.

Incident history in vpsAdmin:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

More information about these incidents:

  https://kb.vpsfree.org/manuals/vps/incidents#oomd

Best regards,

vpsFree.cz team

(This is an automated mail from vpsAdmin, your reply will be sent to our support)
```

## vps_oom_stopped en; enforcement=true; limits=6/15

```text
[vpsFree.cz] VPS 12345 stopped after repeated resource incidents

Hi example-member,

Your VPS 12345 example.vpsfree.cz was stopped after repeated resource incidents.

  Incidents in the last 7 days: 7 (warning limit: 6)
  Incidents in the last 30 days: 12 (stop limit: 15)
  Incident time: 2026-10-30 16:20:00 CET
  Stopped at: 2026-10-30 16:23:00 CET

This resource pressure affects other VPS on the same node and may disrupt their
services. Please review your VPS's memory usage and service configuration. A
common cause is a web server or application spawning more worker processes than
the available memory can support. Reducing the maximum number of workers may
resolve the problem.

If your workload needs more memory, you can increase your VPS's memory through a
membership expansion:

  https://kb.vpsfree.org/information/membership_fees#what_the_membership_fee_is_composed_of

The automatic stop also disabled autostart. You can start the VPS again in
vpsAdmin to adjust its configuration.
If another incident occurs while the total remains at or above 15 within the last
30 days, it will be stopped again, at most once per 24 hours. Once the total
falls below this limit, the usual limits apply again.

Incident history in vpsAdmin:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

More information about these incidents:

  https://kb.vpsfree.org/manuals/vps/incidents#oomd

Best regards,

vpsFree.cz team

(This is an automated mail from vpsAdmin, your reply will be sent to our support)
```

## vps_oom_stopped en; enforcement=false; limits=5/10

```text
[vpsFree.cz] VPS 12345 stopped after repeated resource incidents

Hi example-member,

Your VPS 12345 example.vpsfree.cz was stopped after repeated resource incidents.

  Incidents in the last 7 days: 7 (warning limit: 5)
  Incidents in the last 30 days: 12 (stop limit: 10)
  Incident time: 2026-10-30 16:20:00 CET
  Stopped at: 2026-10-30 16:23:00 CET

This resource pressure affects other VPS on the same node and may disrupt their
services. Please review your VPS's memory usage and service configuration. A
common cause is a web server or application spawning more worker processes than
the available memory can support. Reducing the maximum number of workers may
resolve the problem.

If your workload needs more memory, you can increase your VPS's memory through a
membership expansion:

  https://kb.vpsfree.org/information/membership_fees#what_the_membership_fee_is_composed_of

The automatic stop also disabled autostart. You can start the VPS again in
vpsAdmin to adjust its configuration.

Incident history in vpsAdmin:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

More information about these incidents:

  https://kb.vpsfree.org/manuals/vps/incidents#oomd

Best regards,

vpsFree.cz team

(This is an automated mail from vpsAdmin, your reply will be sent to our support)
```

## vps_oom_stopped en; enforcement=false; limits=6/15

```text
[vpsFree.cz] VPS 12345 stopped after repeated resource incidents

Hi example-member,

Your VPS 12345 example.vpsfree.cz was stopped after repeated resource incidents.

  Incidents in the last 7 days: 7 (warning limit: 6)
  Incidents in the last 30 days: 12 (stop limit: 15)
  Incident time: 2026-10-30 16:20:00 CET
  Stopped at: 2026-10-30 16:23:00 CET

This resource pressure affects other VPS on the same node and may disrupt their
services. Please review your VPS's memory usage and service configuration. A
common cause is a web server or application spawning more worker processes than
the available memory can support. Reducing the maximum number of workers may
resolve the problem.

If your workload needs more memory, you can increase your VPS's memory through a
membership expansion:

  https://kb.vpsfree.org/information/membership_fees#what_the_membership_fee_is_composed_of

The automatic stop also disabled autostart. You can start the VPS again in
vpsAdmin to adjust its configuration.

Incident history in vpsAdmin:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

More information about these incidents:

  https://kb.vpsfree.org/manuals/vps/incidents#oomd

Best regards,

vpsFree.cz team

(This is an automated mail from vpsAdmin, your reply will be sent to our support)
```

## vps_oom_stopped cs; enforcement=true; limits=5/10

```text
[vpsFree.cz] VPS 12345 se vypnulo kvůli opakovaným incidentům

Ahoj example-member,

VPS 12345 example.vpsfree.cz se vypnulo kvůli opakovaným incidentům.

  Incidenty za posledních 7 dní: 7 (limit upozornění: 5)
  Incidenty za posledních 30 dní: 12 (limit vypnutí: 10)
  Čas incidentu: 2026-10-30 16:20:00 CET
  Čas vypnutí: 2026-10-30 16:23:00 CET

Taková zátěž ovlivňuje ostatní VPS na stejném nodu a může narušit provoz jejich
služeb. Zkontroluj prosím využití paměti a nastavení služeb ve VPS. Častou příčinou
je webový server nebo aplikace, která spouští více pracovních procesů, než kolik
dostupná paměť zvládne. Problém může vyřešit snížení maximálního počtu těchto procesů.

Pokud aplikace potřebují více paměti, můžeš paměť VPS navýšit rozšířením členství:

  https://kb.vpsfree.cz/informace/platby#z_ceho_se_sklada_clensky_poplatek

Při tomto vypnutí se také zakázalo automatické spouštění VPS. VPS můžeš znovu
spustit ve vpsAdminu a upravit jeho nastavení.
Pokud dojde k dalšímu incidentu a jejich počet za posledních 30 dní zůstane na 10
nebo výše, VPS se znovu vypne, nejvýše jednou za 24 hodin. Jakmile počet incidentů
klesne pod tento limit, opět platí běžné limity.

Přehled incidentů ve vpsAdminu:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

Více informací o těchto incidentech:

  https://kb.vpsfree.cz/navody/vps/incidenty#oomd

S pozdravem

tým vpsFree.cz

(Tento mail automaticky rozesílá vpsAdmin, Tvoje odpověď se zašle na naši podporu)
```

## vps_oom_stopped cs; enforcement=true; limits=6/15

```text
[vpsFree.cz] VPS 12345 se vypnulo kvůli opakovaným incidentům

Ahoj example-member,

VPS 12345 example.vpsfree.cz se vypnulo kvůli opakovaným incidentům.

  Incidenty za posledních 7 dní: 7 (limit upozornění: 6)
  Incidenty za posledních 30 dní: 12 (limit vypnutí: 15)
  Čas incidentu: 2026-10-30 16:20:00 CET
  Čas vypnutí: 2026-10-30 16:23:00 CET

Taková zátěž ovlivňuje ostatní VPS na stejném nodu a může narušit provoz jejich
služeb. Zkontroluj prosím využití paměti a nastavení služeb ve VPS. Častou příčinou
je webový server nebo aplikace, která spouští více pracovních procesů, než kolik
dostupná paměť zvládne. Problém může vyřešit snížení maximálního počtu těchto procesů.

Pokud aplikace potřebují více paměti, můžeš paměť VPS navýšit rozšířením členství:

  https://kb.vpsfree.cz/informace/platby#z_ceho_se_sklada_clensky_poplatek

Při tomto vypnutí se také zakázalo automatické spouštění VPS. VPS můžeš znovu
spustit ve vpsAdminu a upravit jeho nastavení.
Pokud dojde k dalšímu incidentu a jejich počet za posledních 30 dní zůstane na 15
nebo výše, VPS se znovu vypne, nejvýše jednou za 24 hodin. Jakmile počet incidentů
klesne pod tento limit, opět platí běžné limity.

Přehled incidentů ve vpsAdminu:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

Více informací o těchto incidentech:

  https://kb.vpsfree.cz/navody/vps/incidenty#oomd

S pozdravem

tým vpsFree.cz

(Tento mail automaticky rozesílá vpsAdmin, Tvoje odpověď se zašle na naši podporu)
```

## vps_oom_stopped cs; enforcement=false; limits=5/10

```text
[vpsFree.cz] VPS 12345 se vypnulo kvůli opakovaným incidentům

Ahoj example-member,

VPS 12345 example.vpsfree.cz se vypnulo kvůli opakovaným incidentům.

  Incidenty za posledních 7 dní: 7 (limit upozornění: 5)
  Incidenty za posledních 30 dní: 12 (limit vypnutí: 10)
  Čas incidentu: 2026-10-30 16:20:00 CET
  Čas vypnutí: 2026-10-30 16:23:00 CET

Taková zátěž ovlivňuje ostatní VPS na stejném nodu a může narušit provoz jejich
služeb. Zkontroluj prosím využití paměti a nastavení služeb ve VPS. Častou příčinou
je webový server nebo aplikace, která spouští více pracovních procesů, než kolik
dostupná paměť zvládne. Problém může vyřešit snížení maximálního počtu těchto procesů.

Pokud aplikace potřebují více paměti, můžeš paměť VPS navýšit rozšířením členství:

  https://kb.vpsfree.cz/informace/platby#z_ceho_se_sklada_clensky_poplatek

Při tomto vypnutí se také zakázalo automatické spouštění VPS. VPS můžeš znovu
spustit ve vpsAdminu a upravit jeho nastavení.

Přehled incidentů ve vpsAdminu:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

Více informací o těchto incidentech:

  https://kb.vpsfree.cz/navody/vps/incidenty#oomd

S pozdravem

tým vpsFree.cz

(Tento mail automaticky rozesílá vpsAdmin, Tvoje odpověď se zašle na naši podporu)
```

## vps_oom_stopped cs; enforcement=false; limits=6/15

```text
[vpsFree.cz] VPS 12345 se vypnulo kvůli opakovaným incidentům

Ahoj example-member,

VPS 12345 example.vpsfree.cz se vypnulo kvůli opakovaným incidentům.

  Incidenty za posledních 7 dní: 7 (limit upozornění: 6)
  Incidenty za posledních 30 dní: 12 (limit vypnutí: 15)
  Čas incidentu: 2026-10-30 16:20:00 CET
  Čas vypnutí: 2026-10-30 16:23:00 CET

Taková zátěž ovlivňuje ostatní VPS na stejném nodu a může narušit provoz jejich
služeb. Zkontroluj prosím využití paměti a nastavení služeb ve VPS. Častou příčinou
je webový server nebo aplikace, která spouští více pracovních procesů, než kolik
dostupná paměť zvládne. Problém může vyřešit snížení maximálního počtu těchto procesů.

Pokud aplikace potřebují více paměti, můžeš paměť VPS navýšit rozšířením členství:

  https://kb.vpsfree.cz/informace/platby#z_ceho_se_sklada_clensky_poplatek

Při tomto vypnutí se také zakázalo automatické spouštění VPS. VPS můžeš znovu
spustit ve vpsAdminu a upravit jeho nastavení.

Přehled incidentů ve vpsAdminu:

  https://vpsadmin.example.test/?page=incidents&action=list&list=1&vps=12345&codename=oomd

Více informací o těchto incidentech:

  https://kb.vpsfree.cz/navody/vps/incidenty#oomd

S pozdravem

tým vpsFree.cz

(Tento mail automaticky rozesílá vpsAdmin, Tvoje odpověď se zašle na naši podporu)
```

