# Documentation boundary verification

## Content checks

The context owner applied the English writing guidance after establishing the
rule and compared each edited instruction with its original. The generic skill
retains its identity, automatic discovery and existing authoring/review scope.
No runtime implementation, session template, schema or invocation metadata is
changed. Generic sources contain no organization or host-specific examples.

Manual scenario assessment of the edited skill and human guide:

| Scenario | Expected placement and preservation |
| --- | --- |
| Small feature fix | A useful comment or paragraph in existing docs; no required document bundle or deployment heading. |
| Transaction rollback retains ownership | Feature/subsystem behavior, including failure semantics; not extracted as software deployment history. |
| Repeatable diagnostic or repair procedure | Separate operations guidance maintained with supported behavior; particular execution results go to an operational record. |
| Supported schema transition | Project upgrade guidance with real source/target or schema boundaries; accessible to other upgraders and retained while supported. |
| One site's rollout checklist | Session or dated deployment record even without dates/hashes in its steps; site procedures stay with configuration ownership. |
| Reset an earlier unmerged review database | Session records, separated from lasting schema/compatibility facts in the same passage. |

The IP release handoff maps the mixed source section by meaning, preserving
general accounting/locking requirements and identifying which upgrade and site
steps need separate homes. It is an artifact of this initiative only.

## Automated verification

- All three edited skill entrypoints pass skill-creator quick_validate.py.
  Their YAML frontmatter is unchanged. The ambient Python lacked PyYAML; the
  validator passed in a python3.withPackages environment from pinned nixpkgs.
- Changed Markdown relative links (6) and whitespace checks pass across the
  three worktrees. No repository declares a Git hook framework, and no hooks
  were bypassed.
- Workspace deployment-contract tests pass: 3 runs, 14 assertions.
- Extension migration forward/reverse smoke passes: 1 run, 15 assertions. The
  first invocation lacked DEV_WORKSPACE_RUNTIME_CONTRACT and failed before
  running tests; supplying the pinned runtime contract resolved it. See
  [local test setup](../../notes/vpsfree-dev-workspace/2026-09-17-local-migration-test-contract.md).
- All three repositories pass nix flake check --no-build and full
  nix flake check --print-build-logs. Runtime host activation/renewal/rollback
  VM test passes (132.26 seconds); no local kernel build occurred. The existing
  sandbox skips remain: runtime session tests skip unavailable real tmux paths
  (12), host tests skip disabled real tmux tests (3), and the extension migration
  suite skips a supplementary-group case (1). No changed-path test was skipped.
- General and architecture mandatory reviews found no issues, using fresh
  gpt-6-astra/xhigh agents. Reviewed heads are unchanged; no remediation/rerun.
- Runtime feature CI 35195746255 and extension feature CI 35195868059 pass. The
  extension CI also passed its devcluster-check runner/configuration smoke.
- Consumer build passes and produces
  /nix/store/mk716d08x840l2wdlc1mbaqpnhabn30f-dev-workspace-0.2.0. Its three edited
  skill entrypoints are byte-identical to the reviewed source worktrees.
- Pre-deployment read-only App Server skills/list checks passed in a project
  and empty directory. All three documentation/review/handoff skills are enabled
  and no discovery errors were returned; all six managed links match the current
  catalog. This is a baseline, not verification of the new package.
- Final comparisons captured with the exact review bases/heads before integration.
  Runtime integration used a fresh master worktree under this initiative's
  merge/dev-workspace path, with cached catalog/source checks and a normal
  fast-forward push. The clean temporary worktree was removed.
- All three exact final feature heads are merged into remote master. The
  extension also used a fresh target worktree and cached metadata/source checks;
  workspace integration preserved the shared index and unrelated working tree.
- Local nix run .#devcluster-check passes: both providers' bridge/local
  defaults/override configurations evaluate and both packaged runners load.
  It uses disposable configurations, never starts VMs and touched no live cluster.
- Live activation and fresh skill discovery pass; see [rollout.md](rollout.md).
  Both provider default-branch CI runs pass. No validation remains outstanding.
- Clean feature worktrees were removed through dev-session worktree remove;
  temporary master worktrees used non-force git worktree remove. An empty merge
  container directory caused harmless unproven-worktree warnings during helper
  discovery; rmdir removed that directory and the now-empty owned group. No
  branch was deleted and the session remains open.

## Final CI

All runs below tested the exact final provider heads in the review packet.
No failed-attempt rerun, force-push or superseded-run cancellation was needed.

| Repository | Branch | Result |
| --- | --- | --- |
| dev-workspace | feature | [Check 35195746255](https://github.com/aither64/dev-workspace/actions/runs/35195746255), passed |
| dev-workspace | master | [Check 35196917703](https://github.com/aither64/dev-workspace/actions/runs/35196917703), passed, including host activation/rollback |
| vpsfree-dev-workspace | feature | [Check 35195868059](https://github.com/vpsfreecz/dev-workspace/actions/runs/35195868059), passed |
| vpsfree-dev-workspace | master | [Check 35197036965](https://github.com/vpsfreecz/dev-workspace/actions/runs/35197036965), passed |

Both extension runs include the packaged runner/configuration smoke. The
coordination workspace has no GitHub workflow; its full local flake check and
consumer build passed. The final handoff records' relative links also resolve.

## Setup observations

Initial tracking commit: 2c2ca54. The helper successfully restarted the exact
retained slug and recovered its own terminal client after an App Server
disconnect. The managed conversation acknowledged its idle-only request;
the external conversation remains the sole implementation owner.

The extension bare clone has no configured fetch refspec. A plain fetch updated
FETCH_HEAD only; an explicit heads-to-origin tracking refspec confirmed the
current master before creating its feature worktree. No source branch was
rewritten. See the existing [bare fetch note](../../notes/cross-project/2026-09-14-bare-fetch-force-lease.md).

The first Python WebSocket discovery probe failed during its HTTP upgrade.
Disabling compression matched the existing Go client and passed without any
App Server restart or session mutation. See the [probe note](../../notes/dev-workspace/2026-09-17-codex-unix-websocket-probe.md).
