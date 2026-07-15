# WebUI development shell working directory

The `vpsadmin` WebUI development shell changes the working directory to
`webui`. Run repository-relative WebUI commands from that directory, for
example:

```sh
nix develop .#webui --command lang/scripts/locales-update
```

Using `webui/lang/scripts/locales-update` after entering the shell resolves to
`webui/webui/lang/scripts/locales-update` and fails with “No such file or
directory”. This was verified while working on
`work/2026-07-13-security-advisory-automation`.
