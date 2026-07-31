# KB navigation annotation review

Changed pages: 22
New pages: 20
Selected media: 62
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
| cs | navody:notifikace | `b8513345da3cd6c9b140b1bff06cb565163e41496529c92a842e51de574af846` |
| cs | navody:notifikace:udalosti | `2685a9135202ba8b3afb9ca9aa83cda9007444970d6cc73bde01c12f0dec356f` |
| cs | navody:notifikace:routovani | `1dc493bc7f880e805ba1824cd920ab29e904296c1ed41bd8c25accd1a9fd03d9` |
| cs | navody:notifikace:cile_a_prijemci | `3d879a6acc020a073032fe8cf6981672e1ac8fb648f38f121dddf513e1bca7be` |
| cs | navody:notifikace:role_udalosti | `56fdd2403c57be966522b058c9d279709d358ae55f427b6c33be19e2e16745ed` |
| cs | navody:notifikace:ztlumeni_oom | `39f7e5e3c6c5b8702bcfa4fbdacb628f7b8c7b584ec57026f7c5f136c4ecfa8f` |
| cs | navody:notifikace:ztlumeni_incidentu | `975cfb1c80658d3af5fa270229c0108ca09937da0001919f46c6548a283b5ad2` |
| cs | navody:notifikace:telegram | `b2dfc065adf1a7ef4a62e1b983c2fb72d51e56d295c0857f90c1bf8f83e3019b` |
| cs | navody:notifikace:sms | `608746992bb9ac555c39cf05baf42c7e950d472a7ec20839cb49d0573eb6a7e6` |
| cs | navody:notifikace:webhook | `061299a1cc90165bc17adc86eb455580fb0daf9d5463eeea9085f331e9ad3d61` |
| en | manuals:notifications | `ae045656d5a58a3efc14eeaf2bfd9774ea3a22ff3584f71e6672f7afccc73217` |
| en | manuals:notifications:events | `855db5123efc7d0fd3bfccd2968afff3111bbfd9a6c0daf34874d222fdad5ab4` |
| en | manuals:notifications:routing | `f2a408a761793cd0e577a43ffde994e16870f91bff4801117aa02d79ad2310b8` |
| en | manuals:notifications:targets_and_receivers | `c647921d55ac914e0b9e0fc8f27d334a5741a892f8e9eaf8ce089f9806fcaf3b` |
| en | manuals:notifications:event_roles | `b9a9d6c620d27a7a5ab8f8907d24b068d5faf78f2433e9e00ef2af6deb71bcd2` |
| en | manuals:notifications:mute_oom | `1b96a45a00b82fd22379bf9b1a43271f3ad3bd623bf461da3c7082512d33e44c` |
| en | manuals:notifications:mute_incidents | `4c17825ddf31f94b92c582d58336a59e7bf6d075e27c7a402cf410624cab61b8` |
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
| cs | `notifications/routes` | cs:screenshots:vpsadmin:notifications:routes.png | `ebb86528e64a5fc043e34ad16ff6721ae93019621ed9f66a40ebeddfe14477f7` |
| cs | `notifications/event-types` | cs:screenshots:vpsadmin:notifications:event-types.png | `9c14f9a0dd378a9c26934a946c9bf9a3cf4e6b23c76b1cee735acc9c28ae5ac7` |
| cs | `notifications/event-type-vps-oom-report` | cs:screenshots:vpsadmin:notifications:event-type-vps-oom-report.png | `a25bca148a5ba815d8fd9820517acf994f895d1a9d38c7b995e0afab523d98a4` |
| cs | `notifications/matcher-form` | cs:screenshots:vpsadmin:notifications:matcher-form.png | `eb95f1a8dd79f8cb914ff300796cbb27b476175ec5905e58f1768bee5f828b19` |
| cs | `notifications/targets` | cs:screenshots:vpsadmin:notifications:targets.png | `6671e90b8ffe676bb752a51079b46fd023c01995ab659ed72a92f69305d386db` |
| cs | `notifications/receiver` | cs:screenshots:vpsadmin:notifications:receiver.png | `70eb123986ce4c488e8f262d8a9ef372474eb72b228b15d9dabd74b3878f0d59` |
| cs | `notifications/time-interval` | cs:screenshots:vpsadmin:notifications:time-interval.png | `ce74f8496357928381d400a25cac7fb714661919dc34b77092babcf6f59c4d56` |
| cs | `notifications/route-time-intervals` | cs:screenshots:vpsadmin:notifications:route-time-intervals.png | `79db6978c11a432d40d9b302e49ae9450b2b029de8e295c3874ca35901fa8250` |
| cs | `notifications/example-role-receiver` | cs:screenshots:vpsadmin:notifications:example-role-receiver.png | `2aa9017cf93ebdd611641f6a9f5f8d1cd56b96a4fc739334673f87e6bf387a77` |
| cs | `notifications/example-role-routing` | cs:screenshots:vpsadmin:notifications:example-role-routing.png | `2c3dd6693425fd9d66b54d03e9a71465d06208a19de4465e85679665bd53e11e` |
| cs | `notifications/example-role-admin-route` | cs:screenshots:vpsadmin:notifications:example-role-admin-route.png | `7284e3cd41eddf38adf9b1454aca5461add415480936b6ad5d483c8b2427e81a` |
| cs | `notifications/example-role-result` | cs:screenshots:vpsadmin:notifications:example-role-result.png | `fc153dc469993fcdd4de93f9a9ae3a54cab38eb6e1a27c5cee17b1d2553d4571` |
| cs | `notifications/example-mute-oom` | cs:screenshots:vpsadmin:notifications:example-mute-oom.png | `09d8035214fe65285a01a6dfcc503494e82301d92d77d186dd3f393ed7c143d1` |
| cs | `notifications/mute-oom-composer` | cs:screenshots:vpsadmin:notifications:mute-oom-composer.png | `2506f5078a51398b2e73d316584ff4400a779bb001ab25f0fe233894631a6acb` |
| cs | `notifications/example-mute-incident-route` | cs:screenshots:vpsadmin:notifications:example-mute-incident-route.png | `3beeb351929c3df92578a5593b66baa89577738eea9a79a6155872a5401e8f0d` |
| cs | `notifications/mute-incident-composer` | cs:screenshots:vpsadmin:notifications:mute-incident-composer.png | `9de73ffc61436e27364d34001fe3e3f311b9a3114a0ce1a1eeeca580dc9a9da1` |
| cs | `notifications/example-telegram-target` | cs:screenshots:vpsadmin:notifications:example-telegram-target.png | `b79d292785cf213275fcddc8ae1ce1749f743b731f7ef1a34085a892fcde92bb` |
| cs | `notifications/example-telegram` | cs:screenshots:vpsadmin:notifications:example-telegram.png | `17ffb6a4dbb6a927bac77b08652b4f839465676f0979bb021c1a6a865eb222f6` |
| cs | `notifications/example-telegram-monitoring-route` | cs:screenshots:vpsadmin:notifications:example-telegram-monitoring-route.png | `bd3ce3f13ff164c8e1832a3e2fab2d63582c3fe1c595c9b1210729b563368196` |
| cs | `notifications/example-telegram-incident-route` | cs:screenshots:vpsadmin:notifications:example-telegram-incident-route.png | `290c9e4f135488e7ef3f6ab843e82ec5574ab6a39bb9c14918254354e5bc3cd4` |
| cs | `notifications/example-telegram-result` | cs:screenshots:vpsadmin:notifications:example-telegram-result.png | `409867a521dc4cbc65019387d0ef7413b6e916c250a9d4afeedfda830edf0b30` |
| cs | `notifications/example-sms-verification` | cs:screenshots:vpsadmin:notifications:example-sms-verification.png | `65d1000c22d503cecc2f7ff9cd0edad54225381831869f7137020731ba3ef238` |
| cs | `notifications/example-sms` | cs:screenshots:vpsadmin:notifications:example-sms.png | `2e68a0190e7ef04310186fb77536f2d6fcff23e90c41ebc88134408304e61666` |
| cs | `notifications/example-sms-account-route` | cs:screenshots:vpsadmin:notifications:example-sms-account-route.png | `d82c65efe4a213ad747d6ea41b99cbbc934ef40be69f225238b29bf2afec3dcc` |
| cs | `notifications/example-sms-vps-route` | cs:screenshots:vpsadmin:notifications:example-sms-vps-route.png | `1a505b8fa84ac9728de026064b909cafe39a14e706a775878685fa2a67ad2076` |
| cs | `notifications/example-sms-result` | cs:screenshots:vpsadmin:notifications:example-sms-result.png | `bdfdb0bf16b1bcbad1221f46e93da1fecf9e4f9006aca66bfc29168bd3ab5d3e` |
| cs | `notifications/example-webhook-target` | cs:screenshots:vpsadmin:notifications:example-webhook-target.png | `4596ae8d32a0a4e8e6a5a381034130607b62be24361581e3edd6966992b272ac` |
| cs | `notifications/example-webhook` | cs:screenshots:vpsadmin:notifications:example-webhook.png | `4d8ceee179a710a095df9c3bef268fd685af5163c74b621655587e082913fdab` |
| cs | `notifications/example-webhook-route` | cs:screenshots:vpsadmin:notifications:example-webhook-route.png | `17405191482ed3e2639c4c8588585dc1625e84b3404bfff3f65b671dc1171b1c` |
| cs | `notifications/example-webhook-result` | cs:screenshots:vpsadmin:notifications:example-webhook-result.png | `9397ad6e9a80a566247634bfda5a618db31aa3c28b2af1c35a5357f411442904` |
| en | `notifications/routes` | en:screenshots:vpsadmin:notifications:routes.png | `122f6b8cc519be5644e5304df471632333c4c608ddd73d7510c19f62ed79b960` |
| en | `notifications/event-types` | en:screenshots:vpsadmin:notifications:event-types.png | `fc2ddbe5f02b9538517b5d31aa03fd4c3b19b118b33c24a8d17076d54d540174` |
| en | `notifications/event-type-vps-oom-report` | en:screenshots:vpsadmin:notifications:event-type-vps-oom-report.png | `90fc3e195da847963b7b114c33d7fe2a4a96b932c1bf7ca6189e27e76099cebb` |
| en | `notifications/matcher-form` | en:screenshots:vpsadmin:notifications:matcher-form.png | `ce7e6d08ff685d7c903b9a71f14d46c25f4d6cb827c10b562e65fba1cba289bf` |
| en | `notifications/targets` | en:screenshots:vpsadmin:notifications:targets.png | `27da32369d7bf499953147b71c79457382c08bc19334431cb477a12ed37ed7b4` |
| en | `notifications/receiver` | en:screenshots:vpsadmin:notifications:receiver.png | `17d96c17b37e2b76a6a805dc6c0dc60408ef95cbd0dbc7acaaaaddee540c5bba` |
| en | `notifications/time-interval` | en:screenshots:vpsadmin:notifications:time-interval.png | `e15c5dd7ff9527fbb02afc0cee61d6f58b614eb746a18106b6873a2fcdf2b7c1` |
| en | `notifications/route-time-intervals` | en:screenshots:vpsadmin:notifications:route-time-intervals.png | `f847322e670abbacd3929f443350dd47a8cff86ded3656416748316dff42d3dd` |
| en | `notifications/example-role-receiver` | en:screenshots:vpsadmin:notifications:example-role-receiver.png | `948dacd61e2c319c01246706ae0e29895b97bfba42d7b9b3660ae265eff7f382` |
| en | `notifications/example-role-routing` | en:screenshots:vpsadmin:notifications:example-role-routing.png | `ea85bfab975ab835f549712edc38d40987807704bd0bd0d13a977a3d46c9a87c` |
| en | `notifications/example-role-admin-route` | en:screenshots:vpsadmin:notifications:example-role-admin-route.png | `82a5d729e8ecef15e2ce4683cd5a8820448a5fedfe8a6be3c6982ac965a580cf` |
| en | `notifications/example-role-result` | en:screenshots:vpsadmin:notifications:example-role-result.png | `9fb732cd6a365f43ac955edc7701aefc20c1c235d32ba067bcfde1c785169b9e` |
| en | `notifications/example-mute-oom` | en:screenshots:vpsadmin:notifications:example-mute-oom.png | `d5d75854c53cb6f6c6647a779869b52fabe7bfe937faa1a216cddf1937a9000f` |
| en | `notifications/mute-oom-composer` | en:screenshots:vpsadmin:notifications:mute-oom-composer.png | `e37baf2be0bf7314fa798ba82dc797618bfed7ea011d8b96a0434be2e9d43728` |
| en | `notifications/example-mute-incident-route` | en:screenshots:vpsadmin:notifications:example-mute-incident-route.png | `1e6d60343ef27cba3e6a625026ca496e5d32907f8de845ba51ece558215413b0` |
| en | `notifications/mute-incident-composer` | en:screenshots:vpsadmin:notifications:mute-incident-composer.png | `2f27c8f18e4d6333c35840c86e35a72746e5058bacd8345275bf4d544a267ac3` |
| en | `notifications/example-telegram-target` | en:screenshots:vpsadmin:notifications:example-telegram-target.png | `b4613f4dd024dbc0cb0f1e6ffda1b8739bd6e3c64a78ec74101bef623b919f73` |
| en | `notifications/example-telegram` | en:screenshots:vpsadmin:notifications:example-telegram.png | `8d14c7d38d32bb5ab08774cfe3ab868567c436279129c0bfd497265bb6336d85` |
| en | `notifications/example-telegram-monitoring-route` | en:screenshots:vpsadmin:notifications:example-telegram-monitoring-route.png | `28c23cda53158c7d064c56f2410a3413383ff667db2830c17ebcd11fed37e4d3` |
| en | `notifications/example-telegram-incident-route` | en:screenshots:vpsadmin:notifications:example-telegram-incident-route.png | `3067868581f2a2161731b89ebea58f0bdc7268afb6f0bb561929f14f26b73824` |
| en | `notifications/example-telegram-result` | en:screenshots:vpsadmin:notifications:example-telegram-result.png | `2018bb8dd2062124b5fba8fee14f0238ef0a3732a0b59c6e10c6ad12e6040179` |
| en | `notifications/example-sms-verification` | en:screenshots:vpsadmin:notifications:example-sms-verification.png | `67a101798f3083dca3683b89ccc5726401bfbd69c9eae782aedc52e137836ca6` |
| en | `notifications/example-sms` | en:screenshots:vpsadmin:notifications:example-sms.png | `4372bd01843b2b85efcf1392d47ab7243c5a95988aa2518f0c4d29c787fb3e08` |
| en | `notifications/example-sms-account-route` | en:screenshots:vpsadmin:notifications:example-sms-account-route.png | `94393519575157822f9474059a9ab6dd40525bfa56d9c35c73d2c2fba2db173b` |
| en | `notifications/example-sms-vps-route` | en:screenshots:vpsadmin:notifications:example-sms-vps-route.png | `5e200fd7c6a705051e9d3c42361b8d130bc9afe77b2fe45ad63e6826f011e06b` |
| en | `notifications/example-sms-result` | en:screenshots:vpsadmin:notifications:example-sms-result.png | `f6abd41fd87846da62686422e9a51421ecbcc47ec46b5df4fa4d80f8e8407b9c` |
| en | `notifications/example-webhook-target` | en:screenshots:vpsadmin:notifications:example-webhook-target.png | `0f6e0cb39bb30f2f36aac411b220124a440ee01f4a55bebf4bf1cb91a29e127c` |
| en | `notifications/example-webhook` | en:screenshots:vpsadmin:notifications:example-webhook.png | `a544b0313296120ba9301010150b00142af97e3b264741ccc581b43c9411d0d2` |
| en | `notifications/example-webhook-route` | en:screenshots:vpsadmin:notifications:example-webhook-route.png | `d9ad6634f7a3f17c5a8ce27f2fc43109ccc6906fccc031581281efd2fd1e662e` |
| en | `notifications/example-webhook-result` | en:screenshots:vpsadmin:notifications:example-webhook-result.png | `20a159b73c1a677e9c7bdb70d6686274cf6a0b9708712582302ef13896030815` |
| cs | `notifications/grouping-route` | cs:screenshots:vpsadmin:notifications:grouping-route.png | `e2e3bb33fbcd10794a24a751294a39491624f3e481b541957d5aebe9b6902960` |
| en | `notifications/grouping-route` | en:screenshots:vpsadmin:notifications:grouping-route.png | `c108d2f3419533ba325917323849d1b99f61dbb7c8c74bd4795c56558bcd39a1` |
