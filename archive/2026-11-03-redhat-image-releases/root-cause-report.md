# Initial image-test failure: cause and proposed fix

Investigation and proposal only. No application changes, builds, test retries,
CI retries or merges were performed for this investigation. The release branch
remains `3307df52ea5bf875e1d8a23318a64f569d8b3ebc`.

## Established cause of the null-revision failure

The test runner preserves the repository's source files but loses the associated
source identity at the snapshot/framework boundary. Test VMs then bypass the
normal flake builder's version module. A nullable revision reaches a channel
generator that assumes it is a string, causing evaluation to fail before any
image build or VM starts. This is a pre-existing framework defect, independent
of the four release-RPM edits.

The local failure and baseline reproduction are documented in
[verification-diagnosis.md](verification-diagnosis.md). Architect inspection
confirms this source chain at the release branch head:

1. [The source resolver](https://github.com/vpsfreecz/vpsadminos/blob/3307df52ea5bf875e1d8a23318a64f569d8b3ebc/test-runner/nix/resolve-repository-source.nix#L8)
   retains only the original flake's `outPath`.
   [RepositorySource](https://github.com/vpsfreecz/vpsadminos/blob/3307df52ea5bf875e1d8a23318a64f569d8b3ebc/test-runner/lib/test-runner/repository_source.rb#L48)
   returns that path, and
   [the command wrapper](https://github.com/vpsfreecz/vpsadminos/blob/3307df52ea5bf875e1d8a23318a64f569d8b3ebc/test-runner/lib/test-runner/cli/command.rb#L138)
   replaces `TEST_RUNNER_REPO_ROOT` with it.
2. [Evaluation reopens the snapshot](https://github.com/vpsfreecz/vpsadminos/blob/3307df52ea5bf875e1d8a23318a64f569d8b3ebc/test-runner/nix/evaluate-tests.nix#L16).
   [The framework exports paths and nixpkgs identity](https://github.com/vpsfreecz/vpsadminos/blob/3307df52ea5bf875e1d8a23318a64f569d8b3ebc/flake.nix#L83),
   but no equivalent vpsAdminOS identity. [Test VM construction](https://github.com/vpsfreecz/vpsadminos/blob/3307df52ea5bf875e1d8a23318a64f569d8b3ebc/tests/make-test.nix#L104)
   imports `../os` directly, bypassing the normal builder's
   [flakeVersionInfoModule](https://github.com/vpsfreecz/vpsadminos/blob/3307df52ea5bf875e1d8a23318a64f569d8b3ebc/flake.nix#L181).
3. [The revision option](https://github.com/vpsfreecz/vpsadminos/blob/3307df52ea5bf875e1d8a23318a64f569d8b3ebc/os/modules/misc/version.nix#L99)
   explicitly permits null. It falls back to null without a usable `.git`
   directory or `.git-revision`. The tested local snapshot contained a linked
   worktree `.git` pointer file and no `.git-revision`; native evaluation returned
   `revision=null` and `versionSuffix="pre-git"`. The preceding Fedora-45 baseline
   reproduced these values too.
4. [The image VM enables channel registration](https://github.com/vpsfreecz/vpsadminos/blob/3307df52ea5bf875e1d8a23318a64f569d8b3ebc/tests/suite/image-scripts/test.nix#L34).
   [channel.nix:95](https://github.com/vpsfreecz/vpsadminos/blob/3307df52ea5bf875e1d8a23318a64f569d8b3ebc/os/modules/installer/cd-dvd/channel.nix#L95)
   interpolates that null into the shell command writing `.git-revision`.
   This produces `cannot coerce null to a string`.

`TEST_RUNNER_REPO_REV` is already exported by the wrapper, but the
[image template](https://github.com/vpsfreecz/vpsadminos/blob/3307df52ea5bf875e1d8a23318a64f569d8b3ebc/tests/suite/image-scripts/test.nix#L45)
uses it for the later in-guest image command, not the VM's source metadata.
Simply recognizing `.git` pointer files would still depend on mutable external
Git state and would not cover Git-free snapshots.

## Recommended correction

Preserve verified revision and dirty-state metadata alongside the exact resolved
source snapshot, and carry it through the test framework into the test OS.
Factor and reuse the existing `flakeVersionInfoModule` identity rules for both
normal flake builds and test VM builds. This repairs the missing provenance as
well as the evaluation failure. The lead accepted this recommendation as the
proposal; implementation is not authorized in this investigation turn.

The implementation boundary is the resolver/RepositorySource transport,
evaluation/framework plumbing, and `tests/make-test.nix`, with shared identity
logic factored from `flake.nix`. Bind metadata to the captured source, including
dirty content; do not read a live worktree's HEAD later or treat an arbitrary
environment revision as proof that a snapshot is clean. Preserve current source
selection semantics, including any supported untracked content. Keep existing
explicit module overrides and legacy framework compatibility.

Separately, make `channel.nix` honor the existing `nullOr str` contract: omit
the `.git-revision` write when revision is unknown. This is needed for legitimate
Git-free sources, but alone would leave known test-source provenance missing.
Do not substitute an empty string, invented SHA or unconditional clean flag.

Proposed regression validation, not executed:

| Case | Required result |
| --- | --- |
| Clean ordinary checkout | Snapshot and test VM report the captured commit, clean state and existing suffix convention |
| Clean linked worktree | Same identity semantics as an ordinary checkout; no dependency on following a copied `.git` pointer |
| Dirty snapshot | Modified content remains included according to existing selection rules; parent revision and dirty state remain truthful |
| Source changes after capture | Evaluation retains the captured content/identity; later HEAD or working edits cannot change the reported revision |
| Git-free source | Unknown revision stays null without fabricated metadata |
| Channel-enabled evaluation | Known and unknown revision cases both instantiate; known revision is written accurately, unknown revision does not create a bogus `.git-revision` |

Use focused resolver/framework tests and Nix evaluation of the image-test VM,
including the existing explicit override path. After implementation, quick checks
and independent review, run a channel-enabled image test and then all four
required release-image tests. Keep existing successful normal flake behavior.

## Historical GitHub evidence and limits

The user recalls an earlier Fedora-45 failure with the same null-coercion error.
That historical GitHub occurrence is **not verified** by the retained runs found
here. It must not be replaced with the later SSH symptom or claimed disproven.

| Run | Exact retained attempt | Result at `dd188397abe37d0bc33f4c5dfb3605206ce5e326` |
| --- | --- | --- |
| [41666620408](https://github.com/vpsfreecz/vpsadminos/actions/runs/41666620408) | 1, feature-branch push at 15:42:14Z | Fedora-45 image test passed; test job `126024976745` |
| [41677315874](https://github.com/vpsfreecz/vpsadminos/actions/runs/41677315874) | 1, staging push at 16:44:47Z | Image built; 14 subtests passed and `ssh_password` failed; test job `126062384663` |

Both API records reported `run_attempt=1`, `previous_attempt_url=null`; explicit
`/attempts/1/jobs` returned those same job IDs. Explicit `gh run view --attempt 1
--log` downloads byte-matched the default log downloads. Branch-scoped history
returned only the image success and the accompanying general CI run. All-repo
history on 2026-11-03 before that first push returned these two plus three
successful scheduled maintenance runs; no earlier Fedora pre-rebase/repush run
was returned. Removed or otherwise unidentified historical runs remain unknown.

The accompanying [general CI run 41666620193](https://github.com/vpsfreecz/vpsadminos/actions/runs/41666620193)
was still running. Its earliest inspected failed livepatch job `126034272162`
failed building `livepatch_7-exact-candidate.ko`, a separate failure. This check
did not establish a null-revision trace and was not expanded into kernel work.

The retained image failure is also separate: the container entered RUNNING at
18:24:54.697864+01:00; at 18:25:29.357633+01:00 `ssh_password` reported
`ssh not responding`. Its network check passed, but the existing 30-probe port-22
readiness check did not. The harness then deleted the failed container; the
later diagnostic artifact has an empty destroyed-container log, not its sshd
journal. The underlying service cause cannot be established from that artifact.
No SSH timing change or general retry workaround is proposed as the fix for the
null-revision defect.

Original evidence is retained, untracked, beneath `ci-root-cause/`: explicit
attempt-1 logs for both image runs, the failed run's `os-test-logs-41677315874`
artifact (ID `13255251063`, 305252 compressed bytes), and the bounded general-CI
job log. Key original lines: failed artifact `test-runner.log:3125-3128` contains
the SSH failure; line 3152 says `15 tests run, 14 succeeded, 1 failed`.
The native null-revision evidence and exact source paths remain in
[verification-diagnosis.md](verification-diagnosis.md), not inferred from these
GitHub logs.
