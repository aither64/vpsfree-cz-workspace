# Final independent capacity and affected-fixture review

## Findings and disposition

No Blocking findings. One Important finding remains open at the reviewed head.
No separate Advisory finding. Residual verification gaps are recorded below.

### C1 — Important — Retry-state inventory errors bypass the new package capability gate

Lane: risk/compatibility, with general error handling. Owning commit:
`18432f0c8f86dec7405257f5dc244762d7a788ed`.

`libexec/workspace-host:3049-3060` requires both `turnRetryStateSchema` and
`turnRetryManagedTurnProof`, but line 3050 first treats an empty `Dir.glob` result
as proof that no retry JSON exists. Ruby glob suppresses ordinary directory
inventory I/O failures. If the retry root or a nested retry directory becomes
unreadable, retained records can be hidden from this predicate and both
capability checks are skipped. The rescue after the contract read cannot catch
an error that glob suppressed.

This matters at the new persisted boundary: an otherwise admissible predecessor
has StateSchema1 and SessionPolicy1 support but no managed-turn capability. Once
an ordinary save has produced schema 2, that predecessor's strict reader rejects
the record. The faulty presence check can therefore admit a package that cannot
manage retained retry state. An existing policy sidecar does not cure this:
the predecessor already supports its separate policy capability. This is an
ordinary permissions/I/O or configuration failure, without a hostile local
operator assumption. It establishes an unsafe compatibility admission, not
evidence of an actual deployment or lost state.

Source evidence is consistent across the owners: the existing
`turn_retry_policy_state?` at `workspace-host:3076-3106` uses `lstat` and
`Dir.children` and refuses inventory errors; `workspace-session-services.rb:213`
explicitly explains why glob is unsuitable for this purpose. New host tests
cover retained malformed JSON, capability shapes, preparation and candidate
activation, but inventory-error coverage at
`test/workspace_host/profile_transition_test.rb:64` covers the policy tree only.
No reviewer fault-injection probe or test was run.

Smallest requested fix: reuse or narrowly extract the existing fail-closed
JSON-presence traversal for the retry tree. Keep a genuinely absent root and
ordinary empty/lock/temporary-file-only directories free of the capability gate;
keep any retained `.json` sufficient regardless of payload validity. Refuse
root and nested inventory I/O failures before transition. Add focused root and
nested fault regressions and retain existing preparation/activation checks.
Do not add a collector, parse/rewrite retry payloads, migrate live state, or
broaden this into unrelated inventories.

The lead has accepted C1 as Important and assigned that narrow remediation to
the source owner. This report intentionally reviews immutable `18432f0c`, not
the owner's subsequent mutable edits. The fix is **not verified or closed by
this report**. The lead can close the requested narrow correction through
focused inspection/checks under mandatory-change-review step 9; a changed
compatibility/design boundary needs the affected follow-up instead.

Source-review disposition: otherwise no additional issue was established in
the assigned scope. C1 requires a verified fix or an explicit recorded decision
before continuing under the skill. This report does not itself clear that open
gate or authorize any long test, publication, deployment, integration or session
lifecycle action.

## Identity, settings and exact review boundary

Retained independent `reviewer0`, thread
`01a19ca7-8da1-7e63-852f-72d8332c553a`, purpose `review`,
`gpt-6.1-sol` / `xhigh` / `read_only`. Fresh same-session roster inspection
confirmed these saved settings and ready state. No override, fallback, nested
reviewer or substantive authorship.

Before session-record access, `dev-session current` from the tracking directory
returned exactly `2026-11-02-session-temporary-service-cleanup`. Both
`DEV_SESSION_SLUG` and `DEV_SESSION_WORKSPACE` were absent, and the trusted
developer binding matched `/home/aither/workspace/ai/vpsfree.cz` and that exact
slug. Reconfirmed after context continuation.

Read mandatory-change-review and all four lane references in full; applied
general, architecture/repetition, scope/proportionality and risk/compatibility
to capacity, and general/risk to the affected fixture. Consulted workspace and
runtime instructions, required procedures, documentation guidance, packet,
plan/design/state context, committed source/diffs/history, tests and receipts.
The documentation/handoff skills govern this report's placement and session
link; the lead retains coordination-state updates.

Repository/target: `git@github.com:aither64/dev-workspace.git`, `master`.
Complete reviewed range:
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79..18432f0c8f86dec7405257f5dc244762d7a788ed`.
Final tree: `013acdd68b79865ce5f72672e0c2049d529e6464`.

Independently inventoried complete logical series:

1. `19dd03b79a2997098934afafbe70c63b978c1ca7` — Resources navigation/counts and Team count.
2. `f7add7cea8a836810d32688ef2d1cf4cc011af19` — registered service owner/lifecycle.
3. `5b4b711748343f4ffe88b96c50d88a9f98eeb04d` — dependent portal/package integration, including the fixture correction.
4. `18432f0c8f86dec7405257f5dc244762d7a788ed` — compact managed-turn retry proof.

Whole branch: 71 files, 5,503 insertions/281 deletions. Capacity delta from
`5b4b7117`: 24 files, 1,279 insertions/154 deletions. The committed submission's
source/index cleanliness was checked when binding this review; later remediation
work is outside this exact immutable boundary.

Read immutable source
`/nix/store/9pxkf5h3wrmhsfl4lx4ahjd04mc3khgb-source` and independently verified
NAR `sha256-4EjB9p7pb85lZtZr+RqIJOpkgnAMEjSQRtZLFR3cnjI=`. All 676 committed
entries, file contents, symlink targets and executable modes matched, without
extra or missing source entries. The ordinary review root
`capacity-managed-turn-review-source` remains untouched.

## Scope, architecture and behavior conclusions

Overall risk is **High**: persisted automatic-continuation authority, native
protocol interpretation, uncertain delivery and host package compatibility.
Scope was assessed against the actual user amendment before detailed hardening.
The original registered-service cleanup and Resources/Team delivery remains
distinct from the explicit later capacity requirement. The recorded 74-input
failure had native `serverOverloaded` and enabled policy; admission retention
had consumed the turn. Accepted input volume must not disable an otherwise
eligible retry. The records show concrete diagnosis, red/green reproduction,
committed implementation and focused-check milestones, rather than only design
activity. This is a substantive follow-up, not a small fixture-only change.

The shared current-turn authority and chronological hash prefix address that
failure without raising a finite input cutoff or retaining repeated common
instructions in every accepted snapshot. `turnretry` owns durable state and
compaction; `workspacecodex` owns native observation/matching and execution
proof. Portal, CLI, retained-team delivery and the scheduler use that shared
owner. The pinned codex-web Request interface supplies transport; its existing
full-history walker has different completion semantics from this bounded,
restart-verifiable proof reader. I found no additional architecture/repetition
or proportionality issue requiring another abstraction or subsystem.

Inspected exact client-ID/content matching, scope/epoch/binding/socket/provider/
policy checks, context conflict rejection and atomic prefix/source persistence.
The reader uses ascending 64-item pages, a bounded per-invocation page budget
and pre-request time check, with no total-page cutoff. Process-local cursor
hints are bounded and disposable. Restart recomputes the durable prefix;
active-tail replay, rollout identity/tail checks, fresh latest-turn checks and
cache invalidation on failed save preserve the supported authority boundary.
Incomplete proof does not settle the idle gate or consume eligibility. Exact
native execution context still supplies model, effort and collaboration mode.
No fallback model, original-prompt replay or new policy is introduced.

The already-handled exception retires only accepted-bound, nonexecuted,
unprotected admissions of that durably handled turn; it does not rearm the old
failure or manufacture compact authority. Settings changes still advance the
epoch and invalidate earlier proof. Obsolete executed-cache retirement requires
a fresh successful latest-turn observation and an atomic save before dependent
work. Empty/failed observations do not authorize it. Current-turn proofs,
unbound admissions and exact Pending source identities remain protected.
Pending's immutable snapshot, UUID reconciliation, cancellation, quota charges,
provider progress, recovery holds and native socket identity retain their
existing authority. No new collector is needed.

The local operator remains trusted. Ordinary I/O, concurrency, wrong identity,
remote/native input and secret-exposure risks remain in scope; hostile local
filesystem containment does not. All existing unregistered services remain
excluded, with no discovery/adoption gate. No service controls, proxy or links
were added by this follow-up. The later machine-claims proposal/implementation
assignment is outside this reviewed source and is not a condition of this
capacity conclusion.

## Affected fixture and retained review conclusions

Compared `ee3f1fdd..5b4b7117`: only
`nix/tests/session-archive-lifecycle.nix`, 11 insertions/3 deletions. Delete now
answers yes through a real PTY with `script --quiet --return`, preserving the
child exit status. Assertions check the intended shutdown-verification refusal,
preserved files, ordinary `thread_retired` removal journal, `services_pending`
delete prelude, force flag and matching operation ID. Restoring the invocation
then retries the original command through existing cleanup assertions. Stop
answers the exact slug through the same PTY. This corrects the test's real
confirmation contract without relaxing production cleanup or refusal rules.
No new source finding in this fixture correction; its native execution remains
unproved.

Unaffected content conclusions are reused from `review-final.md`,
`review-final-history.md`, `review-revive-ui.md` and `review-native-job.md` under
the skill's narrow-fix policy. Those reports remain unchanged. The original
R1–R3 reconciliations, completed-intent UI guard and native present-empty Job
interpretation are not reopened by capacity or this fixture-only correction.

## Whole-history, consolidation, inputs and migration conclusion

Compared the complete four-commit inventory and final diff with the requested
outcomes, including range-diff against accepted EE3. UI and core are `=`; the
dependent change is exactly the fixture correction. The standalone `52ed98c9`
fixture fix and folded `5b4b7117` have identical tree
`4b299131feba1f8f64ac2dba675d40d542bb98ae`. Historical EE3/52ed and earlier
reviewed refs are retained outside final ancestry. The final series introduces
the final behavior directly. **No obsolete approach, redundant fixup or
transitional implementation remains in this four-commit history.** Supporting
tests/docs belong with their behaviors; the capacity follow-up is separately
reviewable. The commit split and final-result messages are coherent.

**No database migrations.** New local service schema 1 remains its direct
introduction. Existing production retry schema 1 is a supported predecessor,
not an abandoned feature draft. New retry schema 2 is introduced directly by
the fourth, unpublished/unmerged/undeployed commit; no intermediate conversion
version is retained. The strict reader accepts schemas 1/2, rejects schema-1
managedTurn and explicit managedTurn null, and does not rewrite on load. Only
an ordinary admitted atomic save upgrades valid state. Exact predecessor-source
evidence supports its schema-2 rejection and admission of the dual-reader
candidate. Snapshot/Pending hashes, UUID/charge formats, policy sidecar, native
ledger, recovery and ordinary service/journal/receipt formats retain their
supported contracts. Migration provenance is sound; the forward-only host
admission promise still requires C1's correction.

**No repeated dependency/channel/input/generated update stream exists in the
reviewed runtime range.** `flake.nix` and `flake.lock` are unchanged from c218.
Read the actual complete locked graph, including follows: nine dependency nodes
plus root; lock SHA256
`fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955`.
Codex-web remains `d3a29bee90ef00a08816920408c596152339a637` with unchanged NAR.
There is no redundant intermediate runtime pin to consolidate.

Workspace/configuration B7/59d pins and app/system artifacts remain historical
EE3 inputs. They do not certify this source. No future generated pin, refreshed
graph, package output or mechanical-equivalence receipt is accepted here.
Later actual mechanical reuse remains conditional on its installed verifier,
strong source/NAR/full-subgraph and exact-range evidence, retained accepted
review, schema-1 receipt and consolidation/migration obligations. Substantive
baseline changes require affected review. Source review never grants default
integration approval.

## Verification evidence and limits

Inspected the final receipt and retained logs. Core checks report full turnretry
6.960 s, workspacecodex 166.553 s and session 4.094 s passes. Independently
compared tested tree `95b4e7f8afd55d67ccce2a4615e71ae1d15cfc18` with the final
tree: exactly one added active-observation line in the web fixture; all core
production/test inputs unchanged. Affected retry web then passed in 43.415 s;
host checks passed 12 tests/238 assertions. Correct Go entrypoints for the
shipped Composer and BrowserClient JS contract harnesses passed in 0.673 s and
1.238 s. These are actual shipped-code component harnesses, not Playwright or
native acceptance.

Coverage includes the 74-input red/green cause, pure-state large-context cases,
205-small/65-large permanent wrapper cases, incremental 261-page/restart proof,
corrupt/reordered/truncated prefix and cursor/save faults, already-handled and
warm-settings boundaries, and 200-turn obsolete-proof retention with Pending
protection. Earlier one-off 205-large evidence remains scoped to its recorded
inputs. Failed obsolete fixture assumptions and the incorrect standalone Node
invocation are retained honestly; **the combined batch did not wholly pass**.

The new reader has not yet been proved against the real pinned native API.
Synthetic native DTO/page tests do not certify native cursor/order/append
behavior. Two Playwright consumers remain pending. The revised packaged native
archive/service cleanup VM has not passed; older creation/fast/package results
do not establish this exact head's native cleanup. Full final package/CI,
installed browser/usability, downstream source selection and deployment remain
outstanding. The earlier failed raw Job response was not captured; no causal
body or cache/store-absence explanation is invented here.

This reviewer ran no tests, builds, native/live probes, CI, source publication,
claims, deployment or lifecycle operations. No source, Git, store or old report
was mutated. Only this permitted report artifact was written. C1's focused
remediation and required subsequent verification remain with the lead/source
owner; no broad duplicate content rerun is requested for that narrow fix.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
