# HaveAPI 0.32.2 independent final review packet

Status: final packet prepared; lead assignment starts independent review.

## Outcome, scope and owner

User: “Backport commits from haveapi master into haveapi-0.32 and make a new
patch release 0.32.2, publish it.” Acceptance: all applicable source changes,
consistent shared versions, required checks, approved branch fast-forward and
coordinated immutable release through the existing protected workflow.
No HaveAPI/master integration, downstream deployment, new release infrastructure
or broad documentation audit is included.

Session: 2026-11-02-backport-and-publish-release. Plan/state/design and individual
release receipt are adjacent. Canonical repository git@github.com:vpsfreecz/haveapi.git;
worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-backport-and-publish-release/haveapi.
Configured target haveapi-0.32. Base 9efeadf91d894e01d1d4f4a3e3fc64c6309785c7;
accepted source master f29c1e4675bc1f79641faa619b8c68ecec923c71.

Implementer0 owns source/tests/technical documentation and all follow-up fixes.
Lead owns coordination, acceptance, user-facing release-note pass and publication.
Architect0 authored design. Reviewer0 is independent retained review-purpose
Sol/xhigh, read_only, lowest eligible index; preserve saved settings, no overrides.
No fallback. Risk: high because documentation authentication/authorization context,
shared generated-client public contracts and irreversible registry publication
are affected. Apply general, architecture/repetition, scope/proportionality and
risk/compatibility lanes; read all applicable skill references yourself.

## Complete history and provenance

Exact 12 upstream source hashes/order and excluded equivalent backports are in
[design.md](design.md). Preserve original logical commits with -x attribution as
required by HaveAPI patch-release instructions; sources/follow-ups are already
integrated on master and requested as backports. Do not treat these as abandoned
local iterations. New local correction: only generator-runtime installation
example 0.30.2 → 0.32.0, proven inconsistent with supported generator runtime;
separate focused documentation commit. Version/changelog metadata stays separate.
Review the full base-to-final-head series and final diff, not just final metadata.
Explicitly conclude on obsolete history and update streams. No repeated input
pin stream is planned; one coordinated version bump. No migrations, schema or
persisted-state changes; no migration merge/release/deployment/external-use
lineage to preserve. New deliverable has not been published/deployed.

## Compatibility, documentation and consumers

HaveAPI owns protocol/server/client generation. Existing examples and generator
fixtures consume its interfaces. TypeScript output uses the existing npm
haveapi-client runtime; its supported tested version becomes exactly 0.32.0
(independent of 0.32.2 candidate metadata). Existing generated output remains
unchanged until regeneration. New output reserves describe/root helper names;
explicit help routes need matching method selector/placeholders. Local validation
raises ClientInputError, a TypeError subclass; executor errors remain unaltered.
No API data-format migration or coordinated fleet update. Retain matching older
generated source/runtime pairs for rollback. Detailed supported contract and CLI
examples live in clients/typescript/README.md and its docs. Server documentation
source moves to doc/en and doc/cs while public routes remain stable; nested
articles and local assets must be in the server gem. Review catalog ownership,
locale/auth isolation, native controls, content-digest assets, example source and
packaging. Performance normalization must retain strict unrelated input guards.

Owning project docs include README, doc/agent-instructions/{development,releases,localization}.md,
doc/{en,cs} articles, clients/typescript/README.md and doc/en/client-examples.md.
CHANGELOG records the patch and compatibility constraints. Lead applied
vpsfree-user-facing-writing/humanizer-en to new notes and accepted exact version
pin correction because generator support requires it. Temporary branch, release
execution and hashes belong in this session's release.md/implementation.md.

Publication uses existing release.yml, all five gems, npm/browser bundle,
Python wheel/sdist and PHP mirror, finishing GitHub Release last. No master
version bump. Protected environment is configured and original user explicitly
requested publication. Partial publication is non-atomic; original tag/artifacts
must be retained and hashes reconciled before retry. Review does not perform
publication, integration or long checks.

## Final committed range, inventory and quick checks

Final head dca492c680b8d52f1e4c8b51e89cb7a97fc83c38, 14 commits.
Full commit inventory and final diffstat: [final-commit-inventory.md](final-commit-inventory.md).
Raw full diff is available directly with git diff BASE HEAD in the owned worktree.
All intended changes are committed and tracked worktree is clean.

Final-head quick evidence: quick-checks.json, quick-checks.log. Commands in
top-level prepared Nix shell: git diff --check BASE HEAD (0.072s);
bundle exec rake i18n:health (0.709s); ruby utils/release/cli.rb check-clean
(0.405s); make release-check (0.974s). Full make check-format (15.331s) and combined shell/node syntax (0.608s) also pass.
All exit 0. All source/doc/version
commits ran declared normal Overcommit hooks. make version preserved external
resolution records across all ten local lock inputs; six locks byte-identical,
four differ only by local HaveAPI identity/expected npm formatting.
No long integration checks or CI started before final review gate.

Return independent report to lead; lead will preserve it as review.md.
Remain read-only; do not launch tests/builds or nested reviewers. Explicitly conclude on full branch history, source equivalence,
repeated streams, migration lineage/no migrations and readiness to proceed.
Report Blocking/Important/Advisory findings with concrete file/commit evidence;
do not treat packet conclusions as authority.

Additional complete evidence: source-backport-mapping.md (12 identical stable patch IDs),
source-range-diff.txt, final-history.txt, final-diffstat.txt and final.patch.
Final range contains 150 files, +7551/-1111; growth comes from upstream changes.

## Post-review narrow successor (lead verification)

Reviewer report binds original dca492c6 range and has only BlockingB1. Corrected
final head1ef9b204ba45bb261d3334be5c555cc1856b713b uses same base. All12 source
commits unchanged. Local doc commit591a1b6083763e8e7b03edcffd58b4651558056f
adds exactly matching Czech npm0.32.0 token; metadata patch unchanged. Original
packet/inventory preserved. Lead independently inspected final old/new diff,
range-diff, clean source and focused result:1existing example,0failures.
make doc and all11 exact-head quick checks pass. B1 resolved under step9;
review expressly requires no full rerun for this narrow fix. Longer checks may
proceed; publication/fullCI not yet claimed.
