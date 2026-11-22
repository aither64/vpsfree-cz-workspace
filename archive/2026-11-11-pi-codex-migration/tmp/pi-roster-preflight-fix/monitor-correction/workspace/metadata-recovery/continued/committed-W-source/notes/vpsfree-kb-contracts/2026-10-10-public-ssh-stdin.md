# Public SSH input must reach the remote command

The reduced verifier sent resource scripts to `vpsfree-kb-devcluster ssh
SLUG services -- sh -s` on standard input. At K9c551c6 the launcher called
`Engine#ssh` without its existing `input:` argument, so Open3 sent empty input.
The command exited0 and printed only a newline; guest resource assertions then
failed. Public start and guest identity/current-system attestation had succeeded.

Verify script input through the actual CLI and transport child, not only a
mocked verifier command result. Ruby Open3 accepts a supplied IO through
`IO.copy_stream`; forwarding that IO avoids a separate whole-input buffer.
Terminal input needs an explicit contract so ordinary terminal commands do not
wait for EOF. This diagnosis does not authorize replaying a failed campaign.
