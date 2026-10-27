# Final review disposition and refreshed heads

Independent report `final-review.md` is preserved verbatim for original reviewed heads HaveAPI9b7afb2, vpsAdmincfe245130 and clienta914514. Reviewer0 saved gpt-6.1-sol/xhigh, all four lanes, no fallback/nested agents. No Blocking findings; both Important findings accepted for fixes and directly verified by lead under mandatory narrow-fix policy.

## Findings closed

1. Unsupported GET object-input metadata now fails IR construction at meta/object/input before output/emitter; required and optional variants plus no-write regression added. Existing runtime guard unchanged. No alternative query encoding.
2. Nested structural help/path/*_path/*_url checked during capture and saved-schema validation using existing context rules. Help only accepts method query for declared verbs; URL credentials/query/fragment and unsafe paths rejected without echoing values. Resource choices remain structural, validator include.values/default/Custom JSON remain data, with regressions preserving them.

Only parser/snapshot/docs/tests changed,6paths116insertions11deletions. Lead inspected exact diff and tests and applied direct prose pass.21focused parser/snapshot/CLI/output checks,5file scoped lint, actual retained full schema generation+no-write check pass; all3emitted source files remain byte-identical to independently reviewed package. No new IR/public/executor/transport boundary, so no affected-lane rerun required by narrow-fix policy. New expanded encoding would require review; none introduced.

## Accepted heads before the upstream refresh

HaveAPI final baseec84ec874eb209ab59848873998456293ddf3c52..head5d82858ea97f3168bf049d2b28cac16ba3520973: parser32861ab994e5bcb4ea27bca08b4684a5bcc3087c and emitter5d82858e. Fixup2b671f4e folded into parser, both final normal hooks/messages rerun/pass. Treece78a6c07aecb01155ba9af2366e66dfa88150ef equals tested fixup tree; lead checked tree/range-diff equality. Emitter stable patchIDfabc6dcc07bc9a816b63f6e52c326ed48454fe90 unchanged. No obsolete fixup, migrations, repeated pin streams, release/deployed/external generator state boundary.

New client originala914514 ->finale65b2a3cda92764365f5af1c3bcf53e7a18b3fcf, same emptyroot6c67b3c6e10e4096f6717345026371a89691f62a+one coherent initial package commit. Exact delta only tools/generator.json and generated ownership manifest,3insertions3deletions. Lead independently checked diff and three code file byte equalities. Exact-source regen/no-write check pass; no duplicate build/type/runtime tests for unchanged code. Normal hooks/no declared framework, clean tree/index. No old pin stream/scaffold/migration retained.

vpsAdmin remains exact independently reviewedcfe245130badcf2ac8ad8dd69f758ee4da618430, source/provenance/schema unchanged.

Final source digest881b30fd6c83eed4ec6a97e44848a1eacc1a4f5df0769d33fd6b4a7529f60eda; final manifest9b768e586ed0b7144010fe8a5a63c41ffe8064b336f83f236a7e0bd83c390b06. API source SHA dd7a4086877008ff7bcde39310d8ad4c7d72a9243dbf1fe258abce748004b4fd; index308d584b07b94655c6483464398e3285b6fbc7df29d38e9961b737cb908cb12d; runtime335717525047c3e2a803705b1665726adeaabd945bfe1a259dc0e3e3561e23ce.

## Verification and published successors

Postreview batch passed in 69 seconds: independent fresh DB export with exact schema/provenance/lock comparisons, exact published runtime 0.30.2 loopback harness (five single sends), and extracted npm archive ESM/declaration/executor consumers. Logs `/tmp/2026-10-26-typescript-client-generation-postreview.{log,status}`.

Later clean upstream rebases and the authentic provenance refresh are independently certified in `equivalence.json`; original review ranges and narrow-fix heads above remain immutable evidence. Final published heads: HaveAPI `73115aa5e66c5bebdc3150fff27e6054ff0c4271`, vpsAdmin `7456c7eaae11cee0c76a984b1386a94656510f88`, client `6bc81f83e9e5093d501099cd827523cd515d691b`. No substantive reviewed contract changed. No new migrations, repeated pin stream or externally consumed intermediate producer boundary.

Final refresh proof retained for recovery:

| Repository | Accepted pre-refresh range | Published range | Equivalence |
| --- | --- | --- | --- |
| HaveAPI | `ec84ec874eb209ab59848873998456293ddf3c52..5d82858ea97f3168bf049d2b28cac16ba3520973` | `cb43ae2367b12e22e602d69312bfd1f7331b4995..73115aa5e66c5bebdc3150fff27e6054ff0c4271` | Both range-diff entries equal; lead merge-tree reconstruction equals final tree `e883058fc63c07533813df4f7f9b85cb889c589f`; generator subtree and VERSION unchanged. |
| vpsAdmin | `b82eeca50cd4dd7bd76728685c7de8aad66e7ba5..cfe245130badcf2ac8ad8dd69f758ee4da618430` | `898e2881e8230d24fb06baee1c58737ae55e0009..7456c7eaae11cee0c76a984b1386a94656510f88` | Range-diff equal; lead merge-tree reconstruction equals final tree `784361ec663de9f8703b3ea6ddea4e49ad6c84a6`; API/tools/docs/plugins unchanged. |
| Client | `6c67b3c6e10e4096f6717345026371a89691f62a..e65b2a3cda92764365f5af1c3bcf53e7a18b3fcf` | `6c67b3c6e10e4096f6717345026371a89691f62a..6bc81f83e9e5093d501099cd827523cd515d691b` | Independent temporary-index reconstruction with only authentic provenance and expected producer-revision/provenance-hash changes equals final tree `81fdcc733fc185dbc84c03d26d9ac55bc345f1d8`; emitted code/manifest unchanged. |

HaveAPI upstream delta was documentation only; vpsAdmin upstream delta was unrelated dependency metadata. Fresh final vpsAdmin export passed in 36 seconds; schema/tooling lock match exactly, and parsed provenance differs only at actual source revision. Final provenance SHA256 `6f53633219ee1c2c743eeab841a0d0ee2a549924cbd4ea92f312f903ba4acc74`. No migration changed or became released, deployed or externally consumed during the refresh. Targets remain HaveAPI/master, vpsAdmin/master and client/main, without integration approval.

Exact-head CI observation remains in progress. No repository/machine claim held; no default feature integration, registry release, deployment or lifecycle action authorized.
