# E5 native React provenance: exact 2e32 source, qualified development metadata

Bounded independent source/input/output/service proof completed for E5's actual
native artifacts. No source/dependency/runtime writer, build, network/GET,
guest/root query, recursive graph recollection, provider fix or metadata change.
Canonical checkout remains clean at `2e32c814d3af70ac39257f2542075bd580ee38d4`,
tree `ae4e282a33886faff151818255a99bd5710de832`.

E3's [selected native paths](../../../devcluster/e5-runtime/selected-native-paths.json)
and selected config `lwmf26d62k9w45ky98iy4g95ng4rq6zf` bind services output
`/nix/store/4cjjwh6kikppbnqs8r9h0r2mz9jjym2j-nixos-system-vpsadmin-services-26.05pre-git`
and drv `i1rrlmg0bbfbrfrhy6ph8c85gkfxy4yq`. Config bytes match E3's saved SHA256
`cd2e27dc75548fdfd2f81f09025b85dbc7a9f12be40cbc05c5557d1f7ba660f6`.
Only allowlisted selected paths/hashes were used; no raw config/credentials/env
were output. E3's existing services current/booted-system/valid-closure/root
receipt is reused in [handoff bindings](handoff-bindings.json), with no new SSH.
Native completion is Unix1793185097.42711 /2026-10-28 10:58:17UTC; no individual
store build timing is inferred from buffered events.

| Native artifact | Actual derivation | Actual output | NAR |
| --- | --- | --- | --- |
| Frontend | `/nix/store/i7z06mz2xyqkpscxr8ki5mbgi7pn8zp5-vpsadmin-webui-frontend-1.0.0.drv` | `/nix/store/117zwv71hciz75xkc3kh79fsm6h7drzn-vpsadmin-webui-frontend-1.0.0` | `sha256-5D0H25JOIZzxJeZG1/8TYpOIh8w+Aq0VqtMnc3zhRuc=` |
| BFF | `/nix/store/jn4qqwxkpvxkwbr3rh3q5wklhzx754q2-vpsadmin-webui-bff-0.1.0.drv` | `/nix/store/x1wic1f55rrf75mrz6kw39flmmrxbw5i-vpsadmin-webui-bff-0.1.0` | `sha256-mmpWHdaPOxq7S48c81J5fjvfE38pO8VA39cmzjQAN7c=` |

Both outputs' registered derivers and actual derivation input/output records
match the nodes supplied by E3. Their source is
`/nix/store/c054hj749wd59b2qv5784bmkaxb8yg4f-source` (BFF uses `/bff`).
The [complete filtered-source comparison](filtered-source-proof.json) proves
**2,439 files /90,124,104 bytes**, executable bits and no extra files/symlinks
equal exact2e32 Git blobs under the owning `nix/source.nix` filter. This includes
all package/build definitions and locks. [Per-file hashes/modes](filtered-source-files.json).
Actual source NAR `sha256-ZaLAoXcf21glVgdjvUQ47TqCxsMli1ZSXbS30DKF9eU=`
matches the original reviewed filtered-source receipt after checking; no path
or standalone-output equality was assumed.

E3's **6,749-node** [complete native graph](../../../devcluster/e5-runtime/recursive-input-graph.json),
SHA256 `d96e905e8cdce0651431002302b8413ce8421fdb50d7aebac9a06cfa74aaf433`,
has no missing referenced derivation and is reused without recollection. It
links selected services through the newadmin container to actual nginx config
`/nix/store/26cc8fqyi1m16pncrny96h78mz3xjf7q-nginx.conf`, whose root is117zwv,
and BFF unit `sa3i1qk8v3fi1lvziklxld73n3z2nxx5`, whose ExecStart is
`x1wic.../bin/vpsadmin-webui-bff`. Both packages are in E3's saved actual services
closure. [Complete chain, follows, locks and consumers](native-source-output-chain.json),
[actual package/FOD derivations](actual-package-derivations.json),
[actual NARs/references](native-output-nars.json).

Effective native follows resolve WebUI to nixpkgs718f670e845328e9c2cecdd832835712b2cbd065
through OSf4e55a13d7d2f5c1b61737f0300ec8a535ef02f1; full locked nodes and exact
build/runtime Node/stdenv/hooks are bound in that chain. Native npm FODs use the
exact source locks and reviewed recursive hashes:
`sha256-EPQkMRkwpmmQAsf2T2WbK2x9We9M78A/lT8R17x7+vs=` (frontend),
`sha256-pifjCWQ5ShvtQw1V3bAlmutW43nPi93hDVW8Q4HuVMw=` (BFF).
Root selects HaveAPI0.31.2/XHR1.8.0 with the previously verified E2/installed
archive integrity. The native compiled main contains0.31.2; all eight installed
BFF own manifest/runtime files and all89 dependency versions match exactsource/
lock, including qs6.16.1/body-parser1.20.9. The build-only npm cache outputs
are absent; retained FOD derivations/hash/edges were checked, with no restore
or fresh cache-byte claim.

Both embedded metadata records remain schema1 `unknown`, `dirty:true`,
`source:unavailable`: the recorded provider `path:` input has no self.rev/dirtyRev
and the unchanged resolver truthfully reports that absence. Selection labels
are separate and are not the source proof. **Normal embedded clean-release
provenance remains unmet.** Independent exact2e32 source identity is established
under ordinary Nix build/store provenance; standalone binary equivalence,
reproducible-build attestation and application-flow acceptance are not claimed.
No deviation requiring source correction or rebuild was found. Qualified manual
development-use disposition remains with lead/architect and E3's prescribed
actual TLS/login/Go-page checks. Existing roots, old evidence and running cluster
are retained; no lifecycle/default/PR action.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
