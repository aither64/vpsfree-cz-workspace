# Go inline literal: corrected staging receipt

**Corrected, committed and staged in both languages.** Commit
`668291226733ffdb18fe94588078994af02a8594` appends a focused markup correction to the preserved shared
history. Parent `e54e6c3386af2310a5c3b7021031710042ae69bc`. Ten explicitly owned paths changed;
[exact diff](correction.diff), [commit bindings](commit.json).

One constructor literal per language gained DokuWiki no-format escaping inside
its existing inline code: `''%%client.New("https://api.vpsfree.cz")%%''`.
Reversing those two additions restores the exact reviewed pages. No prose,
interface or executable example changed. The same change is included in the
publication step03 pages/diffs and content-chain hashes; earlier steps and all
localized summaries remain unchanged. There are still **three publication
revisions**, with no future production revision invented and **NO MIGRATIONS**.

Quick checks: canonical191/2/189, installed schema5 parser/candidate checksums,
reverse-byteproof and content-chain consequences pass. `git diff --check` exits0.
Normal SSHfetch, nonblocking common Git tracking lock, explicit owned index and
message-file commit were used; index before/after empty, no hook bypass/push.
Unchanged source/example/flow checks retain their earlier accepted scope.
[Quick evidence](quick-checks.json).

| Preview | Staged revision | Content SHA256 | Manifest SHA256 |
| --- | ---: | --- | --- |
| [CS](http://kb-cs.aitherdev.int.vpsfree.cz/navody/vps/api) | 1793202869 | `1bb9489834beb20f4b6faff6bd16a08fad5496c3a9ab2b008785f1fe9940746b` | `e96f0e1171c15bf4356bb60beb832832e8acfb8843928a5f1c0eb6d843e31bc1` |
| [EN](http://kb-en.aitherdev.int.vpsfree.cz/manuals/vps/api) | 1793202888 | `fdbd835aef91632b5cad49b60c3f3a906ef06febb788eb72f3b7039f6f3e13ae` | `26c400ad5065cf4ebbc3e8bcbc4e8b7d621059e5144075ba5927f3b1ec0ed11a` |

Fresh source guards preserve actual production CS1783860648/content
`8ea88de825d7b3823aee1d4ff8fd2704c9eb2f431cfbb944643927eabde3fd13`
and EN1777543182/content
`8006293f735a7e6f45c04d2d59ad82a003afa4547db1ddb38f380504e1e107d3`.
Page-info/content/page-info reads were stable. Pre-reset owner was OURSLUG/up,
pending exact predecessor ENmanifest
`7d6fbfe28cb732321e2da8d0d6c596ebb001a39222db5480ca4f574ffb5357ef`.
Prior staged bytes/revisions were preserved. Authentication/edit ACLs for the
production and staging target pages passed before reset and again afterward.
Committed hashes were rechecked; each stage natively rechecked production guards.

One public `kb-stage reset --yes` completed0/50.909s on
handle48770/nativePID1925524; owned/up/pendingnull mirror confirmed.
Sequential related commands on handle41716:

- `kb-release stage --manifest kb-release-cs.yml --yes`: exit0, nativePID1936247, 17.81s.
- `kb-release verify --manifest kb-release-cs.yml`: exit0, nativePID1938402, 1.454s.
- `kb-release stage --manifest kb-release-en.yml --yes`: exit0, nativePID1938943, 17.698s.
- `kb-release verify --manifest kb-release-en.yml`: exit0, nativePID1941750, 1.37s.

Independent staged-source reads exactly match the committed candidates at stable
revisions. One rendered GET per page proved the code-node text is exactly
`client.New("https://api.vpsfree.cz")`. Both quote characters are ASCII34;
normal HTML entity decoding and span-text concatenation were used. **No
replacement of typographic quotes or other character normalization was used in
this assertion.** No `%%` markers render. The prior inline-copy defect is fixed.
[Rendered-copy proof](rendered-copy-proof.json) retains the literal, UTF8 hex,
HTML hashes, source facts, summaries and history URLs. Earlier unaffected
render/flow/version/pair/language checks remain in the immutable
[original receipt](../receipt.md); no client/browser/SDK campaign was repeated.

Exact unchanged localized summaries and native-verified history links:

- [CS history](http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody%3Avps%3Aapi&do=revisions): Uspořádání autentizace, CLI a klientů pro Ruby a další jazyky; odstranění haveapi-fs
- [EN history](http://kb-en.aitherdev.int.vpsfree.cz/doku.php?id=manuals%3Avps%3Aapi&do=revisions): Put authentication and Ruby/CLI first, document the other clients and remove haveapi-fs

Final authoritative owner `2026-10-24-vpsadmin-haveapi-upgrade`, container **up**,
pending exact ENmanifest
`26c400ad5065cf4ebbc3e8bcbc4e8b7d621059e5144075ba5927f3b1ec0ed11a`. Both pages remain reviewable.
All reset/stage/verify native children were waited; handles48770/41716 and the
read-only verification handle86776 were fully consumed. All exits0; no retry,
uncertain effect or active owned operation/watcher remains. E2's CI utility was
untouched; the original operations used visible direct-owner fallback.

Original staging receipt/failure/render/source evidence remains byte-identical,
verified against [saved evidence hashes](preserved-evidence-hashes.json).
This receipt and all followup outputs are additive. Other evidence:
[production/prior-stage guards](production-and-prior-source-guards.json),
[reset result](reset-result.json), [commands](commands.json),
[CS verify](cs-verify.log), [EN verify](en-verify.log),
[final status](status-final.json), [effects](effects-reconciliation.json).

No production write/promotion, push/default integration, CI query, cluster,
provider, config or lifecycle action. Session, staging and cluster remain open.
Internal development routing/DNS is required. Eventual publication still needs
direct user approval and each real predecessor readback under the existing
[three-step plan](../../publication/README.md). Lead owns direct narrow-fix
acceptance and state/handoff; no new automatic full review was introduced.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
