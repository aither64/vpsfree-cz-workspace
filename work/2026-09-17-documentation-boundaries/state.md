---
lifecycle: complete
---
# Documentation boundaries

## Status

The rule change is merged and pushed to master in all three repositories and
deployed on aitherdev as profile generation 49. Full local flake checks, consumer
build, both reviews and provider feature CI passed. Live skill content, fresh
discovery, services and portal artifact verification passed. The additional local
runner smoke and both default-branch CI runs passed. Clean feature and temporary
integration worktrees are removed, retaining branches and comparisons. No review,
CI, deployment or cleanup remains. The session stays open for follow-up.
IP release documentation is represented only by a handoff artifact here; none
of that session's files, branches, worktrees or cluster has been changed.

## Next actions

No operator action is needed for this rule change. The user can give
[the handoff](ip-release-handoff.md) to the IP release session owner when ready.
That session's documentation reorganization is deliberately outside this
initiative and has not been performed or submitted to its conversation.

## Repositories

Branch: 2026-09-17-documentation-boundaries in all three repositories.
Former registered worktrees: worktrees/2026-09-17-documentation-boundaries/{dev-workspace,
vpsfree-dev-workspace,workspace}. No configuration repository was needed.

| Repository | Base | Current head |
| --- | --- | --- |
| dev-workspace | 0bd68efa9cadb0589148fac40de7645a06b03468 | 5bcb83120cf25974ecd2dad7b7e737473169b173 |
| vpsfree-dev-workspace | 90ce0cfe7c39c944aca0c7b27fe1e53a719075a3 | f2fdbcebc115b7fd07ab6e0c91ebea189a57f341 |
| workspace | 2c2ca547e9067ddcac9cae27f24c31d5f3536d5f | fd626e56f6440834c2ce50f32fd7f218a458f020 |

The extension pins the runtime head; the workspace pins the extension head.
Only those exact inputs changed. All worktrees were clean before removal.
Fetched local/remote feature heads match exactly and are ancestors of
origin/master in every repo.
No final head changed during review or integration. Comparisons were captured
with the table's exact bases/heads before merging.

Both independent projects used fresh master worktrees under this initiative's
merge/{dev-workspace,vpsfree-dev-workspace} paths, cached catalog/source checks
and normal fast-forward pushes. Those temporary worktrees are removed.
Workspace integration fast-forwarded the shared master without staging anything
or disturbing unrelated changes. All feature branches are retained.

## Documentation

- [Plan and accepted decisions](plan.md).
- Generic source: skills/dev-session-documentation/SKILL.md and
  docs/dev-sessions.md in dev-workspace.
- Extension source: mandatory-change-review packet/general review and
  dev-session-handoff skill.
- Workspace source: AGENTS.md, Documentation During Development.
- [IP release handoff](ip-release-handoff.md), [verification](verification.md),
  [review packet](review-packet.md) and [executed rollout](rollout.md).

## Verification evidence

Three edited skills pass metadata validation; frontmatter is unchanged. Changed
Markdown relative links and whitespace pass. Workspace focused tests: 3 runs /
14 assertions. Extension forward/reverse smoke: 1 run / 15 assertions. All three
repositories pass full nix flake check, including the runtime host VM. The
consumer build contains the exact reviewed skill contents. Existing sandbox
skips and their scope are documented in verification.md.

The context owner applied English writing guidance. The setup failures and
fixes are summarized in verification.md; no hook framework is declared in these
repositories and none was bypassed.

Review classification: Low, bounded documentation guidance with mechanical pins,
no runtime/state/contract changes. General and architecture lanes use fresh
gpt-6-astra/xhigh agents because the skill is a reusable provider with consumers.
No scope/risk specialist trigger is present in the committed changes.

Both reviewers independently confirmed the classification and reported no
Blocking, Important or Advisory findings. Reports: [general](review-general.md)
and [architecture](review-architecture.md). No remediation or rerun is needed.
Runtime feature CI 35195746255 and extension CI 35195868059 passed. Runtime
default CI 35196917703 and extension default CI 35197036965 passed.
Workspace has no configured GitHub workflow; its local deployment-contract
checks passed.

The user subsequently instructed not to wait for CI. Both default runs had
already been observed successful before that instruction; no additional CI
polling or waiting followed it.

Deployment selected profile-49-link and
/nix/store/mk716d08x840l2wdlc1mbaqpnhabn30f-dev-workspace-0.2.0, retaining 48.
Codex/tmux kept their processes; all four user services are active. Six managed
skill links match the catalog and fresh discovery has no errors. No NixOS host
change, cluster mutation, schema migration or live rollback was needed.

## Ownership and cleanup

The originating external conversation owns this initiative. Session
2026-09-09-ip-release-mechanism is read-only source material and is excluded
from mutations, notifications, deployment and cleanup. Keep all feature refs
and this session after completion.

Initial tracking commit: 2c2ca54. Started the retained slug through dev-session
with an idle-only goal; its managed thread is
01a0ae4a-724b-7383-9fa8-afe2028746e8. Verified DEV_SESSION_SLUG and current both
identify this initiative with DEV_SESSION_WORKSPACE set to the registered root.
The helper recovered its own terminal after a disconnect, and the managed
conversation is idle. Shared master and unrelated changes remain preserved.

The user explicitly requested the separate IP release handoff. Its artifact,
review/deployment evidence and two reusable setup notes are consolidated into
one handoff checkpoint on shared master. No incremental tracking checkpoints
were made between initial planning and this handoff. No archival, deletion,
session stop or delayed cleanup was performed or scheduled.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-17-documentation-boundaries/
