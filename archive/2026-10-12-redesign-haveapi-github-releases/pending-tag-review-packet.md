# Final review: pending draft tag correction and 0.29.12 candidate

Session2026-10-12-redesign-haveapi-github-releases, workspace
/home/aither/workspace/ai/vpsfree.cz; current state/plan/design apply. Review directly
under mandatory-change-review and all four lane references, no nested agents,
edits, long tests, publication or lifecycle actions. Remain read-only.

Goal: complete user's real automated patch-release test. v0.29.11 user-approved
publishing job39305802582 also failed in draft preparation, nil.fetch after the
REST listing missed the intended pending tag. Credentials and registry/PHP steps
were skipped; all three gem and npm0.29.11endpoints404. Preserve both failed tags
and their original files. No blind retry, tag move, replacement artifacts or
premature public GitHub Release.

Exact committed candidates, canonical SSH git@github.com:vpsfreecz/haveapi.git:
- Master target refs/heads/master, worktree worktrees/<slug>/haveapi,
  branch2026-10-12-redesign-haveapi-github-releases:
  base526648131af45df68c25ac0042a52f22c7a81df5,
  headc58704a08451a231fdf6c6123437133422af46dc.
- Release target refs/heads/haveapi-0.29, worktree worktrees/<slug>/haveapi-release,
  branch2026-10-19-haveapi-0.29.10 (retained name, VERSION now0.29.12):
  base7fb218e28a86ab1d27de74ccb92c2a45063a4f78,
  head355c2990a4bfd3940d3234cb2077ad0127f43551.

Complete new histories/messages in pending-tag-{master,release}-history.txt;
complete diffs in pending-tag-{master,release}-final.diff. Independently recompute
base/head, clean source, merge base and diff hashes. Master one focused commit
c58704a, provenance from release c8cfb16e96c9c9237d733af2a657dee42e71c79f;
release c8cfb16 (helper/regressions/recovery docs), then355c299 version/changelog.
These are all intended edits, committed with hooks. Version metadata is separate
from the functional correction and supporting docs/specs.

Preserved earlier boundaries: both previous master ranges are merged at5266481.
Earlier release history is merged into haveapi-0.29 at7fb218e and consumed by
immutable annotated v0.29.10 (run39291918638) and v0.29.11 (run39305802582), each
with human approval and retained original source-bound artifacts. Neither
published registry packages. Do not rewrite these already shared/tagged sources.
Only the new two-commit release/one-commit master series is unmerged. No obsolete
new fixups, superseded unmerged iterations or repeated pin/dependency/generated
update streams. No pins change; shared version update is one new commit. No
migrations in either range and none merged/released/deployed/externally consumed.
Explicitly conclude whole-history/consolidation and migration lineage.

Implementation: github_release resolves exact intended tag through GraphQL
repository.release(tagName:$tag){databaseId}, then REST get-by-ID; github_api
owns shared JSON/error handling. Only explicit GraphQL null means absent; failed
queries at either stage raise before creation/upload. Creation retains
--verify-tag and missing post-create result now yields clear release error.
REST metadata can use a synthetic untagged-* name; no matching on that field.
Current exact gh2.102.0 implementation uses the same pending-tag resolution:
https://github.com/cli/cli/blob/v2.102.0/pkg/cmd/release/shared/fetch.go#L219
https://cli.github.com/manual/gh_api
Inspect actual schema/contract, not just prior optimistic REST fixtures.

Nine focused examples cover synthetic-name pending draft/no duplicate creation,
new draft, published release, explicit absence, HTTP403/404 failures at each API
stage, and post-create absence before upload. Repro with old implementation:
9examples/8failures (only explicit absence passed); pending-tag-repro.log/status.
Final30examples pass normally and under GITHUB_RUN_ID=123. Release and master
helper/spec/release-procedure files identical. No source/run/hash/assets, PHP
preflight, immutable registry checks, atomic no-force push, finalization,
workflow approval or credential scope changes.

Owning component remains utils/release/Publisher, CLI/Makefile/release.yml;
external destination remains PHP mirror root-layout Composer repository. No new
public interface, schema, recovery framework, permissions or downstream pins.
Runtime sources differ fromv0.29.9 only in maintained version declarations;
existing tests and both Elixir trees unchanged. Master retains0.29.0. Versions,
gem constraints, example dependency, JS metadata and bundle now0.29.12 on release.

Docs: nearby comment explains GraphQL pending-tag requirement. Canonical
 doc/agent-instructions/releases.md now explains that reruns keep original tagged
code, and a source correction needs a new authorized patch version while failed
tags/artifacts remain preserved. Entry points remain correct. Changelog includes
pending-tag correction plus the first consumer-visible automation/npm metadata
changes. Failure history and rollout remain in session records. Main lead applied
workspace user-facing writing/Humanizer directly to public prose.

Quick evidence: pending-tag-{master,release}-quick.sh/log/status, both0. Metadata,
30helper examples normal and under runID123, whole Ruby lint (243/244files), shell
syntax, Git whitespace, runtime-byte preservation; hooks passed. No long checks
on new heads yet. Full components/clean package and safe feature CI planned after
review. No new master integration or version publication authorized.

Risk high: release machinery controls irreversible registry/cross-repo writes.
Assigned lanes general, architecture/repetition, scope/proportionality and
risk/compatibility. Retained reviewer0, native thread
01a1309b-3a6c-7cd2-917f-4426d9b48c52, saved gpt-6-astra/xhigh, read_only, no model
or effort override/fallback. Verify dev-session current from tracking CWD before
owned records, roster, actual native identity/settings and final exact heads.

Live evidence limit: session token cannot retrieve drafts (gh release view says
release not found). User was asked for read-only logged-in gh output with
isDraft/tagName/databaseId/apiUrl to verify actual metadata before another real
release. That answer is pending; do not claim write-token draft lookup or actual
OIDC/SSH publishing exercised. This independent gate concerns completed source;
new tag must not be pushed while diagnostic validation/authorization remains
outstanding. Cross-registry partial publication remains possible after transport
failure or concurrent PHP update; retain originals and diagnose before retrying.

Return concrete findings with severity/file/commit, exact reviewed ranges and
explicit complete-history/repeated-stream/no-migrations conclusions. Leave open.
