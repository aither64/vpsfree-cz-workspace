# 2026-08-07 exporters gem update

## Goal

Update ssh-exporter and syslog-exporter to a supported Ruby baseline and a
Puma release that fixes CVE-2026-47736 and CVE-2026-47737, then consume the
exact exporter commits from vpsfree-cz-configuration.

## Affected repositories

- `ssh-exporter`
- `syslog-exporter`
- `vpsfree-cz-configuration`

All repositories use branch `2026-08-07-exporters-gem-update` and worktrees
under `worktrees/2026-08-07-exporters-gem-update/`.

## Approach

- Require Ruby 3.4, prometheus-client 4.2.5 or newer in the 4.2 series,
  Puma 8.0.2 or newer in the 8.x series, and Rack 3.2 or newer in the 3.x
  series in both exporters.
- Remove the obsolete direct `rubygems-generate_index` workaround, update the
  development shell and CI to Ruby 3.4, and bump patch versions to 0.3.2 and
  0.13.4.
- Push the exporter commits, pin both configuration packages to those exact
  Git revisions, and regenerate their lockfiles and Bundix gemsets.
- Keep one focused commit in each exporter and separate configuration commits
  for the two generated package updates.

## Compatibility and deployment

- The public Ruby compatibility floor changes from 3.1 to 3.4. The current
  nixos-stable input provides Ruby 3.4.9, so known deployments are compatible.
- Puma's PROXY Protocol v1 mode implicated by the advisories is not enabled by
  either service. The update still removes the vulnerable package from the
  closure.
- Both modules bind explicit IPv4 addresses, so Puma 8's default bind change
  does not alter service exposure. The exporters run in single mode and use no
  renamed cluster hooks.
- There are no persisted-state, schema, API, protocol, metric, or
  configuration-format changes. Old and new Nix generations can coexist, and
  rollback restores the old package closure.
- Merge and push exporter masters before configuration master. No production
  deployment is part of this initiative. No coordinated vpsAdminOS update is
  required.

## Testing plan

- In each exporter: resolve dependencies under Ruby 3.4, run RSpec and the
  default Rake task, build the gem, audit a disposable lockfile, run actionlint,
  and run installed Overcommit hooks.
- In vpsfree-cz-configuration: regenerate with Bundix, run nixfmt and
  Overcommit, audit both package locks, build both packages, smoke-test Puma,
  and run targeted confctl builds for `cz.vpsfree/machines/build` and
  `cz.vpsfree/containers/prg/int.log`.
- Monitor feature and master GitHub Actions runs and investigate any failures.
- The mandatory change review is skipped under its dependency-only exemption:
  this session changes dependency constraints, compatibility metadata, CI
  version selection, and generated package locks, but no application code or
  design.
