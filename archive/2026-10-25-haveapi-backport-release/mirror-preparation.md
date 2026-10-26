# Current PHP mirror release candidate

Prepared from original tag run `40238928168`, attempt 1, artifact `12616630970`
(`release-40238928168`), for HaveAPI source
`321ce8256ad4704efaed04f4f2aa1ea4c2a3b4b8`. Protected publication remains held.

Mirror base `195f1a4db7699dc4187463dab0f0e029df375e6c` has one new commit:
`a02dd2506209f54ea782fbd949243207bf9f93bc` (`Release 0.30.2`). The exact
`HaveAPI-Source` line is in both its message and the local annotated `v0.30.2`
tag, object `e69d06bc90722dc9270810ab353037a1d9891cbb`, peeled to that commit.
Only `composer.json` and `src/Client.php` change their version, +2/-2. No
migrations, unrelated content, dependency changes or repeated update streams.

All 36 committed paths, bytes and Git executable modes match the original
PHP tar and tagged HaveAPI PHP source. Tar mode 0664 has no executable bits and
maps to Git 100644; directory Unix permissions are not Git tree entries.
Composer identity is `haveapi/client` / `0.30.2`. No mirror AGENTS.md, `.github`,
declared hook framework, hook-path override or active hooks were present.
No hooks were bypassed. No tests, installs or artifact changes were necessary.

Fresh remote reads before and after preparation show master and peeled .1 still
at the exact base, annotated .1 object `64b9773b5bd704a47e6211595a63456f2fdcc073`,
and remote .2 absent. The feature is clean. Prepared clean detached target:
`worktrees/2026-10-25-haveapi-backport-release/haveapi-client-php-target`, at the
base. Comparison capture binds the same base and final feature head.

[Exact receipt](php-mirror-local-preparation.json) includes all 36 file hashes,
mode semantics, commit/tag/tree, original artifact/run/digest, tar/manifest
SHA-256 values and fresh remote checks. No handles remain. No claim, default
merge, push, approval or publication was performed. Lead owns independent
history acceptance and the later short atomic master/tag publication claim.

## Earlier repository preparation

# PHP mirror repository preparation

Owner: implementer0. Preparation complete; original tagged-run release artifact
and a separate execution assignment remain prerequisites for any snapshot edit,
release commit/tag or publication. No repository claim acquired.

## Identity and registration

On 2026-10-25, `dev-session current` returned
`2026-10-25-haveapi-backport-release`; both environment identity values match
that slug and `/home/aither/workspace/ai/vpsfree.cz`.

The canonical clone already existed. Verified it is bare, with exact origin
`git@github.com:vpsfreecz/haveapi-client-php.git`. Its session feature branch and
worktree did not exist. Reused the canonical clone and fetched only this mirror:

```sh
git --git-dir=repos/haveapi-client-php.git fetch origin --tags \
  refs/heads/master:refs/remotes/origin/master
dev-session worktree add 2026-10-25-haveapi-backport-release \
  haveapi-client-php --as-is --branch 2026-10-25-haveapi-backport-release \
  --base 195f1a4db7699dc4187463dab0f0e029df375e6c --no-fetch
```

The ordinary helper succeeded without catalog changes or identity bypasses. The
session worktree is
`worktrees/2026-10-25-haveapi-backport-release/haveapi-client-php`, on mirror
branch `2026-10-25-haveapi-backport-release`. Portal schema 1 now has a distinct
`haveapi-client-php` project/GitHub registration, target `master` and exact
`initial_base_sha: 195f1a4db7699dc4187463dab0f0e029df375e6c`.

The preexisting HaveAPI registration remains intact, including its
`default_branch: haveapi-0.30` and initial base
`1c3c98f0d77e0b23c8da1a8937f25c5799864a3b`. No HaveAPI checkout/index/canonical
refs were touched. Other mirror worktrees/branches and local master were left
unchanged; only remote-tracking/tag fetch data and this new feature registration/
checkout were prepared. The lead retains state/portal tracking ownership.

## Exact baseline proof

Fresh SSH `ls-remote --symref` identifies remote HEAD as `refs/heads/master`:

| Identity | Exact value |
| --- | --- |
| Remote master / feature initial HEAD | `195f1a4db7699dc4187463dab0f0e029df375e6c` |
| Baseline tree | `2e84b0e7763dcc5724a123e5ebde70a48280f981` |
| Existing annotated `v0.30.1` tag object | `64b9773b5bd704a47e6211595a63456f2fdcc073` |
| Peeled `v0.30.1` | `195f1a4db7699dc4187463dab0f0e029df375e6c` |
| Existing HaveAPI-Source | `1c3c98f0d77e0b23c8da1a8937f25c5799864a3b` |
| Composer identity/version | `haveapi/client` / `0.30.1` |

Existing commit and annotated tag message:

```text
Release 0.30.1

HaveAPI-Source: 1c3c98f0d77e0b23c8da1a8937f25c5799864a3b
```

Remote `v0.30.2` is absent at this preparation check. Existing v0.30.1 is an
unsigned annotated tag: `git tag -v` reports `no signature found`, while its
object type, target and message are valid. No signing requirement was found and
no existing tag was changed. Final worktree/index status is clean at the exact
baseline above.

## Fresh repository guidance and hooks

Inspected the complete tracked inventory, README, composer.json and .gitignore.
There is no AGENTS.md, routed release guide, Nix shell/flake, Makefile or declared
hook framework in this mirror. No `core.hooksPath` override is set; common hooks
contain only the normal `.sample` files, with no active hooks to install or
bypass. No dependencies, hooks or replacement checks were installed. README is
client-use documentation; composer.json currently requires PHP >=8.0.0. No prose
or source change is part of this preparation.

## Artifact and later snapshot contract

Follow the accepted architect's
[PHP mirror publication boundary](architect-evidence.md#php-mirror-publication-and-short-claims).
After reviewed final HaveAPI C is integrated into `haveapi-0.30` and its annotated
`v0.30.2` is verified, use the **original retained tagged-run**
`haveapi-client-php-0.30.2.tar`. Its schema-1 `release-manifest.json` must verify
source C, version `0.30.2`, tag `v0.30.2`, complete artifact identities/hashes and
resolved inputs through the public `verify` CLI in HaveAPI's declared toolchain.
Retain the run/artifact ID, manifest hash and tar hash; do not substitute a local
or later rebuild. Those identities do not exist yet and are not inferred here.

The later mirror snapshot must exactly match all retained tar file paths, bytes
and executable modes, preserving only mirror-owned AGENTS.md and `.github` paths
if they exist then. Composer must report `haveapi/client` / `0.30.2`. Both the
release commit and annotated tag use this exact shape with C's full SHA:

```text
Release 0.30.2

HaveAPI-Source: <C>
```

Mirror commit SHA is distinct from C. Re-fetch/recheck the actual tagged mirror
master before preparing that commit; never overwrite unrelated changes or move
an existing tag. Prepare/validate the complete mechanical snapshot and hooks
outside ownership. Only a later assigned short `haveapi-client-php` claim covers
fresh parent/tag checks, fast-forward integration, normal atomic master+tag
push, exact remote commit/tag-object/peeled-tag proof and immediate verified
release. No registry or Packagist wait belongs inside that claim.

Once that exact PHP tag is published, ordinary protected publisher preflight
verifies its retained snapshot/source and skips a duplicate PHP write. PHP is
then already published even if another registry later fails; preserve original
artifacts/tags and follow the existing partial-release recovery contract.

## Result and next owner action

Mirror preparation is complete and has no outstanding command handles. No source
edit, commit, new tag, push, claim, PHP publication or lifecycle action occurred.
Lead can record this registration/preparation in state. Wait for the verified
original tagged-run artifact and a separate mirror execution assignment.

The session-only [verification plan](final-verification-plan.md) also now includes
the deferred Ruby-client/Go `bundle lock --local` refresh and complete external
graph proof requested by the lead; that step was **not executed**.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-haveapi-backport-release/>
