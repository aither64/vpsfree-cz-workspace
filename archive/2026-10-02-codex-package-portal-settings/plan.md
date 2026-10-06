# Codex package and portal settings

Implement the accepted plan: repair plain Codex startup with a complete Nix
runtime package, update Codex to 0.160.0 in the workspace and on aitherdev,
remove the portal's unsaved-settings notice, verify, and deploy.

## Projects and ownership

- dev-workspace: reusable package assembly, Codex pin, settings presentation,
  package/browser checks, and package-contract documentation.
- vpsfree-cz-configuration: llm-agents and generic-runtime channel pins,
  shared assembly for system codex and codex-ds, aitherdev deployment.
- vpsfree-dev-workspace: consuming generic-runtime pin only.
- workspace: consuming extension pin and deployment records; feature changes
  use a dedicated workspace worktree while tracking remains on shared master.
- codex-web: existing protocol validator; change only if selected-version
  compatibility evidence requires a client correction.

Create a delegated initiative. The retained designer owns design.md, the
implementer owns application edits, and the independent reviewer owns review.
The external coordinator maintains records, pins, review reconciliation and
deployment. Long checks use fresh utility watchers from the pinned catalog.

## Implementation decisions

Expose lib.mkCodexPackage { pkgs; codex; } in dev-workspace. Assemble cached
upstream native binaries in a new derivation, preserving the existing launchers
and completions. Its runtime root contains codex-package.json, bin/codex,
bin/codex-code-mode-host, bin/logs_client, codex-path/rg and codex-resources/bwrap.
Helper files
must be materialized within the runtime root because daemon package copying
rejects escaping links. Reuse this helper for the workspace App Server and
aitherdev's system codex and codex-ds.

Pin llm-agents.nix to 6334544a4bfd921086a252caccc6c1c6eb1d18c7 (Codex 0.160.0).
Configuration channels are changed with confctl, including exact feature pins;
do not edit its lockfile manually. Keep unrelated inputs stable except for the
necessary transitive lock changes.

The user selected normal daemon startup with a complete package. Reference the
existing upstream implementation in numtide/llm-agents.nix PR #9889 rather than
inventing a different layout. PR #10132 additionally changes daemon lifecycle
to run directly from the store; that source patch is outside this accepted
assembly-only approach. Both PRs remain unmerged at planning time.

Remove "Codex settings have unsaved changes" from the live settings controller.
Preserve Apply/Cancel, draft persistence, validation and error recovery. Place
saving/error status below the controls and hide it when empty. The user selected
a single desktop row with existing mobile wrapping. Verify 1280px and 1440px
desktop widths and a narrow mobile viewport.

## Compatibility and deployment

At planning time, system and workspace Codex were 0.159.2. SQL migrations in the
main, queue and thread-history trees are identical between 0.159.2 and
0.160.0. Before real-state compatibility probes, validate old/new readers on
disposable state and inspect any protocol changes. This feature introduces no
workspace database or manifest migration and preserves session/runtime/cluster
formats, ownership and package-generation checks. Retained Codex GC roots
protect the binaries and their Nix dependencies.

Deploy system changes from the configuration feature branch, scoped to
cz.vpsfree/machines/aitherdev, with dry activation before activation. Deploy
the workspace application from the full consuming workspace worktree using
workspace-host switch; the system must not install or pin the application.
Retain the previous system generation. Workspace switches are forward-only;
recover with a corrected newer generation, preserving transition journals.
No coordinated fleet update is required.

Initial authorization covered implementation, checks and deployment. The later
explicit integration direction recorded below additionally covers merging all
four feature branches into their defaults. Archive, delete, stopping the session
and removing branches remain outside authorization.

## Verification and documentation

Run quick Nix evaluation, focused Go/Ruby checks and JavaScript syntax checks;
commit intended changes; inventory complete branch history and migration
provenance; perform mandatory independent review before long integration tests.
Resolve blocking findings and record important/advisory dispositions.

Run package checks, generated-schema protocol validation, isolated daemon
start/version/stop checks and terminal startup checks covering resume/fork.
Exercise Apply/Cancel, dirty drafts/reload and failed saves in the existing
browser suite, with desktop geometry and mobile usability checks. Build only
aitherdev. Stop and investigate unexpected local kernel builds. Watch long
checks and deployment waits with a fresh Luna/low utility.

Keep the reusable runtime layout and semantics in dev-workspace docs, site
operations in configuration docs, and this rollout's revisions/results in state
and linked evidence. Apply the writing skill to user-facing prose before its
commit. Handoff includes the stable initiative portal URL.

Upstream references:

- https://github.com/numtide/llm-agents.nix/issues/9887
- https://github.com/numtide/llm-agents.nix/pull/9889
- https://github.com/numtide/llm-agents.nix/pull/10132
- https://github.com/openai/codex/issues/48050

## Requested upstream-reference follow-up

The user asked for upstream issue/PR references in code comments or commit
messages so the downstream packaging workaround has a clear retirement path.
Add a focused reference/removal comment beside the shared assembly helper and
a matching explanation in its existing package-contract page. Link the Nix
packaging issue9887, complete-layout PR9889 and Codex issue48050. Removal depends
on the selected upstream revision delivering a complete daemon-copyable package
that both consumers can use directly, with normal startup and closure-retention
checks still passing; merely closing an issue does not meet that condition.
No source patch, disabling daemon startup, runtime/pin change or redeployment
is part of the reference edit. Preserve the already deployed assembly commit
and add a separate documentation-purpose commit. The user subsequently approved
merging all four registered feature branches into their default master branches
when done, without waiting for CI. Preserve feature refs and the open session.
