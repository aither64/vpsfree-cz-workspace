# API article restructuring: staging receipt

**Both reviewed cumulative previews staged and verified; retained owned/up.**
Exact final source commit `f66862dc85f65e3f1158c60e4f67b5e03498b540` and the
three-commit owned series from `5c66c35194b63469386168b8fd6c9c4f8c371baf`
received reviewer0 final general acceptance without findings. No content,
manifest or source commit changed during staging.

| Preview | Staged revision | Content SHA256 | Manifest SHA256 |
| --- | ---: | --- | --- |
| [CS](http://kb-cs.aitherdev.int.vpsfree.cz/navody/vps/api) | 1793202239 | `1dac0f87623b0d802882e35fc80939ac41d514c4365323163af2a4c9f2103b9a` | `1cdbdbd111b80b63a13ecb6120390fb685c09023e9beb2b6c71b1597dd772073` |
| [EN](http://kb-en.aitherdev.int.vpsfree.cz/manuals/vps/api) | 1793202258 | `a88bce7f0c13848f3b80029beb7365a0ab8b46d0937ae29f3774b4520f80831b` | `7d6fbfe28cb732321e2da8d0d6c596ebb001a39222db5480ca4f574ffb5357ef` |

Exact localized summaries and native-verified history links:

- [CS history](http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody%3Avps%3Aapi&do=revisions): Uspořádání autentizace, CLI a klientů pro Ruby a další jazyky; odstranění haveapi-fs
- [EN history](http://kb-en.aitherdev.int.vpsfree.cz/doku.php?id=manuals%3Avps%3Aapi&do=revisions): Put authentication and Ruby/CLI first, document the other clients and remove haveapi-fs

Fresh preconditions passed: bound session with both ambient markers absent,
retained implementer3 Sol/xhigh/workspace_write; exact reviewed candidate,
manifest and summary hashes; authoritative OURSLUG/up and predecessor ENpending
`eebd92db26ee86cdc1e8a3c48e78cb38dd4e89ab430268dcaad4cd89253af679`.
Fresh production/staging authentication and target-page edit ACLs passed before
reset and again afterward. Prior staged bytes/revisions were saved before reset
alongside all original evidence; no foreign ownership was discarded.

Fresh consistent production page-info/content/page-info guards matched:
CS1783860648/content
`8ea88de825d7b3823aee1d4ff8fd2704c9eb2f431cfbb944643927eabde3fd13`
and EN1777543182/content
`8006293f735a7e6f45c04d2d59ad82a003afa4547db1ddb38f380504e1e107d3`.
Each ordinary stage also performed its native production-baseline checks.

One ordinary `kb-stage reset --yes` exited0/53.658s,
handle63529/nativePID1778450. Its completed mirror was OURSLUG/up,
pending null. Sequential ordinary commands on handle95448:

- `kb-release stage --manifest kb-release-cs.yml --yes`: exit0, nativePID1822336, 17.87s.
- `kb-release verify --manifest kb-release-cs.yml`: exit0, nativePID1827510, 1.381s.
- `kb-release stage --manifest kb-release-en.yml --yes`: exit0, nativePID1828235, 17.682s.
- `kb-release verify --manifest kb-release-en.yml`: exit0, nativePID1835866, 1.358s.

Canonical verifiers and independent staged-source reads proved the exact reviewed
bytes and stable actual revisions. Bounded public HTML passed in both languages:
authentication/scopes, CLI/main Ruby/read/backup examples, then PHP, Python,
JavaScript/TypeScript, Go, vpsAdmin TypeScript and Rust; no haveapi-fs; generic
0.31.2 and separate client0.1.1/runtime0.30.2; reciprocal links; new Ruby/PHP
reads and PHP/Go install commands. Native verify proved each exact localized
summary and reported its history URL. Only one fresh rendered GET per page was
needed; no browser or external-link/client/SDK campaign.

Rendering limitation: DokuWiki localizes quotes in the inline Go constructor
(the Czech page displays `client.New(„https://api.vpsfree.cz“)`), while exact staged
source retains ASCII quotes. The install code, method and unversioned base are
verified; direct copy of that typographic inline text is not claimed. The first
literal-projection failure is preserved. One bounded check against saved CS HTML
recognized that typography; only missing EN checks followed. Span text was joined
without injected spaces, with NBSP normalized for bounded literals. No raw
highlighted-code equality assertion, parser project, source correction or
reset/stage retry was made.

Final authoritative owner `2026-10-24-vpsadmin-haveapi-upgrade`, container **up**,
pending exact new ENmanifest
`7d6fbfe28cb732321e2da8d0d6c596ebb001a39222db5480ca4f574ffb5357ef`. The one pending ENrecord coexists with
both staged pages. All reset/stage/verify native children were waited; handles
63529/95448 fully consumed, no uncertain effects or active E3 operation remain.
E2 retained the sole CI utility; the documented visible direct-owner fallback
observed the original operations without duplicate watcher or CI query.

Evidence: [reviewed inputs](committed-inputs.json),
[pre-reset status](status-before.json),
[actual production/prior-stage guards](production-and-prior-source-guards.json),
[reset result](reset-result.json), [command results](commands.json),
[CS verify](cs-verify.log), [EN verify](en-verify.log),
[staged/rendered checks](rendered-and-staged.json),
[original rendered failure](rendered-first-check.json),
[diagnosis](rendered-first-failure.json), [final status](status-final.json),
[effects reconciliation](effects-reconciliation.json).

This is the final cumulative preview. The three intended production revisions
remain separately reviewable in [the publication plan](../publication/README.md)
and its committed content chain. Production requires direct approval and each
real predecessor revision/content readback before binding later guards.
No production write/promotion, shared-master push/content commit, stage stop or
release, native/cluster/provider/config or session lifecycle action occurred.
Session, staging and cluster remain running/open; lead owns state/handoff.
Internal development routing/DNS access is required for these preview URLs.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
