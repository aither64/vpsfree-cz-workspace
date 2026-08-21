# Content replacements preserve surrounding page tags

Initiative: `work/2026-08-18-vpsadmin-password-reset`

`bin/kb-contract-build` replaces only the exact text matched by a
`content_replacements` entry. If a production page already has an invisible
`<page>` language-pair tag outside that match, the builder preserves it.

When a full article body is replaced, inspect both the fetched source and the
candidate with `rg -n '<page>'`. Add the shared tag only to a language variant
that does not already contain it. Otherwise the candidate can contain two tags
even though the replacement plan itself contains only one.

After correction, rebuild the candidate and its manifests, then rerun the
all-page annotation checker. Both metrics candidates in this initiative contain
exactly one `<page>manuals:vps:metrics</page>` tag and pass validation.
