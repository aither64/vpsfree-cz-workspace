# Shared incident escalation backend rework

User authorized a predefined per-type registry, initially only trusted VPS-wide
memory-pressure incidents (`oomd`), without arbitrary administrator-created
rules. Architect0 owns the final technical contract; lead owns final prose in
`mail-rework-copy.md`. No dependent schema/API edits before contract release.
Heavy builds, VM images and runtime scenarios remain held after disk cleanup.

## Preserved source and migration lineage

Pre-rework base: `ac10a62f1cb0fc890378ae83cdf18dd0e29f049a`.
Pre-rework head: `4d72e3e754fd47b598de1e54e05b3c5d26c62200`.
Pre-rework tree: `588e65a8a13e3da69483cbf4c44cdfac84694a9e`.
The complete three-commit head is retained at
`refs/review/2026-10-30-oomd-abuse-policy/vpsadmin-before-shared-incident-rework`.
Earlier review refs remain intact; `pre-shared-rework-range-diff.txt` retains the
previous reviewed/published range comparison. Fresh SSH verification confirmed
feature head `4d72e3e7` and master `ac10a62f1` before this rework.

Migration `20261030180000_add_vps_oom_policy` has never been merged, released,
deployed or consumed by an external persistent environment. This package used
only disposable local and hosted spec databases. No physical scenario or
development-cluster deployment booted feature code. Schema/migration rewrites
may therefore describe the final additive schema directly after the architect
releases the contract. Preserve established shared incident New/Create nil
receipts and independent ordinary-mail savepoints.

Implementer0 retains all vpsAdmin Git operations. Implementer1 owns disjoint
legacy WebUI edits after the common contract releases; no mixed staging or
concurrent index/hook mutations. Superseded feature iterations will be
consolidated after final quick checks, with exact ranges and migration evidence
provided for independent review before publication or long checks.

## Current CI diagnosis

Native failed run `41121263198` is exact pre-rework head. Retained artifacts in
`ci-41121263198-attempt1/` prove:

- Core: 1,459 examples, 2 failures, seed 10889. Both expect initial CPU quota 0
  in `cluster_resource_package_spec`, but observe 32.
- Full: 1,459 examples, 72 failures, seed 37763. Initial failures include a
  duplicate disk-resource allowance, old-time node status/evidence, leftover
  resource usages, resource packages, discovery and sessions.
- Both actual hosted helper logs report MariaDB 11.8.6,
  `innodb_snapshot_isolation=OFF`, `tx_isolation=REPEATABLE-READ`. The intentional
  isolated-helper compatibility setting reaches both modes and is retained.

Concrete feature fixture mechanism under investigation:
`vps_oom_concurrency_spec` is `:no_transaction` and calls
`build_standalone_vps_fixture`. That helper commits numeric allowances (CPU 32),
charged VPS/dataset uses and a shared seed NodeCurrentStatus with real current
time. Its existing ensure removes only the VPS/actions/incidents/history;
`with_current_context` also creates sessions without destroying them. In native
example order this example is index 1399 before core failures 1447/1448, and
index 226 before full migration failure 457 and status failure 583. This is a
test pollution hypothesis supported by source and order, pending controlled
negative/corrected slices.

A fresh catalog Luna/low watcher owns negative reproduction on unchanged
pre-rework source: three core examples and seven full examples selected in
their original relative order with `--order defined`. Preserve native
`ci-contamination-negative-{core,full}.{log,json,exit}` and watcher receipt.
Only the needed pinned API shell/gems restoration is authorized, measured
separately; no image/cache wholesale restoration or guest tests.

Controlled diagnosis is complete. On the unchanged source, three core examples
reproduced both CPU 0-to-32 failures, and seven full examples reproduced six
downstream failures (resource duplicate, status, resource use, discovery,
package and session). The only correction replaces the nontransactional
provisioning fixture with a minimal persisted VPS, removes its own sessions,
history and audit rows, and restores the prior mode. The same selected IDs and
relative order then passed core 3/0 and full 7/0, both exit 0, 28/44 seconds.
Positive native evidence is `ci-contamination-positive-{core,full}.{log,json,exit}`.
This establishes the concrete feature fixture cause and correction; final
hosted whole-suite acceptance is still required after final source publication.
The API cache restored for these quick checks occupies 103,661,568 bytes.
Owned diagnostic DB ports were verified closed; the watcher's generic remaining
MariaDB observation did not identify an owned live database and triggered no
foreign process action.

## Current released implementation

The full replacement contract/design and lead copy were read. Generic backend
source implementation now follows that released contract. `IncidentEscalation`
has an explicit registered-type ingestion boundary; trusted node protocol/hash
mapping stays in the node adapter. Registration alone does not enroll old manual
sources. `VpsIncidentPolicy` stores type-specific overrides/warnings; shared
VPS ownership, permission and completed-stop state remain separate. Batched SQL
counts/filtering use registry qualification and selected policy rows. Four mail
templates and selected-language labels replace the prior pair.

The core schema was regenerated in a fresh disposable core DB from exact base
schema plus `AddIncidentEscalation`, retaining version 20261030180000 and no
guards/transitional drafts (`shared-schema-dump.log`, exit 0). No external
persistent schema or service was touched. Renamed concurrency coverage first
passed 1/0. A five-file new policy/registry/summary/mail/API batch is currently
owned by a fresh Luna/low utility; its first result is pending. Source inputs
remain stable during the batch. Registry synthetic source coverage uses the
actual `ingest!` boundary and asserts queued action/template, not only counts.

Owner1 reports legacy source finished, full PHP 120/832 and focused 13/92,
with locale/lint/formatter checks. Exact paths/evidence are in
`legacy-incident-rework.md`; owner0 has not staged or committed that package.
Browser source and owning feature docs are being adapted independently. No
publication, image/VM/browser build or lifecycle action has occurred.

## Final bounded source checks

The corrected affected batch passed 48 examples with zero failures; the revised
migration passed 2 examples separately. The six-file adjacent batch passed 49
examples, zero failures/pending, seed 50834, native 258.779 seconds (shell 280),
exit 0. It covers actual ordinary-mail-disabled API Create, manual lookalike
rejection, qualified node and manual owner-epoch privacy, New/Send, unchanged
node event semantics, scheduler behavior and all-type ownership warning reset.
See `shared-{affected,migration}-specs.*` and `shared-adjacent-corrected.*`.

The first adjacent launch was invalid: a trailing `.` expanded the six intended
paths to the entire API tree, including migrations. It produced no native JSON.
After SIGINT requested shutdown but the reporter remained active, the exact
owned RSpec PID received TERM. The wrapper exited 143 after 677 seconds, both
owned PIDs exited, and disposable DB port 39699 was closed. Preserve
`shared-adjacent-specs.*` as invalid-launch evidence, not application failures.
The parent then ran the literal six file operands without an extra operand.
Future watcher briefs must preserve exact argv, including the absence of a
trailing working-directory operand; prose reconstruction is insufficient.

Actual site source bf32762126f21fb7fc825fac25b5b45d075a2681 passed 9 real backend
registry renders (specific/generic warning/stopped, EN/CS, generic EN fallback),
native 23.69 seconds/shell 44, exit 0. The tracking-only
`shared-site-render-spec.rb` installs the exact site templates into a disposable
DB and calls IncidentEscalationMail. See `shared-site-renders.*`. This is render
and queue preparation proof, not SMTP delivery or a physical VPS stop.

Full-mode API locale generation/health passed. Topic selection has 13 identical
full/core topics and 421 eligible staged files exactly once; the renamed API
resource spec belongs to the existing vps topic. CI selector unit checks passed
16 tests/55 assertions. Nix parse/format, browser Node syntax, migration spec
correspondence and scoped Ruby lint (26 files/no offenses) passed. Normal
formatter-only corrections preserve the runtime behavior tested above. Root
hook environment restoration was limited to 37,791,909 bytes. Normal commits,
consolidation and complete committed-history receipts remain pending here.
