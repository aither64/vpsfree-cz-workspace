# Mandatory change review packet: complete host path and TLS validation

## Outcome and acceptance criteria

Complete the extraction of reusable workspace tooling into the public
`dev-workspace` and `codex-web` repositories while keeping the vpsFree
workspace a thin compatible consumer. The final aitherdev deployment must
preserve the existing password, CA, authentication meaning, TLS identity,
runtime/session state, URLs and service identities. Host reconciliation must
work during boot, reject unsafe configuration and persisted state before
mutation, and remain idempotent across locales.

## Initiative and exact ranges

- Slug: `2026-09-09-workspace-components`.
- Plan and state: `work/2026-09-09-workspace-components/plan.md` and
  `work/2026-09-09-workspace-components/state.md`.
- `codex-web` worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/codex-web`.
  Review `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..e8655b7b2689da9b1aabe10df69858c32725dd61`;
  unchanged since the clean v11 review.
- `dev-workspace` worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/dev-workspace`.
  Review `f39f8e62097b5e9da9de8a5eb678131b1e478e35..0571f1e12e1d2c4c746eecf4de219dd66764adda`
  (`a695d7e`, `f36bd84`, `fa5f7d4`, `de0441b`, `f858c55`,
  `fcad14a`, `12f99ed`, `2e854dd`, `b62abe0`, `d109a9a`,
  `0571f1e`).
- `vpsfree-cz-workspace` worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/workspace`.
  Review `26606cfa0134ce3680cf592f9ab3c345683fbdc2..4fba092f204f7236d6c5e0d9e24bad9b693e0c1b`
  (`9ea0568`, `4fba092`). The branch is a descendant of current
  shared `master@26606cf`.
- `vpsfree-cz-configuration` worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration`.
  Review `7481618dacab04bfd5b09bc730c373c2d2bf14d7..c144b41ff40a8043f95ceb53b8d0ac9e3e74ffb4`
  (`894d938d`, `c144b41f`).

All worktrees are clean and equal their pushed feature refs. Exact dependency
direction and pins are:

`vpsfree-cz-workspace@4fba092 -> dev-workspace@0571f1e -> codex-web@e8655b7`

Configuration `c144b41f` pins `dev-workspace@0571f1e` with NAR
`sha256-7XJmatzfRf/mzynHPnEUWrHVjtxy1tJCkQYT1lyipcI=` and therefore the same
nested `codex-web@e8655b7` revision.

## Commit ownership and public boundaries

- `codex-web` owns the public Go App Server client, browser conversation
  module, path contract and provider-neutral example.
- `dev-workspace` owns reusable lifecycle and cluster tooling, the portal host,
  the NixOS substrate module and provider extension interfaces. Commit
  `f858c55` directly owns the final module, reconciliation behavior, safe-path
  contract and focused VM regression. Commit `b62abe0` owns the corresponding
  public documentation.
- `vpsfree-cz-workspace` retains policy, records, provider capabilities and one
  exact reusable package pin. Its two commits separate component delegation
  from vpsFree presentation capabilities.
- `vpsfree-cz-configuration` owns aitherdev module consumption and one exact
  input update. The feature input was changed only through
  `confctl inputs channel set --commit` and consolidated into its original,
  still-unmerged input commit.

The public path contract is intentionally bounded. Persistent owning
directories must be strictly below root-controlled `/var/lib`, the router
owning directory must be strictly below `/run`, and the lock must be directly
below `/run/lock`. All owning directories are distinct and mutually
non-nested. The histories contain no fixup or repeated input-update commits.

## Reconciled v23 findings

V23 General and Risk reported a Blocking gap in physical alias detection: the
implementation checked only five existing top-level final directories, so it
missed the router, lock, internal authority, pair inventory, selected pair and
aliases hidden behind not-yet-created final paths. Architecture independently
reported that gap as Blocking. Architecture and Risk also reported a Blocking
lossy `readlink` parser that accepted trailing newlines or dot-segment targets.
General and Risk requested strict retained-leaf purpose checks, Risk requested
single-certificate CA publication, and Scope requested explicit public wording
for the distinct and non-nested directory contract.

The remediation:

- derives one complete managed-directory inventory from the pure Nix path
  validator, including router, lock, every persistent output, internal
  `authority` and `pairs`, and the dynamically selected TLS pair;
- records every existing ancestor's device/inode identity together with the
  remaining planned suffix, then compares physical and lexical relationships
  across the complete inventory, including final paths that do not exist yet;
- rejects mounts on `authority`, `pairs` and the selected pair and retains the
  existing symlink, type, ownership and mode checks for every component;
- runs the complete layout check before mutation, again under the protected
  lock, after creating owned directories, after CA creation and before trusting
  a selected pair;
- captures `readlink -n` output losslessly with a sentinel, accepts only
  `pairs/pair-[0-9]+-[0-9]+`, rereads the exact target after validation and
  verifies that `current` and the candidate still identify the same inode;
- accepts the authority certificate only when OpenSSL's canonical single-PEM
  rendering byte-matches the complete file, so an appended certificate,
  private key or trailing data cannot be published;
- retains a leaf only when it is one canonical PEM server certificate with
  critical `CA:FALSE`, critical digital-signature key usage, server-auth
  extended usage, exact SANs, a valid CA signature and a matching key; and
- documents the distinct/non-nested and physical-path restrictions in the
  README and Nix option descriptions.

The first topology implementation repeatedly launched `stat`, `basename` and
`dirname` in nested loops and made VM boot activation take about 2 minutes 17
seconds. It was stopped and replaced with one ancestor walk per configured
path plus in-process array comparisons. The optimized activation phase took
about 9.25 seconds in the emulated VM. A durable note records the failure,
cause, correction and result.

The first complete optimized VM run exposed one stale pre-v23 expectation: an
older test expected a symlinked selected-pair directory to be silently
replaced. The new contract correctly failed closed. The regression now asserts
rejection, unchanged credentials and hashes, explicit restoration and stable
reconciliation. Its generated Python script passes NixOS type checking and
linting.

## Quick verification

For the exact tree now committed as `dev-workspace@0571f1e`:

- Nixfmt and `git diff --check` pass;
- `nix flake check --no-build --show-trace` evaluates every output;
- `nix build --no-link .#checks.x86_64-linux.host-module` passes generated
  ShellCheck and pure path fixtures; and
- `nix build --print-build-logs --no-link
  .#checks.x86_64-linux.host-module-idempotency` passed in 1,055.02 seconds.
  It boots the real module under `en_US.UTF-8`, exercises the complete lock,
  directory, alias, password, authentication, CA, symlink and TLS matrix, and
  proves stable retained state after recovery. Its tested pre-rewrite tree and
  final committed tree are the identical Git tree
  `6a57521a83135662435b93b55e88b4c039fcccf3`. The kernel and initrd came from
  cache; no kernel was built locally.

At the exact downstream heads:

- workspace `nix flake check --no-build --show-trace` passes;
- configuration `nix develop -c nix flake check --no-build --show-trace`
  passes, and generated `.bin` and `.bundle` helpers were removed;
- all four worktrees pass `git diff --check`, are clean and equal their pushed
  refs; and
- exact-head dev-workspace Actions run `34483741579` is in progress. The
  immediately preceding exact-tree run `34474248837` completed successfully.

## Compatibility, deployment and non-goals

Risk is **high** because this changes authentication-derived state, TLS
persistence, public Nix options, host activation, deployment and rollback
behavior. General, Architecture/repetition, Scope/proportionality and
Risk/compatibility all rerun with `gpt-5.6-sol` at `xhigh` because every v23
lane reported at least one finding.

The deployed aitherdev paths satisfy the stricter roots and disjointness
contract. Password, CA, credential meaning, concrete paths, owners, modes,
certificate format, SAN set and mixed-generation readable formats remain
unchanged. Old generations remain able to consume new state but would resume
harmless derived bcrypt and leaf churn on rollback. The retained original TLS
pair will be validated and atomically selected only after the fixed module is
deployed. Two non-C-locale reconciliations must then preserve its exact hashes
and target.

Rejected alternatives were following configurable symlinks, allowing internal
mount boundaries, silently rotating malformed durable password or CA state,
publishing the first certificate from a multi-object PEM file, or accepting a
CA-capable or client-only leaf that OpenSSL could otherwise parse.

Deployment is limited to aitherdev and uses configuration dry activation before
switching, followed by the stable installed `workspace-host switch` for the
user profile. Default-branch integration, releases, archive, delete and session
stop remain out of scope. The user authorized aitherdev deployment only.

## Review request

Run all four required lanes. Focus on complete physical-alias detection,
missing-final-path behavior, symlink and mount boundaries, the lossless
`current` parser and post-validation identity check, canonical single-object
PEM enforcement, strict leaf purpose/extensions, pre-mutation ordering,
history ownership, exact pins, mixed-generation behavior and proportionality.
Report Blocking, Important and Advisory findings with direct evidence and a
specific remediation; explicitly report a clean lane.
