# Affected-lane review: interrupted integration removal

## Findings

1. **Important — risk/compatibility, general: the direct deletion fallback
   bypasses an explicit Git worktree lock.**

   Location: `dev-workspace/libexec/workspace-coordination-gc.rb:425–428`
   and `:568–575`, commit `6ff8560785a33c83310bacba9f50919a855b66cf`.

   After an interruption removes `.git` but leaves the scratch directory,
   an operator can hold its retained registration with `git worktree lock`
   while inspecting recovery. The pending-intent check accepts the record
   because its HEAD remains detached and unchanged; it ignores the `locked`
   field. `FileUtils.remove_entry` then deletes the directory and its remaining
   contents. Only afterward does the native `git worktree remove --force`
   refuse the locked registration. Normal Git removal requires a second
   `--force` to override that hold, which the collector does not otherwise use.

   I reproduced this in the existing disposable fixture, using the repository's
   Nix shell. Before the first attempt I added an ignored `retained-cache` file.
   The injected interruption removed the tracked `base` and `.git` files, after
   which I ran `git worktree lock --reason 'inspect interrupted removal' PATH`.
   The next collection deleted the directory and then raised:

   ```text
   fatal: cannot remove a locked working tree, lock reason: inspect interrupted removal
   use 'remove -f -f' to override or unlock first
   ```

   The lock remained in the Git registration, but the held contents were gone.
   The diagnostic completed in 0.56 seconds: one test, seven assertions
   confirming this behavior. This is an ordinary explicit Git hold, not an
   attack by a hostile local operator.

   Smallest fix: reject a target record containing `locked` or `locked REASON`
   before direct filesystem deletion. Use the freshly read exact registration
   in `remove_worktree`, not only the earlier planning snapshot; planning should
   also report the preservation reason. Keep the pending intent and remaining
   contents, then allow ordinary retry after the operator unlocks it. Add a
   regression for the `.git`-missing pending path, demonstrating retained file
   contents while locked and successful cleanup after unlock. No new metadata
   format or broader deletion behavior is needed.

The original partial-removal finding is resolved at these revisions. The new
finding above must be fixed or explicitly accepted before long verification.
No other actionable finding was identified in these affected lanes.

## Reviewed changes and safety boundary

This review covers only general and risk/compatibility lanes, as requested.
The original report and its architecture/scope conclusions remain preserved in
`review.md`. Risk remains high. The same independent reviewer thread
`01a15329-cb74-7402-932a-efe55a1d4d93` is still configured as
`gpt-6-astra`/`xhigh`, verified from its current native turn context. No
application files were edited and no nested agents were launched.

I compared original runtime head `957dc29` with final `926c669` and inspected
the complete final histories and consumer diffs. The new pending-removal path
checks the saved path, owning workspace/repository, common Git directory,
detached registration and saved HEAD. Existing liveness, process, `.keep`,
integration/profile locks and busy-resource checks still precede removal.
Changed HEAD/branch or a surviving path without its registration is preserved.

The documented choice is an admitted removal intent: remaining contents are
already disposable and operators must not reuse the checkout while that intent
is pending. This is a supported alternative to rechecking pristine contents
after every interruption; it avoids mistaking the collector's own partial
deletion for new uncommitted work. The new direct primitive is otherwise bounded
to the exact registered pending checkout whose `.git` file disappeared. It
still needs to honor the explicit Git lock described above.

I independently exercised interruption after direct directory deletion but
before Git registration cleanup. The next sweep successfully removed the exact
registration and cleared the pending field. The same diagnostic included an
ignored symlink to an external fixture directory; its known file contents
survived. Result: one test, eleven assertions, zero failures, 0.72 seconds.
This confirms the fallback's retry boundary and ordinary symlink behavior;
it does not require protection against hostile filesystem manipulation.

## Final history and compatibility conclusions

| Repository | Base | Reviewed final head |
| --- | --- | --- |
| dev-workspace | `8385699aabcc2cfc74b585ca653a4658ff3eef75` | `926c669f148e05b881bc41bd432389d14998e411` |
| workspace | `92a9a8d3c88e91b81d7a752fc29d1b807ed9d02f` | `1fb8372c939777f5541a00de6ce0804ab6d41e3f` |
| vpsfree-cz-configuration | `95a8b88d383c177fc65bf67d51c901a69c0b2847` | `67616867156d4c541e13b67dddb26c885a0dc4a3` |

- **No obsolete unmerged history remains.** The recovery fix is folded into
  cleanup commit `6ff8560`. `git range-diff` confirms the separately reviewable
  profile-policy commit `926c669` is patch-equivalent to original `957dc29`.
  No intermediate fixup or superseded recovery scheme remains in the series.
- **No repeated dependency-update streams remain.** Workspace and configuration
  each have one final update selecting `926c669`, with identical runtime source
  hashes. Each lock changes only its intended runtime node; other inputs and
  the extension pin remain unchanged. The configuration message is generated
  directly for the final update.
- **No migrations.** The pending journal field retains its existing additive
  shape. No SQL, ledger, public API, module or protocol schema changes were
  introduced by the remediation. Per the packet, these feature versions have
  not been deployed or integrated. Earlier readers preserve the optional field;
  older collectors leave it for the new runtime. Removed disposable contents
  remain irrecoverable through software rollback.

All three worktrees were clean and their final diffs passed `git diff --check`.
The packet reports 33 focused tests/169 assertions and a passing composed
deployment contract. I inspected the new partial-removal, changed-identity,
replacement-data and `.keep` tests and ran the two additional focused diagnostics
above. Long packaged checks, real systemd interaction and native Nix-profile
verification remain pending. This report supplies no deployment, cleanup or
default-branch integration authorization.
