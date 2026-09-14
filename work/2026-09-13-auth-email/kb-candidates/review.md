# KB navigation annotation review

Changed pages: 4
New pages: 0
Selected media: 0
Annotation tags: 2
Content replacements: 4
Managed pages: 0

| Language | Page | Semantic path | Count | Existing text | Candidate text |
| --- | --- | --- | ---: | --- | --- |
| en | manuals:vps:users | `member.email-verification.open` | 1 | ===== Session control ===== | ===== Email verification for new devices ===== ↵ When TOTP or passkeys are not active, vpsAdmin can require an email code after ↵ the correct password on an unknown device. This setting is off by default. ↵ Enable **Verify new devices by email** in <vpsadmin-nav id="member.email-verification.open">**Edit profile** -> **Email verification**</vpsadmin-nav> and enter your current password. ↵  ↵ Verification starts after the account has logged in successfully from at ↵ least one device. Known devices can sign in as usual. Removing a device or ↵ letting its remembered login expire does not switch email verification off. ↵ Active TOTP or passkeys take precedence; the email preference remains saved. ↵  ↵ The code goes only to your primary email address. It expires 30 minutes ↵ after the initial request. Delivery may take a few minutes, so check your ↵ junk folder too. A replacement code invalidates the previous code without ↵ extending the deadline. You can request three codes per login, at least a ↵ minute apart. Five incorrect codes end that login attempt; further limits ↵ apply across attempts. ↵  ↵ Fresh password-based API token requests also require the code. HTTP Basic ↵ cannot be used while email verification is required. Existing tokens, ↵ sessions and single sign-on continue to work. For unattended clients, use ↵ an existing API token. If you cannot access your mailbox, use a known device ↵ or an existing session, or contact support. ↵  ↵ ===== Session control ===== ↵  |
| cs | navody:vps:uzivatele | `member.email-verification.open` | 1 | ===== Nastavení přihlášení ===== | ===== Ověřování nových zařízení e-mailem ===== ↵ Pokud nemáš aktivní TOTP ani přístupový klíč, může vpsAdmin při přihlášení ↵ z neznámého zařízení po zadání správného hesla vyžadovat také kód z e-mailu. ↵ Ve výchozím stavu je toto ověřování vypnuté. Zapni **Ověřovat nová zařízení e-mailem** v <vpsadmin-nav id="member.email-verification.open">**Upravit profil** -> **Ověřování e-mailem**</vpsadmin-nav> a zadej své současné heslo. ↵  ↵ Ověřování se začne používat, až se k účtu úspěšně přihlásíš alespoň z jednoho ↵ zařízení. Ze známých zařízení se dál přihlásíš jako dosud. Odebrání zařízení ↵ ani vypršení jeho zapamatovaného přihlášení ověřování e-mailem nevypne. ↵ Aktivní TOTP nebo přístupové klíče mají přednost; nastavení e-mailového ↵ ověřování zůstane uložené. ↵  ↵ Kód přijde pouze na tvoji hlavní e-mailovou adresu a vyprší 30 minut od ↵ prvního požadavku. Doručení může trvat několik minut, proto zkontroluj i ↵ složku se spamem. Nový kód zneplatní předchozí, ale neprodlouží dobu ↵ platnosti. Na jedno přihlášení si můžeš vyžádat tři kódy, vždy alespoň ↵ s minutovým odstupem. Po pěti chybných kódech přihlášení skončí; další ↵ limity se počítají společně pro více pokusů o přihlášení. ↵  ↵ Kód je potřeba také při získávání nového API tokenu pomocí hesla. Pokud ↵ účet vyžaduje e-mailové ověření, nelze použít HTTP Basic. Existující tokeny, ↵ relace a jednotné přihlášení fungují dál. Pro bezobslužné klienty použij ↵ existující API token. Pokud se nedostaneš do své schránky, použij známé ↵ zařízení či existující relaci nebo kontaktuj podporu. ↵  ↵ ===== Nastavení přihlášení ===== ↵  |

## Guarded content replacements

| Language | Page | Count | Existing text | Candidate text |
| --- | --- | ---: | --- | --- |
| en | manuals:vps:api | 1 |  The name and password must be sent along with every API request in HTTP header //Authorization//. ↵ This is a good choice for one-off actions. However, if you need to call the API repeatedly or ↵ automatically, storing the password on the disk or entering it constantly is not a good idea. ↵ HTTP Basic cannot be used if two-factor authentication is enabled on your account. | Send the username and password in the //Authorization// header with every ↵ request. HTTP Basic suits one-off actions. For repeated or unattended calls, ↵ use a token so you do not have to store or repeatedly enter your password. ↵ HTTP Basic cannot be used when the account requires two-factor authentication ↵ or [[manuals:vps:users\|new-device email verification]]. A Basic request does ↵ not send an email code. |
| en | manuals:vps:api | 1 | The client first requests a token using your credentials and optionally also TOTP. ↵ As soon as the client receives the token, the credentials can be forgotten and the token ↵ is used for authentication. | The client requests a token with your username and password and completes any ↵ required TOTP or email verification. Once it receives the token, it uses that ↵ token for further requests and no longer needs the password. ↵  ↵ When [[manuals:vps:users\|email verification for new devices]] applies, each ↵ fresh password-based token request requires an email code. ''vpsfreectl'' ↵ prompts for it. Existing tokens remain valid; use a previously issued token ↵ for unattended clients. ↵  ↵ Clients that cannot handle the ''email_code'' step, including the ''get-token'' ↵ helper in ''terraform-provider-vpsadmin'', cannot issue a token for an account ↵ that requires email verification. Use ''vpsfreectl'' to obtain a token for ↵ these clients. |
| cs | navody:vps:api | 1 | S každým požadavkem na API se musí zaslat jméno a heslo v HTTP hlavičce "Authorization". ↵ Je to dobrá volba pro jednorázové akce, pokud je ale potřeba API volat vícekrát nebo ↵ automatizovaně, ukládání hesla na disk či neustálé opisování není dobrý nápad. HTTP basic ↵ nelze použít, pokud máte aktivované dvoufaktorové ověřování. | S každým požadavkem na API posíláš jméno a heslo v HTTP hlavičce //Authorization//. ↵ HTTP Basic se hodí pro jednorázové akce. Pro opakované nebo bezobslužné volání ↵ použij token, aby ses vyhnul ukládání hesla na disk nebo jeho opakovanému zadávání. ↵ HTTP Basic nelze použít, pokud účet vyžaduje dvoufaktorové ověření nebo ↵ [[navody:vps:uzivatele\|ověření nového zařízení e-mailem]]. Požadavek přes ↵ HTTP Basic žádný kód e-mailem neposílá. |
| cs | navody:vps:api | 1 | Klient nejprve požádá o vytvoření tokenu, k tomu potřebuje jméno, heslo a připadně i TOTP. ↵ Jakmile klient dostane token, může jméno a heslo zapomenout a dále se autentizuje ↵ získaným tokenem. | Klient si vyžádá token pomocí jména a hesla a dokončí případné ověření přes ↵ TOTP nebo e-mail. Jakmile token získá, používá ho pro další požadavky ↵ a heslo už nepotřebuje. ↵  ↵ Pokud účet vyžaduje [[navody:vps:uzivatele\|ověření nového zařízení e-mailem]], ↵ kód je potřeba při každém získání nového tokenu pomocí hesla. ''vpsfreectl'' tě ↵ k jeho zadání vyzve. Existující tokeny zůstávají platné; pro bezobslužné klienty ↵ použij token získaný předem. ↵  ↵ Klienti, kteří nepodporují krok ''email_code'', včetně pomocného programu ↵ ''get-token'' z ''terraform-provider-vpsadmin'', pro takový účet nový token ↵ nevytvoří. Token pro ně získej pomocí ''vpsfreectl''. |

## Managed pages

| Key | Language | Page | Reconciliation | Canonical source |
| --- | --- | --- | --- | --- |

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
