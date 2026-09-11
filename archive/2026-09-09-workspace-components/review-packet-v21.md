# Mandatory change review packet: boot-safe substrate idempotency

## Outcome and acceptance criteria

Complete the extraction of reusable workspace tooling into the public
`dev-workspace` and `codex-web` repositories while keeping the vpsFree
workspace a thin compatible consumer. The final aitherdev deployment must
preserve the existing password, CA, authentication meaning, TLS identity,
runtime/session state, URLs and service identities. Reconciliation must work
during boot, remain idempotent across host locales and safely replace invalid
derived bcrypt state.

## Initiative and exact ranges

- Slug: `2026-09-09-workspace-components`.
- Plan and state: `work/2026-09-09-workspace-components/plan.md` and
  `work/2026-09-09-workspace-components/state.md`.
- `codex-web` worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/codex-web`.
  Review `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..e8655b7b2689da9b1aabe10df69858c32725dd61`
  (`690ff7d`, `a1721f5`, `a44ec2b`, `994b636`, `e8655b7`); unchanged.
- `dev-workspace` worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/dev-workspace`.
  Review `f39f8e62097b5e9da9de8a5eb678131b1e478e35..efff4d2dd683d3de85cb38461314ba70b78e33af`
  (`a695d7e`, `f36bd84`, `fa5f7d4`, `de0441b`, `21831fd`,
  `f8b2b0c`, `9ff2b54`, `c804c83`, `32cb196`, `d5e0f62`,
  `b3040c5`, `efff4d2`).
- `vpsfree-cz-workspace` worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/workspace`.
  Review `26606cfa0134ce3680cf592f9ab3c345683fbdc2..6acc69dfe9de139b61f2d2402cbc9f2cc02595e7`
  (`bfd618c`, `4a23ecc`, `6acc69d`). The branch is a descendant of
  shared `master@26606cf`.
- `vpsfree-cz-configuration` worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration`.
  Review `7481618dacab04bfd5b09bc730c373c2d2bf14d7..ab29e61a001b16856cfa12b3c7729090f2213db3`
  (`986a93d7`, `710a2fba`, `ab29e61a`).

All worktrees are clean and equal their pushed feature refs. Exact dependency
direction and pins are:

`vpsfree-cz-workspace@6acc69d -> dev-workspace@efff4d2 -> codex-web@e8655b7`

Configuration `ab29e61a` pins `dev-workspace@efff4d2` with NAR
`sha256-QGt0G8MrU8ZnNt/+mfNVF02pG8W8yDi5fcWmGUv2WVc=` and therefore the same
nested `codex-web@e8655b7` revision.

## Commit ownership and public boundaries

- `codex-web` owns the public Go App Server client, browser conversation
  module, path contract and provider-neutral example.
- `dev-workspace` owns reusable lifecycle/cluster tooling, the portal host,
  the NixOS substrate module and provider extension interfaces. Commit
  `efff4d2` owns reconciliation behavior and its provider-level regression.
- `vpsfree-cz-workspace` retains only policy, records, provider capabilities
  and the exact reusable package pin.
- `vpsfree-cz-configuration` owns aitherdev module consumption and its exact
  input pin. The pin commit was generated only by
  `confctl inputs channel set --commit`.

The intended retained histories are the commit lists above. Implementation,
tests and documentation are separated by their owning component; dependency
pins remain in the consumer repositories that require them.

## Delta and verification since v20

Packet v20 added an executable provider-owned VM test but was superseded before
reviewer conclusions. Exact-head GitHub Actions run `34463804815` then failed
deterministically during that VM's boot activation because the configured
`/run/lock` parent did not yet exist. The dependent nginx service consequently
failed. The remediation:

- derives the configured lock-file parent and creates it as root with mode 0755
  before opening and locking the file, including during boot activation;
- accepts the precise Apache `htpasswd -niBC 12` output shape: one credential
  line followed by at most one empty terminator, while rejecting a second
  entry, extra empty lines, the wrong user, malformed bcrypt or a password
  mismatch;
- retains stdin-only password verification and generation, same-directory
  atomic replacement and the single-quoted bcrypt ERE;
- retains byte-stable `LC_ALL=C` SAN sorting;
- runs the real NixOS module under `en_US.UTF-8`, including boot, two stable
  reconciliations and stable one-time recovery of malformed, mispermissioned,
  misowned and password-mismatching authentication state.

Quick verification at `dev-workspace@efff4d2`:

- `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check flake.nix nix/host-module.nix`
  passed;
- `git diff --check` passed;
- `nix flake check --no-build --show-trace` evaluated all packages, the
  example module and the VM check successfully;
- `nix build .#checks.x86_64-linux.host-module --no-link --print-build-logs`
  passed, including generated-script ShellCheck and the fast bcrypt check;
- `nix build .#checks.x86_64-linux.host-module-idempotency --no-link --print-build-logs`
  passed in 62.49 seconds. It booted the module, exercised every recovery case
  above and preserved password, bcrypt, CA key/certificate, public CA, leaf
  key/certificate and the `current` target. It used cached NixOS VM kernel and
  initrd outputs and did not build a kernel.

## Compatibility, deployment and non-goals

Risk is **high** because this changes authentication-derived state, TLS
persistence, host activation, deployment and rollback behavior. All reviewers
must use `gpt-5.6-sol` at `xhigh`.

The password, CA, credential meaning, paths, owners, modes, certificate format,
SAN set and mixed-generation compatibility remain unchanged. New generations
preserve valid derived state; old generations remain able to consume it but
would resume harmless bcrypt and leaf churn on rollback. The retained original
TLS pair will be validated and atomically selected only after the fixed module
is deployed. Two reconciliations under `en_US.UTF-8` must then preserve its
exact hashes and target. Deployment is limited to aitherdev and uses
configuration dry activation before switching, followed by the stable
installed `workspace-host switch` for the user profile.

Rejected alternatives were unconditional bcrypt regeneration,
locale-dependent SAN comparison, tolerating multiple persisted credential
formats, passing the password as an argument, or moving host behavior into the
thin workspace consumer. Default-branch integration, releases, archive,
delete and session stop remain out of scope. The user authorized aitherdev
deployment only.

## Review request

Run all four required lanes: General, Architecture/repetition,
Scope/proportionality and Risk/compatibility. Focus on boot ordering and lock
creation, the exact Apache output validation, secret handling, file
validation/replacement, locale-stable SAN equality, retained-leaf restoration,
the VM test's fidelity, commit boundaries, exact pins and whether the
remediation is proportional. Report Blocking, Important and Advisory findings
with evidence and remediation; explicitly report a clean lane.
