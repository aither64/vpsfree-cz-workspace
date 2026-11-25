# G-PHP visible string handoff

Root owns this exclusive writing window. Implementer4 freezes visible text and catalog while root edits.

## Changed feature strings

```po
#: forms/incident_policy.forms.php
msgid "Shutdown limit reached"
msgstr "Dosažen limit pro vypnutí"
```

```po
#: forms/incident_policy.forms.php forms/incidents.forms.php
msgid "View incidents"
msgstr "Zobrazit incidenty"
```

```po
#: forms/incident_policy.forms.php forms/incidents.forms.php
msgid "Automatic shutdown"
msgstr "Automatické vypínání"
```

```po
#: forms/incident_policy.forms.php forms/incidents.forms.php
msgid "Incident history"
msgstr "Historie incidentů"
```

```po
#: forms/incident_policy.forms.php
msgid "Policy settings"
msgstr "Nastavení pravidla"
```

```po
#: forms/incident_policy.forms.php
msgid "Shutdown limit"
msgstr "Limit pro vypnutí"
```

```po
#: forms/incident_policy.forms.php
msgid "Warning limit"
msgstr "Limit pro upozornění"
```

```po
#: forms/incident_policy.forms.php
msgid "Leave a field empty to inherit its limit."
msgstr "Prázdné pole použije výchozí limit."
```

```po
#: forms/incident_policy.forms.php
msgid "Limits"
msgstr "Limity"
```

```po
#: forms/incident_policy.forms.php
msgid "Use inherited limits"
msgstr "Použít výchozí limity"
```

```po
#: forms/incident_policy.forms.php
msgid "Allow automatic shutdown"
msgstr "Povolit automatické vypínání"
```

```po
#: forms/incident_policy.forms.php
msgid "Last automatic shutdown"
msgstr "Poslední automatické vypnutí"
```

```po
#: forms/incident_policy.forms.php forms/vps.forms.php pages/page_incidents.php
msgid "Incidents"
msgstr "Incidenty"
```

```po
#: forms/incident_policy.forms.php
msgid "Incident limits are misconfigured."
msgstr "Limity incidentů nejsou správně nastavené."
```

```po
#: forms/incident_policy.forms.php forms/incidents.forms.php
#, php-format
msgid "Incidents in %d day"
msgid_plural "Incidents in %d days"
msgstr[0] "Incidenty za %d den"
msgstr[1] "Incidenty za %d dny"
msgstr[2] "Incidenty za %d dní"
```

```po
#: forms/incident_policy.forms.php
msgid "Unable to save changes"
msgstr "Změny se nepodařilo uložit"
```

```po
#: forms/incidents.forms.php
#| msgid "Records"
msgid "Recorded"
msgstr "zaznamenáno"
```

```po
#: forms/incidents.forms.php
#| msgid "VPS action"
msgid "No action"
msgstr "žádná akce"
```

```po
#: forms/incidents.forms.php
#| msgid "Version"
msgid "Decision"
msgstr "Rozhodnutí"
```

## Preserved meaning

Queued warning, confirmed shutdown, pending/failed/uncertain physical outcome labels retain existing translations. Current policy labels/descriptions come from escaped API metadata. Live counts/limits stay separate from historical evaluation rows.

## Scope

Source visible strings: `webui/forms/incident_policy.forms.php`, `webui/forms/incidents.forms.php`; sidebar `webui/forms/vps.forms.php`, routes in `webui/pages/page_adminvps.php` and `webui/pages/page_incidents.php`. Catalog: `webui/lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.po`, generated `vpsAdmin.pot` and `.mo`. Existing shared labels remain unchanged except exact approved strings.

Views: actual PHP/XTemplate with synthetic real HaveAPI client responses, two arbitrary keys, admin/member, CS/EN. No live API/runner/reset. Files `admin-en-{390,1280}.png`, `member-cs-{390,1280}.png` and matching combinations. Legacy template viewport remains1150.
