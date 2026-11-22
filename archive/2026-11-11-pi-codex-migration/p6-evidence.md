# P6-A execution evidence

Owner implementer4; prior H accepted. This records isolated source, not a live
question/Plan release. Lead owns acceptance, tracking, review and integration.

Current: ready for acceptance. D P6 head `9a4f44e9c64106bc36d65fead1be881412c778c3`
is committed but publication remains lead-sequenced. Final C dependency
`a2b58b5e8d5c59cb448453e113b5dd48b20c3477` is published and CI passed.
Owned source/index windows are closed; live features remain gated.

## C dependency and process window

Source base `f9b9b4831b23aab5ddf61316eefdd02edca1cc7c`; preserved P1-F parent
`ee0c866317419209b859b27a09026d63e722c4c7`. Presentation commits:
`1a0fd1856ad02023f02670022195948022e89683` (shared card) and
`83f2fb594f5bd23e746664f6b37d2db18f5622dc` (distinct host choice values).
Only `conversation/assets/questions.js` and
`test/questions_browser_contract_test.cjs` changed. Legacy state machine,
Codex defaults/envelope and queue correction preserved.

Final head `83f2fb594f5bd23e746664f6b37d2db18f5622dc` pushed over SSH to
`git@github.com:aither64/codex-web.git`, branch
`2026-11-11-pi-codex-migration`; exact `ls-remote` matches. Worktree/index clean
when window closed. No default integration or history rewrite. This intermediate history was later consolidated as recorded below; final
whole-branch review remains required. No migrations or externally consumed state.

Quick command, in C:
`nix shell --inputs-from . nixpkgs#nodejs --command node --test test/questions_browser_contract_test.cjs test/conversation_browser_contract_test.cjs`
passed all 16 cases. Whitespace check passed. No declared hook framework or
active hooks were present; ordinary commits used the existing configuration.

Final GitHub Check run `43208496802`, attempt 1, exact final head above:
completed/success, flake job and `nix flake check --print-build-logs` passed.
Fresh verification watcher used installed package
`/nix/store/9hr3ppqzzwb12x51vwjasw8hq0ka7dab-dev-workspace-0.2.0`, catalog
`f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`,
utility `dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569`,
Luna/low, full access, danger-full-access/never. `gh run watch` exited 0;
authoritative run view confirmed success. No operation left running. Previous
`1a0fd18` Check run also succeeded; no superseded active run needed cancellation.
P7/implementer0 received this intermediate C head and the later consolidated
head below; the D pin remains that owner's later update.

## C final history consolidation

Lead explicitly released a history-only window. Fresh fetched/remote default
remained exact `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`; feature remote was
exact old `83f2fb594f5bd23e746664f6b37d2db18f5622dc`, with clean worktree/index.
Local safety branch `2026-11-11-pi-codex-migration-p6-preconsolidation` preserves
that old head. The old four-commit range is now exactly two logical commits:

1. `99ca5d26827e3eb4f6a7d6d87b4fb4af22f735c7`: original neutral API plus the
   legacy queue error-stage correction. Its tree exactly equals old `ee0c866`.
2. `a2b58b5e8d5c59cb448453e113b5dd48b20c3477`: presentation extraction plus
   distinct host choice IDs. Its tree exactly equals old `83f2fb5`.

Old range `dd90fb4..83f2fb5`; final range `dd90fb4..a2b58b5`. Both full-tree
comparisons passed `git diff --exit-code`. Final tree hash is unchanged:
`18dca609c3847283f615982236d6f2e65f789bf0`. The range-diff shows only the two
requested fixups and is retained at `/tmp/pi-p6-c-history-range-diff.txt`.
No source or check inputs changed; exact-tree successful checks above remain
applicable. No migrations, deployed commits, releases or consumed state exist.
This preserves source equivalence; it is not a deployed-lineage claim.

Force-with-lease explicitly expected old remote83 and succeeded. Authoritative
remote now equals final `a2b58b5e8d5c59cb448453e113b5dd48b20c3477`. C mutation
window closed clean/index0. Final Check run `43210515235`, attempt 1, exact a2 head, completed/success.
A fresh installed Luna/low watcher confirmed flake and Nix check success with
`gh run watch` exit 0 and authoritative run view; no operation remains running.
No superseded active run required cancellation.
No default-branch content or refs were deleted. Final reviewer still needs the
complete two-commit range and migration conclusion. P7 must pin final a2, and
consolidate the superseded old f9 D pin in its own stream.

## D source and verification

Initial observed shared D head `4f390101de7ca5047d9e41faa0b483088d591185`;
other owners' subsequent commits are preserved. Own only isolated piquestions,
piplan, additive web handlers/tests, Pi browser modules/tests, host-tool factories
and `docs/pi-questions.md`. No central resolver/server/app/CLI, worker entrypoint,
provider, package metadata or pin changes. The lead released the short index window after P5. Exact P6 parent is
`7584b9077b84c4a7e40d6c8da13f9571d40c9126`; P6 commit/head is
`9a4f44e9c64106bc36d65fead1be881412c778c3` (`pi: retain optional question and
Plan intent`). It adds exactly 21 owned files, 2529 lines. D was not pushed:
lead explicitly retained shared publication until the intended graph is complete.
No default integration is authorized or claimed.

Before staging, the exact parent and empty index were verified. A per-file
SHA256 inventory at `/tmp/pi-p6-d-hashes.json` matched staged paths, committed
bytes and unchanged working bytes. `git diff --cached --check` passed. Normal
Git configuration/hooks and a temporary commit message file were used; no hook
framework or active hook was declared. Index was verified empty and the mutation
window explicitly released to the lead immediately after commit.

Exact committed inventory:

- `docs/pi-questions.md`
- `pi-runtime/src/host-tools/plan.mjs`
- `pi-runtime/src/host-tools/questions.mjs`
- `pi-runtime/src/host-tools/questions.test.mjs`
- `portal/internal/piplan/service.go`
- `portal/internal/piplan/store.go`
- `portal/internal/piplan/store_test.go`
- `portal/internal/piplan/types.go`
- `portal/internal/piquestions/file.go`
- `portal/internal/piquestions/projection.go`
- `portal/internal/piquestions/service.go`
- `portal/internal/piquestions/service_test.go`
- `portal/internal/piquestions/store.go`
- `portal/internal/piquestions/store_test.go`
- `portal/internal/piquestions/types.go`
- `portal/internal/web/pi_plan.go`
- `portal/internal/web/pi_questions.go`
- `portal/internal/web/pi_questions_test.go`
- `portal/internal/web/static/pi-plan.js`
- `portal/internal/web/static/pi-questions.js`
- `portal/test/pi_workflows_browser_test.cjs`


Pure checks in D use the repository's pinned nixpkgs inputs:

```
nix shell --inputs-from . nixpkgs#go nixpkgs#nodejs nixpkgs#gcc --command bash -c 'set -e
node --test portal/test/pi_workflows_browser_test.cjs pi-runtime/src/host-tools/questions.test.mjs
cd portal
go test -mod=readonly ./internal/piquestions ./internal/piplan
go test -mod=readonly ./internal/web -run "TestPiWorkflow|TestPlan|TestImplementPlan|TestLegacyPlan|TestIdenticalPlan"'
```

Seven new Node fixtures pass. Question/Plan Go fixtures and selected new HTTP plus
legacy Plan decision/delivery regressions pass. Coverage includes private strict
records, capacity refusal, duplicate publish/restart identity, concurrent ordered
corrections, stale branch, preserved drafts/reconnect, crash handoff lookup only,
Unknown/NotSubmitted no resend, exact Plan bytes/digest, duplicate acceptance,
mode ACK loss, unsupported ports and no native effects from reads. Factory
fixtures prove immediate persisted pending return and cancellation forwarding.

Environment findings: concurrent P7 editing temporarily made `nix develop`
evaluation reject `piWorker`; no packaging source was changed to work around it.
Pinned standalone Go/Node/GCC supplies the same declared nixpkgs tools. The first
standalone shell omitted GCC and web compilation refused; adding the pinned
compiler resolved it. A misplaced Go `-C` flag was corrected to `go -C portal`.
These were check-launch failures, not accepted results.

A later web recheck encountered P3 supervisor source mid-edit (undefined
conversation/create/lookup/resource helpers), so that attempted check could not
compile. P3 files were left untouched. After the P3 owner confirmed coherent source,
the final full quick batch passed: seven Node cases, both Go domain packages,
and the selected web/Plan suite (7.549 seconds). No command remains running.
All 21 owned files passed a direct whitespace/final-newline check.

The existing optional/required Playwright scripts are driven by Go's browser
fixture with `PORTAL_BROWSER_TEST=1`, Node/Playwright modules and browser paths;
they are not standalone node:test suites. A direct Node invocation failed for
missing Playwright and launched no service. Proper real-browser integration
remains after committed final review, under the existing fixture environment
and a fresh watcher; no test or expected result was weakened.

## Minimal owner registration, still gated

P2 mounts `PiQuestionHandler` and `PiPlanHandler` beneath its already resolved
conversation route, injecting exact origin, request admission and stores.
`PiWorkflowAdmission` rechecks auth, operation permission, current binding and
shutdown without native loading. Operations are `pi-questions.read/respond` and
`pi-plan.read/accept`. Handler reads are observational; capture returns 202 for
host persistence, not native acceptance. No route is mounted by P6-A. Public snapshots fold immutable partial replies
into a per-item answers map; untouched items stay answerable and already
answered items require an explicit correction. Group predecessor CAS preserves
order without erasing unrelated answers.

P2 browser hooks inject the current conversation/incarnation-scoped namespace,
request API, storage and shared `createQuestionCard` into `mountPiQuestions`;
Plan hooks inject the existing Plan DOM renderer into `mountPiPlan`. The card
returns `{root,update}` and supports `choiceValues` for stable host choice IDs.
Mode/accept controls remain absent unless real policy support is proved. Drafts
and pre-network identities live in browser storage; server snapshots own status.
No direct Pi native URL, transcript entry or native path is synthesized.

P3 alone registers factories, callback transport and worker policy. Question
factory callback: `host.publishQuestion(nativeToolCallId,params,signal)`; Plan:
`host.publishPlan(nativeToolCallId,params,signal)`. The host is already caller
bound; arguments cannot choose identity. The third SDK cancellation signal is
forwarded. Native assistant entry plus tool-call ID and a stable supported
selection token must be proved before publication. P3 supplies current/idle/
hold, prepare/digest, ordinary Send and original-receipt Lookup ports. Nil ports
mean unsupported. Busy stays pending; Unknown and terminal NotSubmitted never
resend. Plan additionally needs applied/confirmed all-tool Default/Plan policy
and completed origin. The modules and fake fixtures supply none of those proofs.

## Proposed P2 compatibility hunk (not implemented)

Architect2 technically accepted the following scope/absence policy. P2 and lead
must separately release the existing central window before live writers.

The sole owner is Ruby
`Host#require_compatible_session_backends!(package, entries = registry.entries)`.
Use trusted `@state`, canonical entry roots and the existing strict target
`share/workspace-portal/runtime-contract.json` reader. Do not add entry-point
guards or a generic schema framework.

Proposed narrow observational helpers in P2's owned compatibility code:

- `question_plan_state_requirements(state_root:, workspaces:)` returns only
  `{piQuestionsSchema: 1?, piPlanSchema: 1?}` requirements or raises the existing
  error. It never creates, repairs, cleans, loads workers or changes selection.
- For `pi-questions` / `pi-plans`, missing roots or no retained JSON records add
  no requirement. Empty expected directories/known lock files are not retained
  state. Unexpected entries, malformed/unreadable/private-permission failures
  refuse. Every retained record must strictly bind a registered canonical
  workspace SHA256, slug, session/conversation incarnations, member and full
  native conversation ref; unknown/foreign scope refuses rather than disappears.
- Merge requirements into the existing hook; when retained state requires a
  field, the target must expose that exact integer 1. Missing/wrong field refuses.
  Add fields only with packaged implemented readers/writers. Missing state does
  not imply a selected backend or authorize any live writer.

Required P2 fixtures: genuine absence, expected empty/lock-only tree, retained
question-only/Plan-only/both with compatible target, missing/wrong target field,
unregistered workspace hash, mismatched path/ref, malformed/unknown/null keys,
wrong permissions and unreadable evidence. Preserve existing activation,
compensation and restoration coverage through the single hook. No P6 metadata,
central hunk or live writer is advertised by the current isolated source.

## Remaining delivery gates

Lead writing pass, including the settled per-item projection paragraph, is
complete. D's short index/commit window is complete and closed. Publication remains
lead-sequenced; no D push was made. P6-A is reported ready for acceptance and
retains follow-up/review-fix ownership. Lead owns
independent final review and whole-history/migration conclusions. Real browser
integration and combined package checks follow that review. No provider login,
model call, activation, lifecycle/default switch, conversion or deployment ran.
No legacy format is rewritten; schema-1 Pi-only records require forward readers
before any future live registration. User authorization of implementation is
not repository default-branch integration approval.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

## Final package conclusion

P6-A implements only isolated question/Plan persistence, validation, projections,
fake-port service behavior, unmounted HTTP handlers, browser controllers and
caller-bound tool factories. Reads/renders do not call native APIs. Independent
items remain answerable; corrections replace only explicitly listed item answers.
Unknown/terminal NotSubmitted never resend; Plan mode strings do not prove
policy enforcement. No successful stub, live writer or metadata advertisement
substitutes for missing integration proof.

No existing state or migration was rewritten. New Pi-only schema-1 question/Plan
formats are unregistered and have not been deployed, released or externally
consumed. The C source history is consolidated as requested; the final reviewer
still owns the complete C range and combined D history/migration assessment.
D follow-up changes, packaging/pin consolidation, bridge/compatibility release,
independent review and longer browser/integration checks remain lead-owned
sequencing dependencies, not completed capabilities. No command, watcher, claim
or reservation remains running or held by implementer4. Session remains open.
