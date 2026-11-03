Identify the problem with the failing vpsAdminOS livepatch tests and suggest a
solution. The user explicitly requested a new workspace session with a full
team. Use the selected Full team preset with retained settings and ordinary
architect/implementer/reviewer ownership. This is investigation and a concrete
solution proposal, not authorization for implementation, merges, deployments,
changing integrity pins, or lifecycle actions. Prepare enough evidence and a
reviewable recommendation for the user to decide the next step.

Initial evidence from the Fedora 45 image work (all facts below are leads to
verify independently against canonical source and GitHub; do not access another
session's files, worktrees, team, transcript, or credentials):

- vpsfreecz/vpsadminos general CI run41666620193 on
  dd188397abe37d0bc33f4c5dfb3605206ce5e326 has nine Livepatch lifecycle failures.
  The Fedora addition only adds image-scripts/images/fedora-45/{build,config}.sh
  and moves Fedora latest/stable registration in os/configs/image-repository.nix.
  Its actual image workflow41666620408 passed the Fedora45 image test.
- All nine lifecycle jobs fail BEFORE test-runner/VM startup, at
  nix-build tests/fixtures/livepatch -A corrected. Derivation:
  /nix/store/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv
  Expected output:
  /nix/store/kmm41zgxg3ai8r84jqm2mk02r4py6cdv-livepatch_7-exact-candidate.ko
  Builder exits1. The fixture currently performs an exact sha256sum check
  followed by symlink creation; silent checksum failure is inferred, but actual
  module digest has not been measured. Do not weaken/re-pin blindly.
- Expected candidate module SHA256:
  573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d.
  AMD artifact13248340186 contains that pin plus empty output-path file. Missing
  test.log failures in evaluation/upload are secondary to preparation failure.
- Current failed job IDs:126034272083 amd-scale-aged-v5,
  126034272129 amd-low-memory-v6,126034272155 amd-low-memory-v5,
  126034272162 intel,126034272226 amd-scale-aged-v6,126034272312 amd,
  126034272377 amd-fresh,126034272602 intel-representative-v6,
  126034272704 intel-representative-v5.
- Direct pre-existing same-error proof: CI41072532280 on ancestor
  05201326975fc19d20a545c52f651cce0420dbc9, AMD job124217753063,
  failed at2026-10-30T17:42:39Z on identical derivation/output. All nine lifecycle
  jobs failed there while native suite passed. Older run40296454457 on d9be8c...
  had lifecycle green; inspect exact revisions rather than guessing regression.
- Between Fedora base5918f94e5e4eef3733b60aca4e03c1a6c0d43748 and headdd188397a,
  relevant .github/workflows/ci.yml, full flake.lock graph, livepatch fixture
  tree, tests/configs/vpsadminos/livepatch-6.12.95-boot-base.nix,
  os/packages/linux tree and os/overlays/packages.nix are identical.
- vpsadminos/staging now integrates Fedora commitdd188397abe37d0bc33f4c5dfb3605206ce5e326
  (remote proof2026-11-03T16:44Z). Fetch fresh canonical defaults for your own
  session; do not reuse the Fedora branch/worktree.

Use independent session-owned worktree and required workspace/repository
procedures. Architect should determine the dependency/fixture provenance,
actual candidate identity vs expected pin, likely regression boundary and
smallest sound correction. Implementers can own bounded independent diagnostic
packages, including workflow/fixture lineage and candidate reproducibility.
Bound expensive checks, use fresh Luna/low utilities for long/uncertain builds,
and stop unexpected local kernel builds under the workspace policy. Prefer
already-published derivations/artifacts; a full kernel build is not implied by
this investigation request. Preserve integrity and existing recovery contracts.

Deliver a concise evidence-backed root cause (or precisely bounded uncertainty),
a concrete proposed solution with affected files/compatibility/test plan, and
remaining user decisions. Do not turn the investigation into unrelated livepatch
architecture changes. No cross-session communication grant is included; the
initial evidence above is sufficient to begin independently. Keep session open.
