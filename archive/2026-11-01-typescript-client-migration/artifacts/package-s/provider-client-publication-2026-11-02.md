# Provider and client documentation feature publication

Session identity and both environment variables matched
`2026-11-01-typescript-client-migration` and the bound workspace. The lead
granted the HaveAPI/client publication turns only. Both repositories had clean
indexes/worktrees, no Git operation/lock markers, configured contributor
author/committer `Jakub Skokan <jakub.skokan@havefun.cz>`, canonical SSH remotes
and the expected checked-out feature branch. No source/head rewrite occurred.

Both remotes were freshly fetched with explicit default/feature refspecs and
`--no-tags --no-prune`. Feature publication used ordinary fast-forward SSH
pushes to `refs/heads/2026-11-01-typescript-client-migration`, without force.

| Repository | Old remote feature | Verified new remote feature | Fresh default, unchanged by these pushes |
| --- | --- | --- | --- |
| `git@github.com:vpsfreecz/haveapi.git` | `eea3ae5e82c3db23d5f5bc9f1a5e7784117c4e1b` | `52c37027f194ba1141fb7f5e5b6b45828989b126` | `master`: `eb91a4d031c2c1f1c6ec6dd1aaed62e1f320eea7` |
| `git@github.com:vpsfreecz/vpsadmin-typescript-client.git` | `99ee06654ef956a09b52749f4cd02d1435362087` | `e16663a9e7ed1bbd7e25337b824283f635f47395` | `main`: `e5786f69b7c223c3bb5b1de99b7f97186eec368a` |

HaveAPI's fresh default has ten documentation/localization/server-UI commits
beyond the feature's base `391b0190241cf195a69b06f7297d3e4eebec5a83`.
Its 108-file delta includes TypeScript documentation emitter/spec changes.
Those default changes were inspected as upstream context only; they were not
rebased, merged, tested or substituted for the client's exact generator pin.
The feature/default merge base remains `391b0190`. The client's default remains
its original base. Each old remote feature was independently proved an ancestor
of its approved documentation follow-up before pushing.

The first HaveAPI push failed locally with exit 1 because the publication
environment could not load Overcommit. The initial Git 2.54/Ruby 3.4.9 and
restricted `GEM_PATH` did not reproduce the owner's successful hook environment.
The failure was not counted as success. Authoritative remote reconciliation
proved the feature still at exact `eea3ae5e`, with clean local `52c37027`.

The owner then recovered the exact already-realized environment from the
successful `52c37027` commit and supplied it without installation or Nix
evaluation. A read-only load/version probe passed. One corrected normal
HaveAPI push then completed with exit 0 through its ordinary Overcommit
pre-push hook, without bypass:

- Ruby: `/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`.
- Git: `/nix/store/2k05jnr38sryn0fnvlrmjrshxbphj3jp-git-2.56.0/bin/git`.
- Bundler 4.0.23 and Overcommit 0.74.0 from the existing HaveAPI `.gems`.
- `GEM_HOME` was the exact HaveAPI worktree `.gems`; `GEM_PATH` was the pinned
  Ruby `lib/ruby/gems/3.4.0`, with its matching `RUBYLIB` and executable path.

The client has no declared hook framework and its hooks directory contains
samples only. Its ordinary push completed with already-realized Git 2.54.0.
Both remote feature SHAs and default SHAs were verified with `ls-remote` after
the successful pushes. Both final indexes/worktrees are clean:

- HaveAPI HEAD `52c37027f194ba1141fb7f5e5b6b45828989b126`, parent
  `eea3ae5e82c3db23d5f5bc9f1a5e7784117c4e1b`, tree
  `ab690f37de793babf1a066eca5c431aadaa4106d`.
- Client HEAD `e16663a9e7ed1bbd7e25337b824283f635f47395`, parent
  `99ee06654ef956a09b52749f4cd02d1435362087`, tree
  `2cafe84faeecb0e4ff52291ec874d236dc4880b1`.

One bounded registration snapshot per repository was handed to the lead;
these are registration/status observations, not CI acceptance:

| Repository/head | Workflow | Run | Snapshot status |
| --- | --- | --- | --- |
| HaveAPI `52c37027` | release | [41461452497](https://github.com/vpsfreecz/haveapi/actions/runs/41461452497) | in progress |
| HaveAPI `52c37027` | i18n health | [41461452603](https://github.com/vpsfreecz/haveapi/actions/runs/41461452603) | in progress |
| HaveAPI `52c37027` | servers/ruby performance | [41461452542](https://github.com/vpsfreecz/haveapi/actions/runs/41461452542) | in progress |
| Client `e16663a` | Package validation and release | [41460425540](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/41460425540) | in progress |

The branch snapshots showed no queued/in-progress superseded old-head runs to
cancel; prior runs were terminal. No CI wait, rerun, dispatch or cancellation
was performed. The parent coordinates fresh utility monitoring after handoff.

The selected generator/source and artifact remain exact `eea3ae5e` and
`99ee066`: the new README Git heads are documentation follow-ups, not a new
generation identity or a repacked selected artifact. Existing source, archive,
review and CI receipts retain their original inputs. No tests, builds,
dependency installs, regeneration, packing, PR/comment creation, registry
publication, tag/version change, default-branch write, deployment or session
lifecycle action ran. No operation or uncertain effect remains. Both Git turns
are returned to the lead.
