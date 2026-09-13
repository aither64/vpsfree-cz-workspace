# Mandatory change review: General lane

Reviewer lane: general
Model and effort: `gpt-5.6-sol`, `xhigh`
Risk classification from the review packet: high

Reviewed the exact committed ranges from `review-packet.md`:

- dev-workspace `8f75ece30462b184065f21867508af5e14365c4a..6735370851447ec62f6fbce25175c21db97c4686`
- vpsfree-dev-workspace `213a3db57dea9298f61309eb157c0853f2310e9b..67c217eb65f554b1d234a2e4ec69cdb8ab0fa9c2`
- workspace `ec3f99b42a7f6b850c3eb14219ae796ccacba98a..7a2e9caad9bd91bc4fd64f7c9f3830d8a9feeef8`
- vpsfree-cz-configuration `8ef765d339ac792ef4f01a5c7a160e48600adcaf..192e163ed71bcbeefcbc296691c03da6a2692087`

I read the initiative plan/state, every repository-local `AGENTS.md`, commit
messages and complete diffs, the repository and artifact access paths, the
viewer/editor integration, tests, documentation, and dependency propagation.
All four remote feature branches resolve to the packet heads.

The commit split is focused and reviewable. The provider commit contains one
source-viewer capability and its supporting access helper, browser integration,
tests, documentation, and package syntax check. Each consumer pin is isolated;
the configuration message is the generated `confctl` message required by the
repository rules. I found no abandoned protocol, repeated dependency-update
stream, fixup history, or unrelated bundled behavior.

## Findings

No Blocking findings.

### Important: curated artifacts are filtered by the repository path contract

Commit `6735370851447ec62f6fbce25175c21db97c4686` applies
`repository.ValidSourcePath` to the whole absolute workspace-relative path and
to the `artifact` query (`portal/internal/web/source_files.go:53-55,96-107`).
That validator is deliberately a repository-path policy: it rejects backslashes,
non-canonical components, and every component named `.git`.

Curated artifacts already have a different public contract. Manifest validation
accepts any safe relative path and identifies it by its cleaned path
(`portal/internal/session/manifest.go:198-215`); `OpenArtifact` uses that same
cleaned-path allowlist before the confined regular-file open
(`portal/internal/session/manifest.go:672-696`). A valid published artifact such
as the literal Linux path `reports\status.md`, or a regular file below a `.git`
directory inside the tracking directory, remains available through the existing
artifact endpoint but its absolute Markdown link is not rewritten and both the
viewer and file API reject it. This contradicts the promised behavior for
explicitly registered artifacts and makes the new route depend on a second,
narrower definition of the artifact interface.

Use the session artifact normalization/authorization contract for artifact
targets, while retaining `ValidSourcePath` for repository targets. Add a
regression using an artifact path accepted by the manifest contract but rejected
by the repository-path validator, covering rewrite/redirect and the file API.

### Advisory: a completed line reveal can overwrite a newer missing-line notice

The hash-change handler starts an asynchronous reveal without identifying the
navigation that owns its result (`portal/internal/web/static/source-file.js:59-71`).
A valid line reveal waits for an animation frame inside `editor.revealLine`. If
the hash changes to an absent line before that frame, the newer call reports the
missing line immediately; the older call then completes and clears the notice
with `announce("")`. The selection is already cleared by the newer call, so the
page can show neither a highlight nor the required unavailable-line message.

Ignore reveal results when the hash has changed or supersede each invocation
with a generation token. A browser contract with a deferred valid reveal
followed by an immediate absent-line result would cover the ordering reliably.

## Residual validation gaps

- The planned live browser checks remain necessary for actual highlight and
  scroll placement, reload/back/new-tab behavior, narrow layouts, clipboard
  behavior, plain-source escaping, and source/unavailable-line messages.
- I relied on the packet's exact-head CI and focused quick-check record for the
  committed series. During review, the repository and session Go packages
  passed, and the web package passed in the declared Nix environment; the latter
  run included the coordinating agent's uncommitted direct remediations and is
  not evidence for the original packet head.
- Full package/host validation, dry activation, deployment, and rollback remain
  pending as intended until review findings are resolved.
