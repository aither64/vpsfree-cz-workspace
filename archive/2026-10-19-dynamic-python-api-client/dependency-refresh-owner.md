# Dependency refresh: committed owner receipt

2026-10-20; implementer1. Source is committed and paused for the lead's retained
independent general/architecture and history review. No long test suite or
feature push has been started for this follow-up.

- Base: `c1823f3d70365b0442d0e2171bdf83bd4c6dbe31`, already merged history.
- Head: `18331877660ed0f736a25b29914756da89df0df9`.
- Tree: `320fc303f5ae2af73bc34139a918cccf1ea4b254`.
- Held repository claim: `342cd062-0205-45c7-b636-20d958b8fa75`.
- Clean source/index; all owned commands have exited. The lead owns the claim.
- Remote master and feature still equal the base; nothing pushed or merged.

## Complete new series and scope

1. `67ecb6797c2794113b078044395d7a2ed54dfda2` — select explicit Ruby 3.4 in
   exactly three native shell declarations. Accepted design amendment resolves
   current nixpkgs removing Ruby 3.3; no Ruby minimum or CI matrix change.
2. `7b7697e5c2dbb82d120cb5fa321d67b489d59a3e` — retain the updater's exact
   generated nixpkgs lock, `fe13242281a67641c0102cdb1087f0ebe586c7df` to
   `02c087f3fe673c9e317f206a627cb6b910336dbe`, with its required commit subject.
3. `18331877660ed0f736a25b29914756da89df0df9` — update the exact Ruff pin,
   certifi/Ruff resolution and matching contributor version note.

Final diff: five files, +31/-31. Only `flake.nix`, `flake.lock`,
`clients/python/pyproject.toml`, `clients/python/uv.lock` and
`clients/python/CONTRIBUTING.md` changed. Binary diff SHA256:
`4173a3192a284571f6eaec0d1bc6df5ff126e2d3a550b9e3d669634399d12a28`.

[Series](verification/dependency-refresh/followup-series.txt),
[diff](verification/dependency-refresh/followup.diff) and
[package inventory](verification/dependency-refresh/package-inventory.json)
contain the exact new range. There are no obsolete fixes, repeated new update
streams or migrations. The original eight merged commits remain intact; no
merged history was rewritten. Each new stream has one owning commit.

| Dependency | Before | After |
| --- | --- | --- |
| certifi | 2026.10.18 | 2026.10.19 |
| Ruff | 0.16.10 | 0.17.1 |
| Native Ruby | 3.3 selection | 3.4.11 from refreshed input |

uv remains 0.13.1; lock format 1/revision 5 is preserved. All 25 other Python
package versions are unchanged. The 24 other non-project package records are
equal; project metadata only changes the Ruff specifier. Shared/package version
remains 0.29.0. Runtime dependency ranges, Python minimum, backend range,
protocol/authentication code, CI and release behavior are unchanged. The certifi
CA bundle change is intended; certificate verification remains enabled.

## Verification and recovery evidence

- Fresh setup utility passed in 141 seconds: normal flake check; ordinary
  declared Ruby 3.4 root, server, Ruby-client, Go-generator and Python hook
  environments; Bundler and native-extension/application load smokes. Existing
  root/server locks and exact generated/source hashes were preserved. Initial
  client/Go ignored locks were created through ordinary setup and hashed.
  [Watcher receipt](verification/dependency-refresh/ruby34-attempt2-watcher-last.md).
- `nix develop .#client-python --command bash -euo pipefail -c
  'cd clients/python; ./utils/check.sh'` passed: 38 formatted files, clean Ruff
  lint, 18 strict mypy modules and 261 unit tests in 1.60 seconds. No formatter
  fallout or application/test changes.
  [Quick log](verification/dependency-refresh/python-quick-check.log).
- Normal Ruff entrypoint confirms native/locked 0.17.1 parity. certifi reports
  2026.10.19 and loads 120 CA certificates into a standard SSL context with
  hostname checking and `CERT_REQUIRED` intact.
  [Smoke log](verification/dependency-refresh/ruff-certifi-smoke.log).
- All three commits used normal hooks and `git commit -F`. PythonChecks and
  HaveapiI18n passed for the Python commit. The compatibility commit had one
  advisory message-width warning for a body line within the workspace's
  80-column limit; hooks passed. Other commit-message checks passed.

The original updater failed at removed Ruby 3.3 before committing; its generated
lock was preserved exactly rather than restored or blindly regenerated. Setup
attempt 1 was canceled for the diagnosed frozen-first-install recipe error;
its completed all-systems no-build evaluation remains useful, while the
interrupted later check is not a source failure. Its script/log/status are
preserved separately from the successful corrected setup attempt.

The retired external hook environment no longer had its gem home. Compatibility
commit preparation then used the working ordinary native environment. Workspace
claim CLI reads needed Ruby/Bundler variables cleared so the packaged workspace
Ruby did not load project native gems; actual Git/hooks kept their declared
project environment. Custom hooks/configuration were compared to reviewed
bytes and signed through ordinary Overcommit in Ruby 3.4; signature verification
stayed enabled. These were environment/trust corrections, with no bypass,
manual signature values or runtime source change. Failure/signing/success logs
remain under `verification/dependency-refresh/`.

Only the contributor's exact version mention needed updating; no new product
behavior or operational procedure was introduced. Longer Ruby/Python integration,
standalone package and release checks await committed-deliverable review and a
fresh utility. No vpsAdmin rerun is planned absent a concrete concern.

No release, tag, registry, protected environment, PR, deployment, default-branch
change or lifecycle action was performed. Recovery refs, retained stash, old
coordinator payloads and unrelated files remain preserved.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-dynamic-python-api-client/>
