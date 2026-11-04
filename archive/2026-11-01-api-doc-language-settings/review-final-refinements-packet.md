# Final user refinements and measured rendering fixes

Retain reviewer0/Sol/xhigh/read-only, all four affected lanes. Read prior
[original review](review.md), [CI follow-up acceptance](review-followup.md),
[design](design.md) and current [state](state.md). Do not repeat unaffected
protocol-article translation or the already accepted receipt-policy review.

HaveAPI worktree unchanged. Base `391b0190241cf195a69b06f7297d3e4eebec5a83`.
Exact final HEAD `aa190aa749f80720546d6786d45b16335feaa42b`, clean index/worktree.
Inspect affected delta from accepted/published `e7ac8578a2ffd07b3ac7da05a27996191619a8f9`:
48 files, 2194 additions / 220 deletions, primarily catalog translations and
meaningful behavior/parity tests. No long final tests after these changes yet.

## User additions and final acceptance

- JS documentation-language select changes immediately with no visible Apply
  button; functional native form/button remains without JS.
- Generated explanatory comments must localize, including Ruby token reuse.
  Noncomment code, literals, package names, commented commands and transcript
  sample data stay unchanged. All framework-owned generated Go/Rust/TypeScript
  text (comments, labels/variants, limitations) also translates.
- Use Czech sidebar `Jazyk`; overview `Projdi si všechny zdroje`; remove the
  redundant permission reminder in both languages; API address text has no
  redundant GitHub client link. Keep legitimate library guide links.
- Czech breadcrumbs must retain styling; style/behavior use stable markers,
  translated accessibility labels remain.
- Add a working native Apply action for no-JS example language/client/detail
  selection. JS immediate controls remain; both Apply buttons hidden after
  enhancement. HTML-only validated selectors do not change API/OPTIONS/search
  semantics or add persistence.
- User confirmed existing i18n:health was the remembered translation guard.
  Extend recognized calls only; no arbitrary-literal scanning framework.

## Complete final series and consolidation

1. `9b93273eabd6211942cc341d31fa1a2632559834`: original runtime/UI/catalog plus
   final controls/breadcrumb/text/helper/scanner changes and rendering fast paths.
2. `1c758555455e011bed6200eb2339d7af0146bf0c`: articles/source layout/package.
3. `824b795502bdea0a426e6601d80e98141a5e61ea`: previously accepted exact
   packaging receipt policy, patch preserved.
4. `ef19be9433aa0fc9f897f2db8ce7b117a00ee0dc`: localized generated comments,
   immutable Context locale/messages, adapter notices, syntax/parity tests/guides.
5. `aa190aa749f80720546d6786d45b16335feaa42b`: native example selection.

UI/catalog follow-up and measured helper fixups folded into runtime owner. The
UI guide delta stays with article owner because `doc/en/` is introduced there.
Comment/message/catalog source keys ship in runtime; emitting optional messages
ships with comment package; native Apply label is inseparable from native form.
No superseded branch approach or standalone fixup should remain. Assess final
series and migration/repeated-stream provenance explicitly. No migrations,
dependency pins, changed budgets/reference or supported intermediate DB states.
Prior heads were published/previewed, not deployed/integrated defaults.

## Implementation boundaries

Immutable Context captures locale (default English), retains it through `with`,
exposes optional documentation_message/example_comment capability. Actual authored
comment emission owns physical-line prefixing; no regex postprocessing of rendered
programs. Standalone/older contexts preserve exact English defaults; adapters gain
no server dependency or changed render signature/shared mutable request locale.
Typed Go/Rust limitation metadata translates at request rescue; TypeScript keeps
one generic reason and does not reveal hidden schema details. Results retain
existing frozen String reason contract. Stable IDs/package names stay machine data.

Native example query fields: example_language/client/detail. Validate shape and
encoding, allowlist available renderers/profiles, stale scalars safely fall back;
language wins mismatching old variant. Selected supported detail opens in each
existing disclosure; alternatives remain accessible. Valid page/resource/q/explicit
doc_lang retained. No new storage writes on native submit/load. JS explicit query
initializes ahead of saved choice, then normal immediate preference behavior.

Measured optimizations, separately justified by actual failed original-base pair:
English helper avoids a duplicate translation; only successful static String
translations with String keys/nil defaults/no values memo within request+locale,
stored owned/frozen and returned as fresh copies on hits. Defaults/interpolation/
non-String/missing/hash bypass; nested/error scopes clear. Available renderer list
is computed once per request; metadata/detail union remains live. Fresh identity,
version, locale, description/profile request tests guard against stale authority.
No global/thread cache, generalized subsystem, budget/reference/runtime relaxation.

## Verification completed before final review

- A2 UI/catalog/scanner: health/generated checks; UI+overview18/18; scanner16/16;
  assets; scoped style/hooks. Stable breadcrumb classes tested both languages.
- Comment package: server114/114, Go2/Rust2/TS2 adapter matrices, 260 exact English/
  direct baseline outputs identical. Emission-boundary tracing compares complete
  en/cs templates and reconstructs actual outputs; does not regex-strip final
  source. Actual Czech Ruby/PHP/JS/TS/Python syntax plus Go/Rust formatter parsing,
  multiline comment inertness, hostile shell data, old/frozen context defaults,
  missing-Czech fallback, dynamic path escaping and TS privacy checks passed.
- Native selection/search18/18, navigation1/1, assets/node/style/hooks. Real generated
  TypeScript fixture included; malformed scalar/duplicate/array/encoding, empty/
  stale client, singleton, limitation, query and protocol isolation covered.
- Static memo locale19/19, style/hooks; available-list35 focused cases, style/hooks.
  All intended source authored commits passed required hooks; no bypass.
- Exact whole-source final diagnostic under Worker policy (test/C.UTF8/UTC/JIT off),
  same frozen graph, 2 warmups/3×8/setup excluded: English resources +3.56%, actions
  +3.41%; Czech +7.01%/+7.07% versus original base, below unchanged10% diagnostic
  allowance. English 17 codeblock hash exact across base/e7/final; perlocale bodies
  stable. Prior development-mode diagnostics retained/qualified, not gate proof.
  Hosted exact-head original-base comparison remains mandatory and unrun for final.

## Preview evidence and limits

Requested live candidate at port4567 serves exact committed native-feature
snapshot `ebc3e7d46bcada90f4209213c9f66a4b1262cef4`, isolated from uncommitted
work and verified933 blobs. Actual Chromium en/cs passes all three profiles,
comments/generic TS privacy, code equivalence, JS-hidden controls, no-JS language
and example form flows, query retention, breadcrumbs/Jazyk/editorial and storage
separation. See [preview receipt](preview.md). It is a visual candidate; final
rendering memo successor still needs browser refresh after review/tests.

Review risk High for request locale/authorization freshness/public adapter
capability/native input boundaries. Reuse existing reviewer/settings. Assess all
four affected lanes and final whole-history/no-migrations/repeated-stream conclusion.
Remain read-only, no nested reviewer/build/test campaign. Report findings to lead
for durable save. No merge/deployment approval is requested or implied.
