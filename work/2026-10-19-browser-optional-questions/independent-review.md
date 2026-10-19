# Independent final review

Reviewer: `/root/optional_questions_review`, standalone review-purpose task,
configured `gpt-6-astra` / `xhigh` under installed catalog digest
`ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376`.
No nested agents, application edits, commits, deployment or long integration
tests were performed. The parent owns native launch-metadata verification.

Risk: High. General, architecture/repetition, scope/proportionality and
risk/compatibility lanes were reviewed directly.

## Findings

### Important R1: unfinished idle turns permanently clear questions

`codex-web/conversation/assets/questions.js:134-135`, commit `803e877c`.

The condition clears and persists every question whenever the thread status is
not `active`, even if its owning latest turn remains `inProgress`. Native thread
status can become `idle` during sleep and subagent waits; this is an established
supported state in `codex-web/README.md:124` and
`codex/activity_test.go:453` (`TestActivityAutomaticWaitUnionAndRuntimeIdle`).
`codex/thread_page.go:276` forwards the native thread status, so the browser can
receive this combination in normal operation.

Reproduction using the committed controller: supply an active snapshot with one
question in the latest `inProgress` turn, update the same snapshot to `idle`,
then back to `active`. Pending questions change from one to zero to zero; the
persisted record contains `cleared: true`. This can unpin an optional question
as soon as Codex sleeps to give the user time to answer, and it stays unpinned
after the wait and reload. That contradicts the selected turn-completion
lifetime. Use authoritative turn completion/current-turn identity for permanent
expiry; transient thread idleness must not expire an unfinished turn. Cover
idle-during-sleep/wait and return-to-active, as well as actual turn completion.

Lanes: general and risk/compatibility.

### Important R2: a definitively rejected answer cannot be corrected

`codex-web/conversation/assets/questions.js:67-79` and `:179-180`, commit
`803e877c`; relevant existing limit: `conversation/handler.go:562-565`.

The controller retains an immutable attempt for every failure and disables both
text inputs and all suggestions whenever that attempt exists. It does not bound
the complete reply envelope before saving and sending. A pasted answer exceeding
the HTTP handler's default 48 KiB message budget gets a definite HTTP 400 before
any native send, but the user can only retry that same oversized payload. Reload
restores the same lockout; dismissing only unpins it. A local persistence failure
before the network call can also leave the in-memory controls locked to an
answer that was never sent.

A focused controller probe submitted a 49 KiB answer to a sender returning the
handler's HTTP 400 error, then tried a short answer. Only the first send occurred;
the 50,176-character attempt remained and no answer was recorded. Validate the
complete encoded reply against the supported message budget before publishing
an attempt, and leave definitely local/rejected submissions editable. Preserve
the original identity for uncertain network effects. Cover correction after
oversize rejection/local persistence failure while retaining the existing
uncertain-delivery retry test.

Lanes: general and risk/compatibility.

## Reviewed history and contracts

Inspected actual complete series, final diffs, repository instructions, shared
controller and both consumers, native reply framing reference, existing send
authorization/retry boundaries, documentation and deployment composition:

- codex-web `c064ce09cfcea8d8af6bf676635a53cd823f772c` to
  `803e877c84ec4139e03192699f24af0f350e52ae`;
- dev-workspace `09a407953026514ae84be81dab9442fd74b6a362` to
  `db17a984d2e3b4a3f5ae41b872dc4e0041d9595f`;
- workspace `94eb7c055b44e37c5b82902788e36eb05c37179f` to
  `37740d89976d771d479c168fc393fcced6f0a5ab`;
- configuration `a2ad6da408715de811cc6d8ea7b29ac55ea341ec` to
  `26692e9da1abad570e9ad2c6d25edd740c32cd9e`.

Each range contains one logical feature or final pin commit. No obsolete branch
approaches, fixup series or repeated update streams remain in these reviewed
ranges. Bundling the portal's exact codex-web module, source pin and vendor hash
with its shared-control consumer is justified. Workspace and configuration
select the same runtime; the workspace extension selection and unrelated inputs
remain unchanged. No additional architecture or scope findings: the shared
provider owns the behavior and both actual browser consumers use it.

No migrations. There is no database, session schema, server ledger or native
protocol migration in the diff. Browser storage uses new isolated schema-1 keys.
The packet records that none of this initiative was deployed, released or merged;
application refs were published for composition. Additive transcript fields and
unchanged ordinary send endpoints preserve existing authorization and old-reader
compatibility. Deployment, native live validation and integration authorization
remain outstanding; another initiative's host reservation must be preserved.

During review the lead amended runtime to
`f2b3e827e51c7969e1af34344489fdf2df41ae30`. I separately inspected its delta from
`db17a984`: only two browser fixtures changed, adding `questions.js` to the
temporary module set and `questions.js`/`refresh.js` to the repository-browser
asset server. This fixes the original-head missing-module fixture defect without
changing application behavior. The lead records focused checks passing. Final
readiness still needs consolidated final pins and an updated exact inventory
after the substantive findings are reconciled.

## Verification and limits

The lead's packet reports quick Go, browser-state, authorization, paging, syntax
and deployment-contract checks passing. I independently ran short read-only
Node controller probes through Nix for R1 and R2; both reproduced. No application
files or tests were modified by this review. Actual-template Playwright,
native reply/CLI reconciliation and package/deployment verification remain
post-review gates. Existing new state tests do not cover native idle during an
unfinished turn or recovery from a definitively rejected oversized answer.

R1 and R2 require fixes or explicit recorded decisions before long integration
tests. Narrow corrections can be verified directly under the review skill;
contract expansion requires affected-lane review.
