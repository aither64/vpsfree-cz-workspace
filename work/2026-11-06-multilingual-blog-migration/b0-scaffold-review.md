# B0 local scaffold review material

Ready for lead acceptance and independent final review. No source edits remain
intended. No source publication, default initialization or production deployment
has been performed.

## Source and whole-history scope

- Repository: `git@github.com:vpsfreecz/blog.git`.
- Canonical bare clone: `/home/aither/workspace/ai/vpsfree.cz/repos/blog.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog`.
- Local feature branch: `2026-11-06-multilingual-blog-migration`.
- Final head: `04b6ecc6dd286a4932910c1a8da12a5d28be1df8`, clean worktree.
- Complete series: one genuine root commit, `Add a pinned bilingual Hugo scaffold`.
  Review the full diff against empty tree
  `4b825dc642cb6eb9a060e54bf8d69288fbee4904`; this is a comparison coordinate,
  not an invented historical base. There was no preexisting source commit.
- 27 files, 572 added lines: Hugo config, layouts/CSS/i18n; pinned Nix build;
  `bin/{build,check,preview}`; README/AGENTS; empty shared data and isolated
  synthetic paired/unpaired draft fixtures. No real content or translations.
- No database migrations, import output, dependency refresh streams, deployed
  history or externally consumed schema versions. Initial local scaffold heads
  `11d94a5c2083fabb5d1d0be8d707cece65f2b786` and
  `cc71ea80655a9b445bc1b42e45815d4c9e51c2c5` were amended into the final root;
  they were never pushed, released or deployed as production/supported source.
  Required follow-up fixes are consolidated; no obsolete approach remains in
  the final series.

## Verification

All final checks passed at the exact final head:

- `nix develop -c bin/check --preview`: dual host roots, production canonicals,
  reciprocal alternate and paired translation links, explicit underscore paths,
  missing counterpart/shared metadata, draft exclusion, no production embeds,
  feed placement/self URLs and deterministic duplicate output. Runtime assertions
  prove both local `/feed/` endpoints return 200, RSS content type/body and no
  `Location` or followed redirect.
- `bash -n bin/build bin/preview`, `git diff --check` and clean Git status.
- `nix build .#site --no-link --print-out-paths`: passed. A repeat
  `nix build .#site --rebuild --no-link --print-out-paths` passed Nix's output
  equality check. These were completed before the lead's latest instruction to
  defer any still-remaining build until review; no further build is pending.
- Four live HTTP pages returned 200: each homepage and its paired synthetic
  article; article language links used the two loopback listeners.

The first uncertain environment acquisition and Nix build used fresh retained
catalog Luna/low watchers under the full-access/approval-never policy. Logs:
`/tmp/blog-b0-environment.log`, `/tmp/blog-b0-nix-build.log`. Initial build failed
because `/usr/bin/env` is absent in Nix's sandbox; standard `postPatch =
"patchShebangs bin"` fixes this. With dependencies already cached, the final
build/rebuild ran inline as known short checks (seconds). No kernel build.
No repository hook framework exists; only inactive Git hook samples are present.
No hook was bypassed.

## Exact final artifact and inputs

- Output: `/nix/store/sh2ak12cwykqhllwkfkck0kkn3i9zf3i-vpsfree-blog-0`.
- Derivation: `/nix/store/9i2pzmm702dqqkhbkisncdf3x4d1fr7j-vpsfree-blog-0.drv`.
- Source: `/nix/store/8iy7pf073kkga8310x5bn0d9riy9bi0j-source`, revision
  `04b6ecc6dd286a4932910c1a8da12a5d28be1df8`, NAR hash
  `sha256-b12Nboll8RqTs6OCdiK26UEW+WB1N6O/ZDgpavwdA9o=`.
- Single external flake input: Nixpkgs
  `f3a73bcf5d1c5b75a66cf35a48957e30d41d647a` (`nixos-26.05`), NAR hash
  `sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=`.
- Hugo `0.167.0`, Python from that same locked Nixpkgs input. `flake.lock` is the
  complete source/input graph. `metadata.json` records these exact source/input
  identities and SHA-256 for all 12 served files outside `cs/` and `en/`.

## Preview and native feed mapping

Registered service `blog-b0-preview`, ID
`b0930238-6cc2-4cc0-b511-e1d36c306067`, remains running. Launch command:
`nix develop -c bin/preview`, registered through `dev-session service run` with
the exact worktree above. It binds loopback only:

- Czech <http://localhost:1313/>; fixture
  <http://localhost:1313/synteticky-priklad_1/>.
- English <http://localhost:1314/>; fixture
  <http://localhost:1314/synthetic-example_1/>.

Native Hugo preview configuration rewrites `/feed/` internally to
`/feed/index.xml` with RSS response headers on both listeners. Architect accepted
this verified contract. Later production nginx must map `/feed/` explicitly and
emit `application/rss+xml`; generic directory indexing will return 404. Source
feed links and RSS self links retain `/feed/`.

## Registration and limits

Remote SSH `ls-remote --symref ... HEAD refs/heads/*` returned no refs. Bare HEAD
still points at unborn `refs/heads/main`; it has not been changed. No branch has
been pushed. Remote default and initial publication target remain unselected;
`main` is only the clone's provisional unborn target.

Initial helper attempts failed on empty remote HEAD, then on nonexistent
`origin/master` with `--no-fetch`. The runtime's existing-branch path rejects
`--base` as a way to establish historical origin. Current portal manifest now
contains the exact blog branch with no `initial_base_sha`, but has helper fallback
`default_branch: master`. That value is not an observed remote default or approval
of a target. Implementer has not rewritten the manifest or origin/default HEAD
to conceal this mismatch. Lead owns resolving the actual target after explicit
initialization/integration direction; no runtime-tooling project is needed.

The shell tolerates missing optional shared metadata/comments and has a passive
discussion-URL slot plus forum link. It has no production embed integration or
historical comment renderer. RSS intentionally has no items; real GUIDs/full
content and English feed policy await import work. No full corpus, browser visual
or keyboard sweep, real content fidelity, Discourse runtime test, CI, authoring
skill, publication automation or production hosting is claimed. Independent
final review and source initialization approval remain outstanding.

Lead applied the user-facing writing skill directly to the initial README and
CS/EN labels, with no requested wording changes. The only subsequent README
addition documents the verified native feed rewrite and production mapping.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/>.
