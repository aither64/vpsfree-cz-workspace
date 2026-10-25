# Go temporary-consumer build metadata: final review

**No new Blocking, Important or Advisory findings.** The general, architecture/
repetition and scope/proportionality review gate passes for the completed Go
harness correction. Actual Go SDK compilation and rendered-program execution
remain unproven. This report grants no integration, publication or lifecycle
authority.

## Identity and exact range

- Session `2026-10-22-haveapi-release`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`.
- Retained independent reviewer `reviewer0`, purpose `review`, thread
  `01a16406-faaa-7cd0-bde3-c20802c18a72`, project
  `01a16406-fa76-7532-9ee4-a890352500df`.
- Live same-session roster confirmed ready state and saved/assigned
  `gpt-6.1-sol` / `xhigh` / `read_only`. No overrides, fallback or nested agents.
  `dev-session current` matched the trusted binding; both identity environment
  variables were absent.
- Repository `vpsfreecz/haveapi`, intended target `master`; worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi`.
- Complete final range `a32b15e379f44fc6dae4b15ef4ec17a142e5f465` →
  `3fb91caf783eaeacf49bf3647b8409d536339d71`, tree
  `8698b4a7b707b2c165877931071d31505f346370`.
- Prior reviewed head `48543f8cd254eb0fc087931a5dc98ea730fd94af`; exact last
  complete message remains `Version 0.30.0`, with no body.

Read the mandatory-review skill, Shared Reviewer Instructions and all three
selected lane references; inspected the packet, receipt, actual source delta,
complete final series and input evidence. Overall release risk remains high and
its earlier four-lane reports remain retained. This three-path delta is low risk:
only disposable test-consumer VCS metadata and its regression/docs change.
Product risk/compatibility conclusions remain supported by exact unchanged source;
no new auth/URL/security contract was introduced or presumed reviewed from a label.

## Findings assessment

`GoDocumentationAcceptance.build_command` owns the actual temporary consumer's
build argv, adding only explicit `-buildvcs=false`. `run!` consumes that exact
command. Existing SDK generation, imported package/module replacement, source
formatting, actual Go build and execution/assertions remain required. The flag
does not turn compilation into a dry run, bypass Go type checking or change the
rendered programs. No global `GOFLAGS`, ambient Git state, renderer/generator
output or product build policy is changed.

The new explicit regression requires the harness without constructing its
server, creates its own invalid `.git` ancestor plus a minimal module and main,
and inserts Go's native `-n -x` into the same build argv. The flagged command must
succeed without Git-status discovery; the otherwise identical unflagged command
must fail obtaining VCS status and locate that operation at the owned ancestor.
This is a real-tool positive/negative control for the observed failure rather
than a string-only assertion or repaired fake repository. `-n` prevents compiler
execution while Go still performs the VCS discovery needed by the negative case.
The fixture does not depend on or modify the unowned ambient `/tmp/.git` marker.

Both test paths retain `GOWORK=off`, `GOPROXY=off`, `GOSUMDB=off` and
`GOTOOLCHAIN=local`; no new dependency installation or toolchain download path
is added. The native regression uses the existing dedicated documentation bundle,
not an ordinary server dependency. Loading the acceptance file does not invoke
its guarded main or construct a listener. The small shared argv method has one
production-test caller and one regression caller and is proportional to the
demonstrated failure. The short owning guide accurately limits the flag to the
disposable consumer and asks callers to retain actual source/artifact evidence.

## Full history and consolidation

Independently reconstructed all 22 final commit positions and stable patch IDs
against `48543f8c`: **21 equal**, only Go owner position 11 changes
(`4479c930` → `cb21d5ce`). First ten hashes are exact. The complete semantic delta
is only:

- `clients/go/spec/documentation_acceptance.rb`;
- `clients/go/spec/documentation_build_check.rb`;
- `clients/go/docs/documentation.md`.

Actual merge base is the stated base. Prefold
`fa409240308cde895d6d02a0f45c934faec91be1` and final head have equal trees and
identical complete binary base-to-head diffs. Final whitespace checks pass.
The correction is folded into its owning acceptance purpose, with no fixup-only
commit, obsolete unmerged approach, transient workaround, abandoned generated
revision or unused compatibility mode remaining. Other authored, generated,
cleanup/diagnostic and version purposes remain independently reviewable and in
their accepted order. Released maintenance provenance remains exact.

Repeated-stream conclusion: **no new dependency, input, channel, lock, version or
generated stream**. One cumulative JS payload `9c0cd9b4` follows its helper and URL
source features, with final version-literal metadata separate in `3fb91caf`.
Shared npm/Python/Rust version/lock updates remain one final stream; Node test
declarations remain a distinct single dependency update. Highlighter pin/build/
license/bundle, PyPA action and shared CI action-role streams remain consolidated.
No intermediate pin or payload requires a release/consumer/state-boundary exception.
Earlier exact refs and execution records remain separate provenance.

Migration conclusion: **no migrations**. Entire final history contains no database
schema or persisted-format conversion, no transitional migration, and no migration
merge/release/deployment/external-use lineage to reconcile.

## Verification and retained-input conclusions

Reviewer ran the known quick native regression and environment preflight in the
declared root tools-only Nix shell with
`BUNDLE_GEMFILE="$PWD/clients/go/spec/documentation.Gemfile"`:

```sh
bundle exec ruby clients/go/spec/documentation_build_check.rb
bundle exec ruby clients/go/spec/documentation_acceptance.rb --check-environment
```

Both passed. The first printed that the dry-run and unflagged VCS control passed;
the second completed without error. No compiler, SDK generation, listener,
package installation or full acceptance was started. Owner syntax/style/hooks
were inspected as supporting evidence, not relabeled reviewer-run checks.

Independently checked original Rust inventory SHA-256
`538c6330ad3647cf30b1ee2134e5e2594c91701419ae02b4f1b456086a3007f4`, mapped every
one of its **310** original mode/type/blob identities to both actual `48543f8c`
and final Git trees, and independently checked `flake.nix`/`flake.lock` identities.
No mismatch was found. This is tracked-input equivalence, not new-head execution.

The retained Rust result records actual execution at **`48543f8c`**, exit 0 after
915.38 seconds. Its log confirms root and `/mounted/api/` acceptance, 26 programs
per mount; retained mount directories contain those emitted programs and actual
snapshot/TOML/Cargo manifest/lock/source plus tool receipts. Development tools are
1.99 and independently selected MSRV tools are 1.95. This source change cannot
invalidate those unchanged repository inputs; retain the original generated/input
graphs and report the actual tested head rather than calling it final-head
execution. Previous dynamic wheel/sdist results likewise keep their actual
source/artifact identity; their encompassing verification batch ended in the
recorded Go VCS failure.

Remaining gate: build/verify exact final artifacts and run the actual generated
Go consumer and rendered programs. A native build plan proves the VCS policy,
not compiler/type/import success or request behavior. Final-head CI and any
lead-selected package checks remain separate evidence. Do not replace the failed
earlier Go run with a success label, or relabel earlier Rust/dynamic runs as
literal final-head execution.

Tracked source/index remained clean at exact `3fb91caf`. Only this assigned
report was written. No source/Git/default/tag/registry/deployment/lifecycle action
was performed. Lead owns state reconciliation and subsequent verification;
session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
