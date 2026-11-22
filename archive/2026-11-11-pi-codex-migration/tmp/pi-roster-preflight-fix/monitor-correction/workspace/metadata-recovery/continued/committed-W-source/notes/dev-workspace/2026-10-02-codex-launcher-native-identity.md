# Compare running Codex with its declared native entrypoint

An isolated verification launched the selected real Codex through normal
`workspace-host run-codex`, then rejected `/proc/<pid>/exe` because the probe
compared it with the public `bin/codex` command. The public command is a launcher;
it forwards to the assembled package's native executable.

Use the owning `docs/codex-package.md` layout and
`libexec/codex/codex-package.json`: layoutVersion1 declares the native
`entrypoint` relative to `libexec/codex`. Validate the selected package/version
and compare the recorded process with that declared native path. Retain the
normal launch/registration evidence; do not guess another executable or weaken
registration checks.

This was a verification-fixture assumption, with no application package defect.
The failed run retained its genuine private App Server and original diagnostics
before any model goal or measured creation. A follow-on must preserve that
failure and prove the exact recorded process/pre-portal state without clearing
its earlier claim or restarting it.

Related initiative: `work/2026-10-02-portal-creation-performance/`.
