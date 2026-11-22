# Root a long Nix app invocation

The extension's `nix run .#devcluster-check` passed two package-backed
evaluations, then failed reading a previously present config file. The entire
tools output and app had disappeared. The host's
`nix-store-gc-on-pressure.service` journal explicitly records deletion of both
outputs while the smoke ran, at 23:34:08 CEST on 2026-09-30. Ordinary
`nix-collect-garbage` ran because store usage was 82%.

The package installs and checks the config file, and the fixture removes only
its own temporary workspace. This incident is not evidence of a missing-file
package defect. Keep an explicit GC root for the app closure while a long
verification uses paths embedded in its launcher.

For this app, `nix eval --json
.#apps.x86_64-linux.devcluster-check.program --apply builtins.getContext`
returns its derivation and output name. Build that derivation's `^out` with
`nix build --out-link <task-root>`, verify that the closure includes the tools
output, then execute `<task-root>/bin/devcluster-check`. A fresh Luna watcher
completed this exact rooted retry at extension `8e04f262`: exit 0 after about
5m40s, with enabled/disabled configurations and runner builds/loads passing.
The app and tools roots stayed intact. No GC service or application source
change was made.

Related evidence: [session state](../../work/2026-09-30-portal-review-improvements/state.md),
`/tmp/portal-review-store-gc-evidence.txt`, and the failed attempt's
`/tmp/portal-review-final-cluster-8e04f262.log`. Successful retry output:
`/tmp/portal-review-rooted-cluster-8e04.log` and `.status`.
