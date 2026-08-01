# Test framework and CI integration

## Goal

Merge the reusable vpsAdminOS test-runner and workflow improvements into the
default branches of all affected repositories, while keeping vpsAdmin event
work on `2026-06-15-vpsadmin-events` branches.

## Repositories

- `vpsadminos`: shared test-runner behavior, CI actions, workflow adoption,
  NixOS test stability, and symmetric bounded OSVM command retries.
- `vpsadmin`, `confctl`, `terraform-provider-vpsadmin`, `vpsfree-irc-bot`:
  cancellation-safe logs, current checkout action, and direct adoption of the
  shared state lifecycle.
- `vpsadminos-org-configuration`: prevent scheduled Nix garbage collection
  from overlapping self-hosted runner jobs.

## Decisions

- Drop the one-path Nix store repair workaround. Fix GC coordination in runner
  configuration instead.
- Squash every inline state preparation commit into its later shared-lifecycle
  conversion, including the vpsAdminOS action implementation and local use.
- Keep `stop_on_failure` opt-in and disabled by default.
- Add `fails_with_retries` as the symmetric counterpart to
  `succeeds_with_retries` on both OSVM shell and machine APIs.
- Improve the initrd coldplug commit message with the observed module-loading
  crash and root-disk consequence.
- Merge, but do not deploy, the runner configuration change.
- Do not wait for obsolete multi-hour vpsAdmin aggregate CI runs.

## Compatibility and deployment

The test framework changes are additive CI/test interfaces. They change no
database schema, application API, persisted state, host daemon protocol, or
deployed vpsAdminOS module option. The initrd coldplug setting affects generated
test VMs only. Runner GC protection becomes effective only after a later
activation of `vpsadminos-org-configuration`; until then, existing runners can
still encounter the diagnosed GC race.

No coordinated update of production nodes is required. Rollback removes CI
helpers and configuration hooks without changing application state.

## Integration order

1. Merge `vpsadminos` into `staging`.
2. Merge `vpsadmin` and `confctl` with final `vpsadminos` pins.
3. Merge the Terraform provider and IRC bot with final `vpsadmin` pins.
4. Merge `vpsadminos-org-configuration` without activating it.
5. Rebase every existing `2026-06-15-vpsadmin-events` branch onto its updated
   default branch and regenerate dependent pins.

## Commits to integrate

`vpsadminos` into `staging`:

1. `test-runner: name unexpected suite results`
2. `github: share image test result evaluation`
3. `github: retain interrupted test logs`
4. `github: update checkout action`
5. `github: quote workflow output paths`
6. `tests: bound module-autoload log assertion`
7. `github: centralize CI test state lifecycle`
8. `tests: serialize NixOS initrd coldplug`
9. `osvm: add bounded command retries`

`vpsadmin` into `master`:

1. `github: retain interrupted test logs`
2. `github: update checkout action`
3. `github: use shared CI test state lifecycle`
4. `tests: avoid implicit logout navigation wait`
5. `flake: vpsadminos 736f68939 -> 0b102133b`

`confctl` into `master`:

1. `github: retain interrupted test logs`
2. `github: update checkout action`
3. `github: use shared CI test state lifecycle`
4. `flake: vpsadminos 6f9b2c755 -> 0b102133b`

`terraform-provider-vpsadmin` into `master`:

1. `github: retain interrupted test logs`
2. `github: update checkout action`
3. `github: use shared CI test state lifecycle`
4. `flake: vpsadmin cba29b57c -> 47fc93e3d`

`vpsfree-irc-bot` into `master`:

1. `github: retain interrupted test logs`
2. `github: update checkout action`
3. `github: use shared CI test state lifecycle`
4. `Update advisory fixture publication contract`
5. `flake: vpsadmin bb38a42cd -> 47fc93e3d`

`vpsadminos-org-configuration` into `master`:

1. `gh-runner: defer Nix GC while jobs run`

## Verification

Run repository hooks, focused unit/spec checks, workflow syntax and shell
checks, Nix evaluation/build checks, and a standalone mandatory change review.
Use focused exact-head CI without making the long vpsAdmin aggregate run a
merge gate. Verify final commit trees, dependency pins, and event-branch
ancestry/range-diffs.
