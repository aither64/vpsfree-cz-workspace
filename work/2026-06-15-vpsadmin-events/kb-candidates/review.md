# KB navigation annotation review

Changed pages: 16
New pages: 14
Selected media: 52
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
| cs | navody:notifikace | `a77d94b107dec79a54b34160d9c8269f1fb995d224c00f2314daa09e4914bda0` |
| cs | navody:notifikace:role_udalosti | `fb7de2a0ec83c69e18c0ba4d9be2b0f91aeb3d90e23d9456d8093de322cda970` |
| cs | navody:notifikace:ztlumeni_oom | `d3d0da77decfd2216d1dc8347458737e0fd78c4e3eda258d7ad511093225d4a0` |
| cs | navody:notifikace:ztlumeni_incidentu | `8ce7441926b08019d82f287615e3a56219c27182cf1f7c24d1500e757c3c5411` |
| cs | navody:notifikace:telegram | `ab211390bd5bf44eb262bd26900d5cab9211c138e78ee933ed108430a625e4c8` |
| cs | navody:notifikace:sms | `855837540a58589b5ceae0240c49d4ddfd895bde1a9b0ab2976fb36aa6949a39` |
| cs | navody:notifikace:webhook | `9b345d1b41f0d34743f20741565b8d8fab4d0c5d85398a3c8403d7c7da33b203` |
| en | manuals:notifications | `3d2d6a11ace2a4f13e8752eca9eac60fc137aab9496d1c300ce7f8c76ce4e398` |
| en | manuals:notifications:event_roles | `9cce327588d1d9826b03a1a4e3880f968e2c6f2c99b8bb35d4eebc88192cf5cd` |
| en | manuals:notifications:mute_oom | `bca481667aef5d7e63f726595f21f885ebf3144504285516973ad3336a1d806e` |
| en | manuals:notifications:mute_incidents | `4c8eaed348894294eff930eb9aa8ec083ff22be4ef427cb5a79f7b46d4680881` |
| en | manuals:notifications:telegram | `311307aca7a88e69f8237c30ffb00dfbedad652e0e26ee5bbe5b2c9ee146b462` |
| en | manuals:notifications:sms | `062dd8c3427ac85beec386721231f2a76a349f3b2689471137508749e4f2da56` |
| en | manuals:notifications:webhook | `5c781d2cd72a92ab8ba70638f307def65f90241dfce740460e4723db863952a3` |

## Selected capture media

| Language | Capture | Media ID | SHA-256 |
| --- | --- | --- | --- |
| cs | `notifications/receiver` | cs:screenshots:vpsadmin:notifications:receiver.png | `7161a9b1f6c08a3f6a1a327e2fd1bbfa32b2254c1b12534b38b4e9e27acf21ce` |
| cs | `notifications/time-interval` | cs:screenshots:vpsadmin:notifications:time-interval.png | `82277ac2c5ef3cb1ce8e2fad7165ab75e7c38c096f73d6460160d8f015c8e558` |
| cs | `notifications/route-time-intervals` | cs:screenshots:vpsadmin:notifications:route-time-intervals.png | `389ef724e324677442b7edebeabf84bac31e929369806d4de217862a2284ff13` |
| cs | `notifications/event-suppressed` | cs:screenshots:vpsadmin:notifications:event-suppressed.png | `1eaad29e7690e50d4320ee804d37e44dc31131d362ad9b80892183b67888a707` |
| cs | `notifications/example-role-receiver` | cs:screenshots:vpsadmin:notifications:example-role-receiver.png | `199793e51baac91f8b950be9803cf284a035552f2d7f818b65b189cf347a48a5` |
| cs | `notifications/example-role-routing` | cs:screenshots:vpsadmin:notifications:example-role-routing.png | `1b50b9a1d05a6f44e0cd5d76873761358695f4edbe40ce7acb9c8e56bb4f7d61` |
| cs | `notifications/example-role-admin-route` | cs:screenshots:vpsadmin:notifications:example-role-admin-route.png | `9e8fe7a083458411e6cbb417ce7624923d0a73279d128f35c928f3ef8aaec188` |
| cs | `notifications/example-role-result` | cs:screenshots:vpsadmin:notifications:example-role-result.png | `fc153dc469993fcdd4de93f9a9ae3a54cab38eb6e1a27c5cee17b1d2553d4571` |
| cs | `notifications/example-mute-oom` | cs:screenshots:vpsadmin:notifications:example-mute-oom.png | `063d7162e66062f8c699106f74718275e41318da73e3f00d9cef65e674fb2c17` |
| cs | `notifications/example-mute-incident-route` | cs:screenshots:vpsadmin:notifications:example-mute-incident-route.png | `b32728ffc697e2d9209e7214990014dcd61c9c52192851ca59d89111bf789f18` |
| cs | `notifications/example-mute-result` | cs:screenshots:vpsadmin:notifications:example-mute-result.png | `487dc94659f4961e0284edc8dec50342a0b45382892332dc816a0353b4e0e7e2` |
| cs | `notifications/example-telegram-target` | cs:screenshots:vpsadmin:notifications:example-telegram-target.png | `b79d292785cf213275fcddc8ae1ce1749f743b731f7ef1a34085a892fcde92bb` |
| cs | `notifications/example-telegram` | cs:screenshots:vpsadmin:notifications:example-telegram.png | `43bbb3dd4cd01238408eae58058f7ad1e945f616c4187287ac10fd543680b14c` |
| cs | `notifications/example-telegram-monitoring-route` | cs:screenshots:vpsadmin:notifications:example-telegram-monitoring-route.png | `b68f3e681cbfb43d60bd538c1aec8c3fbd7d5175ee380a5835da5edb207b4309` |
| cs | `notifications/example-telegram-incident-route` | cs:screenshots:vpsadmin:notifications:example-telegram-incident-route.png | `a3c093f271e2e544f8e7f9e0aebd3c95eb9f58a4550daa68ccb0d3768d32bbb8` |
| cs | `notifications/example-telegram-result` | cs:screenshots:vpsadmin:notifications:example-telegram-result.png | `409867a521dc4cbc65019387d0ef7413b6e916c250a9d4afeedfda830edf0b30` |
| cs | `notifications/example-sms-verification` | cs:screenshots:vpsadmin:notifications:example-sms-verification.png | `65d1000c22d503cecc2f7ff9cd0edad54225381831869f7137020731ba3ef238` |
| cs | `notifications/example-sms` | cs:screenshots:vpsadmin:notifications:example-sms.png | `bf6b307039367d90feb5d771595142a81a1219ed67ab37e486149cd460f1039e` |
| cs | `notifications/example-sms-account-route` | cs:screenshots:vpsadmin:notifications:example-sms-account-route.png | `61a4a79a6b16357ba5766f7683d7ff46ef466cedfd796bea9e56ca24cdeeae53` |
| cs | `notifications/example-sms-vps-route` | cs:screenshots:vpsadmin:notifications:example-sms-vps-route.png | `9f1958f8a099f9b12fe40906960250ebbc74cf464f8682cfd358a73ed3885d14` |
| cs | `notifications/example-sms-result` | cs:screenshots:vpsadmin:notifications:example-sms-result.png | `bdfdb0bf16b1bcbad1221f46e93da1fecf9e4f9006aca66bfc29168bd3ab5d3e` |
| cs | `notifications/example-webhook-target` | cs:screenshots:vpsadmin:notifications:example-webhook-target.png | `4596ae8d32a0a4e8e6a5a381034130607b62be24361581e3edd6966992b272ac` |
| cs | `notifications/example-webhook` | cs:screenshots:vpsadmin:notifications:example-webhook.png | `cb9f9fbb752087371b89bb3037722f6ca0857f16beca8ba043a8f55a5ffc2fc4` |
| cs | `notifications/example-webhook-route` | cs:screenshots:vpsadmin:notifications:example-webhook-route.png | `85f18dd0c5457811e5b5b11e581bb1db6b21e7eabf6875bff811924656f8e248` |
| cs | `notifications/example-webhook-result` | cs:screenshots:vpsadmin:notifications:example-webhook-result.png | `9397ad6e9a80a566247634bfda5a618db31aa3c28b2af1c35a5357f411442904` |
| en | `notifications/receiver` | en:screenshots:vpsadmin:notifications:receiver.png | `9909b554a00c7efab9c996f84c02e5f772b278e3df03adbea49a5859bb1772aa` |
| en | `notifications/time-interval` | en:screenshots:vpsadmin:notifications:time-interval.png | `57b09b3a779a5e96ed10f2d156484b04cd1b86455a9242b9b3c47c23f1082a20` |
| en | `notifications/route-time-intervals` | en:screenshots:vpsadmin:notifications:route-time-intervals.png | `5fa2f42f7ae29ac4a9afba48bd627fd86e3a13a697a190c1525c59374bceec1b` |
| en | `notifications/event-suppressed` | en:screenshots:vpsadmin:notifications:event-suppressed.png | `d7d671b6e2eb52b17223c6400b3124c47c97443f56f1ab622bdb71440aaa61f1` |
| en | `notifications/example-role-receiver` | en:screenshots:vpsadmin:notifications:example-role-receiver.png | `7d86ca1acbd4fc99e92ccc9cf9b0ce13d631263051446cd38c9111b3243d5ed4` |
| en | `notifications/example-role-routing` | en:screenshots:vpsadmin:notifications:example-role-routing.png | `7c61a30563096235bd3ad0550c7448a1e8c80990d00bb9cfb5776a87e1d584f3` |
| en | `notifications/example-role-admin-route` | en:screenshots:vpsadmin:notifications:example-role-admin-route.png | `bc3b20f0f313f6979c40665ba1bf5580662ce1979ca8e1f7c2c5813f2b68bb5d` |
| en | `notifications/example-role-result` | en:screenshots:vpsadmin:notifications:example-role-result.png | `9fb732cd6a365f43ac955edc7701aefc20c1c235d32ba067bcfde1c785169b9e` |
| en | `notifications/example-mute-oom` | en:screenshots:vpsadmin:notifications:example-mute-oom.png | `ef344dfded6ff4b2f2cc5afe229cd504f5acf7f6630d42fd0bdf0da6e7bf8dee` |
| en | `notifications/example-mute-incident-route` | en:screenshots:vpsadmin:notifications:example-mute-incident-route.png | `53baf084613888b042007e7be4a09c883c965eb74c238c82c2a76da654903a41` |
| en | `notifications/example-mute-result` | en:screenshots:vpsadmin:notifications:example-mute-result.png | `933679a955b0fb562e4284ef828928f97194aa1aca5a6adf2ad153fe5dba49bc` |
| en | `notifications/example-telegram-target` | en:screenshots:vpsadmin:notifications:example-telegram-target.png | `b4613f4dd024dbc0cb0f1e6ffda1b8739bd6e3c64a78ec74101bef623b919f73` |
| en | `notifications/example-telegram` | en:screenshots:vpsadmin:notifications:example-telegram.png | `a417fdb482b6a83c11b6b10eb7eabde3eb7b8077b5ffc8c34bb29c4beb3bca8d` |
| en | `notifications/example-telegram-monitoring-route` | en:screenshots:vpsadmin:notifications:example-telegram-monitoring-route.png | `fa37689ffc18690213fd22bc4468d575e496c8980e7d79bc76c50b16b5f2ac8e` |
| en | `notifications/example-telegram-incident-route` | en:screenshots:vpsadmin:notifications:example-telegram-incident-route.png | `e29ff0d62d55c901399700dcfd1909bfe26bbbcc0c6e009494d73dea0609a563` |
| en | `notifications/example-telegram-result` | en:screenshots:vpsadmin:notifications:example-telegram-result.png | `2018bb8dd2062124b5fba8fee14f0238ef0a3732a0b59c6e10c6ad12e6040179` |
| en | `notifications/example-sms-verification` | en:screenshots:vpsadmin:notifications:example-sms-verification.png | `67a101798f3083dca3683b89ccc5726401bfbd69c9eae782aedc52e137836ca6` |
| en | `notifications/example-sms` | en:screenshots:vpsadmin:notifications:example-sms.png | `f4f90bf2b3e4d237725a646228f80b46e7846faab1ed6d08daf44862dd96dc09` |
| en | `notifications/example-sms-account-route` | en:screenshots:vpsadmin:notifications:example-sms-account-route.png | `27122b01eccb06c9601d332d11c26b050b816b619f752da5307119b28ba3c48a` |
| en | `notifications/example-sms-vps-route` | en:screenshots:vpsadmin:notifications:example-sms-vps-route.png | `04dcc061c74f3cf9f0e223f65762bfbb200e8e731c87f02a4e35aa704dcf4c35` |
| en | `notifications/example-sms-result` | en:screenshots:vpsadmin:notifications:example-sms-result.png | `f6abd41fd87846da62686422e9a51421ecbcc47ec46b5df4fa4d80f8e8407b9c` |
| en | `notifications/example-webhook-target` | en:screenshots:vpsadmin:notifications:example-webhook-target.png | `0f6e0cb39bb30f2f36aac411b220124a440ee01f4a55bebf4bf1cb91a29e127c` |
| en | `notifications/example-webhook` | en:screenshots:vpsadmin:notifications:example-webhook.png | `711feffe549a7cfa1d3051055035addfb6a02db86226832022919a781764329c` |
| en | `notifications/example-webhook-route` | en:screenshots:vpsadmin:notifications:example-webhook-route.png | `5d188a9e5335db67bd41509720e27d1a3370025c639e235e2962af222b86246a` |
| en | `notifications/example-webhook-result` | en:screenshots:vpsadmin:notifications:example-webhook-result.png | `20a159b73c1a677e9c7bdb70d6686274cf6a0b9708712582302ef13896030815` |
| cs | `notifications/grouping-route` | cs:screenshots:vpsadmin:notifications:grouping-route.png | `8fd5a77b21ef9729b801cc832b15316c952241d04a8413fa74e1278a72c7e239` |
| en | `notifications/grouping-route` | en:screenshots:vpsadmin:notifications:grouping-route.png | `3ff3641f1374770ceb6f8e14dbee2d0adc6841e5d089fa92566c84a841636134` |
