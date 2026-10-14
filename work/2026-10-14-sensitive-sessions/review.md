# Independent final review

**Blocking — B1: effective exclusion is checked for only one journal filename.**

In `dev-workspace` commit `cbcacdbe593643bd82ab659f02f3d1726940029d`,
`libexec/workspace-sensitive-sessions.rb:105` probes only
`worktrees/.locks/<slug>.creation.json` for the shared journal exclusion. A
tracked `.gitignore` can override `info/exclude` for a different journal while
that probe still succeeds. For example, with a pre-existing
`!/worktrees/.locks/private.fork.json` rule and no workspace-wide `worktrees/`
ignore, selecting sensitivity succeeds, the normal fork journal writer writes
the private source/conversation metadata, and ordinary `git add -A` stages
`worktrees/.locks/private.fork.json`.

This is an ordinary configuration conflict, without force-adding or a hostile
local operator. It violates the documented refusal on conflicting effective
ignore rules and the feature's local-records guarantee. The same probe gap
applies to the other journal/sidecar filenames. Validate the actual owned
journal and temporary paths before writing them, using Git's effective ignore
decision; preserve unrelated rules and refuse the operation on conflict. Add
a regression case with a pre-existing exception for a non-creation journal.

Origin: general and risk/compatibility lanes. Fix before long integration tests.
No other Blocking or Important findings identified.

**Reproduction and checks**

The following independent check ran in the repository's cached Nix environment,
using only the existing temporary-workspace test fixture. Its assertion
confirmed the unwanted staged filename; no source or production state changed.

```ruby
require_relative 'test/dev_session_test'
class DevSessionTest
  def test_review_journal_override
    with_workspace do |workspace|
      runner = sensitive_fixture(workspace, 'seed')
      ignore = File.join(workspace, '.gitignore')
      File.write(ignore, File.read(ignore).sub("worktrees/\n", '') +
        "!/worktrees/.locks/private.fork.json\n")
      assert_git_success('git', '-C', workspace, 'add', '.gitignore')
      assert_git_success('git', '-C', workspace, 'commit', '-m', 'preexisting journal exception')
      runner.send(:select_sensitivity!, 'private', requested: true)
      runner.send(:prepare_fork_journal!, 'private', 'source', 'private-thread',
        model: 'gpt-test', effort: 'xhigh', requested_model: nil, requested_effort: nil)
      assert_git_success('git', '-C', workspace, 'add', '-A')
      assert_equal("worktrees/.locks/private.fork.json\n",
        git_capture_success('git', '-C', workspace, 'diff', '--cached', '--name-only'))
    end
  end
end
```

Executed via `nix develop --command ruby - --name /review_journal_override/`:
1 run, 10 assertions, and the staged file was exactly the fork journal.

Independent focused verification also passed:

- Ruby sensitive/start/fork filter: 9 tests, 148 assertions, no failures. Run
  with a Nix-provided Ruby through `nix shell --offline nixpkgs#ruby`.
- `nix develop --command go -C portal test -mod=readonly ./internal/session
  ./internal/web -run '^TestSensitive' -count=1`: both packages passed.
- Preparation browser contracts through the repository Nix environment:
  22 cases passed.

The initial standalone Ruby reproduction omitted aggregate fixture support and
failed with `NullTmux` undefined; rerunning through `test/dev_session_test` fixed
the harness. That harness error is not a product finding. No long integration,
deployment, or live lifecycle operation was run. The packet's unrelated web
constructor failure was not independently rerun in this review and remains a
reported limitation on full-package verification.

**Complete history and migration lineage**

I checked each complete base-to-head series, final diff, clean worktree, and
merge base against the locally available default-branch refs:

| Repository | Base | Reviewed head and complete series |
| --- | --- | --- |
| dev-workspace | `3b5550fdb8724d886a2515dd535217d98a02f2e2` | `cbcacdbe593643bd82ab659f02f3d1726940029d` — one commit |
| vpsfree-dev-workspace | `c697acc70b05c9bc6cf7bf53fe63700f1f6c1276` | `3f0777ffb020b5d02c21c65ee7bcd46804768ff1` — one commit |
| workspace | `04bc7050edbb414bfad8a8ff4171f342a64e6780` | `8e21e75d632e4b0f4e54ba1f2ecc8cc6665266f6` — one commit |

No obsolete unmerged approaches or follow-up/fixup history remain in these
series. The runtime commit has one coherent feature purpose: persistence,
creation, lifecycle, policy, presentation, packaging, tests, and its supporting
documentation establish the same sensitivity contract. The extension and site
policy changes are appropriately separate.

**No migrations.** There are no database or state-conversion migrations in the
diffs. The new private sensitivity metadata starts directly at schema 1; the
optional true-only marker is added to existing records. The packet reports that
these formats have never been merged, released, deployed, or externally
consumed. The inspected branch histories contain no intermediate formats or
upgrade-only migrations requiring retention. That lineage is coherent; live
deployment provenance was not independently queried.

**No repeated update streams.** The complete series contains no dependency,
channel, input, generated-artifact or lockfile update stream and no superseded
pins requiring consolidation.

**Architecture, scope, and compatibility conclusions**

The generic runtime correctly owns the capability. I inspected the extension's
`lib.mkPackage` consumption and the workspace's runtime override: the extension
still pins runtime `a0be88432ead4df93eb950f51d08b748ebde2e37`, and the site
overrides it to `3b5550fdb8724d886a2515dd535217d98a02f2e2`; neither consumer pin
changes in this deliverable. The extension and site edits provide policy only.
The feature therefore remains undeployed until a separately prepared package
selects it. No codex-web interface change or node coordination is needed.

The implementation is proportionate to immutable creation-time sensitivity:
one private record/exclusion owner, existing lifecycle journals and content
proofs, and small portal/agent-policy extensions. I found no speculative
framework or abandoned conversion path. The multiple strict readers correspond
to existing Ruby/Go persistence boundaries, although the concrete exclusion
omission in B1 must be corrected.

Ordinary serialized objects omit the added fields, preserving their prior
encoding and digest inputs. Sensitive creation requests retain their choice in
accepted snapshots; fork and plan acceptance inherit source sensitivity.
Creation writes select sensitivity before tracking/conversation writes, and
Ruby manifest validation checks the private choice. Lead and member policies
receive the sensitive-record instruction. Archive/revive retain content proofs,
branch/ownership checks, coordinator fencing, and recovery state while skipping
tracking commits. The tested archive retry preserves the unrelated index and
Git HEAD. Package preparation and activation require sensitive-session support
when private metadata exists; older strict readers reject sensitive fields.

Residual verification gaps are the full packaged suite, live matching-package
activation/recovery, and a browser-to-CLI sensitive plan/fork integration run.
The new Go web tests exercise request/encoding helpers rather than that complete
flow. These checks remain for the lead after B1 is resolved. Force-adds,
out-of-band writers, encryption, and portal access-policy changes remain outside
the accepted contract.

Review performed independently by `/root/final_review`, catalog fallback
`lead_reviewed/reviewer`, GPT-6 Astra/xhigh, with read-only application access.
All four required review references and applicable workspace/repository guidance
were read. Only this report was written. This is a review finding record, not
integration or deployment approval.
