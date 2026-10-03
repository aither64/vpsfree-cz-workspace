# Mandatory independent whole-branch review

Completed by reviewer0 (retained thread 01a1021a-42ed-7e62-9bc2-43fbd84c6a48),
review purpose, read_only, saved gpt-6.1-sol/xhigh. Identity/settings were checked
against the live same-session roster; no override, fallback or nested reviewer.
Overall risk High; all four required lanes were independently completed.
Reviewer validated dev-session current and trusted session binding before access.
This record consolidates the complete report sent to lead through team assignment.

Reviewed base `b66c929bb7c202ad31bd8994a691ade14c40ebf0`, first commit
`36b6b874096e0bbd344cc140d07c358ab6799c41`, final head
`f3f8688b7ffc517a9a24150bd1f3d4056fbd35b7`; final tree
`406b654f992c65815806615e86c7a84fe267451c` matched passing checks.
Merge base equaled the supplied base. Reviewer inspected both commits and their
messages/inventories, complete final diff, source, tests, documentation, evidence
and pinned confctl 7bee58a metadata/system-argument implementation. The packet
and actual diff were byte-identical (SHA256
cb821d4f384e0c2bebdfe29b48465bdc6daa02ddb9a6458e60ed78b2ea9332b7).
Reviewer performed no edits, tests/builds, hooks, commits or deployment.

## Findings and lead disposition

No Blocking or Important findings.

Advisory R1 (general/verification): the filesystem warning equality test at
`tests/prometheus/infra-monitoring-filesystem.yml:21,38` is vacuous. Its 20%-free
series uses `/boundary`, whereas the unchanged rule selects only `/`, `/run`
and `/nix/store`. The series is excluded before threshold comparison, so an empty
result does not prove the strict 20% boundary. Reviewer recommends a selected
mountpoint on a separate instance, with that instance selected in the assertion;
a companion 19% positive case makes the intent explicit. Production filesystem
expressions are unchanged and the critical identity/hold checks are meaningful.

Lead decision: correct this bounded fixture defect. Implementer owns the edit,
then lead will inspect it and run the known-warm focused config check. Fold the
fix into the first unpublished behavior commit and replay the CPU commit,
preserving exactly two commits. This changes no production behavior/design or
accepted boundary. Under mandatory-review steps 9–10, direct inspection and
focused verification suffice; no specialist-lane or full reviewer rerun is
required for this narrow test correction. Updated history/head evidence follows
in the remediation section once complete.

## Lane conclusions

- General: all accepted behavior is implemented. The exact terminal exception
  follows continuing email/Telegram and precedes both SMS siblings; warnings,
  fatal alerts, other jobs/classes, VM/physical hosts and missing type preserve
  routing. Production-route amtool covers positive and negative cases. Common,
  infra and lock files are byte-identical; nodes changes only four CPU rules.
  CPU fixtures cover policies, equality, holds, labels, OS restriction, cores
  and boot boundary. Docs agree and are discoverable. R1 is the only gap found.
- Architecture/repetition: typed machine metadata is the site-owned finite
  contract; no duplicated runtime registry. Defaults and three explicit VMs
  are appropriate. All four label constructors enforce precedence, including
  shared node/ZFS/IPMI labels and preserved type=node. Actual generation and
  both monitors are tested. Confctl preserves metadata for consumers; no pin
  update is needed. Tiny label appends do not justify a production abstraction.
- Scope/proportionality: uses existing blackhole and CPU policies, retains
  alert names and strict counterparts. No speculative routing framework,
  runtime classification, compatibility shim or general safety layer. Larger
  fixtures/docs are focused and proportionate. Retained /run exception and
  raw pgnd load-average policy are accepted choices.
- Risk/compatibility: no new credential exposure, authorization-boundary or
  destructive-action issue identified. Typed site labels win custom conflicts;
  existing metadata consumers receive defaults. Exporters/nodes need no update.
  Missing type and old alerter config retain SMS eligibility. Label and pgnd
  alert-identity transitions, pending resets, partial HA deduplication limits,
  alerter-first rollout and rollback are documented. Existing state remains
  readable; no coordinated vpsAdminOS fleet update is required.

## Explicit history and migration conclusions

Reviewer inspected the entire linear two-commit series. The first owns typed
classification, target labels and immediate SMS consumer with its checks/docs;
the second is an independent CPU policy change with its checks/docs. The split
has a causal rationale. Neither replaces the other's design. No obsolete
unmerged approaches, superseded thresholds, fixup/tidy history, transitional
compatibility paths or redundant input-update history remain. No consolidation
was required on the reviewed branch.

**No migrations.** No schema/migration/seed/persisted-format change exists, so
there is no migration version or provenance to reconcile. The series/alert
identity transition is an operational effect, not a data-format migration.
Session evidence reports no merge/release/deployment/external consumption;
reviewer inspected local refs but performed no live deployment-state audit.

## Remaining limits

The exact reviewed tree passed focused metadata/labels/routing/rules and adjacent
regressions. Hooks were reported passed and their configuration inspected, not
rerun by the reviewer. Full central configs still need planned post-review
builds. Direct-import fixtures substitute inventory lookup/inert receivers and
cannot cover every full-system receiving option or real transport secret.

Offline amtool proves receiver selection, not live delivery, daytime execution,
repeat timers or inhibition. These existing structures were inspected and
preserved. Mixed monitors may emit distinct identities and old unlabeled alerts
may still SMS; relabeling resets pending/rate windows and can resolve/refire.
The accepted /run exception does not make tmpfs exhaustion auto-expand.

The review gate permits central configuration builds after lead records the
R1 decision. Review alone supplies neither deployment nor integration approval.

## Narrow remediation verification

Lead directly inspected the R1 staged diff: only
`tests/prometheus/infra-monitoring-filesystem.yml` changed. The 20% and 19%
inputs use selected `/` on distinct instances, with an empty warning assertion
at equality and a positive five-minute assertion carrying full expected labels.
Existing critical mount/hold assertions remain. On staged tree
`8978bc46c53107705a7dc587c0f036ff6d88a219`, the known-warm focused
`infra-monitoring-config` check passed (exit 0, 5.636 seconds), recorded in
r1-check-result.json/log. No production, documentation, CPU fixture or dependency
changed. R1 is fixed; no reviewer rerun is required under steps 9–10. Implementer
is folding this into the first commit and replaying the unchanged CPU commit;
final exact-head/history verification remains before central builds.

Final history verification: e7b029165e3304e6f1ca4ec7e261d007ff4cab81 followed by
f725dd3f407b0e5b82c9f9c1ad7720bbc7b14b68, based on the same b66c929b. Checkout/index
are clean; final tree is the passing R1 tree 8978bc46c53107705a7dc587c0f036ff6d88a219.
Lead compared the complete series and final diff: only the specified filesystem
fixture changed relative to the reviewed tree. Range-diff shows the CPU commit
patch-identical and the first commit differing solely by R1. Exactly two logical
commits remain, with no obsolete history or migrations. Implementer explicitly
ran active hooks for both final rewritten commits and recorded r1-hooks.log.
The review gate is closed.
