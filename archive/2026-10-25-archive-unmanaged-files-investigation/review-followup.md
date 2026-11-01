# Follow-up final review: archive preparation

## Findings and decision

**No new Blocking or Important findings. All four findings in review.md are
resolved at `f094a94b50836028a62920c75f2ebd2a9ea97d94`.** The branch may proceed
to the planned packaged lifecycle integration tests. This is review clearance,
not evidence of deployment readiness or authorization to merge.

## Resolution of the original findings

1. **Saved tmux authority / read-only behavior — resolved.**
   `libexec/workspace-archive-check.rb:37` selects the exact slug's authority in
   read-only mode. The loader's additive read-only option avoids initializing a
   missing authority directory. Conversation validation at lines 51–54 uses
   the non-mutating authority validator with a required creation identity;
   it no longer calls the retirement helper. A legacy live authority without
   that identity becomes a blocker without being rewritten. The fresh-reader
   regression tests modern authority, unchanged authority bytes, unchanged
   tmux identity, legacy refusal and a missing directory.

2. **Cancellation before native send — resolved.**
   `portal/internal/web/archive_preparation.go:387` rechecks the current
   receipt/attempt and active preparation after acquiring the message mutex.
   The cancellation handler uses that same mutex. Cancellation that wins the
   mutex therefore prevents submission; a send that wins it must leave the
   mutex before cancellation can succeed. The shared predicate preserves the
   existing transition/runtime/message lock order. The overlapping regression
   recreates the reviewed interleaving and proves zero native sends after
   successful cancellation.

3. **Removal parent permissions — resolved.**
   `libexec/workspace-archive-check.rb:73` derives required removal parents
   from the discovered containers, checkouts and Git administration records.
   It checks write/search access before the existing checkout-content walk.
   This covers the session group, nested containers and the parent's ability
   to remove the group. The group/nested-parent regression requires archive
   refusal before quiescence or journal publication.

4. **Native identity proof on the ready path — resolved.**
   `libexec/workspace-archive-check.rb:60` invokes the new read-only
   `require-archive-identities` command for every retained-root check, including
   sessions whose filesystem checks already pass. CLI construction preserves
   the selected root, cwd, socket, Codex home and authority coordinates; the
   command validates them using the existing archive-command boundary.
   `portal/internal/teamruntime/runtime.go:1660` proves the root and each
   retained member through their existing native proof owners, permits active
   turns and rereads the atomic roster to reject a changed retained set. Missing
   roster remains the supported root-only case. Missing/foreign/unavailable
   native identity fails before archive execution.

## Affected-lane assessment

I reapplied general, architecture/repetition, scope/proportionality and
risk/compatibility review to the remediations, including the new native helper.
The original report remains the review of unchanged behavior.

The helper belongs in teamruntime, which already owns the retained roster and
member archive identity semantics. It reuses `ProveArchivedRootThread` and
`retainedMemberArchiveState` rather than defining another identity policy. The
new method on the internal Client interface is already implemented by the
pinned concrete workspacecodex client; affected test implementations compile.
No dependency revision or App Server protocol change is introduced.

The helper does not acquire the roster writer operation lock, initialize a
member, resume a thread, archive conversations or change queues. Store.Load
reads without creating state. The existing proof methods validate cwd, source,
project and rollout identity using read operations. Roster revalidation handles
appearance, disappearance and replacement during observation. The stricter
final archive idle/retirement checks are unchanged, so allowing an owned active
turn at this boundary does not weaken destructive-phase validation.

The read-only loader flag and shared current-preparation predicate are bounded
changes to their owning components. They do not add migration paths, another
lifecycle reservation or a generalized safety framework. The documentation now
correctly includes native conversation identities among readiness checks.
The private preparation / old-readable receipt compatibility design from the
initial review remains unchanged.

## Final series, consolidation and migration conclusion

Reviewed the final diff from base/merge base
`9634151b9836311c331a58880fbb4c46133fd98f`, the full current series, and the
range-diff against the previously reviewed head:

1. `fd06d9d9f4aebb581882f3b5d061664c6da95eaa` — archive readiness checker,
   including its read-only authority/native proof and permission remediations,
   supporting CLI/packaging/documentation and owning tests.
2. `f094a94b50836028a62920c75f2ebd2a9ea97d94` — portal preparation and repair,
   including the cancellation remediation and overlapping regression.

The remediations are folded into their owning commits. The two purposes remain
independently reviewable. **No obsolete branch approaches or fixup history
remain; no additional history consolidation is needed. No repeated dependency,
input, channel or generated-update streams exist. No migrations.** The private
preparation schema remains its initial schema 1; existing lifecycle and recovery
formats are unchanged. The packet records no merge, release, deployment or
external consumption requiring an intermediate version.

## Verification and residual risks

Focused checks run during this follow-up in the repository Nix environment:

- Ruby authority/reader/parent-permission regressions: **3 runs, 44 assertions,
  no failures or errors**, 1.529 seconds of test execution.
- Focused Go cancellation, native identity, strict archive readiness and root
  proof tests: **pass** — web 0.211 seconds, teamruntime 2.094 seconds,
  workspacecodex 0.045 seconds. The command package compiled successfully;
  the selected expression matched no command-package tests.
- `git diff --check 9634151b..f094a94b`: pass. The implementation worktree is
  clean. No implementation files were edited by the reviewer.

A concurrent Nix evaluation briefly reported a busy evaluation-cache database;
the invocation continued and all selected checks passed. No VM, long integration
or live lifecycle operation ran during this review.

The packaged native VM is still required to prove the full CLI-to-native
identity command, real shell-tool repair, held inference across portal restart,
unrelated session creation and existing journal recovery after later I/O
failure. Unit tests and command-package compilation alone do not prove that
path. The older-reader/package-shutdown boundary also remains a packaged
verification requirement. The scheduling-sensitive inotify failure fixture and
external writers changing state after preflight remain the residual limits
listed in review.md. Final locked validation and journal-owned recovery remain
necessary.

Reviewer: same independent standalone `/root/final_review`, unchanged
`gpt-6.1-sol` / `xhigh` assignment. Overall risk remains high; all four review
lanes were applied where affected. No subagents or nested reviewers were used.
