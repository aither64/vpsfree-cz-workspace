# Mandatory change review packet: bounded host state validation

## Outcome and acceptance criteria

Complete the extraction of reusable workspace tooling into the public
`dev-workspace` and `codex-web` repositories while keeping the vpsFree
workspace a thin compatible consumer. The final aitherdev deployment must
preserve the existing password, CA, authentication meaning, TLS identity,
runtime/session state, URLs and service identities. Host reconciliation must
work during boot, reject unsafe configuration and persisted state, and remain
idempotent across locales.

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
  Review `f39f8e62097b5e9da9de8a5eb678131b1e478e35..f9ef74b99fcc616efd3eab99b4a88cde4563d9a2`
  (`a695d7e`, `f36bd84`, `fa5f7d4`, `de0441b`, `5589e98`,
  `948da2a`, `5104c1e`, `880474f`, `9e5ad7c`, `4e28213`,
  `f9ef74b`).
- `vpsfree-cz-workspace` worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/workspace`.
  Review `26606cfa0134ce3680cf592f9ab3c345683fbdc2..010e3dd4e3d41aa5812b9ecdc7c70e610eef615a`
  (`a02bf99`, `010e3dd`). The branch is a descendant of shared
  `master@26606cf`.
- `vpsfree-cz-configuration` worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration`.
  Review `7481618dacab04bfd5b09bc730c373c2d2bf14d7..141daeb8f284b172708bfaeee955315cdadf0ce1`
  (`7c6c5bf`, `141daeb`).

All worktrees are clean and equal their pushed feature refs. Exact dependency
direction and pins are:

`vpsfree-cz-workspace@010e3dd -> dev-workspace@f9ef74b -> codex-web@e8655b7`

Configuration `141daeb8` pins `dev-workspace@f9ef74b` with NAR
`sha256-MBOQ8iqu+ldp5DLsjqaayccRZxDTTm3cER1pYcpNXCY=` and therefore the same
nested `codex-web@e8655b7` revision.

## Commit ownership and public boundaries

- `codex-web` owns the public Go App Server client, browser conversation
  module, path contract and provider-neutral example.
- `dev-workspace` owns reusable lifecycle and cluster tooling, the portal host,
  the NixOS substrate module and provider extension interfaces. Commit
  `5589e98` directly owns the final module, reconciliation behavior, safe-path
  contract and focused VM regression. Commit `9e5ad7c` owns the corresponding
  public documentation.
- `vpsfree-cz-workspace` retains policy, records, provider capabilities and one
  exact reusable package pin. Its two commits separate the component
  delegation from vpsFree presentation capabilities.
- `vpsfree-cz-configuration` owns aitherdev module consumption and one exact
  input update. `7c6c5bf` was generated through
  `confctl inputs channel set --commit` and then consolidated while still
  unmerged.

The reusable module intentionally exposes configurable state paths only within
bounded roots: all persistent paths are below `/var/lib`, the router is below
`/run`, and the lock is directly below `/run/lock`. Its reconciler verifies
root-controlled, non-symlink directory components and rejects physical aliases
before mutating state. Provider consumers own concrete paths, source networks,
hostnames, labels, capabilities and modes. The histories contain no fixup or
repeated input-update commit; tests remain with the behavior they validate.

## Reconciled v22 findings

V22 Scope reported one Blocking issue: the public arbitrary-path promise was
broader than a safe implementation that necessarily traversed parent
directories. Architecture reported two Important issues: directory paths could
resolve through symlinks or mounts to the same storage, and the password check
did not enforce the complete byte shape. General and Risk independently
reported an Important retained-TLS metadata gap. General and Scope also
reported Advisory gaps in negative lock, password and TLS testing; Scope
reported redundant auth validation and narrow implementation-spelling probes.

The remediation:

- bounds persistent state below `/var/lib`, runtime routing below `/run`, and
  the reconciliation lock directly below `/run/lock`, with pure evaluation
  fixtures and public documentation for each constraint;
- rejects symlinks at every managed directory component, non-root owners,
  group/world writable components, unsafe final metadata, and distinct lexical
  paths that resolve to the same directory;
- reconstructs and byte-compares the password as exactly one lowercase
  64-hex value followed by one newline, while failing closed for dangling
  password and CA-authority symlinks;
- accepts a retained leaf only through one direct `pairs/<name>` target and
  validates exact directory/certificate/key types, owners and modes, expiry,
  CA signature, exact SAN set and certificate/key public-key equality;
- sends generated TLS output through the same leaf validator before atomic
  publication, and preserves the validated CA and password instead of silently
  rotating them;
- expands the real boot-level VM with non-truncating lock failures, symlink and
  bind-alias directory failures, complete password-shape failures, retained TLS
  type/metadata/content failures, exact generated SAN and key checks, and one
  stable reconciliation after every necessary leaf renewal; and
- removes the redundant retained-auth revalidation and implementation-spelling
  probes while retaining behavioral output gating.

The first fast check exposed a ShellCheck reference to a generated-script
variable that was not in lexical scope; constructing the temporary path from
the candidate fixed it. No compatibility behavior or public interface changed
beyond the explicit path-root restriction required to make the safety contract
enforceable.

## Quick verification

At exact `dev-workspace@f9ef74b`:

- Nixfmt and `git diff --check` pass;
- `nix flake check --no-build --show-trace` evaluates all outputs;
- `nix build .#checks.x86_64-linux.host-module --no-link --print-build-logs`
  passes generated-script ShellCheck and pure path fixtures; and
- the exact final `host-module-idempotency` Nix build passes in 285.65 seconds
  under `en_US.UTF-8`. It boots the real module, exercises the complete lock,
  directory, password, authentication and TLS recovery matrix, and proves
  stable password, bcrypt, CA, public CA, valid leaf and `current` target. The
  kernel and initrd were fetched from cache; no kernel was built locally.

At exact downstream heads:

- workspace `nix flake check --no-build --show-trace` passes;
- configuration `nix develop -c nix flake check --no-build --show-trace`
  passes and its generated shell helpers were removed;
- all four worktrees pass `git diff --check`, are clean, and equal their pushed
  refs; and
- exact-head dev-workspace Actions run `34474248837` is in progress.
  Superseded run `34469910621` could not be cancelled because GitHub returned
  HTTP 403 for the available token, which lacks Actions write permission.

## Compatibility, deployment and non-goals

Risk is **high** because this changes authentication-derived state, TLS
persistence, public Nix options, host activation, deployment and rollback
behavior. All reviewers must use `gpt-5.6-sol` at `xhigh`. General,
Architecture/repetition, Scope/proportionality and Risk/compatibility all rerun
because remediation narrowed a public path contract and changed shared state
validation.

The deployed aitherdev paths already satisfy the bounded roots and exact
disjointness contract. Password, CA, credential meaning, concrete paths,
owners, modes, certificate format, SAN set and mixed-generation readable
formats remain unchanged. Old generations remain able to consume new state but
would resume harmless derived bcrypt and leaf churn on rollback. The retained
original TLS pair will be validated and atomically selected only after the
fixed module is deployed. Two non-C-locale reconciliations must then preserve
its exact hashes and target.

Rejected alternatives were following configurable symlinks, silently rotating
malformed durable password or CA state, accepting any TLS material that OpenSSL
could parse, or using disposable development-state guards to weaken the live
contract. Compatibility aliases outside this host-state remediation remain
bounded as documented in earlier packets.

Deployment is limited to aitherdev and uses configuration dry activation before
switching, followed by the stable installed `workspace-host switch` for the
user profile. Default-branch integration, releases, archive, delete and session
stop remain out of scope. The user authorized aitherdev deployment only.

## Review request

Run all four required lanes. Focus on whether the bounded directory preflight
can be bypassed or rejects supported configuration; exact password and TLS
file-shape validation; generated-output gating; lock creation/opening and boot
ordering; physical-alias behavior; history and ownership boundaries; exact
pins; mixed-generation behavior; and whether the remediation is proportional.
Report Blocking, Important and Advisory findings with direct evidence and a
specific remediation; explicitly report a clean lane.
