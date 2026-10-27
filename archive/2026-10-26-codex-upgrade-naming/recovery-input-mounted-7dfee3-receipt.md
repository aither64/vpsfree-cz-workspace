# Recovery input mounted check: recovered tool-transcript evidence

Lead accepted the original four-case PASS and actual settlement, with the
evidence limitations below. This is a recovered transcript receipt, not a raw
stdout/stderr capture. No replacement test was run to recreate evidence.

- Source: `7dfee3be82af34caea940a4c325d847fb8184587`.
- Tree: `6ce15025bbd2912e1e6eb20c6dcf67fadff9e920`.
- CWD: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-codex-upgrade-naming/dev-workspace`.
- Parent independently verified exact clean source before launch and after settlement.
- Fresh utility: `/root/recovery_input_7dfee3_watcher`, Luna/low, retained catalog
  `3ff7a2129ed39b4d6774466e53060bbff33d2cd2d893aa168c87cb3d64bd6b41`,
  `danger-full-access`, approval `never`.
- Original exec handle: `86036`. Final `write_stdin` returned `exit_code: 0`
  with no session ID. Original command and watcher are FINAL and settled;
  no running or uncertain operation remains.
- Go package duration: `29.409s`; test duration: `29.34s`. Actual launch/end
  timestamps and total operation wall time are unknown.

The watcher quoted this original invocation from its existing tool context:

```sh
nix develop --impure --expr 'let runtime = builtins.getFlake "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-codex-upgrade-naming/dev-workspace"; pkgs = import runtime.inputs.nixpkgs { system = "x86_64-linux"; }; in pkgs.mkShell { inputsFrom = [ runtime.devShells.x86_64-linux.default ]; packages = [ pkgs.playwright-test ]; NODE_PATH = "${pkgs.playwright-test}/lib/node_modules"; PLAYWRIGHT_BROWSERS_PATH = "${pkgs.playwright-driver.browsers}"; PORTAL_BROWSER_TEST = "1"; }' --command bash -c 'set -euo pipefail; cd portal; go test -mod=readonly ./internal/web -run "^TestRetainedOpenInputBrowser$" -count=1 -failfast -v'
```

Available completion output quoted by the watcher:

```text
--- PASS: TestRetainedOpenInputBrowser (29.34s)
    --- PASS: TestRetainedOpenInputBrowser/chromium/accepted (6.25s)
    --- PASS: TestRetainedOpenInputBrowser/chromium/unknown (3.87s)
    --- PASS: TestRetainedOpenInputBrowser/firefox/accepted (10.51s)
    --- PASS: TestRetainedOpenInputBrowser/firefox/unknown (8.71s)
PASS
ok  	github.com/aither64/dev-workspace/portal/internal/web	29.409s
```

The required direct `.log`, `.meta` and `.exit` files were never created.
The first `write_stdin` result was truncated at `max_output_tokens: 2000`;
complete raw output is unavailable. Original chunk IDs were not supplied.
This receipt does not reconstruct missing output or timestamps. Provenance is
the watcher's original exec/poll context and subsequent quotation, forwarded to
lead in report `d3bcc7df-8a08-4853-a086-3c652ef694b7`. Lead explicitly accepted
the limitation in its following assignment.

Separately, the watcher mistakenly invoked the same command from
`/home/aither/workspace/ai/vpsfree.cz` while attempting evidence capture.
That operation had handle `19832`; the watcher sent Ctrl-C in a later poll.
Its final result was exit `1`, no session ID, with:

```text
bash: line 1: cd: portal: No such file or directory
```

It stopped before `go test` launched and is not another mounted test result.
No project source changed. The earlier failing `125a` run remains separately
preserved in `recovery-input-mounted-125a.log`, `.meta` and `.exit`.

Owners0/1/2 were notified of accepted PASS and actual settlement/free.
Owner0 may publish the authorized exact head; consumer pins still require its
actual SSH publication. CI observation remains conditional on publication and
final profile PASS, assessment and actual command/watcher settlement.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-codex-upgrade-naming/>
