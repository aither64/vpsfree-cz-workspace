# vpsAdmin WebUI development shell changes directory

Related initiative: `work/2026-07-13-security-advisory-automation`

`nix develop .#webui` enters the `webui/` component directory automatically.
Running `composer --working-dir=webui test` from that shell therefore fails with
`Invalid working directory specified, webui does not exist`.

Run the suite from the repository root with:

```sh
nix develop .#webui -c composer test
```

This completed the WebUI suite successfully (72 tests, 277 assertions).
