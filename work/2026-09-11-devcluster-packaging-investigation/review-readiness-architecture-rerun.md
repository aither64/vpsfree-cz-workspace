# Architecture and repetition review rerun: vpsAdmin SSH readiness follow-up

Reviewed the remediation from
`3d83a8392cd77fb7e92587ed4ea1a5cc665bd3fb` to
`9e8783d68fdf40de04683e419d4f373bc27e3730` in
`worktrees/2026-09-11-devcluster-packaging-investigation/vpsfree-dev-workspace`
using the architecture and repetition lane of the mandatory change review.

## Findings

No Blocking, Important, or Advisory findings.

The remediation remains inside the vpsAdmin provider's existing refresh and
transport boundary. The readiness helper derives the target from
`machine_host` and the provider's normal connection settings from `ssh_opts`,
then adds probe-specific noninteractive and process-timeout policy at the one
call site that needs it. Constructing this invocation separately from
`ssh_cmd` is appropriate: adding the timeout or `BatchMode` to `ssh_cmd` would
silently change the public interactive SSH command and every remote mutation.
The shared host and option helpers retain the parts that must stay equivalent.

The five-second attempt bound, one-second forced-kill grace, and remaining
120-second budget form one localized policy. GNU `timeout` comes from the
provider package's existing coreutils runtime path, so the helper does not add
an undeclared dependency or a consumer-side requirement. The hanging-process
regression exercises the real process boundary, confirms that no remote action
runs, and checks lifecycle-lock release.

No equivalent bounded readiness behavior exists elsewhere in the repository.
The vpsAdminOS provider does not own the post-seed refresh sequence, so moving
this policy into the shared runner or a cross-provider helper would still be
speculative. Public CLI arguments, dispatcher registration, runner readiness,
and cluster state contracts remain unchanged.

## Residual risks and test gaps

- The automated transient-transport regression still uses local port
  forwarding. Repeated bridge startup is the material acceptance check for the
  original `No route to host` failure.
- The suite covers a transient node exit 255 and a hanging services probe. It
  does not directly exercise transient services exit 255, expiry of the full
  120-second budget, or a prompt non-255 SSH failure. These branches share the
  reviewed helper and do not indicate a separate architecture concern.
- Probe and action counts are asserted, but their complete event order is not.
  The committed call structure makes the ordering explicit; the test would be
  less precise if that orchestration is later refactored.
