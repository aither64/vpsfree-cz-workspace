# Development environment and verification

Required workspace procedure, selected by the routing table in `AGENTS.md`.
Its rules retain workspace scope and precedence. Paths and commands are relative
to the coordination workspace unless the text specifies another repository.

## Development Environment

Use the generic `dev-session-monitor` skill for authorized tests, CI checks and
builds expected to exceed one minute, and delegate uncertain-duration integration
tests and builds before launching them. Resolve the fresh verification watcher
from the installed catalog's separate utility policy. It is not a team member
and must not edit source, diagnose, retry, approve, or deploy.
Keep known quick checks inline. Resolve planning, implementation and diagnosis
settings from the retained team roster. Mandatory review uses an eligible
retained review-purpose member's saved model and effort; without one, use a
review-purpose role from the installed catalog's default development team in a
fresh standalone thread, including for solo sessions. Do not invent a team or
change the roster. Pass
project escalation rules, including
unexpected local kernel builds, in the watcher's brief. The parent continues
automatically on completion or escalation. If the skill or delegation is
unavailable, report
that once and use minimal-output parent monitoring. A user's instruction not to
wait for CI takes precedence.

Development is generally Nix-based. Prefer each repository's `nix develop`,
`nix-shell`, flake outputs, or documented development shell before running
language-specific tools. Deployment is usually to NixOS or vpsAdminOS systems,
often through `confctl` and the configuration repositories.

Treat an unexpected local Linux kernel build in vpsAdminOS development or test
workflows as a bug unless the current work intentionally changes kernel sources
or configuration. vpsAdminOS kernels should normally be substituted from the
vpsAdminOS binary cache after GitHub Actions or its runners build them. When a
command starts building a kernel, stop it and investigate why the derivation
missed the cache. A local rebuild is acceptable only when the kernel or its
configuration is intentionally changed, or when the responsible runner has not
yet built and published the expected derivation; record the justification in
the initiative `state.md`.
If the work needs an additional kernel output, update the vpsAdminOS CI builder
to build and publish that output as part of the same initiative instead of
relying on recurring local builds.

When running `vpsadmin-devcluster`, use the bridge network by
default. Do not choose `--network local` unless the user explicitly asks for it
or the bridge network is genuinely unavailable; if local networking is used,
record the reason in the initiative state.

Use GitHub Actions as a feedback loop after pushing branches. If `gh` is not
available in the current shell, run it through Nix, for example
`nix shell nixpkgs#gh -c gh run list ...`. Inspect failed logs, monitor reruns,
and resolve failures instead of leaving CI for the user to chase.
Successful checks, review, and CI are verification evidence, not permission to
merge or push feature content to a default branch; follow the Git approval gate.

After a force-push or a follow-up fix push, cancel superseded queued or
in-progress GitHub Actions workflow runs for the same branch. Only cancel runs
whose `headSha` no longer matches the current branch head; do not cancel
workflows for other branches or workflows already running on the current head.

When creating or editing GitHub workflows, verify the latest upstream version of
each imported action from its official repository before choosing the `uses:`
ref. Do not rely on remembered version numbers; use the newest compatible
version unless the workflow records a specific reason to pin an older one.

Rerunning a failed GitHub Actions job is not a substitute for investigation.
Before accepting a rerun as validation, download or open the failed attempt's
logs and artifacts, identify the root cause as far as the available evidence
allows, and record the finding in the initiative `state.md`. If the artifacts
are insufficient, improve the test or runner diagnostics rather than treating a
green rerun as proof that the failure did not matter. Prefer fixing the
underlying problem; when the failure is unrelated to the current change, record
the evidence for that conclusion.

When a repository is missing a tool in the ambient shell, enter the repository's
Nix shell or use an appropriate `nix shell` command. Do not work around missing
tooling by recording local environment limitations in commit messages.

When adding new integration tests that use the vpsAdminOS test-runner, write
test scripts in the current RSpec-style structure with examples and
expectations, such as `describe`, `it`, and `expect`. Do not refactor existing
tests solely to convert their style unless the user explicitly asks for that
refactor.
