# Static package proof complete; execution pending

Retained CI source is **a06b0cfa2abd7560f10cb58ebe99d8eb3f10b8f9**,
run40745814145/attempt1, artifact12842017816, version0.31.0. Final runtime source
is separately lead-bound to **cefe8c5d43277dbaba35632b5239d95a1959cf1e**,
tree7af42033e378e354a035e9eb99b6c78d85a11d84. Packages are not relabelled as
built from the CSS successor.

## Integrity and contents

ZIP SHA256 `86c49d97e29e628bf87a6ba6f74892216c9b31a5514bc93b218a60175810b2e4` matches its retained API digest.
Safe extraction used only a new own evidence directory, rejecting duplicates,
unsafe paths and links. Manifest SHA256 is `366b7d7605fed60d46b69e0f8d8ec148624a55ec7ba4eed7a53fd6384c3411a4`.
Exact schema/source/version/tag/run identity passed; all **11** manifested file
SHA256 values match actual members; all **10** complete dependency locks and all
**12** build-tool identities are retained in manifest-proof.json and ci-locks/.
No artifact was rebuilt, repaired or overwritten.

| Input | Actual SHA256 |
| --- | --- |
| npm haveapi-client-0.31.0.tgz | `1f01aea5cd29415013b21cbe763ae5823d6889d8b6a93567916801ac50705af3` |
| Python wheel | `016a08dfe2ca6c629034bb2308267c234a21cb00edda019bd56a206e8c1e1aca` |
| Python sdist | `75c48e61e7cb87639f6b0e32f4beca4cd458a3a591a99b1afbb9e1f41d78f7cf` |
| Built JS runtime | `38be7c0552cb29193d576b5150159b5268374cba14b889f3160fe8ebe41e11ad` |

npm package metadata exactly matches current source name/version/main/types/
dependencies. Runtime bytes match the retained companion runtime and checkout
build; all **46** packaged declarations match current prepared declarations.
All **19** Python module payload files match wheel, sdist and current source;
README/license bytes match source. Wheel METADATA and sdist PKG-INFO match
name/version/summary/Python range/license/classifiers/dependency bounds/source
URLs; no unexpected script entry points. The existing read-only Python artifact
inspector passed. Exact hashes in package-and-source-proof.json.

## Preserved first failure and classification

The initial raw pyproject byte-equality failure remains in first-failure.json,
receipt.md and pyproject-byte-difference.patch. It is ordinary TOML serialization:
only array indentation/line wrapping differ. The **entire parsed TOML document
is exactly equal**, with no ignored fields or version normalizer: project values,
dependency/list order, URLs, build backend/range and all tool/dev settings agree.
The repository declares uv_build>=0.13.0,<0.14 and documents native uv backend
use; CI manifest records uv0.13.4. Thus byte equality was the incorrect assertion,
not a package-input mismatch. metadata-classification.json records the corrected
semantic proof while preserving both source/sdist raw hashes. No product fix.

## Final source and input closure

All **905** recorded a06b source blobs were compared against the current final
worktree using Git object hashing without Git mutation. The sole difference is
the accepted documentation.css blob `b373493a319813ec20b6812d7b95edb6a5e83ef5`
(SHA256 `ed81059d84817e80b27b64910d23544f981e461c35fa760aaebf6d73de8622cb`). All renderer/runtime/generator/
fixture/harness/spec/manifest/build-declaration inputs are unchanged. The harness
fetches HTML and executes extracted code; it does not load or evaluate CSS.
A **256**-blob broad source dependency closure and prepared file identities are
retained in harness-inputs.json. This supports later unchanged-input reuse;
it is not an installed-program result.

No static selected-platform prerequisites are missing. Compiler6.0.3,
Node declarations24.19.2, root/server bundle files, Ruby3.4.11 bundled gems and
Python3.11.17 interpreter are present. Two gems are supplied by Ruby itself;
nine foreign-platform sqlite records do not require local installation.
CI root/JS/Python/Rust locks that are actually byte-equal are labelled so;
local server lock differs solely io-console0.9.4 versus CI0.9.5 and its checksum,
retained in ci-local-server-lock.diff. Graphs were not changed or conflated.
Network reachability, actual isolated install resolution and bundle loading are
unexecuted prerequisites to observe during the later authorized harness run.

## Commands and boundary

commands.pending.md supplies both exact existing dynamic_acceptance.rb commands,
same retained npm plus wheel then sdist, prepared absolute compiler/type paths,
new distinct output directories and root Nix/server-Gemfile environment. They
remain **UNEXECUTED**, awaiting main's final run grant and one fresh retained
Luna/low watcher. No duplicate CI suite is planned. Scope is six **thorough**
variants; no installed simple-program pass or real provider/OAuth acceptance.

This operation performed only static archive/metadata/source comparisons and
own evidence writes. No dependency resolution/install, network, tests/builds,
Git/hooks, source repair, service/browser/preview/peer/TLS/lifecycle action.
No active command/watcher; utility capacity untouched and released.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
