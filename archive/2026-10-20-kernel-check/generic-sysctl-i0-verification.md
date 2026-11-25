# Generic sysctl tests and documentation: quick-check receipt

Latest fixture follow-up: the `89587060` native run passed six examples but
both intended failure examples failed because procps `--system` ignores unknown
keys. The [source-proven correction](generic-sysctl-failure-injection.md) uses
an invalid value for an existing benign integer instead. Its quick checks pass;
the combined correction still needs commit/review and a fresh native run.

## Follow-up: separate boot readiness from sysctl completion

Implementer2 reports the focused run at exact `88486d43` failed before any
example: the first `/service/sysctl/check` timed out after about 61 seconds,
with only firmware console output and no guest command sent. That result
does not establish a sysctl service failure or explain the missing boot progress.
Preserved run: `/tmp/os-test-runner/os-test-system__sysctl-8ae7035e`.

Source confirms a fixture setup problem: `Machine#start` defaults to
`wait_for_boot: false` (`osvm/lib/osvm/machine.rb:221`). `Shell#execute`
first waits for shell readiness under the supplied command deadline before
sending a command (`osvm/lib/osvm/shell.rb:156`). The fixture's first service
check therefore spent its 60-second service budget on boot/readiness too.

The only source correction is
`machine.start` → `machine.start(wait_for_boot: true)` in the before-suite hook.
This uses existing `Machine#wait_for_boot` (`machine.rb:457`) and the existing
default 900-second boot/readiness timeout (`machine.rb:172`), followed by the
unchanged independent 60-second service check. No service, product, test-runner
implementation, kernel or documentation behavior changed. It improves the
deadline and failure classification; successful boot is still unproven.

The corrected fixture SHA-256 is
`6f82716856c9c9f63552ce2dbafba213926426e6b7156dd8d37812748eda04d6`.
This supersedes only its earlier hash below. Implementer2 retains all Git
ownership; implementer0 has not rerun the VM. Follow-up quick-check evidence is
[generic-sysctl-i0-boot-wait-quick.log](generic-sysctl-i0-boot-wait-quick.log).
Nixfmt, Nix parsing, whitespace, actual fixture graph rendering and rendered
Ruby syntax all passed (exit 0, `Syntax OK`).

## Initial package and committed checkpoint

2026-10-22, implementer0. Session/current/environment and saved workspace-write
roster binding verified. The accepted
[design](design.md#approved-generic-sysctl-service) governs this package.

Committed checkpoint: implementer2 included the checked files unchanged in
`88486d43f7d47917b6ab796163abf8cd1f0be94a` after panic-policy `85282623`.
Implementer0 independently verified that exact HEAD, a clean source worktree,
and all three owned file hashes below. Implementer2 reports hooks passed;
final independent review and VM verification remain pending. No duplicate
evaluation or integration run was started for this checkpoint.

Source is in the session-owned `vpsadminos` worktree. At these checks, HEAD was
`8528262315b0794a8f50917cf33c53a07fd14030`, with the generic feature uncommitted.
Implementer2 owns the module and all Git operations, including the combined
generic-feature commit. Implementer0 has performed no Git mutation or VM run.

## Owned files

- `tests/suite/system/sysctl.nix`: eight ordered RSpec examples using benign
  settings in a disposable guest, with five configuration switch targets.
- `tests/all-tests.nix`: register `system/sysctl`.
- `docs/os/configuration.md`: sysctl behavior, completion/error limits and
  explicit retry procedure. Lead accepted the complete section and its final
  clarification that an otherwise unchanged switch does not rerun the service.

The fixture covers boot's intentional second application; unchanged-input
manual override retention; stale generation rejection despite `done`;
dry/boot-only non-application; add/change/remove/null/effective-target rename;
procps `/etc/sysctl.conf` precedence; partial failure after success without
automatic retries; and successful/failed explicit same-generation retries.
It observes a fresh log attempt before waiting for the supervisor to be down,
then checks completion markers and actual runtime values. These are test
assertions awaiting execution, not runtime results.

## Passed quick checks

Run from the owned OS repository root, inside `nix develop`:

```sh
nixfmt --check tests/suite/system/sysctl.nix tests/all-tests.nix
nix-instantiate --parse tests/suite/system/sysctl.nix >/dev/null
nix-instantiate --parse tests/all-tests.nix >/dev/null
git diff --check -- docs/os/configuration.md tests/all-tests.nix tests/suite/system/sysctl.nix
timeout 40 mkdocs build --site-dir /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-kernel-check/generic-sysctl-doc-site
```

All exited successfully. [Log](generic-sysctl-i0-final-quick.log). MkDocs built
in 0.81 seconds, including the sysctl section and retry anchor on the existing
configuration page. Its unrelated informational notice lists the existing
`os/faulted-write-ci-handoff.md` outside navigation. No navigation change needed.

Actual full fixture graph render, with the final service module, also passed:

```sh
timeout 50 nix eval --impure --raw --expr '
  let
    f = builtins.getFlake (toString ./.);
    t = import ./tests/suite/system/sysctl.nix {
      pkgs = f.inputs.nixpkgs.outPath;
      system = "x86_64-linux";
      testFramework = f.lib.testFramework;
    };
  in t.config.testScripts.default.script
' > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-kernel-check/generic-sysctl-test.rb
ruby -c /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-kernel-check/generic-sysctl-test.rb
```

Exit 0, `Syntax OK`. [Final render log](generic-sysctl-i0-render-final.log).
This forces the five interpolated switch-target toplevel paths without building
or booting them. Source hashes before/after the final render were identical:

| File | SHA-256 |
| --- | --- |
| `os/modules/config/sysctl.nix` (i2-owned) | `6551efbc6474ff2822a8ecbd4930ca79e802f604e3d4c661cbced063d4ebde45` |
| `tests/suite/system/sysctl.nix` | `c112249ab8277db8f439015e57679d57cde21a0e991de55cdb77334e15475ffd` |
| `tests/all-tests.nix` | `474525ea63d05a54c05f46512c99066a311e1260c4af7ceae7c3cc27799d56ad` |
| `docs/os/configuration.md` | `9930c462dd8d7cca689958eb4f1bb868dc956e362582ea6d7f513bc5b6fb58d8` |

The first render failed with an `environment.etc` → `sysctl.check` identity
recursion; [failed log](generic-sysctl-i0-render.log) is retained. Implementer2
resolved this by carrying the identity in the existing service environment;
the subsequent [retry](generic-sysctl-i0-render-retry.log) and final render above
passed. This was an evaluation failure, not a guest result.

## Remaining verification and handoff

Implementer2 has included these files in the separate generic logical commit,
run hooks, and sent the exact committed deliverable/history for final review.
No VM or product integration test may start before lead confirms acceptance.
Then a fresh policy-selected watcher runs this exact focused command from the
owned OS repository root:

```sh
./test-runner.sh test system/sysctl
```

No runner implementation, kernel sources or kernel configuration changed.
Expect kernel cache substitution; stop and investigate any unexpected local
kernel compile under the verification procedure. The real boot/switch/sysctl
and supervisor once/no-retry integration remains unverified by this receipt;
rendering and isolated checks cannot replace it. No production writes,
deployment, input bump, merge or session lifecycle action occurred.

Stable session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-check/>.
