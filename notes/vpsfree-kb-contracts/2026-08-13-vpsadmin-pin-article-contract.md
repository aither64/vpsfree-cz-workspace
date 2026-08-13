# vpsAdmin pins must include the article contract

Initiative: `work/2026-08-12-dns-secondary-zone-transfer-failure`

Command:

```sh
nix develop -c bin/check
```

Symptom: after updating the vpsAdmin revision in `flake.nix`, `flake.lock`,
`captures.json`, and `contract/navigation.yml`, the check failed with
`vpsadmin revision differs` from the article-contract checker.

Cause: `contract/articles.yml` has its own `revisions.vpsadmin` provenance pin.

Fix: update that field to the same exact commit and run `bin/check` again. The
canonical WebUI workflow now lists this file explicitly. Verification passed
with the navigation, article, test, and screenshot inventories green.
