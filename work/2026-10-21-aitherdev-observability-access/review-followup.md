# Focused independent final-review follow-up

No new findings: no Blocking, Important or Advisory issues in the reviewed
correction. The committed change is acceptable for the planned full VM and
affected-host build verification. Full VM success and deployment readiness are
not established by this review.

## Reviewed scope and identity

- Repository: `vpsfree-cz-configuration`, worktree under this session.
- Base: `38e7c837893695999e588a73f5d2a0088b8257b1`.
- Frozen head: `d07b4251172020472b21e8830e92b023849d543f`.
- Immediate preceding tested head: `5d910028d32ce9305dc8161c51b3ed17ec4179bb`.
- Prior full review: [review.md](review.md), at
  `072f7e01f5000bfd43439c5ba27aee28cfe69b17`.
- Reviewer: retained independent `reviewer0`, `gpt-6.1-sol` / `xhigh`, saved
  `read_only` access. Same-session roster and thread identity verified, no overrides
  or fallback. No nested agents.
- Lanes reassessed: General; Risk and compatibility. Prior Architecture and
  repetition, and Scope and proportionality conclusions remain applicable.

`dev-session current` printed the exact bound session slug from the session CWD,
both identity environment variables were absent, and the check was repeated before
writing this report. Git HEAD matched the frozen revision and the project worktree
and index were clean. `ready.diff` exactly matched the actual complete base-to-head
diff (1,694 lines); `logger-permission-fix.diff` exactly matched the actual delta
from the preceding tested head (four files, +35/-7).

Read the follow-up packet, diagnosis, updated design clarification, complete
series/final diff and delta/range-diff. Inspected the affected production action,
quick/VM fixtures, operations guide, native probe programs and recorded outcomes,
plus the failed VM evidence. Reused applicable unchanged workspace/repository
guidance and the mandatory-change-review workflow; reread its affected lane
references. This is a targeted follow-up under the skill's affected-lane policy,
not a blanket rerun of the unchanged components.

## General assessment

The failure was substantive: `runtime-verification-01.log:2310` and the following
metadata show the reconciled parent as `root:log-readers 0750`, but newly created
descendants as `root:root 0700` and the current file as `root:root 0640`. The SSH
read predicate then failed. Legacy configuration globals had not supplied the
remote RainerScript action's group/directory creation policy. The earlier review
did not catch that distinction; its creation-policy assessment is superseded by
this correction and the behavioral evidence.

The correction at
`cluster/cz.vpsfree/containers/prg/int.log/config.nix:109` places all six native
properties on the owning remote `omfile` action: root owner, `log-readers` group,
file mode `0640`, directory mode `0750`. It keeps the dynamic filename, inputs,
remote-pipe call, local selectors and umask intact. It implements the accepted
policy directly without adding another operational mechanism.

The actual-group probes are materially stronger than substituting root for the
reader group. I inspected `logger-omfile-permission-probe.py` and the outputs in
`logger-permission-probe-01.log` and `logger-permission-probe-02.log`. Their explicit
action matches the committed properties; they change only disposable paths,
ports and the test group name. The programs do not repair the created remote
metadata after rsyslog writes it. Their results distinguish the previous incorrect
GID/modes from UID 0/GID 100 directories `0750` and files `0640`. The second probe
retains a separate exporter GID 200 and confirms local/remote/exporter markers.

`tests/log-reader-access.nix:90` now asserts the six action properties. The
root-group substitutions at line 57 remain limited to the syntax rendering and
must not be counted as proof of reader-group behavior. The native probes provide
that focused evidence, while the production-derived VM remains the final runtime
acceptance check.

The VM at `tests/log-reader-vm.py:75` first requires the new subtree to be absent,
then checks the actual positive SSH read, every new ancestor's group/mode, the
current file, the separate pipe group and local messages metadata. Existing
rotation, post-HUP ingestion, protected-write denials and SSH restrictions remain
asserted. No permission bypass or wider timeout was added to make the test pass.

Original A1 is resolved: the two historical reads are separately checked at
`tests/log-reader-vm.py:68` and `:69`. Earlier fixture corrections use the actual
RFC5424 sender format, stop socket activation during reconciliation, keep the
synthetic FIFO consumer available, and produce bounded failure diagnostics. The
proxy fixture's h2c setup and native missing-file status correction retain the
authentication/no-upstream assertions. Those changes do not alter production
proxy policy or weaken the reviewed access boundary.

The operations clarification at `docs/operations/log-reader-access.md:22`
accurately distinguishes action-specific remote creation, legacy local selectors,
and existing metadata. Its historical reconciliation and recovery instructions
remain necessary and discoverable. No documentation finding remains.

## Risk and compatibility assessment

The explicit properties grant only the intended group read/traverse permissions;
they retain root ownership and deny group/other writes. They are scoped to the
remote file action. Local messages retain their existing legacy creation policy,
and the exporter pipe uses its separately managed group/mode. The distinct-GID
probe specifically supports that separation. Logrotate create settings,
retention, paths, HUP behavior, account/key restrictions and the metadata helper
are unchanged by the correction.

`logger-existing-metadata-probe.py` and its recorded output show existing remote
directories UID 0/GID 0/mode `0700` and a file mode `0600` remain unchanged while
rsyslog appends the marker. Creation properties therefore do not replace the
operator's reviewed reconciliation procedure or unexpectedly rewrite historical
access. Actual required existing readers and ACLs still need inspection before
rollout.

There is no wire/log-format, public API, account interface or persisted schema
change in this fix. Components can still deploy independently; no fleet-wide
coordinated update is introduced. Rolling software back does not restore
historical group/mode metadata. Inventory-based recovery and explicit revocation
remain the supported boundary; root-key removal remains the user's separate
action. No additional compatibility path or migration is warranted.

Architecture/scope reuse is justified: the same native rsyslog action owns
creation and the same legacy selectors own local logging. The two declarations
are required by those distinct native configuration contexts, not competing
policy engines. No provider/consumer interface, generalized framework or new
component has appeared.

## Updated complete history and migration conclusion

The full base-to-head series contains exactly two logical commits:

1. `bd54b28c63770b782a4af435ad8dfb9619b6032c`:
   `int.log: add unprivileged SSH log reader`.
2. `d07b4251172020472b21e8830e92b023849d543f`:
   `proxy: add dedicated Prometheus query access`.

The logger correction and related tests/docs are folded into the owning logger
commit. The proxy commit is patch-identical to its immediate predecessor in the
supplied range-diff. The original logger/proxy split and shared registration
ordering remain coherent. Earlier test-only corrections are also folded into
their owning commits and introduce no superseded design.

No obsolete unmerged approach, fixup stream, transitional shim or superseded
creation policy remains in the final series. Earlier frozen revisions stay in
session evidence as verification provenance, not extra commits required in the
feature history. The packet records no merged, released, deployed, published or
externally consumed intermediate branch version; no retained compatibility
boundary requires an intermediate commit.

There are no repeated dependency/channel/input/generated-artifact update streams
and no dependency or lockfile changes. There is nothing to consolidate in those
categories.

**No migrations.** No database/TSDB/log-format migration or transitional schema
lineage exists in the complete branch. There are no migration versions requiring
merge/release/deployment/external-use provenance. The already reviewed optional
metadata reconciliation remains an explicit operator operation, not an automatic
activation migration.

## Verification limits and next action

The packet records successful final-head quick Nix policy/rsyslog/logrotate checks,
AST/format/whitespace checks and required hooks. I inspected the behavioral probe
programs/outcomes and the actual failed VM evidence rather than treating a planned
rerun as validation. No tests, probes, builds, network requests, deployments,
provisioning or Git mutations were launched during this follow-up. Only this
report was written.

The full VM has not passed on `d07b4251`; the preceding VM failed for the now
corrected metadata cause. The recorded combined verification result remains
failed, and both affected-host builds were skipped after that failure. Run fresh
watcher-owned full VM verification and the required logger/proxy host builds after
this review. Preserve any earlier reusable proxy result only under its exact
derivation/input evidence; this report does not certify such reuse.

Production metadata/ACL/readers, credentials and their permissions, public TLS,
live ingestion/exporter behavior and ordinary rotation remain separately
authorized deployment acceptance work. The unredacted data access, ordinary-shell
behavior, API quota/CPU limitations and revocation limits in the prior report
remain accepted residual boundaries. No merge, provisioning, deployment or session
lifecycle action is authorized by this review.

Session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-21-aitherdev-observability-access/>.
