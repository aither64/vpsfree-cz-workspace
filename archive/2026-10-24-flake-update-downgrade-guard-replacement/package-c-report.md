# Package C current handoff

Current final R handoff: [package-c-r-report.md](package-c-r-report.md). All five
reviewed R heads are published; original records below are historical 7ba evidence.
The R report preserves P/Q provenance, the independent status fix and remaining
runtime/CI gates.

---

# Package C: five ordinary flake updater workflows

Implementation by implementer0. All five feature branches have one logical
adoption commit each, passed final quick checks and ordinary hooks, and are
published with exact remote proof for independent review. Every workflow and
shared-doc link selects final provider
`7ba361d22a4aac044cb02abf8397800bcf5726bf`. No default integration, deployment, machine reservation or
session lifecycle action was performed.

## Scope and source

Exact baseline and full branch inventories are in
[package-c-branches.json](package-c-branches.json). All worktrees use
`worktrees/2026-10-24-flake-update-downgrade-guard-replacement/<project>` and the
same initiative branch slug. Canonical remotes are SSH under `vpsfreecz`.

| Project | Target | Fresh fetched baseline |
| --- | --- | --- |
| haveapi | master | `67fcd34ba506264a5c7ee2e8e18a88d221c6f469` |
| terraform-provider-vpsadmin | master | `2a2c1055302f86f8e250f1d7e4c331d62012efe8` |
| vpsadminos | staging | `e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854` |
| vpsf-status | master | `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb` |
| vpsfree-irc-bot | master | `94ac4eb5a7caf0456fff7df86a44cae198463276` |


Final published heads (fresh SSH remote equality proof; all worktrees clean):

| Project | Final head |
| --- | --- |
| haveapi | `d4dc3c7c6b15d3bdad51ce18f6959136dc68b23e` |
| terraform-provider-vpsadmin | `171e32d8bf6706748651ba33df6abb05849244fa` |
| vpsadminos | `0552cfeecf127671e21dcb72db78b7188d342107` |
| vpsf-status | `7641e48787281d29cdd0df95f7ee06555c73fac6` |
| vpsfree-irc-bot | `a2ab57b8169ad978f6f8542dd19cf5199517b0cb` |

One workflow-level `CONFCTL_FLAKE` selects the same exact external CI tool in
all consumers. Helpers require that explicit environment reference and invoke
`nix shell "$CONFCTL_FLAKE" -c confctl`; there is no ambient-tool fallback or new
runtime input. `GITHUB_TOKEN` is passed explicitly. All nonzero update/check
outcomes stop publication.

The jobs explicitly fetch their target branches, save the original lock under
`RUNNER_TEMP` before updating, retain existing input selection and checks, and
use ordinary non-force pushes. Their final check reads `HEAD:flake.lock` into a
separate temporary file and validates that exact committed blob against the
original baseline. This covers a hook/test leaving worktree bytes different
from what Git will publish. A concurrent target change requires a fresh run;
no stale-lock pull/rebase/merge retry is added.

HaveAPI and IRC retain their 11/9-character flake commit subjects; Terraform
retains its vpsadmin subject/body and lock-only checks; status retains Go updates,
tests/builds and 11-character flake subjects; vpsAdminOS retains all-root updates
and generated single/multi-input subjects, using a message file for all commits.
Metadata comes from shared `inputs ls --json` with one matching non-null
revision, including nested follows and arbitrary serialized node IDs. No ancestry
or graph resolver algorithm is copied into consumers.

## Paths and lasting documentation

- HaveAPI: `.github/workflows/update-nixpkgs.yml`, `utils/update-nixpkgs.sh`,
  `doc/agent-instructions/development.md`.
- Terraform: `.github/workflows/update-vpsadmin-flake.yml`,
  `tools/update-vpsadmin-flake-input.sh`, `README.md`.
- vpsAdminOS: `.github/workflows/flake-update.yml`, `README.md`.
- Status: `.github/workflows/update-dependencies.yml`, `README.md`.
- IRC: `.github/workflows/nixpkgs-update.yml`,
  `tools/update_nixpkgs_flake.sh`, `README.md`.

The shared lasting guard contract remains confctl's `docs/flake-inputs.md`;
consumer documentation links its selected immutable revision. Lead applied the
required direct user-facing writing pass to all changed docs/help/errors.
Temporary setup, branch and verification details remain here.

## Checks and operation evidence

Each repository's AGENTS/README and applicable routed procedures were read.
IRC has no repository AGENTS. Fresh SSH fetches before worktree creation and
before publication found the baselines above unchanged. All five worktrees are
registered; exact comparisons captured in the portal.

Declared environment/hook setup:

```sh
# HaveAPI, vpsAdminOS and IRC:
nix develop -c bash -c 'bundle exec overcommit --install && bundle exec overcommit --sign'
# Status:
nix develop -c make hooks
# Terraform has no declared hook framework:
nix develop -c bash -c 'bash -n tools/update-vpsadmin-flake-input.sh'
```

Setup logs: `package-c-setup-<project>.log`. Reviewed Overcommit configuration
and HaveAPI custom hook source before signing. Initial HaveAPI/vpsAdminOS/IRC
worktree creation physically succeeded but returned a post-checkout signature
failure; standard hook setup and normal registration retry reconciled this.
No hook bypass or repository-wide stash/reset occurred.

Quick command per project, in its own worktree:

```sh
nix develop -c python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-fixtures.py <project>
```

The harness is [package-c-fixtures.py](package-c-fixtures.py). It uses disposable
Git repositories, actual shared FlakeLock metadata resolution, mocked guard
command outcomes, and no network/build/push. It covers forward/no-change,
rejection 3/evidence error 1, final rejection/error preventing push, malformed
metadata, missing explicit tool, exact commit subjects, external immutable
baseline retention, and committed-blob validation despite post-commit worktree
drift. The actual five repository locks also pass local graph equality without
API requests. All workflow shell blocks pass `bash -n`.

Workflow/helper lint uses the HaveAPI repository's locked nixpkgs:

```sh
nix shell --inputs-from . nixpkgs#actionlint nixpkgs#shellcheck -c actionlint <five workflow paths>
nix shell --inputs-from . nixpkgs#actionlint nixpkgs#shellcheck -c shellcheck <three helper paths>
```

Actionlint 1.7.12 and ShellCheck 0.11.0 passed. Exact logs are
`package-c-actionlint.log`, `package-c-shellcheck.log` and per-project
`package-c-quick-<project>.log`. The committed-blob correction passed 40 scenarios: HaveAPI 9, Terraform 9,
vpsAdminOS 6, status 7 and IRC 9. All five ordinary hook commits passed; Overcommit
reported advisory 72-column message-width warnings, with all lines within the
required 80-column limit. Status's required i18n-health hook passed. Logs:
`package-c-commit-<project>.log` and `package-c-final-commit-<project>.log`.

Fresh Luna/low utilities performed initial environment setup. Follow-on watcher
launches failed before checks (missing profile CLI path and an unrelated wrapper
syntax error), despite supplied literal CLI/path. The monitor skill's visible
parent fallback ran the bounded checks with full status/log capture. HaveAPI's
first setup command succeeded, then its watcher's login-shell logout failed;
the operation status 0 and installed/signed hooks were confirmed separately.
The IRC fixture's stdlib Ruby subprocess initially inherited the dev shell's
`RUBYOPT=-rbundler/setup` and conflicted with its pinned JSON gem; isolating only
the fixture's Ruby/Bundler environment resolved the check. Real workflow updates
run the external package outside `nix develop`; provider-package artifact checks
remain a later gate.

Action upstream/version/runtime compatibility evidence is in
[package-c-actions.json](package-c-actions.json). Only imported refs in the five
assigned workflows changed: checkout v7 (latest v7.0.1, Node 24) and Nix installer
31.11.3 (composite Bash, Linux support). All use maintained GitHub-hosted
`ubuntu-latest` with scheduled/manual events; no unsafe fork-checkout or container
credential path is introduced. This is source-backed compatibility evidence,
not a live workflow-dispatch result. No unrelated workflow refs were edited.

## History, migrations and remaining gates

Each final branch contains one external CI tool adoption; no runtime input,
lockfile, schema, migration or persistent format changed. There are no
superseded pin commits, obsolete implementation approaches or transitional
migration paths in final history. The original publication ranges are retained in
[package-c-branches-initial.json](package-c-branches-initial.json). Final ranges
and `git range-diff` are in [package-c-branches.json](package-c-branches.json);
the committed-blob correction is substantive and does not claim patch
equivalence. The provider refresh changed only its guide/manual, with source
code/input equivalence recorded in
[package-c-provider-refresh.json](package-c-provider-refresh.json).

No full local integration suite or updater workflow dispatch was started.
Existing push-triggered CI observations are in
[package-c-ci-initial.json](package-c-ci-initial.json) and
[package-c-ci-final-push.json](package-c-ci-final-push.json). Only superseded
active runs for these exact branches were eligible for cancellation; final-head
runs were preserved. No self-hosted VM suite
matches these C paths. HaveAPI's doc change automatically starts its Ruby suite;
Final-head CI monitoring and longer checks follow the lead's complete-deliverable
review gate. Prepared, unexecuted commands and receipt requirements are in
[package-c-live-checks.md](package-c-live-checks.md). At the final push observation, Terraform Go Tests passed on its exact final
head; HaveAPI Ruby and IRC RSpec were running on their final heads. Old-head
runs had already completed successfully, so no cancellation was necessary.
No branch is declared independently reviewed or ready for default integration.
All commands launched by C have finished; there is no machine or repository
claim. Keep session active and open.

The later preparation-only assignment is recorded in
[package-c-post-review-brief.md](package-c-post-review-brief.md), with
[the source/lock manifest](package-c-verification-manifest.json) and
[the nonpublishing driver](package-c-post-review.py). Static preparation checks
passed; no provider build, live updater, VM test or watcher was launched.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
