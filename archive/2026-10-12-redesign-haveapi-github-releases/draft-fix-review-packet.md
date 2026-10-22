# Final committed-candidate review: draft release lookup and corrected patch

Session 2026-10-12-redesign-haveapi-github-releases, workspace
/home/aither/workspace/ai/vpsfree.cz. Read plan.md, design.md and current state.md.
Goal: complete the user's real patch-release test without changing runtime
behavior or Elixir. The approved v0.29.10 publishing job created a draft, then
queried the published-only release-by-tag endpoint, obtained nil and failed
before registry writes. Preserve its immutable source, draft and saved originals.

Review both complete new ranges in vpsfreecz/haveapi, SSH origin
 git@github.com:vpsfreecz/haveapi.git:

| Candidate | Worktree under worktrees/2026-10-12-redesign-haveapi-github-releases/ | Target | Base | Head |
| --- | --- | --- | --- | --- |
| Master fix | haveapi | refs/heads/master | c14e7d3158b91c134c2817b489cd29772fc09f82 | 526648131af45df68c25ac0042a52f22c7a81df5 |
| Corrected patch | haveapi-release | refs/heads/haveapi-0.29 | b27a031fa03d8d985a3abd2679ce2fc14fe53602 | 7fb218e28a86ab1d27de74ccb92c2a45063a4f78 |

Both worktrees clean, all intended changes committed. Master branch name remains
2026-10-12-redesign-haveapi-github-releases; release branch name remains
2026-10-19-haveapi-0.29.10. Do not confuse branch name with current VERSION.

Complete new history:
- Master: 5266481 release: find draft GitHub releases before uploading assets.
  Provenance from 2b745b7; identical helper/spec files in both candidates.
- Release: 2b745b738f08a1cfb55b9983eac48b7094c527e2 focused fix and regressions;
  7fb218e28a86ab1d27de74ccb92c2a45063a4f78 Version 0.29.11.
- Full messages: draft-fix-{master,release}-history.txt.
- Full diffs: draft-fix-master-final.diff SHA256
  85c60bb23e5356ab2c41012bd9d5a7fdceff36f1f61ff097c359a57a04db2901;
  draft-fix-release-final.diff SHA256
  0a9dc4f56cc1931a619e99b9539429f60871a64766363f389b421d99cf6b3692.

History disposition: the earlier master two-commit implementation is already
merged in master. The earlier four release commits (974e57b toolchain, 41e37c2
implementation, c59483e docs, b27a031 version) are already integrated in
haveapi-0.29 and immutable annotated v0.29.10. That exact source was consumed by
Actions run 39291918638 and has retained original artifacts (manifest hash in
release-tag-approval.md). No registry package was published for 0.29.10.
Do not rewrite these existing merged/tagged boundaries. New fix and version
metadata are deliberately separate; no obsolete new fixup/design iterations,
new pins or repeated dependency update streams remain. No migrations anywhere
in either new range; none merged, released, deployed or externally consumed.
Please independently conclude on complete history, consolidation and migrations.

Implementation: Publisher#github_release lists all releases using gh api
--paginate --slurp, finds exact tag_name, includes authorized drafts, and raises
API errors before any create. Retains existing immutable asset validation,
source/run/hash checks, PHP preflight, registry order, atomic no-force PHP push
and finalization. Five regressions cover later-page existing draft, newly
created draft, published tag and HTTP403/404 refusal without create/upload.
Old code with those examples: 5 failures, draft-lookup-repro.log. No generalized
release framework, early-publication workaround, source substitution or retagging.

Owning code remains utils/release, called through its CLI/Makefile and release.yml;
PHP mirror remains vpsfreecz/haveapi-client-php. No new public interfaces, artifact
schema, package identity or supported runtime contract. New release VERSION,
maintained constants/dependencies, tracked JS bundle and changelog use 0.29.11;
master version remains 0.29.0. No application behavior, existing component tests,
Elixir, translations or dependency/action pin changes in new ranges.

Docs checked: each repo AGENTS.md and canonical
 doc/agent-instructions/releases.md; README points to that procedure. Procedure
already describes draft retention and finalization correctly; a nearby comment
records published-only endpoint rationale. No new procedure is needed for this
bounded bugfix. CHANGELOG.md describes the correction and user-visible contents
of the first automated release. Individual failure/approval/source evidence
belongs in release-0.29.10.md, release-tag-approval.md and state.md.

Quick checks: draft-fix-{release,master}-quick.sh/log/status, both exit0:
make release-check; make release-test (26 examples); GITHUB_RUN_ID=123 make
release-test (26 examples); whole Ruby RuboCop; shell syntax; Git whitespace.
Release runtime comparison against v0.29.9 proves only version declarations
changed, existing tests and Elixir unchanged. Master servers/clients unchanged.
All commit hooks passed. No long integration tests for the new heads yet.

Risk high: irreversible registry publication / cross-project PHP synchronization.
Assign all four lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. Retained reviewer0, native thread
01a1309b-3a6c-7cd2-917f-4426d9b48c52, gpt-6-astra/xhigh, read_only, saved settings,
no overrides or nested agents. Read mandatory-change-review SKILL.md and all four
lane references in full, plus applicable workspace/repository procedures.
Perform the review directly; no edits, long builds, pushes, approvals or lifecycle
actions. Verify current identity with dev-session current from tracking directory.

Acceptance: exact drafts found with pagination, API failures remain visible;
retained originals and publication invariants preserved; coherent patch version
metadata and unchanged runtime sources; no new unauthorised publication. Actual
OIDC/deploy-key/Packagist use remains untested. After review, run fresh complete
component/package and safe Actions checks. New master merge needs explicit user
target approval. Corrected version needs fresh publication authorization and
human protected-environment approval; old approval does not cover 0.29.11.

Return concrete findings ordered by severity, exact reviewed ranges and explicit
whole-history/repeated-stream/no-migrations conclusions. Leave session open.
