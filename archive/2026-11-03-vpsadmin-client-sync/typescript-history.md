# TypeScript history ownership correction

Current final head: `c53cb4dabb0b3aac8d05834478872d2cfa698fa7`. Final tree
unchanged: `c85e30b1fc1ae27bba9c08884e11fa78bbb15f7b`. No product changes.
Lead is inspecting the narrow history remediation; current-head native CI
passed. The CI-only utility completed and released its slot; no new local
build/test/setup.

The user correctly challenged the original combined TypeScript commit. Lead
and owner accepted that consumer coverage, generated refresh and release metadata
were independently reviewable. The first split still put a future release-lock
hash in the generated commit and delayed its existing schema assertion update.
Reviewer identified that forward dependency as Blocking. Lead accepted that its
instruction permitting the future hash was wrong. Both earlier decisions and
review records are retained historically, not treated as current acceptance.

## Complete final series and logical ownership

Repository `git@github.com:vpsfreecz/vpsadmin-typescript-client.git`, target
`main`, feature `2026-11-03-vpsadmin-client-sync`, base
`d354491537f8b654b4d2c33a705cad84474f95d6`.

| Commit | Owned change |
| --- | --- |
| `ec08ec18c4d9ba9f4f311cfb9e5af12fd4f01c97` | One schema/provenance/generated refresh, saved inventory docs and the existing consumer schema-hash assertion; 18 files |
| `2071a164eab6a7681c5ba35542768c8a5e16251b` | Added HTTP and strict-type consumer coverage only; 2 files/62 insertions |
| `c53cb4dabb0b3aac8d05834478872d2cfa698fa7` | Package/lock 0.4.0, changelog/README and the one package-lock tooling hash change; 5 files |

`tools/generator.json` contains distinct identities with distinct logical owners.
The generated commit changes schema/provenance hashes, while retaining the actual
0.3.0 lock hash. The release commit changes the package-lock hash exactly once,
alongside the corresponding package/lock version. This is appropriate ownership
of separate keys in one file, not a repeated schema/pin stream. No forward hash
excuse remains in the generated commit message. Consumer additions follow the
new generated operations; the existing schema assertion is updated immediately
with that generated schema. No intermediate generation or compatibility path.
No migrations, new runtime dependency, API source edit, deployment or publication.

## Read-only per-commit proofs

Git-object inspection at base and every final commit proved:

| Commit/version | Actual package-lock SHA256 equals recorded pin | Existing schema assertion equals generated export and raw schema hash |
| --- | --- | --- |
| Base d354491 / 0.3.0 | `ea6d84d57e98a4085399d2a40f5e702822744845a0eaf93d5385210e6208fdd8` | `476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794` |
| ec08ec1 / 0.3.0 | same 0.3.0 hash | `d6ec617653913c56e92398a6032aa350118597a0e3f45c599bc92b6071ea0a26` |
| 2071a16 / 0.3.0 | same 0.3.0 hash | same new schema hash |
| c53cb4d / 0.4.0 | `00f789d4786fdcb2c9e61481e86180e376ea1ed86a022c2e22567b4d03946066` | same new schema hash |

Package and both root lock versions agree at each commit. These are object/hash
checks, not executed local suites. Whitespace checks passed; ordinary commits
used hooks enabled and messages from files. No declared hook framework/custom
hook path or active common hooks. Worktree clean.

## Ranges and retained evidence

Original tested range:
`d354491537f8b654b4d2c33a705cad84474f95d6..a4fc2449a1b5255b93b0c669ea9c454fac990536`.
Rejected first-split range:
`d354491537f8b654b4d2c33a705cad84474f95d6..2256ea46a8d8d135f352a524fbf048869d6eddf4`.
Current final range:
`d354491537f8b654b4d2c33a705cad84474f95d6..c53cb4dabb0b3aac8d05834478872d2cfa698fa7`.

All three heads have the exact final tree above; `git diff --exit-code` old/new
is empty. [Object proof](typescript-history-proof.json),
[original-to-final range-diff](typescript-history-range-diff.txt),
[first-split-to-final range-diff](typescript-history-ownership-range-diff.txt).
Original first-split [receipt](typescript-history-2256ea4.md),
[packet](typescript-review-packet-2256ea4.md),
[proof](typescript-history-proof-2256ea4.json) and
[range-diff](typescript-history-range-diff-2256ea4.txt) remain intact. Old heads
are locally anchored by own `reviewed-a4fc244`/`reviewed-2256ea4` refs.

Authorized exact-2256ea4 force-with-lease succeeded. Fresh remote feature is
c53cb4d; remote main remains d354491. Superseded CI41667969378 had already
completed successfully, so it was not cancelled. Current CI
[41668853169](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/41668853169)
checks actual final head. Feature comparison capture repeated at base/c53cb4d;
clean native detached integration target remains at base. No repository claim,
default merge/push, tag, publication, Phase 2 or lifecycle action.

## Verification boundaries

Old local checks, archive and receipt remain exact old-head a4fc244 evidence;
never relabel them as current-head execution or publication provenance. Archive
SHA256 remains `e3c1cee328c8c0bb6826c209bee971d5e6939d2acbeebf9938fc6f032db95326`.
The original executed command is preserved as
[typescript-checks-tested-a4fc244.sh](typescript-checks-tested-a4fc244.sh).
Current `typescript-checks.sh` is an unexecuted c53cb4d template only. Exact tree
identity preserves content review; it does not independently certify Nix checks.
Current native CI provides its own actual-head matrix/artifact/receipt. Later tag
publication uses its own exact tagged workflow artifact, not the old tarball.
Original pinned toolchain/generator paths and inputs remain in old receipts;
no new local build/regeneration/test/setup was run for either history split.

Current native CI41668853169 completed successfully on exact c53cb4d.
Artifact13245379341 and its downloaded receipt bind that head/version0.4.0/tag
null; archive SHA256
`3a6f2a2a6f4eaeb31f490035b312e9b5403cf21589d649dc1fd31d60b64e1906`,
verified independently after watcher completion. Evidence:
[CI result](typescript-ci-c53cb4d-result.md),
[metadata](typescript-ci-c53cb4d-artifacts.json),
[receipt](typescript-ci-c53cb4d/receipt.json). This is branch-validation evidence;
later exact tagged native workflow supplies the publication artifact.
