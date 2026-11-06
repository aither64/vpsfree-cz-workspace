# W: blog project-map entry

Status: implementation and quick checks complete; published and source accepted
by the lead, pending independent final review by reviewer0. Integration is not
authorized by this package. Implementer3 retains ownership of W review fixes.

## Requested result and scope

The user requested adding the blog repository to the instructions, then selected
this workspace's `docs/agent-instructions/projects.md` after the lead linked it
("yep, that's it"). The direct lead brief authorizes one ordinary project-map
bullet. It identifies Hugo, the Czech and English domains, the canonical SSH
remote, content/layout/build/author scope, and configuration ownership of hosting
and shared Discourse setup. Acceptance is this concise entry in the maintained
map, matching its existing style.

The extension repository has no concrete project list. Its canonical default
`master` at `f8da821e3c76e26e73aa9d89a712eab0e0faa319` has README.md:18-19
delegating project destinations to consumers and AGENTS.md:48 assigning concrete
site procedures to consuming workspaces/configuration. Inspection and fetch only:
no extension worktree, source edits, commits, publication or registration.

No duplicate list, registry, instruction cleanup, input changes, package build,
deployment or default-branch integration is part of W. These are technical agent
instructions; no member-facing prose or translation was authored.

## Source and history

- Owner: implementer3; retained Sol/xhigh, workspace_write. Lead owns shared
  plan/state, acceptance and mandatory review invocation.
- Repository: workspace, `git@github.com:aither64/vpsfree-cz-workspace.git`.
- Feature checkout:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/workspace`.
- Branch: `2026-11-06-multilingual-blog-migration`, created/registered with
  `dev-session worktree add` from shared local master.
- W base: `c122387075f6109135db2f53845aa77b8cf2838e`.
- Final/published head: `c3799bb22e7ead2a3738105bad96bfc34d3b8641`.
- W series: one commit, `c3799bb22` — Document the bilingual blog in the
  workspace project map. Only `docs/agent-instructions/projects.md` changes:
  five insertions, zero deletions.
- Shared checkout remains on master; its project-map working file is unchanged.
  Feature checkout is clean. No shared index changes were made.
- No migrations, schema/state changes, obsolete approaches, follow-up fix commits,
  dependency/pin/generated update streams or compatibility paths in W.
  Existing master history was retained without rewriting.

Fresh SSH remote proof reports feature head `c3799bb22e7ead2a3738105bad96bfc34d3b8641`
and remote master `2b5944e8df2ba06fb3193264c231adafa8329b5c`.
Native capture-comparison saved that remote merge base and final head. Shared
local master was already 19 coordination commits ahead of remote master; their
changed paths are exclusively `archive/`, `notes/`, and `work/`. The full remote
base-to-head range therefore has these 20 commits in order:

```text
3f3cd76d11a81527e9344363cacc5a964e9f179f workspace: archive 2026-10-31-team-workload-parallelization
3d01ff72dd93058a988c1edad516262e2003d5b5 Record container image pipeline investigation plan
5e5b3282bff4972716b7f4b7182387d8741fd5c1 workspace: archive 2026-11-02-session-temporary-service-cleanup
46f0389ff359a84eea65ab67326e1aa7318c841d Plan urgent Alpine SSH password authentication mitigation
88ee4e2426511586dc225fd1a0351dce99a62043 Finalize container image pipeline plan
4c45c02acd9eccb1905ea4e60da3769f4caba520 workspace: archive 2026-09-13-partial-ip-replace
ce7ed71561b968fa8e604e12a063838eb0d09123 workspace: archive 2026-09-13-upload-test
d99e714eb5fe75b2a8bb2d1cbf238cb9956829d8 workspace: archive 2026-09-14-restore-into-vps
f3926020a55b77cc3d82e665b733501213f1b6a6 workspace: archive 2026-09-14-user-metrics-docs
b5bcd3fb01348c2de1940514bb88bdcbf2e3e846 workspace: archive 2026-09-24-vpsadmin-pr-44
7e834463e03ffc06d5ca5820dab9a4d312942e6b workspace: archive 2026-10-04-Slug_canary_a459229a
4e97a37a32127951d3dcece18c378cb5bccbff20 workspace: archive 2026-10-04-automatic-slug-verification
d46dbd80088027e0df9ecee5a601a224a9e62381 workspace: archive 2026-10-16-idle-coordination
b73645a294b74681e034669800c02344748d2d0c workspace: archive 2026-09-01-vpsadmin-rbac
f591e85ba5b737ca6701d0d3f02cab3355e6b224 Record container image pipeline implementation and local acceptance
0b25061aafbd328cacc6b7bea5dc558bc8c7f3b4 work: plan reliable portal message delivery
91b6a431223f031562008431fe58d6458b45e7a1 workspace: archive 2026-11-05-disable-ssh-password-authentication
85f0da48be1e87641ea0ea7857c8987e7aa598c1 Record mx2 public cutover and acceptance
c122387075f6109135db2f53845aa77b8cf2838e Plan multilingual static blog migration
c3799bb22e7ead2a3738105bad96bfc34d3b8641 Document the bilingual blog in the workspace project map
```

Inspect the complete substantive W diff in the feature checkout with `git diff
c122387075f6109135db2f53845aa77b8cf2838e..c3799bb22e7ead2a3738105bad96bfc34d3b8641`.
The remote comparison includes inherited coordination-only records (185 files,
28,404 insertions and 1,033 deletions including W); W itself remains five lines.
The inherited 19 commits are metadata classification context only; do not inspect
peer record contents or rewrite their existing shared-master history.

## Verification and review routing

- `nix develop -c ruby test/agent_instructions_test.rb`: passed, 10 runs,
  217 assertions, zero failures/errors/skips.
- `git diff --check` and the final committed W-range whitespace check: passed.
- No declared hook framework/configuration or custom active hooks; core.hooksPath
  is unset. Commit used a temporary message file with `git commit -F`; no hooks
  were bypassed.
- `git merge-base --is-ancestor master HEAD`: passed against unchanged local
  master `c122387075f6109135db2f53845aa77b8cf2838e`.
- SSH push succeeded, and `git ls-remote --heads` independently verified exact
  published head. No GitHub workflows exist in this workspace source tree.
- No new tests or long builds are needed for this catalog entry. Existing checks
  do not validate live blog hosting or forum behavior; this package changes
  neither. No runtime, schema, protocol or rollback behavior changes.

Risk: low; localized, reversible technical documentation. Applicable review lane:
general only. The lead has assigned reviewer0 for mandatory-change-review with
saved settings, requiring explicit complete-W-history,
no-migrations and no-repeated-update-stream conclusions. This packet does not
claim independent review is complete. No design deviation from the corrected
lead brief; the initial extension location was rejected after authoritative-source
inspection and the user's explicit workspace-map selection.

Session plan/state: [plan.md](plan.md), [state.md](state.md).
Stable session URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/
