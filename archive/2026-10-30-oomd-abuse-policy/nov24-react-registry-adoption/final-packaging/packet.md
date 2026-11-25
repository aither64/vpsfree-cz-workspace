# Exact React candidate — final package verification

**PASS**, clean frozen **6c6792a62d5bb1193b1ce96c0d6ff9167341de49**, tree **c591e51b6e701b19b5ec5daf2284ef0696f9bd16**.
All five documented outputs/checks succeeded in one ordinary batch0/**88.276s**.
No source/index/ref/lock or runtime mutation. Root retains CI observation; no
CI request/poll/wait was duplicated. No deployment or default integration claim.

Admission used the immutable local Git flake at the exact revision, no lock
writes, no updates/IFD/keepgoing, one job/core. Dry-run admitted six application
metadata/cache/build/check derivations plus ten small substitutions923KiBunpacked;
no kernel/compiler/system/VM or new toolchain build. Full saved graph contains1799
derivations; graph membership does not mean they were built. Graph/dry-run/resource
receipts distinguish current resident inputs from actual required work.

| Target | Actual successful resident output | NAR hash |
| --- | --- | --- |
| bff | `/nix/store/10wi281ym1hf55hb9zgpjd5vhzxm6xqi-vpsadmin-webui-bff-0.1.0` | `sha256-5nCtfeYN25uQy5QlYUw4lil4VmFjF+kQWRgmvJhBv8g=` |
| frontend | `/nix/store/4ma85rxiga402qa5i67ynjmzg4agi0j1-vpsadmin-webui-frontend-1.0.0` | `sha256-TZuB9ou5McQYHobHQzfL5lAe5CFKkx08fQLQJ3IZTiA=` |
| package-contents | `/nix/store/fx1dphmvzllkzg9k08jhfnyza8s3vyb0-vpsadmin-webui-package-contents` | `sha256-d6xi4mKdjkX2JFicDIv5niSzpyI0m/Hnm8GGAIU04kY=` |
| provenance | `/nix/store/p3vlsh9drr8mjjvahb4h4sy3r915n6sn-vpsadmin-webui-provenance` | `sha256-d6xi4mKdjkX2JFicDIv5niSzpyI0m/Hnm8GGAIU04kY=` |
| source-contents | `/nix/store/7ms2fxppwshj6g6m50clch775diy4mxw-vpsadmin-webui-source-contents` | `sha256-d6xi4mKdjkX2JFicDIv5niSzpyI0m/Hnm8GGAIU04kY=` |

Exact expected and registered derivers/NAR sizes are in output-bindings.json;
full paths/input edges in graph.json/derivation-graph.json/root-input-bindings.json.
Provenance check reused its exact existing derivation. Other roots were realized;
BFF fixed-output cache was already resident with the exact unchanged declared hash.
No unchanged-package metadata was relabelled as a new result.

Frontend+BFF actual schema1metadata both say full **6c6792**, **dirty=false**,
source=environment. Source `/nix/store/6s0ia6gknr3nv5jz34g8xz4cjqmhxs01-source`,
NAR `sha256-d35qzMZtzRYN98R1AhXT2qrr8gGuAjz+6RZBqVmz5dk=`, has **2893** included tracked files with every
Git blob/executable mode equal and no extras. This actual source selects exact
registrySDK0.6, SHA256f4ea2206e80798f001cd16942c99fab1c3c4bcaccac707ea3ca841b65efd1f3d,
348076B, sourceaed11 and the verified locked SHA512. The actual Nix npm-cache
blob matches those archive bytes/digests (registry-cache-binding.json).

Frontend FODcache `/nix/store/sbpxxhbwv8agiad5rq4nhay0wb2aval3-vpsadmin-webui-frontend-1.0.0-npm-deps`
NAR equals declared **sha256-yAOJrTTzxZeveFPN7kCFHA/0t0r+G2aoz2hqSL19+iI=**.
The normal frontend build consumed that cache successfully. Six documented
bundledWASI missing-resolved warnings remained and did not prevent this x86_64
build. Vite's existing chunk-size advisory remains; no threshold change.

Actual Gitless source check:18required inputs PASS. Actual Gitless design audit:
270routes/79API modules/294docs PASS. Actual package-contents check: **389public
assets**, matching clean frontend/BFF revision metadata; no extra public files or
source maps and required BFF contents/wrapper present under the documented checker.
These checks do not independently certify browser behavior or a running service.

BFF runtime files copied into the output equal current source; BFF source/lock/
package recipe are byte/mode unchanged from4499. Its actual cache NAR remains
**sha256-pifjCWQ5ShvtQw1V3bAlmutW43nPi93hDVW8Q4HuVMw=**. The BFF package has new
finalcommit metadata and an actual new derivation/output; this is fresh packaging,
not a claim of changed BFF application logic. No new credential/session/runtime
input was read. No closure claim beyond the actual package-content checker.

Fresh installed g7wv/catalog7659519 Luna/low watcher17585 reportedPASS; native99959
originalbatch joined0. All current handles61264/60500/18329/17585/99959/28011 joined,
no unknown command or effect. Complete logs are build.stdout/build.stderr and
watcher-message.md; no failure/retry or unsupported fallback occurred.
No service, claim, host, default, deployment, profile, lifecycle or cleanup action.
All source/check/effects windows and capacity **RETURNED ROOT ONLY**; implementer2
retains technical follow-up. Session/demo remain unchanged and open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
