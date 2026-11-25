# Shared incident escalation copy

Lead-applied vpsfree-user-facing-writing and EN/CS humanizer pass, 2026-10-30.
This supplies exact prose for the approved shared escalation rework. Technical
IDs/variables follow the released implementation contract. Preserve existing
site greeting, team signature, subject prefix and exact automated-mail notice;
core fallback uses its existing generic convention and contains no site branding,
membership links or external KB links.

## UI and type labels

| Meaning | English | Czech |
| --- | --- | --- |
| Registered memory-pressure type | VPS memory-pressure incidents | Incidenty přetížení paměti VPS |
| Generic section | Incident escalation | Opatření při opakovaných incidentech |
| Type label | Incident type | Typ incidentu |
| Settings heading | Incident settings | Nastavení incidentů |
| Save | Save incident settings | Uložit nastavení incidentů |
| Unavailable | Incident settings unavailable | Nastavení incidentů není dostupné |
| Saved | Incident settings saved | Nastavení incidentů bylo uloženo |
| Failure | Unable to save incident settings | Nepodařilo se uložit nastavení incidentů |
| Mixed update error | Update incident settings separately from other VPS properties. | Nastavení incidentů měň odděleně od ostatních vlastností VPS. |

Shared physical-state help EN: `Automatic shutdown permission, the cooldown and any unfinished shutdown are shared across incident types for this VPS.`

Shared physical-state help CS: `Povolení automatického vypínání, ochranná lhůta a dosud nedokončené vypnutí jsou společné pro všechny typy incidentů tohoto VPS.`

Generic exemption help EN: `An exemption disables automatic shutdowns by vpsAdmin for repeated incidents. Incident collection and warnings remain active.`

Generic exemption help CS: `Výjimka vypíná automatická vypnutí ve vpsAdminu kvůli opakovaným incidentům. Sběr incidentů a upozornění zůstávají aktivní.`

For the memory-pressure rule, preserve this additional fact as type-specific
help EN: `The node's memory protection remains active.` CS:
`Ochrana paměti na nodu zůstává aktivní.` Do not attach this specific claim to
unrelated generic incident types.

Keep existing accepted status/count/cooldown/restart help where its facts remain
identical. Replace new-feature OOM headings with the type label or generic section
as appropriate. Existing individual OOM-report names and protocol IDs remain.

## Generic warning

Subject EN: `Action required: repeated incidents on VPS <%= @vps.id %>`

Subject CS: `Je potřeba zásah: opakované incidenty ve VPS <%= @vps.id %>`

English body between existing greeting and signature:

```erb
Repeated incidents have been reported for your VPS <%= @vps.id %> <%= @vps.hostname %>.

  Incident type: <%= @incident_type_label %>
  Incidents in the last <%= @warning_period_days %> days: <%= @incident_count_7d %> (warning limit: <%= @warning_limit %>)
  Incidents in the last <%= @stop_period_days %> days: <%= @incident_count_30d %> (stop limit: <%= @stop_limit %>)
  Incident time: <%= local_time(@incident_at, '%Y-%m-%d %H:%M:%S %Z') %>

Please review the incident reports and address their cause to prevent further incidents.
<% if @stop_enforced -%>
If a new incident of this type brings the total to <%= @stop_limit %> or more within <%= @stop_period_days %> days,
your VPS will be stopped automatically. If you start it again and incidents of
this type continue while it remains at or above this limit, it will be stopped
again, at most once per <%= @repeat_stop_hours %> hours.
<% end -%>

Incident history in vpsAdmin:

  <%= @base_url %>?page=incidents&action=list&list=1&vps=<%= @vps.id %>&codename=<%= @incident_type %>
```

Czech body:

```erb
Ve VPS <%= @vps.id %> <%= @vps.hostname %> byly zaznamenány opakované incidenty.

  Typ incidentu: <%= @incident_type_label %>
  Incidenty za posledních <%= @warning_period_days %> dní: <%= @incident_count_7d %> (limit upozornění: <%= @warning_limit %>)
  Incidenty za posledních <%= @stop_period_days %> dní: <%= @incident_count_30d %> (limit vypnutí: <%= @stop_limit %>)
  Čas incidentu: <%= local_time(@incident_at, '%Y-%m-%d %H:%M:%S %Z') %>

Prohlédni si prosím přehled incidentů a vyřeš jejich příčinu, aby nedocházelo k dalším.
<% if @stop_enforced -%>
Pokud nový incident tohoto typu zvýší jejich počet za posledních <%= @stop_period_days %> dní na <%= @stop_limit %> nebo více,
VPS se automaticky vypne. Pokud VPS znovu spustíš a incidenty tohoto typu budou
pokračovat, dokud jejich počet zůstává na tomto limitu nebo nad ním, VPS se znovu
vypne, nejvýše jednou za <%= @repeat_stop_hours %> hodin.
<% end -%>

Přehled incidentů ve vpsAdminu:

  <%= @base_url %>?page=incidents&action=list&list=1&vps=<%= @vps.id %>&codename=<%= @incident_type %>
```

## Generic stopped notification

Subject EN: `VPS <%= @vps.id %> stopped after repeated incidents`

Subject CS: `VPS <%= @vps.id %> se vypnulo kvůli opakovaným incidentům`

Use the warning body's type/count/time block and add actual stop time after
incident time, following existing accepted localized formatting. Opening EN:
`Your VPS <%= @vps.id %> <%= @vps.hostname %> was stopped after repeated incidents.`
Opening CS:
`VPS <%= @vps.id %> <%= @vps.hostname %> se vypnulo kvůli opakovaným incidentům.`

Replace the warning advice/consequence block with EN:

```erb
Please review the incident reports and address their cause. The automatic stop
also disabled autostart. You can start the VPS again in vpsAdmin to investigate
and resolve the problem.
<% if @stop_enforced -%>
If another incident of this type occurs while the total remains at or above
<%= @stop_limit %> within the last <%= @stop_period_days %> days, it will be stopped again, at most once per
<%= @repeat_stop_hours %> hours. Once the total falls below this limit, the usual limits apply again.
<% end -%>
```

Czech:

```erb
Prohlédni si prosím přehled incidentů a vyřeš jejich příčinu. Při tomto vypnutí se
také zakázalo automatické spouštění VPS. VPS můžeš znovu spustit ve vpsAdminu,
zjistit příčinu a vyřešit problém.
<% if @stop_enforced -%>
Pokud dojde k dalšímu incidentu tohoto typu a jejich počet za posledních <%= @stop_period_days %> dní
zůstane na <%= @stop_limit %> nebo výše, VPS se znovu vypne, nejvýše jednou za <%= @repeat_stop_hours %> hodin.
Jakmile počet incidentů klesne pod tento limit, opět platí běžné limity.
<% end -%>
```

Keep generic advice independent of memory, worker counts, other VPS effects or
membership. Specific memory-pressure templates retain the approved current EN/CS
memory/configuration/worker/membership and KB paragraphs, current-enforcement
condition and past autostart effect. Rename their IDs to the new specific pair;
no wholesale prose rewrite is needed. Existing specific codename links stay oomd.
Registry-derived incident_type is a fixed safe key, never a free-form report
codename interpolated into template selection; if the contract permits keys
needing URL encoding, owner must encode the query value using existing tooling.
Core generic fallback need only EN per existing fallback convention; site owns
both languages. Specific core memory-pressure fallback retains generic memory
advice and internal incident link, omitting site branding/KB/membership content.
