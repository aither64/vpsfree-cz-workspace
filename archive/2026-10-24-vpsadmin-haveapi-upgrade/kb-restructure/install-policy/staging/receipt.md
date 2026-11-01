# Separate KB staging revisions — completed

Reviewed KB commit `41b34dbfe490ddb221b6752aeacd05ea59b72c66`; retained reviewer0 final general/history/scope/risk: **NO FINDINGS / NO MIGRATIONS**, accepted by lead. Nine ordinary public saves created two explicitly labelled baseline restorations and seven logical edits. No reset, duplicate save, production write or private-state edit.

| Language | Logical step | Actual revision | Review diff |
| --- | --- | ---: | --- |
| CS | 00-baseline | 1793311433 | [actual predecessor→result](http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody%3Avps%3Aapi&do=diff&rev2%5B0%5D=1793202869&rev2%5B1%5D=1793311433) |
| CS | 01-remove-fs | 1793311439 | [actual predecessor→result](http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody%3Avps%3Aapi&do=diff&rev2%5B0%5D=1793311433&rev2%5B1%5D=1793311439) |
| CS | 02-main-ruby | 1793311496 | [actual predecessor→result](http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody%3Avps%3Aapi&do=diff&rev2%5B0%5D=1793311439&rev2%5B1%5D=1793311496) |
| CS | 03-other-clients | 1793311557 | [actual predecessor→result](http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody%3Avps%3Aapi&do=diff&rev2%5B0%5D=1793311496&rev2%5B1%5D=1793311557) |
| CS | 04-obsolete-header-note | 1793311563 | [actual predecessor→result](http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody%3Avps%3Aapi&do=diff&rev2%5B0%5D=1793311557&rev2%5B1%5D=1793311563) |
| EN | 00-baseline | 1793311436 | [actual predecessor→result](http://kb-en.aitherdev.int.vpsfree.cz/doku.php?id=manuals%3Avps%3Aapi&do=diff&rev2%5B0%5D=1793202888&rev2%5B1%5D=1793311436) |
| EN | 01-remove-fs | 1793311493 | [actual predecessor→result](http://kb-en.aitherdev.int.vpsfree.cz/doku.php?id=manuals%3Avps%3Aapi&do=diff&rev2%5B0%5D=1793311436&rev2%5B1%5D=1793311493) |
| EN | 02-main-ruby | 1793311554 | [actual predecessor→result](http://kb-en.aitherdev.int.vpsfree.cz/doku.php?id=manuals%3Avps%3Aapi&do=diff&rev2%5B0%5D=1793311493&rev2%5B1%5D=1793311554) |
| EN | 03-other-clients | 1793311560 | [actual predecessor→result](http://kb-en.aitherdev.int.vpsfree.cz/doku.php?id=manuals%3Avps%3Aapi&do=diff&rev2%5B0%5D=1793311554&rev2%5B1%5D=1793311560) |

Final previews: [CS](http://kb-cs.aitherdev.int.vpsfree.cz/navody/vps/api) / [EN](http://kb-en.aitherdev.int.vpsfree.cz/manuals/vps/api).

Exact final source hashes:

- CS `933c4a1e565d75b092cc9854f11cb0aa08e7ce66109b2d6bff12155b75e02fc9` (step04).
- EN `fea084c46c5e3b998f6b4fd7add5827390600d409528e5335487bdfb54b0dd20` (step03; no artificial step04).

Each save used `kb-page save --wiki WIKI PAGE FILE --summary EXACT_LOCALIZED_SUMMARY --update`; original commands, native PIDs/exits and readbacks are in the per-step `.result.json` files. Ownership/authentication/edit ACL checks ran natively on each write. Fresh pre-write source guards and exact predecessor reads passed. Stable page-info/content/page-info reads and bounded rendered HTTP200/headings passed after every save. Reviewed diffs applied to each actual predecessor reproduce the actual result exactly. Six versionless install commands and the Go constructor copy exactly from rendered code; highlighting spans were joined normally, with ASCII34 URL quotes and no typographic quote substitution.

[Exact sequence/source/summaries/diff URLs](sequence-proof.json) and [live history proof](history-proof.json) retain all seven logical summaries plus the two labelled baseline entries. Both previous cumulative revisions1793202869/1793202888 remain in live history. Original evidence hashes are unchanged; initial staged sources/renderings/metadata are preserved as `prior-cs.*` and `prior-en.*`.

Fresh production before/after guards remained CS1783860648 / `8ea88de825d7b3823aee1d4ff8fd2704c9eb2f431cfbb944643927eabde3fd13` and EN1777543182 / `8006293f735a7e6f45c04d2d59ad82a003afa4547db1ddb38f380504e1e107d3`. Both exact target identities and ACL255 passed. Final native reciprocal language-link verification passed. Final owner is this session, container **up**, managed ref master, **pending null**, with no active owned operation. The aggregate manifests remain preview/check inputs; future production requires exact changeset approval and real predecessor readback.

Original handles72433/94552/38314/98723/68984 are consumed and all18 exact save/observer PIDs are gone. Two evidence assertions initially stopped continuation after already-successful saves: differing filename labels, then differing GNU/difflib alignment of a repeated blank line. Exact source/render checks had passed; patch-application proof reconciled both without repeating a write. Original scripts/failure reconciliation remain alongside results. See [effects](effects.json).

Monitoring used the documented visible owner fallback: retained840 watcher catalog/config unavailable from the selected package; no substitute watcher or CI operation. Selected runtime g650/provider d50 retained. Session, cluster and staging remain open/running. Previews require internal development routing/DNS. No further client, SDK, browser or link campaign.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
