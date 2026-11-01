# Final review finding reconciliation

Original independent report: final-review.md, reviewer0 Sol/xhigh, all four lanes,
High risk. Original modern range63d484fc..b02c922a is retained unchanged in that
report and refs/evidence/2026-11-01-published-advisory-corrections/reviewed-b02c922a.

Reviewed successor by lead:1c8478bceb3943645ec06ccde895ee4b0985873f over SAME
base63d484fc070dbee633d32624de545e834d483701. Single logical commit remains;
tree7d3169bc4f80af199631e73cc4442b7985d8cf6d, clean/pushed/draftPR122 exact.

## Direct narrow-fix inspection

Lead inspected full ten-path b02c→1c847 diff and both new rendered test files.
Changes are+282/-13:243 regression lines, prescribed source/copy/assertion and
ten-line factual worklog. No API/dependency/transport/schema/capture changes.

- R1 RESOLVED: captureEditor uses returned coherent snapshot, maps current child
  by node, requires clicked existing row ID to match or rejects missing/replaced/
  wrong-node; stale Add rejects newly appeared row. Panel initializes current
  state, precise times and notes from that result. Five rendered cases stage
  fresh parent revision9 with stale child values; note-only payload keeps latest
  state/times and leaves unchanged Czech note omitted/preserved, no create.
- R2 RESOLVED: DetailDialogs receives live advisory/CVEs for ordinary dialogs,
  distinct editorAdvisory/editorCves only for original editor. Failed editor keeps
  its captured snapshot. Two full rendered detail cases (saveT1→T2 and cancel then
  externalT2) assert unchanged-date announcement sendsT2,state:null,send_mail:false
  and retains explicit state/mail controls.
- R3 RESOLVED: existing admin browser asserts published Edit visible and Publish
  absent. It no longer contains the contradictory post-publication restriction.
- A1 RESOLVED: exact main-authored English/Czech copy requires close/reload/review,
  completed/remaining placeholders preserved; runtime write block unchanged.

Focused evidence:38advisory tests/12files pass, scoped ESLint/Prettier,
catalog parity/structure, structural budgets, frontend and strict E2E types
(100checked/183deferred),design-doc audit pass. First new-fixture typing failures
were corrected to actual envelopes/indexed notes, not disabled. Log:
/tmp/2026-11-01-advisory-review-typed-checks.log. New tests were also inspected by
lead; no duplicate test run required for this evidence.

These implement the reviewer's prescribed narrow corrections without new design,
public contract or accepted-boundary expansion. Mandatory skill step9 applies:
direct diff/focused regression reconciliation, no broad reviewer rerun solely
to confirm fixes. Original report remains authoritative for original ranges;
this record binds the actual successor and resolved findings.

## Independent verification release decision

All3Important+1Advisory findings resolved, noBlocking. Modern source is committed
and quick-verified. Its longer declared unit/build/browser/package verification
is released independently while the primary API refreshes an unrelated upstream
HaveAPI0.32.1 dependency/docs baseline and a diagnosed one-line test fixture.
Modern inputs remain pinned/current reviewed63d484fc and do not use that mutable
API worktree. No API acceptance claim until new API/pin ranges are quick-checked,
affected compatibility refresh reviewed and real API tests pass. No production,
integration/deployment/lifecycle authorization.

No migration/obsolete history/repeated stream introduced by these narrow fixes.

## API endpoint-inventory completion

Final API successor inspected directly by lead:
097226b22edf8b59f80b5dfaa55265e9d0cac633..
4cf556e56b522722db18ebf1f1bb5859523e8b4c. Its complete series remains A
03dd433f3fa97c3129283b10c8df1df1378f3719 and B
4cf556e56b522722db18ebf1f1bb5859523e8b4c. Previous reviewed/runtime-tested
c8ef is preserved. The entire c8ef-to-successor diff adds exactly two entries
to api/spec/api/covered_endpoints.yml: security_advisory#delete and #retract.
These are the existing intended actions, already covered by executed resource
specs. No pending rules, assertions, runtime, docs or other test files changed.
The complete final path inventory has no migrations/schema/seed changes.
Range-diff shows only that A hunk; B is equal. No obsolete intermediate commit
or repeated pin stream is introduced.

The failed current-head full/foundation CI result is preserved in api-acceptance.md.
Focused endpoint coverage passed1example/0failures/0pending. Lead inspected the
entire successor diff, inventory consumer and original/final native results.
Direct JSON comparison proved actual API shell derivation (including builder
and inputs) and both full/core tool/version/effective-lock environments equal.
Git object equality outside the inventory establishes unchanged loaded API,
selected specs, DB helpers and dependency inputs. Inventory is consumed by the
separately verified endpoint-coverage/generation specs, not the released runtime
advisory selection. Full88/core79 successful examples are retained for those
identical effective inputs; they are not misrepresented as rerun on a new SHA.

This completes the existing reviewed scope through conventional test bookkeeping;
no new design, public contract or accepted boundary requires a broader review.
The skill's narrow-fix rule applies. Final strict KB acceptance must use the
refreshed committed pin; legacy browser acceptance must use exact4cf556e56.

Final KB successor is41097bd4cd973ecaa185905114e481aed5c3c536 over unchanged
ce2c8cd9358c3636e5d39343e595df813a0b197f, one consolidated five-file pin commit.
Lead inspected the full beeb-to-successor diff and independently parsed both
lock graphs: only selected vpsadmin node changes; root/follows/other nodes and
selected node input edges are equal. Capture provenance is equal except the
selected source revision; explicit OS6bdf458f and page provenance remain.
No content/capture/migration additions or obsolete intermediate pin commits.
Final strict check and legacy browser verification are released under the
existing bounded acceptance brief; no integration/deployment authorization.

## Legacy notification assertion correction

Lead directly inspected the entire0111e977-to-006454821ee35b291def4bfafee19cd0553bc7b2
diff: only three new Update failed assertions now use the existing imported
expectNotification helper. That helper targets#perex; the old content helper
targets#content-in. Lead inspected both helpers and the production template's
sibling containers. Expected text, guard/revision/rerender assertions and runtime
behavior remain unchanged. This repairs the source-proven wrong container;
the real failed run remains7passed/1failed/10notrun with guest trace unavailable.

Complete API series remains exact A9415cf2855a3f9caef6ab68dc7df8405ed9f3ef8 and
amended B006454821ee35b291def4bfafee19cd0553bc7b2 over unchanged097226b. A is the
same Git object. API/WebUI runtime/runner trees and lock graph are equal. Node
syntax/exact-delta checks and mandatory hooks passed; actual API shell derivation
comparison is retained in notification/reuse.json. Existing runtime evidence is
retained for its recorded effective inputs, not claimed as new execution.

Final KB17d06c8bcd5a645601898316acf722708c6defc8 overce2 remains one consolidated
five-file pin commit. Lead independently parsed before/after lock graphs and
capture data: only selected vpsadmin node/revision changes; unrelated nodes,
root/follows/input edges and capture provenance equal. ExplicitOS6bdf is preserved.
No migrations, product/public-contract change, obsolete history or repeated pin
stream introduced. This narrow assertion correction fits the existing reviewed
test contract; direct inspection/quick checks under the narrow-fix rule suffice.
Strict final pin check and legacy retry on006454 are released; no unchanged long
API/client/modern repeats or optional diagnostics subsystem.
