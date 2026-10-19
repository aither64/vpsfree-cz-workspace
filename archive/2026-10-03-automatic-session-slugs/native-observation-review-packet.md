# Native observation fixture: related review

All application worktrees are clean. Provider head is
`4651d76447cdbd1fa742358baeef01f0ebcdf250`, base
`4c170393a96ed0a6ac2e43488d073f6fcab36132`. The related delta from local
`5f6c7e255c2bd18361107cf322be1ec3e3e91ea2` is
[native-observation-fixture.diff](native-observation-fixture.diff), confined to
the tagged fixture. Public source/policy remain byte-identical to reviewed
published d371a772. Changes are folded into the one owning, unmerged utility
unit; the preceding head is retained in an owned feature ref.

Owning Nix profile quick check passed `go test -mod=readonly -race
-tags=codex_integration ./codex -run '^TestEphemeralIntegration' -count=1 -json`:
11 top-level groups/90 tests and subtests, zero failures/skips, 2.759 seconds.
Full evidence is `/tmp/automatic-session-slugs-native-observation-quick.jsonl`.
Gofmt and whitespace checks passed. These pure groups exclude the actual native
entry. No new native result exists.

Retain independent reviewer0, saved gpt-6.1-sol/xhigh/read_only. Overall High
risk because this fixture is a release gate for model-action isolation and
persistence. Review the affected general, architecture, scope, and risk lanes
under mandatory-change-review. Carry forward the completed full-history review
and direct diagnostic remediation in fixed-file-review.md; do not rubber-stamp
new behavior. No application edits, tests, native execution, Git or deployment.

The requested feature and user choice remain model naming with file/network
action tools disabled and questions rejected immediately. Diagnostic logging is
a newly demonstrated native contract conflict. A user preference question is
pending; this change must not waive the existing persistence assertion or
change public helper/runtime/policy semantics.

The related fixture change provides bounded model-tool mismatch metadata and
SQLite marker-owner metadata without descriptions, parameters, arguments,
prompts, rows, configuration or credentials. It also replaces the blocked
default-transport HTTP probe with one owned, synchronous cancellable TCP dial,
and targets question cancellation at the actual current native async question.
Inspect bounds, callback ownership, negative controls, deadline effects,
attribution claims, and retention of the original pass/fail gates.

Accepted rationale and exact source evidence are in design.md's final section,
"Native contract diagnosis after the fixed-file run, 2026-10-04". The original
failed native evidence is native-fixed-file-observation.md and the retained
private log. Only35 main leaves entered; tools and later SQLite failed; no
isolation pass or packet-owner attribution exists. The public source remains
identical to reviewed provider d371a772, and runtime8acd7220, extension2e3733ad,
workspace725db671 are unchanged. Their exact bases/complete series and migration
provenance are in branch-inventory.md. Preserve consumed runtime4ef298b3 and
extension399c3302 ancestors; no incoming migrations.

Final pins, package/resources, native matrix, live model canary, profile switch
and default-branch integration remain pending. No merge approval exists.

Other exact bases/heads: runtime924c0ec2/8acd722029f3c1d0abd8c2801b734a554a4a2eef;
extension8f8d8ecf/2e3733ade1bac712f0b852d1960a681e5bca5076;
workspacea51fa51e/725db6717a82524776f1a687ae9ff96515168b79.
Complete full SHAs and base-to-head series are in branch-inventory.md. No
incoming DB, preparation, lifecycle or host-schema migration is introduced by
this delta. Prior consumed migration/history conclusions remain unchanged.

Return findings by severity with concrete source references and residual gaps
to the native lead. Explicitly distinguish permission for a diagnostic rerun
under unchanged assertions from release readiness; logging preference remains
pending. Perform the review yourself without nested agents.
