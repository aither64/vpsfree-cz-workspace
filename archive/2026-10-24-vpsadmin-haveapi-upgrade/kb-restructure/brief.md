# API article flow and logical changesets

The user requests authentication first, then the CLI and its main Ruby client,
followed by other clients. Cover the supported clients without privileging the
generated ones. Remove the unmaintained haveapi-fs material. Make the KB changes
individually understandable instead of publishing one combined edit.

The lead owns Czech and English prose under vpsfree-user-facing-writing and the
two pinned humanizers. Implementer3 owns the existing release tooling, guarded
manifests, focused verification and staging. Reviewer0 will independently review
the committed final text and complete changeset sequence. No production writes.

Editorial commits separate removal of haveapi-fs, restoration of article flow
and Ruby prominence, and completion of the other-client introductions. Prepare
an ordered publication sequence against the captured production baseline with
localized summaries and per-step diffs; retain the previous combined candidates
as historical evidence. The supported release mechanism determines how each
reviewed step is staged and eventually guarded for promotion.

Preserve authentication/CLI executable content, reciprocal page markers,
existing useful links and examples, generic HaveAPI 0.31.2 versions, and the
separate vpsAdmin TypeScript client 0.1.1/runtime 0.30.2 pair. Existing Ruby backup
examples stay with the main client. Add concise PHP and Go introductions and a
simple Ruby read example from the actual client interfaces. Do not expand into
an SDK build campaign, refresh unrelated legacy examples, or touch the cluster.

Acceptance: both articles read in the requested order; Ruby is explicitly the
main client; all supported language clients have identifiable sections;
haveapi-fs is absent; protected examples remain unchanged except newly added
bounded examples; final review passes; staged source and rendered headings,
language links and localized revision summaries match the reviewed changesets.
