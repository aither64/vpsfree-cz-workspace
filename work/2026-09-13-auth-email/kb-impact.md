# KB impact

The new profile section has semantic ID `member.email-verification`, with
path `member.email-verification.open`. Local bilingual candidates add an
email-verification section to `navody:vps:uzivatele` / `manuals:vps:users`.
The complete source inventory contains 114 Czech and 77 English pages.

Existing account screenshots capture individual sections: email roles,
multifactor status, session settings, mail-template recipients, TOTP device
confirmation/list, and sessions. The new section is outside their crops and
changes none of the captured labels, controls or contents. No existing bitmap
needs regeneration, and the new prose does not require a screenshot.

The all-page annotation validator found four pre-existing mismatches between
production and the fetched contract base:

- `cs/navody:vps:ip_adresy`: `networking.host-addresses.add` expects 1, has 0.
- `en/manuals:vps:ip_addresses`: same expected 1, actual 0.
- `cs/informace:jak_psat`: `member.public-keys.add` is present once but is not
  registered in the contract.
- `en/information:kb`: same unregistered annotation.

These are outside the changed account-management pages. Do not silently
rewrite unrelated pages or accept their contract evidence as part of this
feature. Focused account-page validation and schema-5 bilingual release
manifests are complete. The contract now pins pushed vpsAdmin revision
`1b82f44b88663b9a50e82012c1e77f561b294bc5`; full contract checks and both
documentation reviews passed (with focused pin validation for the final
test-only API revision). Production has not been changed.

## API authentication guides

The Czech `navody:vps:api` and English `manuals:vps:api` guides also need their
HTTP Basic and token-authentication descriptions updated. The candidates now
cover required email codes, Basic refusal without sending mail, continued use
of existing tokens, vpsfreectl prompting and the unsupported get-token helper
in terraform-provider-vpsadmin. These are API/CLI instructions and introduce no
new WebUI navigation action. Existing language markers, navigation markup and
other guide content are preserved.

The replacement plan uses schema 3 for four guarded content replacements.
Candidate construction changes four public pages in the complete 191-page
inventory. Each schema-5 release now contains the account page and API guide
for its language, with per-page summaries and no media or deletions. Both
expanded releases are staged and verified; production is unchanged. See
review-api-docs-packet.md for the separate GENERAL review of this addition.
