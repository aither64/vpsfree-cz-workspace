# Final quick batch: Unix socket path diagnosis

Parent watcher outer4758 settled with exit 1. No test retry or native process
was launched by implementer0. Original `go-all-naming.log/.exit`, batch exit and
`final-quick-watcher-result.md` remain unchanged. The tagged helper stage did
not run because the batch stopped after the full untagged suite failure.

The complete test log reports only one failed test:

```text
TestQueueDeletionResponseLossReconcilesAfterClientRestart
client_test.go:2790: listen unix /tmp/nix-shell.m7EGFi/TestQueueDeletionResponseLossReconcilesAfterClientRestart1134934474/001/app-server.sock: bind: invalid argument
```

That exact pathname is **109 bytes**. In the selected Go 1.26.7 immutable source,
`share/go/src/syscall/syscall_linux.go:547-560` returns EINVAL when a named Unix
socket pathname exceeds the raw path array or consumes the full array without
room for NUL. `share/go/src/syscall/ztypes_linux_amd64.go:170-173` defines the
array as 108 bytes. Thus this pathname is rejected before binding or any client
reconciliation can execute; the new naming/capacity code is not on this path.

The existing fixture at `codex/client_test.go:2774` uses `t.TempDir()` followed
by `filepath.Join(directory, "app-server.sock")` and direct `net.Listen`.
Nix supplied `/tmp/nix-shell.m7EGFi` as the temporary base. Most socket tests use
the existing short `/tmp/wpc-*` shared helper, but this fixture uses its own
persistent-state directory. The fixture bytes are unchanged from the selected
8b60554bc10c2a6bcbf9732a8b77ad959c317036 baseline:

- client_test.go SHA256 f4cbe72204046362418bc3540b6acaacf3a911662c553ae3078aba20cb77f422
- client.go SHA256 a454c0b5b56e60354f78fffd260125085a296bccc752ec682251bc632b9f9520
- go.mod SHA256 b3c1aa067a83e282f0a48e85b41c866aa37ffa3c04daf652499ff4b2d687716b
- go.sum SHA256 ca1bc0423d2069fe12491aad0acd4e46cddf6b83bab83a4cddb9549689927f20

The bounded correction is environment-only: after entering the same declared
Nix environment, create a new mode-0700 directory with `mktemp -d /tmp/cw.XXXXXX`
and set TMPDIR to that owned path. The observed suffix would yield 102 bytes,
below the 108-byte rejection threshold. Do not alter the fixture or its
assertions, disable CGO, skip cases, enlarge timeouts or change application
source. No socket reproduction probe was needed to establish this cause.

`run-go-quick-naming-tmp-v2.sh` retains the full untagged suite and the same
explicit tagged non-native helper stage, stop-on-first-failure, exact Nix
Go/CC/CXX/CGO environment and before/after source verification. It also refuses
any set CODEX_WEB_TEST_BINARY before launch, records its new owned TMPDIR in
`go-owned-tmpdir-v2.txt`, and retains that directory with a session/purpose owner
record. It performs no automatic cleanup or lifecycle action.

All 136 source files still match the original stable manifest. The new manifest
copy `quick-inputs-tmp-v2.json` has the same SHA256:
`bb6792edaf72b18df8dc842a977ea912b6de48aae1fdf18ede7b91160d925ef7`.
New runner SHA256:
`32398174933f4b3fc8a5725a59c2581c3c7645cfe1265bf5dfc924bfaa6f0e8a`.
Bash syntax check passed; the runner has not been executed by this owner.
Fresh receipts use the `naming-tmp-v2` names; original failure receipts remain.

The parent owns the fresh watcher and actual rerun result. This diagnosis and
runner preparation establish no native compatibility, acceptance, publication
or default integration. No own operation remains running.
