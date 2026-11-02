# mx2 import and rebase evidence

## Boundaries and source

Session identity independently verified with `dev-session current` and matching
`DEV_SESSION_SLUG` / `DEV_SESSION_WORKSPACE`. Source checkout is read-only:
`/home/aither/workspace/vpsfree.cz/vpsfree-cz-configuration`.

| Boundary | Exact revision |
| --- | --- |
| Historical base | `0bcc165f13059782bf686da39a3a9b5698b10275` |
| Original mx2 commit / source remote feature tip | `be8435d1d4f3e656af1d7d090d867797d2713a66` |
| Original local feature tip | `40411d67ee97cea800bcccd89b0473432b4502c4` |
| Fresh canonical default, `origin/master` | `c040c14cdbacc07998700b524996a89306188d7f` |
| Final refreshed feature head | `e4c1ac0c5ae7426fb019b79ba936b30ce63e6e6c` |
| Final feature tree | `6ca8b7fd5a9a6653a9970959f8d100303eb1fc87` |

Canonical remote is `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
`git fetch origin` and `git ls-remote --symref origin HEAD` agreed on `master`
and the default revision above. Imported exact local source using:

```sh
git fetch --no-tags /home/aither/workspace/vpsfree.cz/vpsfree-cz-configuration \
  refs/heads/2025-05-30-mx2:refs/heads/2026-11-01-mx2-nixos-migration-source
```

The retained import ref points to the original local feature tip above. It is
separate from the dated working branch and is not rewritten.

## Original complete series

1. `be8435d1d4f3e656af1d7d090d867797d2713a66`, `cluster: add mx2.vpsfree.cz`:
   five paths, 68 additions; host definition, cluster import, public key and
   container placement metadata.
2. `40411d67ee97cea800bcccd89b0473432b4502c4`,
   `environments/deploy: use cache.vpsadminos.org`: one path, two additions.

Complete source diff: six paths, 70 additions. No database migrations or
branch-specific dependency/channel-pin updates. Historical deployment or other
external consumption of mx2 remains unknown; original refs are preserved.

## Worktree and hook recovery

Native registration command:

```sh
dev-session worktree add 2026-11-01-mx2-nixos-migration \
  vpsfree-cz-configuration --as-is \
  --branch 2026-11-01-mx2-nixos-migration \
  --base refs/heads/2026-11-01-mx2-nixos-migration-source --no-fetch
```

It created the owned branch and worktree at the exact original local head and
registered `initial_base_sha: 40411d67ee97cea800bcccd89b0473432b4502c4` in
`portal.yml`, then returned failure because shared Overcommit `post-checkout`
read a missing `.overcommit.yml`. The historical branch predates that file.
Inspection confirmed the created branch/worktree were clean at the imported
tip; no unrelated worktree or ref was touched. A normal `git rebase --onto`
also refused in `pre-rebase` for that missing historical configuration, before
changing history.

Lead accepted reconstructing the owned feature on the fetched current base
with normal hooks and replaying the original mx2 patch; no bypass was authorized
or used. A detached checkout of the exact current base took effect, but its
`post-checkout` hook reported missing locked gems. A fresh policy watcher
(`gpt-6-luna`, low, full-access/never approval policy) ran `nix develop -c true`
at the current base, exiting 0 in 43 seconds. See
[setup evidence](devshell-setup-result.md). Original source and
the exact import ref remain intact. The registration base records the actual
initial import, not the historical feature base or refreshed default.

Recovery then used the current repository development shell:

```sh
bundle exec overcommit --install
bundle exec overcommit --sign pre-commit
git switch -C 2026-11-01-mx2-nixos-migration \
  c040c14cdbacc07998700b524996a89306188d7f
git cherry-pick --no-commit be8435d1d4f3e656af1d7d090d867797d2713a66
```

The branch rewrite affected only this session's feature branch; the source import
ref stayed exact. All three shared-file patch applications merged cleanly, with
no conflicts. Converted the mx2 metadata option from `swpins.channels` to
`inputs.channels` and ran RFC Nix formatting on its two new files. No other
functional change was made. Committed with `git commit -F` in the repository
development shell, preserving the original author and author date. The normal
Overcommit pre-commit Nixfmt hook passed; commit-msg hooks passed with an advisory
72-column text-width warning (all message lines satisfy the required 80-column
limit). No hooks were disabled.

Native worktree registration was retried successfully after recovery and retained
the honest original `initial_base_sha`. Captured the final comparison with
`dev-session worktree capture-comparison`, explicitly supplying the exact fresh
base and final head. Owned worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-mx2-nixos-migration/vpsfree-cz-configuration`.

## Cache disposition

Fresh default `environments/deploy.nix` already contains the exact original
`substituters` and `trusted-public-keys` values. `git log --cherry-mark` marks
the original cache commit and upstream
`17ac0d2b842a88ae7f7b76b1651f36d984dadb2c` as patch-equivalent. Current upstream
also supplies newer fallback and timeout settings. Omit the redundant cache
commit from the refreshed feature and retain no final change to that file.

## Final series and equivalence

Final range is the fresh default through the final refreshed feature head above.
It contains exactly one commit, `cluster: add mx2.vpsfree.cz`, five paths and
94 additions. Original mx2 intent remains; the additional 26 lines are formatting.
The only functional adaptation is the channel option spelling. See the complete
[range-diff](range-diff.md): original mx2 maps to the final commit and the
redundant cache commit is dropped. `flake.nix`, `flake.lock`, `profiles/ct.nix`
and `environments/deploy.nix` are identical to the fresh default. No dependency-pin
stream was added or refreshed, and no database/schema migration is present.
Historical mx2 deployment/consumption remains unknown; do not infer it from this
replay or classify the preserved source as a verified undeployed migration.

## Quick checks and evaluated identity

Passed on the final source content, with final committed-head evaluation repeated:

- `nixfmt --check` and `nix-instantiate --parse` on all five changed Nix files.
- `git diff --check` for staged, working and complete final base-to-head diffs.
- Declared Overcommit hooks during the final commit; clean final worktree.
- `confctl ls -H -o name,spin,host.fqdn,container.id,inputs.channels
  cz.vpsfree/containers/mx2`: exactly one result, NixOS, `mx2.vpsfree.cz`, ID 27627,
  channels `nixos-stable`, `os-staging`.
- `nix eval --raw .#confctl.build.m_cz_vpsfree_containers_mx2_d27c8511.toplevel.drvPath`:
  passed. Only warning is the supported rename of `services.postfix.config` to
  `services.postfix.settings.main`; policy was preserved.
- Exact final base is an ancestor of the feature head. Fresh remote checks after
  push still report the same default.
- Source before/after snapshots match exactly: HEAD, symbolic HEAD, all refs,
  status including untracked files, and index/config/HEAD SHA-256 hashes. The
  disposable snapshot JSON files are session evidence; original source files,
  index and refs were not modified.

Evaluated final derivation:
`/nix/store/0b88m9lch1bcvzn6iwbp60i7lf7jb5ip-nixos-system-mx2-26.05.20261026.718f670.drv`.
Its evaluated system output is
`/nix/store/yi0wph12csy27bzvwdj7idpd70wpyxd6-nixos-system-mx2-26.05.20261026.718f670`.
Neither path proves a realized build, activation or runtime result. There is no
deployed profile or machine claim for this import.

The complete unchanged input graph is bound by final `flake.lock` blob
`ec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86` and SHA-256
`505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a`.
It can be recovered exactly with `git show e4c1ac0c5ae7426fb019b79ba936b30ce63e6e6c:flake.lock`;
`input-graph.json` is a disposable copy of the complete lock graph. Effective
mx2 roles from `confctl.buildPlan`:

| Role | Channel/input | Exact revision and source path |
| --- | --- | --- |
| nixpkgs | nixos-stable / nixpkgsStable | `718f670e845328e9c2cecdd832835712b2cbd065`, `/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source` |
| vpsadminos | os-staging / vpsadminosOsStaging | `b45b27b4330a08d85f413999e4bf66ba4503eee1`, `/nix/store/c24mbj25ajwn8zixx4hagr85i5kmqlmy-source` |
| tooling | confctl | `7bee58a52372b95c2198ce3f2a719807a3c2c66b`, `/nix/store/8mjng71gica53p9jr4085f22xq1zslzg-source` |

The vpsAdminOS input follows `nixpkgsStable` and `nixpkgsUnstable`; complete
transitive locked identities and follows edges are in the exact lock above.

## Evaluated mail settings and residuals

Read generated derivation text without realizing or running it; full bounded
evidence is [evaluated mail configuration](evaluated-mail-config.md).

- Postfix 3.11.7 generates an SMTP inet service and preserves the three transport
  destinations `smtp:prasiatko-mail.vpsfree.cz`.
- `relay_domains` is empty; a transport map does not authorize backup-MX relay.
  The inherited `reject_unauth_destination` policy therefore still needs an
  explicit domain/recipient acceptance decision before production use.
- `smtpd_tls_security_level = none` and empty `smtpd_tls_chain_files` provide no
  configured inbound TLS certificate. Outbound `smtp_tls_security_level = may`.
- `mynetworks_style = host`; configured recipient restrictions reference
  `unix:/run/postgrey.sock` and the existing DNSBLs. Postgrey service is generated.
- The absent milter remains configured at `inet:localhost:11332`, with failure
  action `accept`. No runtime claim is made about its reachability.
- Queue/data paths are `/var/lib/postfix/queue` and `/var/lib/postfix/data`.
  No CentOS queue migration or rollback compatibility has been tested.

These are existing policy gaps, not fixed by this bounded import. Identity,
stateVersion, public key and placement remain unchanged. The design brief owns
the staged runtime-verification recommendation and operational unknowns.

## Publication and next verification

Published feature branch:
`2026-11-01-mx2-nixos-migration` at
`e4c1ac0c5ae7426fb019b79ba936b30ce63e6e6c`.
`nix develop -c git push -u origin 2026-11-01-mx2-nixos-migration` succeeded over
SSH; `git ls-remote --heads origin` verified the exact feature head and unchanged
default `c040c14cdbacc07998700b524996a89306188d7f`.
`gh run list --repo vpsfreecz/vpsfree-cz-configuration --branch
2026-11-01-mx2-nixos-migration` returned no runs; the repository workflow is a
scheduled/manual daily updater, not a push-triggered feature check.

Independent final review is coordinated by lead. After review, the repository's
required longer targeted build should run under a fresh policy watcher from the
owned worktree, at this exact head and unchanged lock:

```sh
nix develop -c confctl build --yes cz.vpsfree/containers/mx2
```

Use installed full-access execution with approval policy `never`. Retain its logs
and exact system result in session records. Stop and escalate an unexpected local
kernel build under the verification procedure. Do not deploy or dry-activate;
those operations contact a target. No long build/test has been started by this
execution package, and no deployment, production access, mail sending or default
integration is authorized or performed. The session and all feature refs remain
open and retained.
