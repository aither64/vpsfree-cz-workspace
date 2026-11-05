# Bounded CI livepatch failure investigation

Owner `implementer1`; 2026-11-05. Prior P2 accepted, capacity and exact session/env
verified. Investigation only: three requested failed job logs downloaded, source
read at fixed refs. No source/index edits, rerun, cancellation, build, guest/live
host action or cross-session access. Other CI jobs were not monitored or altered.

## Exact provenance

Run [42120921101](https://github.com/vpsfreecz/vpsadminos/actions/runs/42120921101),
attempt **1**, workflow `.github/workflows/ci.yml`, push on the feature branch,
head **`8d5093e3d65f561dd305898074dd8add5e49323e`**. API snapshot and each exact job's
metadata are retained beside their raw logs in `artifacts/ci-42120921101-*`.
The run status is only that snapshot, not a current whole-CI conclusion.

| Job | Matrix label | Runner | Failed step interval, UTC |
| --- | --- | --- | --- |
| [127578864220](https://github.com/vpsfreecz/vpsadminos/actions/runs/42120921101/job/127578864220) | intel | gh-runner1.int.vpsadminos.org | 22:35:01–22:35:10 |
| [127578864291](https://github.com/vpsfreecz/vpsadminos/actions/runs/42120921101/job/127578864291) | intel-representative-v5 | gh-runner1.int.vpsadminos.org | 22:35:24–22:35:33 |
| [127578864321](https://github.com/vpsfreecz/vpsadminos/actions/runs/42120921101/job/127578864321) | intel-representative-v6 | gh-runner3.int.vpsadminos.org | 22:35:01–22:35:12 |

Raw logs are exactly those three jobs. `gh api` initially refused terminal escape
sequences; reran the same read with `--allow-escape-sequences` into files. No escape
content was executed. File byte lengths and SHA256s are in
[log receipt](artifacts/ci-42120921101-failed-job-log-receipt.json); bounded ANSI-stripped
[line-numbered excerpts](artifacts/ci-42120921101-failure-excerpts.txt) retain original
line numbers. No uploaded test artifact or unrelated job log was downloaded.

## Demonstrated common failure

All three fail building the same derivation:
`/nix/store/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv`,
output `/nix/store/kmm41zgxg3ai8r84jqm2mk02r4py6cdv-livepatch_7-exact-candidate.ko`,
builder exit **1**. Intel raw log lines 205–212, v5 203–210, v6 207–214.
This occurs before the test runner or guest lifecycle tests run. Evaluation's
missing `test.log` is secondary (raw lines 328, 326, 330 respectively).

At the exact run SHA, workflow `ci.yml:420–440` uses `set -euo pipefail` and
first builds `tests/fixtures/livepatch -A corrected`; releasedV5, shippedV6 and
`./test-runner.sh` (`:471`) come later. Fixture `tests/fixtures/livepatch/default.nix:47–49`
contains only the exact candidate checksum guard followed by a symlink:
`printf ... | sha256sum --check --status; ln -s candidateModule "$out"`.
Expected SHA256 (`:13`) is
`573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d`.
Candidate is `candidateSystem.config.system.build.livePatches` plus
`/lib/modules/6.12.95/extra/livepatch_7.ko` (`:14–18`), using the frozen boot config.

This strongly suggests candidate bytes failed the exact reviewed pin guard.
However, `--status` suppresses checksum diagnostics, and the job logs contain no
actual candidate hash/path or builder command trace. Missing/unreadable input or
a symlink-stage error cannot be conclusively excluded. No actual byte mismatch,
underlying module defect, compiler nondeterminism or changed ABI is proven here.

## Correlation and shortest next action

Compared implementation base **`d2fe1489f0b0b213fb247aeee6e081d349adaf42`** to the exact
run SHA; merge-base equals that base. No diff in CI workflow, livepatch fixtures,
frozen boot config, `os/livepatches`, livepatch module, Linux/kpatch package sources
or `flake.lock`. The branch's package overlay only adds `osctl-repo-server`;
flake additions expose packages/dev shell. General runner/pool/service changes
exist, but none were reached by the observed failure.

There is **no demonstrated direct livepatch-source regression** in the branch.
This is not proof the failure is unrelated: exact candidate derivation inputs and
bytes were not captured, so source-path/build reproducibility or prior pin drift
remain unresolved. Three identical failures on two runners establish a shared
pre-test fixture problem rather than three observed guest/runtime failures.

Shortest corrective diagnosis: an authorized owner should retrieve the failing
derivation's `nix log` and exact candidate pathname/hash from the affected build
state, then reconcile those bytes against the reviewed pin and complete inputs.
Preserve the expected pin; do not recompute it from the failing candidate or rerun
blindly. Improve fixture failure diagnostics only if assigned, then verify the
identified correction. This investigation performs no follow-up runtime action.

## Bounded cache/store retrieval follow-up

Lead authorized a separate five-minute read-only retrieval after accepting the
initial investigation. Session/env matched again. No source/index/other-session
state, SSH, realization, build, rerun or pin update was used. Retrieval completed
in approximately one minute, 2026-11-05 22:46 UTC.

- `nix log /nix/store/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv`
  exits **0**, reports its log from configured `https://cache.vpsadminos.org`, but
  produces **zero stdout bytes**. [Fetch receipt](artifacts/ci-42120921101-candidate-builder-fetch.txt),
  [empty builder log](artifacts/ci-42120921101-candidate-builder.log).
- A bounded read of the exact configured-cache URL
  `https://cache.vpsadminos.org/log/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv`
  confirms **HTTP/2 200**, `content-type: text/plain`, **zero body bytes**.
  [Headers](artifacts/ci-42120921101-cache-log-headers.txt),
  [empty body](artifacts/ci-42120921101-cache-log-body.txt). Thus the issue is
  missing diagnostic content, not an asserted cache outage or denied log access.
- Exact failing `.drv` is **absent from the local store**. Ordinary read-only
  `nix derivation show --store https://cache.vpsadminos.org` for that `.drv`
  exits **1**: `error: path '...livepatch_7-exact-candidate.ko.drv' is not valid`.
  [Exact error](artifacts/ci-42120921101-candidate-derivation-error.txt);
  derivation JSON output is empty. No store input was fetched/realized or built.
- Rechecked only the three already-retained job logs: they contain the wrapper
  `.drv` and output path, not the underlying `candidateModule` store path or
  actual candidate SHA256. No upload artifact or extra job logs were downloaded.

**Parked: root cause UNKNOWN; actual candidate hash unavailable.** The observed
failure remains wrapper builder exit 1, consistent with its silent exact-byte
check but lacking the diagnostic needed to prove a mismatch. Do not classify
this as an unrelated failure or silently replace the reviewed expected hash.

Owner/action: lead routes any further work to the responsible livepatch/build
owner with separately authorized access to the exact affected builder state.
That owner needs the evaluated candidate input pathname, its actual SHA256 and
whether the guard or following symlink command failed, preserving the original
run/source/expected pin. If original state cannot supply this, assign bounded
diagnostic improvement before a deliberate verification run. This retrieval
package is complete and parked; no automatic retry or infrastructure work follows.

## Final CI and pre-feature staging comparison

Separate bounded comparison authorized by lead; 2026-11-06 local date (2026-11-05
23:01 UTC). Prior retrieval accepted; capacity/session/env verified. Downloaded
**exactly two new job logs**: the requested final-CI failure and one matching
baseline livepatch job. No other logs, builds/evaluations, reruns, SSH, guest/local
VM inspection, source/index mutation or expanded kernel investigation.

| Evidence | Exact source | Job and outcome |
| --- | --- | --- |
| Final CI [42124511747](https://github.com/vpsfreecz/vpsadminos/actions/runs/42124511747) attempt 1 | `fab23ed26aefaed635c41cdb89ff30bf82632c61` | [127590658264](https://github.com/vpsfreecz/vpsadminos/actions/runs/42124511747/job/127590658264), intel-representative-v5, runner1, failure 2026-11-05 23:00:08–23:00:18 UTC |
| Staging CI [41822392601](https://github.com/vpsfreecz/vpsadminos/actions/runs/41822392601) attempt 1 | `54b4313404cea35b58ebb9df951ae75e27c44971` | [126551401270](https://github.com/vpsfreecz/vpsadminos/actions/runs/41822392601/job/126551401270), same intel-representative-v5 label and runner1, failure 2026-11-04 11:43:39–11:43:57 UTC |

Both raw logs' lines **205–212** name the exact same failing derivation and output:
`/nix/store/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv`,
`/nix/store/kmm41zgxg3ai8r84jqm2mk02r4py6cdv-livepatch_7-exact-candidate.ko`,
builder exit **1**. Both later report missing test.log at line **328**. This is
also the exact signature retained for old feature run 42120921101, not merely a
comparison of whole-CI red status. No guest lifecycle tests started in these jobs.

Baseline metadata lists failed livepatch jobs; only its matching representative-v5
log was downloaded. Raw logs and run/job metadata are retained in
`artifacts/ci-42124511747-*` and `artifacts/ci-41822392601-*`.
[Comparison receipt](artifacts/ci-livepatch-baseline-comparison-receipt.json) records
log SHA256/lengths, exact ancestry and changed paths;
[bounded excerpts](artifacts/ci-livepatch-baseline-comparison-excerpts.txt) retain
original line numbers.

Ancestry/source checks used canonical bare Git, fixed SHAs only. Baseline `54b43134`
is an ancestor of **both** implementation base
`d2fe1489f0b0b213fb247aeee6e081d349adaf42` and final `fab23ed2` (each merge-base is
the full baseline SHA). Exactly two commits separate baseline and feature base:
`2951a632c4254a44747a8da326e3dde897eaa0e2` updates packaged gem dependencies;
`d2fe1489f0b0b213fb247aeee6e081d349adaf42` updates nixpkgsUnstable.
Only three paths change: osctl-env-exec Gemfile.lock/gemset.nix update
rake-compiler **1.3.2 → 1.3.3**, and flake.lock changes nixpkgsUnstable
**`0bb2eedc20e4739f29e8045034f2828ad7054f8f` →
`1d060086d60cb76a40cf37109f979d88a5bd6396`** with matching metadata.
No fixture, workflow, livepatch/frozen boot config, Linux/kpatch/livepatch source
change exists in that range. Feature base → final head also has no diff in these
relevant source paths **or flake.lock**. The fixture's expected hash remains the
reviewed `573e8d1e...` pin already recorded above.

**Conclusion: this exact pre-test fixture failure signature is inherited from an
ancestor staging run before the feature.** The same `.drv` identity, output,
exit and matrix job demonstrate that boundary despite the two intervening
unrelated input/package updates. This does not prove the candidate's actual hash,
which remains **unavailable**, or establish the silent guard's underlying root
cause. It does not certify all CI failures or all branch behavior as unrelated.
Responsible livepatch/build owner still needs exact original candidate bytes and
guard diagnostics before changing the pin. No further action was performed.
