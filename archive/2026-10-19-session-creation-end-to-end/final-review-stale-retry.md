No Blocking, Important, or Advisory findings in the stale-retry response fix or
HTTP restart-readiness correction. Prior production, inventory and consumer-pin
review conclusions remain unchanged outside this delta.

Independent affected-lane review by `/root/creation_final_review`, retaining the
same gpt-6-astra/xhigh identity and original catalog fallback. Verified the exact
session/environment binding and live null roster. Read the review packet, delta
and complete series, applicable guidance, mandatory-review skill and all four
lane references. Verified both supplied diff artifacts byte-for-byte against
their committed Git ranges and assessed the complete final diff against the
previously reviewed tree. No project edits, long checks, nested agents, deployment,
integration or lifecycle operations were performed.

Runtime reviewed from `7ceb6b943c7fa6e6db2b42b1fc2d9732c6413e03` through
`814568f3a28ae916ef193fd0be129a9f28fe1ffd`. New changes are
`11620fc9793083a8ba2a8ac25cc4cf7357c3c489` and
`814568f3a28ae916ef193fd0be129a9f28fe1ffd`, following accepted `95cc08d`.

- General: `portal/internal/web/preparation.go:721` separates terminal mappings
  from runnable preparations. Receipt/attempt validation and persistence
  confirmation still precede this branch. The handler releases `operationMu`
  before calling the existing status projection, avoiding recursive locking.
  It returns 202 only for current `ready` status; `gone`, `cancelled` and
  `conflict` return 409. No terminal branch launches work or increments an
  attempt. The existing handoff retry owner is unchanged. The extended
  compaction regression at `preparation_test.go:957` verifies ready replay,
  subsequent gone refusal, preserved receipt identity, no new creation receipt
  and no recreated directory. The documented distinction between unfinished
  retry-owner attempts and compacted preparation attempts matches the code.
- Architecture: status and removal-identity decisions remain owned by the
  existing `preparationStatus` projection. The fix does not duplicate removal
  history parsing, create another retry path, or change persistence ownership.
  The browser's ordinary non-success handling already consumes an error from
  rejected responses, and subsequent status polling still observes terminal
  state. The HTTP correction stays entirely in the fixture's restart helper.
- Scope: both changes address demonstrated failures with narrow mechanisms.
  `nix/tests/session-creation.nix:151` waits for successful HTTP service on the
  actual portal Unix socket instead of accepting a surviving pathname. Failed
  readiness probes are retried by the test runner; scenario/API failures after
  readiness are still asserted normally. There is no API replacement, product
  readiness hook or relaxation of the duplicate-turn/identity assertions.
- Risk and compatibility: the change intentionally tightens the HTTP response
  for an already-refused terminal retry; it does not introduce a new destructive
  operation or permit resurrection. Ready replay remains idempotent. Existing
  origin, package-generation, receipt, attempt and removal-history checks are
  retained. Persistent formats, native Codex, provider formats and dependency
  selections are unchanged. A rollback to `95cc08d` restores the misleading
  202/gone response but retains its existing no-relaunch guard; the earlier
  optional-provider reader rollback constraint remains applicable.

Whole-branch history: the complete series is `98ae6b3` journal compatibility,
`bc29fab` packaged acceptance/CI/docs, `95cc08d` retirement discovery,
`11620fc` terminal retry refusal and `814568f` HTTP restart readiness. The new
production correction and fixture correction are independently reviewable and
properly separate. Retaining the exact `95cc08d` ancestor is justified here by
concrete consumers: workspace `d27d7615` and configuration `a0970c69` pin that
revision, and the recorded prepared/active urgent rollout requires it. The
recorded system activation has succeeded and the profile job consumes that exact
source. Keeping these two follow-ups additive preserves an inspectable upgrade
from the consumed runtime without disturbing the in-flight rollout. No obsolete
protocol design, unused compatibility path or migration-only branch iteration
remains; no runtime-history rewrite is required for this review.

There are no repeated runtime dependency/pin/generated-update streams. The two
unchanged consumer branches still each contain one selection commit, as reviewed
in `final-review-consumers.md`. Their planned later final selection must remain
one consolidated update per consumer; development deployment alone is not a
reason to retain redundant pin commits. Preserve the required exact `95cc08d`
source/ref and rollout provenance if later history work changes reachability.
**No migrations** in the runtime range or either unchanged consumer range;
there are no migration versions requiring provenance preservation.

The runtime worktree was clean at the reviewed head and the full-range whitespace
check passed. The packet records gofmt, Nix parse and all focused
`TestSessionPreparation` checks passing in 4.751 seconds. I inspected their
coverage and did not rerun long verification. The failed exact `95cc08d` VM and
CI remain diagnostic evidence, not a full pass. This review permits the parent
to proceed with verification of the new head; it does not declare full acceptance
or integration readiness. The separately authorized urgent `95cc08d` rollout is
unaffected. Final package/negative-control/live acceptance and matching final
consumer selections remain required before merge or release.
