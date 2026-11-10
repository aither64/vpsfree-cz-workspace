# Bounded interrupted-verification diagnosis

Source remains clean and frozen at
`9ad4f869699fee02e2bc4c8f3cceccdea95d8a29`. No fixture or production code was
changed, and no VM retry was launched during this diagnosis.

## What the complete evidence establishes

`refresh-verification-2026-11-02-01.log`: 2231 lines / 248374 bytes, SHA256
`256157d2a886dae352992234730f15ad95ac520f7ec4465ba19d9847a99544bf`.
The original log and incomplete cancellation result are preserved.

- Historical reconciliation/refusals, new-host ingestion, exporter output,
  initial messages access and every fresh-directory/file/pipe mode check have
  finished success banners. All protected-write/escalation denials also finish.
- The last unfinished driver operation is line 2192: SSH running
  `touch ~/allowed-home-write /tmp/allowed-temp-write`. The SSH server subsequently
  records session disconnect/close, but the driver never records completion.
- The guest-67s Shutdown messages are the UID1000 **user manager** exiting after
  logout. They are not VM poweroff, test cleanup, VM success or Nix completion.
- Group assertions, remaining pipe denial, SSH policy/home-key/forwarding tests
  and rotation are not reached. There is no natural assertion failure. Parent
  cancellation establishes only incomplete verification.

## Completed proxy integration receipt

At this exact frozen head the evaluated integration derivation is
`/nix/store/jv9pghphqs0qb8aafyk34bvnqmaa2z3w-prometheus-query-access-integration.drv`.
Its output
`/nix/store/4q80ppz76vk8d8xivb356bvnsbdikawx-prometheus-query-access-integration`
passes `nix-store --check-validity`; `nix-store --query --deriver` returns that
same evaluated derivation. The captured log also contains the integration's
success message. This is completed integration evidence, not a proxy host-build
receipt. Reuse it only while the exact evaluated derivation remains identical.
Neither host-build command was run by the interrupted batch.

## Pinned driver inspection and bounded comparisons

The pinned nixpkgs driver sends `timeout ... bash -c COMMAND | (base64 -w 0; echo)`
over its guest shell connection, reads the stdout frame, and only then sends
`echo ${PIPESTATUS[0]}` for status. Its next-frame reader blocks on socket reads.
The guest shell is Bash reading the raw `/dev/hvc0` TTY with echo disabled.
All fixture SSH commands inherit that stdin; none currently use `-n`.

Two disposable native comparisons used OpenSSH10.5p1, synthetic keys, an
unprivileged loopback test sshd and the driver's command/status framing. The
first used a socket control channel; the second corrected that model to a raw
PTY with Bash reading the terminal pathname. In **both** comparisons, inherited
stdin and `-n` each created the silent-command marker and returned status0.
Logs: `ssh-stdin-probe-2026-11-02.log` and `ssh-tty-probe-2026-11-02.log`.
Each probe took less than one second, with 3s startup, 2s command/read and 1s
owned-child shutdown bounds. No production endpoint, key or service was used.

The comparison does not reproduce the guest hang or prove `-n` as its causal
fix. The native server lacks the VM's root/PAM/user-session/virtio environment;
server disconnect alone also cannot distinguish client exit from a missing
driver stdout/status frame. No actual code defect is established from the
remaining evidence. Adding a speculative fix or increasing timeouts is unjustified.

## Shortest remaining recovery

Retain the exact proxy integration result and run only the existing affected
logger check in a fresh utility, if the lead selects one controlled diagnostic
rerun:

```sh
nix build --no-write-lock-file --no-link -L --keep-failed \
  .#checks.x86_64-linux.log-reader-access.vmTest
```

Guard the canonical worktree and exact frozen head. Keep the original predicate
set and result classification. If the same finite silent SSH operation again
remains unfinished, escalate that exact operation for active guest/client/driver
descriptor observation while the watcher retains ownership. Do not infer VM
shutdown or turn silence into a failed/passed test, and do not launch repeated
unchanged retries. Failed-build retention is native Nix support, not a new driver.

The independent remaining host builds are still required, separately from the
runtime gap:

```sh
nix develop --no-write-lock-file --command confctl build --yes \
  'cz.vpsfree/containers/prg/int.log'
nix develop --no-write-lock-file --command confctl build --yes \
  'cz.vpsfree/containers/prg/proxy'
```

The lead is handling those host builds independently; this implementer launches
none and leaves source/Git read-only. Further useful evidence requires the
active guest/control-channel state at the stalled command, rather than additional
general native hypotheses or an upstream test-driver project.
