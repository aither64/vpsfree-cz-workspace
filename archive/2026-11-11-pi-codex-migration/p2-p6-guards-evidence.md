# P2/P6 retained workflow guards

Status: source, focused checks, clean committed-parent assurance and lead writing
pass committed; exclusive index and document freeze released. Source package
acceptance pending lead assessment. This is one source guard
package, not producer publication, writer activation or installed readiness.

Owner: implementer3, retained Sol/xhigh/workspace_write, exact bound session
`2026-11-11-pi-codex-migration` in `/home/aither/workspace/ai/vpsfree.cz`.
Session/current and both absent DEV_SESSION environment values were verified.
Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace`.
Checked committed base: `6b64c7447674340db63b96c1c07cbc2b13878748`, plus owned
source and concurrent disjoint peer source. Final committed range:
`6b64c7447674340db63b96c1c07cbc2b13878748..3318ca32392444167c4369ecd8cd17891bdaa4ce`.

The complete source brief is design.md, “P2/P6-GUARDS: sufficient retained
workflow compatibility source package”. Lead released exact ownership after
accepting the prior P5 helper. Central Go/templates/app.js, existing P3 code,
runtime-contract.json and Nix remain with their owners and are not edited here.

## Source boundary

Checked pre-writing 17-path manifest: `p2-p6-guards-checked-source-sha256.txt`, SHA256
`f8998167b08388da56e2b42250f977e73252eb413f146fc66cd5ff1f48051fb3`.

```text
portal/internal/session/pi_workflow_contract.go
portal/internal/session/pi_workflow_contract_test.go
portal/internal/piquestions/retention.go
portal/internal/piquestions/retention_test.go
portal/internal/piplan/retention.go
portal/internal/piplan/retention_test.go
portal/internal/piruntime/retained_conversation_inspection.go
portal/internal/piruntime/retained_conversation_inspection_test.go
portal/cmd/workspace-portal/pi_workflow_preflight.go
portal/cmd/workspace-portal/pi_workflow_preflight_test.go
portal/cmd/workspace-portal/pi_team_preflight.go
libexec/workspace-session-backends.rb
libexec/workspace-host
test/workspace_session_backends_test.rb
test/workspace_host/provider_sessions_test.rb
test/support/pi_team_preflight_driver.rb
docs/pi-questions.md
```

- Owning `session.DecodePiWorkflowContract` reads the entire <=64KiB runtime
  metadata object with existing strict duplicate/encoding/object handling, then
  selects exactly piQuestionsSchema1, piPlanSchema1, piToolPolicy{policy1,
  conversationSchema2}, hostCallbacks1, linearLineage1, workflowObservations1.
  All are exact integers; missing/null/partial/unknown nested fields refuse.
  Unrelated top-level fields remain permitted. Embedded initialization is not
  changed and optional support is never defaulted.
- New piquestions/piplan `DecodeRetainedRecord` wrappers call the owning decoder,
  ValidateRef and full private semantic validator. They return complete detached
  present records, including empty collections, old/closed evidence and every
  response/acceptance phase. No live validator, policy, StateFile.Read lock,
  Snapshot or lossy view is used.
- New P3 `InspectRetainedConversations` uses only owning readPrivate,
  validateConversationRecord, stateDirectory and exact handle/root checks, with
  private owned directories/files and all member mappings. It explicitly admits
  schemas1/2 and refuses3 even if the shared native codec understands3. It retains
  literal UUID-or64hex creation refs; the production schema4 proof still requires
  its own exact64hex receipt. No Manager, native call, history parse, lock,
  mkdir/write, repair or cleanup is introduced.
- Existing pi-team-preflight argv and schema1 `{required,sessions}` output are
  unchanged. P6 discovery validates exact owning StateFile.Path and registered
  workspace, including all private ancestor directories and full records. Only
  exact bounded empty owned questions.json.lock/plans.json.lock artifacts are
  recognized. Unknown/temp/symlink/unreadable/disappearing/orphan files refuse.
  Whole-namespace absence is ordinary absence; present-empty files emit claims.
- Source kinds questions/plans/tool_policy extend the existing claim shape.
  P6 source IDs hash the exact validated namespace-relative pathname. Schema2
  mappings emit member constraints (including lead) with original creation ref;
  schema1 mappings validate and count without a new workflow obligation. CLI
  output contains no question/answer/plan/tool/history/input content. Existing
  contradictory identity detection and equal-claim merge are reused.
- Combined <=65536 record budget includes P6, all retained mapping schemas and
  existing utility receipts. Roots stay unique <=1024, traversal bounded, stdout
  <=4MiB and diagnostics <=4096 bytes. Host existing joined30s child handling,
  executing-package-only helper and transition exclusion remain intact.
- Ruby accepts those exact workflow claims through the same complete original
  ready schema4 journal/request/completion cross-proof after binding/cache
  retirement. Structural retention of a nonlead tuple does not fabricate native
  readiness. A target needs the whole six-field workflow bundle independently of
  existing base/team maps. Empty-registry checks include both P6 namespaces.
  Candidate code is never executed to determine compatibility.

## Checks and source applicability

All commands used cached exact D shell
`/nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv`, explicit Go
`-mod=readonly`, disposable state and existing fixtures. No current-flake lock
evaluation, native/model/auth call, profile activation or live lifecycle action.

| Check | Result / log |
| --- | --- |
| Whole-metadata decoder initial/final edges | Passed0.021s, final0.037s; `p2-p6-guards-exports.log`, `p2-p6-guards-final-edge.log`. |
| Full retained P6 wrappers, all phases/empty/closed | Questions0.102s/Plan0.102s; `p2-p6-guards-exports-fixed.log`. |
| P3 retained inventory, cold/held/pending/loaded + final malformed/private/bound/UUID cases | Passed0.423s, final0.668s; same exports/final-edge logs. |
| New scanner path/private/artifact/count/schema/empty/ref claims | Passed0.155s; `p2-p6-guards-scanner.log`. |
| Existing ordinary team/utility join regressions | Passed0.144s; `p2-p6-guards-team-regressions.log`. |
| Owning Ruby metadata/fence readers | New cases3/102, full affected file8/224, no failures/errors/skips; `p2-p6-guards-ruby-codec.log`, `p2-p6-guards-ruby-full.log`. |
| Each new source kind + target metadata refusal |1/69, no failures/errors/skips; `p2-p6-guards-host-target.log`. |
| Existing executing helper/argv/error/output/timeout/missing-helper and old team fence |2/25, no failures/errors/skips; `p2-p6-guards-transport.log`. |
| Actual Go test-process scanner -> Ruby host |1/22, no failures/errors/skips, command~4.2s; `p2-p6-guards-crosslanguage.log`. |
| Built actual CLI + current Ruby host | Build0, current1/22, no failures/errors/skips; `p2-p6-guards-actual-build.log`, `p2-p6-guards-actual-current.log`. |
| Actual complete pre-Pi predecessor entry points |1/27, no failures/errors/skips; `p2-p6-guards-actual-predecessor.log`. |

Initial wrapper tests incorrectly attempted a lowercase Backend key substitution
against the actual exported uppercase field, and the initial retained fixture
used Go TempDir's nonprivate mode. These fixtures exposed their own setup errors;
tests were corrected to actual key spelling/private mode without relaxing
production checks. Initial failure is retained in p2-p6-guards-exports.log.
Only affected cases were repeated; successful unchanged checks were reused.

The actual scanner/build/predecessor batch used the original17-path manifest
`p2-p6-guards-source-sha256.txt`, SHA256
`b0ca7b481e52b35ebf45506c5997aee56647ea9f0f441868a78a6ec006474444`.
Only two test files changed afterward: session metadata nested value cases and
P3 retained private/size/duplicate/null/UUID cases. Their final focused checks
passed; implementation and driver bytes stayed unchanged. No unchanged broad
six-package/Node campaign was run.

Fresh watcher policy was resolved from installed
`/nix/store/a0nhkz2khja7qp17vw5fh1p8327i10iw-dev-workspace-0.2.0`, validated
catalog `f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`:
verification_watcher GPT-6 Luna/low, full_access, matching native utility
danger-full-access/never. Separate fresh operation identities ran the uncertain
cross-language test and actual CLI/predecessor batch. Full logs are
`p2-p6-guards-crosslanguage.log` and `p2-p6-guards-actual-watcher.log`; both are
terminal, with no remaining tool sessions or effects. A final fresh watcher
also checked an isolated git archive of committed parent
`6b64c7447674340db63b96c1c07cbc2b13878748` plus only the final17 assigned files,
at `/tmp/p2-p6-guards-committed-hkx4i8v5`. All five owning Go package families
passed, without any uncommitted P3/central/UI dependency. Snapshot/input receipt:
`p2-p6-guards-committed-snapshot.json`; log:
`p2-p6-guards-committed-check.log`. This resolves source build/applicability on
the committed baseline rather than inferring equivalence from dirty peer code.
That watcher is terminal too. Ruby syntax, owned Go formatting and whitespace
checks passed; no unrelated source was reformatted.

## Actual predecessor and producer boundary

The full original pre-Pi D base is
`6587c4c1cedabee95bcc52f4667e7d33e3a82859`, retained complete archive
`/tmp/p2team-predecessor-oq1e4wcl`. Every739 tracked blob was reverified against
that exact Git revision before execution; receipt `p2-p6-guards-predecessor.json`.
The existing driver was extended with actual-shaped empty questions/plans and a
cold held policy2 mapping, all bound to one consistent original full schema4
ready tuple. Cache/binding are removed, original journal/request/completion remain.
Its real predecessor prepare_profile rejects both stable and --from-candidate
paths through that recognized journal; all retained bytes remain unchanged, no
scanner/profile/quiesce/configure/native effect occurs. No fabricated missing
fields or new legacy parser/harness stand in for that old source path.

Current driver writes complete WORKFLOW_FIELDS into synthetic target
share/workspace-portal/runtime-contract.json; actual scanner/host accepts it and
rejects each missing field. The owning Go whole-metadata decoder verifies the
same complete selection. Architect0 confirmed this producer fixture sufficient
for the source checkpoint. Real runtime-contract.json is untouched. Owner0 must
later verify actual published metadata and verbatim installed copy against the
owning consumers; synthetic proof does not establish installation/readiness.

## Documentation, history and remaining work

Only the append-only “Retained workflow compatibility” subsection of
docs/pi-questions.md belongs here. It preserves scope/retention/rollback and the
complete bundle rather than operational rollout instructions. First technical
append window was explicitly released to owner2 after checkpoint; his central
appendix is separate. Lead main writing pass closed on this subsection only:
plain wording preserves bounds, source/fence/rollback/schema3 meaning and makes
clear that metadata declares support rather than certifying actual enforcement.
All new guard errors were read and accepted unchanged. Only documentation bytes
changed after the clean-parent check; all16 code/test hashes remain identical.
Final document SHA256:
`fcd23e8c63886c993fcc3c7f7ab41deb9e9a09d49f01f57a0a6f6ffe41c2f75d`.
Final post-writing17-path manifest `p2-p6-guards-final-source-sha256.txt` SHA256:
`40193f71d102c5a2a2476786acd6203f87b727c28d12a8fd3c2a49698c9fd714`.
The complete owned source diff is1113 additions/6 deletions. Exact owned
whitespace check passed; no unchanged behavioral check was repeated for prose.
Session evidence owns temporary source/check/parent/status details.

No state-schema conversion, record/receipt migration, normalization, deletion,
retirement, default switch or alternate ledger is added. Retained records/fences
continue to block incompatible rollback. Native-routing schema3 is refused until
its actual owning reader and separately released export/scanner/target guard
exist. Central routes/admission/refresh, native functionality and installed
containment remain separate required proofs. No metadata, registration, writer
activation, profile/deployment, push or merge is authorized or performed.

## Final commit and ownership receipt

Commit: `3318ca32392444167c4369ecd8cd17891bdaa4ce`.
Parent: `6b64c7447674340db63b96c1c07cbc2b13878748`.
Subject: `pi: guard retained question plan and tool-policy records`.
Exactly17 owned paths/1113 additions/6 deletions were staged and committed.
Every staged, committed and current owned file SHA256 matched final manifest
`40193f71d102c5a2a2476786acd6203f87b727c28d12a8fd3c2a49698c9fd714`.
The entire document retained final main-pass SHA256fcd23e8c through commit.

Fresh session/current, environment, own saved roster, exact parent and empty
index were verified before staging. Normal tempfile `git commit -F` with
`--only` exact paths was used. No declared hook framework or active executable
hook was present; no bypass was used. Owned17 paths were clean and the post-index
empty after the completed commit; all unrelated peers remained excluded. No
behavioral/prose rerun, partial push, merge, activation or lifecycle action ran.

Index window released immediately through report_to_lead message
`46b10268-8780-4411-8d50-1196d0583716`; raw receipt:
`p2-p6-guards-commit-receipt.json`. The whole docs/pi-questions.md freeze was
explicitly released to implementer2 in same-session message
`4a06e0fb-d7a4-4514-8680-81d300f63bda`, with the committed owning decoder/export
handoff. All own commands/watchers are terminal and no claim is held.

Package reported for lead source acceptance. H0/P5/guards fixes remain retained,
capacity available after acceptance; no next package is queued. P7 producer,
central/native3 and installed-flow proofs remain separate required work.
Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
