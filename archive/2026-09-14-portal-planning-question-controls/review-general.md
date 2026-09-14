# General review

Reviewed the committed portal question-composer change across these exact ranges:

- dev-workspace: `e9ed544bf66ba8be07b4fca27aede6e6fd1bfe0a..df21f2ea8fe27efdb2cb8c0330fa31acd0f3a933`
- vpsfree-dev-workspace: `916223fce1c5b7b78578ca8a16aaaa472c68b08c..89a03581b13056fa83114e592f2e2993e6a87887`
- workspace: `f523eddf3e1d1cdebf445992318247030e11c7f3..1e01e557cac5527666d5b1e35fa52fadcdbb81af`

The review covered requested behavior, commit history and messages, JavaScript
and CSS implementation, the opt-in Go/Playwright regression, recorded browser
evidence, and the two downstream Nix pin updates.

## Findings

No Blocking, Important, or Advisory findings.

## Review notes and residual gaps

The dev-workspace commit has one coherent purpose. `createComposerView` gives
rendered answerable questions priority over completed-plan decisions and the
composer, moves the existing Interrupt control into the first question header,
keeps the composer DOM mounted, and transfers focus through question replacement
and removal. Non-answerable approvals, terminal-only requests, unavailable
authority, and error cards do not acquire the question class and therefore leave
ordinary controls available. The CSS change supports that layout and removes the
superseded short-window composer compaction rule. The focus remediation and
browser test directly support this behavior and do not require a separate commit.

The real-renderer regression covers Plan and Default modes, blocking and
asynchronous questions, repeated and changed snapshots, multiple question cards,
failed and successful responses, disconnection, plan priority, draft and upload
retention, Interrupt identity and behavior, and representative desktop, short,
mobile, and zoom-equivalent viewports. The recorded 22-second Chromium run passed
with no page errors. Focus behavior was not exercised in another browser engine,
and the opt-in regression does not run in ordinary Go test invocations; those are
residual coverage limits rather than defects in this bounded deployment.

Each downstream repository contains one reviewable dependency-pin commit. The
organization extension changes only the dev-workspace revision and matching lock
metadata. The site workspace changes only the vpsfree-dev-workspace revision and
the transitive dev-workspace lock node. Remote feature refs resolve to the exact
reviewed heads, worktrees are clean, commit subjects follow the local conventions,
and `git diff --check` reports no whitespace errors.

Packaged checks, CI completion, assembled-package validation, and live deployment
verification remain pending after review as planned. No documentation update is
needed for this internal presentation change, and no protocol, persisted-state,
or public API behavior changed.
