# vpsAdmin WebUI development shell changes directory

- Command: `nix develop .#webui --command bash -lc 'webui/lang/scripts/locales-update'`
- Symptom: the shell reports `webui/lang/scripts/locales-update: No such file or
  directory` even though the path exists from the repository root.
- Cause: the `.#webui` development shell changes its working directory to the
  repository's `webui/` directory before running the command.
- Workaround: use paths relative to `webui/`, for example
  `nix develop .#webui --command bash -lc 'lang/scripts/locales-update'`.
- Verification: the relative command regenerated and health-checked the WebUI
  catalogs successfully.
- Initiative: `work/2026-07-10-czech-translation-fixes/`.
