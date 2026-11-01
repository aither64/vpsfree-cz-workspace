# KB06: client-selection continuation staged

Reviewed exact commit `1c7f990d9ccd61c510c22da18f4771cdaaef640b`; reviewer0 native01a18d63-0518-78a1-8367-0b37cdaae591 final GENERAL/history LOW: **NO FINDINGS / complete owned history / no redundant stream / NO MIGRATIONS**, accepted by lead. One ordinary public step06 save per language appended directly after step05, with no reset, baseline restore, replay, private-state edit, production write or save retry.

| Preview | Actual predecessor → step06 | Exact summary |
| --- | --- | --- |
| [CS](http://kb-cs.aitherdev.int.vpsfree.cz/navody/vps/api) | [1793369708 → 1793373737](http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody%3Avps%3Aapi&do=diff&rev2%5B0%5D=1793369708&rev2%5B1%5D=1793373737) | Upřesnění dynamických a generovaných klientů a odstranění zbytečných verzí z příkladů |
| [EN](http://kb-en.aitherdev.int.vpsfree.cz/manuals/vps/api) | [1793369764 → 1793373856](http://kb-en.aitherdev.int.vpsfree.cz/doku.php?id=manuals%3Avps%3Aapi&do=diff&rev2%5B0%5D=1793369764&rev2%5B1%5D=1793373856) | Clarify dynamic and generated clients and omit unnecessary versions from examples |

- CS source SHA256 `c62e8a04cc21400357010d25b31cd27842b07431debade64327b5b03bf43318f`.
- EN source SHA256 `0eb30a80f0b0ab8abb896f40fa4c947bbc330a12976c1c5ab5bdc8506d4dedc7`.

Fresh guards matched actual05 CS1793369708/c7b1f412… and EN1793369764/d6ca6635…. Both staging and production authenticated as aither with ACL255. Each `kb-page save --wiki WIKI PAGE FILE --summary SUMMARY --update` ran native owner/auth/ACL checks. Stable page-info/content/page-info, exact reviewed source and summary, and reviewed patch applied to the actual predecessor all passed. Original commands/PIDs/exits are in per-language `.result.json` files.

Both rendered pages return200, with all headings in source order. Each actual seven-item overview contains all eight expected links, including the renamed Dynamic and Generated heading IDs. Optional PHP/Python/JS selectors and old auth URL are absent; dynamic/generated labels and the generated TypeScript required schema-prefix prose are present. Four rendered code blocks equal their captured05 predecessors plus only the four intended transformations. Every other rendered block is byte-identical (36CS/33EN), including token handling and installation commands. Gem.bindir and the escaped Go constructor copy are checked with ASCII quotes; no quote/whitespace normalization. See [rendered code proof](rendered-code-proof.json) and [exact source/link/diff proof](final-proof.json).

Native reciprocal links, exact latest summaries, retained05 predecessors and every earlier separate revision passed: [history proof](history-proof.json). All previously preserved staging evidence hashes remain unchanged.

Fresh production before/after remains CS1783860648 / `8ea88de825d7b3823aee1d4ff8fd2704c9eb2f431cfbb944643927eabde3fd13`, EN1777543182 / `8006293f735a7e6f45c04d2d59ad82a003afa4547db1ddb38f380504e1e107d3`. Final owner is this session, container up, managed ref master, **pending null**. All four exact save/observer PIDs are gone; handles18288/9796/93960/8037 are consumed. No active owned operation; [effects](effects.json).

The first local CS verifier compared full PHP source directly with rendered code and stopped on GeSHi U+00A0 blank-line padding already present in the captured predecessor. Source/summary/render200/links had passed. The corrected check proved exact rendered-before→after transformations from retained artifacts without any repeated request/save or normalization. Original failure/script evidence remains. A diagnostic print used the last code-change label; authoritative result files retain the correct language/step identity. No content/render regression was found.

Known short public operations ran inline. No browser/client/runtime/install/package/provider campaign, CI or cluster/guest/0.32 endpoint query. Current4x public method reused; only routine evidence was written after review. Internal development DNS/routing is required. Production still needs direct exact-change approval and actual predecessor readback. Session, staging, cluster and private OAuth state remain open/running.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
