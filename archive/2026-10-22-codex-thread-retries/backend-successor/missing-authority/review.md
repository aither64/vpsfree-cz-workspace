# Retained affected FINAL review: missing creating authority

Reviewer0, gpt-6.1-sol/xhigh/read_only, thread01a162d6-4bf1-7142-bb04-7b871eb2d1af, roster34. Completed independent review delivered2026-10-24; no overrides/fallback/nesting. No Blocking, Important or Advisory findings in general, architecture/repetition, scope/proportionality or risk/compatibility. HIGH risk for persisted authority used by destructive recovery.

Reviewed Bbf6d4b0c49600c15e17fe71248807ef43424e932..032badc8ed232855173ac7b9c5cd72ee6a16dcb7/tree5f404a6448669086da27e71a8ce2e7884d77b729, against reviewed e06578e4/treec1a8e974. Correction folded into owning18; first17 exact. A11ec57d2/allGo/CJS/pins/assets unchanged. Verified exact session/environment/trusted binding, live reviewer identity, full release, mandatory skill/all4 references, current B instructions and applicable workspace guidance. Inspected design, code/callers/locks/writer/tests/docs and evidence; reviewer ran no checks or mutations.

## General and architecture

At libexec/dev-session:2422–2425 ordinary deletion captures cleanup_session, calls publication only with failed-creation context, then unchanged ensure_retirement_identity! before prepare_removal/cancellation/quiescence/retirement. Normal creation can fail after terminal/direct-team initialization and before creating-authority publication.

Private helper:6342–6365 returns for absent authority directory/terminal or valid existing authority. Strict loaders/context/trust reject malformed/conflicting records. Typed FailedCreationDeleteContext is required for the slug; fresh exact request context must preserve request/root/receipt/operation/completion/force identity, original nonce and start bytes; completed recovery cannot publish. Terminal is reread by ID/name and must retain exact IDs/name/managed mark/environment/workspace/configured tmux socket/root/native socket/client version/nonce. Authority absence is checked again before existing write_session_authority(state:'creating').

Existing writer preserves schema1, uid/mode0600, exclusive temporary creation, flush/fsync, rename/directory fsync and runner selected authority. No nonce generation or ready claim. Existing ordinary trust then validates the captured terminal. Existing lifecycle request/provider/creation/exclusive slug/runtime locks serialize cooperating writers; no new lock order or detached writer. Generic deletion/archive gains no authority. One owning Ruby seam delegates to existing context/writer/trust; no adoption framework/ignore-trust flag. Extra tuple checks establish the particular publication prerequisite.

## Scope and risk

Exactly four paths change: ordinary executor, its test, public recovery test, existing recovery guide. Production delta28 additions/one removal. No host/API/Go/native/queue/policy/UI/pin change. Failed/direct/unsubmitted/root/roster/start requirements remain. No terminal means no authority, existing record is never overwritten, and generic same-name trust is unchanged. Tests cover the actual refusal and interruption without a new recovery subsystem/native campaign.

Within the trusted-local-operator boundary, absence alone grants nothing: exact accepted provenance plus terminal tuple are required. Crash after publication leaves normal creating authority and intact start/creation/team records. Replay verifies the same record without a new phase/marker, recreate/bootstrap/resume/send. Publication precedes removal journal, so no fabricated removal progress. Injected interruption proves identical authority bytes survive without rewrite.

This establishes neither historical authority absence nor native absence/completed live deletion. Missing/conflicting provenance and ordinary package/provider/coordination/lifecycle fences remain. Prior D1/R1/transport/product conclusions retain exact-content scope; no unrelated audit/confirmation-only rerun.

## Evidence and documentation

Reviewer matched accepted/candidate maps/all586 source hashes to final commit. Syntax/green before/after586 maps match; receipt/stdout/stderr hashes match. Raw results: authorityhost6/318, authorityexecutor2/12, existinghost13/388, existingexecutor8/42, guards8/45:37tests805assertions, zero failure/error/skip; three syntax checks pass. Predecessor red1test15assertions reproduces expected postconfirmation untrusted same-name refusal. These are owner runs, not reviewer reruns.

Actual public candidate->ordinary CLI/Runner uses configured authority and real disposable tmux. Tests prove original nonce, one completed removal/replay, postpublication crash/intact retained bytes, context drift,11 terminal tuple mismatches, malformed/conflicting records, no-terminal and unchanged generic/switch guards. External native/provider/portal effects remain synthetic.

Existing README-linked docs/session-archive-recovery.md:348–355 accurately explains exact managed-terminal/absent-authority proof, existing creating writer, unchanged trust/deletion and interrupted recovery; excludes record replacement, no-terminal publication and ready claims. Approved doc hash1576cbf58643f3b9b7bd5ae1fce4b6a8d1a57c3ecce878c52c9bdc17fc16bec1 matches. Rollout/effect evidence stays in session records.

## Whole history and migrations

Reviewer independently reconstructed complete18/messages/path inventory; final18.series.txt/full-final.diff/e065.delta.diff match SCM. First17 exact; only owning18 changes with message describing final behavior. Exactly four of586 blobs/modes differ,582 equal. No obsolete approach, redundant fixup or transitional migration; correction cohesive with recovery18.

Sole consolidated A update65e58006->A11ec; complete lock graph byte-identical to e065, no redundant pin stream. Prior A8/B18 history/deployed provenance remains at recorded scope. Deployed B7b8c is supported nonancestor via exact patch/receipt provenance, not literal merged ancestry. Substantive successor requires verified rollout/acceptance.

No database/data migration, new schema/API/native protocol/journal phase/conversion/reset. Uses existing schema1 creating authority and ordinary fields; retry/policy1, generic submission3/MaxSnapshots64 and start/removal formats preserved. No branch-iteration compatibility layer.

SSH publication matches exact032badc8/masterbf6d unchanged; source clean. e065 browser32/package/Ruby/native/composition receipts retain exact-input scope and do not prove the new package. Ruby change alters declared shard/full-package inputs: fresh affected packaged checks/build/output identity and downstream selection remain lead-owned gates. No blanket browser/native rerun requested.

Reviewer performed no tests/build/browser/native/CI/live/prompt/history query, source/tracking write, Git mutation, claim, integration/deployment/lifecycle or nested review. No operational/deletion/integration permission or readiness claim. Same reviewer retained for material followups. Complete original report delivered in lead conversation; this record preserves its findings, reasoning, history and limits.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
