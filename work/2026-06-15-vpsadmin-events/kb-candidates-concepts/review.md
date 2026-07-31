# KB navigation annotation review

Changed pages: 22
New pages: 20
Selected media: 58
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
| cs | navody:notifikace | `83283d0fe4417ee898072386dd7d3c40c374bc607004f7ad250621a5cd164e13` |
| cs | navody:notifikace:udalosti | `2685a9135202ba8b3afb9ca9aa83cda9007444970d6cc73bde01c12f0dec356f` |
| cs | navody:notifikace:routovani | `62621854fe2937ecf77e4d0dc1ff1b4602f81215cf808ee0f1e7f502aae18080` |
| cs | navody:notifikace:cile_a_prijemci | `3d879a6acc020a073032fe8cf6981672e1ac8fb648f38f121dddf513e1bca7be` |
| cs | navody:notifikace:role_udalosti | `56fdd2403c57be966522b058c9d279709d358ae55f427b6c33be19e2e16745ed` |
| cs | navody:notifikace:ztlumeni_oom | `4d07d5b82c922c71317b4da306d358fc72ec9517810701a50e55622a5359d19e` |
| cs | navody:notifikace:ztlumeni_incidentu | `71474d071d721f5d8fb7f956d6f7798324e87f4524ccbab33ae2f89bc46807d4` |
| cs | navody:notifikace:telegram | `b2dfc065adf1a7ef4a62e1b983c2fb72d51e56d295c0857f90c1bf8f83e3019b` |
| cs | navody:notifikace:sms | `608746992bb9ac555c39cf05baf42c7e950d472a7ec20839cb49d0573eb6a7e6` |
| cs | navody:notifikace:webhook | `061299a1cc90165bc17adc86eb455580fb0daf9d5463eeea9085f331e9ad3d61` |
| en | manuals:notifications | `8a2e5257a7087a336719f87939d461f304fa71c8b211aa6be6dce9f407f3f753` |
| en | manuals:notifications:events | `855db5123efc7d0fd3bfccd2968afff3111bbfd9a6c0daf34874d222fdad5ab4` |
| en | manuals:notifications:routing | `9551114113e429b5dada54194f793eea168c8353b1a5b4f1fd4d3e07194272c6` |
| en | manuals:notifications:targets_and_receivers | `c647921d55ac914e0b9e0fc8f27d334a5741a892f8e9eaf8ce089f9806fcaf3b` |
| en | manuals:notifications:event_roles | `b9a9d6c620d27a7a5ab8f8907d24b068d5faf78f2433e9e00ef2af6deb71bcd2` |
| en | manuals:notifications:mute_oom | `81c444bbd1b90b216cb03d8a51bd036e77018ebffc88ee1ec9cee52d0c015184` |
| en | manuals:notifications:mute_incidents | `24503da2de341bfb5976f867e0c53c34994ad218c4a392f5b17d60aec4c4778b` |
| en | manuals:notifications:telegram | `18e9bb3b7fe0ca4d9a4bf623b237676bf3901c6d3d8760c8447b4cf5d3eacbd9` |
| en | manuals:notifications:sms | `1200bb40ef7c4d9f4170170ff623f36264242e3b7d043da0ca41a47caffbc55c` |
| en | manuals:notifications:webhook | `5e675c62f792d0d16ef2ecba6fd6e7477cbe5015b66646458040f2b167a8d885` |

## Canonical code samples

| ID | File | Language | Uses | SHA-256 |
| --- | --- | --- | ---: | --- |
| `notifications.webhook-server` | doc/examples/notifications/webhook_server.py | python | 2 | `82572c438f5ded1389d65c6f0896c86f0eb9b221d1f08a7795151d10b9b05274` |
| `notifications.webhook-single-payload` | doc/examples/notifications/webhook_single.json | json | 2 | `3ecced6bfbdbdc0d3669f646008dbd0909e2024676707d817c1691ea91dbbc97` |

## Selected capture media

| Language | Capture | Media ID | SHA-256 |
| --- | --- | --- | --- |
| cs | `notifications/routes` | cs:screenshots:vpsadmin:notifications:routes.png | `ec408459f4d3b1a9271e06f5312a5b81ce5d93e2282ddb52a43d185d71ff540e` |
| cs | `notifications/event-types` | cs:screenshots:vpsadmin:notifications:event-types.png | `9c14f9a0dd378a9c26934a946c9bf9a3cf4e6b23c76b1cee735acc9c28ae5ac7` |
| cs | `notifications/event-type-vps-oom-report` | cs:screenshots:vpsadmin:notifications:event-type-vps-oom-report.png | `f2b2a22af650dc7d398e4c124217d59df037e64c5aa98cd8611d7b50c7bbcad1` |
| cs | `notifications/matcher-form` | cs:screenshots:vpsadmin:notifications:matcher-form.png | `eb95f1a8dd79f8cb914ff300796cbb27b476175ec5905e58f1768bee5f828b19` |
| cs | `notifications/targets` | cs:screenshots:vpsadmin:notifications:targets.png | `6671e90b8ffe676bb752a51079b46fd023c01995ab659ed72a92f69305d386db` |
| cs | `notifications/receiver` | cs:screenshots:vpsadmin:notifications:receiver.png | `70eb123986ce4c488e8f262d8a9ef372474eb72b228b15d9dabd74b3878f0d59` |
| cs | `notifications/time-interval` | cs:screenshots:vpsadmin:notifications:time-interval.png | `ce74f8496357928381d400a25cac7fb714661919dc34b77092babcf6f59c4d56` |
| cs | `notifications/route-time-intervals` | cs:screenshots:vpsadmin:notifications:route-time-intervals.png | `389ef724e324677442b7edebeabf84bac31e929369806d4de217862a2284ff13` |
| cs | `notifications/example-role-receiver` | cs:screenshots:vpsadmin:notifications:example-role-receiver.png | `2aa9017cf93ebdd611641f6a9f5f8d1cd56b96a4fc739334673f87e6bf387a77` |
| cs | `notifications/example-role-routing` | cs:screenshots:vpsadmin:notifications:example-role-routing.png | `817dc1476580c3a5d58dbcd396fdc3c480f80beb53b25779e40660eeeb5a50d8` |
| cs | `notifications/example-role-admin-route` | cs:screenshots:vpsadmin:notifications:example-role-admin-route.png | `67d0c4ccda12bae36c647f36dd4980fbaeb676b47d0a269a73afcc63d25d9235` |
| cs | `notifications/example-role-result` | cs:screenshots:vpsadmin:notifications:example-role-result.png | `fc153dc469993fcdd4de93f9a9ae3a54cab38eb6e1a27c5cee17b1d2553d4571` |
| cs | `notifications/example-mute-oom` | cs:screenshots:vpsadmin:notifications:example-mute-oom.png | `b55000cff81f053aaa2203a9415d9a78b290ce8a60c4d2a7057390c8d0781d58` |
| cs | `notifications/example-mute-incident-route` | cs:screenshots:vpsadmin:notifications:example-mute-incident-route.png | `09cc0c816a9d811597fd711baf6c7f9a3eb1679f66f308e910d933e2bf3fa681` |
| cs | `notifications/example-telegram-target` | cs:screenshots:vpsadmin:notifications:example-telegram-target.png | `b79d292785cf213275fcddc8ae1ce1749f743b731f7ef1a34085a892fcde92bb` |
| cs | `notifications/example-telegram` | cs:screenshots:vpsadmin:notifications:example-telegram.png | `17ffb6a4dbb6a927bac77b08652b4f839465676f0979bb021c1a6a865eb222f6` |
| cs | `notifications/example-telegram-monitoring-route` | cs:screenshots:vpsadmin:notifications:example-telegram-monitoring-route.png | `671efc67f4e1af839aeb9cdf749cccedc7e25b603cf4e70476cf21830a8dfe1f` |
| cs | `notifications/example-telegram-incident-route` | cs:screenshots:vpsadmin:notifications:example-telegram-incident-route.png | `10c483660eaa9244c4443429abbf8bc82fe05c7da39f1a02d25a54c5ca7d41f8` |
| cs | `notifications/example-telegram-result` | cs:screenshots:vpsadmin:notifications:example-telegram-result.png | `409867a521dc4cbc65019387d0ef7413b6e916c250a9d4afeedfda830edf0b30` |
| cs | `notifications/example-sms-verification` | cs:screenshots:vpsadmin:notifications:example-sms-verification.png | `65d1000c22d503cecc2f7ff9cd0edad54225381831869f7137020731ba3ef238` |
| cs | `notifications/example-sms` | cs:screenshots:vpsadmin:notifications:example-sms.png | `2e68a0190e7ef04310186fb77536f2d6fcff23e90c41ebc88134408304e61666` |
| cs | `notifications/example-sms-account-route` | cs:screenshots:vpsadmin:notifications:example-sms-account-route.png | `1183730bbc3b085d94792ddc208b3808f321b11562554daca96106ae27be8f91` |
| cs | `notifications/example-sms-vps-route` | cs:screenshots:vpsadmin:notifications:example-sms-vps-route.png | `6f628f40322b39a3c7e94bfe7e6257c5e29fd443ad6c7f036d7ff65f78dcb26f` |
| cs | `notifications/example-sms-result` | cs:screenshots:vpsadmin:notifications:example-sms-result.png | `bdfdb0bf16b1bcbad1221f46e93da1fecf9e4f9006aca66bfc29168bd3ab5d3e` |
| cs | `notifications/example-webhook-target` | cs:screenshots:vpsadmin:notifications:example-webhook-target.png | `4596ae8d32a0a4e8e6a5a381034130607b62be24361581e3edd6966992b272ac` |
| cs | `notifications/example-webhook` | cs:screenshots:vpsadmin:notifications:example-webhook.png | `4d8ceee179a710a095df9c3bef268fd685af5163c74b621655587e082913fdab` |
| cs | `notifications/example-webhook-route` | cs:screenshots:vpsadmin:notifications:example-webhook-route.png | `3d427bd9344a858a6ccc4826307c644337c08354128bac5c271eeb1acbf4d80c` |
| cs | `notifications/example-webhook-result` | cs:screenshots:vpsadmin:notifications:example-webhook-result.png | `9397ad6e9a80a566247634bfda5a618db31aa3c28b2af1c35a5357f411442904` |
| en | `notifications/routes` | en:screenshots:vpsadmin:notifications:routes.png | `122f6b8cc519be5644e5304df471632333c4c608ddd73d7510c19f62ed79b960` |
| en | `notifications/event-types` | en:screenshots:vpsadmin:notifications:event-types.png | `fc2ddbe5f02b9538517b5d31aa03fd4c3b19b118b33c24a8d17076d54d540174` |
| en | `notifications/event-type-vps-oom-report` | en:screenshots:vpsadmin:notifications:event-type-vps-oom-report.png | `b940c866425da3f2d273429f217a74722662881a909e8c727e9763dd7c9d562c` |
| en | `notifications/matcher-form` | en:screenshots:vpsadmin:notifications:matcher-form.png | `ce7e6d08ff685d7c903b9a71f14d46c25f4d6cb827c10b562e65fba1cba289bf` |
| en | `notifications/targets` | en:screenshots:vpsadmin:notifications:targets.png | `27da32369d7bf499953147b71c79457382c08bc19334431cb477a12ed37ed7b4` |
| en | `notifications/receiver` | en:screenshots:vpsadmin:notifications:receiver.png | `17d96c17b37e2b76a6a805dc6c0dc60408ef95cbd0dbc7acaaaaddee540c5bba` |
| en | `notifications/time-interval` | en:screenshots:vpsadmin:notifications:time-interval.png | `e15c5dd7ff9527fbb02afc0cee61d6f58b614eb746a18106b6873a2fcdf2b7c1` |
| en | `notifications/route-time-intervals` | en:screenshots:vpsadmin:notifications:route-time-intervals.png | `5fa2f42f7ae29ac4a9afba48bd627fd86e3a13a697a190c1525c59374bceec1b` |
| en | `notifications/example-role-receiver` | en:screenshots:vpsadmin:notifications:example-role-receiver.png | `948dacd61e2c319c01246706ae0e29895b97bfba42d7b9b3660ae265eff7f382` |
| en | `notifications/example-role-routing` | en:screenshots:vpsadmin:notifications:example-role-routing.png | `9dc25bbfd05df7d9a18c7a754b3f4979bf79687624d38addea004c4b4fde1e70` |
| en | `notifications/example-role-admin-route` | en:screenshots:vpsadmin:notifications:example-role-admin-route.png | `e43a682960ea5ca4c85816c394d91e311313e0679c20dc74fa6ac78a09f0794d` |
| en | `notifications/example-role-result` | en:screenshots:vpsadmin:notifications:example-role-result.png | `9fb732cd6a365f43ac955edc7701aefc20c1c235d32ba067bcfde1c785169b9e` |
| en | `notifications/example-mute-oom` | en:screenshots:vpsadmin:notifications:example-mute-oom.png | `8df92c01f158ff61c43f334b7e98f55d6cf2d53a39f01508e751c4b657da9a67` |
| en | `notifications/example-mute-incident-route` | en:screenshots:vpsadmin:notifications:example-mute-incident-route.png | `876e5e7fe251810d7a7577622d964c218807cf16a28833ad372b85645c54feb5` |
| en | `notifications/example-telegram-target` | en:screenshots:vpsadmin:notifications:example-telegram-target.png | `b4613f4dd024dbc0cb0f1e6ffda1b8739bd6e3c64a78ec74101bef623b919f73` |
| en | `notifications/example-telegram` | en:screenshots:vpsadmin:notifications:example-telegram.png | `8d14c7d38d32bb5ab08774cfe3ab868567c436279129c0bfd497265bb6336d85` |
| en | `notifications/example-telegram-monitoring-route` | en:screenshots:vpsadmin:notifications:example-telegram-monitoring-route.png | `1a7f892cc78b1ce543af5f2a156003105cd578a3987a595087ff85e36bb3fa23` |
| en | `notifications/example-telegram-incident-route` | en:screenshots:vpsadmin:notifications:example-telegram-incident-route.png | `2bfd453a8d190c0235f015df1bb9fa529234b0fc7ea39805b80b7f09ad40d470` |
| en | `notifications/example-telegram-result` | en:screenshots:vpsadmin:notifications:example-telegram-result.png | `2018bb8dd2062124b5fba8fee14f0238ef0a3732a0b59c6e10c6ad12e6040179` |
| en | `notifications/example-sms-verification` | en:screenshots:vpsadmin:notifications:example-sms-verification.png | `67a101798f3083dca3683b89ccc5726401bfbd69c9eae782aedc52e137836ca6` |
| en | `notifications/example-sms` | en:screenshots:vpsadmin:notifications:example-sms.png | `4372bd01843b2b85efcf1392d47ab7243c5a95988aa2518f0c4d29c787fb3e08` |
| en | `notifications/example-sms-account-route` | en:screenshots:vpsadmin:notifications:example-sms-account-route.png | `e883bad56e665a58d3479b26bec393c8083e7ecf71e6dba9c576732149de77db` |
| en | `notifications/example-sms-vps-route` | en:screenshots:vpsadmin:notifications:example-sms-vps-route.png | `32218c3847c3b0ba0ee0de1878309528b25eba5e53a126cffc19982a3d065ee8` |
| en | `notifications/example-sms-result` | en:screenshots:vpsadmin:notifications:example-sms-result.png | `f6abd41fd87846da62686422e9a51421ecbcc47ec46b5df4fa4d80f8e8407b9c` |
| en | `notifications/example-webhook-target` | en:screenshots:vpsadmin:notifications:example-webhook-target.png | `0f6e0cb39bb30f2f36aac411b220124a440ee01f4a55bebf4bf1cb91a29e127c` |
| en | `notifications/example-webhook` | en:screenshots:vpsadmin:notifications:example-webhook.png | `a544b0313296120ba9301010150b00142af97e3b264741ccc581b43c9411d0d2` |
| en | `notifications/example-webhook-route` | en:screenshots:vpsadmin:notifications:example-webhook-route.png | `01253fe398264d514886543276125f2240df989805a9df2e1123e4c290ebdf42` |
| en | `notifications/example-webhook-result` | en:screenshots:vpsadmin:notifications:example-webhook-result.png | `20a159b73c1a677e9c7bdb70d6686274cf6a0b9708712582302ef13896030815` |
| cs | `notifications/grouping-route` | cs:screenshots:vpsadmin:notifications:grouping-route.png | `88282e6998a43948bd8006f74e9dd9c246faa5e0ce7ebdcf2fadc17d6e3e1882` |
| en | `notifications/grouping-route` | en:screenshots:vpsadmin:notifications:grouping-route.png | `0c90e9e62fbf78d8284df221af2d1768c78456907449f7047703e2472c11860e` |
