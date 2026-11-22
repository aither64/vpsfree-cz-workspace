# Short state roots for isolated VM tests

Related initiative: work/2026-10-05-network-ipv4-left-counter/.

The vpsAdmin test-runner --state-dir under the full tracking path made an OsVm
shell socket address 141 bytes long. UNIXServer rejected it (108-byte maximum)
before feature assertions. The selector inventory and environment build had
completed; this was not evidence of an admission or routing failure.

The pinned Executor puts sockets in state_dir/socks. OsVm appends an eight-byte
hash and machine/shell filename. Use the supported --state-dir option with a
short, uniquely created private directory for isolated VM tests, for example a
mktemp -d /tmp/n6-XXXXXXXX result. Record its exact owner/session/revisions/test
selector and path with the initiative logs, and retain failed evidence. Reuse
same-head selector inventory rather than reevaluating it without a reason.

Do not apply this workaround to persistent development clusters or KB capture
providers. Their generation, transition-lock and ownership contracts remain
required; a random path or absence preflight does not satisfy those contracts.
Do not delete another operation's state or sockets.
