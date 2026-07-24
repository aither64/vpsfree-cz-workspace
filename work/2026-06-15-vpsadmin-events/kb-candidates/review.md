# KB navigation annotation review

Changed pages: 4
New pages: 2
Selected media: 50
Annotation tags: 33

| Language | Page | Semantic path | Count | Existing text | Candidate text |
| --- | --- | --- | ---: | --- | --- |
| cs | navody:vps:uzivatele | `notifications.open` | 1 | ===== Konfigurace e-mailových adres ===== ↵ vpsAdmin umožňuje nastavit jeden primární e-mail patřící majiteli účtu -- ↵ členovi v našem spolku. Ten musí být nastaven a může být jen jeden. Krom toho je ↵ možné nastavit různé e-mailové adresy pro různé typy kontaktů -- např. účetní a ↵ správce VPS. Toto nastavení lze měnit v detailech uživatelského účtu ↵ (<vpsadmin-nav id="member.edit-profile.open">vpsAdmin -> Upravit profil</vpsadmin-nav>). ↵  ↵ {{:cs:screenshots:vpsadmin:account:email-roles.png?300\|}} ↵  ↵ Například, správce členství (role Vedení účtu) dostává následující ↵ maily: ↵  ↵   * upozornění k platbě členského příspěvku, ↵   * pozastavení/obnovení členství, ↵   * potvrzení přijetí platby. ↵  ↵ Správce VPS (role Správce systému) pak maily o: ↵  ↵   * změně stavu VPS, ↵   * změně konfigurace VPS, ↵   * stahování záloh, ↵   * migrace VPS. ↵  ↵ ==== Detailní nastavení ==== ↵ Komu by nestačilo nastavení různých e-mailových adres pro různé role, nebo ↵ některé e-maily nechce vůbec dostávat, existuje ještě pokročilé nastavení ↵ (<vpsadmin-nav id="member.advanced-email-configuration.open">vpsAdmin -> Upravit profil -> Pokročilá konfigurace e-mailu</vpsadmin-nav>). Zde si můžete ↵ nastavit libovolné adresy pro vybrané typy e-mailů, případně zasílání zrušit ↵ úplně. ↵  ↵ {{:cs:screenshots:vpsadmin:account:mail-template-recipients.png?300\|}} | ===== E-mailová adresa a notifikace ===== ↵ Primární e-mailová adresa patří majiteli účtu — členovi spolku. Je povinná, ↵ může být pouze jedna a mění se v nastavení účtu (vpsAdmin → Upravit profil). ↵  ↵ Doručování provozních zpráv se nyní nastavuje pomocí událostí, rout, příjemců ↵ a cílů. Výchozí e-mailový cíl používá primární adresu; další adresy lze přidat ↵ a ověřit jako vlastní cíle. Postup včetně ztlumení vybraných událostí popisuje ↵ návod <vpsadmin-nav id="notifications.open">vpsAdmin → Notifikace</vpsadmin-nav>. |
| cs | navody:vps:uzivatele | `member.edit-profile.open` | 1 | vpsAdmin → Upravit profil | <vpsadmin-nav id="member.edit-profile.open">vpsAdmin → Upravit profil</vpsadmin-nav> |
| en | manuals:vps:users | `notifications.open` | 1 | ===== E-mail addresses ===== ↵ vpsAdmin allows users to set one primary e-mail address belonging to the ↵ account owner -- a member of our association. This address must be set and ↵ can only be a single address. In addition to the primary e-mail address, you ↵ can set different addresses for certain contact roles, such as an accountant ↵ or system administrator. These settings can be changed in user profile details ↵ (<vpsadmin-nav id="member.edit-profile.open">vpsAdmin -> Edit profile</vpsadmin-nav>) ↵  ↵ {{:en:screenshots:vpsadmin:account:email-roles.png?300\|}} ↵  ↵ For example, the account manager receives e-mails about: ↵  ↵   * payment notification, ↵   * suspension/activation of the membership, ↵   * accepted payments. ↵  ↵ The system administrator receives e-mails about: ↵  ↵   * VPS status changes, ↵   * VPS configuration changes, ↵   * backup downloads, ↵   * VPS migrations. ↵  ↵ ==== Advanced settings ==== ↵ Should contact roles not be enough or if don't wish to receive certain ↵ e-mails, there is an advanced settings form (<vpsadmin-nav id="member.advanced-email-configuration.open">vpsAdmin -> Edit profile -> ↵ Advanced e-mail configuration</vpsadmin-nav>). You can choose different e-mail addresses for ↵ specific mail templates or disable receiving of some mails altogether. ↵  ↵ {{:en:screenshots:vpsadmin:account:mail-template-recipients.png?300\|}} | ===== E-mail address and notifications ===== ↵ The primary e-mail address belongs to the account owner, a member of the ↵ association. It is required, only one can be set, and it is changed in the ↵ account settings (vpsAdmin → Edit profile). ↵  ↵ Delivery of operational messages is now configured using events, routes, ↵ receivers and targets. The default e-mail target follows the primary address; ↵ additional addresses can be added and verified as custom targets. The ↵ <vpsadmin-nav id="notifications.open">vpsAdmin → Notifications</vpsadmin-nav> ↵ guide explains the complete setup, including how to mute selected events. |
| en | manuals:vps:users | `member.edit-profile.open` | 1 | vpsAdmin → Edit profile | <vpsadmin-nav id="member.edit-profile.open">vpsAdmin → Edit profile</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.open` | 1 | hlavní nabídce Notifikace | <vpsadmin-nav id="notifications.open">hlavní nabídce Notifikace</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.target-form.open` | 1 | V části **Cíle** přidejte dva e-mailové cíle | <vpsadmin-nav id="notifications.target-form.open">V části **Cíle** přidejte dva e-mailové cíle</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.receivers.open` | 1 | V části **Příjemci** vytvořte příjemce **Kontakt účtu** | <vpsadmin-nav id="notifications.receivers.open">V části **Příjemci** vytvořte příjemce **Kontakt účtu**</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.routes.open` | 1 | V části **Routy** klikněte na **Přidat routu** | <vpsadmin-nav id="notifications.routes.open">V části **Routy** klikněte na **Přidat routu**</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.event-route-matches.open` | 1 | detail v **Událostech** | <vpsadmin-nav id="notifications.event-route-matches.open">detail v **Událostech**</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.target-form.open` | 1 | V části **Cíle** přidejte cíl typu **Telegram** | <vpsadmin-nav id="notifications.target-form.open">V části **Cíle** přidejte cíl typu **Telegram**</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.routes.open` | 1 | dočasnou routou | <vpsadmin-nav id="notifications.routes.open">dočasnou routou</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.event-route-matches.open` | 1 | v jejím detailu nebo pomocí počítadla zásahů | <vpsadmin-nav id="notifications.event-route-matches.open">v jejím detailu nebo pomocí počítadla zásahů</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.event-route-matches.open` | 1 | v detailu nebo počítadlem zásahů | <vpsadmin-nav id="notifications.event-route-matches.open">v detailu nebo počítadlem zásahů</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.target-form.open` | 1 | V části **Cíle** přidejte cíl typu **Webhook** | <vpsadmin-nav id="notifications.target-form.open">V části **Cíle** přidejte cíl typu **Webhook**</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.event-route-matches.open` | 1 | V detailu události | <vpsadmin-nav id="notifications.event-route-matches.open">V detailu události</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.routes.open` | 1 | v Notifikace → Routy. | v <vpsadmin-nav id="notifications.routes.open">Notifikace → Routy</vpsadmin-nav>. |
| cs | navody:notifikace | `notifications.receivers.open` | 1 | Notifikace → Příjemci | <vpsadmin-nav id="notifications.receivers.open">Notifikace → Příjemci</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.target-form.open` | 1 | v nabídce Notifikace → Cíle. | v nabídce <vpsadmin-nav id="notifications.target-form.open">Notifikace → Cíle</vpsadmin-nav>. |
| cs | navody:notifikace | `notifications.time-intervals.open` | 1 | Notifikace → Časové intervaly | <vpsadmin-nav id="notifications.time-intervals.open">Notifikace → Časové intervaly</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.route-time-intervals.open` | 1 | Notifikace → Routy → upravit routu | <vpsadmin-nav id="notifications.route-time-intervals.open">Notifikace → Routy → upravit routu</vpsadmin-nav> |
| cs | navody:notifikace | `notifications.event-route-matches.open` | 1 | Notifikace → Události → detail události | <vpsadmin-nav id="notifications.event-route-matches.open">Notifikace → Události → detail události</vpsadmin-nav> |
| en | manuals:notifications | `notifications.open` | 1 | main Notifications menu | <vpsadmin-nav id="notifications.open">main Notifications menu</vpsadmin-nav> |
| en | manuals:notifications | `notifications.target-form.open` | 1 | Under **Targets**, add two e-mail targets | <vpsadmin-nav id="notifications.target-form.open">Under **Targets**, add two e-mail targets</vpsadmin-nav> |
| en | manuals:notifications | `notifications.receivers.open` | 1 | Under **Receivers**, create an **Account contact** receiver | <vpsadmin-nav id="notifications.receivers.open">Under **Receivers**, create an **Account contact** receiver</vpsadmin-nav> |
| en | manuals:notifications | `notifications.target-form.open` | 1 | Under **Targets**, add a **Telegram** target | <vpsadmin-nav id="notifications.target-form.open">Under **Targets**, add a **Telegram** target</vpsadmin-nav> |
| en | manuals:notifications | `notifications.event-route-matches.open` | 1 | in its detail or from the route hit count | <vpsadmin-nav id="notifications.event-route-matches.open">in its detail or from the route hit count</vpsadmin-nav> |
| en | manuals:notifications | `notifications.event-route-matches.open` | 1 | in the event detail | <vpsadmin-nav id="notifications.event-route-matches.open">in the event detail</vpsadmin-nav> |
| en | manuals:notifications | `notifications.routes.open` | 1 | at Notifications → Routes. | at <vpsadmin-nav id="notifications.routes.open">Notifications → Routes</vpsadmin-nav>. |
| en | manuals:notifications | `notifications.receivers.open` | 1 | Notifications → Receivers | <vpsadmin-nav id="notifications.receivers.open">Notifications → Receivers</vpsadmin-nav> |
| en | manuals:notifications | `notifications.target-form.open` | 1 | from Notifications → Targets. | from <vpsadmin-nav id="notifications.target-form.open">Notifications → Targets</vpsadmin-nav>. |
| en | manuals:notifications | `notifications.time-intervals.open` | 1 | Notifications → Time intervals | <vpsadmin-nav id="notifications.time-intervals.open">Notifications → Time intervals</vpsadmin-nav> |
| en | manuals:notifications | `notifications.route-time-intervals.open` | 1 | Notifications → Routes → edit route | <vpsadmin-nav id="notifications.route-time-intervals.open">Notifications → Routes → edit route</vpsadmin-nav> |
| en | manuals:notifications | `notifications.event-route-matches.open` | 1 | Notifications → Event log → event detail | <vpsadmin-nav id="notifications.event-route-matches.open">Notifications → Event log → event detail</vpsadmin-nav> |

## Explicit exceptions

| Language | Page | Semantic path | Reason |
| --- | --- | --- | --- |

## New pages

| Language | Page | SHA-256 |
| --- | --- | --- |
| cs | navody:notifikace | `aa5b1fba594c2838ae85ef2afe4a8c3e445641744e12f141364484c2b6086636` |
| en | manuals:notifications | `3df8685ac2abfcc91af57fc0145ed49be29de180a01492c53e1ed722f3ee5f41` |

## Selected capture media

| Language | Capture | Media ID | SHA-256 |
| --- | --- | --- | --- |
| cs | `notifications/receiver` | cs:screenshots:vpsadmin:notifications:receiver.png | `7161a9b1f6c08a3f6a1a327e2fd1bbfa32b2254c1b12534b38b4e9e27acf21ce` |
| cs | `notifications/time-interval` | cs:screenshots:vpsadmin:notifications:time-interval.png | `82277ac2c5ef3cb1ce8e2fad7165ab75e7c38c096f73d6460160d8f015c8e558` |
| cs | `notifications/route-time-intervals` | cs:screenshots:vpsadmin:notifications:route-time-intervals.png | `ac7e16c9756ae1e3915c3efc8bd1a9860f409599a92e415322ca9850ba1df83f` |
| cs | `notifications/event-suppressed` | cs:screenshots:vpsadmin:notifications:event-suppressed.png | `90f459113368fbbba6e1ab181817c01a45536c43efb00d630ef6d7886e0e9a90` |
| cs | `notifications/example-role-receiver` | cs:screenshots:vpsadmin:notifications:example-role-receiver.png | `199793e51baac91f8b950be9803cf284a035552f2d7f818b65b189cf347a48a5` |
| cs | `notifications/example-role-routing` | cs:screenshots:vpsadmin:notifications:example-role-routing.png | `25d5ff584f17b287e00d5e625398adae244866a4c28b9f6c05cf3aabe0d2838a` |
| cs | `notifications/example-role-admin-route` | cs:screenshots:vpsadmin:notifications:example-role-admin-route.png | `abe8882980836c6c0417c6e1894bd4fb9a10e207d4959984d869cb56d794507e` |
| cs | `notifications/example-role-result` | cs:screenshots:vpsadmin:notifications:example-role-result.png | `fc153dc469993fcdd4de93f9a9ae3a54cab38eb6e1a27c5cee17b1d2553d4571` |
| cs | `notifications/example-mute-oom` | cs:screenshots:vpsadmin:notifications:example-mute-oom.png | `79c08386c76538174c38603227300f1a798c7ee36dc330563efcf7676ae6f627` |
| cs | `notifications/example-mute-incident-route` | cs:screenshots:vpsadmin:notifications:example-mute-incident-route.png | `9213e16fa026c627f57371559b969a03ad9134caaaeea2fe27c322171984b71b` |
| cs | `notifications/example-mute-result` | cs:screenshots:vpsadmin:notifications:example-mute-result.png | `487dc94659f4961e0284edc8dec50342a0b45382892332dc816a0353b4e0e7e2` |
| cs | `notifications/example-telegram-target` | cs:screenshots:vpsadmin:notifications:example-telegram-target.png | `b79d292785cf213275fcddc8ae1ce1749f743b731f7ef1a34085a892fcde92bb` |
| cs | `notifications/example-telegram` | cs:screenshots:vpsadmin:notifications:example-telegram.png | `43bbb3dd4cd01238408eae58058f7ad1e945f616c4187287ac10fd543680b14c` |
| cs | `notifications/example-telegram-monitoring-route` | cs:screenshots:vpsadmin:notifications:example-telegram-monitoring-route.png | `7cd756e047e75c62a29c737e9176b32ce30c640121846de25af38575f1f146ec` |
| cs | `notifications/example-telegram-incident-route` | cs:screenshots:vpsadmin:notifications:example-telegram-incident-route.png | `4951436738b8629c4463fd3def013ccf360f91a136d92363fb11d94ae391ed0c` |
| cs | `notifications/example-telegram-result` | cs:screenshots:vpsadmin:notifications:example-telegram-result.png | `409867a521dc4cbc65019387d0ef7413b6e916c250a9d4afeedfda830edf0b30` |
| cs | `notifications/example-sms-verification` | cs:screenshots:vpsadmin:notifications:example-sms-verification.png | `f64a61ebb56e0f99e6a6d80318e69fa7366123da46ad1f20bcf597c41f600d75` |
| cs | `notifications/example-sms` | cs:screenshots:vpsadmin:notifications:example-sms.png | `bc170c721ed7a85a717390567bfa76c091d1254e7bab1c2c6b61da21dadf5393` |
| cs | `notifications/example-sms-account-route` | cs:screenshots:vpsadmin:notifications:example-sms-account-route.png | `85759b9720e636eaba0fabce7bbd46d8e1bf8726266e8169365c38f9febdad67` |
| cs | `notifications/example-sms-vps-route` | cs:screenshots:vpsadmin:notifications:example-sms-vps-route.png | `29a164b0079b84db0b2407ff9d12347f5eee63ae79d45de5a98517554e43fde0` |
| cs | `notifications/example-sms-result` | cs:screenshots:vpsadmin:notifications:example-sms-result.png | `bdfdb0bf16b1bcbad1221f46e93da1fecf9e4f9006aca66bfc29168bd3ab5d3e` |
| cs | `notifications/example-webhook-target` | cs:screenshots:vpsadmin:notifications:example-webhook-target.png | `4596ae8d32a0a4e8e6a5a381034130607b62be24361581e3edd6966992b272ac` |
| cs | `notifications/example-webhook` | cs:screenshots:vpsadmin:notifications:example-webhook.png | `a526d77d45d285691f03164f6440bbd5ed496ee50b16e3edbefae8ad6a3c78e3` |
| cs | `notifications/example-webhook-route` | cs:screenshots:vpsadmin:notifications:example-webhook-route.png | `e644c6dc6ddaec1443368470a39e4047015885b063d5eeb894ef091a1eff8d72` |
| cs | `notifications/example-webhook-result` | cs:screenshots:vpsadmin:notifications:example-webhook-result.png | `39d1fcdf16f00ff490ee41a5725e6244642570cb343d35580d4a4b6fc56c1a4b` |
| en | `notifications/receiver` | en:screenshots:vpsadmin:notifications:receiver.png | `dd6ada08a4926e1e114309869c4988b7d4c09bc29c8efb0f183a40b20621ead4` |
| en | `notifications/time-interval` | en:screenshots:vpsadmin:notifications:time-interval.png | `e15c5dd7ff9527fbb02afc0cee61d6f58b614eb746a18106b6873a2fcdf2b7c1` |
| en | `notifications/route-time-intervals` | en:screenshots:vpsadmin:notifications:route-time-intervals.png | `934adb0770c163bde825ff84eacf68694aaf38cfbf3463ecb03bcf05f229f490` |
| en | `notifications/event-suppressed` | en:screenshots:vpsadmin:notifications:event-suppressed.png | `137edfbabb28db1b4100f76af15103863f25efbd9ac6f380e0c60230f6a27a2e` |
| en | `notifications/example-role-receiver` | en:screenshots:vpsadmin:notifications:example-role-receiver.png | `659f8a3c03db2805d30fb0c7b6376186d3bb99caa7c03f5aa092d2e8002d9669` |
| en | `notifications/example-role-routing` | en:screenshots:vpsadmin:notifications:example-role-routing.png | `bbb34564628742d1cbbf9afdc254d321f4def422fe5e1076a17145c85ba2c88c` |
| en | `notifications/example-role-admin-route` | en:screenshots:vpsadmin:notifications:example-role-admin-route.png | `44985b09e724c548a964a558f30c6a615b55a093e1bbcbe5e1b55e411064ed3e` |
| en | `notifications/example-role-result` | en:screenshots:vpsadmin:notifications:example-role-result.png | `9fb732cd6a365f43ac955edc7701aefc20c1c235d32ba067bcfde1c785169b9e` |
| en | `notifications/example-mute-oom` | en:screenshots:vpsadmin:notifications:example-mute-oom.png | `ebe5b1bdfa5fba75c7959a5e128e4062976b829e8f474c6433686890a64bae6a` |
| en | `notifications/example-mute-incident-route` | en:screenshots:vpsadmin:notifications:example-mute-incident-route.png | `c31f064f5c6399b9021aeffcab2783aca5db8d6d1867af06962551cd21f0def9` |
| en | `notifications/example-mute-result` | en:screenshots:vpsadmin:notifications:example-mute-result.png | `933679a955b0fb562e4284ef828928f97194aa1aca5a6adf2ad153fe5dba49bc` |
| en | `notifications/example-telegram-target` | en:screenshots:vpsadmin:notifications:example-telegram-target.png | `b4613f4dd024dbc0cb0f1e6ffda1b8739bd6e3c64a78ec74101bef623b919f73` |
| en | `notifications/example-telegram` | en:screenshots:vpsadmin:notifications:example-telegram.png | `6edb25693a674b1ee0876e822efb1f36a45c531424290b2a21bf4c4a65b7c74c` |
| en | `notifications/example-telegram-monitoring-route` | en:screenshots:vpsadmin:notifications:example-telegram-monitoring-route.png | `a4c3bfc2ab1d33f4d89fcd83ad67dbd343f5265e295bbf1567eacb56330f0dae` |
| en | `notifications/example-telegram-incident-route` | en:screenshots:vpsadmin:notifications:example-telegram-incident-route.png | `56b13cb8098394729104c714b4e90ccc57c44209341560fb66f7efe5f9b14b58` |
| en | `notifications/example-telegram-result` | en:screenshots:vpsadmin:notifications:example-telegram-result.png | `2018bb8dd2062124b5fba8fee14f0238ef0a3732a0b59c6e10c6ad12e6040179` |
| en | `notifications/example-sms-verification` | en:screenshots:vpsadmin:notifications:example-sms-verification.png | `7c2d407559f180ee338cf6c31ce43ceb7726582f11ab9898320fb132ee52c24e` |
| en | `notifications/example-sms` | en:screenshots:vpsadmin:notifications:example-sms.png | `912ce4b2c4edc81ce81975df28fbcfc0bea65ebedf8cf5807f2412fe7f50315d` |
| en | `notifications/example-sms-account-route` | en:screenshots:vpsadmin:notifications:example-sms-account-route.png | `9367b40b80e92a33bb9960948616de79f1dd4b1e9c13eee88e5a263dd2a3938c` |
| en | `notifications/example-sms-vps-route` | en:screenshots:vpsadmin:notifications:example-sms-vps-route.png | `ce958b63c071d7f90141432979dbc7ecb440c4ec6911758e0ebe2ff9efbf905b` |
| en | `notifications/example-sms-result` | en:screenshots:vpsadmin:notifications:example-sms-result.png | `f6abd41fd87846da62686422e9a51421ecbcc47ec46b5df4fa4d80f8e8407b9c` |
| en | `notifications/example-webhook-target` | en:screenshots:vpsadmin:notifications:example-webhook-target.png | `0f6e0cb39bb30f2f36aac411b220124a440ee01f4a55bebf4bf1cb91a29e127c` |
| en | `notifications/example-webhook` | en:screenshots:vpsadmin:notifications:example-webhook.png | `9587dc4ef8a7682984dc22044ace2ef523c9cc79392602dff7ebc80ff02c1cb4` |
| en | `notifications/example-webhook-route` | en:screenshots:vpsadmin:notifications:example-webhook-route.png | `5ba59ce2e8b31e7b140bec0cb0ea17766887ef91cd69773b563c0d69dd113242` |
| en | `notifications/example-webhook-result` | en:screenshots:vpsadmin:notifications:example-webhook-result.png | `8dba59fc858de61919d63523a1a274caa77b46ca7572cc6b1756b026ad87d65b` |
