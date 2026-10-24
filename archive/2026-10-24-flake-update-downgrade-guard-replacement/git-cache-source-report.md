# Git-cache provider: source and accepted package evidence

Confctl head `822c0e35dbe2549111912f539116b4225dfd3035` passed independent final
review and is published, with exact R preserved remotely. The lead accepted the
published package's exported check: **203 examples, zero failures, zero pending**,
exit 0 in 98 seconds. See [accepted package evidence](verification/git-cache-exported-check.json)
and [publication proof](git-cache-publication-report.md). The source inventory
below preserves its original prepublication checkpoint; it was not rewritten.

The lead reports all seven exact reviewed consumers published. Its fresh utility
owns the selected-path/caller/cache operation; this report does not claim its
completion. No duplicate check, active-log polling or additional CI observation
was performed by the implementer. No default integration, deployment or lifecycle
action is authorized or claimed.

## Complete history and provenance

Base: `cc40679d267165aecfa569128438bb55fe910268`.

1. `550717765d58e9f28d960ea5bca3459ace86eb9e` — guarded updates and shared Git
   ancestry evidence, transaction/graph/CLI/JSON contracts, specs and owning docs.
2. `822c0e35dbe2549111912f539116b4225dfd3035` — independent packaged Ruby startup
   compatibility fix, retaining both real caller/preload/hook regressions.

The [inventory](git-cache-source-inventory.json) records all 28 base-to-head paths
and the 16-path R-to-new delta. Review the [complete series](git-cache-full-series.txt),
[full diff](git-cache-full.diff) and [delta from R](git-cache-from-r.diff).
The final tree `e004bb150090777e53d9796011f191a7ba80fd4a` exactly equals the tested
pre-consolidation tree at `67cb2b31e7cd0e5b0e8c2949c401795bc37216a1`.

The Git rework was folded into the owning guard commit. No obsolete API-provider
commit remains in the final branch series. The Ruby fix remains a separate
commit: its stable patch ID is unchanged,
`28c777b2e44b88a2757213ac112b4bcfacdd0504`; see
[range comparison](git-cache-ruby-equivalence.txt). Neither `flake.lock`,
`Gemfile.lock` nor the R package wrapper changed in this rework.

Published provider R `5436d3d7c36d3d5174eab3c44e3578830749d3db` remains at local
`refs/heads/2026-10-24-flake-update-downgrade-guard-replacement-provider-r-evidence`.
The same ref was created and SSH-verified remotely before replacing the feature
head, preserving the old source during staged rollout. The
[separate publication receipt](verification/git-cache-publication/published.json)
records that order and exact old/new refs without changing the source inventory.
Original R reviews, failed attempts and successful package/workflow/race/VM
receipts remain unchanged; they are historical evidence for their exact sources.

There are no database, lockfile or mirror-format migrations. Exact URL hashes
reuse existing full mirrors. New sibling locks coordinate new callers; old/new
concurrent writers are unsupported, while sequential cache reuse remains valid.
R was consumed as development CI/local source, with no released or deployed
state boundary. The [independent final review](review-git-cache-report.md)
explicitly accepted the complete history, preserved source ref and no-migrations
conclusion with no findings across all four lanes.

## Behavior and documentation

`GitCompare` replaces the API provider and delegates immutable commit proofs to
`GitRepoMirror`. Cold mirrors install atomically; warm mirrors fetch only missing
SHAs. Strict cache checks and negative-history traversal fail as evidence errors.
Both changelog callers share the per-URL lock through setup/read. Guard rejection
and error retain their existing transaction and publication-stop semantics.
Graph/source policy, follows resolution, manual updates and full-SHA JSON output
remain unchanged. Git's ordinary URL/authentication configuration and the caller
Ruby/Bundler contract are retained; no API fallback or token lookup remains.

The owning [input guide](../../worktrees/2026-10-24-flake-update-downgrade-guard-replacement/confctl/docs/flake-inputs.md)
and [manual source](../../worktrees/2026-10-24-flake-update-downgrade-guard-replacement/confctl/man/man8/confctl.8.md)
describe cache cost, shared locking, strict failures, authentication and visible
cache recovery. The lead read the full prose/error diff and approved it; the
requested generic error wording was applied. Man generation passed normally.
Exact rollout/provenance belongs here; design remains architect-owned in
[design.md](design.md) and [verification brief](git-mirror-verification.md).

## Quick evidence

All commands ran in confctl's declared `nix develop --no-write-lock-file` shell.
Focused RSpec groups passed 147 distinct examples with no failures:

- [86 examples](git-cache-focused-final.log): mirror/provider/guard, commit-message
  and cluster-log callers. The mirror cases use real local Git objects/processes.
- [36 examples](git-cache-transaction-cli.log): transaction, cached-metadata
  fallback and additive CLI compatibility.
- [25 examples](git-cache-manual-graph.log): existing manual behavior, graph and
  Nix output guarding.

The [final narrow check](git-cache-precommit-final.log) passed all 32 mirror
examples, linted all 12 touched Ruby files without offenses and passed diff
checks. [Man generation/lint](git-cache-lint-man-final.log) passed. Ordinary
[pre-commit and commit-message hooks](git-cache-commit.log) passed before the
[interactive consolidation](git-cache-rebase.log), without bypass or stash/reset.
Commit-message TextWidth warnings concern lines above 72 but within the owning
80-column rule.

The initial quick fixture attempt failed because RSpec mocks ran from an `around`
hook before the example mock lifecycle and a test double yielded the wrong block
arity. Both fixture problems were corrected before the passing checks; preserve
[that failed attempt](git-cache-quick-1.log) and [the following pass](git-cache-quick-2.log).

[Dry-run discovery](git-cache-suite-manifest.json) reports **203 examples**, with
both packaged caller/hook cases present and no pending examples. This establishes
the expected exported-suite count; it is not a full-suite execution result.
The later lead-owned exact published-package check passed all 203, including the
two real caller/hook cases. Its [acceptance](verification/git-cache-exported-check.json)
binds completed review `6bb7afca`, immutable source NAR
`sha256-/GFHeCx/ebnOHHzDmpyN+J/qWXafCT5k+1tkcq/wI8M=`, actual package
`/nix/store/nd9w86b14i55h95azazdn1rs7g8z1qgd-confctl`, and bundled Git 2.54.0,
Nix 2.34.8 and Ruby 3.4.9. Root retained 19 byte-identical receipt/graph files in
[verification/git-cache-exported-check/](verification/git-cache-exported-check/);
the original owned package/check/source roots remain intact.

## Handoff

Final review, provider-first publication with R preservation, all seven consumer
publications and exact exported-package verification are complete per their
owner receipts/reports. Selected updater/commit/final-lock, actual caller-shell,
cold/warm cache and race acceptance remain with the lead's serialized watchers.
The last bounded provider CI observation still records Tests 40118754612 in
progress; the lead will request one final observation after runtime. No CI wait,
dispatch or rerun is authorized here. Unchanged dependency refresh/build and
Terraform VM stages remain explicitly omitted under the accepted brief.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
