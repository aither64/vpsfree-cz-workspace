# Go query assertions: final independent review

**No Blocking, Important or Advisory findings.** The general, architecture/
repetition and scope/proportionality lanes pass for this completed harness
correction. Full final-head Go execution, artifacts and CI remain verification
gaps; the earlier failed run remains failed.

## Identity and scope

- Verified session `2026-10-22-haveapi-release` in workspace
  `/home/aither/workspace/ai/vpsfree.cz` using `dev-session current`; both identity
  environment variables are absent, consistent with the trusted thread binding.
- Retained independent `reviewer0`, review purpose, ready in live roster revision
  34; thread `01a16406-faaa-7cd0-bde3-c20802c18a72`, project
  `01a16406-fa76-7532-9ee4-a890352500df`.
- Actual retained settings: `gpt-6.1-sol` / `xhigh` / `read_only`, with no
  override, fallback, nested agents or substantive authorship.
- HaveAPI worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi`.
- Full reviewed range: `a32b15e379f44fc6dae4b15ef4ec17a142e5f465` →
  **`b64fb25bea8d8222fb3263b99956c0b61438a859`**, tree
  **`05384a632290653cb4560c7451b3897acd5956c8`**.
- Reviewed predecessor: `ee67d27419c48d27a01c83a29114adf9a82062ba`;
  [prior wire review](go-wire-final-review.md) remains unchanged.

Applied mandatory-change-review, Shared Reviewer Instructions and the full
general, architecture and scope references. Reused unchanged required workspace/
HaveAPI procedures read in this context. Inspected the new packet, receipts,
diagnosis, actual source delta, template/transport chain, pure controls, complete
history mapping, streams and input evidence. Earlier high-risk product reviews
are retained through exact unchanged inputs. This low-risk two-file test delta
does not introduce a new product/authentication/URL/schema contract.

## Affected-lane assessment

**General: expectation matches the actual encoder; strict comparison remains.**
In owning commit `47c54cb0`, `clients/go/spec/documentation_acceptance.rb:29`
corrects only the expected false query value to string `"0"`. The existing Go
parameter mapping (`go_client/parameters/typed.rb:33`) selects `bool`;
`template/action.go.erb:564` uses the selected parameter's converter and sends
nullable nil as the empty string. `template/types.go.erb:150` explicitly converts
false/true to `"0"`/`"1"`; integer zero uses decimal formatting. The transport at
`template/request.go.erb:172` adds those values to the request URL and encodes the
query. Expected empty name, zero count and omitted unused field remain intact.

At `documentation_acceptance.rb:228`, the verifier still compares the complete
parsed query hash with its exact expected hash. No coercion, normalization,
key stripping or subset check was added. Body, path, authentication, output,
state-follow-up and unexpected-request assertions retain their earlier behavior.

The new capture at `:194` obtains WEBrick's existing `query_string`. The mismatch
at `:229` reports expected, parsed actual and raw query with `inspect`, helping
distinguish encoding from parser failures. It is confined to this deterministic
local fixture's fixed noncredential query sample. No authentication header,
token or body is added to that diagnostic; no product logger or production
request path changes. The comment accurately describes the existing SDK encoding.

**Architecture/repetition: native parser and the existing verifier own the seam.**
`clients/go/spec/documentation_wire_check.rb:43` supplies one explicit encoded
query and eight mutations. `:56` parses an in-memory real WEBrick request, calls
the actual fixture `serve`, then calls the actual private `verify` against the
shared expected table. Allocation avoids server construction. The negative helper
requires the real mismatch prefix and raw diagnostic payload; unexpected success
or unrelated exceptions cannot pass. The new code does not copy the parser or
comparison rule. Existing seven body positives and 52 body negatives remain.

**Scope/proportionality: bounded test correction.**
The implementation corrects a demonstrated expectation mismatch and adds useful
failure evidence plus focused controls. Eight negatives cover word false, true,
wrong count, word null, each missing field and an extra input field. This is
proportional to the owned assertion; there is no generalized wire compatibility
layer, renderer/SDK capability expansion or new dependency. A nearby comment is
sufficient documentation for a test-only change.

## Full history, streams and migrations

Independently reconstructed all **22** final positions and compared every patch
and message with the reviewed predecessor. First ten hashes are identical;
**21 other raw diffs and stable patch IDs are equal**. Only Go owner position 11
changes (`277c931a` → `47c54cb0`); messages remain equal. The exact semantic delta
is only the two existing harness/checker paths. All 137 final changed paths and
the complete binary diff export match Git; merge base equals the stated base.

Prefold `d4a3b4137e3a80eb5f04a3140a3dd55dc6aa401e` and final have identical trees
and complete binary base-to-head diffs. Whole-range whitespace passes. Final
message is exactly the one-line `Version 0.30.0`, with no body. The three released
maintenance patches still match the stable patch IDs of their referenced
released-source commits and retain `-x` provenance.

History conclusion: no obsolete unmerged approach, fixup-only step, transitional
workaround or unused compatibility path remains. This correction is folded into
its existing owning Go purpose. Separate source, generated, cleanup/diagnostic
and version purposes remain reviewable and retain the prior accepted order.

Repeated-stream conclusion: no new dependency/channel/input/lock/generated
payload stream, and no redundant update remains. One cumulative JS generation
`4ee83c0f` follows both authored JS features. Final shared version metadata
`b64fb25b` is separate and last; its browser-bundle change is only the version
literal. Node test declarations and final package identity are distinct logical
purposes despite sharing a lockfile. Highlighter pin/build/license/bundle, PyPA
action and shared CI action-role updates remain consolidated. No retained
intermediate revision needs a release, consumer or state-boundary exception.
Earlier exact refs and rollout/verification records remain separate provenance.

Migration conclusion: **no migrations**. The complete final history/diff has no
database schema migration, persisted-format conversion or transitional migration.
There is no migration merge/release/deployment/external-use lineage to reconcile.

## Verification and execution boundaries

Reviewer ran the allowed quick pure checker in the declared tools-only root
Nix shell with the explicit existing dedicated bundle:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euc '
  export BUNDLE_GEMFILE="$PWD/clients/go/spec/documentation.Gemfile"
  bundle exec ruby clients/go/spec/documentation_wire_check.rb
'
```

Exit 0: **7 accepted bodies / 52 rejected body mutations; 1 accepted query /
8 rejected query mutations**. No compiler, listener, generation, build, package
installation or long acceptance was started. Owner syntax/style/hooks are
supporting evidence, not relabeled reviewer-run checks.

Independently reconstructed both complete **750-entry** tracked Git trees and
every comparison row: **748 exact mode/type/blob identities unchanged**, only
the two harness blobs differ. Entire product, renderer, fixture schema,
server/JS/Python/Rust/Ruby-client, release/workflow and toolchain sources match.
The baseline inventory SHA-256 matches its receipt. The actual retained ee67
artifact manifest SHA-256 is
`e08a672e7402c483cf1b52df6fc319141bd173535a5e1706668d25a7608041d1`;
its source and tool metadata match the proof. All **nine** live lock hashes were
independently derived from the manifest's saved lock contents and match live files.

Original Rust inventory SHA-256
`538c6330ad3647cf30b1ee2134e5e2594c91701419ae02b4f1b456086a3007f4`
matches. All **310** original mode/type/blob identities and separate
`flake.nix`/`flake.lock` identities match both actual execution head `48543f8c`
and final. Original generated Cargo/source/lock/tool graphs and successful
915.38-second root/mounted, async/blocking, development/MSRV result remain bound
to that actual head. Dynamic successes remain bound to actual `3fb91caf`.
Input equivalence is not literal final-head execution.

The retained ee67 result is **exit 1 after 27.4 seconds**. Log and actual runner
control flow establish artifacts/manifest and compilation of all 16 programs
passed, and execution passed object/empty/omitted/list/failure/association before
the query mismatch. That run retained neither parsed nor raw query. The source
chain and current native constructed controls explain the expectation defect;
they do not recover the actual failed query capture. Owner constructed
operation/state/auth/hostile controls likewise do not establish Go execution.

**Remaining gap:** final-head artifacts/verification, all 16 actual Go programs
through completion, and lead-selected final-head CI. Operation, authenticated
action and hostile cases remain unreached in the last actual run. Preserve all
failed results and exact earlier successful execution labels.

Source/index remained clean at the exact reviewed head; `dist/` remained empty.
Existing unrelated untracked caches were preserved. Only this assigned report
was written. No source/Git/default/tag/registry/deployment/lifecycle action was
performed. Lead owns state reconciliation and subsequent verification; the
session remains open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
