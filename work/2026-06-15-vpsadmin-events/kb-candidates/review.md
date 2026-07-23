# KB navigation annotation review

Changed pages: 4
New pages: 2
Selected media: 20
Annotation tags: 18

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
| cs | navody:notifikace | `notifications.event-route-matches.open` | 1 | z detailu skutečného incidentu v přehledu událostí | <vpsadmin-nav id="notifications.event-route-matches.open">z detailu skutečného incidentu v přehledu událostí</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.event-route-matches.open` | 1 | Notifikace → Události → detail události | <vpsadmin-nav id="notifications.event-route-matches.open">Notifikace → Události → detail události</vpsadmin-nav> |
| en | manuals:notifications | `notifications.open` | 1 | main Notifications menu | <vpsadmin-nav id="notifications.open">main Notifications menu</vpsadmin-nav> |
| en | manuals:notifications | `notifications.routes.open` | 1 | at Notifications → Routes. | at <vpsadmin-nav id="notifications.routes.open">Notifications → Routes</vpsadmin-nav>. |
| en | manuals:notifications | `notifications.receivers.open` | 1 | Notifications → Receivers | <vpsadmin-nav id="notifications.receivers.open">Notifications → Receivers</vpsadmin-nav> |
| en | manuals:notifications | `notifications.time-intervals.open` | 1 | Notifications → Time intervals | <vpsadmin-nav id="notifications.time-intervals.open">Notifications → Time intervals</vpsadmin-nav> |
| en | manuals:notifications | `notifications.route-time-intervals.open` | 1 | Notifications → Routes → edit route | <vpsadmin-nav id="notifications.route-time-intervals.open">Notifications → Routes → edit route</vpsadmin-nav> |
| en | manuals:notifications | `notifications.event-route-matches.open` | 1 | from the detail of a real incident in the event log | <vpsadmin-nav id="notifications.event-route-matches.open">from the detail of a real incident in the event log</vpsadmin-nav> |
| en | manuals:notifications | `notifications.event-route-matches.open` | 1 | Notifications → Event log → event detail | <vpsadmin-nav id="notifications.event-route-matches.open">Notifications → Event log → event detail</vpsadmin-nav> |

## Explicit exceptions

| Language | Page | Semantic path | Reason |
| --- | --- | --- | --- |

## New pages

| Language | Page | SHA-256 |
| --- | --- | --- |
| cs | navody:notifikace | `4c653cbcf8975513407dc6290a1ce4a04f98c8bac199361797b14e3740e6d123` |
| en | manuals:notifications | `c268652e9e509e117f95d7cc8ef2dd071ad881c14c0d28205f84573714226409` |

## Selected capture media

| Language | Capture | Media ID | SHA-256 |
| --- | --- | --- | --- |
| cs | `notifications/routes` | cs:screenshots:vpsadmin:notifications:routes.png | `ce112aff059e9f6e516b53a7f6fe183495a255aa92fe7949cd9de306fae60057` |
| cs | `notifications/receiver` | cs:screenshots:vpsadmin:notifications:receiver.png | `7161a9b1f6c08a3f6a1a327e2fd1bbfa32b2254c1b12534b38b4e9e27acf21ce` |
| cs | `notifications/time-interval` | cs:screenshots:vpsadmin:notifications:time-interval.png | `82277ac2c5ef3cb1ce8e2fad7165ab75e7c38c096f73d6460160d8f015c8e558` |
| cs | `notifications/route-time-intervals` | cs:screenshots:vpsadmin:notifications:route-time-intervals.png | `ac7e16c9756ae1e3915c3efc8bd1a9860f409599a92e415322ca9850ba1df83f` |
| cs | `notifications/event-suppressed` | cs:screenshots:vpsadmin:notifications:event-suppressed.png | `2f848ed07d69c6925ff78ea02420fd36ef253857058495de7ca220464a6f83e0` |
| cs | `notifications/example-role-routing` | cs:screenshots:vpsadmin:notifications:example-role-routing.png | `25d5ff584f17b287e00d5e625398adae244866a4c28b9f6c05cf3aabe0d2838a` |
| cs | `notifications/example-mute-oom` | cs:screenshots:vpsadmin:notifications:example-mute-oom.png | `204b4fe0db30630b40df5b9df64617d564b886e873c86608ec8ccaf4adf63d47` |
| cs | `notifications/example-telegram` | cs:screenshots:vpsadmin:notifications:example-telegram.png | `43bbb3dd4cd01238408eae58058f7ad1e945f616c4187287ac10fd543680b14c` |
| cs | `notifications/example-sms` | cs:screenshots:vpsadmin:notifications:example-sms.png | `bf6b307039367d90feb5d771595142a81a1219ed67ab37e486149cd460f1039e` |
| cs | `notifications/example-webhook` | cs:screenshots:vpsadmin:notifications:example-webhook.png | `cb9f9fbb752087371b89bb3037722f6ca0857f16beca8ba043a8f55a5ffc2fc4` |
| en | `notifications/routes` | en:screenshots:vpsadmin:notifications:routes.png | `5ba10809dfcf8ddbbdfb1e55ead3af167688f40eea9358e16b7450231ef2f77a` |
| en | `notifications/receiver` | en:screenshots:vpsadmin:notifications:receiver.png | `9909b554a00c7efab9c996f84c02e5f772b278e3df03adbea49a5859bb1772aa` |
| en | `notifications/time-interval` | en:screenshots:vpsadmin:notifications:time-interval.png | `57b09b3a779a5e96ed10f2d156484b04cd1b86455a9242b9b3c47c23f1082a20` |
| en | `notifications/route-time-intervals` | en:screenshots:vpsadmin:notifications:route-time-intervals.png | `934adb0770c163bde825ff84eacf68694aaf38cfbf3463ecb03bcf05f229f490` |
| en | `notifications/event-suppressed` | en:screenshots:vpsadmin:notifications:event-suppressed.png | `166279cb37cbf4c0242f39c3b4b7ddb561431c6cbdfdcee0e08adb3b5b7011b4` |
| en | `notifications/example-role-routing` | en:screenshots:vpsadmin:notifications:example-role-routing.png | `bbb34564628742d1cbbf9afdc254d321f4def422fe5e1076a17145c85ba2c88c` |
| en | `notifications/example-mute-oom` | en:screenshots:vpsadmin:notifications:example-mute-oom.png | `b11e3a68b5840a558a6fab0667e2f6b12d14c3cabf51344d77b4927f1756199a` |
| en | `notifications/example-telegram` | en:screenshots:vpsadmin:notifications:example-telegram.png | `a417fdb482b6a83c11b6b10eb7eabde3eb7b8077b5ffc8c34bb29c4beb3bca8d` |
| en | `notifications/example-sms` | en:screenshots:vpsadmin:notifications:example-sms.png | `f4f90bf2b3e4d237725a646228f80b46e7846faab1ed6d08daf44862dd96dc09` |
| en | `notifications/example-webhook` | en:screenshots:vpsadmin:notifications:example-webhook.png | `711feffe549a7cfa1d3051055035addfb6a02db86226832022919a781764329c` |
