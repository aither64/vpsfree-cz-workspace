# Archive policy review packets and results

Current correction heads: runtime 1a27453c0b67c8c24cbe1474d5a05607eb698a9a,
workspace d1e5888a9f96e32833d56f5ae18da477df44472b, configuration 1697613eab00a4bb0642b79c355c0b673b758a41.
Earlier reviews below retain their historical exact revisions. The bounded
shutdown-context correction passed affected General/Architecture/Risk review with
no findings.

Outcome: normal CLI/browser Archive closes any explicitly selected session without
merge/publication/cleanliness gates. Auto-archive retains exact merged-head proofs.
User chose private local recovery, forced removal of all owned worktrees, stopping
owned agents and retaining conversations/queued prompt records. Revival restores
checkout files and index. Neutral archived lifecycle does not claim completion.
Deploy to aitherdev via matching configuration channel and application user profile;
retry the originally requested session. No default-branch integration authorized.

Initiative: 2026-10-12-session-archive-policies. Plan, state and design are alongside
this packet. Read AGENTS.md and all applicable procedure routes at the workspace
root and each affected worktree before reviewing. Read mandatory-change-review and
its general, architecture, scope and risk lane references fully. Review directly,
read-only, without nested agents. Inspect committed whole-branch histories and
final diffs; do not rely only on this packet. Report findings to the parent with
severity, concrete evidence and file/line. Include explicit history, repeated-pin
stream and migration conclusions.

## Historical initial review: repositories and exact scope

All worktrees are under /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-session-archive-policies/.

- dev-workspace: base 60c679c52c263a0fc7a4b08c5f83a291cfd89191,
  head adf7b83f58471bfd83fab805b5cbe76338351aef.
  Three commits: af741aed1e6b5f0d99418a9b11df6181c0239003 (strict target proofs),
  73eb11f7d8b92058d699726b538034b5bd9cf3be (explicit archive/recovery),
  adf7b83f58471bfd83fab805b5cbe76338351aef (artifact reader/writer prevention).
- workspace: shared master baseline 93e478b00c51fe6ef03610c46866a88509646fdb,
  head 3bfdb6947cdcd6a05d21959d7e826acae4538ab6.
  Three owned commits: 59e321f861a2653de501c2112faa3cfb37f3d517 (archive guidance),
  110e0d14062a7008912213393f90de5416ca7e9e (one final runtime pin),
  3bfdb6947cdcd6a05d21959d7e826acae4538ab6 (artifact authoring guidance). Remote origin/master is 7ac561bc9db8b821d1bf10945bd20b144798444e.
  Complete origin-to-head series also contains six inherited coordination commits
  on shared master. Inventory those but do not amend other sessions' records.
  The feature was rebased onto current shared master before final review.
- vpsfree-cz-configuration: base b17dbea2cb1b9bf93714c929da776a4d4a6618f8,
  head 024196c3c46d77da54393ee7a4011a65e0d55a1a. One generated confctl channel
  update, dev-workspace/devWorkspace to runtime adf7b83. Generated message retained.

No obsolete feature iteration or follow-up fix commits. No database migrations.
New explicit archive journal 3, cleanup sidecar 2, manifest 3 and revival journal 4
are introduced directly in one behavior commit; existing formats remain supported.
None of these new formats has been deployed or externally consumed. No repeated
input-update streams: each consumer has one logical update to runtime adf7b83.

## Contracts, placement and deployment

Generic lifecycle, local snapshot recovery and session archive policy belong to
runtime dev-workspace. Codex transport remains provided by the existing pinned
codex-web; archive prompt preservation/goal/parent policy lives in workspacecodex.
No codex-web source/pin changes. Browser and CLI use the selected 0.160.0 protocol;
new goal/set parameters were checked against its generated JSON schema.

Consumers: workspace's flake composes vpsfree-dev-workspace extension
7157c8098dcf60127aa4df823fab82b4185ad22a with the direct nested generic override;
configuration consumes matching devWorkspace host module via its existing channel.
Extension identity, sibling inputs and follows paths stay unchanged. Host module
selection does not install the application, which comes from the user profile.
Only aitherdev is targeted; no node/database rollout. Application rollout remains
forward-only. Finish pending journals before package changes. Old executors reject
new manifest/journal versions; predecessor operations retain their saved policies.

Documentation changed: runtime docs/dev-sessions.md and
session-archive-recovery.md; workspace procedures lifecycle.md and sessions.md.
Existing README links reach these contracts. Individual rollout evidence stays in
initiative records, not generic feature docs. Main agent applied the required
English writing skill directly. Documentation explains held prompts, private local
snapshots, exact target selection, retry and revival, and supported old formats.

Local operator trusted. Review wrong selection, ordinary configuration mistakes,
concurrent writers, data integrity, interruption and remote inputs. Do not invent
hostile-local-operator or filesystem attack scope. Sharing a CWD is not authority
to retire a foreign conversation; native utilities require parent ancestry.
External editors/builds remain operator-owned and must be stopped before archive.

## Verification and review policy

Quick checks passed: Ruby/JS syntax and diff whitespace; 4 focused Ruby tests,
104 assertions covering dirty/detached removal and exact restoration, strict
unmerged refusal, retries and multiple registered targets. Extended recovery check
passed with a locked checkout and git gc --prune=now before restoring staged
objects (1 run, 31 assertions). Shared valid schema-3 fixtures passed in Ruby/Go.
Focused Go checks passed for full queue capture before deletion, lost delete reply,
goal pause/turn interruption, positive native descendant ownership, retained team
identity without recreation and manifest contracts. Config Overcommit installed
and active; generated update passed pre-commit/commit-msg hooks with its permitted
message-width warning. Cross-consumer deployment contract is checked before review.
The first packaged attempt and superseded CI failed on two old CLI expectations
and one Git fixture lacking author identity. Those tests are corrected and the
three focused checks pass with global/system Git configuration disabled (59
assertions). Final packaged/browser/CI verification and deployment remain pending.

Risk high: destructive session cleanup, private persisted snapshots, new journal
and manifest versions, App Server retirement, and host/application package rollout.
Lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
No retained root or roster exists in this threadless initiative. Installed catalog
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd selects
lead_reviewed/reviewer: gpt-6-astra, xhigh, read_only. Standalone fallback does not
add a team member. This independent review is mandatory before longer checks.


## Affected-lane final follow-up

General/Risk only, skill step 10, same independent reviewer/settings. Earlier
whole-branch Architecture/Scope conclusions remain applicable. Review the final
threadless terminal observer/signal boundary; do not repeat unaffected lanes.

Fresh explicit preflight validates normalized tracking, no retained team, exact
owned shell/authority with no Codex identity; shell stays through capture/tracking
commit. Fresh capture is journaled before full negative conversation proof, which
precedes any checkout removal. Unknown proof leaves original checkouts intact and
a retryable capture. Prepared/journal retries use exact ID/mode evidence. Browser
receipt rules remain unchanged. No conversation is adopted from a CWD.

Go's actual observer uses RequireThreadlessArchiveRuntime only for archived
operations: exact shell authority/identity or proven absence. Automatic keeps
RequireNoRuntime. Native/pane/changed identity and unknown conversations refuse.
Missing/stale authority cannot adopt a foreign same-name or reused-id terminal.

Final retirement ignores SIGHUP only for the exact caller socket/pane/session
until journal completion. Phase and final status EIO/EPIPE tolerated only for that
closed caller terminal. Other errors propagate; prior signal handler restored.

Quick checks passed: real tmux hangup executes actual phase advancement and journal
completion with synchronous output, proves journal absence. Two threadless Ruby
cases also pass (3 runs/52 assertions). Eight actual Go observer/RPC cases pass:
valid terminal, absence, automatic refusal, native/pane/changed identity, unaccepted
context and conversation residue. Explicit browser receipt plus wrong/moved/changed
receipt cases pass. Authority/manifest checks pass. Host package-layout fixture
includes the new helper in both manually assembled locations; focused test passes.

Superseded CI 38274754897 passed all session Ruby tests but found missing helper in
that host fixture. Production Nix install/link was already present. Final CI
38279110178 runs at 73eb11f. Packaged/browser checks and deployment pending.

All intended content committed; final pins published. Runtime two logical commits,
workspace two owned plus six inherited coordination commits, config one generated
pin atop b17dbea2. Superseded iterations folded. No obsolete history, repeated pin
streams or migrations. New formats never deployed/consumed. Shared master 93e478b0.

## Final review result and narrow verification correction

Independent reviewer /root/archive_policy_review (Astra/xhigh) cleared final
General/Risk and whole-branch histories at runtime 93c92dc, workspace 0f993e47
and configuration 6fa2e584. No remaining findings; Architecture/Scope conclusions
retained. Later packaged verification found only a stale v29 browser asset test
expectation. Runtime 73eb11f folds its one-line v36 expectation into the reviewed
behavior commit; the parent verified the focused test and complete range-diff.
Consumer pins were regenerated and consolidated once each. This is a narrow
test-only correction under skill step 9; no design or behavior boundary changed.


## New artifact scope: final affected-lane review

The user explicitly asked to fix the network-ipv4 session parser failure and
prevent agents breaking their own tracking. No previous artifact behavior was
reviewed; assess this new delta in General, Architecture/Repetition,
Scope/Proportionality and Risk/Compatibility. Earlier archive conclusions remain
applicable, while the complete final branch series and diff still require an
explicit final history conclusion at the new heads above.

Root cause: agents hand-wrote artifact name captions; both strict readers accepted
only label, and no typed artifact writer existed. The live application is still
the predecessor. The only direct repair to the user-selected network session was
three name-to-label key changes, preserving all unrelated uncommitted entries.
That manifest is outside owned source commits and must not be staged wholesale.

Runtime owns both readers and the new public CLI:
    dev-session artifact add SLUG PATH --label TEXT --as-is
Ruby/Go accept name as a caption alias, prefer a nonempty label, and canonical
writes retain label/path. The writer requires existing ordinary active tracking,
shares package-generation, creation and slug locks, refuses pending lifecycle,
start/fork/creation operations, validates paths/contents/output size, compares
expected bytes to avoid clobbering a concurrent manual edit, and atomically syncs
replacement. No format version change. Old readers can load canonical output;
name-only hand-edits were already invalid to them. Unknown fields stay strict.
Local trusted operator boundary applies; do not design for hostile local root.

New documentation: runtime docs/workspace-portal.md, docs/dev-sessions.md,
skills/dev-session-documentation/SKILL.md; consumer workspace
 docs/agent-instructions/sessions.md. Both actual consumer locks select adf7b83
and the same content hash, preserving extension identity and sibling pins.
Final cross-consumer deployment contract passes. No other consumers were changed.

Quick checks: Ruby artifact registration 4 runs/42 assertions passed, shared
valid/invalid fixtures passed, full Go internal/session package passed, syntax
and whitespace passed. Coverage includes canonical aliases/precedence,
insert/update, normalized duplicates, empty repository scope, invalid/oversized
input/output, builtin exclusion, operation exclusions, missing tracking,
CLI arguments, and concurrent manual edits preserving the other writer's bytes.

No migrations. No new-format state deployed or externally consumed. Each consumer
contains one final pin; all superseded pins were consolidated. The archive code
is unchanged from reviewed 73eb11f. Artifact adf7b83 is one independent logical
commit with its own tests/docs. Workspace guidance is independently committed.
No default-branch integration authorized. Final CI identity is 38284294337.


Artifact review completed with two Important findings, corrected directly under
skill step 9 in runtime 97ce087acc27923d625fc9a938444684da255551. Ruby now matches
Go Unicode whitespace blankness for validation/alias precedence, and a valid ready
manifest may initialize its omitted artifact list after readiness validation.
Focused tests/fixtures verify both supported boundaries. No design expansion.
Final consumer pins are regenerated and consolidated once each; see state/rollout
for final selection. No additional review rerun is required for these direct fixes.


## Final candidate inventory after direct fixes

Runtime base 60c679c52c263a0fc7a4b08c5f83a291cfd89191 to
97ce087acc27923d625fc9a938444684da255551: af741ae, 73eb11f, 97ce087.
Workspace shared baseline 93e478b00c51fe6ef03610c46866a88509646fdb to
bb9ba7e8b8b12813febd40c61fc8b12d966782f8: archive guidance, one generated
composition pin, artifact guidance. Configuration base b17dbea2 to
f40eb824d687f20ad4b4c574679a71164882f85f: one generated confctl pin.
Each final consumer selects runtime 97ce087 and
sha256-1t7fGOsOGukUXAZC6oXfxkwupccHmrybYn7aJsgXWMU=.
Parent inspected complete runtime range-diff: only the two requested direct
remediations and supporting regression coverage differ from the final review.
Consumer changes are generated final-pin replacements, consolidated in their
owning update commits. No obsolete history or migrations. Final deployment
contract passes at runtime 97ce087. Exact CI is 38285693900.

## Final browser correction review

Final heads: runtime ebe612f8c890bfc5325c0e5f8e86490ffa2534e3,
workspace 7f932c7d44464c0de070e88ad17f9e903fe7ff78, configuration
edeb94c1a810f17a148de3edc59209e0f580a967. Bases unchanged.
Review only affected General and Architecture lanes. Runtime range-diff
60c679c..97ce087 against 60c679c..ebe612f shows two DOM-presence guards
in pending/queue refresh-notice renderers plus exception stack diagnostics
in the existing archive browser regression. Read-only pending archival pages
intentionally omit those controls; the shared refresh library publishes on
visibility events regardless of whether a request started. Unsafe callbacks
also exist in base 60c679c. Chromium/Firefox regression passed after correction;
node syntax and git whitespace checks passed. No new API/persistence boundary.
The fix belongs to the archive page behavior; it is folded into that commit.
Runtime still three logical commits. Workspace still three owned commits
plus six unchanged inherited coordination records. Config still one generated
runtime pin; both select ebe612f8. No migrations and no new-format deployment.
Confirm consolidation and final branch history. Unaffected review conclusions
remain in force. Existing project docs cover read-only pending archival; this
DOM fix needs no additional behavior documentation.


Final browser follow-up completed: no General or Architecture findings.
Independent inspection confirmed the two missing-control guards match the
read-only template boundary and the shared refresh library's visibility
callbacks. Range-diff contains only those guards and diagnostics; artifact
remediations are unchanged. Final history: three runtime logical commits,
three owned workspace commits, one consolidated runtime pin per consumer,
no obsolete iterations, no migrations. Prior unaffected lanes remain valid.

## Real archive boundary correction

The deployed ebe612f runtime's first real explicit archive failed before any
worktree removal: `private archive recovery storage is required`. The Ruby caller
omitted both --workspace and --user-state-root for thread quiesce-explicit. The
Go provider already requires these fields to scope durable queued-prompt records.
The correction passes the same selected context used by existing recovery and
team commands. No new behavior, schema, or recovery bypass is introduced.

Focused checks passed: Ruby command regression 1 run / 8 assertions; real Go
thread CLI against a Unix App Server fixture retains queue data in the selected
private storage before deletion; Ruby syntax and whitespace pass. The fixture
covers a selected flag overriding different ambient state. Old Ruby fixtures
accepted unrelated commands and missed the absent context. No feature docs
change needed: this realizes the already documented private-recovery contract.

Review affected General, Architecture and Risk lanes only using the same retained
independent reviewer/settings. Scope and all other previously reviewed behavior
are unchanged. Inspect complete final series and range-diffs as well as the
bounded correction; no full repeated review of unaffected implementation needed.

Runtime base 60c679c52c263a0fc7a4b08c5f83a291cfd89191; current 1a27453c0b67c8c24cbe1474d5a05607eb698a9a.
Three commits: af741ae strict proofs, f02ed71 explicit archive (correction folded),
1a27453 artifact prevention. Config base b17dbea, current 1697613e; one generated
final pin. Workspace base e76c0c146a47fc9ce10d4a811610b5a9f6a02bda; current d1e5888a9f96e32833d56f5ae18da477df44472b.
Three owned commits, same feature diff except final pin; inherited coordination
commits are preserved. Each input stream is consolidated once, selecting runtime
1a27453c with sha256-z8n/lDZiB5pwmzZPdCCUiN4ATDAXZHgvmBplIzUvRLo=.
Actual first rollout retains ebe/7f/edeb exact revisions in rollout.md. No new
archive operation journal or schema-3 archive was written by the failed attempt;
existing recovery hold may be present and must be retained. No database migrations.
The new package preserves every previously deployed format and boundary; an exact
old source ref is not required for a supported consumer. Deployment itself does
not justify retaining repeated pins. Configuration hooks pass, only runtime lock
identity changes, unchanged extension/siblings/native selection.

Same independent reviewer /root/archive_policy_review, Astra/xhigh/read-only,
completed correction review at1a27453c/d1e5888a/1697613e: no findings in General,
Architecture or Risk. Selected context matches existing recovery commands,
ownership and persistence-before-deletion preserved. Caller and real CLI tests
cover boundary and flag precedence; existing provider tests cover structured
input. Three runtime/three owned workspace/one config pin; no obsolete history,
redundant streams, migrations or new formats. Prior unaffected conclusions stand.
Live retry remains required. Parent accepts evidence and starts only necessary
corrected builds/CI through fresh Luna/low /root/archive_corrected_builds.


## Final deployed acceptance

The reviewed correction was built, tested and deployed at the current heads.
Exact CI 38297311907 passed. Normal archive of the explicitly selected original
session completed with exit 0; the independent utility verifier passed all ten
full snapshots, removal/ref/journal checks. Parent verified archived portal and
runtime retirement. State.md, rollout.md and requested-archive-result.json record
the final outcome. No subsequent source change or new format was introduced.
Shared master advanced only through coordination/archive tracking; future approved
integration must perform the normal current-target checks.
