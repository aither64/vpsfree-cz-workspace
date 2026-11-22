# P7 workflow-contract candidate

Owner: implementer0. **Source support committed**, 2026-11-12:
`d4e15e9d6b36fb2c4f4ff93e4f68a290494e265b` over
`25af2aba72f6f45570cc56d5269c3d9ec44fbbf9`, exactly two files / 29 insertions.
Staged, committed and current hashes match the frozen values below. Index empty
and owned paths clean at immediate window release; native peer WIP preserved.
Normal file-message commit, no active hooks/framework or bypass, push, long
build, native3 declaration, activation or lifecycle action. This is source
support publication only; installed/runtime readiness is not claimed.

Candidate was prepared at accepted guard base
`3318ca32392444167c4369ecd8cd17891bdaa4ce` at 17:55 UTC.
Retained settings: Sol/xhigh/workspace_write; exact session/environment verified.

Final pre-commit assurance is now bound to accepted coherent checkpoint
`25af2aba72f6f45570cc56d5269c3d9ec44fbbf9`: a clean Git archive plus **only
the same two frozen candidate files**, at
`/tmp/2026-11-11-pi-codex-migration-p7-workflow-final/source`. Active native WIP
was excluded. Identity packet: adjacent `identity.json`. The exact-source/embed,
owning strict workflow/negative and retained-team Go cases passed again in that
actual snapshot cwd (`portal/`), **0.050 s**, using the same declared cached Nix
environment and `-mod=readonly`. Command wall time 5.933 s. Terminal output was
inspected before reporting success.

Semantic comparison to **25af** again proves all 46 old fields/values preserved,
exactly the six selected additions, policy1 unchanged and native3 absent. Current
assigned files equal the tested snapshot hashes below; owned whitespace passes
and the index is empty. Owning Go/Ruby consumer files are byte-identical to 3318,
so the earlier 97-assertion Ruby/source-consumer evidence is reused within scope;
no repeated Ruby or long/installed build ran. Lead accepted actual composition/
common-P3 dependencies and the coherent checkpoint, then separately granted
the exact-two-file window used for the recorded commit.

Only two application files change, 29 insertions:

| Candidate file | SHA256 |
| --- | --- |
| `portal/internal/session/runtime-contract.json` | `ce634514f80a365920bc03ae1d31b6bb6cbf5ceac82fcabdf6e55e32a8ce623e` |
| `portal/internal/session/pi_workflow_contract_test.go` | `7fac2fb550e20238b394f91fe074cdebe6957a5a8292b2c54dab9a490b9ab715` |

The metadata adds exactly `piQuestionsSchema:1`, `piPlanSchema:1`,
`piToolPolicy:{policy:1,conversationSchema:2}`, `hostCallbacks:1`,
`linearLineage:1`, `workflowObservations:1`. A comparison to the base proves
all 46 pre-existing top-level fields/values unchanged, including complete
`piTeamRecords`, base/creation contracts and `sessionBackendBindingPolicy:1`.
No `piNativeRouting` declaration or native3 support was added. Old metadata
SHA256 is `e4d867326ec221a070cc7bf57ced23c9c4041216811de3f29aff936d3206ad53`;
its canonical semantic map SHA256 is
`0b6ac6125b89e03ee3ef0a6d1ddde5aaa71cab3087ee9c3c29ab7b51ac2047f6`.

One fixture hunk adds `TestPiWorkflowContractMatchesRuntimeMetadataSource`.
It reads the actual metadata file, compares it byte-for-byte to the Go embedded
metadata, feeds it to owning `DecodePiWorkflowContract`, and checks the existing
team map through owning `DecodePiTeamRecordsContract`/`PiTeamRecords`. It does
not substitute a synthetic expected workflow object. Decoder implementations,
all existing guard fixtures, CLI/Ruby scanners, Nix producer and other manifests
are untouched. No new prose in the application requires a writing pass.

## Quick source/consumer checks

Actual cwd for Go was the assigned D worktree's `portal/`; Ruby and semantic
comparison used that same D worktree root. Tools came from the retained exact
D Nix environment `/nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv`.

```sh
go test -mod=readonly ./internal/session \
  -run '^(TestPiWorkflowContractMatchesRuntimeMetadataSource|TestDecodePiWorkflowContractRequiresCompleteWholeMetadata|TestPiTeamRecordsContractRequiresCompleteExactSupport)$' \
  -count=1 -v
ruby test/workspace_session_backends_test.rb \
  -n test_workflow_contract_requires_complete_exact_bundle
```

Both passed: Go package **0.044 s**; Ruby **1 test / 97 assertions / 0 failures**,
0.059 s. A separate inline Ruby source fixture wrote the exact actual metadata
bytes into a disposable expected package layout and invoked existing
`WorkspaceSessionBackends.require_contract!`, `require_team_contract!` and
`require_workflow_contract!`; all accepted. That is direct consumer evidence on
candidate bytes, **not installation proof**. Scoped `git diff --check` passed.
No Git index mutation, commit, full package build or runtime action occurred.

## Prepared installed-copy verification — pending post-review

The unchanged declared producer in `nix/workspace-portal.nix` installs the source
verbatim at `$out/share/workspace-portal/runtime-contract.json` with `install
-Dm644`. Its normal package check runs the Go fixture through `go test ./...`.
Actual final package realization would be a long build and is not authorized
before mandatory final review. No temporary copy is presented as that proof.

After final source is committed/reviewed and a fresh verification watcher is
assigned, bind `p7_reviewed_source` to the reviewed immutable Nix source root.
The prepared check is the existing `packages.x86_64-linux.dev-workspace` build,
followed by exact source/install comparison and the installed owning consumers:

```sh
nix build --impure --json --print-build-logs \
  --out-link /tmp/2026-11-11-pi-codex-migration-p7-workflow-package \
  --expr "(builtins.getFlake \"path:$p7_reviewed_source\").packages.x86_64-linux.dev-workspace"
p7_package=$(readlink -f /tmp/2026-11-11-pi-codex-migration-p7-workflow-package)
cmp "$p7_reviewed_source/portal/internal/session/runtime-contract.json" \
  "$p7_package/share/workspace-portal/runtime-contract.json"
ruby -r "$p7_package/libexec/workspace-session-backends" -e '
  package = ARGV.fetch(0)
  WorkspaceSessionBackends.require_contract!(package)
  WorkspaceSessionBackends.require_team_contract!(package)
  WorkspaceSessionBackends.require_workflow_contract!(package)
' "$p7_package"
```

Use the declared Nix environment's Ruby; retain actual build JSON/derivation,
immutable source/NAR and package GC root, then positively verify the output
identity before accepting. The final full package's embedded/source fixture,
byte comparison and installed consumers together establish that boundary.
This check is prepared, **not run**. No Nix or application-source edit is needed.

## Publication gate and next dependency

Lead explicitly gates index/commit/advertisement on acceptance of the actual
central composition proof with matching common P3 ports, plus a later named
short window. Actual composition/common-P3 and coherent `25af…` are now accepted;
the exact-two-file window was separately granted and has now closed. Commit
receipt `/tmp/2026-11-11-pi-codex-migration-p7-workflow-commit-receipt.json`
records the complete parent/head/inventory/hash proof. This source support alone
enables no installed/live runtime. No profile activation, merge, push, lifecycle
operation, native3 follow-on or other package is implied. Lead owns final review
and the prepared installed-copy check; implementer0 retains review fixes and
reports this package complete for acceptance with capacity available.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/)
