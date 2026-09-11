# Architecture and repetition review: vpsAdmin SSH readiness follow-up

Reviewed `d2380cbe77f711627ba461ef9359724b6255a5db..3d83a8392cd77fb7e92587ed4ea1a5cc665bd3fb`
in `worktrees/2026-09-11-devcluster-packaging-investigation/vpsfree-dev-workspace`
using the architecture and repetition lane of the mandatory change review.

## Findings

No Blocking, Important, or Advisory findings.

The new readiness behavior has one clear owner: the vpsAdmin provider's refresh
orchestration. `wait_for_machine_ssh` reuses that provider's existing machine
address, network-mode, SSH-option, and command abstractions. It is called before
the services seed query and before each node preparation action, while the
actions themselves remain single-shot. Adding this behavior to the shared Ruby
runner would broaden its boot-readiness contract and require it to know
provider-side SSH routing that it does not currently own.

There is no equivalent readiness loop elsewhere in the organization repository.
The vpsAdminOS provider has similar SSH command glue, but it does not run this
post-boot refresh workflow. Extracting the new helper across providers would be
speculative and would couple separately packaged provider scripts. The changed
CLI behavior remains behind the existing `start`, `refresh`, and services-update
paths, so the stable workspace dispatcher and its public state, lock, socket,
and package-generation interfaces do not change.

## Residual risks and test gaps

- The focused command regression covers one transient SSH exit 255 for `node1`
  in local-network mode and confirms that all three remote actions run once. It
  does not exercise a transient services-VM failure, the 120-second terminal
  timeout, or immediate propagation of a non-255 probe result. These are small
  branch-coverage gaps in one bounded helper rather than evidence of a design
  defect.
- The test checks probe/action counts rather than recording their exact order.
  The committed call sites make the ordering direct, but a future refactor could
  weaken the test's ability to detect an ordering regression.
- The reported production-like failure used bridge networking. The automated
  regression uses local forwarding, so repeated bridge start acceptance remains
  the material validation for the original `No route to host` scenario.
