Administrators can enable or disable networks while retaining existing service.
Network lists now show authoritative **Available to users** and **Owned, not
assigned** counts instead of deriving free inventory from capacity. Tooltips
explain assignment/ownership overlap and distinguish the editor's owned total.
Missing fields on older APIs remain unknown. Count descriptions and the disabled-IP
warning use a shared viewport-positioned body portal so table overflow cannot
clip their explanations.

Disabled networks appear as a warning only in the admin IP-list Flags, on desktop
and mobile. Owned disabled addresses remain visible; new assignment selectors
filter disabled pools when supported. Availability writes require current
capability metadata. This implements REQ-071 and extends REQ-050.

The branch is rebased onto current main, retaining its mobile/language changes
and proxy-addr 2.0.8. Hosted CI and Playwright smoke passed at `ce856841a65d72648d03b6cba1748dd7dd9af048`. The final bilingual geometry checks pass on desktop and mobile Chrome. All12 count/editor/IP-description screenshots were manually inspected as readable. Chromium429, mobile Chrome370 and mobile WebKit28 cases passed; the availability cases are selected in desktop/mobile Chrome. Independent affected component review is complete with no new findings; the original tooltip-clipping finding is resolved.
No local CI was run for this refinement.
The fixtures do not establish real API or deployment behavior. The two related
legacy KB screenshots remain pending. No merge or deployment is included.

Česky: správce může povolit nebo zakázat síť bez přerušení stávajícího provozu.
Přehled sítí rozlišuje **Volné pro uživatele** a **Vlastněné, nepřiřazené**;
počty vycházejí z API, ne z teoretické kapacity. Vysvětlivky popisují překryv
vlastnictví a přiřazení. U staršího API se chybějící údaje zobrazí jako neznámé.
V přehledu IP adres na desktopu i mobilu se příznak **Síť zakázána** ukazuje
pouze u zakázaných sítí. Vlastněné adresy zůstávají viditelné, nové přiřazení
je omezené dostupností sítě. GitHub Actions tohoto commitu prošly a vysvětlivky jsou na snímcích v obou jazycích čitelné na desktopu i mobilu. Nezávislá kontrola komponenty skončila bez nových nálezů; problém s ořezanými vysvětlivkami je vyřešený. Lokální CI se nespouštělo.

[Session evidence and review](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/)
