# Livepatch qualification failure: first-interface diagnosis

Package D2, architect0, 2026-11-17. Read-only investigation complete.

## Conclusion

The producer failed on a pre-existing runner evidence path **before plan
revalidation or any producer build**. This is a baseline workflow staging-path
collision, not evidence of a Linux 6.12.118 compile, boot or livepatch regression.
The update triggered the workflow through its Linux catalog path filter; it did
not change the failing workflow, guard, livepatch catalog, target entry or locked
inputs. The qualification remains failed and provides no product validation.

The log proves that the evidence path already existed or was a symlink. It does
not prove its creator, age, content, ownership, filesystem type or why runner
temporary-directory cleanup left it available. No runner inspection, cleanup,
retry, cancellation or source mutation was performed.

## Exact attempt and first failure

- Repository: `vpsfreecz/vpsadminos`.
- Workflow: `418457006`, `.github/workflows/livepatch-qualification.yml`.
- [Run 44120818064, attempt 1](https://github.com/vpsfreecz/vpsadminos/actions/runs/44120818064/attempts/1), push event.
- OS source: `ba7e99b5e3d435826bd387e64f1c1a6ec173169c`.
- Comparison base: `a7d71a54a15496976cb0fccebb8a1b589f24f5e2`.
- Discovery job `134171358090` passed.
- [Producer job 134174364543](https://github.com/vpsfreecz/vpsadminos/actions/runs/44120818064/job/134174364543), step 6, “Capture one dynamic producer identity set”.

Producer log lines 141–161 show the workflow command, source/plan identity
comparison, `mkdir -p "$RUNNER_TEMP/livepatch-capture"`, then:

```text
tools/livepatch/capture.sh \
  --plan "$RUNNER_TEMP/livepatch-input/plan.json" \
  --output "$RUNNER_TEMP/livepatch-capture/capture.json" \
  --evidence-dir "$RUNNER_TEMP/livepatch-capture/evidence"
2026-11-17T16:13:43.2042385Z refusing pre-existing evidence directory: /run/github-runner/runner/_temp/livepatch-capture/evidence
2026-11-17T16:13:43.2086758Z ##[error]Process completed with exit code 1.
```

At this exact source, `tools/livepatch/capture.sh:43–46` requires
`[[ ! -e "$evidence_dir" && ! -L "$evidence_dir" ]]` and exits with that message
on failure. The earlier regular-plan and absent-output checks passed. The guard
precedes creating evidence, temporary capture work, `discover.sh --input` at
line 62, and the first producer `nix build` at line 97. The workflow's subsequent
`verify.sh` and upload steps therefore did not execute successfully.

The workflow uses a fixed `$RUNNER_TEMP/livepatch-capture` parent at
`.github/workflows/livepatch.yml:83–101`. Its artifact *name* includes run/attempt,
but its producer filesystem root does not. This is the concrete collision
mechanism; weakening the capture refusal would conceal stale evidence.

Close job `134180343394` then failed at `2026-11-17T16:14:03.6912422Z` with
`receipt count does not match the plan`. This is downstream of absent capture
and skipped consumers, not a second kernel failure.

## Selected plan and unchanged target

The only available artifact was `livepatch-plan-44120818064-1`, ID
`14346320716`, 1,864 compressed bytes, unexpired. Downloaded through GitHub's
artifact API and inspected in memory; it contains `plan.json` and `matrix.json`.
No capture artifact or accepted row receipts were available.

The actual plan reports:

| Field | Value |
| --- | --- |
| `sourceRevision` | `ba7e99b5e3d435826bd387e64f1c1a6ec173169c` |
| `system` | `x86_64-linux` |
| `selectedSets` / `plannedMembers` | 1 / 1 |
| set / release | `6.12.113.1` |
| kernel | `6.12.113` |
| `producerAttr` | `livepatch-release-6_12_113_1` |
| payload revision | 1 |
| fix / oracle | `nfs-sysfs-client-lifetime` / `nfs-client-operation-safety` |
| planned rows | 10: eight generic AMD/Intel rows and two fix-oracle rows |

`flake.nix:230–246` builds livepatch systems from catalog kernel versions and
explicitly sets `boot.kernelVersion = kernelVersion`. The selected kernel is
therefore the retained 6.12.113 entry, Linux
`1dfea587406b7dd79973831d1677fb2418e5e9aa`, with archive hash
`sha256-IvyBosmZkpWxAK4Bz0sQ+RBwUQZwN+GtBxwjBY1lAdQ=`. The changed stable
selector does not replace this explicit target. No exact realized producer or
module identity can be reported because this attempt never reached realization.

## Changed-range proof

`git diff --stat a7d71a54..ba7e99b5` contains only seven files: `AGENTS.md`,
`README.md`, `docs/os/kernel-updates.md`, `mkdocs.yml`,
`os/packages/linux/available-kernels.nix`, and the new skill's two files.
The catalog diff only adds 6.12.118 and switches stable from 6.12.117 to 6.12.118.
Every older entry, including 6.12.113, is unchanged.

Direct Git blob comparisons at the full base/head above prove these inputs
identical (the blob IDs below are the same on both sides):

| Path | Git blob |
| --- | --- |
| `.github/workflows/livepatch-qualification.yml` | `e11a9905ece00b66f697b694ad2df57f034c3377` |
| `.github/workflows/livepatch.yml` | `7a4f1749dd46aa301608ff9cf246ca21f54e8b97` |
| `tools/livepatch/capture.sh` | `aef0c8bbf47013e9b8c6d206ccc2bb10585231fd` |
| `tools/livepatch/discover.sh` | `fe0c95d630a95f2e825fb3f9c4371b4c0d33d3cb` |
| `tools/livepatch/verify.sh` | `de8ef6bd461c10a7aa019ae7ad7312f3a67c1b28` |
| `flake.nix` | `74a87d96d5e3acdb95a44b322b7f551a9b283ee5` |
| `flake.lock` | `3db52b818025eaedb416fff0ac082d62af632ff6` |
| `os/livepatches/batches/6.12.113/1/default.nix` | `54ee29d27261789a7fdbdaca7e9d57f14d46878e` |
| `tests/configs/vpsadminos/livepatch.nix` | `aceba8a22be00f86447a14ad18f0497f199bf736` |
| `os/packages/linux/packages.nix` | `5609ad020c2c12ae77d0a4897597d06b041500ec` |
| `os/packages/linux/default.nix` | `c825cc82b129416b567d556fae7c06d5d3f771c9` |

No livepatch catalog, payload, builder or qualification-tool path changed in the
complete range. This proof establishes relevance of the observed early failure;
it does not claim that an unrun capture or qualification campaign would pass.

## Smallest future remediation and residual gap

If separately assigned, the workflow owner should allocate one fresh capture
root per run/attempt/job invocation (for example `mktemp -d` under
`RUNNER_TEMP`, with run/attempt context), pass its initially absent `capture.json`
and `evidence` child paths consistently to capture/verify, and upload that same
root via a step output. Preserve existing evidence and capture's refusal and
recovery semantics. Do not delete the shared fixed path or automatically retry
until stale evidence happens to disappear. No broader livepatch redesign is
indicated. A lead-assigned implementer can own this narrow workflow fix; D2 does
not assign it or authorize changing this kernel branch.

The smallest future check is that fresh staging is distinct across two workflow
invocations, capture/verify/upload consume the same root, and pre-existing child
paths remain refused. Follow the existing focused qualification check before any
new long campaign. Any change to this workflow still requires its normal hooks,
review and final-source verification; a rerun alone is not remediation.

For this kernel task, retain this failed qualification result as an unrelated
pre-producer baseline collision and state the missing livepatch qualification
coverage. Actual target readiness must come from exact 6.12.118 source/build/boot
and applicable runtime results. Main CI `44120817659` remains with its existing
runtime observer; D2 neither watched it nor launched a duplicate build.

Evidence collection used read-only `gh api` job logs, run metadata and artifact
retrieval, plus exact-source Git reads. Raw logs were not saved. Only this
Markdown finding was written; no commits, reruns or remote mutations occurred.
