Team assignment from implementer0 to lead:

Source-only verification fixes COMPLETE and FROZEN for 2026-10-03-automatic-session-slugs. Same-session current verified; both identity environment variables absent and trusted workspace binding matches. Read/reused unchanged fully-read required workspace/provider/runtime guidance and documentation skill; read full accepted local diagnostic retention amendment. No production, managed-integration/VM, policy/API/model, pin, tracking or prose changes.

1. ONLY dev-workspace/portal/cmd/workspace-portal/naming_runtime_test.go.
namingTestPublish owns a mode0600 CreateTemp sibling in the evidence directory, writes all bytes, closes, then same-directory renames to the reader's exact target. On error it removes only its owned temporary sibling. The hold-mode JSON and descendant PID publications use it; HTTP cleanup uses the same hold-mode JSON seam. This removes the concrete create/truncate-before-write window exposed by namingTestWait's first successful ReadFile. Existing read/stop/deadline, argv/environment/privacy/exact-one-child/lifetime/HTTP assertions and production code unchanged; no sleep/timeout adjustment or mirror test. Current source SHA256 c3faa21c181f6befb1f18638115bc665ade934eab3fb8a5c3c45e28c855fbdf0.

Runtime affected existing nonzero selectors:
^TestNamingRuntime(StartupAndLifetime|LeaderExitKillsResidualGroup|HTTPExitKeepsChildForWorkerCleanup)$
No new runtime selector. Parent-reported base87eb917f50986d5206a08b3355837800a03e4529; no Git inspection/mutation by member.

2. ONLY codex-web/codex/ephemeral_integration_test.go, on parent-reported de874bc39553f8955cecdfaaeb4216959b40bd3c.
Read actual pinned state/logs_migrations/0002_logs_feedback_log_body.sql in kdq60x8qayhgkx6d3zbfdgw1i7dqp9q5-source/codex-rs, confirmed only0001/0002 logs migrations, and current runtime/logs.rs inserts. Fixed DDL copied verbatim: feedback_log_body/current12-column definition, not old message schema.

One full quote/comment-aware statement walk is shared with reporting. At EXACT root-relative logs_2.sqlite only, the in-memory view requires complete BEGIN/COMMIT dump and exactly one current logs DDL (whitespace normalization and exact quoted logs spelling). Missing/old/changed/ambiguous schema, incomplete quote/comment/statement/transaction, unsupported envelope and >4MiB fail. Only complete exact INSERT INTO logs VALUES(...) or quoted "logs" dump-style row statements are omitted. Qualified/near-match names, column-list INSERTs, extra clauses/comments and all other statements remain. Neither DB nor stored dump is modified. Database inventory remains in snapshot; all non-row DDL/index/migration/sqlite_sequence/other statements remain in the view.

Existing marker checks now share a fixed-category full-scan predicate with no ID/reporting count cap. Snapshot applies the same view to initial and later inspection; normal files and all other SQLite paths remain unfiltered, owned filename checks unchanged. Goal/memory dumps still retain all bytes, seeds/timestamps unchanged, no rebaseline/reseed/restoration/new file/WAL exclusion. Diagnostic log memory/goal text is excluded only by omitting known log row statements before existing sensitive-line comparison. integrationSQLiteDiagnostic remains safe reporting-only with existing64-statement/16-owner/ID summary bounds; those limits never authorize acceptance. No raw rows/prompts/IDs/native errors emitted by new code.

New pure selector:
^TestEphemeralIntegrationPersistenceAcceptance$
One group,36 source cases (NOT run): correct unquoted/quoted logger rows with both markers, multiline/doubled-quote fake INSERT/DDL text and memory/goal words; quoted/whitespace current DDL; empty valid logger; other tables/DB/nested logger/DDL/metadata/normal files; old/missing/type/default/ambiguous schema; near-match/qualified/column-list/extra-clause/comment rows; missing COMMIT/unterminated quote/comment/tail; non-row statement preservation; late non-log marker after70 allowed rows; owned ID beyond64 diagnostic IDs; unchanged whole seeded goal/memory dumps and detectable byte change;4MiB bound. Existing SQLiteDiagnostics safe privacy/bounds cases preserved.

Parent pending owning Nix command from provider worktree:
nix develop /tmp/automatic-session-slugs-codex-web-env -c env TMPDIR=/tmp GOWORK=off go test -mod=readonly -race -tags=codex_integration ./codex -run '^TestEphemeralIntegration(SQLiteDiagnostics|PersistenceAcceptance)$' -count=1 -json
Current provider source SHA256 6efd166e453987506c0d841a090f0d297eaf58f6b117f3167fdadb87df16bec6 (before parent formatting).

ZERO tests, Nix, native/model/network calls, Git/hooks/pins/deploy/lifecycle operations run; no sandbox/access workarounds. Source edits only. Parent owns formatting/quick checks, owning-unit consolidation, public retention prose and affected independent review before native/package/managed VM/release gates. User's local diagnostic choice is accepted; no further consent blocker or question. Known exception permits local diagnostic rows only, not utility history/rollout/goal/memory persistence, and supplies no isolation/native/deployment pass. Existing kernel ownership/counter/tool/binary/catalog/deadline gates unchanged.

Ready for parent checks and idle. Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/

Delivery/source follow-up: requested dev-session team assign --message-stdin attempt (message_id51fc39f7-10fc-4595-a945-d340edbe1e57) was refused before delivery with Errno::EROFS opening /home/aither/.local/state/dev-workspaces/transition.lock. No bypass/retry with access changes; reporting through report_to_lead instead.

Your optional-schema follow-up is already addressed in the frozen source: raw bytes.HasPrefix(IF NOT EXISTS) was replaced by three integrationSQLiteWord consumes (IF, NOT, EXISTS), each using whitespace trimming and token boundary checks. Therefore CREATE TABLE IF\nNOT EXISTS logs is detected as a second logs definition and rejected; canonical acceptance remains exact pinned DDL. Read-only confirmation only, no additional edits. Current provider SHA remains6efd166e453987506c0d841a090f0d297eaf58f6b117f3167fdadb87df16bec6. Actual parent SQLite3.53.3 dump evidence of CREATE TABLE logs is acknowledged, not a member execution claim.

Runtime stays frozen; parent-reported three affected selectors -race -count5 passed46 events/0fail/skip/5.665s after parent gofmt. Member ran no tests. Provider source is complete/frozen for parent formatting/quick checks; no more edits until instructed.
