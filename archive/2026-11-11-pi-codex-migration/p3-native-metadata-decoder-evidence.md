# P3 native metadata decoder

Status: exact two-file source committed and accepted by lead at
`329bd4910082d3cfb4d2fe7b04743f0c5e8d4603`; index window closed. H0/P5/guards
and this decoder's fixes remain retained; capacity available, no next package
queued. This decoder does not enable native3.

Bound session `2026-11-11-pi-codex-migration`, workspace
`/home/aither/workspace/ai/vpsfree.cz`, retained implementer3
Sol/xhigh/workspace_write/full-access execution verified before work. Both
DEV_SESSION environment values were absent. D worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace`.
Checked committed parent: `699d8f85b20b89772fbcb4d49ecccfb6d24b8f75`.

## Release, source and invariants

Lead released the independent decoder package from design.md's
“Source-sufficient independent native metadata decoder package”, following
accepted GUARDS `3318ca32392444167c4369ecd8cd17891bdaa4ce` and confirmed capacity.
Architect0's direct clarification agrees with that exact boundary.

Only these two new files are owned:

```text
portal/internal/session/pi_native_routing_contract.go
portal/internal/session/pi_native_routing_contract_test.go
```

Source manifest `p3-native-metadata-decoder-source-sha256.txt` SHA256:
`36644996e61e6fdb96fdf0ba0447d8b491265a97a002d39d950b86a0d5e9062e`.
The two new files contain156 additions, with no existing-file deletion or edit.

Frozen API:

```go
type PiNativeRoutingContract struct {
    Workflow PiWorkflowContract
    Policy int
    RecordSchema int
}
func DecodePiNativeRoutingContract([]byte) (PiNativeRoutingContract, error)
```

The decoder first invokes the actual owning DecodePiWorkflowContract on the same
whole metadata bytes, preserving its64KiB bound and complete exact six-field
prerequisite selection. It selects piNativeRouting using the existing owning
strict JSON helper and requires exactly `{policy:1,recordSchema:3}`. No duplicate
parser or relaxed subobject interpretation is added. The detached return value
is a metadata selection, not a new wire format, live guard result or retained
conversation record. Unrelated top-level metadata remains permitted under the
owning strict JSON rules. Every error returns an empty selection.

No existing workflow source/test file or owner0 producer-fixture hunk changed.
No P3 record parser/export, scanner, Ruby, command, web, metadata or Nix file was
edited. The existing inventory1/2 whitelist still refuses3. Both production
guard injection sites remain unavailable; no consumer registration or support
advertisement follows from this pure decoder.

## Exact source assurance and checks

Owning dependency files pi_workflow_contract.go, pi_creation_selection.go and
backend_binding.go matched their committed parent bytes before the check.
Their hashes are retained in
`p3-native-metadata-decoder-dependencies-sha256.txt`.

The established source-copy method extracted exact committed parent
`699d8f85b20b89772fbcb4d49ecccfb6d24b8f75` and overlaid only these two files at
`/tmp/p3-native-metadata-decoder-893nvvsh`. It excludes all uncommitted native,
central, producer and existing workflow-test work. Source/input receipt:
`p3-native-metadata-decoder-snapshot.json`.

Command ran once from that committed-parent overlay:

```sh
nix develop /nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv --command \
  go -C portal test -mod=readonly ./internal/session \
  -run '^TestDecodePiNativeRoutingContract' -count=1
```

Passed: session package0.060s, exit0. Complete log:
`p3-native-metadata-decoder-check.log`. Known quick focused check ran inline;
no long build, broad suite, native test or new harness was launched. Go formatting
and owned whitespace checks passed. The command is terminal; no own tool session
or process is running. A tool-orchestration syntax error before any command
execution was corrected; no check command was duplicated.

Three focused tests cover positive whole metadata with unrelated top-level
fields; equal detached workflow selection and unchanged input; exactly64KiB
acceptance and overflow refusal; every missing workflow/native prerequisite;
missing nested keys; null, boolean, string, fractional/exponent, negative/zero/
unsupported integer and array/object type refusals; extra workflow/native map
keys; native recordSchema2 refusal; duplicate native/nested/unrelated keys;
case-mismatched exact names; invalid UTF-8, absent/top-level wrong shape and
trailing JSON. Required workflow support cannot be bypassed by a native-only map.

## Documentation, history and remaining gates

Technical comments document the owning whole-metadata contract and lack of live
authority in the new source file. No product document or existing visible wording
needed amendment for this independently inert decoder. Session evidence owns
temporary heads/checks/status. No record/receipt/schema migration, normalization,
converter, cleanup, retirement, default switch, service or ledger is introduced.
No native/model/auth call, profile/lifecycle/deployment, push or merge ran.

Positive all-cold/pending/held schema3 inventory requires owner1's accepted exact
core UnmarshalJSON/validateRetainedNativeRouting/validateConversationRecord
checkpoint, then the separately released export/scanner/Ruby amendment and actual
predecessor proof. Producer/consumer wiring and native functionality remain
separate required work. This package has no dependency on unfinished native core
and makes no production capability or activation claim.

## Final commit and acceptance receipt

Final commit: `329bd4910082d3cfb4d2fe7b04743f0c5e8d4603`.
Exact parent: `699d8f85b20b89772fbcb4d49ecccfb6d24b8f75`.
Subject: `session: decode complete Pi native routing metadata`.
Exactly two new files/156 additions. Staged, committed and current SHA256 values:

```text
52ed757cc6d5eccf1401b94936400504e217d6a18213bfe5bbcdba915adc5948  portal/internal/session/pi_native_routing_contract.go
cf477c4458aac5180cdd81734adaca342c71582ec946b2c2390c736e82012b57  portal/internal/session/pi_native_routing_contract_test.go
```

These match the frozen manifest above. Fresh binding, saved roster, exact parent
and empty index were verified before staging. Normal tempfile `git commit -F`
and exact `--only` paths were used; no declared hook framework or active
executable hook was present and no bypass was used. Owned two paths were clean
and post-index empty. Existing workflow source/test, owner0 producer hunk and all
native/central/metadata peer files were excluded.

Immediate index release report:
`052398d4-3523-4254-a064-f6d3185ab9d5`; raw receipt:
`p3-native-metadata-decoder-commit-receipt.json`. Lead independently verified
the final boundary and accepted the decoder source package. Unchanged clean-
parent0.060s evidence was reused without a test repeat. All own commands are
terminal; no push or lifecycle action followed acceptance.

Known consumers receive the literal landed API only. Positive schema3 inventory
is still blocked on the accepted strict core reader and later explicit release;
no export/scanner/metadata/production consumer injection is granted here. Capacity
and permanent fix ownership are retained, with no next source package queued.
Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
