# Language link review

## L11-I read-only implementation inventory

Owner: `implementer2`. All 125 English HTML articles were inventoried at observed blog head `c829fbf4abcd7f7ab47b44386b3d12ec39090b55`. This is source-target evidence for D11; it does not choose renderer behavior or certify KB counterparts. No article prose was reread for this inventory.

Machine evidence: [complete exact-target inventory](language-link-inventory.json) and [KB-only authority handoff](language-link-kb-inventory.json). Each exact raw target includes occurrence counts, affected article IDs and individual anchor ordinals/source lines/raw `href` attributes. Complete raw attributes retain quoting and entity spelling; decoded URL parts are separate classification fields. The files contain no private snapshot or user records.

| Link class | Occurrences | Distinct exact targets | Affected articles |
| --- | ---: | ---: | ---: |
| blog | 134 | 119 | 73 |
| kb | 70 | 39 | 39 |
| external | 326 | 274 | 100 |
| mail | 1 | 1 | 1 |

Total: **531** live `a[href]` attributes. Counts of affected articles overlap. Blog targets are 55 article occurrences/44 exact targets/41 destination article IDs, 75 media occurrences/71 exact targets, two taxonomy/archive occurrences/two targets, and two self-fragment occurrences/two targets. There are **no unknown blog targets**, no blog legacy `?p=ID` links, no blog/KB `.org` host links and no blog/KB query strings in this corpus. Legacy-ID support was considered through authoritative `legacy_post_id`/manifest aliases, but none was needed for an actual occurrence.

### Exact blog article target set

Every match below comes from current CS/EN frontmatter `url` plus stable IDs in `data/articles.json`; original Czech `discussion_url` supplies the resolution base for relative links. No slug/title guessing is used. All 41 matched English destinations currently exist as drafts; source existence does not prove that a production page is rendered. Draft/missing-destination fallback remains architect-owned. All 55 matches are exact current routes.

| Exact original href | Destination ID / current English path | Count / source IDs |
| --- | --- | --- |
| `/byli-jsme-na-konferenci-installfest-2015/` | `wp-37` → `/we-attended-installfest-2015/` | 1: wp-269 |
| `/haveapi-v0-7-blokujici-akce/` | `wp-470` → `/haveapi-v0-7-blocking-actions/` | 1: wp-474 |
| `/jak-vyuzit-256-gb-ram-na-serveru/` | `wp-244` → `/how-to-use-256-gb-of-ram-in-a-server/` | 1: wp-343 |
| `/jsme-v-ankete-kristalova-lupa-hlasujte-pro-nas/` | `wp-114` → `/we-are-in-the-kristalova-lupa-awards-vote-for-us/` | 1: wp-205 |
| `/nominujte-vpsfree-cz-do-kristalove-lupy/` | `wp-107` → `/nominate-vpsfree-cz-for-kristalova-lupa/` | 2: wp-114, wp-205 |
| `/prechazime-z-openvz-na-vpsadminos-spoustime-testovaci-prostredi/` | `wp-547` → `/were-moving-from-openvz-to-vpsadminos-and-launching-a-test-environment/` | 1: wp-730 |
| `/setrvacnost-konferencniho-efektu/` | `wp-82` → `/the-lasting-effect-of-conferences/` | 1: wp-123 |
| `/stale-rosteme-cisla-za-tri-roky/` | `wp-133` → `/we-keep-growing-three-years-in-numbers/` | 1: wp-210 |
| `https://blog.vpsfree.cz/1000-clenu-znamena-ze-jsme-nic-nepokazili/` | `wp-387` → `/1000-members-means-we-have-not-messed-anything-up/` | 1: wp-815 |
| `https://blog.vpsfree.cz/1000-clenu/` | `wp-381` → `/1000-members/` | 1: wp-387 |
| `https://blog.vpsfree.cz/20-gigabitu-bude-uz-letos/` | `wp-433` → `/20-gigabits-is-coming-this-year/` | 2: wp-443, wp-455 |
| `https://blog.vpsfree.cz/byli-jsme-na-linuxdays-2015-foto-a-video/` | `wp-123` → `/we-were-at-linuxdays-2015-photos-and-video/` | 1: wp-151 |
| `https://blog.vpsfree.cz/centos-7-template-jsme-prohlasili-za-stable/` | `wp-8` → `/we-have-marked-the-centos-7-template-as-stable/` | 1: wp-15 |
| `https://blog.vpsfree.cz/distribuce-po-roce-vedou-debian-ubuntu-a-centos/` | `wp-367` → `/distributions-a-year-on-debian-ubuntu-and-centos-lead/` | 1: wp-516 |
| `https://blog.vpsfree.cz/distribuce-provozovane-na-vpsfree-cz/` | `wp-61` → `/distributions-running-at-vpsfree-cz/` | 3: wp-333, wp-367, wp-516 |
| `https://blog.vpsfree.cz/inovujeme-skoro-vsechen-hardware-chceme-byt-energeticky-uspornejsi/` | `wp-773` → `/were-upgrading-almost-all-our-hardware-to-save-energy/` | 1: wp-815 |
| `https://blog.vpsfree.cz/jak-vyuzit-256-gb-ram-na-serveru/` | `wp-244` → `/how-to-use-256-gb-of-ram-in-a-server/` | 1: wp-406 |
| `https://blog.vpsfree.cz/jsme-v-pulce-migrace-na-vpsadminos-ted-prijde-na-radu-brno/` | `wp-713` → `/were-halfway-through-the-vpsadminos-migration-brno-is-next/` | 1: wp-730 |
| `https://blog.vpsfree.cz/kdyz-se-rozbiji-disky-aneb-jak-nas-pozlobil-nas/` | `wp-403` → `/when-disks-fail-our-nas-gave-us-trouble/` | 1: wp-408 |
| `https://blog.vpsfree.cz/linuxove-distribuce-rocky-linux-rychle-roste-slackware-uplne-zmizel/` | `wp-792` → `/linux-distributions-rocky-linux-grows-quickly-slackware-disappears/` | 1: wp-847 |
| `https://blog.vpsfree.cz/linuxove-distribuce-ubuntu-roste-rychleji-nez-debian-stoupa-popularita-nixos/` | `wp-702` → `/linux-distributions-ubuntu-grows-faster-than-debian-nixos-gains-popularity/` | 1: wp-792 |
| `https://blog.vpsfree.cz/linuxove-distribuce-vede-debian-a-ubuntu-nahoru-se-dere-alpine/` | `wp-516` → `/linux-distributions-debian-and-ubuntu-lead-alpine-is-climbing/` | 1: wp-702 |
| `https://blog.vpsfree.cz/mame-prvni-server-s-ssd-a-512-gb-ram/` | `wp-406` → `/our-first-server-with-ssds-and-512-gb-of-ram/` | 1: wp-408 |
| `https://blog.vpsfree.cz/migrace-nasi-infrastruktury-na-20-gigabitu/` | `wp-625` → `/migrating-our-infrastructure-to-20-gigabits/` | 1: wp-667 |
| `https://blog.vpsfree.cz/migrujte-na-vpsadminos-uz-je-cas-na-aktualni-virtualizaci-s-novym-jadrem/` | `wp-730` → `/migrate-to-vpsadminos-time-for-current-virtualization-and-a-new-kernel/` | 2: wp-762, wp-773 |
| `https://blog.vpsfree.cz/novinky-ve-vpsadminu-hostitelske-klice-ssh-upravy-v-sablonach-a-cgroups/` | `wp-805` → `/vpsadmin-news-ssh-host-keys-template-changes-and-cgroups/` | 1: wp-807 |
| `https://blog.vpsfree.cz/novinky-ve-vpsadminu-vychozi-vlastnosti-vps-a-oom-reporty/` | `wp-692` → `/vpsadmin-updates-default-vps-features-and-oom-reports/` | 1: wp-730 |
| `https://blog.vpsfree.cz/podporujeme-alpine-linux-ma-u-nas-hlavni-mirror/` | `wp-506` → `/we-support-alpine-linux-and-host-its-main-mirror/` | 1: wp-516 |
| `https://blog.vpsfree.cz/post-mortem-par-slov-k-vypadku/` | `wp-746` → `/post-mortem-a-few-words-about-the-outage/` | 1: wp-759 |
| `https://blog.vpsfree.cz/predstavili-jsme-vpsadminos-system-pro-provoz-kontejneru/` | `wp-539` → `/we-introduced-vpsadminos-a-system-for-running-containers/` | 2: wp-547, wp-713 |
| `https://blog.vpsfree.cz/prejdeme-na-ipv6-spolecne-potrebujeme-to/` | `wp-662` → `/lets-move-to-ipv6-together-we-need-it/` | 1: wp-667 |
| `https://blog.vpsfree.cz/proc-chceme-mit-20gigabitovou-sit/` | `wp-408` → `/why-we-want-a-20-gigabit-network/` | 2: wp-433, wp-625 |
| `https://blog.vpsfree.cz/prvni-den-s-video-horovy-na-meet-vpsfree-cz/` | `wp-646` → `/the-first-day-of-video-calls-at-meet-vpsfree-cz/` | 1: wp-653 |
| `https://blog.vpsfree.cz/prvni-server-s-vpsadminos-v-brne/` | `wp-722` → `/the-first-vpsadminos-server-in-brno/` | 1: wp-730 |
| `https://blog.vpsfree.cz/prvni-vpsfree-hackaton-pojdte-s-nami-sitovat/` | `wp-465` → `/the-first-vpsfree-hackathon-come-and-work-on-networking/` | 1: wp-481 |
| `https://blog.vpsfree.cz/setrvacnost-konferencniho-efektu/` | `wp-82` → `/the-lasting-effect-of-conferences/` | 2: wp-275, wp-493 |
| `https://blog.vpsfree.cz/spoustime-video-hovory-na-meet-vpsfree-cz-zdarma-a-bez-registrace/` | `wp-639` → `/were-launching-video-calls-at-meet-vpsfree-cz-free-and-without-registration/` | 2: wp-646, wp-651 |
| `https://blog.vpsfree.cz/sprava-pameti-na-vpsadminos/` | `wp-678` → `/memory-management-on-vpsadminos/` | 1: wp-730 |
| `https://blog.vpsfree.cz/stale-rosteme-cisla-za-tri-roky/` | `wp-133` → `/we-keep-growing-three-years-in-numbers/` | 2: wp-275, wp-69 |
| `https://blog.vpsfree.cz/terraform-provider-pro-vpsadmin-spravujte-infrastrukturu-automatizovane/` | `wp-597` → `/terraform-provider-for-vpsadmin-automate-infrastructure-management/` | 1: wp-667 |
| `https://blog.vpsfree.cz/umime-pridelit-kazdemu-serveru-vlastni-blok-64-adres-z-ipv6/` | `wp-717` → `/we-can-allocate-a-dedicated-64-ipv6-block-to-each-server/` | 2: wp-722, wp-730 |
| `https://blog.vpsfree.cz/vpsadmin-2-1-0-konzole-vps-v-terminalu/` | `wp-253` → `/vpsadmin-2-1-0-the-vps-console-in-your-terminal/` | 1: wp-692 |
| `https://blog.vpsfree.cz/vpsadminos-v-produkci-v-praze/` | `wp-621` → `/vpsadminos-in-production-in-prague/` | 1: wp-713 |
| `https://blog.vpsfree.cz/vykonnejsi-servery-jako-lek-na-zvysovani-cen-energii/` | `wp-762` → `/more-powerful-servers-to-counter-rising-energy-prices/` | 1: wp-773 |

### Exact KB target set and unresolved authority

All 70 KB occurrences use `https://kb.vpsfree.cz`; 39 exact hrefs cover **27 distinct slash page paths**, including `/`. Thirteen exact hrefs carry fragments (23 occurrences). No query or entity form occurs in these KB targets. The following candidate IDs are a reversible slash-to-colon parsing aid, **not** evidence of real English page identity or existence; the root is deliberately unresolved. Architect0/KB authority owns the actual `<page>` linkage and any translated-fragment proof. No network/KB lookup was made by L11-I.

| Exact original href | Candidate source page ID / fragment | Count / source IDs |
| --- | --- | --- |
| `https://kb.vpsfree.cz/` | `(root unresolved)` / `(none)` | 1: wp-112 |
| `https://kb.vpsfree.cz/informace/chat` | `informace:chat` / `(none)` | 1: wp-390 |
| `https://kb.vpsfree.cz/informace/chat#bot` | `informace:chat` / `bot` | 1: wp-390 |
| `https://kb.vpsfree.cz/informace/chat#bouncer` | `informace:chat` / `bouncer` | 1: wp-390 |
| `https://kb.vpsfree.cz/informace/chat#irc` | `informace:chat` / `irc` | 3: wp-465, wp-636, wp-759 |
| `https://kb.vpsfree.cz/informace/infrastruktura` | `informace:infrastruktura` / `(none)` | 1: wp-667 |
| `https://kb.vpsfree.cz/informace/ip_adresy` | `informace:ip_adresy` / `(none)` | 2: wp-210, wp-387 |
| `https://kb.vpsfree.cz/informace/kam_psat` | `informace:kam_psat` / `(none)` | 3: wp-573, wp-576, wp-636 |
| `https://kb.vpsfree.cz/informace/komunikace` | `informace:komunikace` / `(none)` | 1: wp-636 |
| `https://kb.vpsfree.cz/informace/openvz` | `informace:openvz` / `(none)` | 2: wp-215, wp-709 |
| `https://kb.vpsfree.cz/informace/podpora` | `informace:podpora` / `(none)` | 6: wp-564, wp-573, wp-713, wp-722, wp-730, wp-773 |
| `https://kb.vpsfree.cz/navody/server/gre` | `navody:server:gre` / `(none)` | 1: wp-174 |
| `https://kb.vpsfree.cz/navody/vps/api` | `navody:vps:api` / `(none)` | 3: wp-308, wp-378, wp-500 |
| `https://kb.vpsfree.cz/navody/vps/api#cli` | `navody:vps:api` / `cli` | 9: wp-253, wp-264, wp-284, wp-455, wp-474, wp-490, wp-601, wp-709 |
| `https://kb.vpsfree.cz/navody/vps/api#prace_s_api` | `navody:vps:api` / `prace_s_api` | 1: wp-601 |
| `https://kb.vpsfree.cz/navody/vps/cgroups` | `navody:vps:cgroups` / `(none)` | 1: wp-805 |
| `https://kb.vpsfree.cz/navody/vps/datasety` | `navody:vps:datasety` / `(none)` | 1: wp-326 |
| `https://kb.vpsfree.cz/navody/vps/datasety#stahovani_zaloh` | `navody:vps:datasety` / `stahovani_zaloh` | 1: wp-284 |
| `https://kb.vpsfree.cz/navody/vps/exporty` | `navody:vps:exporty` / `(none)` | 2: wp-730, wp-773 |
| `https://kb.vpsfree.cz/navody/vps/konzole` | `navody:vps:konzole` / `(none)` | 2: wp-253, wp-738 |
| `https://kb.vpsfree.cz/navody/vps/konzole#zajisteni_spravne_funkce` | `navody:vps:konzole` / `zajisteni_spravne_funkce` | 1: wp-253 |
| `https://kb.vpsfree.cz/navody/vps/kvm` | `navody:vps:kvm` / `(none)` | 2: wp-174, wp-215 |
| `https://kb.vpsfree.cz/navody/vps/oprava` | `navody:vps:oprava` / `(none)` | 2: wp-112, wp-326 |
| `https://kb.vpsfree.cz/navody/vps/playgroundvps` | `navody:vps:playgroundvps` / `(none)` | 2: wp-291, wp-326 |
| `https://kb.vpsfree.cz/navody/vps/prenosy#monitor_v_cli` | `navody:vps:prenosy` / `monitor_v_cli` | 1: wp-455 |
| `https://kb.vpsfree.cz/navody/vps/rdns` | `navody:vps:rdns` / `(none)` | 1: wp-521 |
| `https://kb.vpsfree.cz/navody/vps/sprava` | `navody:vps:sprava` / `(none)` | 1: wp-455 |
| `https://kb.vpsfree.cz/navody/vps/sprava#klonovani_vps` | `navody:vps:sprava` / `klonovani_vps` | 1: wp-576 |
| `https://kb.vpsfree.cz/navody/vps/start_menu` | `navody:vps:start_menu` / `(none)` | 1: wp-738 |
| `https://kb.vpsfree.cz/navody/vps/uzivatele` | `navody:vps:uzivatele` / `(none)` | 1: wp-490 |
| `https://kb.vpsfree.cz/navody/vps/uzivatele#detailni_nastaveni` | `navody:vps:uzivatele` / `detailni_nastaveni` | 1: wp-500 |
| `https://kb.vpsfree.cz/navody/vps/uzivatele#dvoufaktorove_prihlasovani_2fa` | `navody:vps:uzivatele` / `dvoufaktorove_prihlasovani_2fa` | 1: wp-601 |
| `https://kb.vpsfree.cz/navody/vps/vpsadminos` | `navody:vps:vpsadminos` / `(none)` | 5: wp-547, wp-576, wp-621, wp-709, wp-762 |
| `https://kb.vpsfree.cz/navody/vps/vpsadminos#user_namespaces` | `navody:vps:vpsadminos` / `user_namespaces` | 1: wp-547 |
| `https://kb.vpsfree.cz/navody/vps/vpsadminos/docker` | `navody:vps:vpsadminos:docker` / `(none)` | 1: wp-692 |
| `https://kb.vpsfree.cz/navody/vps/vpsadminos/oprava` | `navody:vps:vpsadminos:oprava` / `(none)` | 1: wp-709 |
| `https://kb.vpsfree.cz/navody/vps/vpsadminos/oprava#nouzovy_rezim` | `navody:vps:vpsadminos:oprava` / `nouzovy_rezim` | 1: wp-738 |
| `https://kb.vpsfree.cz/navody/vps/vpsadminos/storage` | `navody:vps:vpsadminos:storage` / `(none)` | 2: wp-615, wp-713 |
| `https://kb.vpsfree.cz/navody/vps/zalohovani` | `navody:vps:zalohovani` / `(none)` | 1: wp-24 |

### Unchanged and protected boundaries

- **Blog media:** 75 occurrences/71 exact upload targets, listed separately as `blog_kind=media` in the machine inventory. They are not article destinations and have no inferred English counterpart. All remain unchanged.

- **Taxonomy:** `https://blog.vpsfree.cz/tag/vpsadminos/` in wp-667 and `/tag/vpsadminos/` in wp-730. No article-ID match or translation is claimed. D11 must explicitly decide any archive mapping.

- **Self-fragments:** `#heatmapy-2` in wp-828 and `#shrnut-4` in wp-835. These are page-local references, not links to another article. Both remain unchanged.

- **External:** 326 occurrences/274 exact targets across 100 articles. The complete distinct set and occurrence list are in machine class `external`, including vpsAdmin/project/docs/forum/conference links and the inherited malformed wp-490 URL. No translation, normalization or modernized target is inferred.

- **Mail:** only `mailto:podpora@vpsfree.cz`, in wp-653, remains unchanged.

- **Protected regions:** 46 raw pre blocks, 83 raw code spans and 125 HTML comments were excluded from actionable-link extraction. There are zero literal `href` attributes inside those regions; this does not claim there are no URL text examples in code. No code/comment bytes, CRLF or strings were changed.

- **Raw forms:** 122 blog occurrences are absolute `.cz` URLs; 12 are relative (nine article occurrences/eight exact routes, one taxonomy reference and two self-fragments). Eight relative article routes plus 108 exact absolute blog targets and two self-fragments plus the relative taxonomy target account for all 119 exact blog targets. Seven external occurrences/six exact targets use `&amp;`; these raw forms remain unchanged. All blog/KB raw query strings are empty; all KB fragments and the two self-fragments are recorded exactly.

### Extraction, identity and evidence limits

Python standard-library `HTMLParser(convert_charrefs=False)` tokenized only article bodies. A pre/code stack excludes protected content and comments are handled separately. Raw `get_starttag_text()` supplies the original attribute spelling; URL decoding is used only in classification fields. Every selected EN href was compared by anchor ordinal to the corresponding CS href: **531/531 exact raw targets agree**, with equal per-article link counts and zero ambiguities requiring prose inspection.

All 125 source IDs and current CS/EN routes/draft flags are retained in machine `article_metadata`. SHA-256 identities of all 250 complete article files were captured and reconfirmed unchanged at the end of extraction. The canonical sorted JSON source-path/hash map plus one LF has SHA-256 `c563700aac4e6cd77183db7efefe16e0886cd4e99f8fac44f6a36b4c39bbcfa3`. This checks extraction stability, not build/runtime correctness or human translation review.

- Complete machine inventory SHA-256: `55ebd24837828ebbc070a6e74a169fb7d35defdc456c05e9132a6e53da2d4a9e`.

- KB subset SHA-256: `aef8cfc652beac16822174103bf3fd0510e2051d1a792c10dbd5b5839a0e824e`.

No source/prose/URL/frontmatter/hash/metadata, index, Git ref, KB, network, build, service or production/default action occurred. Only this inventory section and the two linked machine records were written. Existing C/E/T3/S10 ownership and protected-source invariants are unchanged. Architect0 and implementer3 received the deduplicated KB page/fragment contexts before completion. Remaining dependency: authoritative KB counterpart/fragment mappings and architect-owned output policy; no renderer package is allocated to L11-I.


## L11-R committed renderer and verification

Owner: `implementer2`; source accepted by lead. This completes the D11 renderer
package. Earlier inventory is retained as the source snapshot; accepted KB
identity/section authority and exact fallback dispositions are in
[kb-link-review.md](kb-link-review.md).

- Parent: `95a3cae2a1185c096968357e558ee15ad5a2a7f8` (S10; U10 retained).
- Head: `b29f21bfa084d3b99e83d07ca8feb0b57afcfa6d`.
- Tree: `15e46f8e619f60c82c07a612ec8360a4a1f286a6`.
- Exactly five files, 360 additions/36 deletions: `bin/check`,
  `data/english-links.json`, `docs/authoring.md`,
  `layouts/partials/article-html.html`, `layouts/partials/english-link.html`.
- Staged/committed five-file inventory SHA-256:
  `cbe04807e509223db02768ebc2872bb171c16e73bf739f9712044499d9acce39`
  (canonical sorted JSON path/raw-SHA array plus LF). Each committed blob matched
  staged/working bytes. Index confirmed empty and yielded immediately.
- Map copied verbatim from the lead-accepted 23-page/nine-fragment/root-alias
  candidate, SHA-256
  `5b3fee0f5b6ffcf4b80ecedd6fce3967ddc23482e05ec3cf901f14b55a6f1b17`.
  Main accepted the concise authoring paragraph before commit.

Shared body/summary/RSS resolution uses immutable article IDs and actual rendered
English `.Permalink`, with canonical Czech fallback for missing/unrendered draft
counterparts or unknown target fragments. Verified KB page/section mappings are
offline and finite; unknowns and unsupported DokuWiki actions/revisions remain
unchanged. Queries/entities/raw quoting and non-href attributes survive; protected
pre/code/comments/script/style and href-like attribute text are excluded. Existing
media localization and S10/U10 behavior remain intact. All 250 complete article
files match the accepted inventory, including source URLs, hashes, metadata,
code/CRLF, prose and visible labels.

Final verification, on the exact bytes subsequently committed:

| Check | Result / evidence |
| --- | --- |
| `nix develop -c bin/check` | exit 0, about 60s; `/tmp/l11-r-final-check.log` |
| `nix develop -c bin/check-release` | exit 0, one test/about 1s; `/tmp/l11-r-final-check-release.log` |
| Real 125-article previews, dual-port and VPN | all 531 occurrences accounted for: 55 actual EN article links, 52 mapped KB/18 explicit fallbacks, 75 media with prior localization, 331 unchanged external/mail/taxonomy/self links |
| Before/after Czech outputs | all 1,055 CS files byte-identical in each of production, preview and VPN; VPN uses the complete CS/shared file list from dual-host output |
| Output file sets / HTML | stable 1,661 production, 2,110 preview, 1,533 VPN files; production HTML unchanged, preview/VPN each 62 changed HTML files with exactly equal non-href bytes |
| Whitespace / commit | working/staged/exact-range diff check zero diagnostics; normal `nix develop -c git commit -F` exit 0, no hook bypass; repo declares no framework and active hook configs/hooks absent |

The final related batch used a fresh pinned Luna/low watcher, catalog
`a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958`,
`danger-full-access`/`never`; no operation remains running. Fixtures cover three
modes, published/draft/missing targets and actual non-guessed routes, known/unknown
anchors, KB root/page/section, encoded paths and HTML/query preservation, legacy
action/revision exclusions, protected/attribute isolation, summaries and RSS.

An initial correct normal check passed (55s), but the watcher appended `.` to the
release command and unittest rejected it as a test selector. Parent inspected
that log/script; the exact command passed (one test/0.17s). This was invocation
error, not a source defect. Own later inspection added the quoted-attribute
regression, which justified the final complete batch above. No repeated check was
used instead of diagnosis; no further checks followed lead acceptance.

The 18 explicit KB fallbacks cover eight exact targets recorded by L11-K: missing
`openvz`, `storage`, `zalohovani` pages; missing `bouncer`, `cli`,
`stahovani_zaloh`, `user_namespaces` sections; and an infrastructure-language
classification subsequently found wrong in D12. The infrastructure is an English
hardware inventory; the corrected evidence and mapping are below. No guessed
map, dropped fragment or KB repair was introduced.

Lead owns final independent review and later publication. No dependency/pin
stream, migration or persisted schema change; rollback restores the former
renderer/source artifact. No rebase/push/default, KB write, network lookup,
service/production transition, new immutable artifact or human translation
approval is claimed. Earlier artifact receipts retain their exact revision
limits. Source and index are untouched after acceptance; findings ownership is
retained and capacity is free. Previews and session remain open.


## R12: semantic KB mapping follow-up

Lead/main read and accepted all 18 former fallback contexts and exact K12 map
`c869a107479cb980b2473eb54250686772dc363c87a2af6afdf0f7d99abd2cbe` before
application copy/commit. [K12/D12 evidence](kb-link-review.md#d12-semantic-reevaluation)
replaces old anchor-existence-only rejection with verified semantic destinations.
The former infrastructure language classification was wrong: identical sources
were the English hardware inventory, not copied Czech prose. It now maps to the
verified English inventory. This correction does not change article assertions.

- Parent: `ce0f031a1580e2db6e579ed8afeea3af27d5acf8` (U12).
- Head: `b5e3ebe54d9c42ab89142a1bcc50192e580fff10`.
- Tree: `4e5248b97e53b7d34b9bf1a1ccf10d3ace54854d`.
- Scope: `bin/check`, `data/english-links.json`, and only the KB branch of
  `layouts/partials/english-link.html`; 89 additions/14 deletions.
- Exact staged/committed three-file inventory SHA-256:
  `a522e8fbc98b9f61cf8334fd4ce660c1fa843e170ca016bf175da4f75871812c` (canonical sorted JSON path/raw-SHA array
  plus LF). Every committed blob matches staged/working bytes; index empty and
  yielded immediately. No extra source/index operation followed completion.

The accepted map is copied verbatim: 26 page entries, ten same-page fragment
pairs and two explicit full-URL `fragment_targets`. All original 23 targets,
nine fragment pairs, root alias and 52 previously mapped occurrences are intact.
Six newly resolved hrefs cover 15 occurrences, reaching **67/70 KB occurrences**:
all nine API `#cli` links use `manuals/vps/api#using_cli` (including wp-490 and
both wp-284 occurrences); backup downloads use
`manuals/vps/backups#downloading_backups`; user namespaces use
`manuals/vps/userns#user_namespace`; the old storage/backups links and
infrastructure link use the verified English guides/inventory. All source hrefs,
labels, prose, code/CRLF, metadata and all 250 article file hashes are unchanged.

**Three occurrences remain original**, after K12's bounded semantic searches:
wp-390's `informace/chat#bouncer` describes the offered ZNC service, for which no
equivalent documentation was evidenced; wp-215 and wp-709's `informace/openvz`
refer to historical OpenVZ and its former dataset-sharing behavior. Substituting
current LXC/storage/IRC archive documentation would change their meaning.

The helper gives an explicit full section target precedence over same-page
fragments, validates exact HTTPS `kb.vpsfree.org` authority without user/port/
query, inserts the preserved harmless source query before its destination
fragment, and escapes once. Unknown fragments and invalid full targets preserve
the original URL. D11 action/revision exclusions, existing blog routing and
Pagefind/S10 tests are unchanged. The existing authoring note already describes
verified mappings correctly; no redundant documentation/source-copy edit was made.

Final checks on the exact bytes subsequently committed:

- `nix develop -c bin/check`: exit 0, 55s, `/tmp/r12-final-check.log`.
- `nix develop -c bin/check-release`: exit 0, one test/2s,
  `/tmp/r12-final-check-release.log`.
- A fresh pinned Luna/low watcher owned this related batch under
  `danger-full-access`/`never`; no running operation remains. Focused fixtures
  first passed in all three modes, with synthetic precedence conflicts,
  cross-page query order/escaping, unknown fallback and invalid target shapes.
  Final checks additionally assert all nine actual CLI occurrences, both moved
  sections, all 70 KB dispositions, source/hash/draft invariants and retained
  search/release behavior. No KB lookup occurs in a build.
- Initial focused fixture invocation used unsupported Hugo `--dataDir`; it
  failed before rendering. Replaced that invocation with a native `dataDir`
  config overlay and the focused test passed. No product scope expansion or
  failure-blind retry followed.
- Working/staged/exact committed whitespace checks pass with zero diagnostics.
  Normal `nix develop -c git commit -F` exited 0; declared hook framework/configs
  and active hooks are absent as documented by the repository. No hook bypass.

This package reused the finite KB inventory and K12 evidence; it did not repeat
531-link/prose/KB network research. No migrations, dependency/pin streams or
persisted schema change. No artifact/browser/service/push/rebase/default/KB-write/
production operation or human translation approval. Lead owns acceptance/final
review/publication; findings ownership stays with implementer2. Previews, refs,
retained result and session remain open.
