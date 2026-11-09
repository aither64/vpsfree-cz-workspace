# P36 Czech article typo audit — implementer3

Baseline BLOG `63e08c7a1c6a3b4136197e2ec27836619563668b`, tree `0475b8b90300be21b2c0862d5a74da15fdc990b8`.

Read all **42/42 assigned articles**: 13935 estimated title/body words (13628 body words). Read titles and every visible prose passage in the original baseline HTML, including headings, lists, tables, captions, image alt text and visible link labels/tooltips. Inspected code/quotes in place and left them unchanged. This is contextual reading, not a dictionary-only result.

**27 clear candidate instances**, plus **2 context-sensitive proposals** for the lead's decision. **19 articles have no new candidate**. The already-owned wp-841 `technolgii → technologii` fix is excluded from those counts; the rest of wp-841 was read in full.

No source/index edits, Git fetches, tests, builds, dictionary installs, network or runtime actions. No Hunspell run was needed. The lead owns the final wording/scope decision and any later implementation.

## Clear spelling or accidental-typo candidates

| ID | Exact baseline path:line | Before → after | Full sentence/paragraph context | Reason / confidence |
| --- | --- | --- | --- | --- |
| wp-15 | `content/posts/2014-11-10-how-we-build-operating-system-templates-for-vpses/index.cs.html:17` | `balíčku` → `balíčků` | Všechny skripty i šablony můžete najít na GitHubu. Do šablon pak můžeme poměrně jednoduše dostat specifické nastavení pro vpsFree.cz, například automatické zprovoznění vzdálené konzole, kterou máme k dispozici ve vpsadminu, či doinstalování běžně používaných balíčku jako je „vim“, atd... | Chybějící kroužek v množném čísle „používaných balíčků“. / high |
| wp-15 | `content/posts/2014-11-10-how-we-build-operating-system-templates-for-vpses/index.cs.html:18` | `uložišti` → `úložišti` | Všechny dostupné šablony máme uložené na centrálním NFS uložišti, čímž docíleme, že na všech serverech jsou jednotné a bez rozdílů. Vy pak máte možnost přes vpsAdmin šablonu jedním kliknutím nainstalovat na svůj VPS. | Chybějící počáteční čárka ve slově úložiště. / high |
| wp-15 | `content/posts/2014-11-10-how-we-build-operating-system-templates-for-vpses/index.cs.html:18` | `docíleme` → `docílíme` | Všechny dostupné šablony máme uložené na centrálním NFS uložišti, čímž docíleme, že na všech serverech jsou jednotné a bez rozdílů. Vy pak máte možnost přes vpsAdmin šablonu jedním kliknutím nainstalovat na svůj VPS. | Překlep ve tvaru slovesa docílit (docílíme). / high |
| wp-51 | `content/posts/2015-04-07-we-supported-ctu-students/index.cs.html:49` | `Gratulujume` → `Gratulujeme` | Gratulujume oceněným studentům a děkujeme Fakultě informačních technologií ČVUT, zastoupenou panem Žďárkem, za slibně se rozvíjející spolupráci. | Zjevná záměna samohlásky ve slovese gratulujeme. / high |
| wp-84 | `content/posts/2015-06-02-we-supported-volunteer-firefighters-by-hosting-the-dh-cz-portal/index.cs.html:21` | `PostgresSQL` → `PostgreSQL` | Pokud vás zajímá, co na VPS se serverem DH.cz běží, pak vězte, že je to JBoss AS, Apache, mail server Postfix, MySQL a PostgresSQL databáze. „Plánují se i další věci, ale nechci předbíhat,“ řekl nám Jirka. | Nadbytečné s v názvu databáze PostgreSQL. / high |
| wp-123 | `content/posts/2015-10-14-we-were-at-linuxdays-2015-photos-and-video/index.cs.html:21` | `„konferenční efekt“ a je` → `„konferenční efekt“ je` | Přímo na stánku se nikdo členem nestal, ale to asi nelze čekat. Ovšem „konferenční efekt“ a je neoddiskutovatelný, od minulého roku výrazně ubylo lidí, kteří kroutili hlavou a říkali, že nás vůbec neznají. Setrvačnost je pak velmi dlouhá a během několika měsíců teď budeme pozorovat, jak budou přibývat noví členové, kteří si na nás ve správnou chvíli vzpomenou. | Zjevně nadbytečné samostatné a mezi podmětem a přísudkem. / high |
| wp-191 | `content/posts/2015-11-11-we-brought-coffee-and-logo-stickers-to-openalt/index.cs.html:26` | `druhé ho` → `druhého` | Svou přednášku měl i Petr Krčmář, který ukazoval instalaci Debianu pomocí utility debootstrap. Využil dvou VPS na našem playgroundu – z běžící distribuce CentOS nainstaloval do druhé ho VPS základní Debian a pak ho nabootoval. | Náhodná mezera uvnitř slova. / high |
| wp-299 | `content/posts/2016-04-18-the-beginnings-of-vpsfree-cz-how-i-gave-a-server-to-a-stranger/index.cs.html:15` | `Bratoslavě` → `Bratislavě` | O víkendu 9. a 10. dubna proběhl v Bratoslavě OSS Víkend, kde Tomáš Srnka přednášel nejen o minulosti vpsFree.cz. | Záměna samohlásky v místním jméně; stejný článek níže správně Bratislavě. / high |
| wp-367 | `content/posts/2016-06-13-distributions-a-year-on-debian-ubuntu-and-centos-lead/index.cs.html:18` | `Současný stav vypadá takto?` → `Současný stav vypadá takto:` | Protože přibylo 220 nových běžících serverů, nastal čas se podívat, jestli se nějak změnily poměry mezi distribucemi a které systémy rostly nejrychleji. Současný stav vypadá takto? | Zjevně chybný závěrečný znak u oznamovací věty uvádějící tabulku. / high |
| wp-481 | `content/posts/2016-12-07-how-did-our-first-vpsfree-hackathon-go/index.cs.html:23` | `smutné koukali` → `smutně koukali` | Díky všem, co jste dorazili a pomohli; ale zrovna tak všem, co jste dorazili, abyste se něco dozvěděli - příště se klidně víc ptejte, někteří tam jenom seděli a smutné koukali, že tomu ne až tak rozumí - pokud se nebudete ptát zrovna toho, co uber-zuřivě tluče do klávesnice, někdo okolo něj vám problematiku příště rád vysvětlí. | Záměna diakritiky v příslovci smutně. / high |
| wp-490 | `content/posts/2017-02-13-vpsadmin-v2-7-0-payments-emails-and-two-playground-vpses/index.cs.html:35` | `implenentovány` → `implementovány` | Ostatní věci, jako platby nebo uživatelské požadavky, jsou tedy implenentovány jako pluginy. | Záměna m za n uvnitř slova implementovány. / high |
| wp-500 | `content/posts/2017-03-29-vpsadmin-2-8-0-improves-outage-reporting/index.cs.html:18` | `nebyli informování` → `nebyli informováni` | Na outage-list budeme výpadky hlásit stejně jako doposud. Abyste o každém výpadku, který se vás týká, nebyli informování 2x (přímo a přes outage-list), můžete se buď z outage-listu odhlásit, nebo si vypnout maily o výpadcích ve vpsAdminu. | Přebývající čárka nad koncovým i v příčestí „nebyli informováni“. / high |
| wp-506 | `content/posts/2017-05-03-we-support-alpine-linux-and-host-its-main-mirror/index.cs.html:22` | `ponz.:` → `pozn.:` | Tier 1 se plánují tři – pro Evropu, Ameriku a Asii (ponz.: můj návrh, že musíme mít zrcadlo i na Antarktidě se nějak neujal…). Z nich se budou synchronizovat zrcadla v Tier 2 a zároveň je budou používat koncoví uživatelé přes HTTP(S). | Přehozená písmena ve zkratce poznámky. / high |
| wp-564 | `content/posts/2018-10-15-our-new-servers-are-fully-patched-against-known-cpu-bugs/index.cs.html:23` | `vede výkonové` → `vede výkonově` | Ale abych pravdu řekl, úplně nejvíc se těším na to, až se AMD vytáhne s trochu aktualizovaným fabricem mezi těmi jejich čipy a DDR4 až zlevní… Zatím Intel pro naše použití vede výkonové i po nasazení všech záplat na bezpečnostní chyby v procesorech. | Záměna diakritiky v příslovci výkonově. / high |
| wp-580 | `content/posts/2019-01-28-our-first-10-years-are-behind-us-with-plenty-more-to-come/index.cs.html:23` | `Ted přišel` → `Teď přišel` | vpsFree jsem před 10 lety začínal, abych prakticky ukázal, co myslím tím, že se neziskové organizace dá dělat udržitelně. Ted přišel čas se podělit s dalšími plány, kudy (zdaleka nejen) vpsFree vidím dál; jak už může být cítit nějakou dobu, nezůstane jen u virtuálních serverů. | Chybějící háček v příslovci teď. / high |
| wp-601 | `content/posts/2019-05-22-two-factor-login-to-vpsadmin-for-better-security/index.cs.html:17` | `dvoufaktorovu` → `dvoufaktorovou` | Ve vpsAdminu si nyní můžete nastavit dvoufaktorovu autentizaci (2FA) pomocí TOTP. Pro autentizaci můžete používat např. mobil s aplikací Google Authenticator, FreeOTP, nebo libovolný program implementující TOTP. Pro nastavení stačí do aplikace naskenovat QR kód, popř. opsat tajný klíč. Aplikace je pak kdykoli schopna zobrazit aktuální heslo pro přihlášení, které se mění každých 30 sekund. | Chybějící o ve slově dvoufaktorovou. / high |
| wp-606 | `content/posts/2019-06-04-six-months-of-vpsadminos-development-closer-to-launching-a-production-server/index.cs.html:35` | `zjístite` → `zjistíte` | ... používají některé aplikace na detekci počtu procesorů, aby věděly kolik mají používat vláken, workerů, apod. Tyto údaje v Linuxu nejsou nijak virtualizované a řeší se to v userspace pomocí LXCFS. Co všechno máte ve VPS "virtualizováno" přes LXCFS zjístite s: | Délka samohlásek je omylem na jiné slabice; správně zjistíte. / high |
| wp-625 | `content/posts/2020-02-28-migrating-our-infrastructure-to-20-gigabits/index.cs.html:23` | `čekalo, ze migraci` → `čekalo, že migraci` | Poté jsme se pustili do samotných nodů. Každý jsme museli vypnout, vyměnit síťové karty, při té příležitosti rovnou aktualizovat linuxové jádro a znovu nastartovat. Tohle probíhalo na dvě fáze. Minulý rok se montovaly do serveru síťové karty a každou chvíli se čekalo, ze migraci spustíme. Nakonec jsme kvůli firmwarovým problémům migraci samotnou odložili až na leden, přestože už bylo všechno připojené a připravené od podzimu. | Chybějící háček ve spojce že. / high |
| wp-651 | `content/posts/2020-03-30-what-next-for-meet-vpsfree-cz-new-software-and-hardware/index.cs.html:25` | `s nějakou větší propagaci` → `s nějakou větší propagací` | Každopádně s nějakou větší propagaci budeme asi dál opatrní, hlavně aby to fungovalo členům a jejich rodinám, když si mezi sebou chceme volat. My to na škálování připravíme během tohohle týdne a pak uvidíme, kdo přispěje jakým hardwarem. | Chybějící čárka nad koncovým í (propagací). / high |
| wp-702 | `content/posts/2020-12-09-linux-distributions-ubuntu-grows-faster-than-debian-nixos-gains-popularity/index.cs.html:23` | `s jednou instalaci` → `s jednou instalací` | Na úplně stejných číslech pak zůstal Void Linux s jednou instalaci a Slackware se dvěma. Výsledky najdete v následující tabulce: | Chybějící čárka nad koncovým í (instalací). / high |
| wp-807 | `content/posts/2023-04-27-devcgprog-a-utility-for-configuring-the-cgroupv2-devices-controller/index.cs.html:19` | `umožnujeme` → `umožňujeme` | Ve výchozím stavu umožnujeme přístup k /dev/{console, full, kmsg, null, ptmx, random, urandom, tty*}. Podle VPS features pak i /dev/{net/tun, kvm, ppp}. Pro nás je nejdůležitější neumožnit přístup k diskovým zařízením, nad kterými běží ZFS. | Chybějící háček ve slovese umožňujeme. / high |
| wp-807 | `content/posts/2023-04-27-devcgprog-a-utility-for-configuring-the-cgroupv2-devices-controller/index.cs.html:55` | `nastavovaní` → `nastavování` | Celý náš stack je v Ruby, takže jsem na nastavovaní devices cgroup udělal oddělený program v Golangu -- vznikl devcgprog. Ten z Ruby voláme s cestou k cgroup a seznamem zařízení, které mají být povolené. devcgprog vytvoří BPF program, nahraje ho do kernelu, uloží do bpffs a připojí k cgroup. Kdyby se to někomu náhodou taky hodilo, devcgprog najdete na GitHubu. | Délka samohlásky je na jiné slabice; správně nastavování. / high |
| wp-815 | `content/posts/2023-12-19-we-have-discourse-come-and-talk-mailing-lists-have-had-their-day/index.cs.html:24` | `věřejnost` → `veřejnost` | news-list ještě chvíli podržíme v podobě, jak fungoval, ale po nějaké době (půl roku až rok) se přesune na kombinaci Discourse (kde se dá o těch věcech potom diskutovat) a blog (jako nástěnka pro věřejnost). | Přebytečný háček na prvním e ve slově veřejnost. / high |
| wp-821 | `content/posts/2023-12-30-single-sign-on-in-vpsadmin/index.cs.html:17` | `znalostní bázi i Discourse` → `znalostní bází i Discourse` | Změny se týkají především webového rozhraní vpsAdminu běžícího na vpsadmin.vpsfree.cz. Přihlašování nyní využívá OAuth2 a máme tak jeden autorizační server pro všechny webové služby. Mezi vpsAdminem, znalostní bázi i Discourse funguje single sign-on, tzn. přihlašovací údaje stačí zadat jen jednou. Přihlašovací formulář je sice na jiné adrese, i tak by ale prohlížeč měl být schopen doplnit údaje, pokud je máte uložené. | Chybějící čárka nad í v názvu služby po předložce mezi. / high |
| wp-821 | `content/posts/2023-12-30-single-sign-on-in-vpsadmin/index.cs.html:27` | `tlačitko` → `tlačítko` | Noví členové si musí při prvním přihlášení změnit heslo. Někdo to buď nestihl a došlo k automatickému odhlášení, nebo omylem klikl na tlačitko “Login” dvakrát, tím první přihlášení vyčerpal a skončil s uzamčeným účtem. Nový přihlašovací formulář řeší obě situace: změna hesla je vynucena během přihlašovacího procesu, tj. bez ní k přihlášení nedojde a účet tak nejde tímto způsobem zablokovat. Potvrzení přihlašovacího formuláře je taktéž vizuálně znázorněno a je zabráněno opakovanému odeslání formuláře. | Chybějící čárka ve slově tlačítko. / high |
| wp-821 | `content/posts/2023-12-30-single-sign-on-in-vpsadmin/index.cs.html:28` | `váše` → `vaše` | Dále je možné si zobrazit heslo a ověřit tak, že váše klávesnice píše to, co čekáte. Pokud zapomenete heslo nebo ztratíte autentizační zařízení pro TOTP, hned vidíte co máte dělat: použít tzn. recovery code a nebo napsat na podporu. | Přebytečná čárka nad a v zájmenu vaše. / high |
| wp-841 | `content/posts/2025-03-03-two-factor-login-with-passkeys/index.cs.html:17` | `apod.,)` → `apod.)` | Pro přihlášení do vpsAdminu lze nyní jako druhý faktor využít passkey. Lze použít jak hardwarové tokeny (YubiKey, GoTrust IdemKey, apod.,), tak softwarové klíčenky (KeePassXC, KeePassium, iCloud Keychain, Google Password Manager, Microsoft Windows Hello, 1Password, atp.). | Náhodná čárka před uzavírací závorkou ve výčtu. / high |

## Context-sensitive proposals — unchanged, lead decision required

| ID | Exact baseline path:line | Before → suggested after | Full context | Why separate |
| --- | --- | --- | --- | --- |
| wp-592 | `content/posts/2019-03-01-were-heading-to-installfest-come-for-coffee-and-a-new-switch/index.cs.html:17` | `rozhodně si nechte tuhle akci ujít` → `rozhodně si nenechte tuhle akci ujít` | Je jaro a to znamená, že je tu InstallFest! Opět se vydáváme do víru velkoměsta a na tradiční linuxácké konferenci otevřeme svůj stánek. Sedněte na vlak, autobus nebo na svého draka a rozhodně si nechte tuhle akci ujít. | Pravděpodobně vypadlé ne v pozvání na konferenci; výraz obrací smysl. Všechny okolní výzvy zvou k účasti. Vyžaduje výslovné posouzení zamýšleného významu. / medium; lead decision required |
| wp-821 | `content/posts/2023-12-30-single-sign-on-in-vpsadmin/index.cs.html:28` | `použít tzn. recovery code` → `použít tzv. recovery code` | Dále je možné si zobrazit heslo a ověřit tak, že váše klávesnice píše to, co čekáte. Pokud zapomenete heslo nebo ztratíte autentizační zařízení pro TOTP, hned vidíte co máte dělat: použít tzn. recovery code a nebo napsat na podporu. | Pravděpodobná záměna zkratky „takzvaný“ za „to znamená“; kontext to silně podporuje, ale jde o významovou volbu zkratky. / medium; lead decision required |

## Uncertain, protected or out-of-scope observations — unchanged

| ID | Baseline line | Text | Disposition |
| --- | --- | --- | --- |
| wp-24 | 30 | Jak dlouho trvá ZPS snapshotování u vpsfree? | Viditelný název odkazovaného historického vlákna; přestože ZPS připomíná překlep ZFS, název/citaci nepřepisuji. |
| wp-481 | — | hackaton, háčkovací, forwardovacího trafficu, rout, Gluxem, uber-zuřivě | Dobový odborný slang a autorský hlas; beze změny. |
| wp-580 | 19 | koderů | Odborný slang / dobový autorský hlas; možné kodérů nepřidávám jako jistou opravu. |
| wp-191 | [18, 21] | alt="Stanek", alt="Kava" | Původní ASCII názvy obrázků v alt; samotné doplnění diakritiky může být redakční změna, ne prokazatelný překlep. |
| wp-490 | 38 | href="http://https;//projects.vpsfree.cz/..." | Zjevně poškozený cíl odkazu, ale URL jsou explicitně mimo oprávnění auditu; beze změny, není kandidátem jazykové opravy. |
| wp-646 | 15 | měly jsme | Shoda přísudku s autorským kolektivem je gramatická/editorská otázka, ne jistý hláskový překlep v tomto úzkém auditu. |
| wp-592 | 19 | na kterých (ve větě o jednom switchi) | Gramatická shoda je mimo úzký soupis pravopisných/nahodilých překlepů; beze změny. |
| wp-821 | 25 | všechny sezení | Gramatická shoda je mimo úzký soupis; beze změny. |
| wp-807 | — | devices controller, cgroupy, bpffs, mknod, Golang, devcgprog | Odborné názvy a neformální terminologie; ponecháno včetně kódu a jeho parametrů. |
| wp-841 | — | Passkey, passkeys, KeePassium, GoTrust IdemKey | Vlastní názvy a záměrně užité varianty terminologie; ponecháno. |

## Complete actually-read coverage

Each row means the complete title and visible article text were read; zero candidates is an actual no-findings result, not an unread entry. Baseline file-byte hashes are in the companion JSON.

| ID | Exact Czech path | Body-word estimate | Result |
| --- | --- | ---: | --- |
| wp-15 | `content/posts/2014-11-10-how-we-build-operating-system-templates-for-vpses/index.cs.html` | 209 | 3 clear / 0 context-sensitive |
| wp-24 | `content/posts/2014-11-13-backups-at-vpsfree-from-rsync-to-zfs-snapshots/index.cs.html` | 355 | No new candidate |
| wp-51 | `content/posts/2015-04-07-we-supported-ctu-students/index.cs.html` | 1055 | 1 clear / 0 context-sensitive |
| wp-84 | `content/posts/2015-06-02-we-supported-volunteer-firefighters-by-hosting-the-dh-cz-portal/index.cs.html` | 277 | 1 clear / 0 context-sensitive |
| wp-107 | `content/posts/2015-08-12-nominate-vpsfree-cz-for-kristalova-lupa/index.cs.html` | 73 | No new candidate |
| wp-114 | `content/posts/2015-09-16-we-are-in-the-kristalova-lupa-awards-vote-for-us/index.cs.html` | 78 | No new candidate |
| wp-123 | `content/posts/2015-10-14-we-were-at-linuxdays-2015-photos-and-video/index.cs.html` | 380 | 1 clear / 0 context-sensitive |
| wp-191 | `content/posts/2015-11-11-we-brought-coffee-and-logo-stickers-to-openalt/index.cs.html` | 304 | 1 clear / 0 context-sensitive |
| wp-69 | `content/posts/2015-11-16-where-are-we-from-far-beyond-prague/index.cs.html` | 179 | No new candidate |
| wp-244 | `content/posts/2016-01-28-how-to-use-256-gb-of-ram-in-a-server/index.cs.html` | 249 | No new candidate |
| wp-264 | `content/posts/2016-02-10-vpsadmin-v2-2-0-setting-maintenance-windows-for-vpses/index.cs.html` | 225 | No new candidate |
| wp-291 | `content/posts/2016-03-23-the-latest-docker-1-10-now-runs-everywhere-here/index.cs.html` | 132 | No new candidate |
| wp-299 | `content/posts/2016-04-18-the-beginnings-of-vpsfree-cz-how-i-gave-a-server-to-a-stranger/index.cs.html` | 87 | 1 clear / 0 context-sensitive |
| wp-333 | `content/posts/2016-05-05-new-distributions-devuan-fedora-23-and-opensuse-13-2/index.cs.html` | 256 | No new candidate |
| wp-343 | `content/posts/2016-05-16-why-we-do-not-enable-swap-on-vpses/index.cs.html` | 206 | No new candidate |
| wp-367 | `content/posts/2016-06-13-distributions-a-year-on-debian-ubuntu-and-centos-lead/index.cs.html` | 212 | 1 clear / 0 context-sensitive |
| wp-397 | `content/posts/2016-08-16-share-code-snippets-at-paste-vpsfree-cz/index.cs.html` | 113 | No new candidate |
| wp-448 | `content/posts/2016-10-18-haveapi-has-a-new-web-interface/index.cs.html` | 152 | No new candidate |
| wp-450 | `content/posts/2016-10-24-the-dirty-cow-bug-under-openvz/index.cs.html` | 180 | No new candidate |
| wp-455 | `content/posts/2016-10-25-vpsadmin-v2-5-0-private-ip-addresses-and-an-improved-traffic-overview/index.cs.html` | 262 | No new candidate |
| wp-470 | `content/posts/2016-11-24-haveapi-v0-7-blocking-actions/index.cs.html` | 123 | No new candidate |
| wp-481 | `content/posts/2016-12-07-how-did-our-first-vpsfree-hackathon-go/index.cs.html` | 316 | 1 clear / 0 context-sensitive |
| wp-490 | `content/posts/2017-02-13-vpsadmin-v2-7-0-payments-emails-and-two-playground-vpses/index.cs.html` | 479 | 1 clear / 0 context-sensitive |
| wp-500 | `content/posts/2017-03-29-vpsadmin-2-8-0-improves-outage-reporting/index.cs.html` | 233 | 1 clear / 0 context-sensitive |
| wp-506 | `content/posts/2017-05-03-we-support-alpine-linux-and-host-its-main-mirror/index.cs.html` | 460 | 1 clear / 0 context-sensitive |
| wp-564 | `content/posts/2018-10-15-our-new-servers-are-fully-patched-against-known-cpu-bugs/index.cs.html` | 161 | 1 clear / 0 context-sensitive |
| wp-580 | `content/posts/2019-01-28-our-first-10-years-are-behind-us-with-plenty-more-to-come/index.cs.html` | 602 | 1 clear / 0 context-sensitive |
| wp-592 | `content/posts/2019-03-01-were-heading-to-installfest-come-for-coffee-and-a-new-switch/index.cs.html` | 141 | 0 clear / 1 context-sensitive |
| wp-601 | `content/posts/2019-05-22-two-factor-login-to-vpsadmin-for-better-security/index.cs.html` | 162 | 1 clear / 0 context-sensitive |
| wp-606 | `content/posts/2019-06-04-six-months-of-vpsadminos-development-closer-to-launching-a-production-server/index.cs.html` | 1300 | 1 clear / 0 context-sensitive |
| wp-625 | `content/posts/2020-02-28-migrating-our-infrastructure-to-20-gigabits/index.cs.html` | 448 | 1 clear / 0 context-sensitive |
| wp-646 | `content/posts/2020-03-18-the-first-day-of-video-calls-at-meet-vpsfree-cz/index.cs.html` | 323 | No new candidate |
| wp-651 | `content/posts/2020-03-30-what-next-for-meet-vpsfree-cz-new-software-and-hardware/index.cs.html` | 291 | 1 clear / 0 context-sensitive |
| wp-662 | `content/posts/2020-06-04-lets-move-to-ipv6-together-we-need-it/index.cs.html` | 373 | No new candidate |
| wp-702 | `content/posts/2020-12-09-linux-distributions-ubuntu-grows-faster-than-debian-nixos-gains-popularity/index.cs.html` | 316 | 1 clear / 0 context-sensitive |
| wp-730 | `content/posts/2021-12-13-migrate-to-vpsadminos-time-for-current-virtualization-and-a-new-kernel/index.cs.html` | 333 | No new candidate |
| wp-759 | `content/posts/2022-06-08-infrastructure-status-at-status-vpsf-cz/index.cs.html` | 169 | No new candidate |
| wp-792 | `content/posts/2023-01-05-linux-distributions-rocky-linux-grows-quickly-slackware-disappears/index.cs.html` | 351 | No new candidate |
| wp-807 | `content/posts/2023-04-27-devcgprog-a-utility-for-configuring-the-cgroupv2-devices-controller/index.cs.html` | 859 | 2 clear / 0 context-sensitive |
| wp-815 | `content/posts/2023-12-19-we-have-discourse-come-and-talk-mailing-lists-have-had-their-day/index.cs.html` | 413 | 1 clear / 0 context-sensitive |
| wp-821 | `content/posts/2023-12-30-single-sign-on-in-vpsadmin/index.cs.html` | 657 | 3 clear / 1 context-sensitive |
| wp-841 | `content/posts/2025-03-03-two-factor-login-with-passkeys/index.cs.html` | 134 | 1 clear / 0 context-sensitive; known technolgii fix already assigned to owner1/61c414c; rest read |

Preserved throughout: dates/lastmod, facts, identity, technical terms and code, URLs/anchors, author voice, historical quotations, comments and trusted English. Typographical normalization or grammar/style renewal is outside this report.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/
