# Final exact-head preview candidate

Status: candidate browser acceptance passed and the lead subsequently released
the final refresh after exact-head broad/hosted verification. The final source is
now live; see [final live receipt](preview-final-live.md). This file retains the
candidate preparation evidence.

- Exact head: `51047a211d71f817ab25f2def1692517f00c15c6`.
- Exact tree: `9500a75d5f7976796a580b15a512990e6d86b7b0`.
- Isolated export: `work/2026-11-01-api-doc-language-settings/preview-source-51047a21`.
- Export equivalence: all 933 Git blobs match; no missing or mismatched files.
  [Source receipt](preview-final-source.json).
- Fixture preload: [preview_profiles.rb](preview_profiles.rb), SHA-256
  `b10a4863e2d119f5e5aa954b8279b808b5a40aa467827c0e776b9e855cc0828d`.
  Real Go, Rust and TypeScript profiles and inert in-memory samples are retained.
- Runtime launch: [preview_launch.sh](preview_launch.sh), existing prepared
  unbundled benchmark environment, no installs or project worktree/index changes.

The candidate is `haveapi-doc-language-candidate-20261101.service`, Ruby PID
`29112`, invocation `4398ca8e9b6b4ffaa81e64947146bfdf`, started
`2026-11-01 23:04:02 CET`, listening only on `127.0.0.1:14567`. Health passed.
Log: [preview-candidate.log](preview-candidate.log). Its working directory is the
isolated final export above.

Existing bounded Chromium/Playwright harnesses all passed on this candidate:

- [Native selectors and JavaScript preferences](preview-final-native-candidate.json):
  resource/authentication no-JavaScript language/client/detail Apply flows;
  page/resource/query/locale retention; real generated TypeScript examples;
  Go singletons; selected open code and collapsed accessible alternatives;
  explicit Rust/blocking/simple URL selection ahead of stored Python/thorough
  with zero load writes; immediate JavaScript switches; both Apply buttons hidden.
- [UI](preview-final-ui-candidate.json): hidden Apply with JavaScript and visible
  usable native language form; Czech horizontal unnumbered breadcrumbs, Jazyk,
  edited overview, no standalone GitHub link or permissions reminder.
- [Comments and code](preview-final-comments-candidate.json): localized Ruby/Go/
  Rust Async/Blocking/TypeScript comments and labels in English/Czech, unchanged
  executable lines and command/package literals, generic localized TypeScript
  limitation with no schema/sample names in its reason.
- [Generated clients](preview-final-generated-candidate.json): all four generated
  client selections produce visible executable examples; all three initialization
  package identities appear in both locales.

No browser page errors occurred. These were existing known quick checks, each
under one minute; no long browser operation or new watcher was needed.

Before the final refresh, the live service was `haveapi-doc-language-preview-20261101.service`, Ruby
PID `4037161`, invocation `91d236936a5e464e9f1ce7714aeb8623`, on the prior exact
`ebc3e7d46bcada90f4209213c9f66a4b1262cef4` export. URL:
<http://aitherdev.int.vpsfree.cz:4567/v1.0/>. Its
[service definition](preview-ebc-service.txt), exact export and byte-identical
[preload](preview_profiles-ebc.rb) are retained for recovery.

Prepared final payload, subsequently applied to the live service:

```sh
HAVEAPI_PREVIEW_SOURCE_ROOT=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-api-doc-language-settings/preview-source-51047a21 \
  /bin/sh /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-api-doc-language-settings/preview_launch.sh
```

The existing same-service/port replacement contract was executed after the lead
released it; live health and bounded browser checks passed. The live service and
loopback candidate remain running. No session lifecycle, host, firewall, proxy or
cleanup action is authorized by this record.
