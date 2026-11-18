# Package B: vpsadminos.org one-time channel update

Owner: implementer1. Corrected generated change is committed and published;
evaluated inventory complete and all checks passed. Git/index/rebase/hook-preparation window
released to lead; no further feature-head changes without coordination.

## Final source and history

- Repository: `git@github.com:vpsfreecz/vpsadminos-org-configuration.git`.
- Default target: `master`; fresh fetched base
  `91b5f45d8956c1cd8102e74cf720da306107b308`.
- Final head: `72c18d811086dac8e16ec8c7ee6bf8e32ce62123`.
- Branch: `2026-11-18-nixos-channel-update`.
- Registered worktree:
  `worktrees/2026-11-18-nixos-channel-update/vpsadminos-org-configuration`.
- Complete final commit inventory: one generated commit,
  `72c18d811086dac8e16ec8c7ee6bf8e32ce62123 inputs: set nixpkgs to 4077fb98`.
- Complete final file inventory: `flake.lock`, three insertions/three deletions.
  Only `nodes.nixpkgs_3.locked.{lastModified,narHash,rev}` change.
- No database migrations, state-format, API/protocol, module/stateVersion,
  application or reusable documentation changes. No migration was merged,
  released, deployed or consumed in this package. No obsolete commits remain
  in the final base-to-head range.

The initial branch-switch interpretation was superseded by the user's explicit
one-time-update correction. Unpublished commits
`61077af169502940733161e49320045177a0cb89` and
`63b9777d5129bd331f0527cfa11d21e3b2f7a731` were removed from this feature branch
with narrow owned `git rebase --onto <base> HEAD`. Neither was published or
integrated. The final single pin commit was generated afresh from the original
base; it contains no branch-switch or reversal commit.

## Channel command and invariant proof

The original `flake.nix` remains byte-identical to base, including
`github:NixOS/nixpkgs/nixos-26.05`. Channel `nixos-stable`, role `nixpkgs`, maps
to root input `nixpkgs`; its resolved lock node is `nixpkgs_3`, not the unrelated
node named `nixpkgs`.

Final command, run from the repository's pinned environment:

```sh
nix develop -c confctl inputs channel set --commit --no-changelog nixos-stable nixpkgs 4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d
```

Pinned Setter was inspected: it saves the selected root node's complete
`original`, generates a temporary lock through Nix `--override-input`, restores
that complete `original`, and atomically installs the generated lock. No manual
lock editing occurred. The final complete `original` equals base:
`{owner=NixOS, repo=nixpkgs, ref=nixos-26.05, type=github}`. All other lock nodes,
root role mappings and follows edges are unchanged, verified by Python equality
assertions against committed base and head snapshots. Independent source
revisions, including confctl and vpsAdminOS, remain unchanged.

| Locked identity | Base | Final |
| --- | --- | --- |
| Revision | `f68407657ad294471eb4b2e65d193df26edf729f` | `4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d` |
| lastModified | `1794872590` | `1795018498` |
| narHash | `sha256-E+XLAfnC7+bdr4qlEgRv6cdGmiqTU5oeFNKCha7epqQ=` | `sha256-zX+62p0XLF5AbMgzy8JgNBH6cTJSiDovTOSk2NBc0GQ=` |

`vpsadminos` follows root `nixpkgs`, so the selected source is intentionally
shared through that existing edge. Future ordinary updates still track
`nixos-26.05`; the scheduled forward-only job may defer until that branch catches
up. No deployment or coordinated cross-repository update is introduced.

## Quick checks and upstream evidence

All passed at the exact final head:

- Required Overcommit pre-commit Nixfmt and commit-msg subject/period/width hooks.
- `git diff --check <base>..HEAD`; worktree/index clean after commit.
- Committed semantic lock assertions: only resolved root node changes; only
  revision/hash/timestamp attributes change; exact selected SHA; full original
  equality; base/final flake bytes identical; every sibling node and edge equal.
- Fresh GitHub compare of PR #589970 merge
  `1e6cf0d7cf5f5354d1bfd7105813dddb527851d4` to exact final locked SHA:
  `status=ahead`, `ahead_by=6`, `behind_by=0`, merge base equals the PR merge.
  [Exact comparison](https://github.com/NixOS/nixpkgs/compare/1e6cf0d7cf5f5354d1bfd7105813dddb527851d4...4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d).
- Direct locked-source inspection at
  `/nix/store/c4yfavidc9v8h69a14xglml250qnlksw-source`:
  `pkgs/servers/http/nginx/stable.nix` is 1.30.7 with source hash
  `sha256-JWW1yDcFDpWPcPsPc8SOK8pFQq00n9NW9G+wxyYQvG4=`;
  `mainline.nix` is 1.31.9 with source hash
  `sha256-oRxe7uLiV/RHjw5kn4SwBAeH0nfS0+UjOVKqa23LgK0=`.

Publication succeeded over SSH to `origin/2026-11-18-nixos-channel-update`.
Fresh `git ls-remote` verified that remote ref equals exact final
`72c18d811086dac8e16ec8c7ee6bf8e32ce62123`.
No PR was created. Lead owns final independent history assessment and integration.

## Environment and hooks

Session identity and complete environment matched `dev-session current`; roster
confirmed saved Sol/xhigh with workspace-write and full execution access. Initial
plan/state commit `d918b4539a432f4f39fd340f902fb333e195cae2` was verified.
No tracked repository AGENTS, README or Markdown docs exist at the fetched base.
Read flake/workflow/Gemfile/hooks and pinned confctl input documentation.
Pinned confctl: `ff5e017780a35fb97b549db2a51b570193867c3b`; tools-mode shell,
Bundler 4.0.7, Overcommit 0.68.0. Required setup:

```sh
nix develop -c bash -eu -c 'bundle exec overcommit --install; bundle exec overcommit --sign; bundle exec overcommit --sign pre-commit'
```

Bootstrap ran under a fresh installed Luna/low utility, passed in 18 seconds;
log `/tmp/nixos-channel-update-package-b-bootstrap.log`. All utility cells/tool
sessions completed; no kernel build occurred. No hooks were bypassed.

During the now-superseded URL edit, `nix develop` tried resolving the new ref;
it was interrupted before any lock or commit effect (verified only flake.nix
was dirty). The original base store snapshot supplied the same pinned shell
until that superseded channel update finished. Final corrected set used ordinary
repository `nix develop` after original base restoration.

## Evaluated inventory

Completed successfully at exact final head; both evaluation commands exited 0,
with empty stderr. All 11 managed machines resolve the changed root input
`nixpkgs` to `/nix/store/c4yfavidc9v8h69a14xglml250qnlksw-source`. All 11 have
no failed assertions. Four selected toplevel derivation paths evaluated
successfully; no systems or packages were realized.

Configured nginx targets that receive the fix:

| Exact confctl selector | Host alias | Package selection | Change |
| --- | --- | --- | --- |
| `org.vpsadminos/int.images` | `images.int.vpsadminos.org` | stable with fancyindex | 1.30.6 → 1.30.7 |
| `org.vpsadminos/int.iso` | `iso.int.vpsadminos.org` | stable with fancyindex | 1.30.6 → 1.30.7 |
| `org.vpsadminos/int.www` | `www.int.vpsadminos.org` | stable | 1.30.6 → 1.30.7 |
| `org.vpsadminos/proxy` | `proxy.vpsadminos.org` | stable | 1.30.6 → 1.30.7 |

Other changed-channel consumers, excluded from this nginx deployment subset
because evaluated `services.nginx.enable = false`:

| Exact confctl selector | Host alias |
| --- | --- |
| `org.vpsadminos/int.builder` | `builder.int.vpsadminos.org` |
| `org.vpsadminos/int.cache` | `cache.int.vpsadminos.org` |
| `org.vpsadminos/int.docker-registry` | `docker-registry.int.vpsadminos.org` |
| `org.vpsadminos/int.gh-runner1` | `gh-runner1.int.vpsadminos.org` |
| `org.vpsadminos/int.gh-runner2` | `gh-runner2.int.vpsadminos.org` |
| `org.vpsadminos/int.gh-runner3` | `gh-runner3.int.vpsadminos.org` |
| `org.vpsadminos/int.gh-runner4` | `gh-runner4.int.vpsadminos.org` |

Independently sourced enabled nginx consumers outside this fix: **none**.
All four actual `services.nginx.package.src` identities (source derivation,
output path, URL and hash) equal upstream `nginxStable` from their resolved
input in both old and new configurations. All four unit `ExecStart` values
select their evaluated package output `/bin/nginx`; no redirected executable
was found. Fancyindex alters package derivation/output paths while preserving
the same upstream source.

Exact common source identities:

- Old: `https://nginx.org/download/nginx-1.30.6.tar.gz`, `sha256-PPRvXtdQTUYBJYZre+qZ+zV/MdiH4uY7NVAzEOm4tsg=`;
  source drv `/nix/store/0i0g5lbc5jva8wvyh4qmx0xfd91s9g01-nginx-1.30.6.tar.gz.drv`;
  source output `/nix/store/f0zrkfmzd2gfskdxijmrj67dp1sfr4j5-nginx-1.30.6.tar.gz`.
- New: `https://nginx.org/download/nginx-1.30.7.tar.gz`, `sha256-JWW1yDcFDpWPcPsPc8SOK8pFQq00n9NW9G+wxyYQvG4=`;
  source drv `/nix/store/d6kgcj285iifmlnk9w1vq4gz3g4lsyl4-nginx-1.30.7.tar.gz.drv`;
  source output `/nix/store/z255nq6zrhzqaikkjsp9hbks8v9v55hd-nginx-1.30.7.tar.gz`.

Exact evaluated packages:

- fancyindex:
  old drv `/nix/store/drc3h607lmmljv89k14lrwyhk684m9gb-nginx-1.30.6.drv`,
  output `/nix/store/9rp6v4swlcyygvqz6ig1kva9z9qd1kzp-nginx-1.30.6`.
  new drv `/nix/store/nfr49839dpnkysrwz50r47ddhwh44x33-nginx-1.30.7.drv`,
  output `/nix/store/iik03rj0b3gj0sd6ichrh0v5x2j1gy6q-nginx-1.30.7`.
- default stable:
  old drv `/nix/store/i1dqdwsfsnhkvpdhcm2n6nf4q2qs99x8-nginx-1.30.6.drv`,
  output `/nix/store/5dymrmcdrrm9vd8cqbrvmfbm3fd2mphq-nginx-1.30.6`.
  new drv `/nix/store/lz5pkqfpx64qfb6xvq6pz3dyckp9hzay-nginx-1.30.7.drv`,
  output `/nix/store/v5yfyvpd7z7lbzh86bpbh5cjp10qad4m-nginx-1.30.7`.

Exact successful desired-system derivation paths:

- `org.vpsadminos/int.images`: `/nix/store/jxfj248rhy24zz743imnaw6d38sf8k64-nixos-system-images-26.05.20261118.4077fb9.drv`.
- `org.vpsadminos/int.iso`: `/nix/store/fp6pppjrx7xnm3jv4qwhg8ag0yniizm4-nixos-system-iso-26.05.20261118.4077fb9.drv`.
- `org.vpsadminos/int.www`: `/nix/store/jx5042ph6nll1zai3cpw3487nf51fdla-nixos-system-www-26.05.20261118.4077fb9.drv`.
- `org.vpsadminos/proxy`: `/nix/store/bjvlj4vkphlxr3zx84074vpxhnmn7fdf-nixos-system-proxy-26.05.20261118.4077fb9.drv`.

This is desired-configuration evidence, not a claim about deployed generations
or running versions. No build, VM test, machine activation, production read or
machine reservation occurred. Whole-system runtime behavior and rollback for
other package changes remain future rollout checks.

Probe and command evidence:

- `package-b-evaluator.nix` copies pinned confctl evaluator verbatim except
  one lazy output exposing existing `evalConfigFor`. Unique insertion and
  byte equality after removing it were asserted. Original confDir, inputs,
  channels, modules and arguments are unchanged; relocated unused relative
  `moduleOptions` import is never forced.
- `package-b-probe.nix` evaluates the final machine set, assertions and four
  toplevel derivations. `package-b-new-inventory.json` retains the passing data.
- Nix JSON coerces attrsets containing `outPath` into path strings. A second
  narrow `package-b-packages-probe.nix` uses receipt field `outputPath` and
  omits all toplevel/assertion evaluation; old/new package/source identities
  are in `package-b-package-provenance.json`. This avoids repeating the
  successful system derivation check.
- Commands used `nix eval --offline --impure --json --expr` and explicitly
  applied `(import /absolute/probe.nix) { configuration = "/absolute/source"; }`.
  The system pass used the exact final worktree; the narrow pass returned
  `{ old = probe { configuration = "/nix/store/78kjjbxjkhw6p60kaainkrb8fciwdbr0-source"; };
  new = probe { configuration = "<absolute final worktree>"; }; }`.
- `package-b-new-inventory.log` and `package-b-package-provenance.log` are empty
  (both checks exit 0). Complete source graphs are the committed base/final
  `flake.lock` snapshots at the exact revisions recorded above.
- Native utility capacity was occupied by A; monitor skill parent fallback
  was announced once. B inventory tool sessions 38613 and 17672 are both
  completed with exit 0; all corresponding exec cells completed. No unfinished
  commands or uncertain mutations remain. The initial --file/--argstr wrapper
  failed immediately with function-to-JSON; explicit function application
  corrected that probe invocation without source changes.


## Documentation rationale and handoff

This individual pin refresh introduces no reusable behavior or new operating
procedure. Evidence belongs here rather than project documentation. Lead alone
updates plan/state/portal and owns acceptance and integration; session remains
open. No session lifecycle action was requested or performed.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-18-nixos-channel-update/)
