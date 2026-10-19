# Accepted local diagnostics and atomic test evidence: related review

Requested outcome remains automatic dated session slugs from the initial prompt,
optional custom names under Options, deterministic fallback, durable preparation
identity/replay/recovery and upload ownership. User explicitly selected existing
local diagnostic logging: “ok, so use the local diagnostic logs”. No further
consent question, native logger patch or external logging is selected. No default
branch integration, archive/delete/stop is authorized.

Verified initiative2026-10-03-automatic-session-slugs, workspace
/home/aither/workspace/ai/vpsfree.cz. Read plan.md/state.md and design.md section
Accepted local diagnostic retention amendment (2026-10-04), line2978. Architect
saved Astra/xhigh designed; implementer saved Sol/xhigh authored two fixture files;
lead owns retained public prose and commits. This is related source review before
native verification, not final package readiness. Same independent reviewer0,
saved gpt-6.1-sol/xhigh/read_only, no override/fallback.

## Committed source, history and delta

All four worktrees are clean and beneath worktrees/<slug>/:
- codex-web base4c170393a96ed0a6ac2e43488d073f6fcab36132,
  head32775fa7fdd9bc9b41aef74b7f195e5c3bc0f8d5.
- dev-workspace base924c0ec28c41dd8b56aaf17f2212b302ca614899,
  head95272803f457b1e4da8833b0573bc209df433beb.
- vpsfree-dev-workspace base8f8d8ecf5031c40d3e4a4ee2e9425721fc035800,
  head2e3733ade1bac712f0b852d1960a681e5bca5076.
- workspace basea51fa51e2e2503ce658003f75b77a5be1ff6c042,
  head725db6717a82524776f1a687ae9ff96515168b79.

branch-inventory.md contains each complete base-to-head series, final diff and
own incoming diff. accepted-diagnostics-provider.diff is de874-to327 delta;
accepted-diagnostics-runtime.diff is87eb-to952 delta. Both direct source changes
were folded into their existing owning units; backups retain originals. Provider
is one final helper/test/docs unit; runtime naming child b92129d owns its fixture
and retention prose, dependency unit4ec664c remains separate, managed verification
unit952 remains separate. No fixup commits or new migrations. Explicitly inspect
history disposition and no-migration lineage. Externally consumed runtime4ef298b3
and extension399c3302 remain exact unchanged ancestors, schema1/policy3 and
retained maintenance/storage behavior preserved. Workspace needs final rebase
onto shared coordination master5c855f5 after final pins, then comparison capture.

## Boundary and meaningful cases

Provider delta is only codex/ephemeral_integration_test.go and docs/reference.md.
Full bounded quote/comment-aware statement traversal is factored from diagnostic
reporting. For EXACT root-relative logs_2.sqlite, require the pinned native0002
12-column logs DDL (feedback_log_body), complete transaction/dump and exactly
one definition. Omit only complete dump-style INSERT INTO logs VALUES row
statements (quoted logs spelling supported) from the in-memory persistence view.
Preserve all DDL/index/migration/sqlite_sequence/other-table statements, original
file inventory, all owned IDs and4MiB bound. Diagnostic truncation never decides
acceptance. Reject incomplete/unsupported schema/dump. DB/saved dump untouched.
Same view applies to original baseline and every later snapshot; goal/memory
whole dumps and original seeds remain byte-identical. Other SQL/files/path IDs
remain strict. No rebaseline/reseed/store/WAL exclusion.

New pure TestEphemeralIntegrationPersistenceAcceptance covers valid quoted and
multiline rows with both markers and embedded fake SQL; other table/DB/nested
basename/DDL/metadata/ordinary files; altered/old/missing/duplicate schema;
near-match/qualified/column-list/extra-clause/comment row forms; incomplete dump;
preserved non-row statements; marker and owned ID beyond reporting caps; exact
seeded goal/memory bytes and4MiB bound. Existing safe diagnostics preserved.
Inspect correctness and proportionality; this is a fixed fixture seam, not SQL
conformance/framework, public production allowlist or adversarial local operator
containment.

Runtime delta ONLY naming_runtime_test.go plus docs/session-preparations.md and
docs/codex-package.md. Full-source race at87eb failed one leaf /hold (plus parent/
package), bad evidence after0.16s. os.WriteFile exposed create/write window while
namingTestWait returned any successful ReadFile. New mode0600 CreateTemp sibling,
write/close/same-directory rename publishes complete synthetic JSON/PID evidence.
Same hold JSON covers HTTP cleanup. No production behavior, stop/read deadline,
assertion, sleep or timeout change. Real managed integration fixture unchanged.

Existing gpt-5.5/low Direct original catalog, native0.160 binary,55restrictions,
private sink/questions, PID domain/stop ownership, immutable deny/SQL seeds,
10s whole-call/2s stop/180s native bounds remain unchanged. No tool-policy waiver.
Existing native run atde874 passed two PID ownership cycles and38fixed deny
records but failed the previous blanket local logger check. No complete native
pass exists. This review precedes one meaningful strict native matrix covering
remaining fresh-MCP/managed-conflict/final gates, then exact pins/vendor/package/
resources/managedVM/deploy/live MODEL/custom/replay. Native HTTP/SSE fallback
coverage limits stay explicit; positive live serving-transport proof remains.

## Consumers, docs and quick evidence

Provider owns public RunEphemeralTurn; runtime session_namer.go directly consumes
it. Extension consumes runtime mkPackage; workspace consumes extension. Imports,
Go/flake pins and adapter source are in companion worktrees. Runtime committed
pins still oldd371; source tests use explicit temporary modfile with exactly one
absolute local-provider replace. No committed replace/GOWORK change. Final exact
provider/runtime/extension/workspace repins and vendor hash remain required.

Main reconciled provider docs/reference.md, runtime docs/session-preparations.md
and linked docs/codex-package.md; workspace-portal.md already links authoritative
preparation semantics. vpsfree-user-facing-writing/humanizer applied directly.
Plaintext naming input/native identities may persist locally, max first8192 raw
bytes/no attachments; startup ten-day pruning is not guaranteed erasure. Ordinary
request/history and portal outcome/duration logs are distinct contracts.
Operational rollout and execution evidence stay in initiative records.

Parent full delta inspection, gofmt and diff --check passed. No declared hook
framework; normal Git hooks not bypassed. Runtime folded tree identity and exact
protected ancestor asserted. Owning cached Nix Go1.26.7, TMPDIR/tmp GOWORK/off:
- Provider go test -mod=readonly -tags=codex_integration -race ./codex
  -run '^TestEphemeralIntegration' -count=1 -json:15top groups/160pass events,
  0failure/skip,2.832s, including new persistence acceptance. Tagged file SHA
  841e10eebd3cac179fd1cf30f1139c9526bb4368c2a011bb777aa0a30b315a26.
- Runtime go test -mod=readonly -modfile=/tmp/automatic-session-slugs-static-profile-runtime.mod
  -race ./cmd/workspace-portal -run
  '^TestNamingRuntime(StartupAndLifetime|LeaderExitKillsResidualGroup|HTTPExitKeepsChildForWorkerCleanup)$'
  -count=5 -json:46pass events/0failure/skip,5.665s.
Private raw quick JSONL paths /tmp/automatic-session-slugs-accepted-diagnostics-quick.jsonl
and /tmp/automatic-session-slugs-atomic-evidence-quick.jsonl. No native/model/VM/
deployment was part of quick checks. Earlier provider fullrace atde874508pass/
3skip remains qualified; runtime complete suite needs corrected confirmation.

## Review task

High risk: persistence acceptance boundary and deployment/data retention contract.
Apply all affected lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. Read mandatory-change-review skill and all four references
fully; read applicable workspace procedures and repository AGENTS before review.
Assess committed delta, source/schema, meaningful negative cases, docs and final
series/inherited compatibility. Trusted local operator boundary applies to this
application; remote inputs remain untrusted. Do not broaden into hypothetical
compromised-operator filesystem protection.

Return findings ordered Blocking/Important/Advisory with lane/file/commit,
concrete evidence and smallest correction; explicit obsolete-history and
migration-lineage conclusion including no migrations. Separate source review
from unexecuted native/package/VM/deployment proof. No edits/tests/native/model/
Git/pins/lifecycle/deployment/approvals or nested reviewers. Report to lead, then
return idle. This is not a rubber-stamp request.
