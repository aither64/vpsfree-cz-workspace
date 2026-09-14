# Query only the needed test metadata

Initiative: `work/2026-09-13-auth-email/`.

`nix eval .#testsMeta.x86_64-linux --json` successfully evaluated the entire
vpsAdmin test inventory, but took several minutes when checking one new WebUI
script. The result is an attribute set keyed by suite name. Prefer selecting
the suite directly when only its script names and tags are needed:

```sh
nix eval .#testsMeta.x86_64-linux.webui --json
```

Inspect `tags` on the suite and `testScripts.<script>.tags` on the script.
`webui#auth-email` inherits `ci` from the suite and has `auth`, `webui-auth`
and `webui-auth-email`. CI selector tests and Nix parsing remain separate quick
checks. Full inventory evaluation is appropriate when checking global coverage.
