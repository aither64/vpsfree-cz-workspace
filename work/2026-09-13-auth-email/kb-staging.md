# Staged account and API documentation

The account and API pages in both languages are staged and verified.
Production pages are unchanged.
The exact candidates and schema-5 release manifests remain in this initiative.

- [Czech account page](http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody%3Avps%3Auzivatele)
- [English account page](http://kb-en.aitherdev.int.vpsfree.cz/doku.php?id=manuals%3Avps%3Ausers)

Verified revision summaries:

- Czech: **Doplnění volitelného ověřování nových zařízení e-mailem a jeho použití v API**
  ([revision history](http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody%3Avps%3Auzivatele&do=revisions))
- English: **Add optional email verification for new devices and explain API authentication**
  ([revision history](http://kb-en.aitherdev.int.vpsfree.cz/doku.php?id=manuals%3Avps%3Ausers&do=revisions))

`kb-release stage --manifest … --yes` and `kb-release verify --manifest …`
passed for `kb-release-cs.yml` and `kb-release-en.yml`. Each manifest contains
two page writes, no deletions, and no media changes. Verification also
warmed and checked both reciprocal Czech/English page pairs.

The staging container remains owned by this session with the release pending.
Production promotion requires direct user approval of these exact manifests.

API guides:

- [Czech API guide](http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody%3Avps%3Aapi)
- [English API guide](http://kb-en.aitherdev.int.vpsfree.cz/doku.php?id=manuals%3Avps%3Aapi)

Verified API-guide summaries:

- Czech: **Doplnění e-mailového ověřování při získávání tokenů a omezení HTTP Basic**
  ([revision history](http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody%3Avps%3Aapi&do=revisions))
- English: **Explain email verification for token requests and HTTP Basic restrictions**
  ([revision history](http://kb-en.aitherdev.int.vpsfree.cz/doku.php?id=manuals%3Avps%3Aapi&do=revisions))

The expanded manifests passed staging and verification again with both pages
per language. Account-page summaries and content remain unchanged.
