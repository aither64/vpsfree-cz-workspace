# Mandatory change review packet: exact state validation and clean history

## Outcome and acceptance criteria

Complete the extraction of reusable workspace tooling into the public
`dev-workspace` and `codex-web` repositories while keeping the vpsFree
workspace a thin compatible consumer. The final aitherdev deployment must
preserve the existing password, CA, authentication meaning, TLS identity,
runtime/session state, URLs and service identities. Host reconciliation must
work during boot, reject unsafe configuration and state, and remain idempotent
across locales.

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
  Review `f39f8e62097b5e9da9de8a5eb678131b1e478e35..6890ab620715b3630a2ddef6d0aad98dccb1d9b4`
  (`a695d7e`, `f36bd84`, `fa5f7d4`, `de0441b`, `964dbdd`,
  `7e5dbbe`, `702f6df`, `f73c6a4`, `5b1632f`, `53754e2`,
  `6890ab6`).
- `vpsfree-cz-workspace` worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/workspace`.
  Review `26606cfa0134ce3680cf592f9ab3c345683fbdc2..9a10a222a51e7d34067f535bfb6afe3a7de54a96`
  (`c494008`, `9a10a22`). The branch is a descendant of shared
  `master@26606cf`.
- `vpsfree-cz-configuration` worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration`.
  Review `7481618dacab04bfd5b09bc730c373c2d2bf14d7..a564d1cf6f508e4ffcd1a9e42719fd8655f2ba4d`
  (`87dd5556`, `a564d1cf`).

All worktrees are clean and equal their pushed feature refs. Exact dependency
direction and pins are:

`vpsfree-cz-workspace@9a10a22 -> dev-workspace@6890ab6 -> codex-web@e8655b7`

Configuration `a564d1cf` pins `dev-workspace@6890ab6` with NAR
`sha256-gY4J+J75UxCf0VkpTs+Pgyym9sXQAYKN5jBpHUH+1Ko=` and therefore the same
nested `codex-web@e8655b7` revision.

## Commit ownership and public boundaries

- `codex-web` owns the public Go App Server client, browser conversation
  module, path contract and provider-neutral example.
- `dev-workspace` owns reusable lifecycle/cluster tooling, the portal host,
  the NixOS substrate module and provider extension interfaces. Commit
  `964dbdd` directly introduces the final module, reconciliation behavior,
  path contract and provider-level VM regression.
- `vpsfree-cz-workspace` retains only policy, records, provider capabilities
  and one exact reusable package pin in its original extraction commit.
- `vpsfree-cz-configuration` owns aitherdev module consumption and one exact
  input update. Its final revision was generated only by
  `confctl inputs channel set --commit` and consolidated into the original
  unmerged input commit.

The histories contain no fixup commit or repeated update of the same flake
input. Tests stay with the behavior they validate. Non-generated commit-message
lines are at most 80 columns.

## Reconciled v21 findings

V21 General reported two Blocking history issues, one Important auth parsing
issue and one Advisory message-width issue. Architecture reported two
Important validation/ownership issues. Risk independently reported the lock
boundary as Advisory. Scope reported one redundant Apache-only test as
Advisory. The remediation:

- folds the complete reconciler and VM into the original host-module commit,
  removes both consumer pin-only commits, and regenerates the configuration pin
  through `confctl` before consolidating it;
- uses one `auth_file_valid` function for retained state and generated
  temporary output before publication;
- rejects NUL bytes and compares the complete file against exactly one
  credential with one or two terminating newlines, then validates username,
  bcrypt cost/alphabet, ownership, mode and password;
- adds VM recovery cases for trailing and embedded NULs, a second credential
  and excess terminators;
- owns all managed-path validation in one pure Nix helper used by both module
  assertions and focused evaluation fixtures: paths must be normalized and
  absolute, managed directories distinct and non-nested, and the lock directly
  below `/run/lock`;
- creates the root-owned mode-0600 regular lock without truncating it, rejects
  unsafe existing state and verifies the opened inode before flocking;
- removes the duplicated Apache-only self-test and repeated bcrypt ERE.

The first binary comparison triggered ShellCheck SC2094 for a read-only
same-path pipeline, so it now uses a protected temporary file. The first VM
then proved `cmp` was absent during boot because Nixpkgs packages it in
`diffutils`; the generated application now declares that exact runtime input.

## Quick verification

At exact `dev-workspace@6890ab6`:

- Nixfmt and `git diff --check` pass;
- `nix flake check --no-build --show-trace` evaluates all outputs;
- `nix build .#checks.x86_64-linux.host-module --no-link --print-build-logs`
  passes generated-script ShellCheck and pure path fixtures;
- the focused `host-module-idempotency` Nix build passes. The uncached VM
  execution completed in 99.08 seconds under `en_US.UTF-8`, exercised boot,
  lock validation, every textual and binary auth recovery case, and preserved
  password, bcrypt, CA key and certificate, public CA, TLS key and certificate,
  and `current` target. The kernel and initrd were fetched from cache; no kernel
  was built locally.

At exact downstream heads:

- workspace `nix flake check --no-build --show-trace` passes;
- configuration `nix flake check --no-build --show-trace` passes;
- all four worktrees pass `git diff --check`, are clean, and equal their pushed
  refs;
- exact-head dev-workspace GitHub Actions run `34469910621` is in progress.

## Compatibility, deployment and non-goals

Risk is **high** because this changes authentication-derived state, TLS
persistence, public Nix options, host activation, deployment and rollback
behavior. All reviewers must use `gpt-5.6-sol` at `xhigh`. General,
Architecture/repetition, Scope/proportionality and Risk/compatibility all rerun
because the remediation changes the public path contract and shared validator.

The deployed aitherdev paths already satisfy the new explicit disjointness and
`/run/lock` contract. Password, CA, credential meaning, paths, owners, modes,
certificate format, SAN set and mixed-generation readable formats remain
unchanged. Old generations remain able to consume new state but would resume
harmless derived bcrypt and leaf churn on rollback. The retained original TLS
pair will be validated and atomically selected only after the fixed module is
deployed. Two non-C-locale reconciliations must then preserve its exact hashes
and target.

Deployment is limited to aitherdev and uses configuration dry activation before
switching, followed by the stable installed `workspace-host switch` for the
user profile. Default-branch integration, releases, archive, delete and session
stop remain out of scope. The user authorized aitherdev deployment only.

## Review request

Run all four required lanes. Focus on exact file-shape validation, generated
output gating, lock creation/opening, the pure path contract and fixtures,
boot behavior, history boundaries, exact pins, mixed-generation behavior and
whether the remediation remains proportional. Report Blocking, Important and
Advisory findings with evidence and remediation; explicitly report a clean
lane.
