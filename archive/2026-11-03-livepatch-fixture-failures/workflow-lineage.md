# Livepatch workflow and CI lineage

Read-only investigation by implementer0 on 2026-11-03, against canonical
`vpsfreecz/vpsadminos` and this session's independent worktree at
`dd188397abe37d0bc33f4c5dfb3605206ce5e326`. No source changes, Git mutations,
builds, CI reruns, deployments or lifecycle operations were performed.

## Result

The current failure happens while preparing the strict corrected fixture,
before the test runner or any VM starts. It already occurred on October 30,
before Fedora 45 was added. Last observed all-nine-lifecycle green is October
26; first later whole-CI execution is October 30 and all nine lifecycle rows
fail. The exact responsible commit within that interval is not established.

The successful and failing corrected wrappers have different Nix identities,
while the expected module hash, fixture source and workflow remain unchanged.
The October 30 and November 3 failures use the same failing wrapper derivation.
This supports investigating the candidate's input graph before changing the
reviewed integrity pin. The actual candidate digest is absent from these logs.

## Canonical executions

| Date UTC | Revision | Canonical run | Lifecycle result |
| --- | --- | --- | --- |
| Oct 25 | `f715e9d99b56a2f0e52d17b15f086b99cc926e13` | [40217314767](https://github.com/vpsfreecz/vpsadminos/actions/runs/40217314767) | All nine green; entire CI green |
| Oct 26 | `d9be8c4bada590c0405df85444600d40e6f3caa6` | [40296454457](https://github.com/vpsfreecz/vpsadminos/actions/runs/40296454457) | All nine green; native test job failed separately |
| Oct 30 | `05201326975fc19d20a545c52f651cce0420dbc9` | [41072532280](https://github.com/vpsfreecz/vpsadminos/actions/runs/41072532280) | All nine fail in lifecycle step and result evaluation; native test job green |
| Nov 3 | `dd188397abe37d0bc33f4c5dfb3605206ce5e326` | [41666620193](https://github.com/vpsfreecz/vpsadminos/actions/runs/41666620193) | All nine lifecycle jobs completed red; build job green; native job still running when inspected |

The last row runs on the Fedora feature branch, whose exact head has since
become staging. The separate staging run
[41677315937](https://github.com/vpsfreecz/vpsadminos/actions/runs/41677315937)
was still in its build job when inspected; it supplies no additional lifecycle
result here. No wait for either run was required.

The whole-CI run listing contains no intervening execution between the October
26 and October 30 rows. Therefore the observed regression is bounded by
`d9be8c4..0520132`; this is an observed execution interval, not a completed
commit bisect. Earlier individual scale-aged qualification failures do not
establish this fixture-preparation regression: the other lifecycle rows
continued to pass, and all nine passed on October 26.

## Exact failure phase and evidence

The workflow's `Run livepatch lifecycle tests` step performs these operations
in order:

1. Evaluate the source-pinned `correctedSha256` into a text file.
2. Build `tests/fixtures/livepatch -A corrected`, redirecting stdout to
   `livepatch-corrected-path.txt`.
3. Build the released v5 and shipped v6 fixtures.
4. Export fixture paths, construct runner arguments and invoke
   `./test-runner.sh` with output copied to `test.log`.

The step uses `set -euo pipefail`, so failure at operation 2 stops everything
after it. Source: [workflow at the failing head](https://github.com/vpsfreecz/vpsadminos/blob/dd188397abe37d0bc33f4c5dfb3605206ce5e326/.github/workflows/ci.yml#L412),
[strict fixture](https://github.com/vpsfreecz/vpsadminos/blob/dd188397abe37d0bc33f4c5dfb3605206ce5e326/tests/fixtures/livepatch/default.nix#L53).

Inspected logs prove the checked-out full source SHA using checkout's final
`git log -1 --format=%H`, rather than the checkout cleanup's earlier retained
HEAD message. Relevant jobs:

- [October 26 AMD, job 121489063395](https://github.com/vpsfreecz/vpsadminos/actions/runs/40296454457/job/121489063395):
  corrected fixture succeeds, selected configurations prepare successfully,
  and runtime starts. All ten selected AMD test scripts complete successfully.
- [October 30 AMD, job 124217753063](https://github.com/vpsfreecz/vpsadminos/actions/runs/41072532280/job/124217753063):
  at `17:42:39Z`, the corrected wrapper builder fails with exit code 1.
- [November 3 AMD, job 126034272312](https://github.com/vpsfreecz/vpsadminos/actions/runs/41666620193/job/126034272312):
  at `16:01:25Z`, the same wrapper builder fails with exit code 1.
- [November 3 Intel, job 126034272162](https://github.com/vpsfreecz/vpsadminos/actions/runs/41666620193/job/126034272162):
  at `16:00:34Z`, the same wrapper builder fails with exit code 1.

Exact failing derivation and advertised output in all three inspected red logs:

```text
/nix/store/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv
/nix/store/kmm41zgxg3ai8r84jqm2mk02r4py6cdv-livepatch_7-exact-candidate.ko
```

The corrected builder checks the candidate with
`sha256sum --check --status`, then creates an output symlink. The silent
checksum mode prints neither the actual digest nor a mismatch explanation.
The raw log alone establishes the failed builder, not the measured candidate
digest. Given this two-command builder and absent symlink diagnostics, a failed
checksum is the supported explanation; independent candidate measurement is
needed to establish the bytes and cause.

The later missing-`test.log` evaluation error is secondary: the runner command
has not been reached. It supplies no VM, transition, performance or qualification
failure evidence for these three jobs.

## Artifacts and pinned identity

The independently downloaded artifacts provide stronger evidence than the
generic exit message:

| Artifact | Contents relevant here |
| --- | --- |
| October 26 AMD, ID `12646139312` | 66 entries, including populated corrected path and expected digest, plus runtime logs |
| November 3 AMD, ID `13248340186` | Exactly two entries: expected digest file and empty corrected path file; no `test.log` |

Both expected-digest files contain:

```text
573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d
```

The green artifact records this successful corrected wrapper:

```text
/nix/store/m3ig6h5s0ldclfyl3mrss6n5psrw0j7d-livepatch_7-exact-candidate.ko
```

Thus wrapper identity changed from green to red. Its store path alone is not a
measurement of module content, nor does it identify which transitive input
changed. The unchanged red derivation across October 30 and November 3 is exact
derivation evidence that Fedora did not introduce this failure.

The fixture's last edit was
[3ddca3e6b84017f37499568d3efaefa7c4e2e72f](https://github.com/vpsfreecz/vpsadminos/commit/3ddca3e6b84017f37499568d3efaefa7c4e2e72f)
on October 15. It sets this exact hash and records independent producer/ABI and
focused runtime verification. No later fixture edit changed the pin or the
selection mechanism. Its contract says runtime qualification exercises those
exact bytes and forbids deriving the pin from the tested candidate.

## Source, input and runner changes

Across `d9be8c4..0520132`, the final diff changes 13 files. The workflow,
fixture, boot-base configuration, kernel and livepatch source are unchanged.
Changes are `flake.lock`, packaged Ruby dependency metadata, and the
`osctl-oomd` fix/spec. The fixture imports root `inputs.nixpkgs` by default;
its boot-base configuration explicitly keeps the current OS package's v7 build
inputs while restoring frozen boot kernel outputs. A frozen boot SDK therefore
does not freeze the complete candidate producer graph.

| Root input | Oct 26 green | Oct 30 red | Nov 3 red |
| --- | --- | --- | --- |
| `nixpkgs` (`nixpkgs_2`) | `1f607aa79b6356ed45d3cd3c8079c196e79efa2c` | `6f06d204d8f2d8761d9da78778745974a3216381` | `7dcdd87373d72e7a2173e4db02e20d3d7f495cfd` |
| `nixpkgsUnstable` | `3ec636362e1816bc2f0888fa0fa2c69f1bc9e504` | `31ecbaca1bdefa45dffc409f0250bd8039ea0010` | `0bb2eedc20e4739f29e8045034f2828ad7054f8f` |

The root stable input advances through three commits within the bounded
interval: `f4e55a13` (October 27, to `718f670e8`), `449b1dc5` (October 29,
to `08d3a9758`), and `8ce6234d` (October 30, to `6f06d204d`). The unstable
update is `b45b27b4` (October 28). The remaining commits are packaged-gem
updates `f40afdf8`, `a5ad64f8` and the `05201326` OOM daemon fix. This identifies
plausible input drift without claiming which commit first changes module bytes.

The observed AMD host remains `gh-runner4.int.vpsadminos.org` in green,
first-red and current-red logs. All three show Actions runner `2.336.0` and
the same `git-2.54.0` store path. Current Intel runs on
`gh-runner3.int.vpsadminos.org`. The lifecycle matrix uses `amd-livepatch`
and `intel-kvm` labels and has no relevant source change over the interval.
Complete host profile histories were not collected; runner names/versions do
not independently prove absence of all host changes.

Fedora commit
[dd188397](https://github.com/vpsfreecz/vpsadminos/commit/dd188397abe37d0bc33f4c5dfb3605206ce5e326)
touches only `image-scripts/images/fedora-45/{build.sh,config.sh}` and
`os/configs/image-repository.nix`. It changes neither this workflow nor the
livepatch fixture. The same first-red derivation already failed October 30.
Fedora is therefore outside the demonstrated regression cause.

## Handoff and limits

The smallest next diagnostic step is to reconcile the current candidate module
and its input graph against the green wrapper and retained independent producer,
including ABI and byte identity. Architect0 and implementer1 own that analysis.
This workflow evidence does not justify replacing the pin with the current
candidate's checksum or removing fixture/main/perf integrity assertions.

If a later correction changes diagnostics, preserve the fail-closed checksum
guard while emitting expected/actual digests and the producer identity before
failure. Full VM runs or rerunning unchanged CI cannot resolve the existing
fixture-preparation failure.

Disposable evidence is under `ci-lineage-evidence/`: four downloaded job logs
and two artifact ZIPs. Raw artifacts are not intended for Git. Retrieval used
`gh run view --job --log` for completed runs and the job-log REST endpoint for
completed jobs in an ongoing run; the latter required
`gh api --allow-escape-sequences` because the logs contain ANSI coloring.
No live checks or long-running verification were launched.

Lead owns state/portal updates and any Git operations. Project documentation
was read, but no project documentation change is appropriate for this
investigation-only deliverable.

Stable session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
