# WebUI dev shell changes the working directory

Command: `nix develop .#webui -c webui/lang/scripts/locales-update` from the
vpsAdmin repository root.

Symptom: the command tried to execute `webui/webui/lang/scripts/locales-update`.

Cause: the `.#webui` development shell changes the command's working directory
to the `webui/` component before running it.

Use component-relative paths inside the shell, for example
`nix develop .#webui -c lang/scripts/locales-update`. The corrected command was
verified by regenerating the WebUI gettext catalogs for initiative
`work/2026-06-15-vpsadmin-events/`.
