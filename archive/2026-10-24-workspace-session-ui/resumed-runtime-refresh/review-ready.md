# Resumed runtime refresh: committed affected-review packet

Repository: `git@github.com:aither64/dev-workspace.git`.
Owned worktree: `worktrees/2026-10-24-workspace-session-ui/dev-workspace`.
Branch: `2026-10-24-workspace-session-ui`.

- Original reviewed range: `10bb047513c82d1310e8fcaa797e8772f948dd8a..9293e314e6028d71a57595073117b51bdc53c8ff`.
- Current merged default and deployed preservation base: `9634151b9836311c331a58880fbb4c46133fd98f`.
- Final head: `24e66096ae65a97b1e2d14b68a566f44519a8c2d`.
- Final tree: `cd8bbc8dca31258538ff1a49ba4b92e1ab391586`.
- Remote feature remains original `9293e314`; publication is held until affected review.

`before.json` records the first fresh default `ec53874b` and its ancestry into
the deployed `9634151b`. A later fresh fetch found default exactly `9634151b`;
`final-preflight.json` records this transition. Thus this candidate contains all
merged performance/retention changes and the complete deployed reliability delta
as literal ancestors. It does not reconstruct an older baseline or replace those
commits with an equivalence claim. Canonical codex-web default also now equals
deployed `8b60554b`; no foreign worktree, records, team or refs were modified.

## Five owning lanes

| Original commit | Final commit | Purpose |
| --- | --- | --- |
| `1cbb47cd` | `8931ad6e2e5985c7cd025a4308e6ae22b882b9e0` | Consistent settings switches |
| `b93dac11` | `44b440083f927ee7aa2e69c30526575aa26c01b4` | Visible-content unread, cache references and paging fixtures |
| `6c9de003` | `49bc91a478a581b4c4f1378dd06cfdd6114c342b` | Ordered immutable composer and preserved transient retry integration |
| `be43c868` | `e36da70a0c7a977bd1695f50b1b35f8a88d8059f` | Quiet healthy queue refresh and contract fixture |
| `9293e314` | `24e66096ae65a97b1e2d14b68a566f44519a8c2d` | Reconciled recovery guide, lead writing pass |

There are no obsolete fixups, repeated dependency updates or unapplied migration
rewrites in this range. The SQLite schema1/policy1 migration and archive policy3
are already supported deployed boundaries inherited from `9634151b`; they are
retained, not consolidated away. No migration is added or rewritten by the five
UI commits. The codex-web migration/source range and storage guide are preserved
in `codex-web-deployed.*` alongside original runtime/upstream ranges and bundle.

## Substantive integration and preservation

The app integration requires affected final review; it is not a mechanical or
certified equivalent rebase. The receipt codec retains `retryable` together with
failed-head recovery. The existing pinned scheduler remains the only retry
scheduler, including its 250ms-to-5s backoff, hidden/offline/busy gates and restored
retryability. Buffered automatic retries use only the FIFO head. An ordinary
legacy transient may adopt the existing dispatcher only while empty and idle,
with its same ID/text/files/Send-Steer intent. The callback rechecks current
unsent+retryable proof; stale UNKNOWN/positive evidence or a newer capture wins.
Manual legacy reconciliation/copy behavior remains separate and unchanged.

Plan context stays on `implementPlan`, with its saved plan identity and mutual
exclusion. Ordinary drafts can be captured while that request runs, then drain
after it settles. Plan status reads do not become an ordinary message-busy hold.
Positive delivery evidence still wins over later errors. Original copy lineage,
proof retention, fresh validation failure/new-ID recovery and current-draft
ownership remain intact. No labels or other app-facing prose changed in the
refresh; the guide has the lead's approved main writing pass.

`preserved-baseline-blobs.json` proves 576 of the 592 baseline paths retain exact
blob and mode identities. The other 16 baseline paths are UI code, templates,
style, guide or tests; three new test files bring the final total to595. The
full 19-path feature diff is `final.diff.patch` / `final.diff.stat.txt`.
All non-UI performance, retention, provider, accepted-fork and plan/backend
lifetimes remain byte-identical to the deployed preservation base, including
`libexec/workspace-host`, archive recovery, source filtering, Go module files,
SQLite wiring and runtime contract. `final-input-graph.lock` and
`final-flake-metadata.json` retain the entire unchanged dependency graph:
codex-web8b60554b and runtime-owned llm-agents e85b9921. Full runtime contract is
in `final.json`; submissionStoreSchema/policy remain1/1 and archiveRecoveryPolicy3.

## Evidence and quick checks

- `adaptation.patch` is the exact nine-path post-rebase integration, SHA256
  `af03c34eeb3d10b5c9c0f89dc41b57ba7f5516492576e7b81545f155fe13a7b0`.
- Tested pre-fold tree equals final tree. Mechanical-head-to-final diff equals
  that saved patch, including registration order after autosquash conflicts.
- `original-to-final.range-diff.txt`, `mechanical-to-final.range-diff.txt`,
  complete series and old/new mapping are retained. Original9293 bundle and
  complete merged/deployed ranges remain available.
- Source/browser syntax, existing composer recovery and stale-feedback Node
  contracts pass. The new contract uses the actual pinned scheduler and covers
  FIFO/UNKNOWN holds, retryable reload, legacy admission/deferral, stale states,
  storage refusal/current capture, immutable files/drafts and plan context.
- `final-quick.log`: five focused Go tests pass, package1.464s: shipped API/Node
  aggregate, asset versions, admitted plan disconnect survival, preserved
  deadline/shutdown, and typed plan retry contract. The aggregate invokes the
  new pinned scheduler contract. Absent test-provider catalog was selected.
- Parent handler prerequisite passed separately with unchanged fixture
  `9ad87b42`, module `b74bdec9` and sum `dea36404`. It was not repeated here.
- The Chromium composer fixture adds an observable same-ID transient retry
  before a queued successor while retaining the newer draft/files. It is
  authored and syntax-checked; no real browser execution is claimed yet.
- Full base-to-head whitespace check passes. No declared hook framework or
  core.hooksPath exists; normal Git hooks were not bypassed. Nix and temporary
  commit-message files were used for commits and autosquash.

No long browser/native/package tests or builds were launched. Original green
evidence remains bound to its old source/environment; it is not transferred
wholesale to this changed composer integration. Suggested affected review lanes:
general, architecture/repetition, scope/proportionality, risk/compatibility.
Assess complete history, merged-source preservation, deployed SQLite contract,
retry/FIFO interaction and retained migration lineage. Lead owns the independent
review assignment and later watcher selection/publication.

## Consumer and deployment boundaries

No consumer worktree has been changed. After reviewed runtime publication,
configuration will refresh on fresh default and change only its runtime channel.
The latest lead disposition withdraws the old root-e85 re-pin: preserve merged
root llm-agents ea188/system Codex0.164, while the runtime independently retains
e85/workspace native0.163. Compatibility/build/native/startup/dry-run proof is
still required before activation; this packet claims no system-native equality.
Workspace consumer refresh remains with implementer0 after the new published
runtime is available. No claim, deployment or default integration is authorized
or performed by this package. Source/Git work pauses at this committed review
checkpoint; original artifacts and receipts remain retained.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/>
