The read endpoint inherited by the generated Bash barrier is explicitly
blocking before its existing FD4 handoff. Ruby's pipe constructor leaves
O_NONBLOCK set; the supported io/nonblock setter clears it for this endpoint.
The retained native shell error is EAGAIN. No local reproduction was run.

Both existing barrier cases remain exact: successful release must permit
generation, while closed release must refuse without storage/generation.
All ten methods, assertions, generated shell mapping, five-second bounds and
child cleanup remain byte-identical. Only the require, rationale comment and
nonblock assignment were added.

Root-owned contract prose and every other tracked path remain unchanged.
Original source freezes and both native failures remain immutable.
Packet preparation stopped on a control-hashing variable error after ten
controls. Those bytes were retained; the remaining controls were appended
without overwriting them. This was not test or product execution.

Tests are UNRUN; the frozen draft awaits lead inspection/publication and
new exact hosted K/E evidence. No local checks or runtime/Git operations.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/
