# Scope and proportionality review

Reviewer lane: scope and proportionality
Overall risk: high
Reasoning effort: xhigh

## Reviewed ranges

- `dev-workspace`: `8f75ece30462b184065f21867508af5e14365c4a..6735370851447ec62f6fbce25175c21db97c4686`
- `vpsfree-dev-workspace`: `213a3db57dea9298f61309eb157c0853f2310e9b..67c217eb65f554b1d234a2e4ec69cdb8ab0fa9c2`
- `workspace`: `ec3f99b42a7f6b850c3eb14219ae796ccacba98a..7a2e9caad9bd91bc4fd64f7c9f3830d8a9feeef8`
- `vpsfree-cz-configuration`: `8ef765d339ac792ef4f01a5c7a160e48600adcaf..192e163ed71bcbeefcbc296691c03da6a2692087`

The ranges contain one functional provider commit and one isolated dependency
update in each consumer. Concurrent uncommitted remediation in the generic
worktree was excluded; this review used the committed objects named above.

## Findings

No Blocking, Important, or Advisory findings.

The implementation is proportionate to the chosen contract:

- Markdown rewriting uses the existing Goldmark parser and changes only link
  destinations below the configured workspace root. The line-suffix parser and
  legacy absolute-path redirect directly implement the accepted input forms and
  the explicit requirement that previously copied URLs continue to work
  (`portal/internal/web/source_files.go:18-94,115-121`).
- Live and archived reads reuse verified repository registration, the existing
  Git runner, the recorded final head, the confined file opener, and the review
  preview limits. The new path validator and the `ls-files`/`ls-tree` checks are
  required by the approved tracked-file boundary rather than a speculative file
  browsing framework (`portal/internal/repository/source.go:24-109`).
- Artifact viewing reuses the existing manifest allowlist and confined artifact
  opener. Extracting the regular-file opener and preview classifier has two
  immediate consumers and avoids a second file-safety implementation
  (`portal/internal/session/manifest.go:680-728`,
  `portal/internal/repository/review.go:514-564`).
- The standalone viewer and small additions to the existing full-file editor
  are consumed by copied links, reloads, new tabs, line selection, and line
  reveal. They do not introduce editing, browsing, snapshots, line remapping,
  or another rendering framework (`portal/internal/web/static/source-file.js:1-80`,
  `portal/review-ui/editor.js:132-262`).
- The focused path, Git-index, archive, artifact, preview-limit, and browser URL
  tests exercise behavior owned by this change and its remote file-read trust
  boundary. They do not duplicate exhaustive Git or filesystem conformance
  testing (`portal/internal/web/source_files_test.go:1-286`,
  `portal/internal/web/source_files_browser_test.cjs:1-21`).
- The three downstream changes only advance the exact generic and organization
  pins required by the documented package/deployment contract. They add no
  unrelated dependency or configuration behavior.

## Residual risks and test gaps

The remaining risk is behavioral validation in a real browser and deployed
package: scrolling/highlighting, history navigation, new tabs, copy-link state,
responsive layout, and stale or missing line notices. The packet already reserves
these checks for post-review integration. No additional scope is warranted for
this lane.
