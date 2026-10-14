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
and proxy-addr 2.0.8. Hosted CI passed at `1eb3f8d97f9091ec643ff63c2d0e4bb259e81a16`. Its browser
trace exposed a fixture resize crossing the filter breakpoint and moving the
focused row out of view. The fixture now restores that row to the viewport and
captures its open description there. Fresh hosted CI and bilingual browser
geometry/screenshots are pending at `ce856841a65d72648d03b6cba1748dd7dd9af048`.
No local CI was run for this refinement.
The fixtures do not establish real API or deployment behavior. The two related
legacy KB screenshots remain pending. No merge or deployment is included.

Česky: správce může povolit nebo zakázat síť bez přerušení stávajícího provozu.
Přehled sítí rozlišuje **Volné pro uživatele** a **Vlastněné, nepřiřazené**;
počty vycházejí z API, ne z teoretické kapacity. Vysvětlivky popisují překryv
vlastnictví a přiřazení. U staršího API se chybějící údaje zobrazí jako neznámé.
V přehledu IP adres na desktopu i mobilu se příznak **Síť zakázána** ukazuje
pouze u zakázaných sítí. Vlastněné adresy zůstávají viditelné, nové přiřazení
je omezené dostupností sítě. Ověření tohoto commitu a snímky rozhraní čekají na
GitHub Actions; lokální CI se nespouštělo.

[Session evidence and review](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/)
