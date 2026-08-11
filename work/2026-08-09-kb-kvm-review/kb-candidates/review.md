# KB navigation annotation review

Changed pages: 4
New pages: 0
Selected media: 2
Annotation tags: 0
Content replacements: 4
Managed pages: 2

| Language | Page | Semantic path | Count | Existing text | Candidate text |
| --- | --- | --- | ---: | --- | --- |

## Guarded content replacements

| Language | Page | Count | Existing text | Candidate text |
| --- | --- | ---: | --- | --- |
| cs | informace:jak_psat | 1 | ===== Dokumentace vpsAdminu ===== ↵ ==== Navigace ve vpsAdminu ==== ↵ Každý popis navigace, položky nabídky nebo formuláře ve vpsAdminu musí být ↵ uzavřen v párovém tagu ''%%<vpsadmin-nav>%%''. Atribut ''id'' obsahuje stabilní ↵ sémantický identifikátor daného ovládacího prvku. Viditelný text zůstává česky ↵ a musí odpovídat názvům v aktuálním webovém rozhraní. ↵  ↵ Například: ↵  ↵ <code> ↵ <vpsadmin-nav id="member.public-keys.add">Upravit profil → Veřejné klíče → Přidat veřejný klíč</vpsadmin-nav> ↵ </code> ↵  ↵ Identifikátory nevymýšlejte jen v textu KB. Musejí být součástí ↵ [[https://github.com/vpsfreecz/vpsadmin-kb-captures/blob/master/contract/navigation.yml\|navigačního kontraktu]]. ↵ Pokud potřebný identifikátor neexistuje nebo se webové rozhraní mění, postupujte ↵ podle [[https://github.com/vpsfreecz/vpsadmin-kb-captures/blob/master/docs/webui-change-workflow.md\|workflow pro změny webového rozhraní]]. ↵  ↵ ==== Screenshoty vpsAdminu ==== ↵ Screenshoty vpsAdminu nevytvářejte ani nenahrávejte ručně. Jsou reprodukovatelně ↵ generovány pomocí Playwright scénářů, vývojového clusteru a připravených dat v ↵ repozitáři [[https://github.com/vpsfreecz/vpsadmin-kb-captures\|vpsadmin-kb-captures]]. ↵ Repozitář spravuje českou i anglickou variantu každého screenshotu. Nový nebo ↵ změněný screenshot je potřeba upravit a znovu vygenerovat tam, zkontrolovat ve ↵ staging KB a teprve potom publikovat. ↵  | ===== Dokumentace vpsAdminu ===== ↵ ==== Navigace ve vpsAdminu ==== ↵ Každý popis navigace, položky nabídky nebo formuláře ve vpsAdminu musí být ↵ uzavřen v párovém tagu ''%%<vpsadmin-nav>%%''. Atribut ''id'' obsahuje stabilní ↵ sémantický identifikátor daného ovládacího prvku. Viditelný text zůstává česky ↵ a musí odpovídat názvům v aktuálním webovém rozhraní. ↵  ↵ Například: ↵  ↵ <code> ↵ <vpsadmin-nav id="member.public-keys.add">Upravit profil → Veřejné klíče → Přidat veřejný klíč</vpsadmin-nav> ↵ </code> ↵  ↵ Identifikátory nevymýšlejte jen v textu KB. Musejí být součástí ↵ [[https://github.com/vpsfreecz/vpsfree-kb-contracts/blob/master/contract/navigation.yml\|navigačního kontraktu]]. ↵ Pokud potřebný identifikátor neexistuje nebo se webové rozhraní mění, postupujte ↵ podle [[https://github.com/vpsfreecz/vpsfree-kb-contracts/blob/master/docs/webui-change-workflow.md\|workflow pro změny webového rozhraní]]. ↵  ↵ ==== Screenshoty vpsAdminu ==== ↵ Screenshoty vpsAdminu nevytvářejte ani nenahrávejte ručně. Jsou reprodukovatelně ↵ generovány pomocí Playwright scénářů, vývojového clusteru a připravených dat v ↵ repozitáři [[https://github.com/vpsfreecz/vpsfree-kb-contracts\|vpsfree-kb-contracts]]. ↵ Repozitář spravuje českou i anglickou variantu každého screenshotu. Nový nebo ↵ změněný screenshot je potřeba upravit a znovu vygenerovat tam, zkontrolovat ve ↵ staging KB a teprve potom publikovat. ↵  ↵ ==== Články spravované v repozitáři ==== ↵ Některé články jsou společně se svými automatickými testy spravovány v ↵ repozitáři ''vpsfree-kb-contracts''. Poznáte je podle odkazu **Zdroj na ↵ GitHubu** v panelu nástrojů stránky. Editor KB navíc zobrazí upozornění s ↵ odkazy na zdrojový text a automatický test. Takový článek neupravujte přímo v ↵ KB; změnu navrhněte v odkazovaném repozitáři. ↵  ↵ Pokud už byl spravovaný článek změněn přímo v KB, upozorněte správce. Příprava ↵ dalšího vydání změnu odmítne přepsat, dokud ji správce nepřevezme nebo nesloučí ↵ do zdrojového textu a znovu neověří. ↵  |
| en | information:kb | 1 | ===== Documenting vpsAdmin ===== ↵ ==== Navigation in vpsAdmin ==== ↵ Every description of navigation, a menu entry, or a form in vpsAdmin must be ↵ wrapped in a paired ''%%<vpsadmin-nav>%%'' tag. Its ''id'' attribute contains ↵ the stable semantic identifier of that control. The visible text remains in ↵ English and must match the current WebUI labels. ↵  ↵ For example: ↵  ↵ <code> ↵ <vpsadmin-nav id="member.public-keys.add">Edit profile → Public keys → Add public key</vpsadmin-nav> ↵ </code> ↵  ↵ Do not invent identifiers only in KB text. They must be part of the ↵ [[https://github.com/vpsfreecz/vpsadmin-kb-captures/blob/master/contract/navigation.yml\|navigation contract]]. ↵ If the required identifier does not exist, or the WebUI is changing, follow the ↵ [[https://github.com/vpsfreecz/vpsadmin-kb-captures/blob/master/docs/webui-change-workflow.md\|WebUI change documentation workflow]]. ↵  ↵ ==== vpsAdmin screenshots ==== ↵ Do not capture or upload vpsAdmin screenshots manually. They are generated ↵ reproducibly using Playwright scenarios, a development cluster, and prepared ↵ fixtures in ↵ [[https://github.com/vpsfreecz/vpsadmin-kb-captures\|vpsadmin-kb-captures]]. ↵ The repository maintains both Czech and English variants of every screenshot. ↵ Add or update a screenshot there, regenerate it, review it on the staging KB, ↵ and only then publish it. ↵  | ===== Documenting vpsAdmin ===== ↵ ==== Navigation in vpsAdmin ==== ↵ Every description of navigation, a menu entry, or a form in vpsAdmin must be ↵ wrapped in a paired ''%%<vpsadmin-nav>%%'' tag. Its ''id'' attribute contains ↵ the stable semantic identifier of that control. The visible text remains in ↵ English and must match the current WebUI labels. ↵  ↵ For example: ↵  ↵ <code> ↵ <vpsadmin-nav id="member.public-keys.add">Edit profile → Public keys → Add public key</vpsadmin-nav> ↵ </code> ↵  ↵ Do not invent identifiers only in KB text. They must be part of the ↵ [[https://github.com/vpsfreecz/vpsfree-kb-contracts/blob/master/contract/navigation.yml\|navigation contract]]. ↵ If the required identifier does not exist, or the WebUI is changing, follow the ↵ [[https://github.com/vpsfreecz/vpsfree-kb-contracts/blob/master/docs/webui-change-workflow.md\|WebUI change documentation workflow]]. ↵  ↵ ==== vpsAdmin screenshots ==== ↵ Do not capture or upload vpsAdmin screenshots manually. They are generated ↵ reproducibly using Playwright scenarios, a development cluster, and prepared ↵ fixtures in ↵ [[https://github.com/vpsfreecz/vpsfree-kb-contracts\|vpsfree-kb-contracts]]. ↵ The repository maintains both Czech and English variants of every screenshot. ↵ Add or update a screenshot there, regenerate it, review it on the staging KB, ↵ and only then publish it. ↵  ↵ ==== Repository-managed articles ==== ↵ Some articles and their automated tests are maintained in the ↵ ''vpsfree-kb-contracts'' repository. They have a **Source on GitHub** entry in ↵ the page toolbar. The KB editor also displays a warning with links to the ↵ source text and automated test. Do not edit such an article directly in the ↵ KB; propose the change in the linked repository. ↵  ↵ If a managed article has already been edited directly in the KB, notify its ↵ maintainers. The next release will refuse to overwrite the edit until it is ↵ adopted or merged into the source text and verified again. ↵  |
| cs | informace:jak_psat | 1 | V KB mají maintaineři pouze informační význam: ukazují, na koho se obrátit v ↵ případě dotazu či nápadu na vylepšení. Drobné změny, opravy a další informace ↵ můžete samozřejmě přidávat přímo. Pokud napíšete návod a máte čas se o něj ↵ starat, zapište se u něj jako maintainer. | V KB mají maintaineři pouze informační význam: ukazují, na koho se obrátit v ↵ případě dotazu či nápadu na vylepšení. Drobné změny, opravy a další informace ↵ můžete přidávat přímo na stránkách, které nejsou označeny jako spravované v ↵ repozitáři. Pokud napíšete návod a máte čas se o něj starat, zapište se u něj ↵ jako maintainer. |
| en | information:kb | 1 | Maintainers are informational: they show whom to contact with a question or an ↵ idea for improvement. Anyone can still make small changes, corrections, or add ↵ more information directly. If you write a guide and have time to maintain it, ↵ please add yourself as a maintainer. | Maintainers are informational: they show whom to contact with a question or an ↵ idea for improvement. Pages that are not marked as repository-managed can still ↵ be edited directly. If you write a guide and have time to maintain it, please ↵ add yourself as a maintainer. |

## Managed articles

| Article | Language | Page | Reconciliation | Canonical source |
| --- | --- | --- | --- | --- |
| `kvm` | cs | navody:vps:kvm | bootstrap | `contract/pages/navody-vps-kvm.txt` |
| `kvm` | en | manuals:vps:kvm | bootstrap | `contract/pages/manuals-vps-kvm.txt` |

## Explicit exceptions

| Language | Page | Semantic path | Reason |
| --- | --- | --- | --- |

## New pages

| Language | Page | SHA-256 |
| --- | --- | --- |

## Canonical code samples

| ID | File | Language | Uses | SHA-256 |
| --- | --- | --- | ---: | --- |

## Selected capture media

| Language | Capture | Media ID | SHA-256 |
| --- | --- | --- | --- |
| cs | `vps-details/datasets` | cs:screenshots:vpsadmin:vps-details:datasets.png | `5addfc72ce42d8a69bc8ce57ae10bb3da5f8089d1759152ecfe0dacf6352eeb1` |
| en | `vps-details/datasets` | en:screenshots:vpsadmin:vps-details:datasets.png | `5b319b10e335f91d9bd1fc21500dcea7af56a35d85be682397004c84f4563de2` |
