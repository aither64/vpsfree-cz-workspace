# Explicit callback name: final review packet

User request: prefer CallbackClient and AsyncClient, keeping Client as a
backward-compatible alias. Naming addition only; owner0 final commit/head and
quick evidence are supplied with assignment and current inventory.

Session/workspace: 2026-10-19-haveapi-async-client under
/home/aither/workspace/ai/vpsfree.cz. Worktree is
worktrees/2026-10-19-haveapi-async-client/haveapi. See plan.md/state.md and
haveapi-review-inventory.md; original review packets and findings remain evidence.

Acceptance: one callback constructor, Client === CallbackClient under ordinary
UMD/CommonJS/AMD loading; same prototype, statics, callable callback behavior,
undefined returns, no new eager Promise/AbortController requirement. Both names
work as generated TS value and instance type exports. AsyncClient unchanged.
Preserve runtime constructor name Client; prefer CallbackClient in public docs.

Before this addition accepted HaveAPI head was
76f190f9561eabee3414919ddd26e62e48c43f58, base
c14e7d3158b91c134c2817b489cd29772fc09f82. Whole series is fixture `34f431e`,
callback migration `0e63360`, async `81994d2`, guidance `76f190f` plus final naming commit.
No migrations, persisted state, server protocol, dependency/lock/pin/version or
deployment changes. Existing reviewed TS/Rollup introduction is one stream.
Old source-producing callback/async stages remain independently buildable.
Review full series/final diff and explicitly assess whether this additive
user-requested naming commit is a useful separate purpose and whether obsolete
approaches or repeated updates remain. Prior whole-branch conclusions may be
reused where still valid; no unrelated full investigation is requested.

WebUI stays at `5dd2333b9af230d4a81c8f772cbbb08d39b14913` based on
7860521f30826c3886c89c35e8ab6f4e082e0a4b; no WebUI edit. Adapter imports
AsyncClient. Existing old callback consumers import Client, which stays same.
Owning API is HaveAPI clients/js; public entry is src/haveapi.ts and package
main/types refer to generated dist JS and declaration tree. Docs touched:
clients/js/README.md, doc-async-client.md, doc-async-resources.md.

Risk of addition: medium (bounded compatible public API); whole feature retains
previous high-risk compatibility review. Apply general, architecture, scope and
risk/compatibility lanes to addition and history conclusions. Retained reviewer0
is independent read_only gpt-6.1-sol/xhigh, no overrides. Read the mandatory
review skill and all selected references. No nested agents, source edits, long
integration/browser run, publication/merge/release/deploy or lifecycle action.

Non-goals: internal-wide rename, a wrapper/subclass, removal/deprecation of Client,
changed runtime name, extra runtime or entrypoint, WebUI adoption, npm release.
Final installed-tar focused loader/types proof remains after review; prior full
server/browser proof is bound to original source and is not relabeled. No
merge/readiness-for-use or release authorization is supplied by review.

## Committed receipt

Final head: `f5320eae05cbf8256a40cb04358be876ea7bde75`, author and
committer Jakub Skokan <jakub.skokan@havefun.cz>. Clean worktree observed by lead.
Delta from `76f190f`: exactly 8 paths / +69-14. Generated runtime delta one extra
`exports.CallbackClient = Client;` line; declaration entry re-export alias only.
Source typecheck/build, 26 compatibility and both type configs passed. Independent
owner1 ran callback.spec 12/12 and emitted callback consumer successfully; evidence
`/tmp/2026-10-19-haveapi-async-client-implementer1-verification.zpVPaN/callback-alias/`.
All three docs read and accepted by main agent under writing skill. Normal
hooks/pack exact receipt is supplied by owner0 inventory and accepted below.

Final metadata correction: owner rewrapped message only after the `3a440e5` checkpoint,
normal hooks reran clean. Lead verified `git diff 3a440e5 f5320eae` empty and
clean final tree. Final tree `34002c6f9feb965951d63cee71c34d18ff0eba83`. No
source changes and prior four commits untouched. Reviewer notified in real turn.

Final owner receipt read by lead: callback-alias/package-receipt.json and
final-hooks.log under owner0 evidence root. Normal HaveapiI18n + all message
hooks pass. TarSHA25623cad7163435c9d2cd51e83b9d6751db895ddbbfb3c586f1343f42f7070e9647,
55,425bytes,51files44d.ts; all packed files equal committed bytes. Pack owner
assertion plus artifact equality, no cryptographic build provenance.

## Final independent decision

Reviewer0 completed final review at f5320eae, verified native thread
01a154af-cc09-7422-bff8-fcc87e300be1, retained gpt-6.1-sol/xhigh/read_only,
no overrides. No Blocking, Important or Advisory findings in any of four lanes.
Independently ran compatibility26/26 and both generated type configs, verified
new tar hash/size/files/every packed byte. Minimal entry alias preserves one
constructor/value/instance type; docs and tests proportional.

Whole c14e7d3..f5320eae five-commit series accepted: new standalone naming
commit has useful separately revertible public purpose, no obsolete or
superseded implementation/history. Prior coherent source/output stages retained.
One unchanged dependency introduction, no repeated pin or generated-only stream.
NO MIGRATIONS in either repo; no new externally supported state boundary or
release/deployment. Metadata checkpoint3a440e5 confirmed same tree/parent.

Reviewer accepts focused installed-tar three-loader/both-type-consumer proof
as remaining verification for this additive one-export delta. Prior full
Ruby-server/minified Vite/three-engine/browser/CI results remain bound to
76f190f and tested WebUI revisions; do not relabel as f5320eae runs. Node
minimum remains a release prerequisite; no merge/release/deployment approval.
