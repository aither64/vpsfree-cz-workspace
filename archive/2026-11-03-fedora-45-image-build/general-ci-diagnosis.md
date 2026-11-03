# General CI diagnosis

Observed 2026-11-03T16:41:00Z by implementer2. Bounded read-only source
diagnosis; no CI rerun, source edit, build, merge or deployment. Session identity
matches the trusted workspace binding; both `DEV_SESSION_*` variables were absent.

## Conclusion and remaining acceptance

All nine Livepatch lifecycle failures are the same pre-test fixture failure,
also observed on an ancestor before the Fedora change. They do not establish a
Fedora 45 regression. This is a baseline livepatch verification problem, not
evidence of a transient runner/network fault. The current native suite remains
in progress, so general CI is not green and its remaining result is unknown.

Exact reviewed range in `vpsfreecz/vpsadminos`:

- Base: `5918f94e5e4eef3733b60aca4e03c1a6c0d43748`.
- Head: `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
- [General CI 41666620193, attempt 1](https://github.com/vpsfreecz/vpsadminos/actions/runs/41666620193):
  in progress; OS/cache build successful, nine lifecycle jobs failed, native
  suite job `126034272635` still running at the observation above.
- [Image CI 41666620408](https://github.com/vpsfreecz/vpsadminos/actions/runs/41666620408):
  completed successfully on that exact head; build, changed-image detection
  and changed-image test jobs all succeeded.

Shortest valid path: retain the successful exact-head Fedora image evidence and
this baseline-failure exception; do not rerun or repair livepatch as part of the
image change. The lead decides acceptance under the existing conditional merge
approval. Observe the existing native suite through its current owner and
diagnose any additional failures before claiming general-suite success. This
report neither accepts an unseen native-suite result nor grants merge approval.

## Shared failure and artifact evidence

Every failed job aborts at `nix-build tests/fixtures/livepatch -A corrected`,
before `./test-runner.sh`, any guest boot, or Fedora recipe execution:

```text
error: Cannot build '/nix/store/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv'.
       Reason: builder failed with exit code 1.
       Output paths:
         /nix/store/kmm41zgxg3ai8r84jqm2mk02r4py6cdv-livepatch_7-exact-candidate.ko
```

The unchanged `tests/fixtures/livepatch/default.nix` builds this fixture with
only an exact SHA-256 assertion followed by creation of the output symlink.
Its expected module digest is
`573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d`.
The silent exit is consistent with the assertion's `sha256sum --check --status`
failure; the logs do not expose the actual module digest. No assertion or pin
change is justified by this diagnosis.

Downloaded [AMD artifact 13248340186](https://github.com/vpsfreecz/vpsadminos/actions/runs/41666620193/artifacts/13248340186)
contains only `livepatch-corrected-sha256.txt` with that expected digest and an
empty `livepatch-corrected-path.txt`. There is no native `test.log`, because the
preparation command failed first. Consequently “Evaluate test results” also
fails with “Test log ... not found”; that is a secondary effect.

All nine raw job logs were downloaded successfully and contain the exact
derivation/output failure above plus the secondary missing-log error:

| Lifecycle label | Job ID |
| --- | --- |
| amd-scale-aged-v5 | 126034272083 |
| amd-low-memory-v6 | 126034272129 |
| amd-low-memory-v5 | 126034272155 |
| intel | 126034272162 |
| amd-scale-aged-v6 | 126034272226 |
| amd | 126034272312 |
| amd-fresh | 126034272377 |
| intel-representative-v6 | 126034272602 |
| intel-representative-v5 | 126034272704 |

Job URLs use the general run URL above plus `/job/<job ID>`. Raw local logs are
`/tmp/fedora45-general-ci-job-<job ID>.log`; extracted artifact files are under
`/tmp/fedora45-general-ci-artifact-amd/`. Downloads took seconds; no long wait or
watcher was launched, leaving the single utility slot available to implementer1.

## Baseline and source/input identity

[Earlier CI 41072532280](https://github.com/vpsfreecz/vpsadminos/actions/runs/41072532280)
ran on `05201326975fc19d20a545c52f651cce0420dbc9` on 2026-10-30. Git confirms
this commit is an ancestor of the Fedora feature base. All nine lifecycle jobs
failed there, while its native suite succeeded. Its
[AMD job 124217753063](https://github.com/vpsfreecz/vpsadminos/actions/runs/41072532280/job/124217753063)
failed at 17:42:39Z on the **identical** `vg23dzka...` derivation and
`kmm41zgx...` output above, then reported missing `test.log`. This is direct
same-error evidence predating the Fedora feature, not an inferred green rerun.
Raw log: `/tmp/fedora45-general-ci-prior-amd.log`.

The complete feature diff contains only the new Fedora 45 `build.sh` and
`config.sh`, and the Fedora registration/tag change in
`os/configs/image-repository.nix` (+29/-1). Relevant source and input objects
are identical between the exact base and head:

| Object | Identical Git object ID |
| --- | --- |
| `.github/workflows/ci.yml` | `b4bab8fc149f1278085adb1eddc672c463a5befd` |
| `flake.lock` (complete locked input graph) | `785582c0255f718d88b55498e60f16c3d1b3b303` |
| `tests/fixtures/livepatch` tree | `e8b29b7ce808b53ca4dc40c020a4382e24dd9067` |
| `tests/configs/vpsadminos/livepatch-6.12.95-boot-base.nix` | `afa4119b1c3f9be9e1cf6dde9dac2d03723b34d8` |
| `os/packages/linux` tree | `3a4dec1d72deebff9839ea91ed7efddea1cc1017` |
| `os/overlays/packages.nix` | `a1402a3b25acc3cd4d804f2e0d8415f9b89905c1` |

The fixture/workflow/boot-base/Linux paths also have no diff between the earlier
failed ancestor and the current base. No exact-base workflow was rerun. The
same pre-existing derivation failure, unchanged feature inputs, and successful
exact-head image CI provide the bounded causal evidence needed here; further
livepatch investigation belongs to separately authorized work.

The lead owns shared state/portal updates. This investigation adds no project
documentation or code change. Stable session link:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-fedora-45-image-build/
