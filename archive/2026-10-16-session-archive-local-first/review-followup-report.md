# Independent follow-up review

## Finding

### R5 — Important — Raw restoration can turn a regular Git symlink placeholder into a live symlink

General and risk/compatibility lanes. Runtime commit `e5ba4924`,
`libexec/workspace-archive-recovery.rb:276` (`raw_git_contents?`), `:228`
(`restore_git_contents!`) and `:319` (`restore_permissions`).

With Git's supported `core.symlinks=false` configuration, an index/tree entry
with mode `120000` can have a clean regular working file containing the link
target text. The capture predicate discards the Git mode and accepts that file
because its raw bytes match the blob. Its saved permissions correctly record
the filesystem kind as `file`.

The new raw restorer always creates a symlink for mode `120000`, however.
`restore_permissions` then sees the saved `file` kind and runs `File.chmod` on
that newly created symlink. This follows the link: an existing target outside
the checkout can have its permissions changed, while a dangling target makes
restoration fail immediately. Even when chmod succeeds, the final digest rejects
the changed entry type and ordinary retries repeat the mismatch. This is a
normal Git configuration and file-representation case, not a hostile local
operator scenario.

The smallest correction is to require the actual filesystem entry type to match
the Git tree type before selecting Git-backed recovery; otherwise retain the
existing full-copy fallback. Alternatively preserve the captured entry type in
raw reconstruction. Add a fixture with `core.symlinks=false`, a tracked symlink
represented as a regular file, and an external sentinel target. Assert restored
regular-file type, exact bytes/index and unchanged sentinel permissions. This
does not require a new persisted format or a general filesystem-hardening layer.

## Original findings

- **R1 resolved.** Verification now traverses only the retained tree, streams its
  commit/tree/blob contents through Git, and checks raw object hashes. Missing
  and corrupt blob cases before capture and before removal preserve the original
  checkout. It does not substitute a full-history fsck or per-file subprocesses.
- **R2 resolved for the reviewed interruption case.** Worktrees are created with
  `--no-checkout`; an owned incomplete retry reconstructs raw contents before
  permissions and saved administration/index state. Completed restore receipts
  still protect subsequent operator edits. The changed-smudge/partial-checkout
  regression proves exact bytes and index. R5 is a separate entry-type case
  introduced by raw reconstruction.
- **R3 resolved.** A monotonic attempt deadline propagates through lock waits and
  CommandRunner calls, with bounded termination and owned-index cleanup. Normal
  hooks remain enabled. The hanging-hook regression demonstrates pending status,
  released lifecycle locks, subsequent coalescing and preserved unrelated staged
  content. The ordinary creation/slug locks still reject contention immediately;
  the shared tracking lock waits only within the attempt budget.
- **R4 resolved.** A running worker clears an observer's premature finish time;
  a terminal unit replaces it with the authoritative exit timestamp. The test
  now persists/reloads the receipt and checks the final saved timestamp.

## Scope, evidence and lane conclusions

Same independent reviewer `/root/archive_final_review`, configured catalog
`gpt-6-astra` / `xhigh`, read-only except this report. The original report is
preserved. Reviewed the new packet, remediation record, current heads and state,
old-to-new diffs, final series, adjacent restoration/command/lock implementation,
new regression tests and documentation. Existing mandatory-review and all four
lane guidance from the original review remain applicable. No tests, deployments,
source edits or nested agents were launched by the reviewer.

The supplied isolated Ruby evidence reports **8 runs / 301 assertions**, passing
with global/system Git configuration disabled. The stored-worker-receipt Go
regression passes. Runtime and configuration diff checks were clean. All three
worktrees were clean at their packet heads. The additional fixture author
configuration appropriately removes dependence on the operator's global Git
identity. R5 is not covered by those tests.

- General: the original fixes are supported by focused regression evidence;
  R5 needs a narrow correction or explicit disposition before proceeding.
- Architecture/repetition: CommandRunner owns subprocess streaming and deadline
  propagation; ArchiveRecovery owns the finite Git object protocol and file
  representation. This is a clear interface and avoids per-file processes. The
  raw representation needs the type invariant identified in R5.
- Scope/proportionality: object validation is limited to the saved tree, reads
  bounded chunks, and delegates decoding to Git. Retry deadlines reuse existing
  command and locking boundaries. These changes are proportionate to the original
  findings. The documented retained-unit follow-up is accepted as an operational
  residual; no generic task framework or collector is required for this change.
- Risk/compatibility: missing/corrupt recovery and incomplete retry behavior are
  materially improved. Generation/ownership gates, legacy journals and completed
  restore protection remain intact. R5 concerns preservation of actual file type
  and unrelated permissions inside the promised recovery boundary.

## Final series, pins and format conclusion

| Repository | Reviewed base | Reviewed head | Ordered feature series |
| --- | --- | --- | --- |
| dev-workspace | `2b22de8d273a3b75e6cdd62c398fdb2630871d5a` | `73bc5c6e9a74f7bc667ea8f6f19ec3ad6d4b73ea` | `1b2a0e7e`, `3c57e2ea`, `e5ba4924`, `73bc5c6e` |
| workspace | `5a9cb6b6f431f930d88fc0d8aa7b9c9cca652b4f` | `5a7efca3f21924cc439567a6d725348d3b2b4dd3` | `078e8c88`, `87e22508`, `5a7efca3` |
| configuration | `ae98e9dbf05cd3f6b2d0c32255a4cb2d58c3865b` | `6c39b064661d5ccec5a229acb4f59ceafd97d10c` | `8f9b857d`, `81ab9fad`, `3db63e7e`, `6c39b064` |

Whole-branch history remains coherent. Remediations are folded into the two
owning runtime commits; no obsolete unmerged approach or separate fixup remains.
Each consumer runtime-pin stream still has one final update, selecting
`73bc5c6e` with matching content hash. The extension and codex-web selections
remain unchanged. No redundant repeated update stream remains.

Configuration `3db63e7e` preserves the other initiative's DeepSeek correction:
its configuration, operations guide and skill contents match `9721c331`.
The superseded runtime-pin commit `107255f8` was not copied. The distinct system
llm-agents input update remains legitimate. Previously deployed Codex baseline
behavior and original rollout/source provenance remain preserved.

**No database migrations and no new persisted format changes in this follow-up.**
The original inventory/record/journal/receipt lineage and compatibility conclusions
stand. The originally supported predecessors remain readable; incompatible old
packages remain fenced. These corrections do not introduce an intermediate
schema or a migration for an abandoned branch iteration.

Conclusion: original R1–R4 are closed; **R5 remains Important**. Its suggested
capture predicate/full-copy fallback is a narrow correction within the reviewed
design and can be directly verified by the lead under mandatory-review step 9.
After disposition, proceed with long package, scale and real-systemd acceptance.
Deployment still requires the existing owner's reservation to be released and
matching system/profile activation; review supplies no merge authorization.
