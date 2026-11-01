# Proposed KB article revisions

These three revisions take each current production article directly to the reviewed final text. Each diff compares one step with the preceding step.

[View all additions and removals](diff-preview.html)

## 1. Remove obsolete material

Remove the haveapi-fs client and FUSE guide, plus the old haveapi-webui listing. Remove the obsolete HTTP-header warning from the Czech article. Keep the Ruby backup examples.

| Article | Exact changes | Complete page after this step | Lines |
| --- | --- | --- | --- |
| Czech — navody:vps:api | [Readable diff](diff-preview.html#step1-cs) · [Unified diff](01-remove-obsolete/cs.diff) | [Page source](01-remove-obsolete/cs/navody/vps/api.txt) | +0 / −81 |
| English — manuals:vps:api | [Readable diff](diff-preview.html#step1-en) · [Unified diff](01-remove-obsolete/en.diff) | [Page source](01-remove-obsolete/en/manuals/vps/api.txt) | +0 / −77 |

CS: Odstranění zastaralých klientů a upozornění na HTTP hlavičky

EN: Remove obsolete clients and the haveapi-fs guide

## 2. Update authentication, CLI installation and Ruby examples

Update the token and authentication guidance, CLI installation instructions and Ruby examples. Group the Ruby VPS listing and backup examples together, with token acquisition and a commented existing-token alternative.

| Article | Exact changes | Complete page after this step | Lines |
| --- | --- | --- | --- |
| Czech — navody:vps:api | [Readable diff](diff-preview.html#step2-cs) · [Unified diff](02-auth-cli-ruby/cs.diff) | [Page source](02-auth-cli-ruby/cs/navody/vps/api.txt) | +49 / −13 |
| English — manuals:vps:api | [Readable diff](diff-preview.html#step2-en) · [Unified diff](02-auth-cli-ruby/en.diff) | [Page source](02-auth-cli-ruby/en/manuals/vps/api.txt) | +52 / −12 |

CS: Uspořádání autentizace a CLI, aktualizace instalace a příkladů v Ruby

EN: Organize authentication and CLI usage and update installation and Ruby examples

## 3. Add the other clients and the opening overview

Add the final installation, authentication, VPS listing and run examples for PHP, Python, JavaScript/TypeScript, Go, generated TypeScript and Rust. Add the opening overview with links to those sections.

| Article | Exact changes | Complete page after this step | Lines |
| --- | --- | --- | --- |
| Czech — navody:vps:api | [Readable diff](diff-preview.html#step3-cs) · [Unified diff](03-other-clients-overview/cs.diff) | [Page source](03-other-clients-overview/cs/navody/vps/api.txt) | +248 / −13 |
| English — manuals:vps:api | [Readable diff](diff-preview.html#step3-en) · [Unified diff](03-other-clients-overview/en.diff) | [Page source](03-other-clients-overview/en/manuals/vps/api.txt) | +247 / −13 |

CS: Přehled klientů a příklady pro PHP, Python, JavaScript, TypeScript, Go a Rust

EN: Add a client overview and complete examples for PHP, Python, JavaScript, TypeScript, Go and Rust

## Production to final

| Article | Exact changes | Current final staging preview |
| --- | --- | --- |
| Czech | [Readable diff](diff-preview.html#full-cs) · [Unified diff](production-to-final-cs.diff) | [navody:vps:api](http://kb-cs.aitherdev.int.vpsfree.cz/navody/vps/api) |
| English | [Readable diff](diff-preview.html#full-en) · [Unified diff](production-to-final-en.diff) | [manuals:vps:api](http://kb-en.aitherdev.int.vpsfree.cz/manuals/vps/api) |

This preview preserves the reviewed final article text. No production or staging writes have been made for this preview.
