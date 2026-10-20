# Archive recovery repair review

## Finding

**AR-1 — Important — Candidate recovery cannot retry its own completed-sidecar interruption state.**

General and risk lanes; runtime commit
`efaae43fa402bee6b2e25d4f00f9c20931d6dfc8`,
`libexec/workspace-host:937–954`, with
`libexec/dev-session:7242–7251` and
`libexec/workspace-archive-cleanup.rb:396–413`.

The modern candidate path requires an existing ordinary archive journal.
The ordinary executor marks the sidecar complete, deletes that journal, then
revalidates and deletes the sidecar. An interruption after journal deletion,
including an error during the final revalidation, therefore leaves a valid
completed sidecar that this recovery command refuses before reaching its
verifier.

For the Git administration-name collision being repaired, retrying the selected
predecessor also fails: its absence proof still rejects the live replacement
administration directory. The remaining cleanup receipt blocks package
selection in `require_no_unfinished_lifecycle_operations!`. Thus a supported
candidate recovery can leave the operator unable to finish the receipt or select
the repaired package through the documented paths. This is an interruption
recovery defect, not a request to accept fresh or partly removed archives.

Extend the bounded candidate recovery to recognize a strictly verified modern
completed cleanup receipt when its ordinary journal is absent. Reuse the cleanup
owner's operation reconstruction and existing completed-retirement proof; retain
the source/profile/contract, tracking, inventory, root and session-lock checks.
The ordinary candidate executor should clear the receipt. Add a regression that
interrupts after journal deletion with a genuinely reused administration name,
then retries through candidate recovery and proves the live checkout and
selected profile unchanged. Reject an incomplete journal-less sidecar.

No Blocking findings. No additional Important or Advisory findings.
AR-1 must be fixed or explicitly dispositioned before proceeding under the
mandatory review workflow. Remediation observed in the working tree while
finishing this report is outside the committed scope below.

## Scope and identity

Reviewed by `/root/optional_questions_review`, the original independent
standalone reviewer, retained `gpt-6-astra` / `xhigh` settings. The packet records
the installed catalog selection as `ffaf9deb` and no retained session roster.
Risk is High because this change executes persistent lifecycle recovery across
selected and candidate package generations. All four lanes were covered:
general, architecture/repetition, scope/proportionality, and risk/compatibility.
No nested agents, tests, source edits, commits, lifecycle operations or
deployment were performed by this reviewer.

The review supplements the earlier optional-question UI reviews; it does not
reopen those accepted changes. I inspected the new runtime commit, surrounding
cleanup/retirement/host locking code, new tests, relevant documentation and the
complete actual branch series and pin diffs.

| Repository | Base | Reviewed head |
| --- | --- | --- |
| codex-web | `c064ce09cfcea8d8af6bf676635a53cd823f772c` | `641907fb3afa2977050fe61331f9a3411c091245` |
| dev-workspace | `ea3f9d36397e8c2c846bd456e51385d73a3a358a` | `efaae43fa402bee6b2e25d4f00f9c20931d6dfc8` |
| workspace | `f95413431bcff60fd087399a54aeba8a475837b6` | `2acfab45e3ff2810697334d0e448bb54da251093` |
| vpsfree-cz-configuration | `7ffa98a5761e001ed22b70fa24eecc21ff8c58ca` | `92dc134200a1b63bc99a2567c29073ab6a0c79df` |

HEADs, merge bases, complete series and initially clean project worktrees matched
the inventory when independently checked. Configuration `92dc1342` has exactly
the same tree as `f76a59b6`; its corrected commit message records the actual
`6ab3b48f` baseline and complete runtime changelog.

## Lane conclusions

- **General:** The positive replacement proof checks old checkout and
  registration absence, a different administration-directory identity,
  reciprocal pointers, matching Git registration and unchanged common
  repository. The new real-Git case checks dirty binary live-file preservation,
  HEAD, status, pointers and administration inode. The host tests exercise all
  accepted journal phases but mock verification and execution, so they did not
  expose AR-1.
- **Architecture:** Cleanup identity proof stays with `ArchiveCleanup`, lifecycle
  proof and retirement stay with `Runner`, and the host binds the explicit
  candidate to the selected generation. This extends the existing recovery
  boundary without creating a parallel retirement implementation. The composed
  workspace and configuration consume the same runtime and codex-web pins.
- **Scope:** The repair corresponds to the demonstrated administration-name
  reuse failure. Modern admission requires moved tracking, schema-3 cleanup and
  every checkout/container removal already recorded; ordinary phase ordering
  then excludes checkout removal and cluster release. The replacement path is
  inspected through read-only Git queries. No operation on the replacement
  checkout, its Git administration or runtime is introduced.
- **Risk:** Exact source build, runtime-contract equality, selected Codex,
  predecessor profile token and generation remain checked. The exclusive host
  transition lock spans verification and ordinary execution. The verifier holds
  the session creation and slug locks; the executor reacquires them and repeats
  the ordinary journal, inventory, tracking and retirement checks. Normal
  competing lifecycle and package writers remain excluded. The accepted journal
  schema/mode boundary and the legacy selected-executor path are preserved.
  The unresolved compatibility gap is the terminal interruption state in AR-1.

## Complete history and migration conclusion

The complete codex-web range has one feature commit. The runtime range has
`1afca4ab` for optional questions followed by `efaae43f` for the independent
archive repair. The latter's tests, documentation and bounded candidate entry
support that single repair and belong together.

Workspace and configuration each contain one final logical pin-update commit.
Their runtime locked revision and narHash match, and all codex-web locks select
`641907fb`; the runtime Go module selects its matching pseudo-version.
The workspace extension remains `767dfd587e346168e1443e65ccdb67ce748f3fe3`.
Repeated updates in each consumer stream have been consolidated; no superseded
pin commits, obsolete branch implementation or unnecessary compatibility
iteration remains in these ranges. No retained intermediate update requires
a release or consumer exception.

**No migrations.** These ranges add no database, journal, sidecar or other
persisted-format migration. There is therefore no merged, released, deployed or
externally consumed migration lineage to preserve.

## Verification limits and next step

The packet reports passing syntax checks, two new real-Git cases with 57
assertions and all 14 host recovery cases with 244 assertions. I inspected the
tests and did not rerun them, as assigned. Packaged validation and actual
recovery/deployment remain subsequent work. Documentation correctly explains
the replacement identity proof and removed-resource boundary, but should also
cover the completed-receipt candidate retry when AR-1 is resolved.

Next: reconcile AR-1, commit and run focused interruption/retry checks, then
review the affected recovery boundary if its design changes. Preserve the
earlier UI and whole-series conclusions for unchanged content.
