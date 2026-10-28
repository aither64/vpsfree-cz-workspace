# API article restructuring: local checks

Prepared for independent source review; no staging or production write occurred.
The lead authored all three bilingual editorial snapshots, publication snapshots
and localized summaries. Candidate prose remains byte-identical to those inputs.

| Final output | SHA256 |
| --- | --- |
| `kb-candidates/cs/navody/vps/api.txt` | `1dac0f87623b0d802882e35fc80939ac41d514c4365323163af2a4c9f2103b9a` |
| `kb-candidates/en/manuals/vps/api.txt` | `a88bce7f0c13848f3b80029beb7365a0ab8b46d0937ae29f3774b4520f80831b` |
| `kb-release-cs.yml` | `1cdbdbd111b80b63a13ecb6120390fb685c09023e9beb2b6c71b1597dd772073` |
| `kb-release-en.yml` | `7d6fbfe28cb732321e2da8d0d6c596ebb001a39222db5480ca4f574ffb5357ef` |
| `release-changes.yml` | `34a27246bf7082e0016d8b73aad8815437226fba6c77c4fcf4a3481d87a45fb0` |

Each editorial snapshot passed the existing `package-d/prepare-release.rb`
canonical builder and the selected installed `KbRelease::Manifest` parser and
checksum reads: schema5, 191 unique pages (114CS/77EN), exactly2 changed and189
preserved, one write per language, no media/deletions/managed provenance.

The unchanged saved production guards are CS1783860648/content
`8ea88de825d7b3823aee1d4ff8fd2704c9eb2f431cfbb944643927eabde3fd13`
and EN1777543182/content
`8006293f735a7e6f45c04d2d59ad82a003afa4547db1ddb38f380504e1e107d3`.
Source index SHA256 remains
`87c999835a1015665ed985ce2f85e8f05348ae7f11e7c93625538933af6709d7`.
These are preserved source facts; no fresh production query was run in this batch.

Focused checks passed: authentication/scopes before CLI/main Ruby, then all other
clients; exactly one reciprocal page marker in each final/editorial candidate;
no haveapi-fs or SDK/generated framing; protected generic0.31.2 and separate
TypeScript client0.1.1/runtime0.30.2. All35CS/32EN old non-FUSE code blocks and
the general authentication/scopes body remain exact. Existing Python/JS/TS/Rust
blocks retain their bytes. Existing Ruby backup examples remain with Ruby.
No new vpsAdmin WebUI action or navigation annotation was introduced.

Only the new Ruby and PHP read examples were syntax-checked, in each language,
using installed Ruby3.4.9 `ruby -c` and PHP8.4.27 `php -n -l`; all4 passed.
Static interface matching used retained HaveAPI release
`819bba5110e089465535ecd71ca2eb37a7d39caa` Ruby/PHP README, PHP Client/Token
source and composer metadata, the retained vpsfree-client wrapper, and Go README
`73f164dd5eeebfc494705ae27981d30872fa88c3`. PHP has no new runtime-floor claim.
No example/API execution, install, SDK compiler, registry/browser/capture or
client-test campaign was run. Prior consumer evidence retains its original scope.

All6 publication diffs exactly match their predecessor/content hashes in
[content-chain.json](publication/content-chain.json); final publication pages
equal the final editorial candidates. EN publication01 intentionally retains
the original absence of a page marker; publication02 adds it. The supported
[publication plan](publication/README.md) requires real predecessor production
readback before binding each later revision. No future revision was invented.

First checker failures remain local evidence: an initial new-block count missed
the PHP/Go install blocks; an intermediate marker assertion missed EN01's
preserved baseline; direct parser imports initially lacked the installed
wrapper's load-time environment. Each was diagnosed without prose changes,
build repeats or staging actions. Required parser values were then supplied and
both manifests parsed successfully. Whitespace diagnostics identify exact legacy
page lines and unified-diff context/quoted source; those bytes were preserved.
Detailed local results are in `quick-checks.json`, `quick-first-failure.json`,
`canonical-0*.json` and `whitespace-classification.json`.

Exactly three focused KB commits retain the old committed history. Their
publication snapshots and normal manifests support each logical change.
**NO MIGRATIONS:** no application, dependency, API, database, persisted format,
deployment, auth policy or cluster behavior changed. No source branch was
integrated or pushed by this package. No shared unrelated path was staged.
Lead owns final review assignment, state and handoff. The current owned KB stage,
cluster and session remain open; their last verified facts were not refreshed.
