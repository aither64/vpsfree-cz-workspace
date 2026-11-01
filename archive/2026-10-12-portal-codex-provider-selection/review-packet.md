# Final committed deliverable review

User direction: implement the approved provider-selection plan, including safe
aitherdev rollout from configuration and workspace user-profile feature branches.
Default integration, forced interruption, archive/delete and unrelated work are
not authorized.

Review all four lanes: general, architecture/repetition, scope/proportionality,
and risk/compatibility. Risk is high: provider credentials, native lifecycle
protocol, private durable state, process ownership, package admission and recovery.
Read the mandatory-change-review skill and every selected reference. Review
directly without nested agents or source edits.

## Cancellation follow-up review

User reported the canceled verification operation appearing without a local
switch. The approved fix shows canceled confirmation only for the exact Switch
or Cancel action initiated in the currently open popup. Close and preview-change
events clear local feedback; refresh, polling and other tabs cannot restore it.
Keep shared waiting/applying/failed/recovery and applied terminal-restoration
messages visible. Do not erase backend receipts or submit live test mutations.

Current delta: runtime 42791ba..7c07b54; configuration 82ad72d0..bfb1d89c and
workspace 28167f33..06a0a8a5; client unchanged. Assess this delta directly and
independently conclude on the complete branch history and migration lineage.
The bounded popup fix has a separate independently reviewable commit after the
reported deployed behavior; its tests/docs/assets belong to that behavior.
Configuration and workspace pin streams are each consolidated to one final
update, with generated configuration text preserved. Required native source
42791ba remains an ancestor; deployed closures and rollout evidence are retained.
No obsolete schema/protocol, intermediate migrations or repeated pins remain.

CI38365011654 identified the stale asset assertion (review finding, folded
into e0cbf22) and a preexisting 40ms retirement deadline assumption. Separate
7c07b54 permits expiration before interruption while retaining DeadlineExceeded,
no archive and ready roster checks. Adjacent successful retirement still proves
the exact interrupt/wait sequence. Production code is unchanged. Focused page
regression passes; both retirement cases pass five repetitions. No CI retry
was used to conceal either failure; final published head has its own workflow.

Quick checks pass: JS syntax, seven focused Node regressions (including shipped
popup event wiring), git diff --check, configuration Overcommit hooks, and final
composed deployment contract. Only the intended runtime lock nodes changed in
both consumers; extension/siblings/follows remain unchanged. Browser versions
are app.js v37 and codex-providers.js v2. Documentation updated:
dev-workspace/docs/codex-providers.md; design.md covers the bounded brief and
rollout.md retains the previous live deployment evidence. Longer package/CI
checks begin after this review. Existing native and VM coverage is unaffected.

The prior standalone reviewer is no longer available in the live agent tree;
no retained roster exists. Use a fresh installed default lead_reviewed reviewer,
gpt-6-astra/xhigh/read_only, catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd.
The review remains high risk for whole-branch deployment/state provenance; apply
all four lanes. The follow-up itself is browser-only and reversible through a
newer compatible package. Local operator administration is trusted; remote
clients remain untrusted. Do not broaden the implementation or add host defenses.

## Complete series and final diffs

All paths below share
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-portal-codex-provider-selection/.
All branches are 2026-10-12-portal-codex-provider-selection. All are published and clean.

| Repository | Base | Final head | Complete feature series |
| --- | --- | --- | --- |
| codex-web | 7aff1632ee97c177e68c8bc45258abe055a087dd | 5f15b9293f9b1eef7469a34d7b2044c743160283 | 5f15b92: explicit lifecycle routing |
| dev-workspace | 1a27453c0b67c8c24cbe1474d5a05607eb698a9a | 7c07b540a5e45cac4b39351f713cf3528e4df614 | eb1564a: client dependency; 5421e56: provider feature; 42791ba: scheduling fixture; e0cbf22: local cancellation feedback; 7c07b54: deadline fixture |
| vpsfree-cz-configuration | 1697613eab00a4bb0642b79c355c0b673b758a41 | bfb1d89c95308024a9269974c207bf7cefe1fb1c | cf5b8471: site configuration/docs; bfb1d89c: generated runtime input |
| workspace | 306548c348afdd409c5bc032003670c1fd547afd | 06a0a8a529c686556b33165f7a536bf7bff50050 | 06a0a8a5: nested runtime pin |

Inspect git log BASE..HEAD and git diff BASE HEAD in each worktree. The workspace
feature was rebased onto current shared master before its pin commit; shared
coordination records are excluded from its feature series.

There are no database or history migrations. New private provider state begins
at schema 1 directly. Provider schema 1, configuration and runtime were deployed on October 13;
execution evidence belongs to rollout.md. This follow-up changes no format or
protocol. The feature remains unmerged and unreleased. Old catalog-absent/state-absent behavior
remains supported. Native history is preserved through native APIs, with no raw
database replacement. Require explicit whole-branch history and migration-lineage
conclusions, including no migrations.

Each dependency stream has one final update: client flake/module/vendor hash in
eb1564a, configuration dev-workspace/devWorkspace in bfb1d89c, workspace nested
vpsfree-dev-workspace/dev-workspace in 06a0a8a5. No superseded pin commits remain.
Inspect their exact selected revisions and unchanged extension/sibling/follows
identities. Functional feature and site configuration remain separate from
generated dependency updates. Feature tests and docs are bundled with their
owning behavior; the worker, reservation admission and popup are one atomic
contract across Ruby/Go/Nix.

## Acceptance and boundaries

Sidebar shows active provider only. Existing info popup previews configured
providers through a select box without changing routing. Separate Switch action
changes every retained root/member in one registered workspace. Initial site
catalog is subscription/openai and Snajpa/codex-lb; future operator-configured
LB instances use the same contract. No per-thread selection or browser endpoint,
token or command editing. Global Codex config/auth/backups and other workspaces
stay unchanged. LB credentials are server-side token files; no LB reset API or
dashboard credentials. Keep selected native Codex 0.160.0 unchanged.

Wait durably for idle ownership; cancel only while waiting; never interrupt.
Block active turns, unresolved requests/submissions, queues, goals, unfinished
lifecycle work and unknown loaded threads. Prove native daemon and exact idle direct helper identities before stopping;
VM, unknown and helper-descendant processes refuse. Preserve saved model/effort,
member policy, directories, runtime roots, approval, sandbox, modes/plugins and
terminal identities. Private cold resumes verify effective provider responses.
Before-stop failure leaves original routing alive; later failure compensates
via native resumes and blocks writes until recovery verifies. Compatible package
updates preserve waiting intent and require matching saved-state contracts.

The local host operator is trusted as specified by dev-workspace/AGENTS.md.
Assess ordinary configuration mistakes, concurrency, wrong ownership, interrupted
operations, rollback and remote browser boundaries. Do not invent defenses
against a compromised local filesystem administrator.

## Ownership, consumers and docs

codex-web owns the public Go lifecycle resolver, provider settings and native
effective-response proof. Its example/integrations retain unconfigured behavior.
dev-workspace imports and pins it and owns catalogs, state readers, routing policy,
limits API/UI and the stable workspace-host switch worker. Configuration consumes
its host module; workspace composes its user package through the existing site
extension, which is unchanged. No reverse dependency.

Owning explanations: codex-web/README.md; dev-workspace/README.md,
docs/codex-providers.md and docs/workspace-portal.md. Site operations:
configuration/docs/operations/codex-providers-aitherdev.md and mkdocs navigation.
Session plan, state and design are at
/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-portal-codex-provider-selection/.

## Initial quick evidence (historical review checkpoint)

Passed: client TestLifecycle and full generated request corpus against selected
0.160.0 experimental schemas; runtime TestProvider/TestMetrics/TestCredential/
TestCatalog/TestCodexLimits packages, Ruby worker 5 tests/16 assertions, Ruby and
JS syntax, popup Node contracts 3/3, local provider protocol payloads; git diff
checks; active Overcommit config hooks; final composed deployment contract.
Logs: /tmp/provider-quick-client.log, /tmp/provider-quick-complete.log,
/tmp/provider-quick-setup.log, /tmp/provider-deployment-contract.log.
The setup log records a corrected synthetic enum mistake; later protocol check
passes. No hook bypass. Full packaged checks and isolated native failure/history
checks have deliberately not begun before final review.

No production provider mutations. Deployment must separately prove package
transition restart safety: portal/tmux cgroups may contain VM runners. Long
checks/builds will use a fresh installed Luna/low utility watcher after findings.

Reviewer selection: no valid retained lead/roster in this tracking-only session
(stable team list refuses). Installed default development team lead_reviewed,
review-purpose reviewer: gpt-6-astra/xhigh, read_only; catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd.
Use a fresh standalone reviewer with those exact settings.

## Affected-lane follow-up

The initial four-lane review is complete; see state.md for its eight findings and
remediation evidence. Review the changed general, architecture and risk/compatibility
lanes. Scope remains the accepted catalog/preview/workspace-wide guarded switch.
All changes are committed and focused checks pass. Long native integration has
not started. Runtime functional commit is amended; no repair-series commits remain.
Configuration's follow-up input was consolidated into one final generated update;
its final generated message was preserved byte-for-byte. Workspace pin is amended.
All four exact branches remain unmerged/unreleased/undeployed and no migrations exist.

Material follow-up behavior: atomic bounded receipts within state, persistent worker
between requests, exact shared-service health wait, native built-in profile support
and direct idle helper ownership. The latter replaces the sole-PID requirement;
selected-version capture can start required team MCP helpers. Accept only exact
native code-mode binary/argv or exact selected/validated launch-marker runtime
team-MCP binary with all saved member arguments, direct parent and idle proof.
Reject every other process and every helper descendant; no names-only allowlist.
Evaluate practicality and safety from code and verification, not the prose claim.

Native cold TurnContextItem stores compiled permission_profile separately from
active_permission_profile identity. The reader uses the actual selected 0.160.0
format. References checked: protocol/src/protocol.rs and utils/approval-presets
src/lib.rs under https://github.com/openai/codex/tree/rust-v0.160.0/codex-rs .
Three exact built-in IDs are supported; custom identities/inheritance, unsupported
sandboxes and missing effort fail before quiesce/stop. Root/member environment,
terminal pending warning, active limits invalidation and existing ManagedTmux
socket API are fixed as requested.

New tagged native fixture compiles but has not executed: provider_transition_
integration_test.go uses isolated state/socket and loopback providers, real private
helper/team-MCP handlers, cold/loaded histories, explicit built-in profile, model/
effort preservation, history-prefix assertions and endpoint counts both directions.
Focused checks: Ruby provider 12/44; exact four prior CI terminal failures 4/31;
Go provider/helper/cache/limits; shipped browser contract including A-to-B failure;
JS syntax; selected-native fixture compile; final composed deployment lock contract.

## Final history confirmation after native execution

Current heads and complete series are in the table above. Scope and schema
lineage are unchanged; no migrations and no feature state has been deployed.
All previous general/architecture/scope/risk findings are recorded in state.md.
At 10112f, general/risk fixture review found only the canonical priority tier,
now fixed and directly checked. Native execution then required fixture child
arguments and per-task process enumeration, and revealed an unnecessary settings
update that materialized default collaboration instructions. The helper now
skips values equal to the effective resume result, reducing mutation. The
fixture explicitly resumes retained policy before a new turn after short-lived
helper subscriptions disappear. These are bounded repairs within reviewed
restoration semantics; no public contract or ownership boundary changed.

Native TestNativeProviderRouting passes at 0fd76973, both directions and
compensation, 46.44s, log /tmp/provider-native-0fd.log. Focused helper tests,
tag compilation, Ruby fixture regression and diff checks pass. The real-worker
VM check is running. The exact composed deployment contract passes, retained in
/tmp/provider-deployment-contract-0fd.log (the older unsuffixed log is historical).
Runtime
functional repairs remain in the owning commit. All generated configuration
pins are consolidated into one, preserving the final confctl message exactly.
Workspace pin is amended, preserving extension/siblings/follows identities.

Only general whole-branch history confirmation is requested now: independently
inspect all four final series/diffs, consolidated pin streams and migration
lineage. Do not repeat completed unaffected content lanes. Report a concrete
serious issue if the final narrow changes introduce one.

Final review completed at 0fd/d776/04b8: no new findings, no obsolete history,
consolidated streams, no migrations. Subsequent VM execution exposed only an
unquoted fixture cgroup path. One-line shlex.quote repair is folded into da86,
with exact generated pins consolidated again in d9e/1f94. Parent inspection
confirms no other source difference, and Nix parse/diff checks pass. This bounded
fixture repair requires direct verification under review step 9, with no new
design or boundary; unaffected review conclusions stand. Final exact contract
evidence is /tmp/provider-deployment-contract-da86.log. No feature state deployed.

## Bounded CI scheduling fixture repair

Review general and architecture lanes for separate committed runtime
16a4e9ff6e691f1189323a6e9446e46c29b5a532, parent da86d090. This is an
independently reviewable repair to a baseline test, so it is deliberately
separate from the provider feature. Full runtime series is eb1564a, da86d09,
16a4e9f; no obsolete update or migration is added. No production code changes.

CI 38321148579 failed only the unchanged scheduling test's 3-second progress
wait; /tmp/provider-ci-da86-failed.log. The old fixture creates a full server
whose activity reads fsync snapshot files and directories while holding read
slots. That adds disk latency to its queue-fairness assertion. The repaired
fixture uses a server with only the required workspace configuration and no
operation store. It retains all 40 readers, concurrency bound, unique progress
and cancelable browser-read assertions. Twenty focused repetitions pass in
0.518s; log /tmp/provider-activity-scheduling-quick.log. Risk of this bounded
unit is low, with no state, API, process or provider boundary changed. No lasting
product documentation update is needed for an internal fixture.

Matching generated pins are being mechanically refreshed/consolidated. Their
final exact heads will replace the table before deployment. Evaluate the new
test unit and any serious issue encountered; do not rerun unaffected completed
feature lanes. Existing immutable da86 host VM operation is still running.

This follow-up review is complete with no findings, no obsolete series and
no migrations. Final generated heads now match the table, with one pin per
stream; their generated message and extension/sibling/follows identities are
preserved. Exact composed contract passes at 16a4e9ff, retained in
/tmp/provider-deployment-contract-16a4.log. Earlier hashes/logs describe their
historical review or execution checkpoints, rather than final deployment.

## Patch-equivalent workspace rebase after review

The reviewed workspace pin was da517c1b on base655648a1. Shared master advanced
only through unrelated coordination archives. Final rebase produces33c0834d
on42c2a388, with range-diff equality and identical package derivation v3jkb98a.
No reviewed implementation, pin identity or contract changed. Original review
conclusions and immutable package-build proof therefore apply directly. All
other final heads are unchanged. CI 38366486448 at runtime7c07b540 passed.

After rollout, one additional unrelated coordination checkpoint advanced master
to 306548c3. The final pin rebased to 06a0a8a5 with range-diff equality and the
same v3jkb98a derivation. The complete final series remains one nested pin;
reviewed implementation, history disposition and migration conclusions stand.
Scoped host/profile deployment and read-only live acceptance pass; details
belong to rollout.md. No browser visual test or live provider mutation occurred.
