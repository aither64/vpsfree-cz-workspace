# KB counterpart review: L11-K and D12

Current K12 status: all eight former fallback hrefs / 18 occurrences reevaluated. The D12 candidate below adds six href mappings / 15 occurrences, yielding **37 exact hrefs / 67 occurrences mapped** and **two hrefs / three occurrences unresolved**. It awaits main/lead semantic acceptance before application copy. The L11 evidence below is historical; its strict missing-anchor decisions and infrastructure language classification are superseded by D12.

## Historical L11-K checkpoint
Status: complete bounded candidate; architect0 confirmed fallback and root-alias decisions, awaiting lead/map acceptance. The map contains only verified page destinations and explicit section pairs; no KB or application changes were made.
Observed on 2026-11-07 UTC. Consumed implementer2’s [exact KB inventory](language-link-kb-inventory.json) at article head `c829fbf4abcd7f7ab47b44386b3d12ec39090b55`: **70 href occurrences,39 distinct exact hrefs,39 articles,27 distinct page paths including root**. There are26 nonroot IDs, not39 pages. Inventory source context/line/ordinal remains authoritative; no duplicate corpus scan.
Candidate [kb-link-map.json](kb-link-map.json): schema1,23 pages and9 explicit fragment pairs;31 exact source hrefs/52 occurrences can resolve to English. Eight exact hrefs/18 occurrences remain unchanged. Target `fragments` values omit the leading `#`; unlisted nonempty fragments must preserve the original entire link. Queries/delimiters are not modified; the current39 exact KB hrefs contain no query component/entity-encoded form. Root key `domů` is observed, not inferred from an empty slash path; `aliases: {"/": "domů"}` records the actual root identity under architect0’s D11 addition.
Native `kb-page get --wiki cz PAGE` and `--wiki org PAGE` supplied source identity/existence and SHA-256. Requests were restricted to linked Czech pages and English candidates evidenced by `<page>` values or actual language-switch links. Public rendered reads verified the actual language links, page identities and target IDs. Public pages and native source were cached only in disposable `/tmp` for inspection; credentials, hidden/private fields and full pages are absent from this record/map. No KB-wide enumeration, new slug guessing, writes, blog/index/ref edits, builds or services.
## Root and translation authority
The rendered Czech root `https://kb.vpsfree.cz/` exposes DokuWiki page ID `domů` in JSINFO/hidden form values and its actual language switch points to `https://kb.vpsfree.org/home`. Native Czech `domů` has `<page>home</page>`; native English `home` exists. This is a verified root pair. No empty page ID or guessed startpage is stored.
Many English pages omit an explicit `<page>` tag. Those pairs use the actual Czech language-switch link plus an existing English target; matching titles or domain substitution alone were never accepted. Seven pairs have matching explicit tags in both sources. The Docker moved-guide pair has inverse tag values (`manuals:vps:vpsadminos:docker` in Czech; `navody:vps:vpsadminos:docker` in English); the actual Czech language switch explicitly points to the English moved-guide notice. Both notices have equivalent meaning. The existing destination is retained rather than following an unlinked replacement page.
## Candidate page evidence
Each row lists exact public URLs, observed tags and stable native-source hashes. Raw rendered response hashes follow separately; HTML can include dynamic presentation state, so source hashes are the content receipt.
| Czech ID / evidence URL | Exact English target | Tags CZ / EN | Authority |
| --- | --- | --- | --- |
| [domů](https://kb.vpsfree.cz/) | https://kb.vpsfree.org/home | `home` / `(none)` | actual Czech language switch + existing English target |
| [informace:chat](https://kb.vpsfree.cz/informace/chat) | https://kb.vpsfree.org/information/chat | `information:chat` / `(none)` | actual Czech language switch + existing English target |
| [informace:ip_adresy](https://kb.vpsfree.cz/informace/ip_adresy) | https://kb.vpsfree.org/information/ip_addresses | `information:ip_addresses` / `(none)` | actual Czech language switch + existing English target |
| [informace:kam_psat](https://kb.vpsfree.cz/informace/kam_psat) | https://kb.vpsfree.org/information/where_to_write | `information:where_to_write` / `(none)` | actual Czech language switch + existing English target |
| [informace:komunikace](https://kb.vpsfree.cz/informace/komunikace) | https://kb.vpsfree.org/information/communication | `information:communication` / `(none)` | actual Czech language switch + existing English target |
| [informace:podpora](https://kb.vpsfree.cz/informace/podpora) | https://kb.vpsfree.org/information/support | `information:support` / `(none)` | actual Czech language switch + existing English target |
| [navody:server:gre](https://kb.vpsfree.cz/navody/server/gre) | https://kb.vpsfree.org/manuals/server/gre | `manuals:server:gre` / `manuals:server:gre` | matching explicit tags + actual Czech language switch |
| [navody:vps:api](https://kb.vpsfree.cz/navody/vps/api) | https://kb.vpsfree.org/manuals/vps/api | `manuals:vps:api` / `manuals:vps:api` | matching explicit tags + actual Czech language switch |
| [navody:vps:cgroups](https://kb.vpsfree.cz/navody/vps/cgroups) | https://kb.vpsfree.org/manuals/vps/cgroups | `manuals:vps:cgroups` / `(none)` | actual Czech language switch + existing English target |
| [navody:vps:datasety](https://kb.vpsfree.cz/navody/vps/datasety) | https://kb.vpsfree.org/manuals/vps/datasets | `manuals:vps:datasets` / `manuals:vps:datasets` | matching explicit tags + actual Czech language switch |
| [navody:vps:exporty](https://kb.vpsfree.cz/navody/vps/exporty) | https://kb.vpsfree.org/manuals/vps/exports | `manuals:vps:exports` / `manuals:vps:exports` | matching explicit tags + actual Czech language switch |
| [navody:vps:konzole](https://kb.vpsfree.cz/navody/vps/konzole) | https://kb.vpsfree.org/manuals/vps/console | `manuals:vps:console` / `(none)` | actual Czech language switch + existing English target |
| [navody:vps:kvm](https://kb.vpsfree.cz/navody/vps/kvm) | https://kb.vpsfree.org/manuals/vps/kvm | `manuals:vps:kvm` / `manuals:vps:kvm` | matching explicit tags + actual Czech language switch |
| [navody:vps:oprava](https://kb.vpsfree.cz/navody/vps/oprava) | https://kb.vpsfree.org/manuals/vps/repair | `manuals:vps:repair` / `(none)` | actual Czech language switch + existing English target |
| [navody:vps:playgroundvps](https://kb.vpsfree.cz/navody/vps/playgroundvps) | https://kb.vpsfree.org/manuals/vps/playgroundvps | `manuals:vps:playgroundvps` / `(none)` | actual Czech language switch + existing English target |
| [navody:vps:prenosy](https://kb.vpsfree.cz/navody/vps/prenosy) | https://kb.vpsfree.org/manuals/vps/traffic | `manuals:vps:traffic` / `(none)` | actual Czech language switch + existing English target |
| [navody:vps:rdns](https://kb.vpsfree.cz/navody/vps/rdns) | https://kb.vpsfree.org/manuals/vps/rdns | `manuals:vps:rdns` / `(none)` | actual Czech language switch + existing English target |
| [navody:vps:sprava](https://kb.vpsfree.cz/navody/vps/sprava) | https://kb.vpsfree.org/manuals/vps/management | `manuals:vps:management` / `(none)` | actual Czech language switch + existing English target |
| [navody:vps:start_menu](https://kb.vpsfree.cz/navody/vps/start_menu) | https://kb.vpsfree.org/manuals/vps/start_menu | `manuals:vps:start_menu` / `(none)` | actual Czech language switch + existing English target |
| [navody:vps:uzivatele](https://kb.vpsfree.cz/navody/vps/uzivatele) | https://kb.vpsfree.org/manuals/vps/users | `manuals:vps:users` / `manuals:vps:users` | matching explicit tags + actual Czech language switch |
| [navody:vps:vpsadminos](https://kb.vpsfree.cz/navody/vps/vpsadminos) | https://kb.vpsfree.org/manuals/vps/vpsadminos | `manuals:vps:vpsadminos` / `manuals:vps:vpsadminos` | matching explicit tags + actual Czech language switch |
| [navody:vps:vpsadminos:docker](https://kb.vpsfree.cz/navody/vps/vpsadminos/docker) | https://kb.vpsfree.org/manuals/vps/vpsadminos/docker | `manuals:vps:vpsadminos:docker` / `navody:vps:vpsadminos:docker` | actual Czech language switch + existing English target |
| [navody:vps:vpsadminos:oprava](https://kb.vpsfree.cz/navody/vps/vpsadminos/oprava) | https://kb.vpsfree.org/manuals/vps/vpsadminos/recovery | `manuals:vps:vpsadminos:recovery` / `(none)` | actual Czech language switch + existing English target |

| Czech ID | CZ source SHA-256 | EN source SHA-256 |
| --- | --- | --- |
| domů | `6c45521cc3d1dbf52fa219ceec3749f4f234cb6bd3a916bd0539094950ae356a` | `b5de1b4ac7a08212a3fc8197779198d8a91bf347730c19f416fe3597de506a79` |
| informace:chat | `f5c5de94e28a7593ae2498f717b122c459fef5cc021deb739868fb6cb4c4dbe8` | `b7e35c64fb298690e2e553c1298efa904ab8e8507a647fd810fa6b50e216cbe4` |
| informace:ip_adresy | `7914883be98377aa410e948c05cb492af10261706b434a2c805b4c6f1f532dee` | `851b39392ee6a2fda747ea73cffde4e103549f1d4773b75bddc79a0a549ab638` |
| informace:kam_psat | `3139216db2dbcad1222f5730121a3b4a7b6b4040da7a756962e50eb8be2ab706` | `43d6ac544a9a5f43cc74bce4370623bbab711c99551484b2d4ddb373951d8625` |
| informace:komunikace | `4f28aabd6cb06adae28b5ebadfcf5e0c30baa1030c94fc2860c9e04c548a8d54` | `f89f886f46854d62727dc6431a3dec9b492dc338d7cd56b1bea097b7c9d428d4` |
| informace:podpora | `54b27fa306fbf691e649fa6ba3cbc8093a7775886c9f49cfa6d2d066b6666bd1` | `29dd985028360075e1f7c25f744d0234d10c8f06ee4e38d7fa4e9823265595e6` |
| navody:server:gre | `4514cce0edc72864294f9d48b7d28c23f208d25e8bf622b11d74f013d9809465` | `06ca0035a8374121a2dffe5b215ba9fda80bea8794ba7920955d638a45e735ea` |
| navody:vps:api | `d18fbda8e3945ce77fc809b740432b90aef1ac7d5641c7635773034b2c887904` | `5cb41ae1d666de9f6b5cb679080c3104b1a56ebd14303d96af1e99696d4e72fd` |
| navody:vps:cgroups | `38c891564fe3edb633d9d06c3dec4abca8bbc7d4ef5f6d605d3c5711e6f00ecd` | `0017e3ce451a5a579a4926968082534511cc94572483235f4ebdcb2311fee114` |
| navody:vps:datasety | `26f4917e483ca28d9f98bfd2180f26f5e31501ed7e709034384e51d2e55a4899` | `8545f2bc0bd7fc74161a6d175d5fc679dcc6a5869397a75fb73afb055dcbc8f6` |
| navody:vps:exporty | `376ca7ab3a7df3951b930c0741ee39306b8b186d9b66b3b36ff0f1c0d35823ab` | `94889260e87f0df66a84cfc56800abddd58403fd92bc94d575c0e35b82df3a9d` |
| navody:vps:konzole | `ba9b4ecc2d961266753ffce1466af9d6a0cf912d93402ab0abab7e69eac6a213` | `27a43f1ec8d596f47037f62348f2bec47d8cdcc31b67582fff07477e29a2eee2` |
| navody:vps:kvm | `4c302a5e85f014462c48b90902632674108ca707d985123bf43a6594c1f8c4b9` | `e16daac7e0361cfa9a108c789bd2146b5ebf158adffbef117e267d1413e552c9` |
| navody:vps:oprava | `69b8151f21d0da943d5de0786c083244075c2ee35faf0da3dff15e1f34cfb3e6` | `85322ff0392119eef9ad82d2c056b6b4ad5c78d3027d0fa4107b99502a899c89` |
| navody:vps:playgroundvps | `c5ee993f56223c69c252f1b74eb739745b1d7a740c9e104822ac8e5e7025fe67` | `29de1534736b157964740b4af5496bd8aec10d027e3f20c1ef2ea65cf518425f` |
| navody:vps:prenosy | `e5ca97d3e5d24d65a8855ea858e04a31ae63c34d03beeabd46ef912c3f5a7997` | `8590b26f4949f2921b72fc9778eca9307f823390f58fca260fca8e51c186cf32` |
| navody:vps:rdns | `ec1153094c1fca5a2fabf1c35509b04205817f566f7f055fa1c0a9b971f1f41e` | `d2a254fcd3c22b79a66bf633037e4dee7097ced99334bc683f72f6be3aba4a49` |
| navody:vps:sprava | `371efdd755caa53d959dcf75dad949dcf9e911cdfb730ae696543a69ad13a8fc` | `bdcfc22911d35c8b24f71f16a8a6fb01f40eb5d1d02a0ea374d0d09f0d9cb14a` |
| navody:vps:start_menu | `b9fb16e264b2a9539edfd2866a795f408db2500ad19a98d1c680412092778506` | `d01c4a90a6305d1d8af80e7f7fa5af95ea4d3b60d130fe87f8274c5cd5ac1534` |
| navody:vps:uzivatele | `2a7d93880ba332933bd263326dacaa9a0053d012ed2655da4b2b27159e943806` | `38b308fba2bddf142e303aba62ae336727aa52d536269aa1630248c78aa07c26` |
| navody:vps:vpsadminos | `9b69ad269712e41d63f254ef27f0c9a340a46745ef7c89223a971f7d64b0fac3` | `f1f9f99463a318ab54b029bc685fbf5ae8c2daf521ee0117d4ade4862c46d2b5` |
| navody:vps:vpsadminos:docker | `bbdf46e5d4014d05f1f6189302a80e8e51f9bced9c00afa9ce886a9312d6345b` | `1a6ad3c95b812bfb8775bf6b682ab4fb2d98d3c96fec7458e9fdb6d34d93ebe2` |
| navody:vps:vpsadminos:oprava | `9e2f618274ca8736452e48a7c0d4e757fa68afb625c532bfde4aba2ab6fbc0af` | `ab8cb53af816fcb72c1b3f3c458bfd2095809b7f9f368a7542dfd7ecae03ae20` |

## Verified fragment meanings
All nine source and target IDs were present in the current rendered pages. Source text and equivalent English sections were read; equal spelling alone was not used.
| Czech page | Source fragment → English fragment | Equivalent section meaning |
| --- | --- | --- |
| informace:chat | `bot` → `bot` | vpsfbot archives messages/responds to channel commands; both link its repository. |
| informace:chat | `irc` → `irc` | Same Libera IRC host/channel and current archive. |
| navody:vps:api | `prace_s_api` → `working_with_the_api` | HaveAPI self-description, available clients and REST access. |
| navody:vps:konzole | `zajisteni_spravne_funkce` → `ensuring_proper_functioning` | Matching locale/encoding, TERM, mc options and bashrc console configuration. |
| navody:vps:prenosy | `monitor_v_cli` → `cli_monitor` | vpsfreectl network top TUI, same options and keyboard controls. |
| navody:vps:sprava | `klonovani_vps` → `cloning_vpss` | Clone to new/existing VPS; overwrite warning and target-selection form. |
| navody:vps:uzivatele | `detailni_nastaveni` → `advanced_settings` | Per-template recipient addresses and disabling selected email deliveries. |
| navody:vps:uzivatele | `dvoufaktorove_prihlasovani_2fa` → `two-factor_authentication_2fa` | TOTP/passkeys, one configured extra device, token-auth requirement and profile enablement. |
| navody:vps:vpsadminos:oprava | `nouzovy_rezim` → `rescue_mode` | Temporary template boot for repairs, same VPS settings, original disk under /mnt/vps and restart exit. |

## Historical L11 unmapped decisions (superseded by D12)
| Exact original href | Count / affected articles | Reason |
| --- | --- | --- |
| `https://kb.vpsfree.cz/informace/chat#bouncer` | 1 / wp-390 | linked source fragment absent from both current rendered counterparts; no certified equivalent section |
| `https://kb.vpsfree.cz/informace/infrastruktura` | 1 / wp-667 | L11 incorrectly called the identical source Czech; D12 reread confirms English Hardware Inventory and proposes mapping it. |
| `https://kb.vpsfree.cz/informace/openvz` | 2 / wp-215, wp-709 | Czech source page absent; no evidenced counterpart |
| `https://kb.vpsfree.cz/navody/vps/api#cli` | 9 / wp-253, wp-264, wp-284, wp-455, wp-474, wp-490, wp-601, wp-709 | linked source fragment absent from both current rendered counterparts; no certified equivalent section |
| `https://kb.vpsfree.cz/navody/vps/datasety#stahovani_zaloh` | 1 / wp-284 | linked source fragment absent from both current rendered counterparts; no certified equivalent section |
| `https://kb.vpsfree.cz/navody/vps/vpsadminos#user_namespaces` | 1 / wp-547 | linked source fragment absent from both current rendered counterparts; no certified equivalent section |
| `https://kb.vpsfree.cz/navody/vps/vpsadminos/storage` | 2 / wp-615, wp-713 | Czech source page absent; no evidenced counterpart |
| `https://kb.vpsfree.cz/navody/vps/zalohovani` | 1 / wp-24 | Czech source page absent; no evidenced counterpart |

The old `#cli` occurs9 times. Current API headings distinguish installing the client from using CLI; neither page has a rendered `cli` anchor. Mapping it to either new section would be a guess. `#bouncer`, `#stahovani_zaloh` and `#user_namespaces` are likewise absent in both current counterparts. The candidate never removes these fragments.
Three native Czech reads explicitly report absent pages: `informace:openvz`, `navody:vps:vpsadminos:storage`, `navody:vps:zalohovani`; their public views have no canonical existing-page/language-switch evidence. No speculative English ID was requested for these.
D12 factual correction to the original infrastructure rejection: the actual switch is `https://kb.vpsfree.cz/informace/infrastruktura` → `https://kb.vpsfree.org/information/infrastructure`; both native sources have SHA-256 `cbe2f4ceae237452666acaf2d0d62aa11195f7e0af2758f1341a24b9aef7f0a0`. L11 incorrectly described that identical source as Czech prose. Hash identity establishes byte identity, not language. Rereading the content shows an English **Hardware Inventory**, generated `2026-04-14 03:34:10`, with English CPU, RAM, DIMMs, System, Storage and Network labels. The prior omission and architect concurrence relied on my incorrect description; D12 corrects that premise with the actual content and proposes the English destination below.

## Raw rendered evidence hashes
| Czech ID | CZ response SHA-256 | EN response SHA-256 |
| --- | --- | --- |
| domů | `31ea94ecd5027633b48571726bd3092eefba0043517f05e0b2da1e11ab0e199d` | `6f0c85bd66e6124fae53cbb00cce5efb1d132428f354a694132652dd87ad109f` |
| informace:chat | `bc55e261ac08be1bd93531ee4347a6d3f6f9f07782846e061328b256fab8ee3f` | `c2c1e64ae0ef0c6a1e18abcc814e4777f418328e2a685a3bda21ef0363db140e` |
| informace:ip_adresy | `9edf1b4c4afdfe4d97b5df02eebe2fe4d756113c0f7dad58108ec9bf3663e6d2` | `778581835bfca27586bbe1458284981055b6945e7130a4cc1056431adc198094` |
| informace:kam_psat | `2b8d97e42252dc61db2ccb3c8eb67a4640cfcaee6bede1e3ba4e740b5b03d237` | `ef22165910e61f29e676316e00d74586198bf43c4317d54988c6771a55cb81b9` |
| informace:komunikace | `0a49f5e3ad5edf2d58810448d85a92ab47f755f1b2ca0c916d0307f92b4e4224` | `b0632dc214ff330f44f2f97542b184d5f6a27abb3f367b1f99961fcaf2eedffa` |
| informace:podpora | `c7452fbb67914527c6bdd6255c771fd38ca64e3985922526a50604b280aeaa80` | `3d0ed2c332ea048764cc9aed7ac337b7ad35d81719d877a021aaec117afd0980` |
| navody:server:gre | `013761a8bcbf2630c9942bcf92bdd8ec6cf849ae680e92eac6a52bd2b393e1a1` | `b67f6004739ea8d86c005a62fded512b0b3629b32477d780810ab027c3a42049` |
| navody:vps:api | `81339a1afe8f338559f31a765056365d0a42c18e16474a9cb60aec110bbce422` | `5037cf43069811b9de08b8363d3fc9ca804cd4e7c755e20ec88d635d6b8de648` |
| navody:vps:cgroups | `2e52187baf14d866a582fb7fd351feed8ed9e0590c5d5ffd09989566998b474f` | `0ea2853dc73105d8fc5443ef8b60bedfb1eb555382fc0cff086483b9b6689114` |
| navody:vps:datasety | `ca9ebc2b6add687e09f0140093283ca540489085245c4a5ded01e7691d115327` | `b35f32b52ded0e4647cf40ba23e3e55ce9bd0821b61ea242ef1fcde18cc32e9e` |
| navody:vps:exporty | `906ce9cf08ad2878e00d0c37103907895a1eddf5b6ce4fd3e393d2189bb164dd` | `07f934c9a7503927aaaa9a0a0c2b44c6bd4539e0a7d69a8c3bb7960909e6dd2f` |
| navody:vps:konzole | `2981f94fed1e998c3392e477352fce3dcf9ddd04876bf573662375f196a36fdc` | `b7acfa1923f8ee234421584cd6a658eec38dae86f84f539dd90dae7134d4735e` |
| navody:vps:kvm | `650b82c688bbc2d7f233be50c54f2ea78b511d8814509a4332b1c5e6775ca8e4` | `cfc51e71d9c28e476c3e51c3756d913cf5f030d8ae56214863e59d768ff4ae84` |
| navody:vps:oprava | `2c7c1a924b175aa417ace5b325ffa2497356ecaeb548f32051203e2cc5c5809b` | `43a576ac89fa39eb11d3e5932b2d5151fe38c8a211017aec4a0967d0e9bf116d` |
| navody:vps:playgroundvps | `806c33605b0824896343b5c73529ff365c28240371f7dfc402dca0c68a8b5546` | `fda76f0f94fb93b8042aab44437605d084f0aae873b4b8dd362991a1ba952767` |
| navody:vps:prenosy | `20ebff4fca67f33ea56631cf027c58ee85129c69417c200bd68bac315bff117c` | `0b874d81412ec80590a6dd3c657a5acab690717b9d20034ec79626c832162158` |
| navody:vps:rdns | `376646a6cf83de2c80d0e052f5f25eb70751cd634428a9235a78e86cdbf63d3c` | `9f9168f859b05951778c054cf1cd7ff9d244fa74ba1998eba3eb1257c5c7afaa` |
| navody:vps:sprava | `ecbbf6ba852ad40180f804821afc24197467d168b76b9e7e4edeb03bf7ac797a` | `0797d88ce5cf21314a2b60bc024f6faaea78a32aca96836ede60e3bf4c27acde` |
| navody:vps:start_menu | `1852ff01988d8ef589892185c68a507acea20f07fda8cb55b32bc95ed367a6da` | `b644833175635b5ba4ef4d4bbc7d9bd00b3d866e5e4312487c578e29e0dc9d4a` |
| navody:vps:uzivatele | `4f739c0830d936986ba8e60d9ff2523937386b62a99489ee3d1fb29e57bb9d2e` | `7e47f314e7b42c80e1acf1b7a29ee54106935e2d1ec8d506d5503792e066bc61` |
| navody:vps:vpsadminos | `5b5d0cf8c34fad2a070ead3758d1e842178397c5c54836f02492ed9bb60e52e2` | `6b0c91d8bc7fec2bbae7526d1a6d0e61f224384feae7e7ddf3b7ec2b03980bc2` |
| navody:vps:vpsadminos:docker | `398c9308c7f2adcc81831fe28c5fedc6f1ea457a2b8c367e40cf32ec74c9ec93` | `8651140327eb94c82c927a3712141f5e70dbf2295db95c9793b9a2d284d8942d` |
| navody:vps:vpsadminos:oprava | `e1e266538d79b6b5c91bc7ddc7255cec2c08deadfe1df58b1b4bbfa97a39c8e6` | `a77875d9a078c0d81b596f965d4a1ec3fc11ef9cf15f19eded81fe96c47c0477` |

## Validation and handoff
Candidate validation confirms23 canonical Czech keys, exact observed HTTPS English targets without query/fragment,9 source/target IDs present, and complete disposition of all39 hrefs/70 occurrences. All candidate target sources exist; unknowns remain outside the map. No live system, production publication or human language-review claim. Architect owns renderer normalization/fallback contract; lead owns map acceptance and any meaningful copy decision.
Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/>.

Final candidate SHA-256 (including observed root alias): `5b3fee0f5b6ffcf4b80ecedd6fce3967ddc23482e05ec3cf901f14b55a6f1b17`. Architect0 confirmed the23-page/9-fragment dispositions, absence fallbacks, Docker switch authority and root identity via same-session clarification. Candidate acceptance remains with the lead; no application copy or index action by L11-K.


## D12 semantic reevaluation

Status: evidence/candidate complete, **pending main/lead semantic acceptance**. Observed 2026-11-07 UTC. D12 replaces the rule that a missing historic Czech page/ID alone prevents mapping. This pass reused the existing exact inventory, the cached public/native KB evidence and only the 18 affected EN/CS link contexts. No corpus reinventory, article edits, wiki writes, application/index/ref changes, builds or services were performed. Original article claims, labels, URLs and dates remain source bytes; selecting present documentation does not update their historical assertions.

The accepted L11 candidate SHA-256 was `5b3fee0f5b6ffcf4b80ecedd6fce3967ddc23482e05ec3cf901f14b55a6f1b17`. All 23 page targets, nine same-page fragment pairs and the observed root alias are preserved. The new candidate has 26 page entries, ten same-page fragment pairs and two explicit cross-page `fragment_targets`; the latter use D12's settled contract, without a per-article mechanism. Candidate SHA-256: `c869a107479cb980b2473eb54250686772dc363c87a2af6afdf0f7d99abd2cbe`.

### Nine CLI occurrences: one evidenced section

For **each of the following nine occurrences**, propose the exact target <https://kb.vpsfree.org/manuals/vps/api#using_cli> for `https://kb.vpsfree.cz/navody/vps/api#cli`. The existing API page pair has matching `manuals:vps:api` tags and the actual Czech language switch. Current rendered HTML contains `id="using_cli"`, headed **Using CLI**. The native section starts with `vpsfreectl --help`, resource/action/parameter syntax, authentication and output options. Its command list includes `vps migrate_many`, `snapshot download`, `snapshot send`, `backup dataset`, `backup vps` and `ip_traffic top`; its resources include `user_request.registration`. Subsections explain authentication, actions/parameters and output formatting. The existing page also has client installation and update guidance; those are available on the same page, but these nine link labels refer to the client or its use, not exclusively to installation. Thus the common using section fits all nine contexts. No old `cli` anchor is invented and no article-specific override is needed.

Ordinals below are the inventory's article-wide href ordinals; body lines retain that inventory's coordinates.

| Article / ordinal / body line | Actual source-context intent (EN checked against CS) | Fit to Using CLI |
| --- | --- | --- |
| wp-253 / 7 / 10 | New CLI features described in the HaveAPI v0.4 email and linked KB article. | General CLI operation/options; link does not request only installation or an unchanged release snapshot. |
| wp-264 / 4 / 11 | Linked `vpsfree-client` release, bug fixes and new administrator command `vps migrate_many`. | Actual command is listed in the target's CLI help. Release-note link and historical release claim stay unchanged. |
| wp-284 / 2 / 5 | Linked “download VPS/NAS backups from the CLI”; immediate downloads and archive/incremental ZFS streams. | Target lists both snapshot commands and the backup commands, establishing CLI entry point. Detailed downloading link is mapped separately below. |
| wp-284 / 3 / 6 | A separate linked `vpsfree-client` sentence introduces four commands for manual/automated backup downloads. | All four named commands occur in the target command list. This is the second occurrence in this article, not the first counted twice. |
| wp-455 / 3 / 9 | Linked `vpsfreectl` gains `ip_traffic top` terminal traffic monitor. | Exact command appears in target help; article's separate monitor-section link remains the accepted `cli_monitor` pair. |
| wp-474 / 5 / 13 | Users of linked `vpsfree-client`/other HaveAPI clients should update after a protocol change. | Link identifies the client, with operation/version/compatibility options in the target and Updates guidance on the same page; no new historical compatibility claim. |
| wp-490 / 1 / 6 | Membership applications/personal-detail requests available through API; example submitting an application with linked `vpsfreectl`. | Target documents resource/action calls and lists `user_request.registration`. It need not invent a new application example. |
| wp-601 / 8 / 9 | Linked `vpsfreectl`/API-library users must update after the 2FA protocol break. | Same documented client and authentication/version options; same-page update guidance is reachable. Source's historical warning remains unchanged. |
| wp-709 / 3 / 9 | Author plans a future linked `vpsfreectl` rescue-mode backup-restore option; manual restore already possible. | Link identifies the documented CLI. Mapping does not claim the planned restore command exists; article's future tense remains intact. |

### Other supported destinations: six occurrences

These five rows cover five additional hrefs / six occurrences. Together with the nine CLI occurrences they resolve 15 of the former 18.

| Original href / occurrence | Exact proposed English URL | Observed section/content and equivalence proof |
| --- | --- | --- |
| `https://kb.vpsfree.cz/navody/vps/datasety#stahovani_zaloh`; wp-284 / ordinal 4 / body line 21 | https://kb.vpsfree.org/manuals/vps/backups#downloading_backups | Link recommends detailed command/options/examples after the article's four download/backup commands. Actual **Downloading Backups**, `id="downloading_backups"`, introduces immediate/automated downloads and tar.gz/incremental ZFS streams. Following sections give all four commands, resume/checksum/rate options and examples. Existing English Datasets → More Information → **Backups**, plus Home → **Backups, restoration and downloads**, explicitly navigate here. Use `fragment_targets.stahovani_zaloh`; other dataset links keep their old target. |
| `https://kb.vpsfree.cz/navody/vps/vpsadminos#user_namespaces`; wp-547 / ordinal 6 / body line 6 | https://kb.vpsfree.org/manuals/vps/userns#user_namespace | Link explains osctl configuring user namespaces for proper VPS isolation. Actual H1 **User namespace**, `id="user_namespace"`, explains process isolation, host-unprivileged IDs becoming root inside the namespace, a namespace for every VPS and unique member UID/GID blocks protecting other members' data. English Home explicitly links **User namespaces** to this page; targeted search confirms it. Use `fragment_targets.user_namespaces`; other vpsAdminOS links keep their old target. |
| `https://kb.vpsfree.cz/navody/vps/vpsadminos/storage`; wp-615 / ordinal 2 / body line 20 and wp-713 / ordinal 4 / body line 7 | https://kb.vpsfree.org/manuals/vps/vpsadminos/storage | wp-615's preceding NFS paragraphs describe exports/host allowlists, mounting within the VPS, `/etc/fstab`/systemd examples and inability to share another VPS's disk. wp-713 asks readers to check NFS configuration and mount volumes inside the VPS before migration. Topic searches `storage`/`backups` expose this existing English page with `<page>manuals:vps:vpsadminos:storage</page>`. Actual H1 **Datasets, snapshots, mounts and exports on vpsAdminOS**, `id="datasets_snapshots_mounts_and_exports_on_vpsadminos"`; **NAS**, **Exports**, **Mounting exports** (IDs `nas`, `exports`, `mounting_exports`) document precisely those operations, limits and examples. Missing old Czech page is not used to reject this equivalent English guide. |
| `https://kb.vpsfree.cz/navody/vps/zalohovani`; wp-24 / ordinal 1 / body line 5 | https://kb.vpsfree.org/manuals/vps/backups | Historical article describes daily rsync/snapshot backups, control-panel access and `.zfs/snapshot`. Current **Backups** (`id="backups"`) explains snapshot preservation, daily VPS backup snapshots, Backups → VPS backups, read/restore access, with filesystem/snapshot examples later in the page. English Home and Datasets navigate to this actual guide. General backup-documentation intent matches; historical `/vpsadmin_backuper`, rsync and timing claims in the article are not rewritten or claimed as current page behavior. |
| `https://kb.vpsfree.cz/informace/infrastruktura`; wp-667 / ordinal 6 / body line 13 | https://kb.vpsfree.org/information/infrastructure | Article explicitly says the hardware inventory is in the KB. Actual Czech switch points here, Home/search exposes **Hardware Inventory**, and rendered `id="hardware_inventory"` exists. Native source is the English machine inventory with CPU/RAM/DIMMs/System/Storage/Network labels. L11's identical-hash ⇒ Czech-language inference was wrong, as corrected above. The current inventory is the same topic without changing the article's historical hardware claims. |

### Remaining three occurrences: bounded semantic checks found no equivalent

These outcomes follow actual context/search/content inspection, not merely missing old source pages or anchors. They are not claims that no English counterpart could ever exist.

| Original href / occurrence | Intent and inspected English alternatives | Disposition |
| --- | --- | --- |
| `https://kb.vpsfree.cz/informace/chat#bouncer`; wp-390 / ordinal 3 / body line 14 | Article offers members an **IRC bouncer (ZNC)** and says to ask IRC/support for access. Searches `bouncer` and `IRC bouncer` return only **Chat**; `ZNC` returns no page. Existing English Chat has IRC connection details, Matrix and vpsfbot archive/lastlog commands; its sole bouncer mention says users **without** one may consult the archive/bot. That does not document the offered persistent ZNC service/access. No rendered bouncer section exists. | Keep exact original href. Mapping to bot/archive/IRC would change the function described; no equivalent ZNC service documentation was evidenced. |
| `https://kb.vpsfree.cz/informace/openvz`; wp-215 / ordinal 1 / body line 5 | Link names the association's original **OpenVZ container virtualization**, contrasted with requests for own kernels/other systems and KVM experimentation. Search `OpenVZ` returns only **IP Address Replacement**: its OpenVZ mention concerns `/128` IPv6 limitations. `OpenVZ Legacy` returns no page. Search `container virtualization` exposes **Virtualization platform vpsAdminOS** and **FAQ**, both read: they describe the current vpsAdminOS/LXC platform, shared kernel and KVM, not historic OpenVZ. | Keep exact original href. Current vpsAdminOS or LXC would misidentify the explicitly named historical platform; the incidental IPv6 note is not an equivalent overview. |
| Same OpenVZ href; wp-709 / ordinal 2 / body line 8 | Source contrasts **OpenVZ Legacy** allowing one VPS dataset mounted inside another (e.g. repair from playground) with the later vpsAdminOS rescue approach. The same bounded searches/candidates above were checked for this distinct intent. Current vpsAdminOS overview describes local ZFS datasets/rescue access; FAQ describes LXC, and IP replacement only IPv6. The evidenced vpsAdminOS storage page explicitly disallows mounting another VPS's dataset, confirming it cannot explain this old OpenVZ operation. | Keep exact original href. A rescue-mode/current-storage substitution would reverse the source's platform/operation distinction. |

### Navigation/search and content receipts

Public/native observations are from 2026-11-07 UTC. Only topic searches and evidenced candidates were read. English Home links `manuals:vps:userns` as **User namespaces** and `manuals:vps:backups` as **Backups, restoration and downloads**; English Datasets links `manuals:vps:backups` as **Backups**. Existing API/infrastructure language-switch evidence was reused. Native page SHA-256 identifies content; rendered SHA-256 identifies the response inspected for actual IDs. No credentials or complete wiki pages are retained here.

| Exact English page | Native source SHA-256 | Rendered response SHA-256 |
| --- | --- | --- |
| https://kb.vpsfree.org/manuals/vps/api | `5cb41ae1d666de9f6b5cb679080c3104b1a56ebd14303d96af1e99696d4e72fd` | `5037cf43069811b9de08b8363d3fc9ca804cd4e7c755e20ec88d635d6b8de648` |
| https://kb.vpsfree.org/manuals/vps/backups | `bf33238145ed6c10f5f88c76f202f27123f2fac4fbe6ba568438b6efc54052a4` | `7b6249d5d68b9ebbb3e9eaa7a8a592f50e8408d90c675234ccd29a8760d99581` |
| https://kb.vpsfree.org/manuals/vps/userns | `dcd72bea08bfd946b6d55f71d5b62fd03c50894ca77cc4f157498ab415955a57` | `eecce8f0ed40e95642f5a3f7fc8512f30517239db2e3c52262924c3c3b8e3159` |
| https://kb.vpsfree.org/manuals/vps/vpsadminos/storage | `e30a5ff6854422f351aa3fabdb8ed8b8419f096c9b4972ce210e7d8c784511cf` | `308d4f7fc1cb82d7bafc11a77a1aa82bfa94a66172f46b0cd1ca83d5fb56e4f4` |
| https://kb.vpsfree.org/information/infrastructure | `cbe2f4ceae237452666acaf2d0d62aa11195f7e0af2758f1341a24b9aef7f0a0` | `813de8b4696420bce2e94c940a4dac25d5375a3725b1e457ed0e75f84307a28e` |
| https://kb.vpsfree.org/information/chat | `b7e35c64fb298690e2e553c1298efa904ab8e8507a647fd810fa6b50e216cbe4` | `c2c1e64ae0ef0c6a1e18abcc814e4777f418328e2a685a3bda21ef0363db140e` |
| https://kb.vpsfree.org/information/ip_replacement | `553006618657e0f2438d1ee23dea5cf25404daaa19178b4518d997901d0234c2` | `de46ea7255e08676653297b8ab9baa0a1259f744c48314484287419ac7d8f8b8` |
| https://kb.vpsfree.org/information/vpsadminos | `45a1c32e673596171960509653bc597213445931dd07fde49dca7196d0d6225e` | `855158d15a2be533efbb60658f968fc7da2a6927774e739dd5971a778548e309` |
| https://kb.vpsfree.org/information/faq | `925afa0e713df74bd10b111b00374084c5116e43cd3dd06531602559b4dd1cbc` | `8525744a0b0fb9afe6ae7783a116e6798c146a943438a155dc15b1426e9d5a88` |

Navigation source receipts: Home `b5de1b4ac7a08212a3fc8197779198d8a91bf347730c19f416fe3597de506a79`; Datasets `8545f2bc0bd7fc74161a6d175d5fc679dcc6a5869397a75fb73afb055dcbc8f6`.

| Exact topic search URL | Observed useful result / inspected alternative | Response SHA-256 |
| --- | --- | --- |
| https://kb.vpsfree.org/?do=search&id=bouncer | Chat only; bouncer mention is absence/archive advice | `962ddfa897a4d04000e75ff57ba3769a11964700c360f38dbb92d4ab9030ae33` |
| https://kb.vpsfree.org/?do=search&id=OpenVZ | IP Address Replacement only; incidental IPv6 mention | `e496082791214dc24db3fc52ab40b69c61be20ceba4d3049a978432b60b28c32` |
| https://kb.vpsfree.org/?do=search&id=user%20namespaces | User namespace; also linked by Home | `6a993133221723fd86d6bda83b12827ed19c9e1ceafb3adaa718d3ae9ffbdec0` |
| https://kb.vpsfree.org/?do=search&id=backups | Backups and vpsAdminOS Storage among matching guides | `e1ddb5b57fc13fdbae642fa59d0bd74905f44af8b94971810d864637eb21557d` |
| https://kb.vpsfree.org/?do=search&id=storage | vpsAdminOS Storage among matching guides | `ecac044d0561253ed4e6b2a649c71526ac8d0e6e4b55ff261a6b30ae25e90e9d` |
| https://kb.vpsfree.org/?do=search&id=infrastructure | Hardware Inventory; Projects inspected but not a hardware-inventory substitute | `60e5b55ac6d8d21f66cd9e3adef5d332dd8be819a0f5fb3b346761d76d94152f` |
| https://kb.vpsfree.org/?do=search&id=ZNC | No matching pages | `03f2eb339e989d401aeb3a7e3c8de47c597bf957825cb1cefe3df980ca8b595d` |
| https://kb.vpsfree.org/?do=search&id=IRC%20bouncer | Chat only | `50ac6d857cfc6b0df61a2302c4da682f10838dcc9026c0a0664c916d81cebc5a` |
| https://kb.vpsfree.org/?do=search&id=OpenVZ%20Legacy | No matching pages | `d5ce24e57c0771d808bd53557123888fe36ec8244beb610e0ffeece839ba36a3` |
| https://kb.vpsfree.org/?do=search&id=container%20virtualization | vpsAdminOS overview and FAQ; both current LXC, not historical OpenVZ | `9d0b0142c3db4cda9fde3c06b1681ab1e0bc6f06f455a213831d2acbb6898a8e` |
| https://kb.vpsfree.org/?do=search&id=Hardware%20Inventory | Exact Hardware Inventory page | `4c0b0bab45d06a8383cbf8ca882e2688c0b62ca32f244aafb08ec92302614dd3` |

### Candidate reconciliation and next owner

All eight former fallback hrefs / 18 occurrences have explicit dispositions: six hrefs / 15 occurrences newly mapped; two hrefs / three occurrences retained. Combined with L11's 31 hrefs / 52 occurrences, the candidate covers **37 exact hrefs / 67 occurrences**, leaving **two exact hrefs / three occurrences**. Existing 23 targets/nine fragment pairs/root alias are unchanged. Queries/programmer anchors/source context are not rewritten; only the two evidenced moved sections use `fragment_targets`. The exact finite inventory contains no query forms; query preservation remains the renderer owner's responsibility under D12.

Quick static validation passed: schema/authority constraints; cached existence for all targets; actual rendered IDs for all ten same-page fragments and both cross-page fragments; preservation of every original 23 target/nine fragment/root-alias entry and all prior 31 href/52 occurrence destinations; complete 39 href/70 occurrence reconciliation. The candidate digest in this record matches the file bytes. These are local candidate/evidence checks, not a Hugo build or application test.

Main/lead owns semantic map acceptance. Implementer2 owns the accepted application copy and offline renderer checks, including cross-page precedence and harmless-query placement; K12 makes no application verification, publication, human-review or integration claim. No migrations or external content writes. Session remains open: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/>.

Additional bounded direct check (2026-11-07 12:33:07 UTC): `kb-page get --wiki org information:openvz` returned exit 1, `page does not exist: information:openvz`, with empty stdout; this excludes the exact orphan/unindexed English candidate and leaves the two OpenVZ occurrences unresolved. No further lookup or candidate/application change.
