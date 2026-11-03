---
lifecycle: active
---

# Red Hat-family image releases

## Current status

Phase: verified locally; waiting for queued CI before approved integration.
Implementation, independent review and all four local image tests are complete.
No merge or deployment yet.

- Final app head: `1a637e9eac4311adba2b08d60dfa7a17d07bcb52`.
  Tree: `49b8a7879e6b363349ae70808c4cdecc996e578e`.
- Feature published over SSH as `2026-11-03-redhat-image-releases`.
  Target is `staging`, the real remote default; initial master assumption was
  corrected before implementation. Last fetched target:
  `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
- Normal four-image batch passed exit0 in2716.16s; all four per-image results
  passed at exact final head. No owned runner/QEMU/virtiofs processes remain.
  Scoped8GiB override hash unchanged; exact source/system/kernel/initrd/resource
  receipts are in verified-image-tests-result.md.
- Next batch uses architect-approved8GiB memory-only verification for image
  suite only, native guards/jobs2 ceiling, normal RepositorySource lifetime.
  Allfour actual passes remain required; no cached diagnostic counts.
- RSpec `41695511664` and RuboCop `41695511719` passed at final head.
  Image workflow `41695651867` and generic CI `41695511680` were queued at the
  last observation. Organization runner status is unavailable to current API
  permissions; no credential changes were attempted.
- Lead owns Git/configuration coordination; no repository or machine claim is
  held. No production deployment or session lifecycle action is authorized.

## Phase checklist

- [x] All-family upstream inventory and design accepted
- [x] Four image-release commits; syntax, whitespace and hooks pass
- [x] Source-identity and nullable channel fixes committed
- [x] Focused Ruby/Nix regression checks and hooks pass
- [x] Independent final review; two narrow findings resolved and inspected
- [x] All four local image tests passed at final head
- [ ] Queued image/generic CI accepted
- [ ] Final head fast-forwarded into remote staging; ancestry verified
- [ ] Final evidence/handoff retained; session remains open

## Authorization and scope

Initial user request: update Red Hat-family releases in vpsadminos;
"when verified, you can merge it." After root-cause diagnosis the user approved
"aha I see, implement your suggested solution and continue". This resumes
verified staging integration including the proposed source-identity and channel
corrections. No other repository, kernel project, SSH timing change, downstream
pin update or production deployment is in scope.

## Repository and final history

- Bare clone: `repos/vpsadminos.git`, SSH origin
  `git@github.com:vpsfreecz/vpsadminos.git`.
- Feature worktree: `worktrees/2026-11-03-redhat-image-releases/vpsadminos`.
- Clean detached merge checkout prepared at
  `worktrees/2026-11-03-redhat-image-releases/vpsadminos-merge-target`, base
  `dd188397abe37d0bc33f4c5dfb3605206ce5e326`; checkout hook passed.
- Native comparison captured at final head against that base.

Complete final series:

1. `09f209688616b60155e9ac99fa8431a11b9e20a0`: CentOS Stream 9, release 36→38.
2. `a3c7c77459762d1a45f323de0f3f8dd5d8447323`: CentOS Stream 10, release 21→23.
3. `6ede3bd22b2ed28fb28a5a912f3a7daf7743fb6a`: Rocky 9, release 1.1→1.2.
4. `3307df52ea5bf875e1d8a23318a64f569d8b3ebc`: Rocky 10, release 1.1→1.2.
5. `52fba5ee5aac2e171375a780d3860a86e71e5d65`: nullable channel consumer.
6. `1a637e9eac4311adba2b08d60dfa7a17d07bcb52`: captured source identity.

Eight other image recipes were already current. No migrations, repeated update
streams, obsolete approaches or repair commits remain. Four image commits retain
the required split. Parent of the metadata owner remains channel commit52fba5ee.
See [CentOS result](centos-result.md), [Rocky result](rocky-result.md),
[channel result](channel-result.md) and [metadata result](metadata-result.md).

## Review and focused acceptance

Same independent reviewer0, saved gpt-6.1-sol/xhigh/read_only, reviewed all four
lanes at base `dd188397` through original metadata head
`58aae8d54887a14f59fada178a833b33a6ebfa81`. High risk classification for framework
compatibility/provenance and generated OS metadata. See
[expanded packet](review-packet-expanded.md) and
[expanded report](review-result-expanded.md).

Two findings were corrected within the reviewed boundary: legacy Git defaults
now have priority1100 below known-source defaults1000 and explicit settings100;
security evidence honors authoritative/explicit revision rather than copied Git
HEAD. Real-module regressions cover capture A with copied HEAD B, full/short/null
overrides, native provider identity and legacy fallback. The original conflict
was reproduced before correction. Lead inspected the exact two-file narrow fix,
then accepted it under the review skill without an automatic full rerun.

Old/new heads and exact diff are retained in metadata-result.md and
[metadata-review-fix.patch](metadata-review-fix.patch), SHA256
`41e5e7e4c8316eab34a08b68cc06df2b6e1ebcddcc9404398a2fd979ce3c8789`.
Old head is retained at exact-session local backup branch
`2026-11-03-redhat-image-releases-reviewed-metadata`; it is not claimed integrated.

Focused checks: 42 Ruby examples pass; source-version and real known/null channel
Nix checks pass, including final real-module evidence regressions. Final hooks
Nixfmt/RuboCop/commit message and committed whitespace checks pass. Ruby source
unchanged by narrow Nix corrections. Native libosctl dependency, shell commands,
logs/hashes and reviewed/final mapping are in metadata-result.md. Existing CI
launcher packages the updated local runner Ruby; no packaging/workflow fix needed.

## Final normal verification batch

Artifact [verification-memory.nix](verification-memory.nix), SHA256
`adef87cd3c928b4a5687150fc5a43f271e64f1fceeb64745bcc4639aad62b582`, contains only:

```nix
{ config, lib, ... }:
{
  boot.qemu.memory = lib.mkIf (lib.hasAttrByPath [
    "boot"
    "zfs"
    "pools"
    "tank"
    "datasets"
    "image-scripts/build"
  ] config) (lib.mkForce (8 * 1024));
}
```

Architect rationale/limits are appended to [design.md](design.md). This is a
supported resource-only test environment; peak sufficiency is unmeasured, all
assertions/timeouts remain, and no 24 GiB success or kernel diagnosis is implied.
OOM and actual failures still require investigation. No reserve bypass.

Normal local-code invocation uses `nix develop .#test-runner --command env`,
sets native RUBYLIB inside the command (the shell overwrites an outer value),
sets exact `TEST_RUNNER_REPO_REV`, sets only the memory VPSADMINOS_CONFIG above,
and runs all four `image-scripts/test@...` cases with `--jobs 2 --stop-on-failure`.
State: `/tmp/redhat-image-releases-2026-11-03-verified8g`.
Logs/result: verified-image-tests.log and verified-image-tests-result.md.
The utility records exact command, generated resource requirements, captured
source, system/kernel/input paths and per-case results. Source-info metadata is
produced by the real runner; no manual source metadata override is used.

Source-only final push did not trigger the image path filter, so image workflow
41695651867 was dispatched explicitly at final head. Superseded old-head image
run41683688934 was cancelled; no other branch workflows were cancelled.

## Earlier failures and diagnostics

- Original linked-worktree evaluation failed before boot with
  `cannot coerce null to a string: null`. Cause and approved correction:
  [root cause](root-cause-report.md),
  [detailed diagnosis](verification-diagnosis.md). Resolved by committed code.
- First fixed 24 GiB normal batch reached VM startup but was interrupted after
  kernel watchdog warnings; three cases never started. This was not an RPM
  failure. [Result](fixed-image-tests-result.md), artifacts under
  fixed-image-test-artifacts/centos-10-stream. Exact children were stopped.
- First cached diagnostic was incorrectly stopped by its watcher after57s,
  before a watchdog event. Parent acknowledged and corrected stop conditions.
- Longer cached diagnostic reached root shell after slow boot, with no watchdog
  trace. Its later checkout check failed because the shared source was unrooted
  and GC collected it during the diagnostic: deletion20:08:32, mount20:14:11,
  guard failure20:14:15. The guard correctly checks required directories, not
  Git metadata. [Observation](boot-observation.md),
  [trace result](boot-trace-result.md). No guard weakening or kernel/security
  change was needed. Normal CLI source lifetime covers the whole batch.
- No diagnostic counts as a passing image test. Historical Fedora45 GitHub null
  error was not found in retained attempts; the located SSH failure is separate.

## Next action and retention

Wait for the normal four-case result and exact-head CI, resolve concrete failures
within scope, then fresh-check staging and the complete final series. Read the
selected runtime coordination guide before the approved merge. Prepare hooks
outside ownership; acquire one short repository claim only for fresh target
check, fast-forward merge/hooks, SSH push and remote proof, then release before
CI/records/cleanup. Preserve unrelated shared workspace changes and all feature
refs. No machine deployment/claim is needed.

Useful project documentation is docs/os/test-framework-integration.md; session
plan/design/evidence own temporary verification instructions. Reusable setup and
cached-lifetime lessons are in
notes/vpsadminos/2026-11-03-local-runner-verification-environment.md.
Retain compact evidence; stop owned processes natively before removing disposable
test data. No archive/delete/stop or delayed session cleanup is authorized.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-redhat-image-releases/)

## Memory metadata setup failure

Global mkForce8GiB conflicted with a separate fixture's mkForce4GiB during
metadata-all evaluation, before any selected case. Receipt final-image-tests-result.md,
full final-image-tests.log retained. This is not an app/image failure. The
operational override will select only the image suite using its existing
`boot.zfs.pools.tank.datasets."image-scripts/build"` marker. Require successful
normal metadata/list evaluation, four8GiB resources and unchanged non-image
fixture before launching a fresh batch. No global stronger priority or new test
framework. Old dbb827... override hash is superseded, not current accepted input.

## Progress response verification-setup-churn

Concern accepted: premature cached diagnostic stop, unrooted cached source and
unscoped memory override caused setup churn without an image pass. Each cause
is now resolved operationally; no further setup/kernel/source expansion planned.
Scoped metadata preflight PASSED99s with selected8192 and preserved4096 fixtures.
One normal rooted four-image batch launched at unchanged reviewed source. Next
observable milestone is first completed per-image result, then allfour results.
Concern resolved after actual CentOS9/10 image passes in the normal rooted batch.

## Image verification milestone

Normal scoped8GiB batch delivered successful CentOS Stream9 (1299.36s) and
CentOS Stream10 (1300.69s) at exact final app head. Both actual image commands
and assertions passed, clearing prior source-evaluation/diagnostic-setup issues.
Rocky9 and Rocky10 admitted next in same rooted invocation, each8GiB RAM/shm,
4CPUs. No setup or source changes; source root remains held across whole batch.
Progress response verification-setup-churn resolved with two delivered image
passes. Remaining: Rocky9/10 results and relevant exact-head CI before merge.

- Rocky9 passed in1391.3s. Normal batch now3 successes/0 failures; Rocky10
  still active. No source/configuration changes during verification.

## Ready pending external CI

CentOS9/10 and Rocky9/10 all passed:1299.36s,1300.69s,1391.30s,1415.45s.
Normal rooted batch exit0, total2716.16s. [Receipt](verified-image-tests-result.md)
and verified-image-tests.log retain evidence. Scoped module hash stayed
adef87cd3c928b4a5687150fc5a43f271e64f1fceeb64745bcc4639aad62b582.
Fresh fetch confirms staging stilldd188397, final feature1a637e9e clean; complete
six-commit series and whitespace inspected again, no migrations/obsolete streams.

RSpec41695511664 and RuboCop41695511719 passed. Image41695651867 and generic
CI41695511680 remain QUEUED at final head. No approval is missing: integration
is already authorized. Native CI utility will observe queued workflows and
notify lead automatically; resolve any concrete failures before integration.
Do not hold a repository claim while waiting for CI or ask user to restart.
After success, prepare hooks outside claim, recheck target/head/history, capture
comparison, acquire short vpsadminos repository claim, ff-only merge/SSH push/
remote proof and explicit release. Leave session open and preserve feature refs.
