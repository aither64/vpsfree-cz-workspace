# Independent remediation review

## Findings

1. **Blocking — retrying the outer runner changes its own saved source fingerprint.**
   General and risk/compatibility lanes; operational source
   `5e267d26a3c99e94a616f0c2a0f29e2ef34eeab8`.
   `rollout.md:618` unconditionally calls `chmod(0600)` whenever a lock is
   acquired. The new fingerprint includes every source entry's `ctime`,
   including `app-server-daemon/daemon.lock` and
   `app-server-control/app-server-startup.lock` (`rollout.md:652`). If the job
   is interrupted after saving publication intent but before the first
   exchange, the next outer `run` reacquires those original-source locks before
   starting the selected-service hook. Even with unchanged file contents and
   permissions, `chmod` updates their `ctime`. The hook's comparison at
   `rollout.md:827` therefore raises `SourceChanged` and permanently sets
   `sourceChangedAfterIntent` for the script's own bookkeeping rather than an
   external write. This leaves the native service unavailable and requires
   manual reconciliation although the source data did not change.

   I reproduced the fingerprint change in a disposable directory using the
   exact reviewed `lock` and `source_fingerprint` function definitions: acquire
   the two locks, capture the fingerprint, release, reacquire, compare; the
   second fingerprint differs without any data write. Existing interrupted
   publication tests call `publish` directly and do not exercise this outer
   lock-reacquisition path. Make lock acquisition leave existing correct lock
   metadata unchanged, or deliberately exclude only the operation's own lock
   bookkeeping from source stability evidence. Add an outer-runner retry case
   interrupted after intent and before the first exchange, while retaining the
   real source-write refusal cases. This is a narrow fix; it needs focused
   verification rather than another observation architecture.

No additional Important or Advisory findings in the remediation. Deployment and
migration remain blocked by the finding above and the remaining release gates.

## Disposition of the original findings

- **Original 1, selected-service recovery: substantially corrected.**
  `recover_selected_native` checks selected candidate and pending native identity,
  then uses `systemctl start` before ordinary switch admission. It does not stop
  an already running service. The hook-entered journal permits recovery before
  publication intent; the outer fixture now checks startup before switch. This
  resolves the missing backend-start path itself. The new fingerprint issue
  above still prevents one required interrupted-publication retry.
- **Original 2, short-lived embedded writers: corrected within the accepted
  trusted-operator boundary.** Process detection includes native `codex exec`;
  recursive inotify observation spans inventory, copy and exchange, refuses
  modification/creation/removal and overflow, and permits only the operation's
  own root exchange. A saved metadata fingerprint re-establishes stability after
  observer loss. Data/WAL changes are observed; root SQLite SHM indexes are
  deliberately omitted as derived reader state. New fixtures include a writer
  that completes within the copy interval, a WAL write, unchanged WAL reads,
  original-source writes across interruption, and preservation of new stock
  writes after exchange. Publication does not silently overwrite changed
  originals or restart a copy after intent.
- **Original 3, VM fixture homes: corrected in committed runtime source.**
  Creation/archive provider configuration, tokens, database assertions and
  diagnostics now select the private fixture home. The fixture changes remain
  with the runtime behavior they validate. Their actual packaged VM reruns
  remain a release gate.

The codex-web asynchronous upload test fix is narrowly scoped and separately
committed. Its elapsed-time wait yields to the WebCrypto worker without changing
product behavior. The independent portal-login wording in configuration's
operations guide matches the selected private credential path.

## Architecture and proportionality

The one-time observation and recovery additions address demonstrated concurrent
write and interrupted-start failures. They remain installation-specific
operational source, with no installed migration framework, new public API or
shared provider abstraction. Inotify is appropriate for detecting ordinary
short-lived writers without trying to reimplement native process management;
overflow and changed-source failures remain explicit. The durable fingerprint
has a clear purpose across observer loss, subject to the bookkeeping defect
above. No broader hostile-local-filesystem defenses or speculative recovery
paths are required. The previous component-ownership and documentation-placement
conclusions remain valid.

## Final complete history, pins and migration lineage

This is the same independent reviewer, `/root/final_review`, using the retained
gpt-6.1-sol/xhigh settings and read-only review behavior. I reviewed the affected
general/risk concerns and the new observation/recovery design's architecture and
scope directly, without nested agents. Unchanged substantive code retains the
conclusions of [final-review.md](final-review.md).

| Repository | Base | Final reviewed head | Complete series |
| --- | --- | --- | --- |
| codex-web | `58300182763a01de7248ddf7c6cb9a4f0c6216cb` | `f6f4a187509b3bebfc81585c535be856eaab0d04` | `ba8dfdd2` compatibility; `f6f4a187` asynchronous test scheduling |
| dev-workspace | `d0e4318cb1872feb69f3109f032870c310f14bdf` | `7d1163585a51da684be0f5cdd500a64822165839` | One final home/native/pin/fixture commit |
| configuration | `7a254c88b0b54a32300a319b3e4ed32936d9b004` | `c92408739d53d0e5198710723d89d8189f0f4d99` | `d432863d` generated channel pin; `c9240873` private credential path and corresponding operations prose |
| workspace | `5e267d26a3c99e94a616f0c2a0f29e2ef34eeab8` | `277833e8f9d8a45a502afca02b5df527da9440f0` | One final composition pin commit |

I independently enumerated these complete base-to-head series and inspected the
final consumer diffs and changes from the previously reviewed trees. The supplied
operational source is the committed rollout at
`5e267d26a3c99e94a616f0c2a0f29e2ef34eeab8`. No superseded runtime, fixture,
configuration pin or workspace composition commits remain in the final feature
series. The separate browser-test fix has an independent purpose and is an
appropriate commit split. There is no obsolete unmerged design or follow-up
fixup history to retain in these ranges.

**Pin-consolidation conclusion:** repeated runtime/library update attempts were
consolidated. Each logical dependency/input update occurs once in each final
consumer series. Both runtime source and Go module now select codex-web
`f6f4a187509b3bebfc81585c535be856eaab0d04`; configuration and workspace select
runtime `7d1163585a51da684be0f5cdd500a64822165839`. llm-agents remains the frozen
`91ff550fe42d4dd51dcf8b6bad87a0134fe7f314`; the extension remains
`767dfd587e346168e1443e65ccdb67ce748f3fe3`. I checked those identities from the
committed locks. No intermediate pin requires a deployment/publication exception.

**Migration-lineage conclusion:** no new project-owned SQL migrations.
The previous upstream native schema-62 conclusion remains valid and unchanged.
The one-time partition still targets the exact existing native schemas rather
than an obsolete branch schema. It has not executed, merged, released, deployed
or gained an external consumer according to the supplied provenance; the older
reviewed script is not a supported migration predecessor. Preserving the latest
operational source does not require retaining the rejected behavior. Recovery
remains forward-only after package selection and must preserve both original
homes and any new stock writes; the finding above concerns implementing that
promised resume path, not its lineage.

## Verification evidence and remaining gates

The working rollout matches its committed blob. I recomputed the six fenced
source checksums and byte equality with the raw inventory/partition/cutover/
acceptance/test/schema files; all match. The packet reports fifteen synthetic
fixtures passing in 8.4 seconds, exact pin/composition checks, a fresh runtime
vendor hash `sha256-2aYEuOcFTjdecQu/GEP2i2sLlYi5eMnDxpKb2nyU7Mw=`, and final
codex-web CI `40852873773` passing. I did not rerun those batches. I ran only the
small disposable lock/fingerprint reproducer described above; no live native
state or service was touched.

After the narrow retry fix, retain the original release gates: exact native
saved-state upgrade/resume/fork and naming/lifecycle checks, packaged VM checks,
outer-hook failure/resume verification, final committed system/application
builds, current inventory/capacity admission, claimed deployment, partition
conservation, all portal thread reads, stock/portal isolation, the two reported
activity endpoints, browser/tmux/provider/team acceptance and the same-attempt
message reconciliation/retry. Those operational checks have not been executed
by this reviewer. This report grants no master integration, forced interruption,
reboot or backup deletion.
