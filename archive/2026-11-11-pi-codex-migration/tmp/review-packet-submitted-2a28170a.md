# Pi integration review packet

## Current verification target: corrected public Pi Solo successor

**Selected source and seven narrow corrections accepted; existing fe1 CI handoff pending.**
D `df991058776aec0553fdb8140131bc13df3300c5` replaces the selected public-feature
commit while retaining exact reviewed e092 ancestry and unchanged C5aa. Actual
independent reviewer0 all-four-HIGH-lane review and complete D46/C2 history,
repeated-stream and migration report remain scoped to d441/C5aa; no new findings,
H1 resolved. Lead directly verified the five-path74 correction under b3466a9e,
the [one-token b0 correction](review-final-schema12.md#asset-token-correction-direct-narrow-fix-disposition),
the [test-fixture d811 correction](review-final-schema12.md#node-fixture-correction-direct-narrow-fix-disposition),
the [runtime-wait17b correction](review-final-schema12.md#runtime-wait-fixture-correction-direct-narrow-fix-disposition),
the [catalog-mode75c8 restoration](review-final-schema12.md#catalog-mode-restoration-direct-narrow-fix-disposition),
the [Plan fixture fe1 precondition](review-final-schema12.md#codex-plan-fixture-precondition-direct-narrow-fix-disposition),
and [preflight termination df99 fixture](review-final-schema12.md#native-preflight-termination-fixture-direct-narrow-fix-disposition)
under mandatory-change-review steps9–10. Repairs preserve the reviewed contract,
including its existing read-only catalog guard; no public/interface/format/
authority/design boundary is added. No new independent-review turn is required.
Do not call df99 independently re-reviewed or equal-source to d441/74/b0/d811/17b/75c8/fe1.
Unaffected review conclusions remain; the final new-head/history/input proof is below.
Risk remains HIGH for the public/persistence/transition feature. This packet-only
reconciliation invokes neither reviewer nor long verification/publication.

| Current target | Exact identity / scope |
| --- | --- |
| D base | `eabb56a278bd8eb1759041467eaebfa6392ddcb2` |
| D final head | `df991058776aec0553fdb8140131bc13df3300c5` |
| D final tree | `5bf7ea9cb540ae007fabaf481ff6eb6d6bdf6805` |
| Prior Plan-corrected source | `fe1d190a4af417b72d028c195e8d0f06f1349bd8`, tree `14abbd4bb66a87e9f77f34d0574463942ecf7510`; existing CI terminal/effect handoff pending |
| Immutable direct preflight fix / history-equivalent source | `b1900fe0aa2cf132a40fc5a20a17c511ce0f202c`, ref `2026-11-11-pi-codex-migration-public-pi-preflight-count-direct-fix`; equal df99 tree only |
| Prior package-corrected source | `75c8b6fa896dce83e5d731cdf35367cccf581c5e`, tree `bd1f592132ed2a39811a18b5bdb03583ecb25dac`; mixed CI results retained |
| Immutable direct Plan fix / history-equivalent source | `e560ae88a27cb44c3a121d0e2d415db5ae0a0c48`, ref `2026-11-11-pi-codex-migration-public-pi-plan-precondition-direct-fix`; equal fe1 tree only |
| Prior wait-corrected source | `17b16cc834d218c69b18cebd74cf8c31f5416a3c`, tree `6a477db0f763808c574bcd95b281f7f02bb7fea3`; mixed CI results retained |
| Immutable direct package fix / history-equivalent source | `35e2f967c78c6d493edd302ca33e278dc88cca1f`, ref `2026-11-11-pi-codex-migration-public-pi-package-guard-direct-fix`; equal75c8 tree only |
| Prior Node-corrected source | `d811f429c6ae67299b00db89152e303692bb7bc5`, tree `87de5da3eac82affb68b8c02f7b85fa9194f04a3`; mixed CI results retained |
| Immutable direct wait fix / history-equivalent source | `1a4eb2b67dd5d7b4fc928aa67b60507938441c94`, ref `2026-11-11-pi-codex-migration-public-pi-runtime-wait-direct-fix`; equal17b tree only |
| Prior asset-corrected source | `b0d1114ea37bbc5f23299579d25c5019fb54e890`, tree `c9c3ad4fa5f27f7419269cb823d36a12f028457b`; published branch/failed CI retained |
| Immutable direct Node fix / history-equivalent source | `33f14f7abd0bd4e86e8e162bf04e929b76452664`, ref `2026-11-11-pi-codex-migration-public-pi-node-direct-fix`; equal d811 tree only |
| Prior narrow-corrected source | `74c3fa9071be86d64677326500b0469e2495fd91`, tree `e107788d9f6a2f53e084e6ce9b38ef5fa15d5b6e`; original feature/CI receipts preserved |
| Immutable direct asset fix / history-equivalent source | `df09bc36646119dc7b529682bb87fdee81032ded`, ref `2026-11-11-pi-codex-migration-public-pi-asset-direct-fix`; equal b0 tree only |
| Actual independently reviewed public source | `d441155f6321979978a275b198e62b5b724cdaff`, tree `1107f00db3fe05f8aaf2f068d49c72f4356adb58`; original published branch preserved |
| Immutable direct correction / history-equivalent source | `e3b38484a93dd5941cd3eb054bb18785948a1b9d`, ref `2026-11-11-pi-codex-migration-public-pi-ci-direct-fix`; tree equals74 only |
| D immediate parent / reviewed predecessor | `e0925346dae8e862df518b3fecc6e857561c1000`, tree `7a82528eeabe43423ef08219f71508b5413e3e39` |
| D complete series | 46 logical commits; existing45 unchanged plus one atomic public Pi feature |
| C unchanged base..head | `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`..`5aa6111db1a71b17191befb8532bad7dcae2e15d`; two commits, tree `ca190011bdc2da235a0e6ffc7a8209e78bb5f55d` |
| Selected isolated worktree / branch | `worktrees/2026-11-11-pi-codex-migration/dev-workspace-public-pi-preflight-count-fix` / `2026-11-11-pi-codex-migration-public-pi-preflight-count-fix` |
| Source/fix owner | implementer2; implementer5 owns only this packet, lead owns state/acceptance/review invocation |

[Original reviewed public source receipt](tmp/public-pi-solo-commit-receipt.json), SHA256
`aa5aed54a60fc11f792e8e28242e0c134988cdf1b57a9bae58da2d66a450284f`, binds the
original d441 35-path delta (1921 additions/143 deletions), its1009 final5/archive/current source
hashes, three approved docs, fixture bytes and joined effects. Lead independently
verified those identities; this packet does not repeat a source inventory/check.
[Owner2's complete source/check handoff](p2central-workflow-evidence.md#public-pi-solo-join-public-preparation-successor-sourcecheck-handoff)
contains the exact inventory, commands, graphs, failures and correction note.
Receipt patchSHA `4f0a3b536132c66934bda810f166906ba41fa70de85ac4129c0250457c8f743a`
labels `git diff --binary`; the independently computed
`git diff --full-index --binary` patch SHA256 is
`17cfb2ea217abf0c21715175abbbfc5503ff06b5046c40bd3d5e9e6cd5321144`.
These are distinct argv encodings of the original d441 delta; its immutable receipt
was not edited to make the hashes agree. Current correction receipt3bee and both
reviewed snapshots remain intact. [Submitted f90 snapshot](tmp/review-packet-submitted-f90ed6da.md),
SHA256 `f90ed6da7e2ffed7558aa375a45a440e0abb1c234b72e4e174f30a98de36b8f3`,
was saved byte-for-byte before its correction update. The accepted74 packet is
now preserved at [submitted c824](tmp/review-packet-submitted-c824e9a1.md), SHA256
`c824e9a177f89b498b6960fbd23e22b0f09b3d8295ad07465dc3fb2cc7f85bcf`, before
that asset update. [Submitted14bf snapshot](tmp/review-packet-submitted-14bf47dc.md),
SHA256 `14bf47dcd375da86e2cf818143e07e74a1ab6971a6cebd970205bb0359392da6`,
was saved byte-for-byte before the Node update. The accepted Node packet is now
[submitted3539](tmp/review-packet-submitted-353900f4.md), SHA256
`353900f4ab8cded31ff9b0af77bfa52489c18a8854f531c5edbac12c9604aa6d`, preserved
byte-for-byte before the wait-fixture update. The accepted wait packet is now
[submitted1cc7](tmp/review-packet-submitted-1cc78675.md), SHA256
`1cc78675b2d840e633d221278b2500bd4a74d4a94fd12538d1742cda2787fe18`, preserved
byte-for-byte before the mode-restoration update. The accepted mode packet is
[submitted ef3d](tmp/review-packet-submitted-ef3dde9a.md), SHA256
`ef3dde9a0c0b1cb9ae7768233c1a9387a2edd6d3ca4a55b6189b8a86230c9ccb`, preserved
byte-for-byte before the Plan-fixture update. The accepted Plan packet is now
[submitted1fac](tmp/review-packet-submitted-1fac94df.md), SHA256
`1fac94df512ba10b775bd432febf97d0b77dab56467b69087928de7a04efd55b`, preserved
byte-for-byte before this preflight-fixture update. Original snapshots/receipts
remain unchanged; no new source inventory/check is repeated.

### Added feature, format and compatibility inventory

The public authenticated/origin-checked form and POST /sessions now join the
existing request-ID preparation/status/retry path for explicitly selected installed
Solo Pi. Codex remains the default; omitted/explicit Codex preserves its old wire
bytes/digests, naming, uploads and provider behavior. Pi requires an explicit custom
name, nonempty text, supported explicit model/thinking and no attachments/upload
scope or contradictory Codex-provider fields. Name-only Pi without the request-ID
protocol refuses with400; no second endpoint or creation protocol is introduced.
Sanitized browser summaries are local composition facts, not entitlement proof.

Pi freezes the exact raw catalog digest, whole package Default, installed preset
and literal role, primary settings/Goal, original request/receipt/attempt/time and
later actual reserved identities. The Pi provider staleness token binds catalog
and complete Default; it is not authority or a label-based credential resolver.
Provider/account/fallback intent stay fixed; only permitted primary model/thinking
are chosen. Frozen configuration/preset drift holds original intent. Original root
receipt takes precedence; immutable Pi replay lookup precedes fresh availability.
Accepted/Unknown/native-started recovery stays original Lookup-only/no replacement
Send. No current catalog/default is substituted into an old accepted request.

Persisted changes are Pi-only preparation schema2/inputVersion2 and Pi draft
schema4. Pi input binds backend=pi and piProviderDigest; its frozen snapshot binds
catalog/Default and the saved preset/role. Compact terminal mappings retain schema,
input version/digest and original IDs after Snapshot/Handoff retirement. Browser
Codex drafts stay schema3, old schema2/3/schema-less text keeps Codex meaning;
existing attempted IDs/body bytes are not rebuilt. Pi draft4 freezes exactly one
backend=pi with token/model/thinking; old browsers refuse it. Backend changes occur
only while editable; delayed Codex responses must match backend/selection epoch.
Locked form/status/identical-POST recovery and uncertainty stay intact. Pi upload
allocation is unmounted, not silently discarded or converted.

The owning strict reader/traversal covers BOTH session-preparations and
session-preparation-mappings, compact/terminal records in either store, orphan
identities, exact workspace/portal binding, privacy, duplicate and aggregate
budgets. Zero-root checks still inspect empty team namespaces and preparation
orphans without feeding fake roots to nonempty native inspectors. Pre-root output
is schema2 only for Pi preparation refs; legacy schema1 output is unchanged.
Metadata `piPreparationSchema:2` joins the complete creation/workflow/role bundle
only with its reader/guard. Target checks run before effects with existing
transition SH/EX ordering and post-wait/activation rechecks; refs confer no native
ready authority. No new runtime writer/Host/Dial/transport/constructor is added.

The actual archived e092 reader accepts unchanged Codex JSON/digests and refuses
both new Pi unfinished and compact arms. Compatibility proof is three selected
nonzero cases on compat1, not a new-runtime/whole-latest-writer proof. There is no
DB migration, converter, record stripping, forced rollback or Codex-to-Pi rewrite.
Preserve records and use a compatible newer reader. The new public arm has no
known released/deployed/external consumption in this package; unknown external
use stays unknown. Earlier runtime1→2/communication1→2 transformations, Pi4
original receipt/creation fences, optional retained2 Instructions and all prior
rollback/old-reader obligations in the preserved packet remain part of D46.

Original d441 35-path owning groups: public form/POST/projection, browser scripts/templates and
existing web fixtures; strict preparation store/compatibility fixture; command
inventory + Ruby host/backend guard + typed preparation decoder and metadata;
one SDK test, three existing VM fixtures; three maintained docs. Exact paths and
hashes are in the accepted receipt, not duplicated here. Public enablement,
owning reader/target fence and final scalar are one inseparable logical commit:
enablement must not precede its compatibility fence. Tests/docs/VM source support
that same public feature. No ancestor rewrite, fixup/correction stream or second
C dependency stream was introduced. C5aa and all five pin files remain unchanged;
whole flake.lock SHA256 is
`358e08b3b35cb6dede0ed0b9e9981e5c80967b84b7d695b4e21a77d289531621`.
The single selected C pin remains existing dependency commit5 below.

### Complete final ordered histories

This is the full eabb..df99 series:336 files,52319 additions/484 deletions.
Rows1–45 keep exact prior SHAs/order and reviewed H1 dispositions. Final row46
is ONE owning public feature (e092..df99:41 files,2137 additions/182 deletions),
with its correction folded into that owner, not a later obsolete fix step. Whole-series scope includes every persisted
format/update stream, the historical aliases and the old53→45 mapping preserved
below; prior review does not exempt the successor from an explicit D46/C2 history
and migration conclusion for the actual reviewed d441 range; lead directly
verifies the narrow final-head disposition without another independent review.

| Final # | Full final commit | Owning feature / source disposition |
| --- | --- | --- |
| 1 | `bfe228e1b32c9c7730b86d696df93ed5ac5581b7` | source1 `1cd30a5577718edca374307fe117bf7def013e32` pi: add finite worker conformance probes; source52 pi-runtime/README.md |
| 2 | `ac3318a716e0feb1ede61dd4c17ecbffb36994ad` | source2 `cf432ce5fb1018e54f917629bad233f082f5121d` session: add strict Pi backend identity readers |
| 3 | `e1f4c3d3865203e47e6208d8e8c3c5b3645c8979` | source3 `f920afaf9fdee6c9f2935706e83d7eae9554c7f4` pi: probe tagged custom input persistence |
| 4 | `3678354a7abf83678fd309ee25f4296f566cac37` | source4 `a0b898e4dbde142b0dd19148909c670ec187a9ce` pi: add host-managed session launcher |
| 5 | `314314c6b5785ddac9601947e8173501430cc3c0` | source5 `34929b6523285b8eff08dfff639e58e07213192a` deps: select the neutral conversation and question client; source48 flake.nix, flake.lock, portal/go.mod, portal/go.sum, nix/workspace-portal.nix |
| 6 | `56f71899381ef87a6dba40579f867d93f26ef3bd` | source6 `30941eaa1ad45f2b8f988b077b78c059fe135945` portal: establish unknown steer before grace recovery |
| 7 | `cc44e6094d1a66628b0e1289c8207f0a666c9584` | source7 `39a7b2ce3b3b7a6408c1e39a8c5cc51e6e7c4052` session: fence legacy writers from Pi backend state |
| 8 | `32e9e7ee6d93bbc11e40ceda0418a62f224a099e` | source8 `cdb11d5aa44d96ca3bb7342527373edb48abce1b` pi: add SDK worker and native acceptance receipt core |
| 9 | `2cf1e85225db90e435fa1da6790e332ce1c03698` | source9 `432b6acb5dfabce9f50cbaea5a276d0ea3f31ef6` pi: add provider policy and member settings coordination |
| 10 | `3ef02759a8b831650ee0d4f6ea904f74d1287610` | source10 `be88189c5b114b4e49bae9160caf1253184b2db7` pi: add typed team policy and inert reporting tools |
| 11 | `54c430f7e94d6055fc8298d4ff81b0f1bbf82c0f` | source11 `5cae9ea31c75c09cc9766719f20925b9196da47c` pi: retain optional question and Plan intent |
| 12 | `eb5782cb66e2419d9bd65aad23232658650151e0` | source12 `2165dff18e47674adb97fdc2c8140f7fcd6b7af6` pi: add scoped first-launch supervisor and controller |
| 13 | `0f2f6c3db36b08cb53bf4f9df4183cd1dd2629b6` | source13 `4385e1989eae53029334b302a8966be8fd12e478` pi: project canonical accounts for provider switches |
| 14 | `b14f45ba4adf819559b78c2586feaec50d1f5ba2` | source14 `4d500eb8caa959c5daef3fd47a1d70868939bbba` session: publish Pi creation authority with retained proof; source52 portal/internal/agentbackend/README.md |
| 15 | `aaa241e363bdec1a82f1c2cb112680f682282871` | source15 `37ae7bd8ccbc5607b611532e959ea08665833609` pi: add admitted team records and utility domain boundaries; source53 all owned hunks |
| 16 | `f2edcc2cf4c044123d91f3c413abeb05f31fd04d` | source16 `10a1c460e19838836d57c0735960832ca22ff642` pi: load explicit provider policy from installed packages |
| 17 | `aab4102613b1c00e63e97f5dd5b03105a04dc151` | source17 `a2a2693ec23499a78b25117920e8f2a978f42889` portal: validate immutable Pi provider configuration |
| 18 | `809b0c94d73d747e95d21426c49d8108ec9b7938` | source18 `79f5c059544f1e2e6075dbe05e4789d85af858a6` pi: define native routing evidence data contracts |
| 19 | `d3532ad61de3143b0f71e999dee138c4143af4f5` | source19 `9799127dc26d431f05c0d6a3d2589fb031546832` pi: compile native retry policy and decide bounded next hops |
| 20 | `68189c19c10d547de1b6efd62e6166aa5e9ad57f` | source20 `c3b1d25fc7726faaf9be392843611557e904d380` pi: package the SDK worker and provider configuration; source52 README.md |
| 21 | `1758ed3e9f074145a6f19e76012e1c2b0c4230c3` | source21 `a0c916235433035390029a70abcef6c2d992b2ce` pi: verify durable callbacks and tagged runtime records; source50 nix/tests/pi-worker.nix |
| 22 | `83284a22364d1affa72dff7f99474fbb30c45741` | source22 `ff53ba77730df5905b3c727c2e9ce5121b096a81` portal: compose Pi creation with the real runtime manager |
| 23 | `b911181a965f9eb4f6b7a2123a91b2480a24712b` | source23 `6451c11cbe7a40c9ac1936f87f0c30a10b7f19cc` pi: connect monitor utilities to the typed runtime API |
| 24 | `2d956fbc393ce3ed21085b4b6142aeada4dd7061` | source24 `4dc8819ea8ce934f9fabe27cf9b3672038e3de5f` pi: enforce explicit tool policies through the SDK |
| 25 | `38f09b1c1f96f1030cd02caec179f4a53706db9d` | source25 `dd4d1a9bfe2ab4ba08eb3ffaf04c1f265fe8eff2` pi: expose retained utility obligations for package preflight |
| 26 | `33a5cbccc6e04f7fbd4df12f311b382d89b85624` | source26 `880c8efdb37ba1940806ac95ac1b24e04092f907` pi: bind Plan and question actions to retained proof |
| 27 | `625b2838b10176f4820dc865c2ba1eef3b144835` | source27 `4361b0f1a80643de075fddd02de4887bb37f8cf2` communication: expose pure retained-record validation |
| 28 | `a1f27462da1c6b849502b7584823d4cfce39d787` | source28 `e25312258c1033711f43fc0ed008ffa91430ae6d` pi: share utility execution and enforce retained tool policy |
| 29 | `f9ebbe9722e7f78ff73cb9a782507f81f1479df8` | source29 `7d314da68c13f80d087e551ed2101778641d98ba` pi: prove native question and Plan receipt recovery |
| 30 | `9b14fbde3cafa50d5ff57038bd617fb0391ea6fb` | source30 `b2d71adcdd4f9ff5fdc342dd97ff1a06587c150c` portal: fence retained Pi team records during package transitions; source49 all owned hunks; source50 portal/cmd/workspace-portal/maintenance_startup_test.go, portal/cmd/workspace-portal/pi_team_preflight_test.go |
| 31 | `f2ca90f6e8f567611f6b7b15a9dba07a5fff7b4c` | source31 `450ad1164e98b68022e9a225bb804ed6b2a37f81` pi: add bounded public SDK native retry component |
| 32 | `f536b6ea968aac59730d07f196de6a802c8f9890` | source32 `87ff7d3bf0bfe39848234b56dd9930c73d323ec2` pi-runtime: retain explicit drained supervisor successors |
| 33 | `57afcaab41dfe6ad679071a9ae2f3f98e4b91e58` | source33 `9f1be5b0d4ba265dfcb966b26439315120525411` portal: project and render retained Pi workflows |
| 34 | `734f8382f3fc2e6b0d07680838ae90755adb5505` | source34 `ad707ed03f2bb832932ea410d84436f597c2f05f` portal: admit retained Pi team record operations |
| 35 | `86b37ad3977bf04f5e5ff9aac238baceba282834` | source35 `47bc2d9987db919104be5c68c7a8d064285d036e` pi-runtime: gate workflow observations with attachment barriers |
| 36 | `1a065cac169f83ffad834e0d059f1a1420062598` | source36 `fc308d34bc0c4414d2c3214ff5311cb0f4762cd9` pi: guard retained question plan and tool-policy records; root7f product/helper/refusal hunks |
| 37 | `f3904b7fd19756e9a6a69a10c0580d1b2750a22f` | source37 `253c5d3e42f3a75cb93d263967ba143de5552add` pi: expose checked submissions and retained runtime identity |
| 38 | `b8c7fc4228d30c1d429bc13f0cf815ab0d2680fa` | source38 `74d3ba8dc0f78ce4a7d1e2a4f62e60ab1a823952` session: decode complete Pi native routing metadata |
| 39 | `ded942c688d436467d6fabe934f534f9e0d2fdfc` | source39 `ad21d6b6d8d19580a87df2dc75d122e5296dc05e` portal: compose Pi question and Plan workflows; source51 all owned hunks |
| 40 | `3433999001511a8aefa6eb38d60475886ccd7345` | source40 `59db5bec1fe1c39f9b689f7ba7369f4055e307e9` session: publish the retained Pi workflow contract |
| 41 | `1abfd2a1f446010129caab296972055f89b52c8f` | source41 `509ca3dca6f90184a8ce9d8b0344846e3584b885` session: decode retained role instruction support |
| 42 | `613bdd705cc7f57d68609734358c1b87e049447d` | source42 `d94ff0f8b6965f69cbb0e661f34aa461d6ef8cb2` pi-runtime: retain and verify literal role instructions; source44 all owned hunks |
| 43 | `5e79de8c7fa5ee6af0277c9176c9b34f17056841` | source43 `f3b426ec5c9435ea08e8a55b85c000f2d8de8d9e` session: guard retained role instruction mappings; root7f role-dependent writer/CLI tests |
| 44 | `20c3f712556448dbe1c0a744e98490b1cb6bb593` | source45 `be12c6783ecb432d86ade6c3ac7a52bb899d05c0` portal: refuse unsupported Pi creation rosters; source46 all owned hunks; source47 all owned hunks |
| 45 | `e0925346dae8e862df518b3fecc6e857561c1000` | source48 `a936d9e92d666fb5fc242e57583f34c465bd0211` portal: align Pi transcript cursors and presentation; source48 C pin excluded here: folded once into final5 |
| 46 | `df991058776aec0553fdb8140131bc13df3300c5` | portal: add explicit Pi Solo session preparation; d441 + narrow74/b0/d811/17b/75c8/fe1 + TERM-handler fixture ordering folded once; all direct refs including b190 retained |

C's complete unchanged dd90..5aa series remains:

1. `462df77a3012395da737faaec44fd9ca10fcbfc1` — neutral adaptation with final
   constructor-specific opaque cursor contract/docs/tests folded into introduction.
2. `5aa6111db1a71b17191befb8532bad7dcae2e15d` — optional question-card presentation.

H1 was independently resolved on D45/C2 by reviewer0 eb1ec18b; source behavior81
conclusions are retained. [Final review record](review-final-schema12.md#h1-closure-and-exact-final-source-review)
and original reviewed packet `/tmp/pi-schema12-candidate.wwMbgc/h1/review-packet-reviewed-1f2da9ef.md`
(SHA256 `1f2da9efd0e0d961f7bb2b43c0d91a832d936c4ae6425d21909c89bff0bfada5`)
remain intact. Reviewer0 completed the d441 all-four-lane/D46/C2 report with no new findings;
main retains those conclusions while directly verifying the narrow74, b0, d811
17b,75c8, fe1 and df99 deltas. Independent review remains on the actual d441 range.
Existing e092 review/source evidence below is historical by scope;
its pending H1/CI wording describes its own submission time, not current status.

### Cheap evidence, graph reuse, failures and effects

Existing manifests bind actual inputs; final5's successful1009-file identity is
not equality with every earlier executed graph. No broad SDK/source rerun follows.
Links: [compat1](tmp/public-pi-solo-compat1-inputs.json),
[browser1](tmp/public-pi-solo-browser1-inputs.json),
[SDK1](tmp/public-pi-solo-sdk1-inputs.json),
[final2](tmp/public-pi-solo-final2-inputs.json),
[final3](tmp/public-pi-solo-final3-inputs.json),
[final4](tmp/public-pi-solo-final4-inputs.json),
[final5](tmp/public-pi-solo-final5-inputs.json),
[final tail log](tmp/public-pi-solo-final5.log).

| Actual graph / scope | Evidence and limit |
| --- | --- |
| compat1 /60b04137,1009 files | Exact e092 reader, sibling baseline fixture and three stored inputs pass in43s; original924c upload cases unchanged/not rerun. New Pi unfinished/compact refuse; no latest-writer/closure equality. |
| browser1 /f7a58976,1009 files | Existing settings and Pi form browser parents pass23.94s/3.36s (package27.362s). Scripts/templates/fixture unchanged; controlled failed POST proves locking/recovery, not production acceptance. |
| SDK1 /c48cbb85,1010 files | One actual Pi1.5.2 builtin Responses case passes901.669ms/TAP2503.718ms,1pass0skip; synthetic stored auth and owned loopback models, normal createSession(sdk,config), no third-argument Runtime/Host/Dial/provider injection. Literal role/system/Goal/original Accepted witness and terminal text; unfinished SSE is execution error while input stays Accepted. |
| final2 /8076f557 | Session2 parents .066s, command8 parents3.204s including actual Ruby scanner1/83; web5 parents pass before real Codex400/409 regression; later tail unrun. Corrected HTTP parent .823s. |
| final3 /b11a67a9 | Remaining47 web parents:25 parents+24 subcases pass; stale asset literal fails, exit1/26.621s. Corrected page/index .076/.070s; later tail unrun. |
| final4 /da594ec9 | Remaining20 parents:17 pass then stale label/span adjacency fails, exit1/23s. Exact corrected preset parent .073s; later tail unrun. |
| final5 /03400791,1009 files | Only two remaining Go parents .363s; Node31; backend Ruby3/78 and host5/40; five Node syntax and diff check. Exit0/real23.72s, tool15431 joined. |

The final2→3 production correction restores early Codex provider validation/400
while preserving Pi replay before fresh availability; VM source inspects BOTH
dirs after ready and orders Pi after all18 Codex arms. Final3→4 changes only three
expected asset URLs5→6; final4→5 only two expected label-span literals. The selected
legacy model/effort and original assertions remain. Within the original d441 feature no production byte changed after final3; the
later74 Ruby Hash guard is the separately identified narrow correction. Compilation/exercised final3/final5 paths and scanner paths have
separate bindings. Session template has only app70→71 for actual shared handlers;
index app71, and historically retained automatic-archival app70. The accepted
b0 token correction below now makes all three consumers app71, superseding that
earlier recommendation. Preparation/creation assets6 and original assertions stay.
Malformed name-only Pi test changes expected status to400 without weakening its
no-receipt/no-Codex/nil-adapter assertions; optional naming changes are truthful.

SDK1 receipt correction: immutable aa5 receipt lists15 final-source differences;
actual union is16 because SDK-only generated
`test/__pycache__/creation_model.cpython-313.pyc` is absent from final Git source.
Keep aa5 and the1010-file manifest unchanged. Owner2's saved correction establishes
the recorded Node test spawns Python3.13.15 with the absolute creation_model.py
script directly (not a module-import invocation). No cache-read trace was collected;
pyc consumption remains UNKNOWN. Do not call it unused. SDK proof retains its
actual1010 inputs. Actual unchanged SDK/package-api/creation_model.py evidence
is component proof, not new final application/VM or builtin TLS readiness.

Failures remain in the existing evidence: expected backend RED, Ruby shard missing
TransitionHost, missing bytes import, Nix embedded-Python quoting, redundant fixture
import, original SDK utility wrong-cwd prelaunch stop, final2 optional-print
misread, final3 invented rolling-hash preflight (no test), and final4 absent
/bin/bash launcher before execution. Same unlaunched operations were corrected
without erasing failures or duplicating successful runs. **Final3 CLI resume used
unapproved Astra/xhigh: explicit parent policy deviation, not compliant watcher
launch/fallback.** Its actual technical failure remains scoped evidence; no later
successful graph erases it. Fresh final4 Luna/low launch/settings were verified
before source execution. No roster change is implied.

Receipt/evidence account all known effects: SDK53019/parent69652, compat82188,
browser55514, final2 parents19748/43273/tool50278, final3 parents69224/80542/
tool70100/cell4, final4 readiness11686/launcher53588/executing24542 and direct
27781/68468/52320/41575/15431 plus commit89596 are terminal/joined. No surviving
process or uncertain command effect is reported. Ordinary Nix/tempfile-F commit,
no declared hook framework/active hooks or bypass. No application command is run
by this packet-only work.

### CI-RUBY correction, checked inputs and main narrow-fix disposition

[Accepted immutable correction receipt](tmp/public-pi-ci-fix-commit-receipt.json),
SHA256 `3bee044b5feebe5776e467b370d02b3437ebd80d2d9f42611bce30af33e6d954`,
and [owner2's complete CI correction evidence](p2central-workflow-evidence.md#ci-ruby-fix-checked-correction-and-consolidated-successor)
bind exact d441→74 source difference: five paths,77 additions/17 deletions.
Lead independently checked all five blobs/filtered Ruby bytes and every1009
archive/current/checked-manifest source hash. The manifest is
[2072456a](tmp/public-pi-ci-fix-inputs.json), file SHA256
`2072456ad67ed64822a6fb2a4938b6e02f333e6d6578eb1b3ff65427bf62907a`.
This packet uses those accepted receipts rather than querying source again.

| Changed path | Narrow purpose / preserved boundary |
| --- | --- |
| libexec/workspace-session-backends.rb | Require Hash immediately after strict JSON.parse, before schema indexing; reuse existing owning Error. All exact/schema1/schema2/identity/session/creation checks remain. |
| test/workspace_session_backends_test.rb | Extend malformed-result fixture with array/booleans/number/string; retain null/duplicate/malformed and positive schema cases. |
| test/support/workspace_host_test_case.rb | Opt-in empty_pi_state_root process helper; original global default heredoc unchanged. |
| test/workspace_host/profile_transition_test.rb | Only two restoration instance joins/marker checks and existing zero-root process test. |
| test/workspace_host/agent_team_registration_test.rb | Only no-workspace reconciliation fixture construction/environment/marker. |

No rescue/coercion/empty fallback, missing-reader exception, new Error text,
public API/schema/metadata/authority, converter or production-host bypass is
added. Existing product readers remain strict. The helper is explicitly opt-in:
actual RbConfig.ruby child, exact pi-team-preflight/--state-root/bound-state argv,
Lstat absence for seven domain roots plus WHOLE portal; only ENOENT is absence.
Present/symlink/error/other argv refuses before marker or empty schema1 output.
It proves a bounded no-state process double, not actual Go inventory. Original
Open3/deadline/output/join, three instance-local joins, restoration errors/profile/
identity/sync effects and registration assertions remain. No global helper
replacement or product preflight skip is introduced.

Direct e3b38484 (parentd441) and consolidated74 (parent exact e092) have identical
treee107788d and empty direct..final diff. Their same-base
`git diff --binary e092..head` patches equal SHA256
`0dd05a9848349e4eabe03b9fc451f90256e29117482c8a9c4ff905399e764a4b`.
Only this direct→consolidated step is history-only equality. d441→74 is a REAL
source difference, binary patch SHA256
`c0131b2edece2ada876e14930f73ac9fd37eb5e3ec11c1f1e4d3066e7751ec44`.
[Whole old/new46 range disposition](tmp/public-pi-ci-fix-whole-range-diff.txt),
[feature range](tmp/public-pi-ci-fix-old-new-range-diff.txt) and
[direct/final range](tmp/public-pi-ci-fix-direct-final-range-diff.txt) preserve all
aliases. Prior45/C2, the single early selected C pin, full lock, approved docs,
Go/SDK/browser/metadata/protocol and VM source are unchanged. No obsolete pin,
correction/migration stream or rewritten published ancestor remains in final46.

Focused actual formerly failing4 parents pass38 assertions/.546737s; another7
bounded schema/transport/zero-root parents pass97 assertions/1.290023s, both
zero failures/errors/skips. Mandatory exact
`nix build --no-link --print-build-logs .#checks.x86_64-linux.ruby-workspace_host-0`
ran ONCE: exit0/real91.70s, tests87.646481s,317 runs/4908 assertions/0 failures/
0 errors/3 existing tmux skips. Complete unique coverage discovered=selected=
executed317; no narrowed shard or extra skip. Existing skips are keeper adoption
and the two socket-cleanup opt-ins under declared DEV_SESSION_SKIP_REAL_TMUX_TESTS=1.
[Shard log](tmp/public-pi-ci-fix-shard.log) and receipt retain exact selectors,
timing coverage and all setup observations.

Actual checked derivation:
`/nix/store/p041pq1drgdln0ymmxpyyxmf1dwyxh2l-dev-workspace-workspace_host-0-of-1.drv`;
output `/nix/store/52g2c8dlmw85na3c9azv54835mnzkac3-dev-workspace-workspace_host-0-of-1`,
NAR `sha256-U9/7zEOkn5ZI9u7VZIt7HutWDaAmHEYxsiiG/3BNfH4=`.
Filtered Ruby input `/nix/store/h7f02qp8mj3im3rq7dq2nlv8d36cqj05-dev-workspace-ruby-source`,
NAR `sha256-+eR/4wUGePv00Bya9wyLKjWjkmpOCdgdh6Y9t3joeMA=`.
Post-fold evaluation returned the SAME checked drv/output, with identical five
checked file bytes. No unchanged shard rerun after the history-only fold.
This filter/check is not the full final Go/runtime/worker/application/VM closure;
no whole-app identity follows from the Ruby result or source equality.

Fresh Luna/low utility01a1d3cf-04f1-7b13-b812-56c2d90eae31 used installed f2d5 policy,
explicit danger-full-access/never and verified initial/resume headers. Source80611,
parent71110 and readiness31578 are terminal/joined; no self-wait/survivor. Source
commit28855, fold68001, post-fold49965 and other listed tools are joined. Existing
metadata envelope/eval/SQLite-cache observations are retained; no source/build
retry erased them. No Go/runtime/SDK/browser/VM repetition accompanies this fix.
Source owner2's window is closed; ordinary Nix/tempfile-F/hooks preserved.

### Published d441 failure and remaining corrected-feature verification

Actual published [Check43381235087/attempt1](https://github.com/aither64/dev-workspace/actions/runs/43381235087)
failed all three fast/archive/creation jobs on the SAME Ruby prerequisite:
317 runs/4865 assertions/3 failures/1 error/3 existing skips, BEFORE either guest.
The null shape/schema ordering defect and three missing reader fixtures caused
that failure. Archive11, original creation18 plus new Pi19 are UNRUN there;
no public/Node TLS/cold attach/target/role/Accepted or new-package success follows.
The accepted317-green local correction is not a new CI result. Raw failures stay
in [original transcript evidence](review-transcript-evidence.md#automatic-check43381235087-terminal-dependency-failure).

Accepted failure-handoff7b4845c3 and native-accounting2cb64ecc distinguish the
raw utility INCOMPLETE self-observation from authoritative remote failure.
The utility finished naturally:132 calls/132 paired outputs, one source observer
joined exit1, parent joined0, normal task_complete and exact PID absence resolve
known effects independently. Raw report remains INCOMPLETE; conditional SIGINT
was UNUSED, no signal/retry/replacement/lifecycle action occurred. No guest
started, so no invented teardown or VM proof is added.

The original d441 all-four-lane and complete D46/C2 report is preserved verbatim
in the final review record/f90 snapshot. Main b3466a9e directly accepts the narrow
source/check/history correction under mandatory steps9–10, retaining unaffected
review conclusions. This is not a new independent review on74 and does not call
74 equal-source to d441. Public preparation2/input2/browser4/old-reader refusal,
forward recovery, existing runtime/communication transformations and original
receipt/no-resend obligations remain as reviewed. No DB migration/converter,
record stripping, forced rollback or new supported boundary is introduced.

The subsequent normal new74 feature publication/automatic CI occurred and failed
at the asset prerequisite, as recorded below. The Ruby correction result does not
prove a final74 or b0 application/worker/VM closure or installed public Go+Pi/
builtin TLS/browser/target success. No force/default integration, duplicate local
VM or automatic reviewer turn follows. E092 CI/HOST3 roots remain baseline only; vb2 evaluation remains historical
source-only. Full TEAM/native3/custom gateway/real entitlement/integration/deploy
remain unfinished or excluded. Session stays open; no lifecycle action.

### One-token asset correction and exact full owning web result

[Accepted asset receipt](tmp/public-pi-asset-commit-receipt.json), SHA256
`13f6dd033bd28df413604936143757df7665a38a2a036eb978c3b7d64e7b8888`, and
[owner2's complete handoff](p2central-workflow-evidence.md#public-pi-asset-token-fix-full-owning-package-prerequisite-and-successor)
record ONLY74→b0 automatic-archival.html app70→71,1 addition/1 deletion.
Complete token-file checked/committed/current SHA256 is
`efe66ebc7445b93101d3ebe34763d8b17c050f61dcbf276985adcbc3eb40e106`.
Original owning asset assertion is unchanged; index/session/automatic-archival
all select71. This existing exact three-consumer contract supersedes the prior
archival70 design recommendation. No JS/DOM/copy/docs/test/assertion/pin/schema/
metadata/protocol/authority change, converter or migration. Token-only correction
needs no new product technical documentation. Approved docs/copy stay unchanged.

Lead independently verified the single replacement and all1008 unchanged paths
using accepted3bee/207 identity evidence. No new1009-file campaign or new whole
source hash scheme is claimed. Source owner2 froze the checked tree; ordinary
Nix tempfile-F/direct commit df09 and owning-feature fold preserve it. Directdf09
(parent74) and consolidatedb0 (parent e092) have equal treec9c3ad4f and equal
same-e092 `git diff --binary` patch SHA256
`350d47be34889ec3164fae7333603516a011755f530b3a2f387dc39cb47260bf`.
Direct..final diff is empty. Actual74→b0 is DIFFERENT, patch SHA256
`3e58e4111ac390716fad161782e6af893ca64a9a697bef99f387cb69fb1cf69d`;
74 is not a literal ancestor of foldedb0. Immutable direct/old74/d441/e3 and all
C refs/receipts remain. [Whole46 disposition](tmp/public-pi-asset-whole-range-diff.txt),
[old/new feature](tmp/public-pi-asset-old-new-range-diff.txt) and
[direct/final](tmp/public-pi-asset-direct-final-range-diff.txt) bind exact prior45
SHAs/order and one final owning feature. No obsolete fix/pin stream or ancestor
rewrite; C2/five pins/full lock/Go/SDK and original formats remain unchanged.

Exact existing owning test
`go test -mod=readonly ./internal/web -run '^TestBrowserAssetVersionsForRetryAndQuestionUI$' -count=1 -v`
passed test.02s/package.083s/real22.87s. Then the full owning package ran ONCE:
`go test -mod=readonly ./internal/web -count=1 -v -failfast`, declared cached Nix
shell, exit0/package308.869s/real313.64s. Raw result628 top-level PASS +829 nested
PASS,11 top-level SKIP,0FAIL. Utility815 nested count omitted14 deeper PASS lines;
raw utility report stays unchanged, parent corrected from raw indentation, no
retest. [Focus log](tmp/public-pi-asset-focus.log),
[full-web log](tmp/public-pi-asset-web.log) and
[raw watcher result](tmp/public-pi-asset-web-watcher-result.txt) retain exact outputs.

| Existing skipped test(s) | Actual opt-in reason |
| --- | --- |
| TestCPUFixture | CPU fixture opt-in; docs/cpu-benchmark.md |
| TestFirefoxTabs; TestFirefoxReadBudget | Separate Firefox/Geckodriver/display flags absent |
| TestNewSessionSettingsBrowser; TestNotificationsBrowser; TestQuestionBrowser; TestRetainedOpenInputBrowser; TestRetryBackendBrowser; TestPiNewSessionFormBrowser | PORTAL_BROWSER_TEST/Nix Playwright opt-in absent |
| TestIndexRefreshPreservesSelection | Browser environment absent |
| TestPiWorkflowExportNativeCatalogFixture | Only finite native composition exports typed fixture |

These are the receipt's11 named skips, not passing browser/native coverage.
Default-tag web completion is not opt-in browser/SDK/runtime/VM/installed proof.
No old Ruby/Go/SDK/VM repeated campaign was launched. The overrun inspection found
an active existing retry-idle test that later passed; no timeout change or signal.
Fresh Luna/low utility01a1d408-e77f-7982-aa0a-6d01efe54a00 used installed f2d5
policy/full_access/danger-full-access/never with initial/resume headers verified.
Source commands and terminal issued calls are bound by the raw transcript;
executing parent68644 and readiness60915 are joined, no self-wait/survivors.
The human result lacks a numeric source-tool ID: none is invented. Worktree91772,
focus27617, commit4298 and fold79615 are joined. No source/index/history window
remains open and no new authority follows from this packet.

### Corrected74 CI failure and next exact-b0 gate

Published [Check43391188642/attempt1](https://github.com/aither64/dev-workspace/actions/runs/43391188642),
event push/exact74, is authoritatively FAILED: all three fast/archive/creation
jobs fail the SAME original asset test before either guest. Ruby317/4908/
zero-failure-error/3existing skips passes; host job skipped as designed. Archive11
and original creation18+Pi19 remain UNRUN: no builtin TLS/trust/public Go+Pi/
role/Goal/Accepted/cold demandAttach/reconnect/followup/target or writable post-Pi
Codex result. Failed planned package/check outputs are not realized identities.
The b0 full-web green fixes the prerequisite but is not a new CI/VM outcome.

[Owner0's immutable failed-result handoff](review-transcript-evidence.md#corrected74-terminal-failed-result-handoff)
binds complete raw fast/archive/creation log hashes:
`494003dadb7747f6cd507db7b15cd1bf5c3227b5a555ffec41d5d5bf16d0e0bb`,
`3f8b3eed4417bc3dbdc61e1709bc958800100c1440413e79538321673e2a18af`,
`495bdccd616d5cb046517a8cc3719a38cf0f685d7f846f830de62b176b99343e`.
Failure-handoff SHA256
`9784761a81738c74d3c76644d6b6b0ebcfc8d8af5d3d605fb1cc43ad6c6ddf31`,
native-accounting SHA256
`b572a2c9678d8251a8fde97ea78f9a682f815d209f0d1471af218f090e6900a5`.
Raw utility FAILED, normal task_complete,29 calls/29 paired outputs/one observer,
source29192 joined1/parent72748 joined0 and positive PID absence close effects;
stillRunning empty. No self-wait/resume/signal/retry/cancel. Workflow952s and
observer869.353s are different clocks; neither reached30min. Historical d441 raw
INCOMPLETE and independent132-call resolution stay unchanged in their own record.

Lead's [asset direct narrow-fix disposition](review-final-schema12.md#asset-token-correction-direct-narrow-fix-disposition)
retains actual independent d441/C5aa all4HIGH+D46/C2 review, directly verifies
b346's five-path74 correction and this one-tokenb0 correction under mandatory
steps9–10. No new reviewer turn, no claim b0 independently re-reviewed or equal
source to74/d441. Existing strict public preparation reader/target bundle,
original receipts/no-resend, old-reader refusal, forward-only recovery and full
runtime/communication transformation lineage stay unchanged; no format/authority
or migration/repair boundary is added.

The later normal b0 asset-fix feature publication/automatic CI completed with
the Node prerequisite failure below. Its accepted outcome/effects are preserved;
that publication was not a final runtime/VM success. No force/default integration,
duplicate local VM, provider/deployment/profile/lifecycle/cleanup authority.
E092 package/HOST3/app2iv/worker80/18roots/1060 closure remains exact baseline;
vb2 VM evaluation remains historical source-only. No inherited b0 runtime/worker/
VM closure or public TLS/cold-reconnect/target acceptance. Full TEAM/native3/
custom gateway/real entitlement/integration/deploy remain unfinished or excluded.

### Actual-source Node fixture correction and exact combined check coverage

[Accepted immutable Node correction receipt](tmp/public-pi-node-commit-receipt.json),
SHA256 `6dd2960fbe2d307d7303a49356ae97aa06edd3b7102a3b01b0c09177c8613005`,
and [owner2's complete fixture/check handoff](p2central-workflow-evidence.md#public-pi-node-fix-fixture-context-correction-sourcecheck-handoff)
bind ONLY b0→d811 codex_providers_browser_test.cjs,19 additions/3 deletions,
SHA256 `eefa6ef370c0010bbdea673edb5373ef25409093abc90d22ce8083e76425325d`.
The fixture extracts four actual-source declarations using five unique ordered
anchors; its three real functions enclose the private WeakMap. Each fixture owns
fresh closure state and API/event contexts share the SAME returned functions/map.
Removing ONLY helper/context additions reconstructs all original19 fixture/test/
assertion bytes exactly. No new case, copied body, stub, product export, framework,
production JS/DOM/copy/docs/pin/format/protocol/authority change. The lead accepted
one-path proof reuses13f6/3bee/207 for unchanged1008; no new1009-file campaign.
Existing docs/copy/hash routing remains approved; fixture-only repair needs no
new product documentation.

Direct33f14f7a (parentb0) and consolidatedd811 (parent exacte092) have identical
tree87de5da3 and empty direct..final diff. Same-e092 `git diff --binary` patch
SHA256 `aa7330f09cfbb3765fe9ddc3d0ab7243ab5622070e8e0acccd9d75be15f767bf`
is equal for direct/final only. REAL b0→d811 differs by patch SHA256
`ae5cd5b2ce98606bcb892b6af000ccea1457e88f0284e5104ba094d31022513b`;
b0 is not a literal ancestor of folded d811 and no source equality is claimed.
Immutable direct ref and old b0/74/d441/e3/df09/C refs remain unchanged.
[Whole46 disposition](tmp/public-pi-node-whole-range-diff.txt),
[feature range](tmp/public-pi-node-old-new-range-diff.txt) and
[direct/final](tmp/public-pi-node-direct-final-range-diff.txt) retain prior45 exact
SHAs/order and one owning public feature. No obsolete corrective/pin/migration
stream or new supported boundary is introduced.

Focused original19 fixture cases PASS/0skip,449.584802ms/shell3.16s. The declared
ordered application Node block ran ONCE: ACTUAL exit1/13.36s. Five suites passed
129/0FAIL/0SKIP: read_cycle19, attention75, coordination14, resources2,
codex_providers19. Nine syntax targets passed; final10th raw-checkout
review-editor.js gave MODULE_NOT_FOUND before parse because preBuild generates
that asset. Preserve the failed batch and raw utility premature ten-check wording;
no passed final syntax or green original batch is invented.
[Focus log](tmp/public-pi-node-focus.log), [batch log](tmp/public-pi-node-batch.log)
and [raw utility result](tmp/public-pi-node-batch-watcher-result.txt) remain intact.

Lead separately released ONLY the remaining generated-file syntax under7fe5419e.
Exact declared producer
`/nix/store/8q2z94mf32mv0j8wxlsshm805xlfysi9-workspace-repository-review-assets-1.0.0.drv`,
source `/nix/store/f1cazw0yis5cdp0srakb5nxx5r4mvnm9-source`, and existing cached
output `/nix/store/hllcfkaav40y98j1v7vl3gkikgpd0w75-workspace-repository-review-assets-1.0.0`
are bound to nix/review-ui.nix and owning preBuild's literal copy. The regular
255836-byte review-editor.js SHA256 is
`26acff84839bdaf5b7274326551e50be8b9d995b8a11cc03c27e29e408d96401`.
Only `node --check` on that exact existing file ran, exit0/1.03s, with the same
application Node24.19.0
`/nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0/bin/node`
and declared51fz shell. [Independent syntax log](tmp/public-pi-node-generated-syntax.log)
records that separate success. No Pi-worker Node, build/realization/source copy/
placeholder, repeated129 suites or repeated nine syntax checks. Combined coverage
is all five suites plus10 syntax across failed batch and independent check, NOT
one green batch, full package, public browser/SDK/installed/VM proof.

Luna/low/full_access/danger-full-access/never initial/resume headers were verified;
source43134 joined exit1, executing parent24681/readiness10874 and all other
commands joined, no self-wait/survivors. Focus34479, producer clarification92468,
inline independent syntax, commit37238/fold95756 and worktree11768 are closed.
Ordinary Nix tempfile-F/direct commit and interactive fold, no hook bypass.
Checked tree and unchanged producer inputs survive the history-only fold with
no test repetition or derived whole-package equality claim. Source/index/history
windows are closed; this packet edit runs no application command.

### Published b0 Node failure and next exact-d811 gate

Published [Check43396963075/attempt1](https://github.com/aither64/dev-workspace/actions/runs/43396963075),
event push/exactb0, is authoritatively FAILED: all three jobs hit the SAME original
Node suite19/13PASS/6FAIL/0skip (missing isPiCreation/helper context), after Go web
and Ruby317/4908 GREEN. Host skipped as designed. Both guests were dependency-
blocked: archive11 and original creation18+Pi19 are UNRUN, including public Go+Pi/
TLS/literal role/Goal/Accepted/cold attach/reconnect/target/post-Pi Codex assertions.
Failed planned outputs/dependency references are not realized final packages or
recursive closures. Neither new d811 runtime/worker/VM closure nor public Pi
acceptance follows from those successes or the local Node correction.

[Original b0 failed-result/effect handoff](review-transcript-evidence.md#asset-verification-terminal-failed-result-handoff)
binds all10 raw/log/identity links and actual boundary, failure-handoff SHA256
`b79dada87818bd129526e7d7629b4ee0c3005e9579f1712ce92b67a9fdbf59b0`,
boundary SHA256
`ac1ce1c5e4c6297b7310c20203fac2a9f844d8544baec11c5d4ef8bebb277345`,
native-accounting SHA256
`bff50473cb543f8938edf74f882d64b61b94d0778fd199b9909d104c206c5e96`.
Raw utility FAILED/normal task_complete,31 paired calls/outputs/one observer,
source37585 joined1, parent83274 joined0 and PID4125347 absence resolve effects;
stillRunning empty. Workflow984s differs from observer932.276s, neither30min;
no self-wait/resume/signal/retry/cancel. Historical74/d441 failures, raw INCOMPLETE
and independent resolution remain preserved, not rewritten by local green scopes.

[Lead's Node direct narrow-fix disposition](review-final-schema12.md#node-fixture-correction-direct-narrow-fix-disposition)
retains ACTUAL independent d441/C5aa all4HIGH/D46/C2 review and lead-verified74/b0
plus d811 deltas under steps9–10. No new independent-review turn or equal-source
claim to old b0. Strict public preparation reader/target, original receipts/
no-resend, old-reader refusal/forward recovery and runtime/communication lineage
remain unchanged; no DB migration/converter/repair boundary is added.

The later normal d811 node-fix publication/automatic CI completed with mixed
fast/archive success and creation failure, recorded below. Its positive archive
result and failed creation prerequisite stay on exactd811, not final17b. No force/default,
provider/deployment/profile/lifecycle/cleanup or duplicate local VM authority.
E092 package/HOST3/closures and vb2 source-only evaluation remain baseline, not
inherited d811 input/closure evidence. Full TEAM/native3/custom gateway/real
entitlement/integration/deploy remain open or excluded.

### Runtime-wait fixture correction and final finite checks

[Accepted immutable wait correction receipt](tmp/public-pi-runtime-wait-commit-receipt.json),
SHA256 `4f994f94709dd90b96deb4ea0cfb5b5b22aebffef13aa156f6a1b4eaca2367b6`,
and [owner2's source/check handoff](p2central-workflow-evidence.md#public-pi-runtime-wait-fix-real-wait-witness-and-joined-worker)
bind ONLY d811→17b pi_creation_test.go,73 additions/16 deletions (superseding
preliminary74/17 estimate), checked/current/committed SHA256
`6cd6f9840c9de2d1934d27c1e0002e11a9a4c5d3155c8719920b62e18ebdf7f3`.
Lead verified the byte-identical mutation block and original error/zero-effect
assertion tail. All three package/unsupported-roster/role-contract cases, actual
package/role mutations, ErrUnavailable condition, held runtime lock and original
1s observation/3s operation budgets remain. No production Go/JS/docs/pins/schema/
protocol/metadata/authority/recovery change or useful new product documentation.

The test context embeds ORIGINAL context.Context; sync.Once witnesses an actual
Done query and returns original Done. Deadline/Err/Value delegate unchanged.
The owning runtime lock path queries Done only after actual flock contention.
Observer selects the witness, buffered worker result,1s timer and BASE context,
NEVER wrapper.Done; it cannot synthesize its own witness. Before mutation the
runtime stays held, worker unfinished, creates/sends0. Early/timeout-buffered
worker errors are explicit. Release/result are single-owned; all Fatal exits
cancel/release/finite1s join. This cleanup bound does not inflate operation budget.
No production hook, wait stub, lock implementation or assertion weakening. It is
an injected owner/callback fixture, not production host/browser/Pi19 proof.
The old competing creation-lock observer race is concrete; exact historical CI
worker error was never recorded and remains UNPROVED, without flake/slow/mode/
product-regression labeling. Original raw6f4daa evidence is preserved.

Final frozen source checks all PASS: existing wait parent once/all3 .322s;
SAME parent count20 ONCE/all60 5.715s; three exact gate/replay neighbors/11nested
(6 role-contract +5 roster) .812s. One ordered batch real28.83s has24 parentPASS/
74nestedPASS/0FAIL/0SKIP, including21 waitparents/63waitsubcases and3 neighbor
parents/11nested. All63 actual Done-contention witnesses have creates/sends0
BEFORE mutation; no early worker/context/cleanup-join error. Original workers are
received before original assertions. [Final log](tmp/public-pi-runtime-wait-final.log),
SHA256 `4de68bdc9ca19e89ae95293a89d17070d32dec2705a14e63ea4aa643ed2350ec`,
records exact commands/counts. [Preliminary focus](tmp/public-pi-runtime-wait-focus.log)
3PASS/.362s/23.68s is separately scoped before the final timeout-buffered-result
diagnostic, not final-source proof. Known quicks ran inline; tool16104 and prior
17973/commit48033/fold13509/worktree60593 are joined. No watcher/native ID is
invented, no Go/web/Node/Ruby/SDK/VM or existing successful batch repeated.
Earlier Node coverage remains its failed batch plus independent syntax result.

Direct1a4eb2b6 (parentd811) and consolidated17b (parent exacte092) have identical
tree6a477db0 and empty direct..final diff. Same-e092 `git diff --binary` patch
SHA256 `35d1f0aaed78e97871c72c1b75a04115ca0c55a9b78f7af46b6831de930b2230`
is equal for direct/final only. REALd811→17b patch SHA256
`86ed441b054b68bb78704a3c35ae7e417f0330a3de8b3990740a336872949182`
is a source difference; folded17b is not a literal descendant/equal source ofd811.
[Whole46 disposition](tmp/public-pi-runtime-wait-whole-range-diff.txt),
[feature range](tmp/public-pi-runtime-wait-old-new-range-diff.txt) and
[direct/final](tmp/public-pi-runtime-wait-direct-final-range-diff.txt) retain
exact prior45 order/SHAs and one owning public feature. No obsolete corrective/
pin/migration stream. All old/direct/public/default/C refs remain; one-path proof
reuses accepted6dd/13f6/3bee/207 for unchanged1008, no new1009-file campaign.
Ordinary Nix tempfile-F and interactive fold, no hook bypass; source/index/history
and known commands closed. Checked source survives history-only fold without
another check or inherited package identity.

### Mixed d811 CI: real archive success and unrun creation

[Check43402708827/attempt1](https://github.com/aither64/dev-workspace/actions/runs/43402708827),
event push/exactd811, remains overall FAILED: fast SUCCESS, archive SUCCESS,
creation FAILURE, host skipped. Fast declared package/check successes are scoped
to actuald811. [Accepted mixed-result handoff](review-transcript-evidence.md#node-verification-mixed-terminal-result-and-concrete-creation-obstruction)
binds all10 raw/log/identity/effect links, SHA256
`b6cd96b29a1e9e87b7ff4b142c71510b8b2b189c2556c482def4d08d7d4a2459`,
boundary SHA256
`49eb914ba43a0a423bb6768928c96c4bcb8a581a3da47e29013dc2642249f233`,
native SHA256
`ad2f44035005f0a28ef5f221b5cbdc67d79d9f96b8efa8a53431f3a55dba790e`.

Lead independently verified ALL11 original archive subtests, exactly once/source
order and original fixture SHA, actual profile install/register plus four active
services. Remote guest app
`/nix/store/27m202rxaa967sb71y1k1s2mr1f3krfn-dev-workspace-0.2.0`, actual drv
`/nix/store/8nrcm5vfycbks3prmy37z9ak7gibxvxs-dev-workspace-0.2.0.drv`, selected at
`/home/developer/.local/state/dev-workspaces/profile`. Original services are
workspace-codex@fixture, workspace-portal@fixture, workspace-tmux@fixture and
workspace-router. Original archive script finishes486.57s, terminates its ONE
QEMU PID12 and cleanup.28s. This is positive exactd811 remote archive execution,
not a badge inference. No local output/NAR/recursive closure export, artifact
manifest or durable GC retention was obtained; no17b equivalence is inherited.

Creation failed BEFORE guest boot in the old wait fixture at pi_creation_test.go1023,
“fixture did not reach runtime wait,” raw6f4daa preserved. Original18+Pi19 public
creation, builtin TLS/role/Goal/Accepted/preparation/cold attach/no-resend/reconnect/
followup/target/post-Pi Codex assertions remain UNRUN. Actual historical worker
error is unknown; archive success supplies none of those results. Failed planned
creation outputs are not realized packages. The fixture17b correction does not
establish a final17b application/worker/VM closure or public Pi acceptance.

Raw utility FAILED and absent final-report.json citation remain unchanged;
authoritative existing observer result.json plus terminal-run/jobs supplies the
separate corrected citation. No command reran to fix reporting. Native45/45
paired calls/outputs, normal task_complete/one observer, source28854 joined1,
parent87961 joined0, PID206055 absence and original archive guest teardown close
known effects; stillRunning empty. All parent tools/yielded cells are joined.
Workflow1433s differs from observer1357.011s, neither30min; no signal/retry/cancel/
lifecycle or invented creation guest teardown. Earlier d441/74/b0 failures,
snapshots and raw INCOMPLETE/independent effect resolution remain preserved.

[Lead's runtime-wait direct disposition](review-final-schema12.md#runtime-wait-fixture-correction-direct-narrow-fix-disposition)
retains ACTUAL independent d441/C5aa all4HIGH/D46/C2 review plus lead-verified
74/b0/d811/17b corrections under steps9–10. No reviewer turn, independent17b report
or equal-source-to-d811 claim. Strict readers/target bundle/original receipts/
no-resend/old-reader refusal/forward recovery and runtime/communication lineage
remain; no DB migration/converter/strip/repair/authority boundary is added.

The later normal17b runtime-wait publication/automatic CI completed with fast/
archive success and a later creation fixup obstruction, recorded below. Its
results remain exact17b; no successful75c8 package/creation result is implied. No force/default/deployment/provider/
profile/lifecycle/cleanup/reviewer or duplicate local VM authority. E092 HOST3/
closures and historical vb2 source evaluation remain baseline; actuald811 archive
is not17b runtime/VM input proof. Full TEAM/native3/custom gateway/real entitlement/
integration/deploy remain open or excluded.

### Catalog mode restoration: conditional projection and preserved guards

[Accepted immutable package-guard receipt](tmp/public-pi-package-guard-commit-receipt.json),
SHA256 `0073ff2c08ddc1ab195c93382de37371af91cffa0a4fa3543a3260d640e6ee55`,
and [owner2's phase/source handoff](p2central-workflow-evidence.md#public-pi-package-guard-fix-restore-the-catalog-mode-after-writable-fixup)
bind ONLY17b→75c8 nix/workspace-portal.nix, TWO added lines, final SHA256
`4fd48b306ae80930ef37f37f12829e1354a678837fd01ac88d0314c2573802e2`.
The nonnull postFixup branch adds an owning comment plus existing coreutils
chmod444 AFTER original bytecmp, BEFORE the UNCHANGED exact444 test and compiled
validator argv. Removing those lines reconstructs the ENTIRE original file.
Null/absent branch, producer/postInstall/config/catalog bytes and all original
other guards/order remain. No guard weakening, parser/API/schema/authority change,
product Go/JS/docs/dependency-pin value/lock/recovery change or new useful product
documentation; the owning comment explains existing mode ownership.

Actual pinned realized stdenv843sqza setup SHA256
`f3454cb657ab9b482c7036f5724489c61a4fb6490e5286299fc188c594e28618`
places literal `chmod -R u+w,u-s,g-s` before postFixup. Pinned coreutils is
`/nix/store/gph17gb73p6qbrqqjnypfjj5npf0ldyx-coreutils-9.11/bin`.
Before editing, authorized conditional4317bcde projection used ONLY exact public
old17b Nix source payload, not actual catalog/auth/validator input. Actual install
produced REG444; actual stdenv chmod produced REG644, cmp0/hashd181f0bd unchanged,
ORIGINAL exact444 guard1. Explicit chmod444 restored REG444, sameguard0/cmp0/hash
unchanged, exit0/real2.34s/tool4042. [Projection log](tmp/public-pi-package-guard-projection.log)
SHA256 `708ecae726851bc677f5f92d3a60c07a64d420dcc5bea06bb5123856808c24ae`
preserves the inner guard1 rather than calling it a package success. Projection
path retained; no runtime/user-state chmod or cleanup occurred.

That criterion justified restoring the SAME invariant after writable fixup.
It proves mode/content-independent phase behavior ONLY, not actual catalog
bytes/schema/compiled validator, all fixup hooks, actual historical first failure
or output mode. No validator ran on the payload. Do not call CI644 measured or
claim validator success. Known raw01433f first failed command remains UNKNOWN.
Nix parse passed exit0/.09s; [parse log](tmp/public-pi-package-guard-parse.log) and
whole-file-minus-two-lines/source-order/diff proof pass. No rendered evaluation
campaign, actual application realization/build, test/suite/Go/Node/Ruby/SDK/VM or
CI replay. Seconds-long checks inline, no watcher/native ID invented. Existing
wait/Node/fullweb/Ruby/SDK proofs retain their exact scopes without repetitions.

Direct35e2f967 (parent17b) and folded75c8 (parent exacte092) have identical tree
bd1f5921/empty direct..final diff and equal same-e092 `git diff --binary` patch
SHA256 `0854cd5be99eb488d8cb6cb62e48ee5c44e6d305644d92dc5bbb1e752cdd6e06`.
REAL17b→75c8 differs, patch SHA256
`dfb2b193113daced15f95acd934c979839e94133f9b304f5a52f5bcd453b6e21`;
folded75c8 is not a literal descendant/equal source of17b. Original/direct/public/
default/C refs retained. [Whole46 disposition](tmp/public-pi-package-guard-whole-range-diff.txt),
[feature range](tmp/public-pi-package-guard-old-new-range-diff.txt) and
[direct/final](tmp/public-pi-package-guard-direct-final-range-diff.txt) preserve
prior45 exactorder and one publicfeature; no obsolete fix/pin/migration stream.
One-path Gitdelta reuses accepted4f99/6dd/13f6/3bee/207 for unchanged1008, no new
1009-file campaign. Source worktree69045/projection4042/parse/commit57205/fold29439
are joined, normal Nix tempfile-F/hooks/fold without bypass. Source/index/history
windows closed; checked tree survives history-only fold without repeat or
application derivation/closure equality claim.

### Mixed17b CI: fresh archive success and unresolved first fixup command

[Check43408749547/attempt1](https://github.com/aither64/dev-workspace/actions/runs/43408749547),
event push/exact17b, remains overall FAILED: fast SUCCESS/archive SUCCESS/
creation FAILURE/host skipped. [Accepted mixed-result transcript](review-transcript-evidence.md#runtime-wait-verification-terminal-fastarchive-pass-creation-fixup-obstruction)
binds all10 linked raw/log/identity/effect receipts, result-handoff SHA256
`4170959e349082f131c00b8c9c08067026b7778b75787e5b3197efa4a178df6c`,
boundary SHA256
`02654d3ee2b8f09d20a5aeaf5ca5d9c8a95bbc241a01753567dcd7f613df5f47`,
native SHA256
`3182eda36ca6612b95b7f2ac862bde5be4b3f85b375122035643d9cec09138f1`.

Lead verified archive11 original names exactly once/in order, actual NEW17b
remote guest app
`/nix/store/yh7rabqn26ar3lqvsn5bsdd6rkk384cb-dev-workspace-0.2.0`, drv
`/nix/store/ywksmm9b7cbx8jznp1wdl8py77r95yrr-dev-workspace-0.2.0.drv`, selected at
`/home/developer/.local/state/dev-workspaces/profile`. Register plus all four
original services complete, script499.06s/QEMU12 termination/cleanup.29s. This is
positive exact17b archive, not inherited d811 evidence. No local NAR/recursive
closure/export/GC retention or successful75c8 package identity is established.

Creation's custom package finishes Go/Node checkPhase4m29, no wait recurrence,
then late fixup exits1 after stripping without the first failed command/mode or
validator outcome. Raw SHA256
`01433f0e70f9728d59b1edc55ab70f3941701d9d54d801100c8d052ab08cfdf8`
remains unchanged; last printed strip line is not a proven cause. Original18+Pi19
never booted and remain UNRUN. No catalog equality/schema/compiled validation,
public Pi/TLS/cold/reconnect/target acceptance can be inferred from completed
checks, archive success or the separate mode projection. Failed planned custom
package output is not a realized package/closure.

Raw utility literal FAILED/result.json and normal task_complete remain intact.
Native37 paired calls/outputs/one observer, source60709 joined1, parent75993
joined0, PID505204 absence and ONE original archive guest teardown settle known
effects; creation has no guest. All tools/yielded cells joined/stillRunning empty.
Workflow1244s differs from observer1110.937s, neither30min. No retry/cancel/signal/
source mutation by verifier. Earlierd811 archive and older failures/snapshots/raw
INCOMPLETE/independent resolution remain in their exact scopes.

[Lead's catalog-mode direct narrow-fix disposition](review-final-schema12.md#catalog-mode-restoration-direct-narrow-fix-disposition)
retains ACTUAL independent d441/C5aa all4HIGH/D46/C2 review plus explicitly
lead-verified74/b0/d811/17b/75c8 repairs under steps9–10. Overall risk remainsHIGH;
no independent75c8 report, rerun or equal-source-to17b claim. Strict reader/target
bundle, original receipt/no-resend, old-reader/forward recovery and actual runtime/
communication transformations remain; no DB conversion/repair/strip/migration
or public authority boundary is added.

The later normal75c8 package-guard publication/automatic CI completed with
fast/archive success and all18 original creation cases, then a first Pi19 finish
precondition failure, recorded below. It supplied actual package-stage evidence,
not substantive Pi19 acceptance or a successful fe1 result. No force/default/deploy/provider/profile/lifecycle/
cleanup/reviewer or duplicate local VM authority. Actual17b archive + projection
is not75c8 app/worker/VM/compiled catalog/public Pi/TLS/cold/target/closure proof.
E092 HOST3/closures and vb2 source evaluation remain baseline. Full TEAM/native3/
custom gateway/real entitlement/integration/deploy remain unfinished or excluded.

### Retained source Plan: two-fixture precondition and faithful control quick

[Accepted immutable Plan correction receipt](tmp/public-pi-plan-commit-receipt.json),
SHA256 `ff31fb98794b8478ac835663dc09831a25db877852f9bb75b6043c0937531461`,
and [owner2's complete handoff](p2central-workflow-evidence.md#public-pi-plan-precondition-fix-resume-the-same-retained-source-plan)
bind exactly TWO fixture paths,35 additions/1 deletion. Current checked hashes:

- nix/tests/session-creation.nix:
  `1ecc1be93a4b46bafd435d60643807e504f50563decf52d7442ac55205ac592d`.
- test/creation_acceptance_browser.cjs:
  `f4365e210d95dc39a0ceeb9bd1580fc25d64d3b4a49b41655799e88e9488fd54`.

ONLY Pi19's FIRST finish call opts in via
`browser("finish", "explicit", keepPlanning=True)`. Inside usable(), after real
canonical source/transcript readiness and before the original unique followup,
it requires finish/same source/current completed Plan/original primary/gpt-5.5/
high. It waits for visible normal Keep planning, clicks without force, then
requires hidden decision and visible ordinary composer. Readonly GETs retain
source ID/latest turn/Plan mode and entries/provider/model/effort and serialized
record.options; no option is written into record.options. No forced fill, DOM
mutation, injected Send, checkpoint rewrite, Plan clear, alternate-session swap
or all-finish normalization. Product control remains unchanged.

Removing ONLY the first-call keyword/local capture/opt-in block reconstructs
BOTH whole75c8 files. All18 Nix prefix, remaining Pi arm/post-Pi finish and every
original usable/followup/Pi assertion are byte-identical: exact-one unique user
input/completed matching reply/Goal once/settings/notifications/reload/receipt,
role/Accepted/IDs/no-resend/TLS/containment/cold reconnect remain. This satisfies
an existing UI precondition rather than dropping coexistence proof. Post-Pi
finish remains independent/no opt-in; native ordering is a later gate.

FIRST, before fixture edits, the exact existing
`PORTAL_BROWSER_TEST=1 go test -mod=readonly ./internal/web -run '^TestQuestionBrowser$/^question_browser_test[.]cjs$' -count=1 -v`
ran on frozen75c8:1 parent/1 subtest PASS/0skip,48.15s/48.24s/package48.300s/
shell70.26s. [Faithful browser log](tmp/public-pi-plan-browser.log), SHA256
`ca077c358121fce67cf214578dc3a913a36a912e72f7e944959184ddd1eb80db`,
shows shipped UI/scripts under controlled model-1/medium Plan APIs: hidden
composer→NORMAL Keep planning→visible/focused preserved draft, plus pending-
question precedence and four viewport checks. This is NOT nativegpt-5.5/high,
maintenance/Pi composition, actual new opt-in invocation/order or installed
successor proof. Unknown-certificate TLS diagnostics remain raw/unattributed.

Declared51fz shell/application Node24.19 and existing accepted cached Playwright
inputs are bound in the receipt; no download/build/harness. The two changed VM
fixtures leave actual quick Go/question-script/app/session-template hashes
unchanged: reuse ONLY this control quick, no repeat/whole-source equivalence.
Fresh Luna/low/full_access/danger-full-access/never headers verified before
source and at resume; source45294/ready26153/parent71851 joined, no survivors or
self-wait. Runtime environment was not relaxed.

Node helper syntax and Nix parse pass exit0/2.40s. [Syntax log](tmp/public-pi-plan-syntax.log)
and [source proof](tmp/public-pi-plan-source-proof.json) bind the actual unique
interpolation-free FIRST Pi19 browser statement via ast.parse ONLY. No rendered
driver execution/new interpolation parser/build/VM or native-order claim. Actual
control inputs unchanged; no browser/Go/Node/Ruby/SDK/full-suite replay.

Directe560ae88 (parent75c8) and folded fe1 (parent exacte092) have identical
14abbd4b tree/empty direct..final diff and equal same-e092 `git diff --binary`
patch SHA256 `7f23c494072ad189bdd12549883711522e15c159ea42e5a86119146d2fe06ec0`.
REAL75c8→fe1 differs, patch SHA256
`b00dcab8211c5597f1a4fd7077928a59f1609a0748b8f5f958db31e384b768fd`;
folded fe1 is not a literal descendant/equal source of75c8. [Whole46 disposition](tmp/public-pi-plan-whole-range-diff.txt),
[feature range](tmp/public-pi-plan-old-new-range-diff.txt) and
[direct/final](tmp/public-pi-plan-direct-final-range-diff.txt) retain exact prior45
order and one owning feature; no obsolete corrective/pin/migration stream.
All prior/direct refs/receipts and C5aa/C2/five pins/full lock remain unchanged.
EXACTTWO-path proof reuses accepted0073/4f99/6dd/13f6/3bee/207 for unchanged1007,
not1008; no new1009 inventory/hash scheme. Worktree59116/syntax38934/commit37533/
fold27060 and known commands joined; ordinary Nix tempfile-F/hooks/fold without
bypass, source/index/history closed. No product documentation is useful for this
fixture precondition; approved docs/copy/routing remain unchanged.

### Mixed75c8 CI: original creation18 passed, substantive Pi19 unrun

[Check43415477758/attempt1](https://github.com/aither64/dev-workspace/actions/runs/43415477758),
event push/exact75c8, remains overall FAILED: fast/archive SUCCESS, creation
FAILURE, host skipped. [Accepted mixed-result transcript](review-transcript-evidence.md#public-pi-package-guard-verification--exact75c8-automatic-ci-mixedoverall-failed)
binds handoff SHA256
`342a50434b0ab744f0fbc4084e75876343a8bc307d6624a7f7239e0ccc1d4760`,
13 result/native/log/checkpoint/header plus5 publication receipts. Raw creation
SHA256 `b5d5139bf24c5d6cb29ba0a2639e9b818f65a4d34fc608131fc94031d0436f06`
and original failures remain unchanged; console500 endpoint/cause is UNATTRIBUTED.

Archive11 original cases complete once/in order, script432.08s, actual75c8 app
`/nix/store/7cw7xlp6bfwwqhq2hnzfgxk4h1cyd2vw-dev-workspace-0.2.0`, drv
`/nix/store/d06s54z5gl5vfri1jjbibl7j64j1spdx-dev-workspace-0.2.0.drv`, original
profile install/register/four services/QEMU12/cleanup.14s. Creation now completes
custom package builds/install/fixup and ALL18 original creation cases exactly
once/in order, including real profiles/registration/maintenance. Actual creation
profile app is `/nix/store/q90ljqw16r0kavwl4d31y1kky724bx4s-dev-workspace-0.2.0`;
maintenance target `/nix/store/8ml1vj17s7x4r70pkxnxl3p6cqp3hbmc-dev-workspace-0.2.0`.
Concurrent observed drvs73hhf0x7/yrx26k59 have no explicit individual output
pairing receipt, so no assignment is guessed. The active original cmp→restoration→
444 guard→compiled validator branch completes through actual package install;
mode/validator outcomes were not separately printed. This is stronger75c8
package-stage proof than the prior public-payload projection, not fe1 inheritance.

Pi19's FIRST finish-explicit encounters a hidden ordinary composer and retained
completed source Plan BEFORE worker Node/TLS probe or Pi creation. Substantive
Pi19 public request/production Go+Pi/role/Goal/Accepted/receipt/preparation/cold
PID/no-resend/reconnect/followup and writable Codex AFTER Pi are UNRUN. Original18
success is not full creation acceptance. Creation driver fails its assertion,
original failure exports/QEMU12/cleanup.60s complete; two original guests total,
not duplicated teardown text. No fe1 runtime/worker/VM/closure/publicTLS/target
success or local NAR/export/GC retention follows. Workflow exports no recursive
closure/artifact manifest; unpaired drv/output identities remain explicit.

Native75 calls/75 paired outputs/one observer/normal task_complete, source8835
joined1, parent58757 joined0 and CLI/observer PID absence close known effects;
all tools/cells and TWO original guest teardowns joined/stillRunning empty.
Raw FAILED retained. Workflow2460s differs from observer2398.626s; requested
status and ONE actual30min checkpoint at1838.959s retained. No self-wait/resume/
signal/retry/cancel/source mutation or lifecycle action by verifier. Earlier mixed
and failed results and raw INCOMPLETE/independent resolution remain scoped.

[Lead's Codex Plan direct narrow-fix disposition](review-final-schema12.md#codex-plan-fixture-precondition-direct-narrow-fix-disposition)
retains actual independent d441/C2 all4HIGH/D46/C2 review plus six explicitly
lead-verified74/b0/d811/17b/75c8/fe1 repairs under steps9–10; no independent fe1
report or equal-source-to75c8 claim. Strict reader/target/recovery/original
receipt/no-resend/old-reader/forward-only and runtime/communication lineage stay;
no migration/converter/strip/authority boundary added. Full TEAM/native3/real
provider/custom gateway/entitlement/integration/deployment remain open/excluded.

The later normal fe1 publication/automatic CI is now solely owner0-observed.
Only the supplied archive prerequisite failure is recorded below; terminal/effect
handoff and fast/creation outcomes remain PENDING, not inferred or queried here.
The UI quick/syntax proof alone supplies no actual native ordering or final18+Pi19
acceptance. No duplicate local VM or new verification is queued by this packet.

### Native-preflight termination fixture: ordering, identities and bounded repeats

[Accepted immutable preflight-count receipt](tmp/public-pi-preflight-count-commit-receipt.json),
SHA256 `d91e1f17e217535e43ca505e40aef9d0a133f0974ab8d188890b1abc1d6ab756`,
and [owner2's complete source/check handoff](p2central-workflow-evidence.md#public-pi-native-preflight-count-fix-install-term-handling-before-publication)
bind ONLY test/workspace_host/commands_and_locks_test.rb,14 additions/6 deletions,
SHA256 `4544db51595bcec5c5b2684b764e8ddbdf9c2302eeda80ce539fba716094c657`.
Unchanged TERM-handler block SHA256
`5c47c59cc3eda29ba10abcb6238eb2a7d45e80151b738310a20c5a98c9b5966c`
now follows resolved home/sqlite/log variables BEFORE BOTH invocation-ledger
append and socket publication. Removing only bounded additions and moving the
exact handler back reconstructs the ENTIRE original fe1 file.

Original count2/four invocations/argv/config0700/scratch/schema/sentinels/parent
ENV+cwd/isolation checks, both refusal variants, .002×150 refusal budget and
product process-group TERM/wait stay unchanged. Diagnostics are bounded to
refusal flag, expected homes, first4 observed termination homes and validated
app-server argv. Two DISTINCT expected homes from validated invocation children
and exact sorted terminated-home equality prevent duplicate masking; original
count2 remains. No new readiness protocol/lock/fsync/hook/fake completion/
signal-wait mock/timeout/retry/product change. This repairs fixture publication
ordering, not shipped Codex/SDK/Pi behavior or arbitrary descendant cleanup.
No new useful product documentation; approved docs/copy/recovery stay unchanged.

Ruby syntax OK, then FIRST exact parent seed1629 PASS:1 run/118 assertions/
0failures/errors/skips,1.985753s/real4.68s. SAME parent then ran ten FURTHER
sequential FRESH Ruby processes once each, stopping on first failure: all status0,
each1/118/zero failures/errors/skips, valid individual real2.47–2.68s. Total11
selected tests/1298 assertions, both variants/four invocations and two DISTINCT
TERM completions per variant each time. [Focus log](tmp/public-pi-preflight-count-focus.log)
and [repeat summary](tmp/public-pi-preflight-count-repeat-summary.log) preserve
all11 per-process log hashes/statuses in the receipt. Literal malformed summary
`real 27.:0` remains unchanged; no numeric repair, new timing query or retest.
Seed1629 on one selected test is NOT historical whole-suite order/signal replay.

Known bounded checks inline, no watcher/native ID invented. Worktree93111,
first56440/repeat61851/commit77043/fold76585 and all issued commands are terminal/
joined. Real fixture children use unchanged product spawn/process-group TERM/wait;
completion/scratch assertions pass. No full317 shard/aggregate, Go/Node/SDK/VM/
application build or CI repeat. Source/index/history windows closed, normal
Nix tempfile-F/hooks/interactive fold without bypass. Checked tree remains
unchanged across direct/final history step, with no equal-input repetition.

Directb1900fe0 (parentfe1) and folded df99 (parent exacte092) have equal5bf7ea9c
tree/empty direct..final diff and equal same-e092 `git diff --binary` patch
SHA256 `bbc2f5d0964f0c4a39e94280b0eee038e4810f366a301c15bc583a6b5488baf0`.
REALfe1→df99 differs, patch SHA256
`d05354224548a56ce17aae360779e0d5597810a5bbe9e6a78c1dbf07f49f3b83`;
folded df99 is not a literal descendant/equal source of fe1. [Whole46 disposition](tmp/public-pi-preflight-count-whole-range-diff.txt),
[feature range](tmp/public-pi-preflight-count-old-new-range-diff.txt) and
[direct/final](tmp/public-pi-preflight-count-direct-final-range-diff.txt) retain
prior45 exact order and one owning public feature. No obsolete corrective/pin/
migration stream; original/direct/public/default/C refs preserved. EXACTONE-path
proof reuses acceptedff31/0073/4f99/6dd/13f6/3bee/207 for unchanged1008, no new1009
source inventory/hash scheme. Production Go/JS/Ruby/formats/protocol and recovery
remain unchanged; no new package/closure/readiness claim.

### Existing exact-fe1 CI: known archive failure, terminal/effects pending

Only lead-supplied existing facts are recorded: normal fe1 feature publication
and exact remote/default/C verification c3761f20 closed its ref window; bound run
a5c63b73 is [Check43427342273/attempt1](https://github.com/aither64/dev-workspace/actions/runs/43427342273),
event push/exactfe1, start12:41:41Z. Archive131891916722 FIRST fails BEFORE VM
in required Ruby derivation
`/nix/store/10jcc1mgwavg18h5g1xwjmmyyiidikaq-dev-workspace-workspace_host-0-of-1.drv`:
commands_and_locks104 Expected2/Actual1 TERM-completion ledger,317 runs/4900
assertions/1failure/0errors/3existing skips/51.874362s/seed1629. Immutable raw
669560bytes SHA256
`f59d0c57f1668621c3affbec5e919f0b496c310b1d58549df910a6686d5e8279`;
four invocation/argv/isolation checks passed before the count failure. Archive11
is UNRUN. The count is completion records, not launches or unjoined children.

Historical failing variant/missing home/signal timing/status/kill-wait result
remain UNKNOWN. The source ordering exposure is not proof of the exact CI cause;
no flake/Pi/Plan/catalog/product-regression attribution. Selected quicks with the
same seed do not prove whole-suite scheduling reproduction. Prior full317/4908
results keep their earlier source/input scopes.

Fast and creation remain solely owner0-observed. Their terminal outcomes,
remaining assertions, native joins/effect handoff and lead acceptance are
PENDING; this packet neither queries/downloads moving CI nor infers a final
result or unjoined child. If later facts arrive they require their own accepted
disposition; no terminal conclusion is supplied here. Previous exact75c8
mixed342a5043 archive11+creation18 positives remain ONLY75c8, with substantive
Pi19/cold/post-Pi still unrun there. No df99 application/worker/runtime/VM/closure/
real TLS/public Pi/target acceptance follows from fixture quicks or old outputs.
All earlier raw failures/snapshots/INCOMPLETE/effect resolutions remain unchanged.

[Lead's native-preflight direct narrow-fix disposition](review-final-schema12.md#native-preflight-termination-fixture-direct-narrow-fix-disposition)
retains actual independent d441/C2 all4HIGH/D46/C2 review plus SEVEN explicitly
lead-verified74/b0/d811/17b/75c8/fe1/df99 repairs under steps9–10. No independent
df99 report, reviewer turn or equal-source-to-fe1 claim. Strict reader/target/
original receipt/no-resend/old-reader/forward recovery and actual runtime/
communication lineage persist; no DB conversion/strip/migration/authority change.
Full TEAM/native3/real provider/custom gateway/entitlement/integration/deployment
remain open/excluded. Native fixture success is not shipped Codex/SDK/Pi proof.

NEXT: later owner0 publication/ONE successor CI needs lead packet acceptance
AND accepted existing fe1 terminal/effect handoff, capacity and SEPARATE
allocation. No new verification queued, duplicate local VM, force/default/
provider/deployment/profile/reviewer/lifecycle/cleanup authority or readiness claim.

### Documentation routing, fidelity and remaining gates

Main-context copy pass327f0670 is closed; lead verified these approved bytes,
unchanged by the74, b0, d811,17b,75c8, fe1 and df99 corrections. Existing Error reuse needs no new product copy or
doc change; correction execution evidence stays with its owning session record.
Protected R2/R4 anchors, commands, predecessor refusal, forward recovery and
original receipt/no-resend meaning remain. Execution receipts stay in the existing
session evidence; README remains the entry route.

| Topic → reader / class | Authoritative owning path / approved SHA256 |
| --- | --- |
| Preparation wire, compatibility/recovery → users and maintainers / reference + supported recovery | docs/session-preparations.md — `1e5749ef938567ed81f00db164c96c378ce54c1b28ec2b49fe012ec179eeb009` |
| Public form, explicit Pi Solo limits → portal users / how-to | docs/workspace-portal.md — `d3dccc4ba1a72c941cdd988bdb35ea030e81e86dba7a48210cc4f0ef8c7bfbed` |
| Builtin runtime composition and readiness → operators / reference | docs/pi-runtime.md — `fc829d87a23383771b014d7ebe125660084cae1f470cc414ea730cd1c66ca04b` |
| Exact attempts/inputs/effects → reviewer and lead / individual execution | existing p2central-workflow-evidence.md final section + immutable receipt/graphs linked above |

Predecessor e092 Check43357315998/attempt1 fast, original archive11 and creation18,
plus accepted OFFLINE-HOST3 host-module-idempotency11/recovery6/pi-runtime-host,
remain successful ONLY for exact e092. Actual app2iv, worker80jaf9,18 roots and
1060-path union in [original transcript evidence](review-transcript-evidence.md#offline-host3-terminal-three-exact-e092-offline-gates-passed)
are not inherited by d441. Host fixture uses synthetic supervisor/auth, not final
public Go+Pi/browser proof. Prior installed/pre-register outcomes remain as recorded.

Original d441 VM fixture hashes below remain historical; fe1 updates exactly
the Nix/helper pair with current hashes above. Original session-creation.nix
`e2a7636f7d01e560792c868a615d684675ba131d9cc5ce00b4f39b3b3a5cb7f1`,
creation_acceptance_browser.cjs
`6884bda19388fbb4108fae06994667017c38ae6d0565f323dc48474836b96c70`,
creation_model.py
`345c9aebbe7234173ef4bddffcf39ec95648cdad2b6d407a17425b2484c90eb9`.
The [evaluated driver](tmp/public-pi-solo-vm-final-script.json) and
[evaluation receipt](tmp/public-pi-solo-vm-final-eval.txt) establish source/AST/
syntax/evaluation only, vb2hk21gywylml4812c7z11qq1x437ja derivation before final
test-only literal corrections. No built final committed application/VM closure,
actual builtin TLS/trust, public form→production Go+Pi, browser/restart/followup
or target success is proved. The source preserves18 Codex cases and adds the
controlled builtin DNS/TLS arm, but assertions in source are not execution.

The d441 independent review is complete;74, b0, d811,17b,75c8, fe1 and df99
narrow corrections are main-verified. Any separately allocated df99 NEW feature
publication/ONE automatic CI requires packet acceptance AND accepted existing
fe1 terminal/effect handoff/capacity, not this edit alone. Full TEAM, native3/production fallback,
custom gateway/real entitlement, integration and deployment remain open or excluded. Session stays
open; no default integration, profile activation or lifecycle action is authorized.
Owner2 retains technical/review fixes; lead owns acceptance and the next verification release.
Owner5's window is ONLY this packet; no source/ref/index/history/test/build/VM/
SDK/CI/publication action accompanies it.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/

---

## Preserved e092/H1 packet and original R history

The following submitted material is preserved verbatim, including its original
status lines and source-scoped claims. Current d441 target/status above supersedes
those submission-time headings; the original reviewed1f2 copy/receipts remain.

> **Current lead status:** H1 is resolved on reviewed D `e0925346` and C `5aa6111`; final source/history review is complete. Both feature refs are published. [Check 43357315998](https://github.com/aither64/dev-workspace/actions/runs/43357315998), attempt 1/exact D head, is in progress. Package/VM and remaining host/installed gates are not yet proved.
>
> The detailed packet below is the submitted H1 snapshot (SHA256 `1f2da9efd0e0d961f7bb2b43c0d91a832d936c4ae6425d21909c89bff0bfada5`), preserved byte-for-byte at `/tmp/pi-schema12-candidate.wwMbgc/h1/review-packet-reviewed-1f2da9ef.md`. Its pending-review/publication wording describes submission time; current status is in [state.md](state.md) and the [final review record](review-final-schema12.md#h1-closure-and-exact-final-source-review). No integration, deployment/profile activation or lifecycle permission follows.

# Pi integration review packet

## Current provisional schema1/2 candidate assembly

**PROVISIONAL — not ready for publication, activation or final integration.**
Owner5's isolated source/history assembly and accepted generic-root correction
are committed; finite checks cover the intended source. The source/history packet
now includes the lead-accepted H1 remediation for completeness assessment and the
same independent reviewer0. H1 remains OPEN until its new history/pin proof is
accepted; reviewer0's source inspection on frozen387d/a883 continues independently.
The actual pre-register failure has a diagnosed product cause and accepted source
correction, but corrected-package registration, original _activate/service-readiness
and broader final checks remain unproved. No diagnostic stop or fixture chmod was
imported. The new D/C ranges have not yet received the final H1/history/pin conclusion.
This current section supersedes the R-only target/status below; historical
sections and their exact source-scoped evidence remain preserved.

| Candidate / input | Exact identity |
| --- | --- |
| Final D base | `eabb56a278bd8eb1759041467eaebfa6392ddcb2` |
| Final D candidate | `e0925346dae8e862df518b3fecc6e857561c1000` |
| Final D tree | `7a82528eeabe43423ef08219f71508b5413e3e39` |
| Preserved pre-H1 D | `387d6758a94d40be8cc9b6150044710a799e86d3`, tree8bf123f0 |
| Exact direct accepted root fix / equal pre-H1 source | `7faba746bb8b9eae5ee50263848375c87cf39bb1`, SAME tree8bf123f0 |
| Preserved prior45 candidate | `c658862c94c3c79241ded0246ee39e0983e9efa9`, tree08f27552, DIFFERENT source |
| Previous combined source before initial history-only consolidation | `37f7b449a0c32d58ae7871adf3becba8d553ab3d`, SAME tree08f27552 |
| Fixed-db4 composed source | `c83acbd3528a70a911979173fd0c48f4b31518ae`, tree `c602ac6d22e7689c8512b5b503c87afd0362c63c` |
| Refreshed pre-monitor-join source | `4cfb1ab883d0ab41aa971fdfd09f330a6736b474` |
| Exact R4 input | `e6717177df3ccdd9846a84ef48d0e3cbc917a4c8`, tree `48a7e41f2dd8a88dc6a93ac201c1c0f1e742e974` |
| Exact R input | `cd5fd5cbc9670311d411466de8ec63ff670d53b0` on db4 |
| Final immutable C | `5aa6111db1a71b17191befb8532bad7dcae2e15d`, tree `ca190011bdc2da235a0e6ffc7a8209e78bb5f55d` |
| Preserved original C source | `a883fcb6610bd41c6bd4e7f8a00c19e9adb5d5e8`, equal final C tree, distinct source identity |

The NEW registered worktree is
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace-schema12-candidate`,
branch `2026-11-11-pi-codex-migration-schema12-candidate`. Owner5 alone owns its
source/index/history. It is clean with an empty index. All R/C/native/parked/
published/correction source refs remain; the temporary reconstruction branch and
fixed-composition/preconsolidation refs are retained. No primary worktree/index/
feature ref transfer or cutover occurred. Saved settings remain Sol/xhigh/
workspace_write. No repository merge claim was taken.

### Frozen sources and current remote facts

Fresh canonical SSH ls-remote/fetch before the initial assembly observed D master exactly
eabb (the known target), published initiative feature0af8ac84 and transcript
featurebe0ce2a6; C masterdd90 and transcript featurea883. No extra D default delta
or changed C prerequisite required fit assessment. Those observations are not
future publication leases: any later feature-only publication must refresh exact
remote values and use an explicit observed lease. The initial assembly ran no push or CI trigger. H1 later explicitly authorized
only the NEW C feature publication needed for real immutable input resolution;
that publication and its automatic CI are recorded below. No D push/CI occurred.

Exact source aliases frozen without modifying their original branches:

| Alias | Head / disposition |
| --- | --- |
| D-transcript | `be0ce2a6d90c82b652e3e191057f329bba62b294`: R1/R3/R5 adapter, final C dependency, tests |
| D-Ruby | `cc8513956fbcff3ef119caf3f127a41823bfc2a9`: explicit retained Codex-only fixture inputs |
| D-checks | `1e6687750e51842e34641470bff32e87939bd71f`: worker golden/cmd/creation fixtures |
| D-legacy | `ead7e362cb2354d908023eb45399b9263b16f5ce`: supported Codex schema2/no-thread compatibility |
| R2 original/adopted | `086ad5652f53904bc30df6b10891f21a5717ad5d` / `e6eb8d28b8f4645de05a7cccb9330e8724924ca8`: one owning roster/root stream |
| A1 | `bd4b606c2264653da30a383563adcb6b4134e475`: root/runtime/backend README corrections |
| R4 full series | `1205321e73938b40440c85e62216380422b75f46`, `c8b647b55ce47d9121dadcd0b3201a9e336c14e7`, `f83b9f94acfa3aaee5862f401103944f7cb5f8d2`, `7324702ac7f77d7d8a3c51eafbec47baabbc1daa`, e6eb8d28, `c2200b9c4ecee9a1f954fc8fef0f0b2777b1c1cf`, e6717177; accepted8c16/602d aliases/receipts retained |
| C H1 successor | `5aa6111db1a71b17191befb8532bad7dcae2e15d`: exact same C content in two logical commits, newly measured immutable inputs |
| Root compatibility | `7faba746bb8b9eae5ee50263848375c87cf39bb1` on exactc658; accepted three-path patch, folded once into inventory/R4 owners |
| Native EXCLUDED | `d3b0057f6b032d19a4b2cc86b81a3493e5220981` / `234dfd530d8412a559e6e0b09b9eaa671037d48a`: retained separately, no native3 writer/TEAM/route claim |

Raw frozen-source/tree table is `frozen-inputs.json`; session ref snapshots retain
32 D refs and six C refs. Existing reviewed source, source aliases, source-input
receipts and prior failed/successful reports remain intact. Links:
[original final review/remediation record](review-final-schema12.md),
[transcript/CI evidence](review-transcript-evidence.md),
[A1 documentation](review-a1-doc-evidence.md),
[R4 guard/full handoff](review-r4-guard-evidence.md),
[P3 instructions/application/proof](p3i-review-instructions-evidence.md).
The prior same-reviewer R4 follow-up found no new findings on exact R..e671;
that conclusion does not review this combined closure or new monitor semantic join.

### Composition, refresh and consolidation are distinct proofs

1. At fixed db4, start complete R4 (R/R2 already present), replay actual four-commit
   R..ead7 transcript/CI stream, then A1. The ONLY omitted replay is the identical
   FreshAcceptance `awaitCreation` hunk in pi_creation_test.go already owned by
   R2. No other cancelOperations/Wait pattern was omitted or generalized.
2. Ordinary hooked52-commit replay onto exact eabb had no textual/substantive
   conflict. Fixed c83 and refreshed4cfb are DIFFERENT sources. The known three
   upstream commits are f124fd4e monitor new-report semantics/guidance,
   e1c67dbe archive preparation contention/rechecks and eabb maintenance completion
   reinspection after worker exit. All15 upstream paths remain in the final tree;
   archive current identity/cancellation/status/pause/retry and maintenance durable
   completion-after-exit behavior are preserved.
3. Add ONLY the settled two-file monitor parity join, producing37f7/tree08f27552.
4. Initially reconstruct history at fixed eabb using ordinary Git/Nix and
   tempfile-F commits.53 source commits become45 logical commits. This initial
   history-only step has equal trees and byte-identical full-index binary patches
   for37f7 and preserved priorc658. Its patch SHA256 is
   `333cafd056b27173153675558c0a8b39599f08929dd017b6a13d8b3244071005`;
   its full range-diff SHA256 is
   `b7b8b9716e09e690cf3dc010fcfc2fb2ae9f534dc4120caf94541eeb934a3f5e`.

The ordinary early pin patch referred to a later Pi-input context line not yet
introduced. Replay therefore checked exact a2 scalar preimages and substituted
only the accepted final five-file C source/version/checksum/vendor values. There
was no source-identity substitution, unrelated lock change or substantive conflict.
All other corrective/doc joins applied directly with final tree equality checked.

The accepted root correction is a later substantive source step: priorc658/tree
08f27552 becomes direct7f/tree8bf123f0, exactly three paths/283 additions and one
deletion. Only its subsequent history fold claims equal trees and binary patches:
pre-H1 final387d6758 and direct7f both have tree8bf123f0, with the same complete eabb..head
patch SHA256 `664cc3c937727f12b1fc9bb43c6735328067ea19d1341ec0756eb269557717fe`.
There is no equality claim across the correction or upstream refresh. Full old45
and new45 series, hunk dispositions and range-diff are retained in root-fold/;
range-diff SHA256 `be0d9dc0801da7d9bb3945696929103037b519035cca5c35add67ad2181058b2`.
Originalc658, direct7f, old53 and all earlier required source aliases remain.

### Final complete D series and source-hunk dispositions

Final eabb..e0925346 has317 files,50247 insertions/367 deletions. Each row gives the
full final ordered commit, its owning original combined-source number, and every
folded/split hunk. Unlisted paths retain their owning source patch. Original R
43->40 and R->refreshed40 mapping below remain historical lineage; the full53
source series and map connect them to this complete45 series.

| Final # | Full final commit | Combined source owner / folded hunks |
| --- | --- | --- |
| 1 | `bfe228e1b32c9c7730b86d696df93ed5ac5581b7` | source1 `1cd30a5577718edca374307fe117bf7def013e32` pi: add finite worker conformance probes; source52 pi-runtime/README.md |
| 2 | `ac3318a716e0feb1ede61dd4c17ecbffb36994ad` | source2 `cf432ce5fb1018e54f917629bad233f082f5121d` session: add strict Pi backend identity readers |
| 3 | `e1f4c3d3865203e47e6208d8e8c3c5b3645c8979` | source3 `f920afaf9fdee6c9f2935706e83d7eae9554c7f4` pi: probe tagged custom input persistence |
| 4 | `3678354a7abf83678fd309ee25f4296f566cac37` | source4 `a0b898e4dbde142b0dd19148909c670ec187a9ce` pi: add host-managed session launcher |
| 5 | `314314c6b5785ddac9601947e8173501430cc3c0` | source5 `34929b6523285b8eff08dfff639e58e07213192a` deps: select the neutral conversation and question client; source48 flake.nix, flake.lock, portal/go.mod, portal/go.sum, nix/workspace-portal.nix |
| 6 | `56f71899381ef87a6dba40579f867d93f26ef3bd` | source6 `30941eaa1ad45f2b8f988b077b78c059fe135945` portal: establish unknown steer before grace recovery |
| 7 | `cc44e6094d1a66628b0e1289c8207f0a666c9584` | source7 `39a7b2ce3b3b7a6408c1e39a8c5cc51e6e7c4052` session: fence legacy writers from Pi backend state |
| 8 | `32e9e7ee6d93bbc11e40ceda0418a62f224a099e` | source8 `cdb11d5aa44d96ca3bb7342527373edb48abce1b` pi: add SDK worker and native acceptance receipt core |
| 9 | `2cf1e85225db90e435fa1da6790e332ce1c03698` | source9 `432b6acb5dfabce9f50cbaea5a276d0ea3f31ef6` pi: add provider policy and member settings coordination |
| 10 | `3ef02759a8b831650ee0d4f6ea904f74d1287610` | source10 `be88189c5b114b4e49bae9160caf1253184b2db7` pi: add typed team policy and inert reporting tools |
| 11 | `54c430f7e94d6055fc8298d4ff81b0f1bbf82c0f` | source11 `5cae9ea31c75c09cc9766719f20925b9196da47c` pi: retain optional question and Plan intent |
| 12 | `eb5782cb66e2419d9bd65aad23232658650151e0` | source12 `2165dff18e47674adb97fdc2c8140f7fcd6b7af6` pi: add scoped first-launch supervisor and controller |
| 13 | `0f2f6c3db36b08cb53bf4f9df4183cd1dd2629b6` | source13 `4385e1989eae53029334b302a8966be8fd12e478` pi: project canonical accounts for provider switches |
| 14 | `b14f45ba4adf819559b78c2586feaec50d1f5ba2` | source14 `4d500eb8caa959c5daef3fd47a1d70868939bbba` session: publish Pi creation authority with retained proof; source52 portal/internal/agentbackend/README.md |
| 15 | `aaa241e363bdec1a82f1c2cb112680f682282871` | source15 `37ae7bd8ccbc5607b611532e959ea08665833609` pi: add admitted team records and utility domain boundaries; source53 all owned hunks |
| 16 | `f2edcc2cf4c044123d91f3c413abeb05f31fd04d` | source16 `10a1c460e19838836d57c0735960832ca22ff642` pi: load explicit provider policy from installed packages |
| 17 | `aab4102613b1c00e63e97f5dd5b03105a04dc151` | source17 `a2a2693ec23499a78b25117920e8f2a978f42889` portal: validate immutable Pi provider configuration |
| 18 | `809b0c94d73d747e95d21426c49d8108ec9b7938` | source18 `79f5c059544f1e2e6075dbe05e4789d85af858a6` pi: define native routing evidence data contracts |
| 19 | `d3532ad61de3143b0f71e999dee138c4143af4f5` | source19 `9799127dc26d431f05c0d6a3d2589fb031546832` pi: compile native retry policy and decide bounded next hops |
| 20 | `68189c19c10d547de1b6efd62e6166aa5e9ad57f` | source20 `c3b1d25fc7726faaf9be392843611557e904d380` pi: package the SDK worker and provider configuration; source52 README.md |
| 21 | `1758ed3e9f074145a6f19e76012e1c2b0c4230c3` | source21 `a0c916235433035390029a70abcef6c2d992b2ce` pi: verify durable callbacks and tagged runtime records; source50 nix/tests/pi-worker.nix |
| 22 | `83284a22364d1affa72dff7f99474fbb30c45741` | source22 `ff53ba77730df5905b3c727c2e9ce5121b096a81` portal: compose Pi creation with the real runtime manager |
| 23 | `b911181a965f9eb4f6b7a2123a91b2480a24712b` | source23 `6451c11cbe7a40c9ac1936f87f0c30a10b7f19cc` pi: connect monitor utilities to the typed runtime API |
| 24 | `2d956fbc393ce3ed21085b4b6142aeada4dd7061` | source24 `4dc8819ea8ce934f9fabe27cf9b3672038e3de5f` pi: enforce explicit tool policies through the SDK |
| 25 | `38f09b1c1f96f1030cd02caec179f4a53706db9d` | source25 `dd4d1a9bfe2ab4ba08eb3ffaf04c1f265fe8eff2` pi: expose retained utility obligations for package preflight |
| 26 | `33a5cbccc6e04f7fbd4df12f311b382d89b85624` | source26 `880c8efdb37ba1940806ac95ac1b24e04092f907` pi: bind Plan and question actions to retained proof |
| 27 | `625b2838b10176f4820dc865c2ba1eef3b144835` | source27 `4361b0f1a80643de075fddd02de4887bb37f8cf2` communication: expose pure retained-record validation |
| 28 | `a1f27462da1c6b849502b7584823d4cfce39d787` | source28 `e25312258c1033711f43fc0ed008ffa91430ae6d` pi: share utility execution and enforce retained tool policy |
| 29 | `f9ebbe9722e7f78ff73cb9a782507f81f1479df8` | source29 `7d314da68c13f80d087e551ed2101778641d98ba` pi: prove native question and Plan receipt recovery |
| 30 | `9b14fbde3cafa50d5ff57038bd617fb0391ea6fb` | source30 `b2d71adcdd4f9ff5fdc342dd97ff1a06587c150c` portal: fence retained Pi team records during package transitions; source49 all owned hunks; source50 portal/cmd/workspace-portal/maintenance_startup_test.go, portal/cmd/workspace-portal/pi_team_preflight_test.go |
| 31 | `f2ca90f6e8f567611f6b7b15a9dba07a5fff7b4c` | source31 `450ad1164e98b68022e9a225bb804ed6b2a37f81` pi: add bounded public SDK native retry component |
| 32 | `f536b6ea968aac59730d07f196de6a802c8f9890` | source32 `87ff7d3bf0bfe39848234b56dd9930c73d323ec2` pi-runtime: retain explicit drained supervisor successors |
| 33 | `57afcaab41dfe6ad679071a9ae2f3f98e4b91e58` | source33 `9f1be5b0d4ba265dfcb966b26439315120525411` portal: project and render retained Pi workflows |
| 34 | `734f8382f3fc2e6b0d07680838ae90755adb5505` | source34 `ad707ed03f2bb832932ea410d84436f597c2f05f` portal: admit retained Pi team record operations |
| 35 | `86b37ad3977bf04f5e5ff9aac238baceba282834` | source35 `47bc2d9987db919104be5c68c7a8d064285d036e` pi-runtime: gate workflow observations with attachment barriers |
| 36 | `1a065cac169f83ffad834e0d059f1a1420062598` | source36 `fc308d34bc0c4414d2c3214ff5311cb0f4762cd9` pi: guard retained question plan and tool-policy records; root7f product/helper/refusal hunks |
| 37 | `f3904b7fd19756e9a6a69a10c0580d1b2750a22f` | source37 `253c5d3e42f3a75cb93d263967ba143de5552add` pi: expose checked submissions and retained runtime identity |
| 38 | `b8c7fc4228d30c1d429bc13f0cf815ab0d2680fa` | source38 `74d3ba8dc0f78ce4a7d1e2a4f62e60ab1a823952` session: decode complete Pi native routing metadata |
| 39 | `ded942c688d436467d6fabe934f534f9e0d2fdfc` | source39 `ad21d6b6d8d19580a87df2dc75d122e5296dc05e` portal: compose Pi question and Plan workflows; source51 all owned hunks |
| 40 | `3433999001511a8aefa6eb38d60475886ccd7345` | source40 `59db5bec1fe1c39f9b689f7ba7369f4055e307e9` session: publish the retained Pi workflow contract |
| 41 | `1abfd2a1f446010129caab296972055f89b52c8f` | source41 `509ca3dca6f90184a8ce9d8b0344846e3584b885` session: decode retained role instruction support |
| 42 | `613bdd705cc7f57d68609734358c1b87e049447d` | source42 `d94ff0f8b6965f69cbb0e661f34aa461d6ef8cb2` pi-runtime: retain and verify literal role instructions; source44 all owned hunks |
| 43 | `5e79de8c7fa5ee6af0277c9176c9b34f17056841` | source43 `f3b426ec5c9435ea08e8a55b85c000f2d8de8d9e` session: guard retained role instruction mappings; root7f role-dependent writer/CLI tests |
| 44 | `20c3f712556448dbe1c0a744e98490b1cb6bb593` | source45 `be12c6783ecb432d86ade6c3ac7a52bb899d05c0` portal: refuse unsupported Pi creation rosters; source46 all owned hunks; source47 all owned hunks |
| 45 | `e0925346dae8e862df518b3fecc6e857561c1000` | source48 `a936d9e92d666fb5fc242e57583f34c465bd0211` portal: align Pi transcript cursors and presentation; source48 C pin excluded here: folded once into final5 |

Every original53 commit is accounted: skipped standalone44 typed proof folds into
42 application;45 R2 combines46 caller and47 final declaration after43 target
inventory guard;49 Ruby fixtures and50 cmd fixtures fold into30 team guard;
50 worker golden folds into21 callback contract;51 legacy classifier/truthful
fixtures fold into39 workflows;52 A1 splits across1 runtime README,14 backend
contract README and20 root navigation;53 monitor parity folds into15 Pi events.
Source48 transcript remains one11-path adapter/cursor/presentation/test feature,
with its five pin hunks folded into early5. No duplicate R2 wait or new schema
alternative remains. Application plus fresh typed proof are one complete boundary;
caller/declaration follow full guards. No blind all-feature squash was used. The later7f correction has no standalone
obsolete fix step: product plus helper/refusals belong to final36, and assertions
using Instructions/HasInstructions plus CLI role claims belong to final43 after
the actual R4 field/guard definitions. The other43 stable patches are identical;
only those two logical patches changed in that root fold. Pre-H1 inventory
b6a6d899 compiled both owning Go packages with `-mod=readonly -run '^$'`;
no later R4 symbol was moved backward.

### Final C history and single five-file pin stream

H1 is an explicit lead-accepted immutable-source decision: original a883 corrects
superseded neutral bounds introduced in99ca. No known release, supported consumer
or persisted-state boundary requires that invalid intermediate contract. Feature
publication, fixture consumption and retained receipts alone do not justify it.
Unknown external use remains unknown. Original99ca/a2/a883 refs and all original
receipts remain frozen; none was rewritten or assigned a new identity.

Final C range dd90fb4308ba85617ee2a4267cc835aa9a4f11ce..5aa6111db1a71b17191befb8532bad7dcae2e15d
contains exactly TWO logical commits:

1. `462df77a3012395da737faaec44fd9ca10fcbfc1`: neutral API introduction99ca with
   final a883 constructor-specific cursor policy, docs and regression tests.
2. `5aa6111db1a71b17191befb8532bad7dcae2e15d`: unrelated a2 optional question-card
   presentation, with the original change preserved.

Final C treeca190011 and complete dd90..head binary patch are exactly olda883,
patch SHA256 `db392f56a765cb705962862c87b6d0bd282279d00d31c383168361e80b673f7c`.
Neutral-introduction compile passed before the question feature; no test symbol
was moved before its owning API. This removes the superseded C history step,
not a supported recovery path. Old C three-commit lineage remains available in
c-refs-before.txt, c.range-diff, original aliases and transcript/old packet receipts.

D's final5 dependency owner `314314c6b5785ddac9601947e8173501430cc3c0` introduces
ONE final selected C revision before requiring consumers. Older f9/a2/a883 pin
values are not additional steps in this candidate. Independent backend-guard,
worker/catalog packaging and all supported format boundaries remain. Final Go
version is `v0.0.0-20261113022749-5aa6111db1a7`; measured source NAR is
`sha256-yB28ZgZ8Bltyac5bPqgv5Dw6WNO3POWutn2WDNdeZ5s=`; actual vendorHash is
`sha256-IFn+OrUkIRjwpN7PRM8mNMO+lYrM9uaqY0COgC3UBIU=`. These are authentic
new-commit measurements, not values inferred from old tree equality. No unrelated
lock node/module/SDK/Codex/catalog pin, replace or local transport was introduced.
Final five-file SHA256 values:

| File | SHA256 |
| --- | --- |
| flake.nix | `3bffc0b993c7b4236bec8d0c56a1a1bda7ed13b879f5feecf3ea0bbb1352f527` |
| flake.lock | `358e08b3b35cb6dede0ed0b9e9981e5c80967b84b7d695b4e21a77d289531621` |
| portal/go.mod | `cd606f078dd6e17cd13533c93b280b54eb10c38a1136dd8523412bc71348ac81` |
| portal/go.sum | `c4e906f6ec3e2325126f88352763468dfdde4d5d56c2373d2e97683f120d868f` |
| nix/workspace-portal.nix | `d181f0bd9b2a57b87c7bfc49ba8d7bbd8129a5d650044f3a1b8036531c7eba26` |

### H1 history correction, publication and actual input evidence

Owner5's NEW registered C worktree is
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/codex-web-schema12-candidate`,
branch `2026-11-11-pi-codex-migration-schema12-candidate`, in canonical
repos/codex-web.git. Fresh canonical SSH observations/fetch found unchanged
masterdd90, featurea2 and transcript a883; no additional source/default delta was
silently imported. Ordinary Nix/tempfile-F commits preserve all old refs. Only
this NEW C feature ref was pushed normally over SSH, then ls-remote verified
exact5aa6111 and unchanged master/old feature/transcript refs. No force, old-ref
cutover or default integration occurred. Future publication must use fresh leases.

The actual Go origin hash is5aa6111, commit timestamp1794536869 (2026-11-13
02:27:49 UTC), and normal Go resolution produced the version above. Generated sum
is `h1:IBdS1tXavy/dBEKnBH6PPVm9EPEwRp7ZUmjiEKiIQR0=`; module-file sum is
`h1:z4to20c2m2G4k2YusCQCw3g7z1g63EugO4dmjTgo+dM=`. Nix freshly prefetched
that published immutable hash, measured the source NAR and all157 source files
against final C Git/worktree bytes. All157 downloaded Go module files also match;
no module file was missing and no replace/modfile/local transport was used.

Fresh installed-policy Luna/low watcher schema12_h1_vendor_watch used package
`/nix/store/0s5dljmmfngj7ia2r9lfkxwydnfiz6b6-dev-workspace-0.2.0`, catalog
f2d5a890, schema6/full_access/danger-full-access/never, native utility
dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569. It ran exactly one
vendor-discovery command against immutable source
`/nix/store/4i6gfd7x4wirsbrdjpcywdr2xmp6f4zp-source`: exact pre-H1 D archive,
four real new C pin files and a deliberate fake vendorHash. Expected exit1 in
17.431s reported actual `sha256-IFn+OrUkIRjwpN7PRM8mNMO+lYrM9uaqY0COgC3UBIU=`.
The mismatch is discovery evidence, not a passing build; it was not retried.

After installing that measured hash, final immutable source is
`/nix/store/4wi905mbwjybgraywy3yb1hkbwwnwj5m-source`, NAR
`sha256-0xKXuVzHkEBoW+6SrTprjn91f15hoLYLy1/PXcDN/LI=`. The matching warm
`nix build --impure --json --print-build-logs --out-link /tmp/pi-schema12-candidate.wwMbgc/h1/go-modules --expr '(builtins.getFlake "path:/nix/store/4wi905mbwjybgraywy3yb1hkbwwnwj5m-source").packages.x86_64-linux.dev-workspace.goModules'`
passed, with actual derivation
`/nix/store/d82sn33di4sl7b98qjnb8w9y91w6q57y-dev-workspace-0.2.0-go-modules.drv`
and output `/nix/store/cxmjffns15wa8kwqraflldfj2yqrp300-dev-workspace-0.2.0-go-modules`.
Parent independently verified output/out-link, measured its NAR equal to the
vendorHash and found the exact new version in modules.txt. No application/runtime,
SDK, VM, full suite or Ruby build was run.

Final D1006 committed/worktree files match all1006 immutable4wi files. Relative to
accepted387d, final D differs EXACTLY in the five pin files (8 additions/8 deletions),
with every other source byte and lock node unchanged. Full final D patch SHA256 is
`1f22c11a2f8750cd9cf3e75720439fe5e53c0f8f255defdddd27e384d39caa68`; old/new45
range-diff SHA256 is `47130d67346fc35d758957a03f5ed8fac51e02be5e5bfd6fa0aeea9a8bc88e97`.
Only logical5 changes dependency content. Packaging20 has identical zero-context
edits but a changed adjacent C URL context, so its stable patch-ID also changes;
the other43 stable patch-IDs match. Earlier full-file preimage/patch-ID assertions
stopped before accepting this known context difference; exact C-node/scalar
preimages and packaging edits were verified, preserving all later Pi additions.
No source/body inequality or substantive conflict occurred.

Required actual-pin quicks use declared Nix and readonly Go: pin checker plus
positive/negative fixtures; four TestAdapter cases (Accepted/Unknown subcases,
no skip),2.884s, from immutable4wi with the recorded PI_PROBE_PACKAGE; final main
consumer compile `./cmd/workspace-portal -run '^$'`,.051s; five focused neutral
cursor/browser-surface/legacy-constructor cases,.040s, from the actual downloaded
new Go module under C's own Nix environment. No broad unchanged C campaign ran.
Whole D/C whitespace and ordinary commit checks pass. An initial optional gofmt
check surfaced existing a883/99ca legacy_external_test.go formatting; its exact
SHA15602c9fde0af8872ac72c9ef1722a212a6f0f3a290d730e2c8ed1c0eb663319 is unchanged.
The failed check/log is preserved, with no source formatting change and no hook
bypass (neither repository declares an active hook framework).

The watcher also observed ONLY automatic C [Check run43352348596](https://github.com/aither64/codex-web/actions/runs/43352348596),
attempt1/exact5aa6111: completed/success, no launch/retry. Both watcher commands and
sessions39282/26028 are joined. CI does not replace review. Both isolated worktrees
are clean/index-empty; no D publication or primary/peer index/ref transfer occurred.

H1's new histories and generated inputs are ready for lead/reviewer assessment;
H1 stays OPEN pending accepted proof. Reviewer0's frozen387d/a883 source inspection
is not called a review of the new immutable identities. Lead supplies these exact
ranges for its H1/general-history/pin conclusion. No new database migration,
format transition, conversion, repair or rollback relaxation is added. Original
receipts, old-reader refusal, native3 exclusion and broader readiness limits remain.

### Accepted generic-root correction and exact source checks

[Canonical owning brief](design.md#generic-state-root-compatibility-settled-owning-correction)
and [the source/diagnostic transcript](review-transcript-evidence.md#generic-root-compatibility-successor-source-and-finite-checks)
record the actual supported producer/reader boundary. Existing host code and the
owning Pi Manager/directory writer can retain a safe generic0755 parent and create
private0700 Pi descendants/0600 records beneath it, whether Pi was absent or is now
present. Fixture-only0700 and absence-only fixes were rejected. This is not an
operator permission repair or a private-state format migration.

The product hunk changes only retained_conversation_inspection.go's generic-root
check: existing absolute/clean/canonical real directory, effective-user ownership,
owner rwx/access and no group/world write. Context and traversal accounting,
workspace validation and all private traversal remain. Starting at pi-runtime,
every visited private directory still requires exact0700/effective owner; mapping
records, schema1/2 whitelist, bounds, identities and postvalidated HasInstructions
are unchanged. Only already optional namespace ENOENT is absence; present malformed,
symlinked, inaccessible or unsafe private state remains refusal. No writer, API,
metadata, constructor, scanner-wide skip, creation or chmod was added.

Accepted direct7f contains exactly three paths (product22+/1-, reader tests175+,
existing CLI preflight tests86+). At the accepted pre-H1 root fold387d, all1006
committed blobs and worktree bytes were independently compared with immutable source
`/nix/store/dy8nhbdi4r78yw6iqq2dp62sxyiw158l-source`; every byte matches. Its NAR is
`sha256-nmFN4N94P566E8TcPe4HrycMOsoeRROAE0z7+BSnw74=`, source-manifest SHA256
`708f20574f49e278db9becbd037554fffd6400844f76bf7b07d3b1c9aafd2e01`.
Original root commit receipt SHA256 is
`e4ba2f6fa93ce1644e1befd1a605d0430c15bdbb80f0dabf35b5ada8e78394a6`.
At387d the source differed from the prior68s graph only in these three root paths.
H1 then changes only five pin files; all root/reader/preflight implementation and
fixture bytes remain unchanged. Reuse the17.821s root proof for that domain with
the final actual-pin compiles above; it is not a whole-new-source test or package
identity. No root/worker/SDK/VM batch was replayed.

Reuse the actual final17.821s immutable-source command, not another batch:
`nix develop /nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv --command go test -mod=readonly ./internal/piruntime ./cmd/workspace-portal -run '^(TestInspectRetainedConversations.*|TestPiTeamPreflight.*|TestPiWorkflow.*)$' -count=1 -json`,
from dy8's portal directory, UID/eUID1000, umask0022, explicit task TMPDIR. It passed
116 named cases/15top with zero skips/failures; package times .822s/3.797s. Tests
cover safe0700/0755 absence, present private state from actual NewManager and the
owning directory/record writer, schema1/2 and independent role/tool obligations,
refusals and unchanged paths/bytes/modes. Existing process-dispatched CLI tests
preserve original identities and omit private content. Writer fixtures establish
no native worker/Create proof.

Preserve RED14.678s reader0755 failures, the corrected undated-slug CLI fixture and
valid RED5.660s CLI0700 pass/0755 refusal, initial GREEN16.113s, and final17.821s in
the transcript. Earlier exactead7/1af5 guest diagnosis saw owned canonical0755 and
failed the direct scanner before registration. Its temporary diagnostic stop is
excluded. That diagnostic is not registration success, and unchanged1af5 is not a
corrected binary. Tree equality with dy8's source does not establish a new package,
derivation, input closure, installed generation or successful registration.

No unchanged final batch was rerun. The only additional source check here compiled
both owning packages at the earlier inventory commit after splitting role-dependent
tests; `go test -mod=readonly ... -run '^$' -count=1` passed (.013s/.057s, no tests
run). This verifies history dependency order only. Final formatting/whole whitespace
pass; ordinary Nix commits used tempfile-F, with no declared hook framework or
active non-sample hooks and no bypass. All isolated commands are joined, index is
empty and worktree clean.

### Settled monitor semantic join and finite checks

`AddPiEvent` keeps validateReport first and the existing immutable-slot loop next.
Exact same-slot replay returns unchanged; changed replay conflicts. Only afterward,
before ordering/ID/marshal/delivery/append, the exact upstream guard rejects new
terminal passed/failed with nonempty StillRunning, including literal `none` or
whitespace, with the same explanatory error. No trimming, historical-validation
rule, store/API/constructor or monitor activation was added. Existing initialLaunch
supplies current guidance only to new operations. Old Launch.Envelope, policy,
settings/incarnation/IDs and delivery context/message/envelope stay immutable.

Existing pi_policy_test.go now checks passed/failed empty vs nonempty, incomplete
with/without running identity, no rejected mutation, historical contradictory
DecodePiOperation/exact replay and changed conflict, new launch guidance and
original envelope stability. The first new test fixture incorrectly paired failed
with exit0 and omitted incomplete detail; validation correctly refused it
(0.661s). Corrected authoritative fixture status/detail, no production change;
focused new+existing legacy parity/replay cases passed0.703s. Historical records
remain readable/replayable, not normalized or retrofitted.

All changed tests use the existing declared D cached Nix environment and
`-mod=readonly`; no new runner/harness. Fresh installed-policy Luna/low watcher
schema12_quick_watch ran ONE batch from immutable combined-source archive37f7,
tree08f27552 (same source bytes as the preserved priorc658). Archive had no Git metadata, so
parent independently verified all1006 archived file blobs against priorc658 and
recorded their SHA256 in the preserved final-source-receipt.json; watcher did not claim that
identity independently. Batch exit0/about68s, log combined-quick.log:

- Actual owning role/source-embedded and workflow decoder cases passed0.085s.
- Owning `TestPiWorkflowMappingKeepsIndependentToolPolicyAndMemberInstructions`
  passed0.069s.
- Finite root solo/original role+goal/all three proof refusals/R2 unsupported
  roster/frozen preparation/FreshAcceptance original wait/historical teams and
  omission checks, plus upstream TestArchivePreparation family passed31.239s.
- Upstream maintenance worker-exit reinspection and active/activating polling
  cases passed two tests/209 assertions,3.043s.
- Parent-known quick follow-up covered exact actual legacy manifest classifier,
  durable workflow namespace and initial policy0.133s, plus real no-thread page/
  details/no native verification/no send regression0.113s. These were separate
  required cases absent from the main selector, not an unchanged batch replay.
- Final pin checker/positive-negative fixtures, Nix parse-only, A1/role link
  inspection, Go formatting and whole-range whitespace passed. Hooks were not
  bypassed; authored/amended messages used temporary files and ordinary commit-F.

For preserved387d and currente0925346, reuse this68s evidence only for unchanged test implementations
and exercised paths; it is not an all-final-source rerun. Its direct workflow-claim
case does not call the changed root scanner; role/workflow decoder, root creation,
archive and maintenance cases are unchanged. The exact final dy8 graph above
compiled/tested the root/preflight packages and behavior before H1; the new pin
checks above verify the changed module/input consumer graph. Neither result is a
new installed/runtime closure proof.

All watcher/cmd sessions completed:24460 plus direct focused sessions; no surviving
owned process, test, cell or index operation. There was no SDK/provider/model,
VM, broad full-web/Ruby suite, CI or package-build campaign. Prior SDK/R4/old-target
checks remain scoped to their original inputs. The combined embedded Go/Nix source
is new; identical vendor content or final-history tree does NOT reproduce a prior
derivation/input closure. Required combined installed/constructor/containment/
public root/browser/Codex/full TEAM checks remain separate lead-released gates.

### Formats, docs, review and corrected-package limits

Carry forward the FULL persisted-format inventory below, including actual runtime
1->2 successor and communication1->2 transformations, Pi4 original request/
receipt/journal/completion/tracking fences and schema1/2 owner separation. R4 adds
optional immutable literal `Instructions` only to retained schema2; nonempty is
bounded4096 UTF8 bytes/noNUL, present-empty/null is not legacy, schema1/utility2
cannot accept it. Omitted old mappings and completed original proof remain
readable. Explicit Create/current replay/load must preserve exact saved bytes and
fresh observed SDK digest; all three root publication proofs compare the original
role. Target capability `piRoleInstructions:1` requires full workflow/role guard
and cold/pending/held/retired/removed-member original-proof inventory. Rollback
must pass the actual guard; do not strip Instructions or reconstruct receipts.

The role decoder, application+typed proof, target guard and final caller/declaration
are complete in source, but not installed readiness. R1/R3/R5 changes bounded
neutral cursor/public row behavior without changing original receipt/digest/no-
resend. Supported Codex schema2 creating/no-thread pages remain readable but grant
no conversation/native mutation. No database migration or Codex->Pi conversion
was added; the initiative is not format-transition-free. Source/fixture consumption
is known; no default integration/deployment/profile activation is recorded and
unknown external consumption remains unknown.

A1's README/runtime/backend navigation and factual readiness corrections are all
present, along with later role/downgrade docs/pi-runtime.md and pi-questions.md.
The earlier documentation reader/class/fidelity inventory remains authoritative;
this addition records literal-role reference/recovery and actual target refusal
with P3/R4 source evidence. No new product-visible prose beyond approved source
was authored. For the root correction, the owning technical comment explains
the generic/private distinction;
temporary diagnosis, exact source and execution limits belong in this packet and
transcript. Existing documentation routing/fidelity inventory remains unchanged.

The exactead7 guest failure has an evidenced root-compatibility disposition and
the accepted product correction is folded once in this complete intended source.
The candidate remains PROVISIONAL pending final reviewer0 and separately released
new-package original registration/_activate/service-readiness, creation and broader
final checks. Scanner/unit success is insufficient for those gates. No temporary
diagnostic stop, VM setup change, guessed permission fix or whole-file replacement
entered the candidate. No runtime/SDK/VM/full-suite/CI rebuild or push was performed.
Rollback still uses the actual compatibility guard; no receipt reconstruction,
Instructions stripping, namespace repair or chmod is introduced.

Native d3/234 work is retained/excluded, not canceled; native3/production route/
original lifetime/Accepted/currentgen/effect authority and TEAM remain unfinished
separate scope. No positive native3 metadata is emitted by this candidate. The
existing team schema2 capability is codec/guard support, not full TEAM activation.

H1 does not change any supported format, constructor behavior, documentation
content or public API: C final content is exactly a883. The only new identities
are its consolidated source history and the actual corresponding D pin graph.
Old C99ca/a2/a883 and D387d remain provenance, not final selected sources.

Raw evidence home: `/tmp/pi-schema12-candidate.wwMbgc/`, including frozen input/
remote refs, fixed/refreshed/consolidated full patches, source53 and final45 maps,
full range-diffs, source1006-hash receipt and quick log. New root-fold/ retains
old/new45 map, exact accepted/split/final patches, final1006 source receipt and
boundary compile log; older receipts are unchanged. H1 evidence is under h1/: C2
equality/publication, actual Go/Nix/vendor inputs, final D45 map/source1006 receipt
and scoped quick/CI logs. Key SHA256 values:

| Receipt | SHA256 |
| --- | --- |
| h1/final-receipt.json | `c1740687d260b6ccb014e3064349cdfddbce7559dd13b759796ea55f4f5b2406` |
| h1/d-final.patch | `1f22c11a2f8750cd9cf3e75720439fe5e53c0f8f255defdddd27e384d39caa68` |
| h1/d.range-diff | `47130d67346fc35d758957a03f5ed8fac51e02be5e5bfd6fa0aeea9a8bc88e97` |
| root-fold/final-receipt.json | `c0e64cdb167fc1b77046e32ba9af93e897f33f44bf1984a113f1f8e5e074d265` |
| root-fold/final.patch (same as direct7f) | `664cc3c937727f12b1fc9bb43c6735328067ea19d1341ec0756eb269557717fe` |
| root-fold/fold.range-diff | `be0d9dc0801da7d9bb3945696929103037b519035cca5c35add67ad2181058b2` |
| final-source-receipt.json | `641bdd94a15a387e5182729fd3cab70d0883a982a24bf9c23ff41bd9df5591c6` |
| consolidation-map-progress.json | `a6d50b6422b6284aa8b39cfcc4fc0b6ec44678b879a3d93332c795b785358d62` |
| combined-quick.log | `9616b7fa6bc0697622d7758c48799f714461b9ec7c9bf855614d9a45f25c230b` |
| fixed-to-refreshed upstream patch | `69bec008fbf604660618fd37c39f06b8e5b6a23e7fa8111eeb2c0690b9500a22` |
| monitor semantic join patch | `66f6c84124ca8cf0d42e31bb0e4ef2891fcbce545c82b00ee6b1193c0c50095f` |
| C dd90..a883 final patch | `db392f56a765cb705962862c87b6d0bd282279d00d31c383168361e80b673f7c` |

Lead accepts packet/source and invokes same independent reviewer0 for the affected
monitor/root joins, H1 C-history/new-pin proof, explicit whole-branch
history/migration/repeated-stream and
applicable high-risk lanes. No self-review or equality-only review exemption:
refresh, monitor join and root correction are substantive. No readiness, push, cutover, default
integration, deployment or lifecycle/session closure is authorized by this package.

---

## Historical R review/source packet (preserved)

The following sections describe their explicit original graphs. Their R/a2
headings and prior pending/complete review status are historical, not the current
candidate target or proof of its combined closure.

## Status and review boundary

The fixed-base reconstruction and separately owned upstream refresh are complete.
This packet binds final D `cd5fd5cbc9670311d411466de8ec63ff670d53b0` on exact
`db4b0fa62633b925e1917ec880737e1776f82cc8`, plus unchanged final C a2. It is
submitted for lead packet acceptance, **not an independent review or a final
merge-readiness claim**. Owner5 used retained Sol/xhigh/workspace_write;
reviewer0 remains the proposed independent retained Sol/xhigh reviewer. Lead
verifies eligibility, accepts the source/check packet and invokes final review.
No self-review, primary cutover, publication or integration is claimed.

The user authorized initial opt-in Pi implementation after the assessment.
Preserve current portal behavior, writable existing Codex sessions and their
original recovery contracts. Pi uses one development-session cgroup/mount namespace
with its member workers/tools inside; no agent host shared across sessions.
Providers inherit the session default with exact member/incarnation overrides;
canonical shared Pi auth does not imply shared histories/settings. Questions stay
nonblocking and durable; Plan is available only with proved tool enforcement.
Provider fallback remains required overall but unsafe redispatch is forbidden.

The committed deliverable is opt-in schema1/2 source plus finite components:
backend identity/admission, creation, SDK workers/host launcher, canonical provider
settings, typed team/utility domain records, callbacks/tool policy, durable
question/Plan workflows, observation and package guards. Native schema3 core/
writer/transport/authority WIP is EXCLUDED. A native metadata decoder, pure planner
or SDK leaf does not establish that capability. Installation, actual full-team/
monitor/communication/observer behavior and physical-provider readiness remain
gates, not results supplied by this packet.

Non-goals: migration/conversion of Codex sessions to Pi, Codex removal, default
backend/provider switches, portal redesign, credential copying/import, login,
real provider/model calls, a classifier service, another retry ledger/engine,
SDK fork, activation, deployment, cleanup or lifecycle action. Retain ambiguous
results as Unknown/held; never resend an original input to repair evidence.

## Exact repositories, worktrees and source identities

| Repository | Fixed base | Old completed tip | Isolated prepared tip | Final tree |
| --- | --- | --- | --- | --- |
| D fixed-base reconstruction | `6587c4c1cedabee95bcc52f4667e7d33e3a82859` | `d4e15e9d6b36fb2c4f4ff93e4f68a290494e265b` | `acdff31637afce84b0f28e5795434b983b58161a` | `fa1be7fab0b6c49d0121602497cb716b0ebd8c33` old = prepared |
| D final refreshed review source | `db4b0fa62633b925e1917ec880737e1776f82cc8` | `acdff31637afce84b0f28e5795434b983b58161a` on6587 | `cd5fd5cbc9670311d411466de8ec63ff670d53b0` | `4c968c5c178ca136c0b60e2a35859a89d507bcac` DISTINCT from old |
| C codex-web | `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce` | `a2b58b5e8d5c59cb448453e113b5dd48b20c3477` | unchanged | `18dca609c3847283f615982236d6f2e65f789bf0` |

D base tree is `761df9a749fb1d88bd694c10fcb834b11b6fe266`; C base tree is
`c294e99dfc86ac44ded7804fae686a98af2971ae`. Fixed-base D diff:309 files,
47433 insertions/362 deletions. Final refreshed db4..R:311 files,47437 insertions/
365 deletions. C: 22 files, 2157 insertions/309 deletions. These
sizes make scope/proportionality an explicit review concern, not a waived gate.

All paths below are under `/home/aither/workspace/ai/vpsfree.cz/`:

- Primary D `worktrees/2026-11-11-pi-codex-migration/dev-workspace`, branch
  `2026-11-11-pi-codex-migration`, stays at old d4; its native WIP is excluded.
- Isolated D `worktrees/2026-11-11-pi-codex-migration/dev-workspace-history`, branch
  `2026-11-11-pi-codex-migration-history`, at acdff; separate index, clean.
- Final refreshed D `worktrees/2026-11-11-pi-codex-migration/dev-workspace-refresh`,
  branch `2026-11-11-pi-codex-migration-upstream-refresh`, at cd5fd, clean/index empty.
- C `worktrees/2026-11-11-pi-codex-migration/codex-web`, original branch, a2, clean.
- Coordination: [plan](plan.md), [state](state.md), [design](design.md),
  [implementation plan](implementation-plan.md) and
  [contracts](implementation-contracts.md). Lead owns state and allocation.

### Remote observation and two separate preparation steps

SSH `ls-remote --symref` plus fetch observed D feature
`0af8ac84bdad55ad44e14a5d840c1ccdebcb6845`, D master
`db4b0fa62633b925e1917ec880737e1776f82cc8`; C feature a2 and C master dd90.
Both remotes are the exact `git@github.com:aither64/<repository>.git` URLs.
Neither completed feature tip is merged into the observed remote default.
D's db4 contains `02881b40` plus `db4b0fa6` beyond fixed6587: repository-review
metadata/count loading behavior, 22 files / 731 additions / 104 deletions. It
includes app.js, session template and documentation overlaps. They were
NOT incorporated during the fixed-base equal-tree reconstruction. Lead then
separately released owner2/owner4 refresh; that step now includes exact db4 and
its compatibility effects, documented below. The fixed-base equality result is
retained independently and is not called equality of the refreshed tree.

Preserved local refs, never deleted:

- D `refs/heads/2026-11-11-pi-codex-migration-history-backup-d4e15e9d` -> old d4.
- C `refs/heads/2026-11-11-pi-codex-migration-history-backup-a2b58b5e` -> a2.
- C `refs/heads/2026-11-11-pi-codex-migration-source-f9b9b483` ->
  `f9b9b4831b23aab5ddf61316eefdd02edca1cc7c`, the obsolete source still required
  by original build receipts. The original primary D/C feature refs are unchanged.

No primary ref cutover or push is granted. The observed feature values above are
only publication lease baselines; later publication must refresh them and use
an explicit exact remote lease. The historical parked acd tip preserves the published
0af prefix; the FINAL refreshed R rebases the first four commits too and does
NOT preserve0af ancestry. Publication of R requires the appropriate explicit
observed remote lease; do not infer a fast-forward from the parked-tip proof. C
already has the final published source; do not republish it unnecessarily.

## Complete history and dispositions

Step A has43 old commits and40 parked logical commits. Only in this fixed-base
step are the first four commits preserved verbatim. For each remaining ordinary replay, stable patch ID equality
was verified. The table's old/new indices define both complete ordered series;
folded rows name the same owning new commit and introduce no extra new entry.

| Original # | Original full commit | Parked # | Parked full commit | Purpose and disposition |
| --- | --- | --- | --- | --- |
| 1 | `ab9ce9234fe2b1f80367b7bb1836a81925b2a034` | 1 | `ab9ce9234fe2b1f80367b7bb1836a81925b2a034` | pi: add finite worker conformance probes — same patch |
| 2 | `063c4a4b151aff3d8d8d16712c688e4a9fa9ac9c` | 2 | `063c4a4b151aff3d8d8d16712c688e4a9fa9ac9c` | session: add strict Pi backend identity readers — same patch |
| 3 | `0af8ac84bdad55ad44e14a5d840c1ccdebcb6845` | 3 | `0af8ac84bdad55ad44e14a5d840c1ccdebcb6845` | pi: probe tagged custom input persistence — same patch |
| 4 | `23b35d5368a27bd189ef7b895dbbfbde4dc0d331` | 4 | `23b35d5368a27bd189ef7b895dbbfbde4dc0d331` | pi: add host-managed session launcher — same patch |
| 5 | `46fd1886ebebd20caba792d3aea218c42556f857` | 5 | `54cbe2aa81f44c77ee7a147b9a6c19c855145a2e` | deps: select the neutral conversation backend client — final-only C pin |
| 6 | `4f390101de7ca5047d9e41faa0b483088d591185` | 6 | `2c660da833a66792389fc87b959a0927cd83bd72` | portal: establish unknown steer before grace recovery — same patch |
| 7 | `67e08f2f10faa288aefb7e97e2d3eb19d8819eb6` | 7 | `0051d317e542b684eb1b1b9e5804c9427ef911dd` | session: fence legacy writers from Pi backend state — same patch |
| 8 | `daa780d1781df025aa918970310f4fb0f5f66a83` | 8 | `e7f91048e6018317d1b261ad5a6851d11e3caa5d` | pi: add SDK worker and native acceptance receipt core — same patch |
| 9 | `f8cd2941626eac5fbe8e12c4e5a3fee9e309735a` | 9 | `b89007abdf262db64a0cdaf6c742d7ffb497f757` | pi: add provider policy and member settings coordination — owning commit + folded fix |
| 10 | `7584b9077b84c4a7e40d6c8da13f9571d40c9126` | 10 | `96249ff92fc441d4661d4db436c370c141d8a1ae` | pi: add typed team policy and inert reporting tools — same patch |
| 11 | `9a4f44e9c64106bc36d65fead1be881412c778c3` | 11 | `1e9e81cded8d0a991ea0da185e8216e2880cccd6` | pi: retain optional question and Plan intent — same patch |
| 12 | `fc02306ab8e66f85fdae06519b1c907dc1728120` | 9 | `b89007abdf262db64a0cdaf6c742d7ffb497f757` | pi: validate provider policy against execution identities — folded owning fix |
| 13 | `a74ae62bfb57cdb1858381a8c66855e2ab9f2b5b` | 12 | `ff179e8f871e64b73aca3cae43cceceedb986e64` | pi: add scoped first-launch supervisor and controller — same patch |
| 14 | `6a3631ef6ee225d7c532f62bd5f0222bb6fc582d` | 13 | `c1c955af06cbfc2c4af492bd4b22be136a25b5b4` | pi: project canonical accounts for provider switches — same patch |
| 15 | `a12c01ee4babf72cf0994d6b49f2f8b834e2be5e` | 14 | `66d6aec834940b1dd2a587ad06f9df77f5937b73` | session: publish Pi creation authority with retained proof — same patch |
| 16 | `e457834e23a2bda09e528ac8c532c16e912c33b2` | 15 | `22415d56b4bcb8546102ca407f79239ee8dfb1d3` | pi: add admitted team records and utility domain boundaries — owning commit + folded fix |
| 17 | `2ced04211af1b9fd22ab77ded1af69aaacb15aed` | 16 | `be09cfdaf8e58a6998d6c3a0156518486641395b` | pi: load explicit provider policy from installed packages — same patch |
| 18 | `558e710232a59c55042a615ac83e5bdda2a9e390` | 17 | `99e7f9eada9b48be78da866cd60ecf9996c5b31e` | portal: validate immutable Pi provider configuration — same patch |
| 19 | `adfde64148b5dc715d972c5782dd60f1bcd49e6b` | 18 | `cb74aa631f800df297944bceb9dc9ca983b0bd40` | pi: define native routing evidence data contracts — same patch |
| 20 | `11888bcb6e37eaffe1cc0f3c99b92b4ccdf34e11` | 19 | `79a6677a8a305636d93768a8d3d4e9f88c3bf202` | pi: compile native retry policy and decide bounded next hops — owning commit + folded fix |
| 21 | `563f6be3ae0498c4b4e9d5fffe0c8844f4555e75` | 20 | `4e3d8438c8ce72c30e26713908c8b731243a44ac` | pi: package the SDK worker and provider configuration — worker packaging; superseded pin removed |
| 22 | `2dd2af9499fa64602bfce94c20a17b6e41139eca` | 21 | `46374d163221248c97a126e5c8c9891df051522d` | pi: verify durable callbacks and tagged runtime records — same patch |
| 23 | `6d2730282d871383dfc56d05143830e29ecfe619` | 22 | `da43d09bcfbaee2eae3150d75515cda8143eedc6` | portal: compose Pi creation with the real runtime manager — same patch |
| 24 | `0e8c0fb5b1357a3810df9f35b1dfe040a874fa41` | 23 | `20e98dd843ac72a8c4b4be0f19219c71ecbc5aee` | pi: connect monitor utilities to the typed runtime API — same patch |
| 25 | `fa43219096e3e8b9e5002cb28efccadf73a1a2ce` | 24 | `75ee4098dc65f1f1068d48b0880feaaa2745d83e` | pi: enforce explicit tool policies through the SDK — same patch |
| 26 | `1eeecfb575220d7f8d152bc42b6b9e91c77c995b` | 15 | `22415d56b4bcb8546102ca407f79239ee8dfb1d3` | teamruntime: preserve original Pi creation receipt references — folded owning fix |
| 27 | `e4b9f861f14c5f6fa803c320e4e66e71cca866f4` | 25 | `4618bbd86075ef3f87ee751b2382ec12d9082b32` | pi: expose retained utility obligations for package preflight — same patch |
| 28 | `74c5646455e1e40f03732347c5eb567dd90d8fbc` | 26 | `06622ac81c6bb0dd7937c122934c061268ac9297` | pi: bind Plan and question actions to retained proof — same patch |
| 29 | `0a647bdfcdfbf900b614cec7935f147dba79997d` | 27 | `cc6d6e159ce34678cdeae562954ebb84645042ff` | communication: expose pure retained-record validation — same patch |
| 30 | `4c0bd9a0f97c15de76d45e8c5fe54a31ef7afce2` | 28 | `af14f6a518f3277e6589159e67c32e04bce08692` | pi: share utility execution and enforce retained tool policy — same patch |
| 31 | `94b4d58480d7545dfd8ddda02872b6e536c42f24` | 29 | `681a3c8b82b89a918bf8e4645a46eefaa51491f6` | pi: prove native question and Plan receipt recovery — same patch |
| 32 | `3872155b55688742355b8dc16b88584f4cb5a303` | 30 | `79f3b7df3e6277dac2c49962189efbd59827fd77` | portal: fence retained Pi team records during package transitions — same patch |
| 33 | `aec5bea24c6a1bf18dd5c7941617286c869e4c7d` | 31 | `0afefb1f37c8e7a5a52a4a2d04396d4875f9515a` | pi: add bounded public SDK native retry component — same patch |
| 34 | `cf3997b35fd1e40208e66437888d4b7d6a71916d` | 32 | `cc69cb7c2d63942db06f581d0cc18af321ec5cca` | pi-runtime: retain explicit drained supervisor successors — same patch |
| 35 | `d681233ed7c143994745a11968dec75a2b16e3c0` | 33 | `6a3797f89a9ea570321ace3864472221b41c6975` | portal: project and render retained Pi workflows — same patch |
| 36 | `bd329bb9775db45351db639044328546c7dae72e` | 34 | `e47c00510592faa66f45b6d9592ab60793dac0f8` | portal: admit retained Pi team record operations — same patch |
| 37 | `6b64c7447674340db63b96c1c07cbc2b13878748` | 35 | `6cde431fc7e0eda3a4eefc71d9ccc066fc2bae8d` | pi-runtime: gate workflow observations with attachment barriers — same patch |
| 38 | `3318ca32392444167c4369ecd8cd17891bdaa4ce` | 36 | `e95a0b28870bbae23117f3d05058a14264c102c4` | pi: guard retained question plan and tool-policy records — same patch |
| 39 | `7e6229da4745db05484864107c03a9c72ab06dfc` | 37 | `e3c32a42703c09a5c8b7596fcadfc74b0bf27984` | pi: expose checked submissions and retained runtime identity — same patch |
| 40 | `699d8f85b20b89772fbcb4d49ecccfb6d24b8f75` | 19 | `79a6677a8a305636d93768a8d3d4e9f88c3bf202` | pi: preserve empty retry categories in compiled virtual policies — folded owning fix |
| 41 | `329bd4910082d3cfb4d2fe7b04743f0c5e8d4603` | 38 | `8fb1ed70aa4dd00182fcd89962c206241627ecd2` | session: decode complete Pi native routing metadata — same patch |
| 42 | `25af2aba72f6f45570cc56d5269c3d9ec44fbbf9` | 39 | `deb41926586020499fd95b561c31398e9e6c9b00` | portal: compose Pi question and Plan workflows — same patch |
| 43 | `d4e15e9d6b36fb2c4f4ff93e4f68a290494e265b` | 40 | `acdff31637afce84b0f28e5795434b983b58161a` | session: publish the retained Pi workflow contract — same patch |

C remains exactly two logical commits in order, with no new rewrite:

1. `99ca5d26827e3eb4f6a7d6d87b4fb4af22f735c7`: neutral conversation/backend
   adaptation, preserving the public Codex API/authority and nullable slots.
2. `a2b58b5e8d5c59cb448453e113b5dd48b20c3477`: optional shared question-card
   presentation. Pi-specific durable state and routing remain D-owned.

## Final refreshed review source: step B

Owner2/owner4 separately refreshed parked acd onto exact db4, without touching the
primary d4/native WIP or parked acd ref. Initial ordinary hooked rebase produced
`fe384323fbab2722b5a5fb3b7e0e520f6fd80ac4`: all40 range-diff entries were `=`
and all980 non-upstream blobs were unchanged. There were **no textual conflicts**.
Owner2 then added only the three required template app cache tokens v70 and the
lead-approved one-line negative-catalog fixture setup. Temporary fixup
`9acbccb97e3b22e8a838711dacd7711f392f8e7a` was autosquashed into owning central
commit39, now `37b696c5f426ed048b40f791c08cfa1eae3b7172`. Its pre-fold tree equals
final R exactly; all1002 source hashes were preserved through that history fold.
There is no leftover fixup/cache-token update stream. Other39 final patches remain
stable-identical to their parked counterparts.

### Complete ordered final D series

Read this table together with Step A's original43->parked40 table: every original
commit, folded correction and final refreshed commit has an explicit disposition.
C's two-commit list above is unchanged. Only final row39 has a changed patch.

| # | Parked full commit | Final refreshed full commit | Refresh disposition |
| --- | --- | --- | --- |
| 1 | `ab9ce9234fe2b1f80367b7bb1836a81925b2a034` | `7605971b4f0dbb7d56168d4fd0ea87583ace0ea1` | same stable patch |
| 2 | `063c4a4b151aff3d8d8d16712c688e4a9fa9ac9c` | `af31696c4a7c8eb7e8a10c28708e0fd5499c186b` | same stable patch |
| 3 | `0af8ac84bdad55ad44e14a5d840c1ccdebcb6845` | `b76df2b280d6a5292a0b2d62a4444de20124f44a` | same stable patch |
| 4 | `23b35d5368a27bd189ef7b895dbbfbde4dc0d331` | `a61537fd9007b7cd238f01da12f53f47395fe827` | same stable patch |
| 5 | `54cbe2aa81f44c77ee7a147b9a6c19c855145a2e` | `be9e7d7b5ad70161148cd0efd4c5b6890ccd0a7a` | same stable patch |
| 6 | `2c660da833a66792389fc87b959a0927cd83bd72` | `957acd4020f066bc6372735f7f8af5d91b8d3f82` | same stable patch |
| 7 | `0051d317e542b684eb1b1b9e5804c9427ef911dd` | `86073c57b776349f96978428463780de0dae2ce1` | same stable patch |
| 8 | `e7f91048e6018317d1b261ad5a6851d11e3caa5d` | `615430c33c81fd94622f2115bdb28e03c6fd334d` | same stable patch |
| 9 | `b89007abdf262db64a0cdaf6c742d7ffb497f757` | `2e7e9b524d1957eb43ddfa8f233676fd144d2931` | same stable patch |
| 10 | `96249ff92fc441d4661d4db436c370c141d8a1ae` | `ed2f826b14da6e4fb8eb0c597d248bd40027eaa6` | same stable patch |
| 11 | `1e9e81cded8d0a991ea0da185e8216e2880cccd6` | `e8b1df465f74c940527c99940f9b1e078af04e3f` | same stable patch |
| 12 | `ff179e8f871e64b73aca3cae43cceceedb986e64` | `0b526b60a5a9495f281ce3080dd40e3b3a150fae` | same stable patch |
| 13 | `c1c955af06cbfc2c4af492bd4b22be136a25b5b4` | `fc02fc2df0162b9cb5269d0ac97e3295ad582021` | same stable patch |
| 14 | `66d6aec834940b1dd2a587ad06f9df77f5937b73` | `0245e4c8b56098a92a0ab2f7f1d36e1908e07ede` | same stable patch |
| 15 | `22415d56b4bcb8546102ca407f79239ee8dfb1d3` | `a231feeaa1e8ad4952c03abb05a8c31d9bc2cd73` | same stable patch |
| 16 | `be09cfdaf8e58a6998d6c3a0156518486641395b` | `4a0ecd4d62ded39b5600a29cfaa4365879507145` | same stable patch |
| 17 | `99e7f9eada9b48be78da866cd60ecf9996c5b31e` | `94d3d236dd94fd0f5892f7a5d64769255945b315` | same stable patch |
| 18 | `cb74aa631f800df297944bceb9dc9ca983b0bd40` | `a20a9210d1a300a3a3e9a0dd5bf029bfec52787d` | same stable patch |
| 19 | `79a6677a8a305636d93768a8d3d4e9f88c3bf202` | `bccd64d18a1e649befb0f1d888fa4243f23d99e7` | same stable patch |
| 20 | `4e3d8438c8ce72c30e26713908c8b731243a44ac` | `12cc3910f2cb40394c451e6c8a58d39ca0b289cb` | same stable patch |
| 21 | `46374d163221248c97a126e5c8c9891df051522d` | `9089aeaf024513d4c7595555fca38cb266b9053c` | same stable patch |
| 22 | `da43d09bcfbaee2eae3150d75515cda8143eedc6` | `48e3a46c4758a13a8d9c0483977f29dded7f343f` | same stable patch |
| 23 | `20e98dd843ac72a8c4b4be0f19219c71ecbc5aee` | `f3cd24aea4d672ac8103e9e5a9cbb1ff36c3bd32` | same stable patch |
| 24 | `75ee4098dc65f1f1068d48b0880feaaa2745d83e` | `2d2b2e0b50edb84003ae8d9efea75a38e4f37ba3` | same stable patch |
| 25 | `4618bbd86075ef3f87ee751b2382ec12d9082b32` | `5da375aabea9c80e9b41f9c1179fd16b37484158` | same stable patch |
| 26 | `06622ac81c6bb0dd7937c122934c061268ac9297` | `1c64b37f7097b64dd5aeae1a4ffbb5f2367ebd5d` | same stable patch |
| 27 | `cc6d6e159ce34678cdeae562954ebb84645042ff` | `f9a90294ca84beae352ddfa1bb1d094edc1486f3` | same stable patch |
| 28 | `af14f6a518f3277e6589159e67c32e04bce08692` | `7c8e29932fc5867d29e99d119278b1b6902c543e` | same stable patch |
| 29 | `681a3c8b82b89a918bf8e4645a46eefaa51491f6` | `47a9e4d34a819a6447d201430187a51ae3a05b5a` | same stable patch |
| 30 | `79f3b7df3e6277dac2c49962189efbd59827fd77` | `93cf438fff52b8453bd5d3bfd7c740e1039c0ce4` | same stable patch |
| 31 | `0afefb1f37c8e7a5a52a4a2d04396d4875f9515a` | `0b7394eea0cef6548a5a7770ec9ba55305e24260` | same stable patch |
| 32 | `cc69cb7c2d63942db06f581d0cc18af321ec5cca` | `f072aa1c98ca00057b7546e2600c5fdbabda5361` | same stable patch |
| 33 | `6a3797f89a9ea570321ace3864472221b41c6975` | `a922bb21b2dc40889ddb55c59174cbe17e74e7a7` | same stable patch |
| 34 | `e47c00510592faa66f45b6d9592ab60793dac0f8` | `111b11d4eeeffebade0c305a90cf5b141c12fae7` | same stable patch |
| 35 | `6cde431fc7e0eda3a4eefc71d9ccc066fc2bae8d` | `d866de6fe23d8800985bab86b25433a596efa4fc` | same stable patch |
| 36 | `e95a0b28870bbae23117f3d05058a14264c102c4` | `3bb2022c3671e8e533bcff44f9da97e3ac00e9e8` | same stable patch |
| 37 | `e3c32a42703c09a5c8b7596fcadfc74b0bf27984` | `5bf47d4356fd604d69f567b5022f3a135a946e5c` | same stable patch |
| 38 | `8fb1ed70aa4dd00182fcd89962c206241627ecd2` | `2c75d23277c9085621940bcea0e08d1d3b191b23` | same stable patch |
| 39 | `deb41926586020499fd95b561c31398e9e6c9b00` | `37b696c5f426ed048b40f791c08cfa1eae3b7172` | central source plus3 cachev70 tokens and approved one-line negative fixture; no production behavior rewrite |
| 40 | `acdff31637afce84b0f28e5795434b983b58161a` | `cd5fd5cbc9670311d411466de8ec63ff670d53b0` | same stable patch |

### Complete old-parked-to-final changed-path and hunk dispositions

Exactly23 paths differ between acd and R: the22 upstream paths plus the one
negative fixture setup. The only manual delta from initial fe384 is four lines:
three `/static/app.js?v=69` -> `v=70` tokens and `s.installedTeams = nil` immediately
before the existing missing-saved-access negative assertion. The shared fixture
now supplies a valid catalog, so that last negative case must explicitly remove
it. Production access validation and the assertion remain unchanged. These four
lines are folded into central39; no new schemas, pins, native source, visible
prose or errors are introduced by the refresh correction.

| Path | Final disposition |
| --- | --- |
| `README.md` | automatic merge; verbatim upstream repository documentation plus unchanged approved Pi sections |
| `docs/workspace-portal.md` | automatic merge; verbatim upstream repository documentation plus unchanged approved Pi sections |
| `portal/internal/repository/review.go` | byte-identical exactdb4 upstream source/test |
| `portal/internal/repository/review_counts_test.go` | byte-identical exactdb4 upstream source/test |
| `portal/internal/repository/review_diff.go` | byte-identical exactdb4 upstream source/test |
| `portal/internal/repository/review_diff_test.go` | byte-identical exactdb4 upstream source/test |
| `portal/internal/repository/review_followup_test.go` | byte-identical exactdb4 upstream source/test |
| `portal/internal/repository/review_summary_test.go` | byte-identical exactdb4 upstream source/test |
| `portal/internal/repository/review_test.go` | byte-identical exactdb4 upstream source/test |
| `portal/internal/web/pi_team_admission_test.go` | approved one-line negative-catalog fixture setup, folded into owning central39 |
| `portal/internal/web/repository_metadata_test.go` | byte-identical exactdb4 upstream source/test |
| `portal/internal/web/repository_review.go` | byte-identical exactdb4 upstream source/test |
| `portal/internal/web/repository_review_browser_test.cjs` | byte-identical exactdb4 upstream source/test |
| `portal/internal/web/repository_review_followup_test.go` | byte-identical exactdb4 upstream source/test |
| `portal/internal/web/repository_review_live_browser_test.cjs` | byte-identical exactdb4 upstream source/test |
| `portal/internal/web/repository_review_parents_test.go` | byte-identical exactdb4 upstream source/test |
| `portal/internal/web/repository_review_test.go` | byte-identical exactdb4 upstream source/test |
| `portal/internal/web/repository_summary_test.go` | byte-identical exactdb4 upstream source/test |
| `portal/internal/web/static/app.js` | automatic merge; only repository-review importv9->11 beyond frozen frontend5451 |
| `portal/internal/web/static/repository-review.js` | byte-identical exactdb4 upstream source/test |
| `portal/internal/web/templates/automatic-archival.html` | fresh app cachev70; session retains original Pi/Codex carriers and controls |
| `portal/internal/web/templates/index.html` | fresh app cachev70; session retains original Pi/Codex carriers and controls |
| `portal/internal/web/templates/session.html` | fresh app cachev70; session retains original Pi/Codex carriers and controls |

The frozen Pi/Codex app body is unchanged except the repository-review dynamic
import v9->v11. The module itself is exactly upstream db4 blob
`952f3c9ffcff874c2fe19c30e6e276bdf90af894`, SHA256
`bb400f673d39967f8b602cd0422422b7c6009f9483f73d13c83027baf2d5c5d8`.
The three template SHA256 values and all six frontend/fixture hashes are in the
frontend receipt and match R. Automatically combined README/docs retain exact
upstream repository guidance plus previously approved Pi copy; lead approved no
new prose rewrite. No supported recovery instruction was retired.

**Protocol compatibility impact exists despite unchanged persisted descriptors.**
The upstream delta adds repository-summary/repository-counts snapshot requests,
`summaryDeferred:true`, metadata file IDs/order and independent count loading.
Exact-content renames match; moved-and-edited files appear as add/delete. An old
explicit file ID can invoke bounded historical similarity ordering in a separate
transient snapshot; missing objects do not fetch or hide the independent file list.
New JS accepts old inline summaries. A rollback can still open comparison
revisions but older code does not recognize metadata-view file IDs. Old open
pages require refresh after activation for automatic file counts. These caveats
remain in docs/workspace-portal.md; cachev70/importv11 identifies the combined JS.
There is no new persisted descriptor/manifest version or source-only migration.

### Refresh checks and source identity limits

- Actual source receipt `tmp/p2-upstream-refresh-final-receipt.json`, SHA256
  `87c0a4fad3b6232c97fb9dbd38a39c15c6fb4cc5138d370650c02a3c169e77bd`, binds
  full1002-file map, exact bases/tips/trees,40 ordered commits, fold and primary/WIP
  observations. Owner5 independently matched every hash to committed R and the
  final ordered Git series; only39 changed patch,23 changed paths/four manual lines
  and all five pinned input files were verified against Git without rerunning tests.
- Main frozen check graph is fe384 plus threev70 template overlays, SHA256
  `3d6abcac789b74fae795e5df7da725cb92eddd12437e743a9418af3e70e9bab0` in
  `tmp/p2-upstream-refresh-check-inputs.json`. Fresh Luna/low watcher ran it once:
  repository selected PASS8.525s; selected web56.796s exit1 with exactly the stale
  negative-catalog fixture described above. All other selected repository metadata/
  count/cache/legacy/missing-blob and Pi/Codex workflow/carrier/scope/details/
  admission cases passed. Preserve actual log and watcher reply; parent recorded
  terminal failure because the watcher omitted its requested resultJSON, without
  relaunching. Sessions41977 and8267 were joined; no work remained.
- Corrected exact failed case passed1.112s (test1.06s, command22.251s including
  compile), session90781 joined. Input map is stable with no during-check changes;
  final R equals that corrected-case graph. It differs from the main Go/browser
  graph only by the test setup line. No broad batch/native/SDK replay occurred.
- Owner4 `tmp/p6-upstream-frontend-receipt.json`, SHA256
  `abb84684e39dd702989b6f5a6bb859eaa781a6851d68221565b16dd1ac2b15df`, records
  zero manual frontend edits: pure repository browser PASS; affected Pi/Codex69/69
  PASS527.034318ms; existing live repository case7.52s/Go7.677s exit0, session96337
  joined. The live check used visible parent fallback while the sole utility slot
  was occupied, then completed that same run without relaunch. Syntax passed.
- Owner2 records diff whitespace/gofmt/pin/cache/hook checks passing. No SDK/model,
  full package/installed/full-team/native3 readiness is inferred from these checks.
- `tmp/p2-upstream-refresh-sdk-reuse.json`, SHA256
  `7d34dd424c42112605fb1e7c9903fe033a48a83637837a6699a0e522209a729a`, compares
 143 runtime/domain/SDK/pin files unchanged to original native component scope.
  Original fourth4.707s and restart2.762s remain those original proofs. Compiled
  repository functions and embedded app/template closure DIFFER. The finite native
  fixture seeds no repositories and does not execute metadata/count/summary/legacy
  review functions; changed functions have separate focused Go/browser assurance.
  This is not a whole-R SDK or installed/native3 capability claim.

Raw final artifacts in tracking/tmp retain:
`p2-upstream-refresh-final-commit-map.json`, `-final.range-diff`,
`-final-feature.patch`, `-final-old-new.patch`, `-upstream.patch`,
`-final-dispositions.json`, `-sdk-reuse.json`, `-go-checks.log`, `-go-result.json`,
`-go-watcher-reply.md` and `-negative-catalog{.log,-result.json}`. Earlier start/
automerge/source-equivalence/rebased-range receipts remain historical evidence.
Exact final hashes are:

| Artifact | SHA256 |
| --- | --- |
| final range-diff | `4aabc353317847d6d7296c433868868f8e0ccced8af0b49eff1b2e6e7aafdf2e` |
| db4..R final feature patch | `166eb314a2c6d04626f073dfdbc610bf5a8be52b7d56b24b788d3ed3d6fefb7a` |
| acd..R old-new patch | `bd19ec598d8d1589bf81d0fc7a817b9ab7f130278d18c2eee18bfd1375071040` |
| 6587..db4 upstream patch | `50b2f5597fc1c15fd42ef181af783ed7cbf630cc2a60ada14ba398831a95c968` |

These final patch hashes are NOT the earlier identical fixed-base patch hash.
The refresh receipt records primary d4/parked acd unchanged, clean refreshed
worktree/index and zero intersection of23 changed paths with22 current native-WIP
paths. Native WIP continues separately and is absent from the review graph. No
primary CAS, push, default integration, deployment or lifecycle action occurred.

### Repeated streams and intended split

- **C source/Go/vendor input:** old46fd f9 and only the C-pin hunks in563f are one
  stream. New `54cbe2aa` selects final a2 in all five files before requiring
  consumers. The obsolete f9 step is removed; no known release, supported
  consumer or state boundary requires retaining it. Owner0 and architect0 confirm
  only source/build/fixture consumption in their scope. Unknown external use
  remains unknown; source refs and receipts remain available.
- **Provider identity correction:** fc023 folds into original f8 at b89007ab.
  Real absolute workspace/session/member incarnation fixtures replace the original
  inadequate synthetic identities; catalog identifier bounds remain unchanged.
- **Original team creation references:**1eee folds into e457 at22415d56. Only the
  specific creation-ID fields use their actual64hex contract; unrelated message/
  utility IDs retain their prior validator and spelling. Original receipt refs
  remain unchanged; no rekey/conversion is introduced.
- **Empty virtual categories:**699d folds into11888 at79a6677a. Explicit compiled
  virtual FallbackOn is detached nonnil[], which permits no hop; data-only/P4 nil
  semantics and original canonical hash bytes/provenance stay unchanged.
- **Worker packaging vs dependency pin:**563f becomes4e3d8438 (eight paths,
  304 additions/seven deletions). It retains Pi source/Node/worker/catalog/check/
  documentation behavior; only the already-final C pin and its message paragraph
  disappear.67e's separate backend-guard packaging substance is patch-identical.
- **Other dependency/generated inputs:** the complete five-file history contains
  only46fd/67e/563f;67e does not change C. Pi a22 and its upstream nixpkgs nodes
  enter once in563f. Main nixpkgs, llm-agents/Codex and model catalogs are not
  upgraded by this package. Worker/host metadata and later six-field workflow
  metadata describe distinct implemented boundaries, not redundant dependency
  selections. The old46 capabilities stay intact when the final six are added.
  Complete producer-field history is67e (backend binding/authority), a12
  (Pi creation4),387 (complete Pi team-record bundle), then d4 (six workflow
  fields). Each field group enters once; no existing capability value is stepped
  through superseded selections. Their owning source/guard prerequisites explain
  the separate boundaries; advertising the complete later bundle in the early
  backend-only commit would claim implementations that are not present there.
- **Additive runtime/domain/UI boundaries:** initial receipt core, supervisor,
  callback/owner separation, utility/tool enforcement, explicit successor,
  workflow barrier, checked submission/current-runtime ports, central composition
  and producer remain separate reviewable features. Component/native test additions
  stay with their interfaces. They do not justify retaining an obsolete pin.
  C's neutral adapter and question-card presentation remain separate features.

No blind all-feature squash was used. Ordinary cherry-pick/rebase and documented
file-message commits/amends were used in the isolated index, with no hook bypass,
commit-tree shortcut, broad reset/stash/clean or primary-worktree checkout. The
worker replay checked every targeted preimage after only the known C-pin
normalization; there was no substantive conflict or guessed resolution.

### Final content equivalence and raw evidence

`git diff oldd4 prepared --` is empty and final tree IDs are identical. The full
binary/full-index base-to-head patches compare byte-for-byte:

- D old/new final diff SHA256
  `a37547200f1f240f307563f17ee151f2729c4b4dfa2d5824b641cddbea377375`.
- C final diff SHA256
  `eb534027fc8f7e1da6c1b3db9c208bb39ce361c4f59952fea4b4e902f2134a91`.
- D full range-diff SHA256
  `3fb039268a41af1e30ae7a80828f24475af7fdd42e1fc1d9f9a90764e234234a`.

Raw evidence is `/tmp/pi-review-history.OkwYpE/`: old/new complete series,
`d-old-final.diff`, `d-new-final.diff`, `c-final.diff`, full `d-range-diff.txt`,
`d-dispositions.json`, remote receipts and index/WIP handoff manifests. Durable
Git refs/ranges above allow regeneration; tmp paths are disposable evidence.
This proves content equivalence only, not build-input/derivation equivalence.
Earlier checks retain their exact source/input scopes, rather than becoming
full-branch checks merely because final trees match.

The primary index's logical stage entries and flags equal the pre-preparation
captures. Primary feature stayed oldd4. Native WIP was not edited/staged: the
observational handoff manifest captures22 source paths, SHA256
`844a72517c9ce38552df5002be1d3d1d642a03af6f069ed85d5f3204716ba264`.
No claim that peer WIP stayed static while its owner worked is made.

## Dependency and input identities

| Selected input | Exact final value |
| --- | --- |
| C Git/flake locked and original | `a2b58b5e8d5c59cb448453e113b5dd48b20c3477` |
| C Go pseudo-version | `v0.0.0-20261112113545-a2b58b5e8d5c` |
| C source NAR | `sha256-SQqd4G/R9zpZXMo0sIVJSm4MgJvQgcBILa5aCy+JJkE=` |
| D vendorHash | `sha256-AQkAmLM+haFVh4AA0o5syMB8rFTnG0d0XrP/Rb9mJEY=` |
| Pi SDK source/package | `a22b888a58fe55b668cc45b80749ec88d4eb4ddc` /1.5.2 |
| Pi output used by components | `/nix/store/9hf2a7rz231w2pn50s4jlmrgs4007xc5-pi-1.5.2` |
| Cached declared D environment | `/nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv` |

Final five-file SHA256 values (old final = prepared final):

| File | SHA256 |
| --- | --- |
| flake.nix | `2a658fec72d117c3eb5a23ea2ab0850a21e91407bf1fab0a68d25abb80aaa3c9` |
| flake.lock | `0060581ff626a7346df5210f0e575a37aa3f480c62b9bc72f4fe55b667bc02a4` |
| portal/go.mod | `c869eae2a75a2683254e492b7ffa9624351b1b72ca4eba72fe629e1c8925ffb6` |
| portal/go.sum | `eb32abd6a0d45efbfe149f187c7e914a22c4ba277d1ed49b451f56f95a89b3c3` |
| nix/workspace-portal.nix | `8c7bc4e6dc5b2a5ea8c4cd6b929895026dbe4d5ba9b3046acca483ba045b6145` |

[P7-C evidence](p7-c-evidence.md) retains old f9 source and forced vendor hash
receipts. [P7 packaging](p7-packaging-evidence.md) retains actual final-a2
source/pin/hash proof: goModules derivation
`/nix/store/d8i0mqppxb2z4i1mnk4ndkvbqm12ysz3-dev-workspace-0.2.0-go-modules.drv`,
actual directory `/nix/store/jlrwjx2h7bdji5ydp71ivsj0768cb67h-dev-workspace-0.2.0-go-modules`.
The matched SRI is independently hashed there; this packet ran no vendoring/build.
Its worker-only source/NAR and retained closure proofs remain scoped to those
recorded graphs. A new history SHA/path is not the same immutable Nix source;
full final package realization remains post-review, on the final refreshed source.

## Persisted formats, transformations and provenance

The following is the format inventory, not a claim of migration-free behavior.
New atomic publications sync private files/directories under owning short locks;
after possible native effect/publication, failure stays held/Unknown and recovery
reads original records. No conversion from existing Codex sessions to Pi exists.

| Owning format/paths | Versions and owning readers/writers | Publication, compatibility and recovery |
| --- | --- | --- |
| Durable backend binding `session-backends/<workspace hash>/<slug>.json` | New schema1, `session/backend_binding.go`, `backend_publication.go`; Ruby `workspace-session-backends.rb` mirrors owning guard | Exact session/conversation incarnations, receipt and revision reserve before native effects; creating/ready/retired CAS; absent legacy selector means ordinary Codex only, malformed Pi never falls through. Binding survives ephemeral authority loss and remains a downgrade fence. |
| Runtime authority projection | Legacy schema1 Codex retained; Pi schema2 `backend_authority.go` and selector | Pi ephemeral generation/revision must match durable binding, not process ownership or Accepted proof. Reconstruct only from admitted evidence; no1->2 Codex conversion. Missing live Pi holds. |
| Root creation receipt/request/journal/completion | Legacy1/2/3 remain; Pi4 `web/pi_creation*.go`, `session/pi_creation_record.go`; journal under worktrees/.locks, immutable request/completion beside portal receipt | Freeze request/team/catalog/full policy/member settings and original IDs before effects; persist native-create intent before Create, initial input handoff before Send; ready binding/retained proof before ready cache. Lost result/Unknown never re-Create/re-Send. Receipt-cache retirement retains request/completion/journal for dependent formats. Earlier incomplete branch4 shape refuses; not a supported conversion path. |
| Tracking `portal.yml` | Legacy manifests preserved, Pi4 `session/pi_manifest.go`, Ruby creation helper | Projection only: exact backend/incarnation, goal digest and ready/initial-sent state; no Codex/tmux placeholders. Existing records are not rewritten to Pi. Original root proof remains after dependent state/retired binding. |
| Runtime `runtime.json` and immutable request history | `piruntime/runtime_records.go`, `successor.go`; schema1 entry, schema2 aggregate/current request | Actual explicit successor transition1->2 only after independent old supervisor/process-group/callback/resource drain. Retains original entry bytes, requests, package/config/account map digests; validates connected history/current full Runtime. Reads do not convert or start anything. Cannot roll back to a reader that lacks retained2. No automatic replay/reload of unfinished original input. |
| Host launch/config/handshake and resource records | Launch1/host contract1/runtime-config1/handshake1; `piruntime/protocol.go`, manager/supervisor, host launcher; resource record1/resources.go | Immutable package/profile/session/request/digest/generation and independent cgroup/PID/mount/user namespace observations precede trust. Start intent before helper effects. Resource starting/status plus original digest; historical completion only stopped+nonnull ExitCode with connected request history. Unknown drain prevents replacement; no PID-only inference. |
| Retained conversation mappings | Schema1 ordinary and schema2 policy-bearing `piruntime/conversation.go`, `tool_policy.go` | Preserve1; new explicit policy Create writes2/PendingToolPolicy before SDK mutation then verifies private tool proof and syncs applied. InitialSettings immutable; later settings/policy uses target CAS+pending and Unknown holds, no guessed rollback. Missing policy is unavailable; no implicit1->2 policy migration. Readers accept only1/2 here. |
| Utility mappings and grants | Distinct schema2 owner arm (`OwnerKind=utility`), `utility.go`, `utility_types.go`, owners | Separate full UtilityRef; no retained Conversation/HistoryRef placeholder or policy pointers. Create/Bind/Send/Load require original grant/current admission; Read/Lookup separate. No synthetic native input to create a history header. Retain original launch ownership and effects; monitor cancellation is not unload or settlement. |
| Native input receipts | Retained schema1 / utility schema2 owner, `receipt_owner.go`, `receipts.go` | Durable full input/settings intent and original op identity precede dispatch. Independently reopened native witness+prefix file/dir sync before Accepted publication. Generation is evidence, not duplicate namespace. Same original IDs including NotSubmitted/Unknown never redispatch; new settings cannot repair original. Wrong owner roots refuse. |
| Pi native history and private settings/auth | Pinned upstream SessionManager current version3, upstream settings/auth formats; wrapper `session.mjs`,`persistence.mjs` | No wrapper history converter. Public reopen proves identity/linear prefix; fsync covers admitted input prefix, not later arbitrary tool effects/power-cut guarantee. Missing mapped history holds. Shared canonical auth directory/data+sidecar locks, not copied grants/file-only mounts; legacy Codex writer not assumed co-safe. No real token/login read in this work. |
| Native retry branch-state component | New branch custom state schema1 in `native-retry.mjs`; pure native types/compiler | Input-scoped immutable policy/user/op fields, cumulative index=extra=hops; public append/reopen/whole-state+parent+branch compare/sync before target, omitted return.state. Crashes consume prospective allowance conservatively; no resume/refund. Explicit virtual empty[] no hop, data-only nil unchanged. Fake admission/route proof only; not a live host mapping3 writer. |
| Provider catalog/default and desired policy | Catalog1 / installed envelope1 / provider-policy1; `piproviders/catalog.go`,`package.go`,`store.go` | Exact raw catalog digest, trusted canonical mappings/full chain, session default+exact member/incarnation override. Private lock+reread+CAS+atomic rename/sync, no-write reads. Requested/effective/physical separate. Noninitial canonical startup map frozen; no aliases/auth inference. Same policy digest algorithm/provenance; fallback sender absent. |
| Creation selection | Inner schema1 frozen within root4, `session/pi_creation_selection.go` plus P4 owning validator | Complete original catalog digest/policy/default/overrides and per-reserved-member source/digest/settings; no browser-supplied catalog, latest-default re-resolution or fallback truncation on retry. Deserialize intent then normal Resolve against exact original catalog; private provenance is not persisted authority. |
| Team roster | Legacy Codex1; new PiRoster2 `teamruntime/pi_roster.go`, schema store | Full role policy/session/lead/member incarnation and original creation/initial-input refs; initially creating then ready only through admitted exact capture+binding CAS. No conversion of Codex roster/member or guessed initialization; old writer refuses Pi schema. |
| Monitor operation | Legacy1; PiOperation2 `monitoroperation/pi_records.go`,`pi_operation.go`,`pi_runtime.go` | Original lead/input, installed utility policy, utility create/launch refs, report events/slots/settlement frozen. Persist before effects; reports idempotent independent from command settlement. Missing original receipt stays Unknown; no resubmission to repair notification. Source fixtures do not enable real full-team monitor flow. |
| Communication workspace aggregate | Legacy1 and explicit mixed2 `communication/pi_records.go`,`store.go`, UpdatePi/Schema2Write | **Actual lazy atomic1->2 aggregate upgrade** on admitted first Pi write. Preserve every old endpoint/grant/message/option/receipt/pending delivery, including legacy nulls. Exact cross-lead approval still required; no reapproval/resend. Legacy writers require complete2 support/held package gate after upgrade; same new reader supports legacy traffic preserving Pi arms. Retired bindings/empty aggregates do not erase downgrade fence. |
| Observer records | Legacy1; PiState2 `progressobserver/pi_records.go` | Key hashes exact session/lead incarnations, original pending conversation/settings/input. No empty key initialization or inference from old thread. Admitted writer, original Lookup-only reconciliation; no duplicate observation Send. |
| Optional question store | Schema1 `piquestions/store.go`,`file.go`; full conversation-incarnation path | Atomic private4MiB bounded aggregate, question/origin/item/answer revisions and exact prepared original SubmissionRef before checked Send. Busy keeps pending; duplicate/lost ACK uses original Lookup only. Branch/origin/current authority changes hold/stale; never mint a replacement original. No automatic collector/converter. |
| Plan/mode store | Schema1 `piplan/store.go`,`mode.go`,`service.go` | Complete proposal hash binds exact UTF8 displayed content; acceptance IDs/revisions and full mode target/handoff precede native effects. Pending mode CAS is verified or held, never guessed rollback; implementation uses original submission once. No missing policy migration/default inference. |
| Ordinary composer/attempt/draft/receipt/retry keys | Frozen D app.js and C `createDurableAttemptStore`; exact families and declared shapes below | Bind once to actual nonempty snapshot thread and frozen Pi scope; no empty/Codex-key migration or automatic restored dispatch. Original receipts remain distinct from the UI order record. Retired callbacks cannot mutate current UI/draft or dispatch successors. |
| Optional question/Plan browser keys | `pi-questions:<namespace>:<id>` draft schema1; `pi-plan:<namespace>:acceptance` exact pending payload, no invented version; Pi UI modules | Namespace includes complete admitted session/member scope. Save/readback exact request identity before network; stale/error retains draft; reload/status is read-only, never auto-send. Separate from ordinary composer storage; browser data grants no host/native authority and is not server record migration. |
| Package/worker/host protocol metadata | Worker metadata schema1/protocol1, host manifest1, existing runtime metadata plus exact team/workflow bundles | Source producer adds six fields to original46 unchanged. Guard/preflight scans actual retained roots incl cold/held/retired originals and requires complete team map, Questions1/Plan1/ToolPolicy1+conversation2/callback1/linear1/observation1. Old candidates refuse. NativeRouting3 declaration is absent even though strict decoder exists. No metadata normalization enables an unknown reader. |
| Existing Codex stores/recovery and unchanged compatibility metadata | Existing receipt/retry/provider/team/authority/session lifecycle formats retained, C native protocol unchanged | Opt-in dispatch resolves backend on every request, denies ambiguity. No Pi-to-Codex fallback, no retroactive Codex process isolation, no deletion of old recovery fences. This branch does not retire older supported formats or convert existing sessions. |

No database schema migration is introduced. There ARE the explicit runtime1->2
successor and communication1->2 transformations above; new Pi4/new policy2 formats
are intentional explicit writers with old-reader fences, not a history-only
excuse to delete predecessor support. Existing source/fixtures have consumed
these formats; no deployment/profile activation/default integration/real model
call is recorded by the package owners. Repository publication and fixture data
are distinguished from supported deployed state. **Unknown external consumption
remains unknown.** Old source tips/receipts are preserved, not asserted absent.
The independent reviewer must explicitly conclude whether this complete
transformation lineage and preserved recovery are sound.

### Ordinary Pi browser persistence

This inventory uses frozen D d4/25af `portal/internal/web/static/app.js` and
C a2 `conversation/assets/conversation.js`/`delivery_retry.js`, confirmed by
owner4's existing [frontend evidence](p6-central-frontend-evidence.md). It does
not read or describe the later refresh WIP. Let `S=encodeURIComponent(slug)` and
`P="pi."+encodeURIComponent(scope)+"."+encodeURIComponent(actualThreadId)`.
The exact rendered scope is `pi-workflow-v1:<lowerhex64>` and excludes NativeID/
runtime generation; the actual first current snapshot thread ID is independently
required, not inferred from P or from P6 availability.

| Family / storage | Exact key or prefix | Existing encoded record |
| --- | --- | --- |
| Ordinary captured composer/FIFO, sessionStorage | `workspace-portal.message-dispatch.S.P` | Declared `{schema:1,entries:[...]}`, at most20 entries. Entries keep `id`, `action`, `message`, `attachmentIds`, `state` and applicable existing retry/context fields. Persist/readback before HTTP; restored order pauses. |
| Send attempt/original receipt, sessionStorage | `workspace-portal.send-attempt.S.P.` + original attempt ID | Unversioned object: `message`, `steered`, optional `attachmentIds`, `context`, applicable `dismissed`, `dropped`, `state`, `retryable`, `replacementId`, `transcriptDigest`. No schema/version field is declared. |
| Queue attempt, localStorage | `workspace-portal.queue-attempt.S.P.` + original attempt ID | Unversioned `{message, optional attachmentIds}`. Original ID comes from the key. C's actual `createDurableAttemptStore` handles bounded identity/prefix reads and write/removal readback; no Pi schema2 is implied by the key segment. |
| Existing request-input draft, when used, sessionStorage | `workspace-portal.request-input.S.P.` + `encodeURIComponent(requestId)` | Unversioned `{page,drafts,questions}`; questions is the existing serialized question set, drafts retain kind/choice/note for nonsecret items, secret entries are empty. No invented schema number or separate ordinary textarea-draft format. |
| Delivery retry | No additional durable Pi key or ledger | C's scheduler keeps in-memory timers and reuses the original dispatcher/send receipt ID/state. Only explicit certified transient non-delivery can schedule retry; restored uncertainty is not permission to dispatch. This is separate from native/provider fallback. |

Typing before identity remains memory-only textarea state. Binding occurs once
after the first current scoped snapshot supplies an actual nonempty string
thread ID; default form/keyboard dispatch is blocked until then. No empty, old
or Codex keys are read, initialized or migrated. Repeated snapshots/reconnects
cannot replay restored attempts or add action listeners. Same-key uncertainty
stays paused for original-identity reconciliation.

Scope/member/thread change or page teardown retires listeners and retries and
requires a fresh page. A late positive in-flight callback may save only its
original receipt under its original key, without touching the replacement draft/
UI or dispatching another attempt. Pi upload composition is nil/unmounted: no
Pi upload-draft, clipboard-number, metadata, XHR or download key/writer is created.
Existing Codex eager initialization, keys/codecs/uploads/retry behavior are
unchanged. Optional question/Plan storage above is a separate domain and does
not version the ordinary dispatcher or per-attempt receipt objects.

## Original component verification and its actual limits

Prepared-history quick checks passed under the declared cached D environment:

- Exact final tree and byte-identical full-diff comparison; all43 old commits
  accounted, unrelated replay patch IDs equal, full range-diff retained.
- `git diff --check 6587c4c1..acdff316` and isolated clean index/worktree.
- Existing `nix/check-codex-web-pin.sh` against actual final go.mod/pseudo-version,
  plus `test/codex_web_pin_test.sh` positive/negative fixtures.
- Nix parse-only of flake.nix and nix/workspace-portal.nix. No build/evaluation
  of final application, vendoring, SDK/model call, broad suite or long CI here.
- Normal hook-preserving Git; no declared active hook framework in these
  repositories. All authored/amended messages used tempfile `git commit -F`.

Earlier component assurance is reused only through exact original evidence:

| Component / evidence | What is established and what remains outside it |
| --- | --- |
| [P1 final C](p1-f-evidence.md), [P0](p0-evidence.md), [P1](p1-evidence.md) | C neutral adaptation/question presentation and finite DTO/browser behavior; C final two logical commits/tree history and reported exact-head CI, not Pi production authority. |
| [H0](h0-evidence.md), [coexistence](coexistence-evidence.md) | Host launcher/strict legacy-writer fence source and finite fixtures; installed host/cgroup/mount/prerequisite verification pending. |
| [P2 creation](p2c-evidence.md), [providers composition](p2providers-evidence.md) | Immutable selection and real Manager composition component boundaries, current settings/creation/CAS; public installed root allocation and actual runtime accounts remain separate. |
| [P3](p3-evidence.md), [checked/common ports](p3i-checked-submission-evidence.md) | Pinned SDK receipt/witness barriers and original no-resend, typed owner separation/current-runtime/checked Send. Native corrected domain2.373s at6b64+99inputs; final pure/control0.831 at3318+103inputs. These exact graphs do not contain central final source or native3 authority. |
| [P4](p4-evidence.md), [canonical/switch](p4-a-evidence.md), [loader](p4-l-evidence.md) | Provider validation/storage/digest/provenance/configuration fake checks; account/Daybreak entitlements or live provider routing not established. |
| [Native pure](p4-native-pure-evidence.md), [SDK](p4-native-sdk-evidence.md), [empty categories](p4-native-empty-categories-evidence.md) | Pure0.046, pinned fake SDK19/19 about8s, red0.015/green0.031 clean7e+ONLY2overlay regression. SDK fake authority labels preserved; real fixed original lifetime/Accepted/currentgen/effects/route proof absent. |
| [P5](p5-evidence.md), [records](p5-i-evidence.md), [utility](p5-utility-evidence.md) | Typed team/monitor/communication/observer schema2 codecs/adapters and owner engine fixtures, not installed automated-team flows. |
| [P6](p6-evidence.md), [B2/native](p6-b2-evidence.md), [workflow UI](p6-workflow-ui-evidence.md) | Optional durable question/Plan, actual pinned native origin/tool policy component and UI scope, not complete installed web flow. |
| [Team fence](p2team-fence-evidence.md), [team admission](p2team-admission-evidence.md), [workflow guards](p2-p6-guards-evidence.md) | Complete retained namespace scans/old-target refusal/admitted writer paths and exact original root proof preservation in source fixtures. |
| [Central workflows](p2central-workflow-evidence.md) | Actual full-domain4.707s: clean base7e+exact19 overlays, manifest `tmp/p2central-native-fourth-inputs.json`; SAME Manager/new Server explicit binder. Real callbacks/question/Plan/actions/original answer+implementation receipts/duplicate no-resend/scoped stream. NOT new Manager/background-only attachment, installed package or live provider proof. |
| [Central restart extension](p2central-workflow-evidence.md) | Actual2.762s non-skipped new Manager/new Server; clean329+21 overlays, manifest SHA `a3c50d13e18d737483a0f049ecf20c94437aefd9bae023076c0d1508aec9345e`; owner1 exact Reopen patch. Background GET demand negotiates AttachHost/ACK/full-ref refresh; original Accepted receipt identical and one original input; no Ensure/Load/resend. Does not replay answer/implementation actions or establish installed/root/team/utility/native3 readiness. |
| [Central frontend](p6-central-frontend-evidence.md) | Exact frozen browser scope/guard/legacy panel source checkpoints within25af; final frontend manifest5451c7ab, actual guard1/1 .238 and Codex2/2 .217, syntax. Not installed-browser acceptance. |
| [P7 packaging](p7-packaging-evidence.md) | Actual source/NAR/vendor/worker/check retained-output proofs, including current worker50.938s graph `0a32d027c30029916d68ce24df4dd696d99546dabcbadbdfe3ad978a97ca0cae`. Managed report was INCOMPLETE while source command PASS; parent reconciled exact terminal cells, without rewriting monitor outcome or duplicate run. No full configured application installation. |
| [Final producer](p7-workflow-contract-evidence.md) | Clean25af+ONLY2 source/embed/strict decoder0.050; original46+six capability values, no native3. Earlier Ruby1test97assertions/source consumers remain byte-scoped; final installed output comparison prepared only. |

The central evidence retains early UUID/managed:false fixture failures, duplicate
invocation uncertainty,20s incomplete third flow, genuine GET-demand coalescing
fix and final passing graphs. SDK evidence retains the persisted-undefined
comparison failure and malformed-state fixture counting correction. Do not turn
a successful rerun into a claim that original failures never occurred.

## Documentation routing and preservation inventory

| Topic | Intended reader / class | Authoritative home | Fidelity and known limits |
| --- | --- | --- | --- |
| Entry points / opt-in source boundaries | Developers/operators, index/reference | D README, pi-runtime/README, docs/dev-sessions.md, docs/workspace-portal.md | Grouped links reach subsystem pages; prefix compatibility kept by lead writing passes. Installation/runtime proof limits remain visible. |
| Refreshed repository metadata/counts and old links | Portal developers/operators, reference and compatibility guidance | README and docs/workspace-portal.md repository sections | Exact upstream copy retains summaryDeferred/new snapshot endpoints, metadata file-ID ordering, bounded legacy-link fallback, rollback ID limit and old-page refresh requirement; unchanged persisted descriptors is not a no-protocol-impact claim. |
| Backend binding, root creation and retention | Portal/runtime maintainers, reference/recovery contract | docs/pi-creation.md; internal/agentbackend/README | Exact schema4 selection/root/receipt publication, older-reader fence and no-conversion/no-resend semantics match owning codecs. No deployment procedure executed. |
| SDK receipt, callbacks, utility, tool policy, successor | Runtime maintainers, reference and reusable recovery | docs/pi-runtime.md, docs/pi-teams.md | Distinguishes Accepted input-prefix sync from arbitrary tool-effect settlement; current-ref/history/drain fences retained. Domain docs' component gates are not final installed guarantees. |
| Process/cgroup/mount ownership | Host operators, reusable operations/reference | docs/pi-runtime-host.md; nix/pi-runtime-host.nix | One session boundary, independent handshake proof; installed host VM/containment remains pending. |
| Catalog/account/settings/native components | Portal/runtime maintainers, reference | docs/pi-providers.md | Trusted canonical store directory/sidecars, per-member override, requested/effective/physical views, native fake-only authority and original deadline limits preserved. |
| Nonblocking questions/Plan/workflow UI | Portal/runtime developers/operators, reference | docs/pi-questions.md; C conversation docs and shared card API | Durable draft/response/acceptance vs host authority, mode enforcement/copy scopes and no-reload-send match source. Ordinary transcript read still has native snapshot boundary. |
| Independent check results and one initiative execution | Lead/reviewer, individual execution evidence | This packet plus linked work/<slug> evidence files | Exact graph/result/source identity and failed attempts stay here, not in generic product docs. No rollout/deployed success invented. |
| Cross-project neutral contract | Shared component consumers, reference | C conversation/backend and HTTP/browser docs; D pin/composition imports | C owns reusable typed adapter/nullable slots/shared card; D owns Pi authorities, durable domains, host routing. Exact final C pin propagated once. |

Fixed-base preparation moved no prose and changed no final source. The separate
refresh retains verbatim upstream guidance plus approved Pi copy; no new prose
rewrite was introduced. Owning technical and lead main writing passes remain in
the recorded packages. No supported
upgrade/recovery document was deleted or retired; source-record recovery stays
with its owner, not replaced by packet prose. The reviewer must independently
check placement, discoverability, factual fidelity and preservation, especially
large cross-component scope and claimed source-vs-installed boundaries.

## Review assignment and next handoff

Overall risk is **high**: auth/account binding, persisted formats, partial effects,
protocols, host process ownership, public/cross-project interfaces, old-reader
refusal and mixed-version recovery. Proposed lanes: general; architecture and
repetition; scope/proportionality; risk/compatibility. Coordinator must pass the
mandatory-review skill and all four lane references to one independent eligible
reviewer0, retained Sol/xhigh/read-only. Owner5 authored provider/history portions
and cannot self-review. No reviewer invocation has occurred in this package.

The reviewer must explicitly conclude on complete final history, all repeated
streams, obsolete approaches, transformation/migration lineage and documentation
preservation, rather than reviewing only the final diff or latest producer.
No automatic approval or absence of findings is prefilled here.

Next: lead accepts this reconciled packet and owner2/4 final refreshed source/
check handoff, then invokes reviewer0 on final db4..R and C dd90..a2, with the
complete original->parked->refreshed lineage above. All intended reviewed source
is committed in the isolated worktrees; primary/native work remains separate.
No final primary cutover/publication window is requested or authorized by packet
acceptance. Prior results retain their explicitly stated input/execution scope.

Any later primary feature-ref CAS requires its own short lead window: fresh
expected-old tip, logical index entries/flags and native dirty manifest; atomically
update only the feature ref with expected-old, equal-tree precondition where
applicable; verify index/WIP unchanged and exact new ref, release before tests or
waits. A substantive refreshed tree cannot use equal-tree cutover assumptions.
Do not check out/rewrite the primary index or overwrite native WIP. No merge
claim/default integration/deployment or cleanup is authorized.

Prepared post-review gates remain: final package/source/installed metadata and
consumer comparison, host launch and cgroup/mount containment, existing Codex
regression, actual root creation/web question/Plan flows, full-team/monitor/
communication/observer operations, and eventually separate native3 authority/
writer/transport/old-target guard/physical-route support. Lead sequences those
checks and feature-only publication; no long CI/build ran during preparation.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
