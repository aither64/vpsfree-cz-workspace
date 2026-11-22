# bpftool Pinned Tracing Link Exit Status

## Symptom

On a vpsAdminOS 6.12.95 test VM, `bpftool 6.18.7` printed valid JSON for a
pinned tracing link but exited with status 255:

```sh
bpftool -j link show pinned /sys/fs/bpf/.../override_uname__uname_fentry
```

The JSON contained the link ID, program ID, tracing type, attach type, target
object, and target BTF ID. Treating the command as an ordinary successful shell
command therefore made the test fail before it could inspect the result.

## Workaround

Use the command output as the primary result: parse the JSON and require the
expected fields. Accept only status 0 or the observed 255 when the JSON is
valid. Continue using ordinary exit-status checks for commands such as
`bpftool link show id ID` whose purpose is to prove that a link was destroyed.

## Verification

Observed while running `./test-runner.sh test ebpf-livepatch-lifecycle` in
initiative `work/2026-08-21-vpsadminos-ebpf-program-check`.
