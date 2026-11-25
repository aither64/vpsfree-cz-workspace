# No-guest bridge-helper diagnostic

2026-10-31, architect0. User-authorized root-cause investigation; no runtime
operations or application edits. Run once as UID1000, using the exact KB runner
Ruby `/nix/store/rc5ywk2fcw0939v498ykjns5sirmlhr0-ruby-3.4.9/bin/ruby`.

Command: that Ruby executes `helper-proc-diagnostic.rb` from this directory.
The prototype invokes `/run/wrappers/bin/qemu-bridge-helper
--kb-proc-diagnostic-invalid` once, with no other arguments. It uses private
anonymous pipes only. A prefilled stderr pipe holds the usage write long enough
to inspect only this direct child; closing/draining it lets the helper exit.
No ptrace, stop signal, sudo, TAP/bridge operation or changed permission is used.

Safety source: installed wrapper embeds
`/nix/store/b3szf0g8xd8z7r1433l780b3m1cc4jys-qemu-host-cpu-only-10.2.4/libexec/qemu-bridge-helper`.
Its derivation selects QEMU10.2.4. Upstream tag `v10.2.4`,
`qemu-bridge-helper.c:main`, rejects the unknown argument and returns failure
before ACL parsing, AF_INET control socket, `/dev/net/tun` or any network ioctl.
All three derivation patches concern guest-agent commands, macOS icons and
`target/i386/cpu.c`; none touches this path. The setuid wrapper's existing
privilege transition is explicitly authorized for this diagnostic.

Collect command argv, caller credentials, helper selected proc status fields,
stat/start-time, proc-directory owner, exe/cmdline read outcome, task child-list
read outcome, ordinary wait status and final proc absence. Do not record full
environment. A same-UID pipe-blocked Ruby child supplies the readable positive
control. The invalid helper must exit1 with usage; no network argument is given.

Bound: two short owned processes, at most five seconds for each observation;
ensure drains/closes the private pipe and waits for the direct child. No retry
or forced termination. Unexpected failure retains exact evidence and stops this
diagnostic package. This known quick check runs inline; no guest/build/watcher.
Evidence proves current helper mechanism, not PID2989738's historical identity.
