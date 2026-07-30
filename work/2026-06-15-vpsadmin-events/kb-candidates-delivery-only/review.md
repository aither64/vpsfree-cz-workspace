# KB navigation annotation review

Changed pages: 16
New pages: 14
Selected media: 48
Annotation tags: 4

| Language | Page | Semantic path | Count | Existing text | Candidate text |
| --- | --- | --- | ---: | --- | --- |
| cs | navody:vps:uzivatele | `notifications.open` | 1 | ===== Konfigurace e-mailových adres ===== ↵ vpsAdmin umožňuje nastavit jeden primární e-mail patřící majiteli účtu -- ↵ členovi v našem spolku. Ten musí být nastaven a může být jen jeden. Krom toho je ↵ možné nastavit různé e-mailové adresy pro různé typy kontaktů -- např. účetní a ↵ správce VPS. Toto nastavení lze měnit v detailech uživatelského účtu ↵ (<vpsadmin-nav id="member.edit-profile.open">vpsAdmin -> Upravit profil</vpsadmin-nav>). ↵  ↵ {{:cs:screenshots:vpsadmin:account:email-roles.png?300\|}} ↵  ↵ Například, správce členství (role Vedení účtu) dostává následující ↵ maily: ↵  ↵   * upozornění k platbě členského příspěvku, ↵   * pozastavení/obnovení členství, ↵   * potvrzení přijetí platby. ↵  ↵ Správce VPS (role Správce systému) pak maily o: ↵  ↵   * změně stavu VPS, ↵   * změně konfigurace VPS, ↵   * stahování záloh, ↵   * migrace VPS. ↵  ↵ ==== Detailní nastavení ==== ↵ Komu by nestačilo nastavení různých e-mailových adres pro různé role, nebo ↵ některé e-maily nechce vůbec dostávat, existuje ještě pokročilé nastavení ↵ (<vpsadmin-nav id="member.advanced-email-configuration.open">vpsAdmin -> Upravit profil -> Pokročilá konfigurace e-mailu</vpsadmin-nav>). Zde si můžete ↵ nastavit libovolné adresy pro vybrané typy e-mailů, případně zasílání zrušit ↵ úplně. ↵  ↵ {{:cs:screenshots:vpsadmin:account:mail-template-recipients.png?300\|}} | ===== E-mailová adresa a notifikace ===== ↵ Primární e-mailová adresa patří majiteli účtu — členovi spolku. Je povinná, ↵ může být pouze jedna a mění se v nastavení účtu (vpsAdmin → Upravit profil). ↵  ↵ Doručování provozních zpráv se nyní nastavuje pomocí událostí, rout, příjemců ↵ a cílů. Výchozí e-mailový cíl používá primární adresu; další adresy lze přidat ↵ a ověřit jako vlastní cíle. Postup včetně ztlumení vybraných událostí popisuje ↵ návod <vpsadmin-nav id="notifications.open">vpsAdmin → Notifikace</vpsadmin-nav>. |
| cs | navody:vps:uzivatele | `member.edit-profile.open` | 1 | vpsAdmin → Upravit profil | <vpsadmin-nav id="member.edit-profile.open">vpsAdmin → Upravit profil</vpsadmin-nav> |
| en | manuals:vps:users | `notifications.open` | 1 | ===== E-mail addresses ===== ↵ vpsAdmin allows users to set one primary e-mail address belonging to the ↵ account owner -- a member of our association. This address must be set and ↵ can only be a single address. In addition to the primary e-mail address, you ↵ can set different addresses for certain contact roles, such as an accountant ↵ or system administrator. These settings can be changed in user profile details ↵ (<vpsadmin-nav id="member.edit-profile.open">vpsAdmin -> Edit profile</vpsadmin-nav>) ↵  ↵ {{:en:screenshots:vpsadmin:account:email-roles.png?300\|}} ↵  ↵ For example, the account manager receives e-mails about: ↵  ↵   * payment notification, ↵   * suspension/activation of the membership, ↵   * accepted payments. ↵  ↵ The system administrator receives e-mails about: ↵  ↵   * VPS status changes, ↵   * VPS configuration changes, ↵   * backup downloads, ↵   * VPS migrations. ↵  ↵ ==== Advanced settings ==== ↵ Should contact roles not be enough or if don't wish to receive certain ↵ e-mails, there is an advanced settings form (<vpsadmin-nav id="member.advanced-email-configuration.open">vpsAdmin -> Edit profile -> ↵ Advanced e-mail configuration</vpsadmin-nav>). You can choose different e-mail addresses for ↵ specific mail templates or disable receiving of some mails altogether. ↵  ↵ {{:en:screenshots:vpsadmin:account:mail-template-recipients.png?300\|}} | ===== E-mail address and notifications ===== ↵ The primary e-mail address belongs to the account owner, a member of the ↵ association. It is required, only one can be set, and it is changed in the ↵ account settings (vpsAdmin → Edit profile). ↵  ↵ Delivery of operational messages is now configured using events, routes, ↵ receivers and targets. The default e-mail target follows the primary address; ↵ additional addresses can be added and verified as custom targets. The ↵ <vpsadmin-nav id="notifications.open">vpsAdmin → Notifications</vpsadmin-nav> ↵ guide explains the complete setup, including how to mute selected events. |
| en | manuals:vps:users | `member.edit-profile.open` | 1 | vpsAdmin → Edit profile | <vpsadmin-nav id="member.edit-profile.open">vpsAdmin → Edit profile</vpsadmin-nav> |

## Explicit exceptions

| Language | Page | Semantic path | Reason |
| --- | --- | --- | --- |

## New pages

| Language | Page | SHA-256 |
| --- | --- | --- |
| cs | navody:notifikace | `d2d03cca70f4607455a04179fa91277108d186d5723d701ef18198efbf1c23e0` |
| cs | navody:notifikace:role_udalosti | `6b48651c51549d68106961a889825e381f0d2148ecb927f38bc38517d0c9b9fb` |
| cs | navody:notifikace:ztlumeni_oom | `0249487d2274089da99133d1ac9147ace9a896d3682e0b1af53566133017688f` |
| cs | navody:notifikace:ztlumeni_incidentu | `181392c67a88ce65981b3ed891f4031bdd95e9d7d1a8fbd02b118777fc867c6e` |
| cs | navody:notifikace:telegram | `ed62a33f3a3bc9d8ad7a9a8e7ae53abfbfc26bd9fb38bbc1bfc60d264e6ee47a` |
| cs | navody:notifikace:sms | `46de429888786708f4e0eabf0fb11751347070428dd16b1a50d14a312dc43425` |
| cs | navody:notifikace:webhook | `3f427383464688eedfd641cabd240bd6c751f1f6e470cd7fe3a9413d552d8b7e` |
| en | manuals:notifications | `366346f089594fd5a4fd9a61b94bb1468001ee5c020ad4109ccc48d3150a21e2` |
| en | manuals:notifications:event_roles | `488e8f9cc9720c0409d7983b6eeae7cae89f23e2372342c031e2a523be66277f` |
| en | manuals:notifications:mute_oom | `c0bd98ea6e0573bf3b1b99867fd3ec02a9e281fe8f12a786a3ecf2ab191140af` |
| en | manuals:notifications:mute_incidents | `362e265084f54f370d92e715a7f7f9cd353779cb5f2882513413b5253ab4041e` |
| en | manuals:notifications:telegram | `8cf3d952b78d13c4a4ba1f003a575707db2786cabdbf8fe82648a80bb41d9dd2` |
| en | manuals:notifications:sms | `6c8428110e97fbb1356231171de788ae529b29c25d0dce0257a581187a129bbe` |
| en | manuals:notifications:webhook | `2d0ed605fb9756bf8c5f36c6bd7dd60d955fccf7e68584658e8e83bfbb4f4219` |

## Canonical code samples

| ID | File | Language | Uses | SHA-256 |
| --- | --- | --- | ---: | --- |
| `notifications.webhook-server` | doc/examples/notifications/webhook_server.py | python | 2 | `82572c438f5ded1389d65c6f0896c86f0eb9b221d1f08a7795151d10b9b05274` |
| `notifications.webhook-single-payload` | doc/examples/notifications/webhook_single.json | json | 2 | `3ecced6bfbdbdc0d3669f646008dbd0909e2024676707d817c1691ea91dbbc97` |

## Selected capture media

| Language | Capture | Media ID | SHA-256 |
| --- | --- | --- | --- |
| cs | `notifications/receiver` | cs:screenshots:vpsadmin:notifications:receiver.png | `7161a9b1f6c08a3f6a1a327e2fd1bbfa32b2254c1b12534b38b4e9e27acf21ce` |
| cs | `notifications/time-interval` | cs:screenshots:vpsadmin:notifications:time-interval.png | `82277ac2c5ef3cb1ce8e2fad7165ab75e7c38c096f73d6460160d8f015c8e558` |
| cs | `notifications/route-time-intervals` | cs:screenshots:vpsadmin:notifications:route-time-intervals.png | `389ef724e324677442b7edebeabf84bac31e929369806d4de217862a2284ff13` |
| cs | `notifications/example-role-receiver` | cs:screenshots:vpsadmin:notifications:example-role-receiver.png | `2aa9017cf93ebdd611641f6a9f5f8d1cd56b96a4fc739334673f87e6bf387a77` |
| cs | `notifications/example-role-routing` | cs:screenshots:vpsadmin:notifications:example-role-routing.png | `9003406a6814490cae83169402c6917a093a08ce2a74db68c44f7d114f104104` |
| cs | `notifications/example-role-admin-route` | cs:screenshots:vpsadmin:notifications:example-role-admin-route.png | `026b9f0aeab8f915b29d394744710dd0df0344c364516cad0bb7a2f1e5c7cf95` |
| cs | `notifications/example-role-result` | cs:screenshots:vpsadmin:notifications:example-role-result.png | `fc153dc469993fcdd4de93f9a9ae3a54cab38eb6e1a27c5cee17b1d2553d4571` |
| cs | `notifications/example-mute-oom` | cs:screenshots:vpsadmin:notifications:example-mute-oom.png | `d5d660a3e0a0635f34ff987a5e43d82483d80203a1b22fdfe138715c5537723b` |
| cs | `notifications/example-mute-incident-route` | cs:screenshots:vpsadmin:notifications:example-mute-incident-route.png | `0f9b7c3589bd3470df7fd746637847347aa6c4246e06f3c9db5328572a3718f4` |
| cs | `notifications/example-telegram-target` | cs:screenshots:vpsadmin:notifications:example-telegram-target.png | `b79d292785cf213275fcddc8ae1ce1749f743b731f7ef1a34085a892fcde92bb` |
| cs | `notifications/example-telegram` | cs:screenshots:vpsadmin:notifications:example-telegram.png | `17ffb6a4dbb6a927bac77b08652b4f839465676f0979bb021c1a6a865eb222f6` |
| cs | `notifications/example-telegram-monitoring-route` | cs:screenshots:vpsadmin:notifications:example-telegram-monitoring-route.png | `c5cbb7a70f5e85e5bd34dca954be357660d79133cb738dcda3295adb731a8272` |
| cs | `notifications/example-telegram-incident-route` | cs:screenshots:vpsadmin:notifications:example-telegram-incident-route.png | `e4245682366d61ba2cfb9fc8f3d97a3ace7abd72cb66751f22b8f075ca55114b` |
| cs | `notifications/example-telegram-result` | cs:screenshots:vpsadmin:notifications:example-telegram-result.png | `409867a521dc4cbc65019387d0ef7413b6e916c250a9d4afeedfda830edf0b30` |
| cs | `notifications/example-sms-verification` | cs:screenshots:vpsadmin:notifications:example-sms-verification.png | `65d1000c22d503cecc2f7ff9cd0edad54225381831869f7137020731ba3ef238` |
| cs | `notifications/example-sms` | cs:screenshots:vpsadmin:notifications:example-sms.png | `2e68a0190e7ef04310186fb77536f2d6fcff23e90c41ebc88134408304e61666` |
| cs | `notifications/example-sms-account-route` | cs:screenshots:vpsadmin:notifications:example-sms-account-route.png | `71f9aee319eaa47cb6989e8b62388b3b948ab86a0266cde3e86e1c04dfd6a077` |
| cs | `notifications/example-sms-vps-route` | cs:screenshots:vpsadmin:notifications:example-sms-vps-route.png | `e3a7370a09eadb6f35627c9add145f56534b09ee43f5241f4a8a3921678ff1c5` |
| cs | `notifications/example-sms-result` | cs:screenshots:vpsadmin:notifications:example-sms-result.png | `bdfdb0bf16b1bcbad1221f46e93da1fecf9e4f9006aca66bfc29168bd3ab5d3e` |
| cs | `notifications/example-webhook-target` | cs:screenshots:vpsadmin:notifications:example-webhook-target.png | `4596ae8d32a0a4e8e6a5a381034130607b62be24361581e3edd6966992b272ac` |
| cs | `notifications/example-webhook` | cs:screenshots:vpsadmin:notifications:example-webhook.png | `4d8ceee179a710a095df9c3bef268fd685af5163c74b621655587e082913fdab` |
| cs | `notifications/example-webhook-route` | cs:screenshots:vpsadmin:notifications:example-webhook-route.png | `ce206e9ddd89e55a3ab9d4c19d600fe4d9774f8b9e6ef5b4499a0f9366d87559` |
| cs | `notifications/example-webhook-result` | cs:screenshots:vpsadmin:notifications:example-webhook-result.png | `9397ad6e9a80a566247634bfda5a618db31aa3c28b2af1c35a5357f411442904` |
| en | `notifications/receiver` | en:screenshots:vpsadmin:notifications:receiver.png | `9909b554a00c7efab9c996f84c02e5f772b278e3df03adbea49a5859bb1772aa` |
| en | `notifications/time-interval` | en:screenshots:vpsadmin:notifications:time-interval.png | `57b09b3a779a5e96ed10f2d156484b04cd1b86455a9242b9b3c47c23f1082a20` |
| en | `notifications/route-time-intervals` | en:screenshots:vpsadmin:notifications:route-time-intervals.png | `5fa2f42f7ae29ac4a9afba48bd627fd86e3a13a697a190c1525c59374bceec1b` |
| en | `notifications/example-role-receiver` | en:screenshots:vpsadmin:notifications:example-role-receiver.png | `948dacd61e2c319c01246706ae0e29895b97bfba42d7b9b3660ae265eff7f382` |
| en | `notifications/example-role-routing` | en:screenshots:vpsadmin:notifications:example-role-routing.png | `9dc25bbfd05df7d9a18c7a754b3f4979bf79687624d38addea004c4b4fde1e70` |
| en | `notifications/example-role-admin-route` | en:screenshots:vpsadmin:notifications:example-role-admin-route.png | `e43a682960ea5ca4c85816c394d91e311313e0679c20dc74fa6ac78a09f0794d` |
| en | `notifications/example-role-result` | en:screenshots:vpsadmin:notifications:example-role-result.png | `9fb732cd6a365f43ac955edc7701aefc20c1c235d32ba067bcfde1c785169b9e` |
| en | `notifications/example-mute-oom` | en:screenshots:vpsadmin:notifications:example-mute-oom.png | `8e85073d9597d0d2ba7f2b9bcee9457abdfa9d9536ed1b0ee78c796d79f66808` |
| en | `notifications/example-mute-incident-route` | en:screenshots:vpsadmin:notifications:example-mute-incident-route.png | `422ceb236781e6b1f7af07b01993e718049914863cb8a42974e7e0a7a803329b` |
| en | `notifications/example-telegram-target` | en:screenshots:vpsadmin:notifications:example-telegram-target.png | `b4613f4dd024dbc0cb0f1e6ffda1b8739bd6e3c64a78ec74101bef623b919f73` |
| en | `notifications/example-telegram` | en:screenshots:vpsadmin:notifications:example-telegram.png | `8d14c7d38d32bb5ab08774cfe3ab868567c436279129c0bfd497265bb6336d85` |
| en | `notifications/example-telegram-monitoring-route` | en:screenshots:vpsadmin:notifications:example-telegram-monitoring-route.png | `1a7f892cc78b1ce543af5f2a156003105cd578a3987a595087ff85e36bb3fa23` |
| en | `notifications/example-telegram-incident-route` | en:screenshots:vpsadmin:notifications:example-telegram-incident-route.png | `fab131b725e61223129d73cb0da2fc3dc5325d854b53bbe2e1a1d1794c786a4a` |
| en | `notifications/example-telegram-result` | en:screenshots:vpsadmin:notifications:example-telegram-result.png | `2018bb8dd2062124b5fba8fee14f0238ef0a3732a0b59c6e10c6ad12e6040179` |
| en | `notifications/example-sms-verification` | en:screenshots:vpsadmin:notifications:example-sms-verification.png | `67a101798f3083dca3683b89ccc5726401bfbd69c9eae782aedc52e137836ca6` |
| en | `notifications/example-sms` | en:screenshots:vpsadmin:notifications:example-sms.png | `4372bd01843b2b85efcf1392d47ab7243c5a95988aa2518f0c4d29c787fb3e08` |
| en | `notifications/example-sms-account-route` | en:screenshots:vpsadmin:notifications:example-sms-account-route.png | `e883bad56e665a58d3479b26bec393c8083e7ecf71e6dba9c576732149de77db` |
| en | `notifications/example-sms-vps-route` | en:screenshots:vpsadmin:notifications:example-sms-vps-route.png | `32218c3847c3b0ba0ee0de1878309528b25eba5e53a126cffc19982a3d065ee8` |
| en | `notifications/example-sms-result` | en:screenshots:vpsadmin:notifications:example-sms-result.png | `f6abd41fd87846da62686422e9a51421ecbcc47ec46b5df4fa4d80f8e8407b9c` |
| en | `notifications/example-webhook-target` | en:screenshots:vpsadmin:notifications:example-webhook-target.png | `0f6e0cb39bb30f2f36aac411b220124a440ee01f4a55bebf4bf1cb91a29e127c` |
| en | `notifications/example-webhook` | en:screenshots:vpsadmin:notifications:example-webhook.png | `a544b0313296120ba9301010150b00142af97e3b264741ccc581b43c9411d0d2` |
| en | `notifications/example-webhook-route` | en:screenshots:vpsadmin:notifications:example-webhook-route.png | `b8a0c8e217fcad6d7e3019200e30ad016c248e3a1229715e8f3139583db7b247` |
| en | `notifications/example-webhook-result` | en:screenshots:vpsadmin:notifications:example-webhook-result.png | `20a159b73c1a677e9c7bdb70d6686274cf6a0b9708712582302ef13896030815` |
| cs | `notifications/grouping-route` | cs:screenshots:vpsadmin:notifications:grouping-route.png | `8fd5a77b21ef9729b801cc832b15316c952241d04a8413fa74e1278a72c7e239` |
| en | `notifications/grouping-route` | en:screenshots:vpsadmin:notifications:grouping-route.png | `3ff3641f1374770ceb6f8e14dbee2d0adc6841e5d089fa92566c84a841636134` |
