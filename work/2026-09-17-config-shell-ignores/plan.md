# 2026-09-17-config-shell-ignores

## Goal and scope

Prevent confctl development-shell artifacts from blocking session archival.
The only project change is vpsfree-cz-configuration's root .gitignore:
ignore /.bin/, /.bundle/ and /.rubocop_cache/ with a rationale comment.
The pinned confctl shell creates Bundler configuration, RuboCop binstubs and
cache files in these directories. Existing .gems remains untouched.

## Approved execution

Create a dedicated configuration worktree on this initiative's branch. Run
quick verification and required hooks, then one focused general review using
gpt-6-astra/xhigh. The user explicitly reduced review scope to one pass.
Capture the comparison, publish the branch, and fast-forward configuration
master over SSH. Master integration is explicitly authorized.

After integration, delete only .bin and .bundle from these worktrees under
worktrees/<session>/<name>:

| Session | Name |
| --- | --- |
| 2026-06-15-vpsadmin-events | vpsfree-cz-configuration-release-cleanup |
| 2026-06-15-vpsadmin-events | vpsfree-cz-configuration-release-cleanup4 |
| 2026-09-09-ip-release-mechanism | vpsfree-cz-configuration |
| 2026-09-11-daily-update-llm-agents | vpsfree-cz-configuration |
| 2026-09-11-portal-trusted-host | vpsfree-cz-configuration |
| 2026-09-14-ddns-exception | vpsfree-cz-configuration |
| 2026-09-14-kernel-history-fix | vpsfree-cz-configuration |

Also remove .rubocop_cache from the first worktree. Recheck exact paths,
generated contents, symlinks, and tracked-file absence immediately before
deletion. Preserve every other file and all existing branch heads. No wildcard
cleanup, git clean, local ignore overrides, rebases of other sessions, lifecycle
changes, or cleanup of the separate temporary merge worktree.

## Compatibility and deployment

No application, API, database, protocol, persistent format, or NixOS module
changes. Old and new runtimes work unchanged; no coordinated rollout or aitherdev
deployment is needed. Rollback only restores visibility of generated files.
Older session branches inherit the fix when their owners resume and rebase.
All sessions stay open; branch refs are retained.

## Verification and documentation

Verify real shell outputs are ignored and tracked files stay unchanged. Verify
unrelated untracked files, tracked edits, and nested directories are not hidden.
Run declared Overcommit hooks. Confirm all seven worktrees are clean afterward
and their heads and other files are unchanged. No host build or integration
suite is warranted for ignore rules. Record evidence here and in state.md;
keep the durable explanation beside the ignore rules and in a workspace note.
