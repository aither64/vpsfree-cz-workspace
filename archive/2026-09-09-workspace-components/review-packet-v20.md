# Mandatory change review packet: executable substrate idempotency coverage

## Outcome and acceptance criteria

Complete the extraction of reusable workspace tooling into the public
`dev-workspace` and `codex-web` repositories while keeping the vpsFree
workspace a thin compatible consumer. The final aitherdev deployment must
preserve the existing password, CA, authentication meaning, TLS identity,
runtime/session state, URLs and service identities. Reconciliation must be
idempotent across host locales and safely replace invalid derived bcrypt state.

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
  Review `f39f8e62097b5e9da9de8a5eb678131b1e478e35..4cb5f58ce24c0e2ce9fe5de4bc4ebf8cec7f0611`
  (`a695d7e`, `f36bd84`, `fa5f7d4`, `de0441b`, `21831fd`,
  `f8b2b0c`, `9ff2b54`, `c804c83`, `32cb196`, `d5e0f62`,
  `b3040c5`, `4cb5f58`).
- `vpsfree-cz-workspace` worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/workspace`.
  Review `26606cfa0134ce3680cf592f9ab3c345683fbdc2..255b43de85e385652632dfecaea5644d9be59980`
  (`bfd618c`, `4a23ecc`, `255b43d`). The branch was rebased onto the
  current shared `master` immediately before this review.
- `vpsfree-cz-configuration` worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration`.
  Review `7481618dacab04bfd5b09bc730c373c2d2bf14d7..770ff95fba7eb9bd59094d680a2f5c84e0bd1984`
  (`986a93d7`, `710a2fba`, `770ff95f`).

All worktrees are clean and equal their pushed feature refs. Exact dependency
direction and pins are:

`vpsfree-cz-workspace@255b43d -> dev-workspace@4cb5f58 -> codex-web@e8655b7`

Configuration `770ff95f` pins `dev-workspace@4cb5f58` with NAR
`sha256-jSES0Giv4MfbGHmREJZebdkqpELYkp+tGNktdeMK/LA=` and therefore the same
nested `codex-web@e8655b7` revision.

## Commit ownership and public boundaries

- `codex-web` owns the public Go App Server client, browser conversation
  module, path contract and provider-neutral example.
- `dev-workspace` owns reusable lifecycle/cluster tooling, the portal host,
  the NixOS substrate module and provider extension interfaces. Commit
  `4cb5f58` owns both the reconciliation behavior and its provider-level
  regression because the test exercises that module's persistent-state
  contract.
- `vpsfree-cz-workspace` retains only policy, records, provider capabilities
  and the exact reusable package pin.
- `vpsfree-cz-configuration` owns the aitherdev module consumption and exact
  input pin. The pin commit was regenerated only by
  `confctl inputs channel set --commit`.

The intended retained histories are the commit lists above. Implementation,
tests and documentation are separated by their owning component; dependency
pins remain in the consumer repositories that require them.

## Delta and quick verification since v19

Review v19 found that the bcrypt ERE was double-quoted, causing shell parsing
to turn its literal dollar signs into end anchors, and that string greps did
not execute the persistent-state contract. The remediation:

- stores the bcrypt ERE in one single-quoted shell variable and uses it for
  both acceptance and post-replacement validation;
- retains stdin-only `htpasswd` verification and generation plus same-directory
  atomic replacement;
- adds a provider-owned NixOS VM test that boots the module with a wildcard and
  alias under `en_US.UTF-8`, runs reconciliation twice, and compares the
  password, bcrypt, CA key/certificate, public CA, leaf key/certificate and
  `current` target;
- exercises malformed, mispermissioned, misowned and syntactically valid but
  password-mismatching htpasswd entries, validates each replacement, and proves
  the replacement is stable on the next reconciliation;
- keeps generated-script assertions and a small two-pass bcrypt check as fast
  supplementary coverage.

Quick verification at `dev-workspace@4cb5f58`:

- `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check flake.nix nix/host-module.nix`
  passed after formatting;
- `git diff --check` passed;
- `nix flake check --no-build --show-trace` evaluated all packages, the
  example module and the new VM check successfully;
- `nix build .#checks.x86_64-linux.host-module --no-link --print-build-logs`
  passed, including generated-script ShellCheck and the fast bcrypt check.

The VM derivation is intentionally not built until this review is clean,
because it is the long integration check required by the v19 findings.

## Compatibility, deployment and non-goals

Risk is **high** because this changes authentication-derived state, TLS
persistence, host activation, deployment and rollback behavior. All reviewers
must use `gpt-5.6-sol` at `xhigh`.

The password, CA, credential meaning, paths, owners, modes, certificate format,
SAN set and mixed-generation compatibility remain unchanged. New generations
preserve valid derived state; old generations remain able to consume it but
would resume harmless bcrypt and leaf churn on rollback. The retained original
TLS pair will be validated and atomically selected only after the fixed module
is deployed; two non-C-locale reconciliations must then preserve its exact
hashes and target. Deployment is limited to aitherdev and uses configuration
dry activation before switching, followed by the stable installed
`workspace-host switch` for the user profile.

Rejected alternatives were unconditional bcrypt regeneration, locale-dependent
SAN comparison, tolerating multiple persisted formats, passing the password as
an argument, or moving host behavior into the thin workspace consumer.
Default-branch integration, releases, archive, delete and session stop remain
out of scope. The user authorized aitherdev deployment only.

## Review request

Run all four required lanes: General, Architecture/repetition,
Scope/proportionality and Risk/compatibility. Focus on the executable test's
fidelity, secret handling, file validation/replacement, locale-stable SAN
equality, retained-leaf restoration, commit boundaries, exact pins and whether
the remediation is proportional. Report Blocking, Important and Advisory
findings with evidence and remediation; explicitly report a clean lane.
