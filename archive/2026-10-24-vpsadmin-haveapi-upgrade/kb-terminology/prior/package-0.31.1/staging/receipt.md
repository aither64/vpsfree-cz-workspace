# KB 0.31.1 staging verification — 2026-10-27

**PASS: both committed articles staged and verified; staging retained for review.**
Lead accepted the mechanical version refresh at workspace commit
`a7e6c0dc1124777ab3dd7a377cbc4192e3e09d9a` and released owned reset/restage.
No article/prose/manifests were changed during staging.

Session/current matched the trusted binding; ambient session markers were absent
and both verified markers were exported for public commands. Authoritative status
before reset showed our owner and the exact saved old EN pending digest
`3d9f5b61436b0c5b76a06cec89f33a09b1fd2a0211e8954177c912693f414b97`.
It matches the preserved `0019dd4` manifest; old page bytes/revisions and receipts
remain in `../kb/prior-0019dd4/`. No uncertain operation remained.

Public `kb-stage reset --yes` completed exit 0 in 49.305 seconds, reconciling
only our pending bundle/mirror through the ordinary tool. A0 held the sole
watcher reservation; visible parent fallback retained command handle 92272 and
bounded waits. No private pending clear or individual-page bypass occurred.

After reset, public authentication and exact target-page ACL checks passed on
both staging wikis (ACL 255). Fresh production page-info/content/page-info reads
agreed and retained the original guards:

| Page | Revision | Production source SHA-256 |
| --- | ---: | --- |
| `navody:vps:api` | 1783860648 | `8ea88de825d7b3823aee1d4ff8fd2704c9eb2f431cfbb944643927eabde3fd13` |
| `manuals:vps:api` | 1777543182 | `8006293f735a7e6f45c04d2d59ad82a003afa4547db1ddb38f380504e1e107d3` |

Committed manifest bytes were rechecked: CS
`548336df87a143f2ed9a6bba215f8e2a11da7e1600ad791e35d329826b14fdcd`,
EN `1253694e0937ad3e696db8a2666a1d83efb53bbb6d8f0de0a422a86daabbb221`.
Sequential CS stage/verify and EN stage/verify all exited 0, completed by
22:39:37 UTC. Parent handle 51807 is complete. No refusal, retry or uncertainty
occurred in this released operation.

| Staged article | Revision | Exact content SHA-256 |
| --- | ---: | --- |
| [Czech](http://kb-cs.aitherdev.int.vpsfree.cz/navody/vps/api) | 1793140740 | `d3c707a1e2f7f7326cf83e036576ff561f93e8c003218b081e3bb3ad886602d3` |
| [English](http://kb-en.aitherdev.int.vpsfree.cz/manuals/vps/api) | 1793140759 | `e93f46443954778b4b03ec0c706150c4cb217c7e92c4d9d095739e41fa100288` |

Canonical verify and bounded public HTML reads confirmed headings, rendered
Python/npm **0.31.1** install commands, unchanged executable snippets, generated
SDK **0.1.1** with exact runtime **0.30.2**, the corrected README factory pointer,
and reciprocal Czech/English links. Both history pages returned HTTP 200 and
contained their exact localized summaries:

- [CS revision history](http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody%3Avps%3Aapi&do=revisions):
  Doplnění klientů pro Python, Rust a TypeScript včetně generických klientů 0.31.1 a závislostí generovaného SDK
- [EN revision history](http://kb-en.aitherdev.int.vpsfree.cz/doku.php?id=manuals%3Avps%3Aapi&do=revisions):
  Add Python, Rust and TypeScript clients, generic client version 0.31.1 and generated SDK dependencies

Final authoritative state: owner
`2026-10-24-vpsadmin-haveapi-upgrade`, container **up**, pending **EN** current
manifest digest
`1253694e0937ad3e696db8a2666a1d83efb53bbb6d8f0de0a422a86daabbb221`.
The public tool keeps one pending manifest; both page sets remain available.
Internal development network/DNS access is required.

Evidence: [pre-reset status](status-before.json), [reset result](reset-result.json),
[commands/exits](commands.json), [production guards](production-guards.json),
[CS verification](cs-verify.log), [EN verification](en-verify.log),
[rendered/staged facts](rendered-and-staged.json),
[final owner/pending](status-final.json).

No production promotion/write, staging stop/release, foreign action, cluster
operation, package query, fixture-test repeat, browser screenshot, source/ref,
Git/index or session lifecycle mutation occurred. This proves staging review
readiness, not production publication or E4 cluster acceptance.

Session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/>.
