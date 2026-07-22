# KB navigation annotation review

Changed pages: 4
New pages: 2
Selected media: 10
Annotation tags: 16

| Language | Page | Semantic path | Count | Existing text | Candidate text |
| --- | --- | --- | ---: | --- | --- |
| cs | navody:vps:uzivatele | `notifications.open` | 1 | ===== Konfigurace e-mailových adres ===== ↵ vpsAdmin umožňuje nastavit jeden primární e-mail patřící majiteli účtu -- ↵ členovi v našem spolku. Ten musí být nastaven a může být jen jeden. Krom toho je ↵ možné nastavit různé e-mailové adresy pro různé typy kontaktů -- např. účetní a ↵ správce VPS. Toto nastavení lze měnit v detailech uživatelského účtu ↵ (<vpsadmin-nav id="member.edit-profile.open">vpsAdmin -> Upravit profil</vpsadmin-nav>). ↵  ↵ {{:cs:screenshots:vpsadmin:account:email-roles.png?300\|}} ↵  ↵ Například, správce členství (role Vedení účtu) dostává následující ↵ maily: ↵  ↵   * upozornění k platbě členského příspěvku, ↵   * pozastavení/obnovení členství, ↵   * potvrzení přijetí platby. ↵  ↵ Správce VPS (role Správce systému) pak maily o: ↵  ↵   * změně stavu VPS, ↵   * změně konfigurace VPS, ↵   * stahování záloh, ↵   * migrace VPS. ↵  ↵ ==== Detailní nastavení ==== ↵ Komu by nestačilo nastavení různých e-mailových adres pro různé role, nebo ↵ některé e-maily nechce vůbec dostávat, existuje ještě pokročilé nastavení ↵ (<vpsadmin-nav id="member.advanced-email-configuration.open">vpsAdmin -> Upravit profil -> Pokročilá konfigurace e-mailu</vpsadmin-nav>). Zde si můžete ↵ nastavit libovolné adresy pro vybrané typy e-mailů, případně zasílání zrušit ↵ úplně. ↵  ↵ {{:cs:screenshots:vpsadmin:account:mail-template-recipients.png?300\|}} | ===== E-mailová adresa a notifikace ===== ↵ Primární e-mailová adresa patří majiteli účtu — členovi spolku. Je povinná, ↵ může být pouze jedna a mění se v nastavení účtu (vpsAdmin → Upravit profil). ↵  ↵ Doručování provozních zpráv se nyní nastavuje pomocí událostí, rout, příjemců ↵ a cílů. Výchozí e-mailový cíl používá primární adresu; další adresy lze přidat ↵ a ověřit jako vlastní cíle. Postup včetně ztlumení vybraných událostí popisuje ↵ návod <vpsadmin-nav id="notifications.open">vpsAdmin → Notifikace</vpsadmin-nav>. |
| cs | navody:vps:uzivatele | `member.edit-profile.open` | 1 | vpsAdmin → Upravit profil | <vpsadmin-nav id="member.edit-profile.open">vpsAdmin → Upravit profil</vpsadmin-nav> |
| en | manuals:vps:users | `notifications.open` | 1 | ===== E-mail addresses ===== ↵ vpsAdmin allows users to set one primary e-mail address belonging to the ↵ account owner -- a member of our association. This address must be set and ↵ can only be a single address. In addition to the primary e-mail address, you ↵ can set different addresses for certain contact roles, such as an accountant ↵ or system administrator. These settings can be changed in user profile details ↵ (<vpsadmin-nav id="member.edit-profile.open">vpsAdmin -> Edit profile</vpsadmin-nav>) ↵  ↵ {{:en:screenshots:vpsadmin:account:email-roles.png?300\|}} ↵  ↵ For example, the account manager receives e-mails about: ↵  ↵   * payment notification, ↵   * suspension/activation of the membership, ↵   * accepted payments. ↵  ↵ The system administrator receives e-mails about: ↵  ↵   * VPS status changes, ↵   * VPS configuration changes, ↵   * backup downloads, ↵   * VPS migrations. ↵  ↵ ==== Advanced settings ==== ↵ Should contact roles not be enough or if don't wish to receive certain ↵ e-mails, there is an advanced settings form (<vpsadmin-nav id="member.advanced-email-configuration.open">vpsAdmin -> Edit profile -> ↵ Advanced e-mail configuration</vpsadmin-nav>). You can choose different e-mail addresses for ↵ specific mail templates or disable receiving of some mails altogether. ↵  ↵ {{:en:screenshots:vpsadmin:account:mail-template-recipients.png?300\|}} | ===== E-mail address and notifications ===== ↵ The primary e-mail address belongs to the account owner, a member of the ↵ association. It is required, only one can be set, and it is changed in the ↵ account settings (vpsAdmin → Edit profile). ↵  ↵ Delivery of operational messages is now configured using events, routes, ↵ receivers and targets. The default e-mail target follows the primary address; ↵ additional addresses can be added and verified as custom targets. The ↵ <vpsadmin-nav id="notifications.open">vpsAdmin → Notifications</vpsadmin-nav> ↵ guide explains the complete setup, including how to mute selected events. |
| en | manuals:vps:users | `member.edit-profile.open` | 1 | vpsAdmin → Edit profile | <vpsadmin-nav id="member.edit-profile.open">vpsAdmin → Edit profile</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.open` | 1 | hlavní nabídce Notifikace | <vpsadmin-nav id="notifications.open">hlavní nabídce Notifikace</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.routes.open` | 1 | v Notifikace → Routy. | v <vpsadmin-nav id="notifications.routes.open">Notifikace → Routy</vpsadmin-nav>. |
| cs | navody:notifikace | `notifications.receivers.open` | 1 | Notifikace → Příjemci | <vpsadmin-nav id="notifications.receivers.open">Notifikace → Příjemci</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.time-intervals.open` | 1 | Notifikace → Časové intervaly | <vpsadmin-nav id="notifications.time-intervals.open">Notifikace → Časové intervaly</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.route-time-intervals.open` | 1 | Notifikace → Routy → upravit routu | <vpsadmin-nav id="notifications.route-time-intervals.open">Notifikace → Routy → upravit routu</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.event-route-matches.open` | 1 | Notifikace → Události → detail události | <vpsadmin-nav id="notifications.event-route-matches.open">Notifikace → Události → detail události</vpsadmin-nav> |
| en | manuals:notifications | `notifications.open` | 1 | main Notifications menu | <vpsadmin-nav id="notifications.open">main Notifications menu</vpsadmin-nav> |
| en | manuals:notifications | `notifications.routes.open` | 1 | at Notifications → Routes. | at <vpsadmin-nav id="notifications.routes.open">Notifications → Routes</vpsadmin-nav>. |
| en | manuals:notifications | `notifications.receivers.open` | 1 | Notifications → Receivers | <vpsadmin-nav id="notifications.receivers.open">Notifications → Receivers</vpsadmin-nav> |
| en | manuals:notifications | `notifications.time-intervals.open` | 1 | Notifications → Time intervals | <vpsadmin-nav id="notifications.time-intervals.open">Notifications → Time intervals</vpsadmin-nav> |
| en | manuals:notifications | `notifications.route-time-intervals.open` | 1 | Notifications → Routes → edit route | <vpsadmin-nav id="notifications.route-time-intervals.open">Notifications → Routes → edit route</vpsadmin-nav> |
| en | manuals:notifications | `notifications.event-route-matches.open` | 1 | Notifications → Event log → event detail | <vpsadmin-nav id="notifications.event-route-matches.open">Notifications → Event log → event detail</vpsadmin-nav> |

## Explicit exceptions

| Language | Page | Semantic path | Reason |
| --- | --- | --- | --- |

## New pages

| Language | Page | SHA-256 |
| --- | --- | --- |
| cs | navody:notifikace | `12cd8975acc8dd165975aa7ce4b7c315f958408e2331a345c17c5c2f674fa14c` |
| en | manuals:notifications | `d59f39c78ec3481512ca9ba1ffb9fee9465d08cd9240ca4129ddb49c7ea26cc5` |

## Selected capture media

| Language | Capture | Media ID | SHA-256 |
| --- | --- | --- | --- |
| cs | `notifications/routes` | cs:screenshots:vpsadmin:notifications:routes.png | `94738ad34c61dc11edc068dbfe9bb416487655af8f69c6759a1d6c77dd9cd297` |
| cs | `notifications/receiver` | cs:screenshots:vpsadmin:notifications:receiver.png | `7161a9b1f6c08a3f6a1a327e2fd1bbfa32b2254c1b12534b38b4e9e27acf21ce` |
| cs | `notifications/time-interval` | cs:screenshots:vpsadmin:notifications:time-interval.png | `4ab5ef2b8b89eb82eceb7d975250087eb6ecc24cb36f2fc00e2c8891491d8e48` |
| cs | `notifications/route-time-intervals` | cs:screenshots:vpsadmin:notifications:route-time-intervals.png | `ac7e16c9756ae1e3915c3efc8bd1a9860f409599a92e415322ca9850ba1df83f` |
| cs | `notifications/event-suppressed` | cs:screenshots:vpsadmin:notifications:event-suppressed.png | `13cd491b775f353536d82a1fed33b31e28661565782a5fbee67b2406fa659fc0` |
| en | `notifications/routes` | en:screenshots:vpsadmin:notifications:routes.png | `bff3b5484a4d6fc19fd0bb97cff07196ef77d16c89777a270248dc45817f99ab` |
| en | `notifications/receiver` | en:screenshots:vpsadmin:notifications:receiver.png | `9909b554a00c7efab9c996f84c02e5f772b278e3df03adbea49a5859bb1772aa` |
| en | `notifications/time-interval` | en:screenshots:vpsadmin:notifications:time-interval.png | `2a8e0e96da43c5c634c5755eb05acbebacaa2aa6fc7e812a511d6a9a847314f2` |
| en | `notifications/route-time-intervals` | en:screenshots:vpsadmin:notifications:route-time-intervals.png | `934adb0770c163bde825ff84eacf68694aaf38cfbf3463ecb03bcf05f229f490` |
| en | `notifications/event-suppressed` | en:screenshots:vpsadmin:notifications:event-suppressed.png | `bae5860bb0ce09ed73a31c361adfa517904463551758f198cc6ea9ec4742e38a` |
