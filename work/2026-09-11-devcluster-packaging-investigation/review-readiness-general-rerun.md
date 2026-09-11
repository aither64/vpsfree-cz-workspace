# General review rerun: vpsAdmin SSH readiness follow-up

Reviewed the narrow remediation between the previously reviewed tree at
`3d83a8392cd77fb7e92587ed4ea1a5cc665bd3fb` and final amended head
`9e8783d68fdf40de04683e419d4f373bc27e3730` in `vpsfree-dev-workspace`, using
the mandatory general lane at high risk and `gpt-5.6-sol`/`xhigh`.

## Findings

No Blocking, Important, or Advisory findings.

The prior Important finding is resolved:

- `dev-clusters/vpsadmin/bin/devcluster:733-734` makes the probe explicitly
  noninteractive with `BatchMode=yes` and restricts identity selection with
  `IdentitiesOnly=yes`.
- Every SSH process is wrapped in GNU `timeout`; its duration is the smaller of
  five seconds and the time remaining before the shared 120-second deadline.
  A one-second forced-kill grace handles a child that does not terminate on
  `TERM`.
- Timeout and other non-255 statuses return immediately at lines 740-742, so no
  real seed or node action runs after a stalled or otherwise invalid probe.
  Exit 255 alone retains the intended retry behavior.
- `coreutils`, which supplies `timeout`, is already part of
  `clusterRuntimePath` in `nix/organization-tools.nix:57-70`; this adds no
  undeclared packaged-runtime dependency.
- The regression at `test/devcluster_commands_test.rb:95-105` uses a genuinely
  sleeping SSH process, checks timeout status 124, confirms that no remote
  action ran, and checks lifecycle-lock release. The stub also rejects probes
  missing either noninteractive option.

The amended commit remains a single coherent behavior/test/documentation unit,
and its message describes both the readiness race and the final bounded design.

## Residual gaps

- Live acceptance of this exact head still needs to exercise the original
  bridge-network `No route to host` startup race.
- The focused suite does not directly run the full 120-second repeated-255
  exhaustion path or a final probe whose timeout is reduced below five seconds;
  these branches are simple and were inspected directly.
- The one-second forced-kill grace can make the elapsed wall time slightly more
  than 120 seconds when a final SSH child ignores `TERM`. This is the explicit
  remediation contract recorded in the packet; the README's two-minute wording
  should be understood as the readiness deadline rather than a strict external
  wall-clock guarantee.
