# Scope and proportionality review: SSH readiness follow-up

Lane: scope and proportionality
Reviewed range: `d2380cbe77f711627ba461ef9359724b6255a5db..3d83a8392cd77fb7e92587ed4ea1a5cc665bd3fb`
Repository: `worktrees/2026-09-11-devcluster-packaging-investigation/vpsfree-dev-workspace`

## Findings

No Blocking, Important, or Advisory findings.

The change is proportional to the demonstrated startup failure. It adds one
provider-local readiness helper, invokes it only before the existing services
seed check and regular-node refresh action, and keeps the actual remote actions
one-shot. The fixed 120-second policy avoids a new configuration surface, while
the harmless `true` probe delegates SSH and authentication readiness to OpenSSH
instead of adding a separate network or protocol implementation. The focused
actual-command regression covers a transient exit 255 and confirms that the
three remote refresh actions still execute once. The two documentation lines
describe the resulting operator-visible behavior without expanding the
supported contract.

I also checked the constructed OpenSSH invocation because `ssh_cmd` places the
additional probe arguments after the destination. The deployed OpenSSH 10.5p1
parses `-n` and `-o ConnectTimeout=3` as client options in that position, so the
probe remains the intended remote `true` command.

## Residual gaps

- The exact 120-second exhaustion path and immediate propagation of a non-255
  probe result are not automated. Exercising the real timeout would make the
  focused suite materially slower, while adding timeout injection solely for a
  test would enlarge this narrow change; inspection covers both branches.
- OpenSSH uses exit 255 for permanent client/authentication errors as well as
  transient transport failures. Such a persistent error can therefore delay
  the final failure by the bounded readiness window, but it does not retry a
  remote mutation or weaken failure propagation.
- The committed head has not yet repeated the live vpsAdmin start that exposed
  the race. Deployment and live startup acceptance remain necessary to confirm
  that the two-minute window is sufficient on the real bridge VM.
