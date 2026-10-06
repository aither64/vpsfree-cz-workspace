# Czech KB vpsAdmin label audit

## Baseline and scope

The live `kb.vpsfree.cz` page tree was enumerated recursively on 2026-07-10
using authenticated read-only DokuWiki RPC. All 116 accessible pages were read.
The shallow root listing is insufficient: it returns only 51 direct pages,
while `core.listPages` with depth 10 returns the complete 116-page tree.

The terminology authority is vpsAdmin `origin/master` at
`299147166ecb8459c712ed8a5c4dd14f673663fc`:

- WebUI Czech catalog:
  `webui/lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.po`;
- API English/Czech catalogs:
  `api/lib/vpsadmin/api/locales/{en,cs}.yml`;
- terminology rules: `doc/i18n-cs.md`;
- current WebUI source where old KB wording no longer has a direct catalog
  entry.

This includes the follow-up Czech wording fixes in that commit, notably the
clarified advanced dataset property labels such as `Komprese (compression)`,
`Čas přístupu (atime)`, `Relativní čas přístupu (relatime)`,
`Velikost záznamu (recordsize)`, and `Synchronní operace (sync)`.

The audit found 28 pages requiring text changes. A complete screenshot refresh
adds two screenshot-only pages, for a total of 30 draft pages. The remaining
86 pages have no direct vpsAdmin text or screenshot work in scope. Generic English
technical prose, command output, third-party interfaces, and vpsAdminOS console
text are not automatically translated merely because a word also occurs in a
vpsAdmin catalog.

## Replacement dictionary

### Membership, profile, and sessions

| Old KB text | Current Czech vpsAdmin text | Authority |
| --- | --- | --- |
| `Members` | `Členové` | WebUI PO, `forms/cluster.forms.php`, `public/index.php` |
| `Edit profile` | `Upravit profil` | WebUI PO, `lib/xtemplate.lib.php` |
| `Payment instructions` | `Pokyny k platbě` | WebUI PO, `forms/users.forms.php` |
| `Public keys` | `Veřejné klíče` | WebUI PO, `pages/page_adminm.php` |
| `Add public key` | `Přidat veřejný klíč` | WebUI PO, `forms/users.forms.php` |
| `Metrics access tokens` | `Přístupové tokeny k metrikám` | WebUI PO, `forms/users.forms.php` |
| `Cluster resources` | `Prostředky clusteru` | WebUI PO, `forms/cluster.forms.php` |
| `Environment configs` | `Konfigurace prostředí` | WebUI PO, `forms/users.forms.php` |
| `Environment` | `Prostředí` | WebUI PO / API `vpsadmin.attributes.environment.label` |
| `Account management` | `Vedení účtu` | WebUI PO, `pages/page_adminm.php` |
| `System administrator` | `Správce systému` | WebUI PO, `pages/page_adminm.php` |
| `Advanced e-mail configuration` | `Pokročilá konfigurace e-mailu` | WebUI PO, `forms/users.forms.php` |
| `TOTP devices` | `TOTP zařízení` | WebUI PO, `forms/users.forms.php` |
| `Passkeys` | `Přístupové klíče` | WebUI PO, `forms/users.forms.php` |
| `Session control` | `Nastavení relací` | WebUI PO, `pages/page_adminm.php` |
| `Enable single sign-on` | `Povolit jednotné přihlášení` | WebUI PO, `pages/page_adminm.php` |
| `Preferred session length` | `Doba nečinnosti před odhlášením` | WebUI PO, `pages/page_adminm.php` |
| `Logout all` | `Odhlašovat všude` | WebUI PO, `pages/page_adminm.php` |
| `Sessions` | `Relace` | WebUI PO, `pages/page_adminm.php` |

Session prose must also call session objects `relace`; `přihlášení` describes
the login event, not the persisted session object, and `sezení` is not used.

### Networking and DNS

| Old KB text | Current Czech vpsAdmin text | Authority |
| --- | --- | --- |
| `Networking` | `Sítě` | WebUI PO, `pages/page_networking.php`, `public/index.php` |
| `Routable addresses` | `Routované adresy` | WebUI PO, `pages/page_networking.php` |
| `Routed addresses` | `Routované adresy` | WebUI PO, `forms/vps.forms.php` |
| `Interface addresses` | `Adresy rozhraní` | WebUI PO, `forms/vps.forms.php` |
| `Manage host addresses` | `Spravovat adresy hostitelů` | WebUI PO, `forms/networking.forms.php` |
| `Add host addresses` | `Přidat adresy hostitelů` | WebUI PO, `forms/networking.forms.php` |
| `Primary zones` | `Primární zóny` | WebUI PO, `forms/dns.forms.php` |
| `Secondary zones` | `Sekundární zóny` | WebUI PO, `forms/dns.forms.php` |
| `Primary servers` | `Primární servery` | WebUI PO, `forms/dns.forms.php` |
| `Secondary servers` | `Sekundární servery` | WebUI PO, `forms/dns.forms.php` |
| `View DNSKEY and DS records` | `Zobrazit záznamy DNSKEY a DS` | WebUI PO, `forms/dns.forms.php` |
| `TSIG keys` | `TSIG klíče` | WebUI PO, `forms/dns.forms.php` |
| `List monthly traffic` | `Seznam měsíčního provozu` | WebUI PO, `pages/page_networking.php` |

`Live monitor` is intentionally unchanged in Czech.

### Datasets, exports, and backups

| Old KB text | Current Czech vpsAdmin text | Authority |
| --- | --- | --- |
| `Create dataset` | `Vytvořit dataset` | WebUI PO, `forms/dataset.forms.php` |
| old field `Parent` | current field `Rodičovský dataset` | API `vpsadmin.resources.dataset.actions.create.input.dataset.label` |
| `Auto mount` | `Automatický mount` | WebUI PO, `forms/dataset.forms.php` |
| `Quota` | `Kvóta včetně potomků (quota)` | API `vpsadmin.attributes.quota.label` |
| `Reference quota` | `Kvóta datasetu (refquota)` | API `vpsadmin.attributes.refquota.label` |
| `Used space` in the dataset list | `Použité místo` | API `vpsadmin.resources.dataset.attributes.used.label` |
| `Referenced space` | `Referencovaný prostor (referenced)` | API `vpsadmin.attributes.referenced.label` |
| `Available space` | `Dostupné místo` | API `vpsadmin.attributes.avail.label` |
| `Disable` / `Enable` mount controls | `Vypnout` / `Zapnuto` | WebUI PO, `forms/dataset.forms.php` |
| `Exports` | `Exporty` | WebUI PO, `public/index.php` |
| `Export dataset` | `Export datasetu` | WebUI PO, `forms/export.forms.php` |
| `Backups` | `Zálohy` | WebUI PO, `public/index.php` |
| `VPS backups` / `VPS Backups` | `Zálohy VPS` | WebUI PO, backup forms/pages |
| `NAS backups` / `NAS Backups` | `Zálohy NAS` | WebUI PO, backup forms/pages |
| `All VPS` | `Všechny VPS` | API `vpsadmin.attributes.all_vps.label` |

For the mount-toggle sentence, prefer natural prose (“mount lze vypnout a znovu
zapnout”) over quoting the catalog's awkward `Zapnuto` action text.

### VPS actions and general terminology

| Old KB text | Current Czech vpsAdmin text | Authority |
| --- | --- | --- |
| `Boot VPS from template (rescue mode)` | `Spustit VPS ze šablony (nouzový režim)` | WebUI PO, `pages/page_adminvps.php` |
| incomplete `Boot from VPS template` | full current title `Spustit VPS ze šablony (nouzový režim)` | current WebUI source |
| `Features` (VPS) | `Funkce` | WebUI PO, `pages/page_adminvps.php`; Czech guide |
| `New VPS` | `Nové VPS` | WebUI PO, `forms/vps.forms.php` |
| `Location` | `Lokace` | WebUI PO / API `vpsadmin.attributes.location.label` |
| `next` / `Next` | `Další` | WebUI PO, `forms/vps.forms.php` |
| `Clone VPS` | `Klonovat VPS` | WebUI PO, `forms/vps.forms.php` |
| `Swap VPS` | `Prohodit VPS` | WebUI PO, `forms/vps.forms.php` |
| obsolete `Create mount` path | current action `Mount` | current `forms/dataset.forms.php` |
| `Deploy to VPS` | `Nasadit do VPS` | WebUI PO, `forms/userdata.forms.php` |
| heading `Start Menu` | `Start menu` | WebUI PO, `forms/vps.forms.php` |
| `Transaction log` | `Transakce` | WebUI PO, menu and transaction pages |
| `Transaction chain` | `Řetězec transakcí` | WebUI PO, `pages/page_transactions.php` |
| `User namespace` | `Uživatelský jmenný prostor` | WebUI PO, user namespace forms/pages |
| `Type` | `Typ` | WebUI PO, `forms/userns.forms.php` |
| `ID within VPS` | `ID uvnitř VPS` | WebUI PO, `forms/userns.forms.php` |
| `ID within namespace` | `ID v rámci jmenného prostoru` | WebUI PO, `forms/userns.forms.php` |
| `ID count` | `ID počet` | WebUI PO, `forms/userns.forms.php` |
| `Resource is locked` / old `Resource is locked. Please try again.` | `Zdroj je uzamčen. Zkuste to prosím později.` | API `vpsadmin.errors.resource_locked` |

`User data`, `Mount`, `Hostname`, `Start menu`, `NAS`, `VPS`, `Playground`,
`Status`, and `Live monitor` are intentional Czech UI terms and stay as shown.
The start-menu console choices (`Start system`, `Run shell`, `Run custom
command`, `Select NixOS generation`) come from vpsAdminOS and remain English;
they are not stale WebUI labels.

## Page-by-page text plan

Line numbers refer to the page source fetched during this audit and must be
rechecked for revision drift before editing.

| Page | Source locations | Planned text changes |
| --- | --- | --- |
| `domu` | 85 | Link label `User namespaces` → `Uživatelské jmenné prostory`. |
| `informace:novacci` | 7 | `Members` → `Členové`. Keep `VPS`. |
| `informace:platby` | 4, 28 | Stale “Admin Členů” wording → menu `Členové`; `Edit profile` → `Upravit profil`; `Payment instructions` → `Pokyny k platbě`. |
| `informace:vymena_ip` | 22, 74–75 | `Interface addresses` → `Adresy rozhraní` (twice); `Routed addresses` → `Routované adresy`. |
| `navody:distribuce:nixos:impermanence` | 27, 110 | Rescue form title → `Spustit VPS ze šablony (nouzový režim)`; `Features` → `Funkce`. Keep `Mount`. |
| `navody:server:primarni_dns` | 6, 21, 25 | `Primary zones`, DNSKEY/DS action, and `Secondary servers` → catalog Czech text. |
| `navody:server:sekundarni_dns` | 7–8, 25 | `Secondary zones`, `Primary servers`, `TSIG keys` → catalog Czech text. |
| `navody:server:ssh` | 80 | `Edit profile → Public keys → Add public key` → `Upravit profil → Veřejné klíče → Přidat veřejný klíč`. |
| `navody:vps:api` | 488 | Replace abbreviated English lock error with the current full Czech API message. Leave literal CLI help/output examples in code blocks unchanged unless a fresh Czech-localized CLI capture is deliberately added later. |
| `navody:vps:datasety` | 23, 29–36, 44–53, 91 | Replace dataset action, parent field, automount, quota, used/referenced/available space, and reference-quota labels. Rephrase the mount toggle sentence without quoting `Disable/Enable`. |
| `navody:vps:exporty` | 9, 15, 18, 24 | `Exports`, `Export dataset`, backup menu entries, and `All VPS` → current Czech labels. Keep `NAS` and `Mount`. |
| `navody:vps:ip_adresy` | 41, 65–66 | `Networking → Routable addresses` and both host-address actions → current Czech labels. |
| `navody:vps:konzole` | — | No text replacement; create a draft so both embedded WebUI console screenshots can be refreshed. |
| `navody:vps:kvm-openrc` | — | No text replacement; create a draft so both embedded old vpsAdmin screenshots can be refreshed. |
| `navody:vps:metriky` | 10 | `Edit profile → Metrics access tokens` → Czech path. |
| `navody:vps:obnova_webu_zo_zalohy` | 11, 15 | `VPS > New VPS`, `Location`, `next`, `Backups > VPS Backups` → Czech labels; keep `Playground` and `Mount`. Do not otherwise rewrite the Slovak article in this initiative. |
| `navody:vps:oprava` | 36–37 | Replace obsolete `Detail … → Create mount` navigation with the current `Mount` action and current flow. |
| `navody:vps:playgroundvps` | 19, 29, 33, 42 | `New VPS`, `Clone VPS`, `transaction log`, and user-facing `Swap VPS` → `Nové VPS`, `Klonovat VPS`, `Transakce`, `Prohodit VPS`. |
| `navody:vps:plny_disk` | 26 | `Backups → NAS` → `Zálohy → NAS`. |
| `navody:vps:prenosy` | 6, 15 | Both `Networking` occurrences → `Sítě`; `List monthly traffic` → `Seznam měsíčního provozu`; keep `Live monitor`. |
| `navody:vps:prostredi` | 12–18 | Both `Edit profile` occurrences, `Cluster resources`, and `Environment configs` → Czech navigation path. |
| `navody:vps:rdns` | 19 | `Interface addresses` → `Adresy rozhraní`. |
| `navody:vps:sprava` | 35, 76–78, 96 | Profile/public-key path → Czech; heading and prose `Features` → `Funkce`; UI term `environment` → `prostředí`. |
| `navody:vps:start_menu` | 2 | Heading `Start Menu` → `Start menu`. Keep the actual vpsAdminOS console choices in English. |
| `navody:vps:userdata` | 16, 21 | `Edit profile` → `Upravit profil`; `Deploy to VPS` → `Nasadit do VPS`; keep `User data`. |
| `navody:vps:userns` | 2–5, 14, 17, 29–31, 44, 55, 67, 72, 77, 80 | Use `uživatelský jmenný prostor` in heading/prose and replace the four UI/table labels (`Typ`, `ID uvnitř VPS`, `ID v rámci jmenného prostoru`, `ID počet`). |
| `navody:vps:uzivatele` | 8, 12, 19, 29, 46, 68, 79–93, 97–101 | Replace every profile path, contact role, device/passkey/session form label, and `Sessions`. Reword session-object prose to use `relace`. |
| `navody:vps:vpsadmin` | 16–25, 36–42 | `transaction chain`/`chain` → `řetězec transakcí`/`řetězec`; navigation `transaction log` → `Transakce`; both old English lock messages → current full Czech API message. |
| `navody:vps:vpsadminos:oprava` | 37 | Incomplete old rescue form title → current `Spustit VPS ze šablony (nouzový režim)`. |
| `navody:vps:zalohy` | 13, 59 | Both `Backups` menu references → `Zálohy`. |

## Screenshot recapture plan

There are 63 affected references to 59 unique replacement images on 18 pages. Their media
revisions range from 2014-10-29 to 2025-03-16. Recapture every listed screen
from current software instead of editing pixels in old images. Where the
component is localized, use Czech; where current vpsAdminOS console or CLI text
remains English, recapture the current interface and treat the asset as
language-neutral content stored initially with the Czech set.

The legacy images `informace:details2.png` and
`navody:vps:root_passwd.png` both show the root-password form and therefore map
to the single canonical `vps-management/set-root-password.png` capture. The
previously proposed `vps-action-menu.png` did not match the surrounding text in
`informace:novacci` and has no remaining KB placement.

| Page | Media to recapture |
| --- | --- |
| `informace:novacci` | `informace:members.png`, `informace:vps1.png`, `informace:detailsvps.png`, `navody:vps:ssh-connection.png`, `informace:details2.png`, `navody:vps:deploy-public-key.png`, `navody:vps:vps-transfers.png` |
| `navody:server:ssh` | `navody:server:add_ssh_key.png`, `navody:server:deploy_ssh_key.png` |
| `navody:vps:datasety` | `navody:vps:dataset_vps.png`, `navody:vps:dataset_create.png`, `navody:vps:mounts.png`, `navody:vps:mounts_detail.png` (`vps_add.png` is only an icon and stays) |
| `navody:vps:exporty` | `navody:vps:vpsadminos:nasexport.png`, `backupexport.png`, `detailexportu1v2.png`, `detailexportu2v2.png` in the same namespace |
| `navody:vps:ip_adresy` | `navody:vps:ip_adresy.png`, `navody:vps:vpsadminos:routedadresses.png`, `navody:vps:vpsadminos:interfaceaddresses.png` |
| `navody:vps:konzole` | `navody:vps:console-1-web.png`, `navody:vps:console-2-web.png` |
| `navody:vps:kvm-openrc` | `navody:vps:features.jpg`, `navody:vps:datasets.jpg` |
| `navody:vps:obnova_webu_zo_zalohy` | `navody:vps:vpsfree_playground.jpg`, `navody:vps:vspfree_zalohy.jpg`, `navody:vps:vpsfree_mounting.jpg` |
| `navody:vps:playgroundvps` | `navody:vps:pgnd_create.png`, `navody:vps:clone_vps.png`, `navody:vps:swap_vps2.png`, `navody:vps:swap_preview2.png` |
| `navody:vps:prenosy` | `navody:vps:datove_prenosy.png`, `navody:vps:net_monitor_web.png`, `navody:vps:net_monitor_cli.png` |
| `navody:vps:prostredi` | `navody:vps:cluster_resources_detail.png`, `navody:vps:cluster_resources.png`, `navody:vps:env_config.png` |
| `navody:vps:rdns` | `navody:vps:reverzni_dns.png` |
| `navody:vps:sprava` | `navody:vps:create_vps.png`, `root_passwd.png`, `distro_reinstall.png`, `resources.png`, `hostname.png`, `vps_features.png`, `clone_vps.png`, `outage_windows.png`, plus the two shared `navody:server` SSH-key images |
| `navody:vps:start_menu` | `navody:vps:vps_details_start_menu.png`, `navody:vps:vps_console_start_menu.png`, `navody:vps:vps_console_start_menu_nixos.png`, `navody:vps:vps_console_start_menu_generations.png` |
| `navody:vps:userns` | `manuals:vps:vps_userns_map.png` |
| `navody:vps:uzivatele` | `navody:vps:user_mail_roles.png`, `user_mail_templates.png`, `2fa_status.png`, `totp_device_confirm.png`, `totp_device_list.png`, `user-session-control.png`, `user-session-log.png` |
| `navody:vps:vpsadminos:oprava` | `navody:vps:vpsadminos:vps-details-boot.png`, `vps-console-boot.png` |
| `navody:vps:zalohy` | `navody:vps:backups.png` |

Shared images (`add_ssh_key.png`, `deploy_ssh_key.png`, and `clone_vps.png`) must
be replaced once and verified on every embedding page.

## Pages with no direct change in this initiative

These 86 pages were read and had no vpsAdmin text or screenshot change under
the scope above:

- Draft/root: `drafts:2026-07-02-kb-staging:bot-ignore-test`, `grafika`,
  `nixos`, `novnc`, `systemd`, `vpsadminos`.
- `informace`: `admin_cheatsheet`, `admini`, `chat`, `chyby_a_napady`,
  `co_nedelat`, `db_spravcu`, `dokumenty`, `faq`, `infrastruktura`,
  `internal_address_plan`, `ip_adresy`, `jabber`, `jak_psat`, `kam_psat`,
  `komunikace`, `lide`, `mapofhw`, `mapofnetwork`, `ochranasoukromi`,
  `parametry_vps`, `podpora`, `projekty`, `projekty:ipv6tunel`, `sdruzeni`,
  `sklad`, `srazy`, `swap`, `vpsadminos`, `zacatek`.
- `navody:distribuce`: `alpine`, `distribuce`, `gentoo`, `guix`, `nixos`,
  `nixos:nginx`, `nixos:zaciname`.
- Other `navody`: `meet`; server pages `drupal`, `firewall`, `glusterfs`,
  `gre`, `mailgun`, `mailserver-nixos`, `nginx`, `openshift_centos`,
  `postfix`, `sysloger`, `wireguard`, `wireguard:openwrt`; user pages
  `moreplavec`, `stepan_schejbal`.
- Other `navody:vps`: `api:arch`, `api:centos`, `api:macos`, `api:ubuntu`,
  `api:windows`, `cgroups`, `incidenty`, `kvm`,
  `odstavky_a_vypadky`, `stagingvps`, `vpsadminos`,
  `vpsadminos:docker`, `vpsadminos:hacking`, `vpsadminos:libvirt`,
  `vpsadminos:snap`.
- Private/user/wiki: `private:acct`, `private:dluh`, `private:private`,
  `uzivatele:aither`, `uzivatele:jirutka`, `uzivatele:kerrycze`,
  `uzivatele:krcmar`, `uzivatele:pavlix`, `wiki:dokuwiki`,
  `wiki:playground`, `wiki:sirotci`, `wiki:syntax`, `wiki:todo`,
  `wiki:trash:navigace`.

This “no direct change” classification is specific to vpsAdmin localization.
It does not assert that the pages are otherwise current, fully Czech, or free
of unrelated documentation problems.
