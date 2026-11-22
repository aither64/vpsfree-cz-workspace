# P4 native empty-category correction

Owner: implementer5, retained Sol/xhigh/workspace_write, verified current/env and
own roster. Previous SDK package accepted at
`aec5bea24c6a1bf18dd5c7941617286c869e4c7d`; this is the sole executing package.
Committed for acceptance at `699d8f85b20b89772fbcb4d49ecccfb6d24b8f75`;
exclusive index window closed and released. No active command, other executing/
parked package or queued next package. Capacity available with P4 fixes retained.

Base: `7e6229da4745db05484864107c03a9c72ab06dfc` in the registered D feature
worktree. Only `portal/internal/piproviders/native.go` (+3) and `native_test.go`
(+58) changed. No SDK/core/types/central/metadata/format/docs edits.

## Hash coverage and correction

`resolve.go:policyBytes` is the existing sole digest encoding: fixed arrays of
schema, catalog digest, source/revision, complete resolved native chain, budget,
and sorted categories. Its `append([]FailureCategory{}, ...)` already produces
canonical `[]` categories for both nil and empty originating selections.
`CompileNativePolicy` copies that existing digest and settings; exported-Go
`NativeRoutingPolicy` object wire bytes are not the originating digest encoding.

The compiler now allocates a detached nonnil `[]string` before converting
categories. This corrects only the explicit virtual projection from null to [];
it changes no covered digest bytes, digest recipe, original policy, chain,
settings, revisions or Resolve provenance. Empty categories permit no retry hop;
they do not select physical mode. Existing P4/data-only nil semantics remain;
strict P3 virtual null refusal is untouched. A nearby technical comment records
why the allocation belongs here; no new visible prose was necessary.

## Focused source proof

Created `/tmp/p4-native-empty.MWkGBb` using `git archive` of the exact base, then
copied only the two owned files over it. Full tracked-blob comparison of 992
files verified precisely those two differences, and their bytes equal the source
hashes below. Uncommitted peer runtime/central/producer files were excluded.

Red regression, with the original compiler and new actual Resolve test:

```sh
nix develop /nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv --command \
  sh -c 'cd "$1/portal" && go test -mod=readonly ./internal/piproviders -run "^TestCompileNativePolicyEmptyCategoriesPreserveIntentAndWireArray$" -count=1' \
  sh /tmp/p4-native-empty.MWkGBb
```

Exit1, package 0.015s: reproduced exact exported-Go `"FallbackOn":null`.
This was the expected original-source failure, not a passing boundary proof.

Green regression and relevant existing owning cases, after the allocation:

```sh
nix develop /nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv --command \
  sh -c 'cd "$1/portal" && go test -mod=readonly ./internal/piproviders -run "^(TestCompileNativePolicy|TestPlanNativeRetryStopsDisabledNonretryableCancelledOrExhausted|TestResolutionOverrideClearAndDigest)" -count=1' \
  sh /tmp/p4-native-empty.MWkGBb
```

Exit0, package 0.031s. The regression starts with actual nil and allocated-empty
originating category selections, obtains intact `Resolve` provenance, compiles
the full canonical chain, and verifies exact `FallbackOn:[]` wire bytes. Certified
retry evidence returns `stop/fallback_disabled`, nil target and unchanged zero
counters. Full targets/settings/digests/budgets remain unchanged; mutation of one
compiled copy cannot alter a second compilation, source policy, canonical hash
input or private Resolve proof. Existing nonempty compilation, disabled data-only
planner and digest fixture cases pass unchanged. `gofmt` and owned whitespace
checks pass. Both known quick operations completed; no active process/watcher.

| Owned file | SHA-256 |
| --- | --- |
| `portal/internal/piproviders/native.go` | `9dcb604f2a48718fbdec4adb2db03f2ca6f4d7a7fc681f4aac780742a2ce13d6` |
| `portal/internal/piproviders/native_test.go` | `33476254dbcc2baebf9f35a1f26c355c96a6b9ba0a2faeb1fa8fdbac8334c506` |

## Remaining boundaries

No SDK/model/provider/long check or new harness ran. No real credentials or
native session data were read or written. Core empty virtual remains unavailable
until this actual compiler output is consumed and proved through the separate
leaf/core/schema3/writer/transport/guards integration. Production original
SubmissionRef/Accepted/current generation/original lifetime/effect/physical-route
proof remains mandatory. This package supplies none of that authority and
activates nothing. No database migration, schema conversion, deployment, push or
lifecycle action. Combined whole-branch history/review remains lead-owned.

## Final commit receipt

Parent `7e6229da4745db05484864107c03a9c72ab06dfc`, head
`699d8f85b20b89772fbcb4d49ecccfb6d24b8f75`. Exact inventory: modified only
`portal/internal/piproviders/native.go` and `native_test.go`, 61 insertions.
Staged, committed and current SHA-256 match the table above. Fresh session/env,
retained Sol/xhigh/workspace_write, feature branch, exact parent and empty index
were verified before mutation. Cached declared D Nix ran normal `git commit -F`
with a temporary message file; no hooks were bypassed, no peer content staged.
The command completed exit0; index empty and owned two paths clean afterward.
Window released immediately in report `bedbff92-1f00-4989-8016-cb35ad810b4f`
before this evidence refresh. No unchanged test rerun or SDK check.

The red original-source and green corrected-source results above bind the exact
now-committed bytes. No database/on-disk schema migration, conversion or external
consumer state was changed; this is one logical narrow compiler correction.
Separate full integration/consumption and final review gates remain required.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
