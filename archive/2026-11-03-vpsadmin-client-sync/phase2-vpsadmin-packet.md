# Phase 2 vpsAdmin canonical policy packet

Implementation and quick checks complete; final independent documentation/history
review and feature publication remain. The lead explicitly held the feature push
until that review, because the AGENTS edit triggers broad existing automatic CI.
No Phase 2 default integration is approved by the Phase 1 approval.

## Exact review range

- Repository: `git@github.com:vpsfreecz/vpsadmin.git`, target `master`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin`.
- Branch: `2026-11-03-vpsadmin-client-sync`.
- Fresh fetched base: `942c6eaed41331f823d8e0f670ed239e2b308440`.
- Final local head: `4ac49f49e63545200df8afa920c6eafda8722523`.
- Complete base-to-head series: one commit,
  `4ac49f49e63545200df8afa920c6eafda8722523 docs: require generated client synchronization`.
- Final diff: [phase2-vpsadmin-final.diff](phase2-vpsadmin-final.diff), two files,
  69 insertions and four deletions, including introductory line wrapping.

Fresh SSH master matched the original API source base, so no rebase was needed.
The source export and all Phase 1 released histories remain unchanged. The
worktree and index are clean. No superseded unmerged approach or follow-up commit
remains. There are no dependency/channel/input/generated-artifact update streams,
version changes or migrations in this range. No migration merge, release,
deployment or external-use lineage is introduced or rewritten.

## Requested outcome and document ownership

Only `AGENTS.md` and `docs/api-schema-export.md` changed. One logical commit keeps
the required procedure route and its complete canonical procedure together.
The introduction now identifies Go, Rust and TypeScript consumers. Existing
export preparation, safety, provenance and database-free check instructions are
unchanged. No scripts, tests, workflows, schema, runtime, configuration, package
metadata or released versions changed.

The canonical heading is exactly `## Generated client synchronization`, unique
at line 101, yielding `#generated-client-synchronization`. The public URL is:

`https://github.com/vpsfreecz/vpsadmin/blob/master/docs/api-schema-export.md#generated-client-synchronization`

The final committed document SHA-256 is
`109f3830f889d61785c17831b795ee3a611f624c3a4a25c0707eada31b3c53c2`.
The default-branch URL is prospective until approved integration; consumers check
the exact candidate source locally. Go/workspace, Rust/HaveAPI and TypeScript/WebUI
owners received the earlier candidate for semantic/anchor checks and receive this
final head/hash for reconciliation. They own their thin links and scoped rules.

The procedure requires all three client assessments and remote-default updates or
revision-specific no-change evidence before API task completion. It records raw
input/profile/generator provenance, owned transformations, source freshness versus
saved-input consistency, compatibility and recovery, bounded explicitly approved
integration order, release-free ordinary sync and the conditional published-TS
WebUI gate. TS releases default to minor unless the user specifies otherwise.
It preserves separate deployed-API capability readiness and makes no unsupported
claim of automatic enforcement.

## Writing and verification evidence

The lead directly applied `vpsfree-user-facing-writing` and `humanizer-en` to
[the exact draft diff](phase2-vpsadmin-prose.diff) before the commit. All requested
edits were applied: normal introductory wrapping; evidence tied to the assessed
API revision; conditional repeat export when exporter/fixture/profile/tooling
changes or determinism is unestablished; explicit remote-default completion and
revision-specific no-change wording. All other approved prose was preserved.

Quick checks passed:

- `git diff --check` before commit and across the final range.
- All six local Markdown links/anchors resolve; the canonical heading/anchor is
  unique. A direct byte comparison preserves the pre-existing exporter sections.
- Exactly the two assigned paths changed; initial index was empty and only those
  paths were staged. Configured author and committer identity were verified.
- The five prose scenarios are covered: schema changes update clients;
  behavior-only changes record justified no-op evidence; ordinary source sync
  requires no release; dependent WebUI merges require a published artifact; TS
  defaults to minor with explicit override. Consumer owners independently checked
  these meanings in the candidate; final head/hash reconciliation follows.
- Normal commit ran all declared hooks with no bypass. Nixfmt, MigrationSpecs,
  VpsadminWebuiI18n and VpsadminApiI18n passed. Commit-message SingleLineSubject,
  TextWidth and TrailingPeriod checks passed.

The declared API i18n hook always uses `api/.gems`; that normal API bundle path was
absent after source-export preparation. Under the already prepared Ruby 3.4 Nix
shell, an ignored `api/.gems` alias reuses the existing isolated exporter gems.
An ignored API lock was resolved locally; its only difference from the retained
tooling lock is the API's original `haveapi (~> 0.32.2)` constraint in place of the
exporter's exact constraint. Installed versions are unchanged; `bundle check`
passed. The exporter lock SHA-256 remains
`62a0e7f65e0755296ea50e3f5efa590f51e8615571a078cf45243f6ca8555f1c`.
Overcommit reported no plugin-signature changes. No shared Bundler config or
HaveAPI worktree was changed.

## Final review and CI boundary

The coordinating lead assigns the saved independent reviewer under
`mandatory-change-review`; this package supplies the complete range and final
diff, no-migrations and no-repeated-stream inventory. The package changes
contributor documentation only; the lead selects lanes/risk for the consolidated
cross-repository review. No long local build/test matrix is needed for this prose.

Existing `ci.yml` integration paths exclude these two files. However,
`api-specs.yml`, `api-migration-specs.yml` and `i18n-health.yml` explicitly include
`AGENTS.md`. Therefore a feature push can start automatic API matrices; there is
no claimed docs-only CI exemption for those workflows. No optional dispatch or
workflow edit was made. Per the lead's latest instruction, feature push is held
until final committed-doc review; the lead will choose bounded CI observation
afterward. Independent review, publication, CI and integration statuses must remain
distinct. Any final review findings remain owned by implementer3.
