# M8 CI correction: final affected-lane review packet

All intended corrections are committed, focused checks pass, and the feature is
consolidated into three commits. Review the completed verification delta before
remaining long integration checks. This is a related affected-lane review under
mandatory-change-review step10, not another full product review.

## Exact source and lineage

Session `2026-10-27-api-documentation-redesign`, workspace
`/home/aither/workspace/ai/vpsfree.cz`; HaveAPI worktree
`worktrees/2026-10-27-api-documentation-redesign/haveapi`.
Branch `2026-10-27-api-documentation-redesign`, SSH origin
`git@github.com:vpsfreecz/haveapi.git`.

Current clean final head `5114746f3a9f87e91c704147c0d99dd4f0d32f02`, tree
`5b9c52d0f0d81957bbca227d254e2e5b09b53373`, base
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`.

| Complete final series | Commit |
| --- | --- |
| Core | `9508921c21449c7cce45b1ed13b6efab8975b529` |
| Optional OAuth | `bdff6c399886a1743d4e1b694cf0b81906eebe73` |
| Performance | `5114746f3a9f87e91c704147c0d99dd4f0d32f02` |

Original full four-lane/history review: f6..b869, saved in
`milestone8-final-review.md`. Its only Important R3 was fixed by the requested
renderer-specific correction and main direct verification, folded into e5ea.
That source passed all assigned native browser coverage, both installed36-program
matrices and actual CI allclient214/0/scaling. Their exact source labels remain.

Review delta: published `e5ea07028e48a6936b947c172fa89eca15e3a416` to current511.
Exactly eight test, contributor-doc and verification-wiring paths, +71/-56.
The full final f6 range is147paths,+11464/-1271; native tracked count908.
Accepted correction sidecars1cec and73c are outside final ancestry and retained.
Their final tree equals511 exactly. Main independently checked empty73c→511
diff and identical f6 aggregate SHA256
`73306702233e552096108812d94e1bae723663115088c6ac8df01b62c38da458`.
All three original feature messages remain verbatim. Each old e5ea-era group to
new group differs by the same eight-path patch. Fold evidence, full series,
range-diff and147-path inventory:
`history-m8-ci-fold-20261029t002925z/receipt.md` and adjacent records.

No migrations, persisted formats, dependency/channel/input/version update streams,
public runtime/API/schema/provider/config changes. Independently verify this
bounded claim and the unchanged history disposition. Exact d67 durable remote
recovery and e5ea/24ec/other local recoveries remain; no nonancestor is relabelled.

## Requested correction and acceptance

Actual e5ea CI exposed three verification failures; retain their raw logs in
`verification/current-CI-e5ea/` rather than treating an unexplained retry as proof.

- Server/reference headings: Ruby now supports both details on overview/resource;
  the empty directory still needs Simple fallback. Change only the stale specific
  expectation, retaining actual group/page-union and unique-anchor assertions.
- Mounted dynamic fixture: replace obsolete fixture-user/password/code/token
  inputs with the implemented public literals in real Rack requests and JS replay.
  Require envelope status:true alongside HTTP200. Keep mount paths, methods,
  challenge/discovery, nested values, request counts and error assertions.
- Rust: a real-Rack literal/provider assertion had been placed in quick units,
  before CI prepares its frozen server bundle. Bundler failed before any request.
  Move that intact case into existing integration/fixture_actions_spec.rb; only
  the relative fixture path changes. Keep its normal/documentation modes, Basic
  and invalid-Basic checks, discovered token issuance/authentication, OAuth valid/
  arbitrary outcomes and isolated frozen child environment. Preserve the existing
  first fixture-action case. Wire both existing full-check entry points after
  preparation and before the unchanged protocol runner; keep quick units free of
  server dependencies. Clarify those commands in the two owning contributor docs.

Design: final `design.md` section “M8 Rust CI correction — prepared fixture
contract boundary”. Earlier server preparation was rejected because it would
expand the documented quick-unit prerequisite. No skip, fallback, new harness,
lock/platform relaxation, fixture/provider implementation or action-ref update.

Changed paths:

- `.github/workflows/clients-rust.yml`
- `Makefile`
- `clients/rust/docs/development.md`
- `clients/rust/spec/integration/README.md`
- `clients/rust/spec/integration/fixture_actions_spec.rb`
- `clients/rust/spec/unit/documentation_harness_spec.rb`
- `servers/ruby/spec/client_examples/dynamic_mounted_paths_spec.rb`
- `servers/ruby/spec/documentation/reference_headings_spec.rb`

These are the actual consumer surfaces: the Rust workflow, full Makefile target,
Rust component quick-unit target and documented developer commands. Production
renderers/server/client libraries, templates/assets, fixtures, generated program
inputs and runtime/lock inputs are byte-identical to e5ea. All900 other tracked
paths/modes and2148 protected inputs match. Shared packaged-doc11 inputs are
unchanged; changed component contributor docs do not require make-doc copying.
Assess ownership and coverage preservation independently, not from path names.

## Checks and review selection

Evidence: `verification/m8-server-ci-remediation/receipt.md` and
`verification/milestone8-rust-ci-correction/receipt.md`.
Actual focused server2files6/0 seed8028, lint2; Rust unit161/0 and prepared
fixture2/0 seed50232, lint2. YAML, exact moved block/retained case, preparation/
execution order/fail-fast and unchanged quick target checks pass. All ordinary
mandatory hooks pass on sidecars and the consolidated three commits. Exact-final
packaging/profile10/0 seed50232 passes once7.225s. No new compiler, wire, MSRV,
installed, browser or measurement run is claimed for these correction commits.
Old Core/Optional smokes retain exact execution labels and scoped input equality.

Risk MEDIUM for this verification-only delta. Applicable lanes: general,
architecture/repetition and scope/proportionality. The original HIGH-risk product/
auth compatibility review remains; no production auth/state/protocol boundary
changes here, so rerunning its unaffected risk lane is not requested. Report a
concrete serious issue from any lane if encountered.

Selected retained reviewer0, purpose review, ready/independent/read_only,
saved gpt-6.1-sol/xhigh, thread01a18193-44f5-7741-8b6e-6893a0e7f14d. No override
or fallback. Read the skill and all three selected lane references, applicable
workspace/repository procedures and the actual committed delta/context. Review
directly without nested agents. Read-only Git/evidence inspection only; no tests,
network, source/Git mutation, service/provider/peer or lifecycle operation.

Return exact reviewed range/model/effort and ordered Blocking/Important/Advisory
findings, distinct lane conclusions and remaining gaps. Explicitly assess intact
coverage, correct entry points/frozen prerequisites, documentation, narrow scope
and folding into Core without obsolete history/migration/update-stream changes.
No rubber stamp or broader acceptance claim. Main saves the returned report.

After reconciliation: exact-final publication/HTTP identity and scoped evidence
rebinding, then uncovered Go/TS wire, Rust development/MSRV, supplemental encoder,
package and single directf6-to-final performance acceptance. Peer owns the
authorized dev-cluster deployment and real HTTPS/OAuth acceptance; no release,
production or default integration authorization is added.
