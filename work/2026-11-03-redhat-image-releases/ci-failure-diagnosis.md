# Generic CI livepatch fixture failure

2026-11-03; architect0; read-only investigation. Feature head
`1a637e9eac4311adba2b08d60dfa7a17d07bcb52`; baseline
`dd188397abe37d0bc33f4c5dfb3605206ce5e326`.

## Finding

The two reported failures reproduce the **same pre-existing fixture build** on
the same matrix configurations. They do not demonstrate a regression from the
release updates or source-identity/security-evidence changes. The livepatch
tests never start. The failed fixture remains a failed required check; this
finding does not turn the matrix green or authorize bypassing it.

| Configuration | Baseline run 41666620193 | Feature run 41695511680 |
| --- | --- | --- |
| amd-low-memory-v5 | [job 126034272155](https://github.com/vpsfreecz/vpsadminos/actions/runs/41666620193/job/126034272155), failure 16:02:29 UTC | [job 126191147517](https://github.com/vpsfreecz/vpsadminos/actions/runs/41695511680/job/126191147517), failure 20:39:44 UTC |
| amd | [job 126034272312](https://github.com/vpsfreecz/vpsadminos/actions/runs/41666620193/job/126034272312), failure 16:01:25 UTC | [job 126191147584](https://github.com/vpsfreecz/vpsadminos/actions/runs/41695511680/job/126191147584), failure 20:40:18 UTC |

All four job logs establish their exact checkout head and report builder exit
1 for the identical derivation and output:

```text
/nix/store/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv
/nix/store/kmm41zgxg3ai8r84jqm2mk02r4py6cdv-livepatch_7-exact-candidate.ko
```

This is an immutable Nix recipe/declared-input identity comparison, not merely
a match of job labels or error wording. The retained baseline Intel job
126034272162 independently reports the same derivation. Utility reports for
current amd-fresh and amd-scale-aged-v6 also match; no further matrix sampling
is needed to establish this relation.

## Failure chain and limits

1. [CI workflow lines 428–434](https://github.com/vpsfreecz/vpsadminos/blob/1a637e9eac4311adba2b08d60dfa7a17d07bcb52/.github/workflows/ci.yml#L428-L434)
   exports the expected digest, then builds the `corrected` fixture under
   `set -euo pipefail`.
2. [Fixture lines 13–18 and 47–50](https://github.com/vpsfreecz/vpsadminos/blob/1a637e9eac4311adba2b08d60dfa7a17d07bcb52/tests/fixtures/livepatch/default.nix#L13-L50)
   select the current package's `livepatch_7.ko` against the frozen boot base.
   The wrapper checks the hard-coded SHA256
   `573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d`
   with `sha256sum --check --status`, then creates an output symlink.
3. That wrapper exits 1. The checksum/readability check is the leading cause
   inferred from the two-command recipe and silent failure. The logs do not
   expose the actual candidate hash or identify the precise failed command;
   `--status` suppresses checksum diagnostics. A mismatch, unreadable/missing
   module, or other builder problem cannot be distinguished conclusively from
   these logs alone.
4. Shell execution stops before predecessor fixture preparation and before
   `test-runner.sh` at workflow line 471. The later missing `test.log` is a
   consequence, not another test failure. The downloaded feature artifact
   contains only the expected digest (64 bytes) and empty candidate-path file.

Base-to-head inspection finds no changes to the workflow, fixture, boot-base
configuration, kernel recipes or `flake.lock`. The candidate is constructed by
direct `import ../../../os` and selects `system.build.livePatches`; the new
runner snapshot transport and framework source module are not invoked here.
The edited `os/modules/misc/version.nix` participates in OS evaluation, but its
[security-evidence JSON revision](https://github.com/vpsfreecz/vpsadminos/blob/1a637e9eac4311adba2b08d60dfa7a17d07bcb52/os/modules/misc/version.nix#L268-L279)
does not feed the livepatch recipe. Crucially, the observed unchanged failing
derivation confirms that these edits did not change this fixture's declared
build inputs.

The derivation is absent from the local store. No candidate was built or
downloaded, and no full transitive derivation graph or actual module bytes were
retrieved. Equal input-addressed derivations do not establish reproducible
output bytes, cache integrity, or successful runtime qualification.

## Smallest next action

Keep the reviewed release/source-identity changes unchanged. Have the lead
arrange a bounded read-only inspection of this existing derivation on a runner
that retains it: preserve its build command and candidate input path, test that
module's readability, and record its actual SHA256 plus input derivation/store
identity. This does not require another kernel build or a workflow retry.
If existing evidence cannot be recovered, a separately authorized diagnostic
change should expose the failed checksum check and actual candidate digest
before another attempt.

Use that evidence to repair the existing livepatch fixture/package contract.
Do not derive the expected pin from whichever candidate happens to be built or
simply replace it to obtain a green check: the fixture explicitly requires
independently established bytes. Any livepatch repair/qualification is outside
this investigation's application-edit authorization. The lead must resolve
the required-check disposition before merging; the continuing image workflow
does not resolve this fixture failure.

## Evidence retained

- `ci-root-cause/ci-amd-low-memory-v5-attempt-1-job-126034272155.log`:
  checkout lines 107–123, failure lines 204–209, missing test log line 326.
- `ci-root-cause/ci-amd-attempt-1-job-126034272312.log`: same line ranges.
- `ci-job-126191147517.log`: checkout lines 107–126, failure lines 207–212,
  missing test log line 329.
- `ci-job-126191147584.log`: checkout lines 107–123, failure lines 204–209,
  missing test log line 326.
- `ci-artifact-126191147517/livepatch-corrected-{sha256,path}.txt`.

No application edits, builds, retries, CI mutations or repository claims were
made. Lead owns tracking integration and ongoing utility monitoring.
