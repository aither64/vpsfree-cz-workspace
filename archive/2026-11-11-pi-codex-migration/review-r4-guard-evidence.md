# REVIEW-R4-GUARD evidence

## REVIEW-R4-PUBLICATION: source capability declaration

The separately assigned final declaration is committed at
**`e6717177df3ccdd9846a84ef48d0e3cbc917a4c8`**, exact accepted caller parent
`c2200b9c4ecee9a1f954fc8fef0f0b2777b1c1cf`, tree
`48a7e41f2dd8a88dc6a93ac201c1c0f1e742e974`.
This publishes source capability only. Installed usability, activation, full TEAM
and native3 support are not claimed. Earlier guard and producer receipts below
retain their historical scopes and have not been rewritten.

New isolated worktree/branch:
`worktrees/2026-11-11-pi-codex-migration/dev-workspace-review-role-publication`,
`2026-11-11-pi-codex-migration-review-role-publication`.
It was registered from exact c220 with no fetch. The original f83 guard and owner2
caller worktrees/branches were preserved. Binding/current/environment and retained
Sol/xhigh/workspace_write were verified before work.

Exactly two existing files changed, 20 additions:

| Path | Final source SHA256 |
| --- | --- |
| `portal/internal/session/runtime-contract.json` | `c539c2d28e3b226eb367bdedcf03b1b2c0db4a62823cbef92aa33bec41e2697b` |
| `portal/internal/session/pi_role_instructions_contract_test.go` | `fd3f844042871d9abd0482bb54d0a9a5cf13ecfd867b98feb69f77014a022fb5` |

Metadata gains only exact top-level Integer1 `piRoleInstructions`; every previous
JSON key/value is unchanged and the native-routing marker remains absent. The
minimal test compares actual source bytes with go:embed and runs the owning
whole-metadata role decoder, comparing its workflow selection and version with
the owning complete workflow decoder. Existing strict refusal tests remain.
No other API, version, pin, docs or packaging source changed.

The unchanged packaging step at `nix/workspace-portal.nix:437-438` uses
`install -Dm644` to copy `portal/internal/session/runtime-contract.json` directly
to `$out/share/workspace-portal/runtime-contract.json`. This records the source
copy path; this package ran no build or installed-copy/activation check.

Focused command from the new isolated worktree:

```sh
nix develop /nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv \
  --command go -C portal test -mod=readonly ./internal/session \
  -run '^(TestDecodePi(RoleInstructions|Workflow)Contract|TestPi(RoleInstructions|Workflow)ContractMatchesRuntimeMetadataSource)' \
  -count=1
```

Result: terminal exit0, owning package **0.077s**; source/embedded role and workflow
tests passed. Changed Go gofmt and whitespace checks passed. No SDK, full package,
Ruby, VM, old CI, build, service or native operation ran for this declaration.
Check session81985 and worktree registration session95045 are terminal; all exec
cells/commit effects are joined. Existing accepted application, inventory,
actual-old-target and original-input/recovery evidence is reused only within
the scopes of the linked owner packets, without repeating their checks.

Normal cached Nix `git commit -F` used temporary message
`/tmp/review-r4-publication-8a8gzz2n` without bypass. No hook framework or active
non-sample hook was declared/present. Exactly two staged hashes matched final
source; committed/current hashes match them too. The entire new worktree is clean
and index empty. Its isolated index window was released immediately, before this
evidence refresh, report `66548357-2917-4ed0-acda-865eabf304c4`.

Source manifest [tmp/review-r4-publication-source-sha256.txt](tmp/review-r4-publication-source-sha256.txt)
SHA256 `eaec0d07b8449e29172f344f6fa485c12eb4ea2f6a5af7a01e84d12ae0547652`;
[ordinary commit receipt](tmp/review-r4-publication-commit-receipt.json) SHA256
`6bf0624312d15cca9cb4cc08832aa912bf9868af374a3e52df6a09b903f37a0b`.

### Complete coherent R4 review handoff

Reviewed R is `cd5fd5cbc9670311d411466de8ec63ff670d53b0`; final source head is
`e6717177df3ccdd9846a84ef48d0e3cbc917a4c8`. The complete seven-commit range
contains 29 changed files, 2137 additions/142 deletions. The exact full-hash
[series](tmp/review-r4-complete-series.txt), [diffstat](tmp/review-r4-complete-diffstat.txt)
and [final complete diff](tmp/review-r4-complete.diff) are saved for the independent
reviewer. Diff SHA256:
`1230dcb7eb6b2c7da6b8021eae2df5626e439a9b9083fac310f108ede9968c26`.

| In-branch commit | Purpose and existing evidence |
| --- | --- |
| `1205321e` | Independent strict whole-metadata decoder; original checkpoint below. |
| `c8b647b5` | Exact accepted8c16 owning immutable codec and same-worker application adoption; [P3 packet](p3i-review-instructions-evidence.md), [receipt](tmp/p3i-r4-commit-receipt.json). |
| `f83b9f94` | Complete inventory/target guard and actual prior-R/pre-Pi refusal; full guard packet below. |
| `7324702a` | Accepted602d verified CreationProof digest adoption needed for incomplete recovery; [P3 successor receipt](tmp/p3i-r4-proof-commit-receipt.json). |
| `e6eb8d28` | Accepted R2 supported-roster refusal adoption; [R2 evidence](p2central-workflow-evidence.md#review-r2-supported-creation-roster). |
| `c2200b9c` | Accepted first-create and incomplete-recovery caller, original input/goal proof; [exact caller receipt and check provenance](tmp/review-r4-p2-commit-receipt.json). |
| `e6717177` | This last source capability declaration and actual/embedded decoder check. |

The logical series adds the decoder, owning application, complete guard, required
typed recovery proof, independent roster refusal, matching caller and final
declaration. It contains no dependency-pin stream or superseded alternative
implementation identified for consolidation. Whole-branch independent history
and migration conclusions remain the reviewer's responsibility; no review or
integration approval is inferred from this source checkpoint.

No database migrations exist in this correction. Retained schema2 gains optional
immutable Instructions presence: omitted legacy fields retain old behavior;
present nonempty fields require matching readers and unsupported old readers
refuse, as proven in the actual prior-R packet. No data conversion, deletion,
normalization, Goal/receipt rewrite or retrofit is introduced. Inherited reviewed-R
schema transitions remain unchanged. No package from this declaration was pushed,
deployed or activated, and no migration is externally consumed by this package.

Ready for lead acceptance and whole-R4 independent review sequencing. Fix ownership
is retained through review; capacity is available after acceptance, no next package
is queued. Session remains open, with no lifecycle action, push or new CI.

## Resumed full guard checkpoint

Full dependent source is committed at
`f83b9f94acfa3aaee5862f401103944f7cb5f8d2` over
`c8b647b55ce47d9121dadcd0b3201a9e336c14e7`. Lead's direct writing/error pass
is closed. The independent decoder checkpoint below remains unchanged.
No capability metadata is published and no production writer is enabled.

Lead accepted owner1 prerequisite `8c16a2865e8ef73aeed6789b72ec99150783c093`
over frozen R. Its receipt SHA256 is
`b06c8a1932f05636ffb5fcae0e04b89957c9e031d8ae2edadaf9556ef857997f`.
The exact commit was cherry-picked without conflict after decoder `1205321e`
as **`c8b647b55ce47d9121dadcd0b3201a9e336c14e7`**. All nine adopted file hashes
match the accepted owning commit and both independent decoder hashes remain
unchanged. Native d3/234 and primary R/C checkouts/refs were not used or changed.

The dependent change owns exactly ten existing paths (256 additions/20 deletions):

- `portal/internal/piruntime/retained_conversation_inspection.go` and its test.
- `portal/cmd/workspace-portal/pi_workflow_preflight.go` and its test.
- `libexec/workspace-session-backends.rb` and `libexec/workspace-host`.
- `test/workspace_session_backends_test.rb`.
- `test/workspace_host/provider_sessions_test.rb`.
- `test/support/pi_team_preflight_driver.rb`.
- Only the Retained workflow compatibility subsection of `docs/pi-questions.md`.

`HasInstructions` is derived after the owning private decode, explicit 1/2
whitelist, full validator and exact path/subject checks. Each mapping is counted
once. Schema2 retains its independent `tool_policy` claim; nonempty instructions
add `role_instructions` using the same mapping-path SHA256 and full member,
incarnation, native ID and original 64hex creation receipt, including the lead.
Both claims consume the unchanged output budget. No instruction text/content
digest, parser, output schema, store, worker or history operation was added.

Ruby recognizes the new source and applies the existing full-member special
validation and original schema4 journal/request/completion joins after cache and
binding retirement. Missing or unfinished original provenance refuses the whole
transition. After all claims validate, the host additionally requires scalar
Integer1 `piRoleInstructions` and the complete six-field workflow contract from
the bounded strict target reader. Existing base/team contracts, limits, helper
argv, timeout/join, retirement and recovery behavior remain unchanged. Metadata
publication remains owner0's later package; P2's writer transport and matching
whole-R4 review remain separate.

### Focused evidence and input provenance

All checks used cached declared shell
`/nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv`; Go used explicit
`-mod=readonly`. The current source is frozen committed R + the two-file decoder
+ exact accepted codec9 + these ten owning overlays; no dirty peer source is a
dependency.

| Scope | Result |
| --- | --- |
| Owning `TestInspectRetainedConversations…` | PASS 0.732s, old field-free plus new cold/held/pending/loaded instructions and retained refusal cases. Final explicit empty/null fixture was strengthened to valid schema2 policy mappings and passed narrowly in 0.066s. |
| `TestPiWorkflowMapping…` | PASS 0.059s, independent claims, full lead/member tuple, one record count, output budget and 1/3 refusal. |
| `ruby test/workspace_session_backends_test.rb` | 10 tests/268 assertions, PASS 0.230s; final original-fence pending-state correction separately passed 1/12 in 0.050s. |
| Aggregate host entry, exact target-support test | 1 test/111 assertions, PASS 0.185s. |
| Actual built current scanner + actual Ruby, including actual prior-R reader/target | 1 test/93 assertions, PASS 2.595s. |
| Complete actual pre-Pi6587 stable and `--from-candidate` | 1 test/27 assertions, PASS 0.079s. |
| Syntax/format/whitespace | All five changed Ruby files syntax OK, changed Go gofmt clean, diff check clean. |

Final actual command and output:
`tmp/review-r4-guard-actual-command.sh` and
`tmp/review-r4-guard-actual-final.log`. It runs the existing driver twice with
the actual built current scanner, exact prior-R metadata/CLI and complete
pre-Pi harness; no new parser or harness substitutes for them. Both builds use
`go build -mod=readonly -buildvcs=false` and output outside the source checkout.
The archive has no Git worktree, hence disabled binary VCS stamping; every
original source blob is independently bound to its exact Git revision instead.

Actual frozen-R `cd5fd5cbc9670311d411466de8ec63ff670d53b0` archive has all
**1002** tracked blobs verified before and after tests; actual pre-Pi
`6587c4c1cedabee95bcc52f4667e7d33e3a82859` has all **739**. The prior owning
CLI refuses a new instruction key with its real `Pi runtime scope mismatch`;
the upgraded host refuses exact prior metadata for missing instruction support.
Removing only the new field restores legacy acceptance by both actual old CLI
and upgraded preflight. Current instruction-bearing cold/held/pending mappings
retain both claims after cache/binding retirement. Empty/null keys, bad/missing/
float capability and each missing original proof refuse. Original ready
journal/request/completion and mapping bytes are preserved on refusal; no profile,
quiesce/configure, lock, native worker/model or repair effect occurs. The complete
pre-Pi original journal refuses both entry points before it can call the scanner.

Input receipts:

- `tmp/review-r4-guard-proof-inputs.json` SHA256
  `54eac12d69aa908749ee76a804d5ce31b181d08957cba24b8f5aa79541c9fb5a`
  binds both exact archives and the full current build source graph.
- `tmp/review-r4-guard-final-inputs.json` SHA256
  `65f39328fdbeb210f4ee7418a71b575635c5ca4b9aba58be5592b3caf1f51bdd`
  reconciles the final tests. Only the retained inspection test and existing
  Ruby driver changed after the successful CLI builds; both passed in their
  final affected checks. Every production build input stayed byte-identical.
- `tmp/review-r4-guard-final-source-sha256.txt`, own12 including decoder2,
  final SHA256
  `e7b8cf3f9f259bb738e4f3df36e02c0043f7e54164223a41650a2dce7115e597`.
  Prior checked manifest `eb375ae9` is retained in the source/check report.
  The only later change was lead's grammar edit to explicit empty/null refusal.
  Final doc SHA256 is
  `08c9f8ac4f57aeda4a50176308200e5c0e8bbb9f54c8d0192545644b0d4a16ea`.
- `tmp/review-r4-guard-commit-inputs.json` SHA256
  `3cb74a1dee9bf34c4ecb74d55d0e5e17d095c6f4185e74852253cdad2f0d6e22`
  binds that prose-only refresh to the unchanged checked source graph.

Initial bounded attempts exposed fixture/environment assumptions, without a
production fix: old archive VCS stamping, UTF8-vs-binread assertion encoding,
and expecting a generic diagnostic rather than the actual old owning ErrScope.
The scanner-order fixture assumed insertion order despite the established
sorted result; the provider shard was first invoked outside its owning aggregate
TransitionHost setup. Only affected checks were repeated. Build artifacts were
reused after test-only corrections; no unchanged SDK, VM, broad suite or full
integration was rerun. Failure logs remain under `tmp/review-r4-guard-*`.

Uncertain build/driver attempts used fresh GPT-6 Luna/low native-only watchers
resolved from installed package
`/nix/store/0s5dljmmfngj7ia2r9lfkxwydnfiz6b6-dev-workspace-0.2.0`, catalog
`f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`,
full_access/danger-full-access/never; matching utility
`dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569`. All watcher cells/tool
sessions are terminal (76861/44062, 29267, 68830). Final known-cheap corrected
driver batch was parent-owned, terminal0/session81683. Earlier inline quick
sessions84635/15873/29376/83873/87670/75087 are terminal as well. No process,
claim, service or native operation remains owned by these checks. Session stays
open. No migration, push, merge, package switch or lifecycle action occurred.

### Final commit and handover

Lead read the 14 new compatibility lines and target gate/error, corrected only
the grammar of explicit empty/null refusal, and approved the error unchanged.
No logic or behavioral test input changed; no unchanged test rerun was required.

Fresh session/current and environment matched the trusted binding before commit.
All other owned hashes, adopted P3nine and decoder2 were reverified exactly;
gofmt and whitespace checks passed. Exactly the ten dirty owning paths were
staged and their index hashes matched the final manifest. Normal cached Nix
`git commit -F` used a temporary message file without bypass. No hook framework
or active non-sample hook is declared/present.

Actual completed head: `f83b9f94acfa3aaee5862f401103944f7cb5f8d2`.
Exact parent: `c8b647b55ce47d9121dadcd0b3201a9e336c14e7`.
Subject: `session: guard retained role instruction mappings`.
Commit inventory is exactly ten existing files, 256 additions/20 deletions;
all own12 committed/current hashes equal the approved manifest. The entire
worktree is clean and index empty; adopted P3nine still match accepted8c16.
Receipt `tmp/review-r4-guard-commit-receipt.json` SHA256
`a294ccb7b33f2797f487b049085d48caab6c513f0328fded6695ce193e13f9b7`.
The short isolated index window was released before this evidence refresh via
report `2711fa86-21e8-4650-9c05-cc71fda6b799`.

Complete branch range from exact R is three logical commits: independent decoder
`1205321e`, byte-exact accepted codec adoption `c8b647b5` (original8c16), then
guard `f83b9f94`. No superseded dependency pin, history rewrite, database migration,
state rewrite, published/deployed migration or externally consumed format change
was introduced by this source checkpoint. Old omitted mappings remain supported;
new instruction-bearing schema2 intentionally refuses unsupported downgrade.
Whole-R4 independent review remains lead-owned after matching P2/producer/metadata
evidence; this checkpoint does not claim that review or integration readiness.

The separately released P3 CreationProof digest producer successor is not a
dependency here. No provisional field or native branch was imported. Lead will
compose that successor with this guard for P2 recovery. This full guard package
is reported for acceptance; fixes remain retained and capacity is available
after acceptance, with no second package queued. No resources/processes remain
owned by checks, and no lifecycle action is requested.

## Historical independent decoder checkpoint

Independent decoder milestone is committed at
`1205321e73938b40440c85e62216380422b75f46` over exact frozen R
`cd5fd5cbc9670311d411466de8ec63ff670d53b0`. The rest of this same package is
held for lead acceptance of owner1's owning instruction codec.
Lead's current clarification parks that dependency behind the retained native
N1+N2 settlement corrections. No instruction projection, scanner, Ruby, producer or
native source changes have been made here.

## Source and ownership

- Session: `2026-11-11-pi-codex-migration`; `dev-session current` matched the
  trusted binding. Both session environment variables were absent.
- Retained roster: implementer3, `gpt-6.1-sol`, xhigh, workspace_write.
- Worktree: `worktrees/2026-11-11-pi-codex-migration/dev-workspace-review-instruction-guards`.
- Branch: `2026-11-11-pi-codex-migration-review-instruction-guards`.
- Exact parent: `cd5fd5cbc9670311d411466de8ec63ff670d53b0` (frozen R).
- Exact completed head: `1205321e73938b40440c85e62216380422b75f46`.
- Exact committed inventory: the two new files below, 155 additions. At the check,
  every tracked file matched committed R and only these two files were untracked.
  The check therefore used committed R plus only this two-file overlay; no native
  or central work in progress was a dependency. After commit, the entire worktree
  is clean and index empty; committed and current hashes match the reviewed and
  checked bytes below.

| New path under the worktree | SHA256 |
| --- | --- |
| `portal/internal/session/pi_role_instructions_contract.go` | `3bebde90e6f80b0e7b4cfa64ac3e1161222a2839b4a087d3fac4cbc6cf2aff6d` |
| `portal/internal/session/pi_role_instructions_contract_test.go` | `b213ea91dc00da554b11a3a90594a421f7d36950d98498a5eb988f088eedec16` |

## Implementation and check

`DecodePiRoleInstructionsContract([]byte) (PiRoleInstructionsContract, error)`
returns detached `{Workflow PiWorkflowContract; Version int}`. It first calls
the unchanged owning whole-metadata `DecodePiWorkflowContract`, then the existing
strict `DecodePiCreationJSON` for exact integer `piRoleInstructions: 1`.
Unrelated top-level metadata is permitted. Every error returns an empty selection.
Metadata declares support; this function grants no write permission or worker
application proof. Nearby technical comments document that boundary; no product
documentation or producer change is useful for this independent milestone.

Both gofmt and the following focused check ran in the declared cached Nix shell
from the isolated worktree:

```sh
nix develop /nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv \
  --command go -C portal test -mod=readonly ./internal/session \
  -run '^TestDecodePiRoleInstructionsContract' -count=1
```

Result: terminal exit 0, owning session package `ok` in **0.059s**. Tests prove
the full six-field prerequisite bundle, every missing field, scalar/type/null/
float/exponent/value refusals, exact nested tool-policy map, duplicate and escaped
duplicate names, wrong casing, malformed/trailing/invalid UTF-8 metadata, role-only
or native-plus-role-only refusal, detached result and unchanged input, exact
65536-byte acceptance and 65537-byte refusal. New-file whitespace checks printed
no diagnostics; their no-index difference status is expected for new files.
No broad suite or unchanged behavioral rerun was run. Before staging, Nix gofmt
verification printed no paths and `git diff --cached --check` passed after staging.
The one Go test process is terminal; no watcher, native
worker, model, service or external operation was launched.

## Remaining dependency and review

Await lead's accepted exact owner1 codec commit handover before deriving
`HasInstructions` or editing the scanner/Ruby path. Owner1 alone owns Instructions
presence/empty/null/schema2 validation, immutable replay/load and same-worker
application acknowledgement. No parser workaround or untested field dependency
is present here. Native schema3 stays outside this package.

The full package still owes the canonical actual scanner-to-Ruby/original schema4
fence, old R reader/target refusal and complete pre-Pi stable/from-candidate
fixtures after that codec handover. Runtime metadata publication remains owner0's
later package. This milestone does not claim those checks, installation or live
readiness. Lead directly read the source/comments/error and approved the main
writing/error pass unchanged before commit. Independent final review belongs to
lead after the complete intended source is committed and quick checks pass.

The isolated ordinary commit used the same cached Nix environment and a temporary
message file with `git commit -F`, without bypass. This repository declares no
hook framework and has no installed non-sample hooks. The completed receipt and
post-commit inspection verified the exact full parent/head, exact two new paths,
155 additions, frozen committed/current hashes, clean worktree and empty index.
The short isolated index window was released to lead immediately, before this
outside-index evidence refresh (report ID
`0a630aa2-5d67-4505-8ceb-b66404a7b251`). Full guard ownership remains retained;
the dependency hold does not complete the package or free capacity for a second.
No history rewrite, migration, push, merge, profile switch or lifecycle action
occurred.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/)
