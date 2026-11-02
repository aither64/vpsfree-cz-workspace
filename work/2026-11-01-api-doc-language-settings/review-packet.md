# Final review packet

Session: `2026-11-01-api-doc-language-settings`. Read [plan](plan.md),
[state](state.md) and architect-owned [design](design.md).

HaveAPI worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-api-doc-language-settings/haveapi`.
Base: `391b0190241cf195a69b06f7297d3e4eebec5a83`.
Final committed head: `fd61d71ea06a971453c3491370dbc8133b410926`.
Working tree and index are clean. No long integration tests started.

## User scope and acceptance

Localize Ruby-server HTML documentation and linked internal protocol articles in
Czech/English. Use browser language initially and English fallback; save manual
choice. Settings must show exactly **English / Česky** above Theme, without an
Automatic option. User approved moving English sources into `doc/en/` alongside
`doc/cs/`. Keep executable examples English; authored comments can translate.
The user requested a temporary API preview/URL after completion; not launched yet.

Inspect locale isolation from API/action/client behavior, authorization and cache
semantics, browser/weighted negotiation and persistence, native/JS selection and
fragment preservation, static/dynamic/a11y text, translated metadata/search,
unchanged executable samples and schema machine representation, article fallback,
existing public routes/anchors and source-link/package completeness.

Plain application-authored descriptions and custom renderer prose retain their
supplied text unless existing localization hooks provide translations. There is
no automatic translation, new API description schema, application-wide i18n,
client rollout, production deployment or integration in this scope.

## Complete series and provenance

1. `aa07bfa91179ffda64d5a101a83ed73b3b77e69b` — runtime/UI/catalog, scoped docs
   locale, search, article lookup, helpers/templates, canonical translations and
   generated server locales; regression coverage/scanner.
2. `fd61d71ea06a971453c3491370dbc8133b410926` — article source move, five Czech
   counterparts, authored comment translation, source links, packaging/build
   consumers and related tests/guides.

Final diff: 84 files, 4440 additions / 811 deletions with rename detection.
Most article additions are Czech translation; English files moved. Review full
`git diff -M BASE..HEAD` and both commits, not only the latest commit.

The split separates executable runtime changes from substantial article content
and its packaging. They ship together because locale-aware lookup needs the new
source tree. A1/A2 were deliberately one runtime commit: new helpers, template
calls and catalog keys are inseparable. Interim fixes were folded into those
commits; no abandoned approach, shim or follow-up fix commit is retained.
The B message-only amendment replaced an unpushed initial commit without source
changes; review the final exact series above.

**No migrations**: no DB/schema/on-disk protocol migration, merged/released/deployed
or externally consumed intermediate migration. No dependency/channel/config pin
updates or repeated update streams. Generated catalogs are one final translation
stream in runtime commit; client catalog regeneration produced no diff. No
feature commits have been published, deployed or integrated at review start.

## Documentation and compatibility

Owning runtime is HaveAPI servers/ruby; consumers include every API mounted through
HaveAPI (vpsAdmin is a known framework consumer), the internal shared docs route,
example renderers and package/release documentation consumers. Existing server
API locale configuration and client interfaces stay stable. No downstream pin
change or new consumer interface is proposed.

Project explanations: `doc/en/documentation-ui.md` language section;
`doc/agent-instructions/documentation.md` article layout/authoring;
`doc/agent-instructions/localization.md` canonical catalog consumers;
English/Czech `protocol`, `create-client`, `typed-input-validation`,
`client-examples`, `readme` articles. Main lead applied pinned bilingual writing
skills directly after drafts settled. Existing shared schema/assets remain shared.

Only new persisted state is a documentation-specific mount-scoped cookie that old
servers ignore. Deploy/rollback a complete matching server package with assets,
catalogs and generated articles; preserve public URLs and English anchor IDs.
No physical machine deployment or reservation is involved in temporary preview.

## Quick verification completed

- Runtime locale/navigation/search/OAuth: 128 examples, 0 failures (9.58s).
- Affected locale/OAuth/detail/exception batch: 122 examples, 0 failures (8.84s);
  final detail 12/12. Covers scoped restore, API isolation, parity and error cases.
- Browser asset target passed; 26-file scoped runtime RuboCop passed.
- i18n update/health passed, scanner 7/7, validators 18/18, all ERB compiled,
  A2 scoped RuboCop 4/4, whitespace clean.
- Shared pages/extracted-gem packaging/exceptions: 43 examples, 0 failures (4.48s).
  Relevant B Ruby style 7/7; 52 relative targets exist; stable bilingual IDs and
  noncomment samples; all four generated schema code blocks per locale match
  exact base template output. `sh -n utils/copydoc.sh` passed.
- Both commits passed required hooks. B Python docstring path update required
  documented ignored `uv sync` environment/lock preparation, then PythonChecks
  passed. No bypass. Root/server/JS dependencies prepared; transient concurrent
  Bundler reinstall race resolved and subsequent commands use no-install shell.

## Review assignment

Risk: **High** for review coverage because documentation authentication/error
paths, locale/cookie persisted preference and authorized search/cache boundaries
are touched; no intended authorization or protocol change.

Reviewer: retained independent `reviewer0`, `gpt-6.1-sol`, **xhigh**, read-only,
same-session ready/identity/settings verified. No fallback or settings override.
Lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
Read each corresponding mandatory-change-review reference. Review directly without
nested reviewers; record findings with severities and explicit full-history,
repeated-stream and migration conclusions. Save report in `review.md` here.
