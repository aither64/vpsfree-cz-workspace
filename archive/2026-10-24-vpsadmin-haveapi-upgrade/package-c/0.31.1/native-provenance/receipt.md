# Native C provenance diagnosis: exact source proved, embedded revision unavailable

Read-only diagnosis requested by lead. No application/provider/package/ref/guest
write, build, network probe, runtime change or cluster retry was performed.
Only this session's evidence files were written. Canonical `vpsadmin-webui` is
now the moved checkout at exact `e468ca48406bde1bd99cc42a05e1832fb42162f4`;
earlier standalone worktree paths are historical.

## Contract cause

Installed provider `vh650zaiazv3n8z12yf12pfbc951xwb9` emits a worktree override
as `--override-input vpsadminWebui path:<canonical-path>` in its
`dev-clusters/vpsadmin/bin/devcluster`, `nix_overrides` function (lines793–802).
The recorded final canonical metadata has SHA256
`eca154989f884c08822beffda85ce064d347f69f5f3ee75f61f62d9cf6d84e38` and records
this input as `locked.type = path` with no `rev` or `dirtyRev`.

WebUI `flake.nix` passes that flake self to `nix/provenance.nix`. The resolver
requires a valid full `self.rev` for clean provenance or a recognized
`self.dirtyRev` for known dirty provenance; otherwise it deliberately emits
`commit = unknown`, `dirty = true`, `source = unavailable`. Both packages consume
this one resolver. The frontend derivation actually receives
`VITE_BUILD_SHA=unknown`, `VITE_BUILD_DIRTY=true`; the BFF installs the generated
unknown metadata file. Thus the installed metadata is truthful for its flake
identity, not evidence that the retained application source differs.

Provider labels come separately from `source_revision/source_dirty` environment
values and are used for test-configuration labels. They are not passed into
the package resolver. Clean labels/current Git status alone do not prove package
identity. The NixOS module requires frontend/BFF metadata equality; it does not
require clean metadata. Both unknown records satisfy that equality. The package
guide explicitly reserves **clean release acceptance** for matching full
commits and false dirty flags. That gate has not passed for these native outputs.

## Independent complete source/input/output proof

[Filtered source proof](filtered-source-proof.json) and
[per-file contents/modes](filtered-source-files.json) compare the **complete**
retained source with Git object contents at exact e468 using the owning
`nix/source.nix` filter: all excluded directory parts, `.env*`, private local
config and E2E result paths are applied. **2,438 files /90,121,622 bytes** match
exactly, including executable bits; no extra retained file or symlink exists.
This includes both npm locks, package definitions, build/plugin scripts and all
application/BFF/test/docs inputs. It is not just a current-checkout or label check.

Both actual native package derivations reference the identical filtered store
source `/nix/store/6p46phpszswrwq6029rmj1gyyi7ynm44-source` (BFF uses `/bff`).
Its NAR is `sha256-v8sM+hBV76YE1COTvEorTg0OUSvWd4OkPzi2006mPmw=`, identical
to the original C0311 committed-source receipt. Raw path-input NAR includes a
different boundary and is not used as the cleaned-source equality proof.

| Native role | Actual derivation | Actual output | Current NAR |
| --- | --- | --- | --- |
| Frontend | `/nix/store/8n5b99rdprlsl97dkgn0dvl4hb1s87ap-vpsadmin-webui-frontend-1.0.0.drv` | `/nix/store/5y1vzyyvqgykc8hvzja4ixm1p6jvlg1v-vpsadmin-webui-frontend-1.0.0` | `sha256-lEKOEyFAA7wIBEPkGADFz0pPv1O0Yy+S0o0EvHrz95E=` |
| BFF | `/nix/store/q8r7d2q3mh3j9zh712z5i5626xiacgkh-vpsadmin-webui-bff-0.1.0.drv` | `/nix/store/nb19j3xdg1gjh4lkq1cd4qpd0g2m88nq-vpsadmin-webui-bff-0.1.0` | `sha256-CfKRW2qf8yI2D6Qwco5Cpyfe/bdqim05QRlyhodov14=` |

[Actual derivations](actual-package-derivations.json) retain full build
environment, outputs and inputs for both packages and both npm fixed-output
derivations. These package input/output edges match E3's already captured
complete **6,749-derivation** native graph, with no missing referenced derivation.
[Source/output chain](source-output-chain.json) binds that graph's hash and the
complete locked metadata. There are no additional application source inputs
outside the exact filtered source; build hooks, builder, Node, Python, stdenv
and runtime-wrapper inputs are explicit in these derivations and graph.

Provider/WebUI follows resolve to native nixpkgs
`718f670e845328e9c2cecdd832835712b2cbd065`, NAR
`sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=`, through native OS
`f4e55a13d7d2f5c1b61737f0300ec8a535ef02f1`, NAR
`sha256-HRAKzl1PywAm/AVo64V1PXOg5xD2i+Z1oMdrC/aG9Mk=`. Resolved node names
and full lock identities are recorded explicitly, rather than assuming a
similarly named lock node is the effective input. Build Node24.21.0 is
`/nix/store/q3ydkdhaj4y6k9pbpnriv5miqdgs1gsf-nodejs-24.21.0`; BFF runtime
is `/nix/store/hi7j7adiizy4cfprlj7xnx9ag3mrzmam-nodejs-slim-24.21.0`.
These are the actual native build/runtime inputs, not a claim of equality with
the standalone frontend/BFF artifacts.

Source lock SHA256 values are
`fed4e085dfc05d9e494e58b4fe981d93443b9954578ffac3d0e3b11b5da49892`
(root) and `50ffa053cd8b22d78505d10117fa2a42db62f73f6aa0b6de18138cbca9277d5a`
(BFF). Native npm FOD derivations use these source boundaries and the reviewed
recursive hashes `sha256-1b+5uUE4OHl47aOHSxV3Ea1VYk14soGFk48beqmmlkM=` and
`sha256-pifjCWQ5ShvtQw1V3bAlmutW43nPi93hDVW8Q4HuVMw=`. Root lock selects exact
HaveAPI0.31.1 and XHR1.8.0 with verified registry integrity. Native compiled
main contains0.31.1; all eight installed BFF own runtime/manifest files match
the exact source and all89 installed dependency package versions match the lock,
including qs6.16.1 and body-parser1.20.9.

The two build-only npm cache output paths are no longer registered/present.
Their retained derivations/FOD hashes and build dependency edges remain present;
no cache restore/rebuild was attempted or required for this diagnosis. There is
**no fresh cache-byte inspection claim**. The source and archive integrity proof
comes from the exact source locks, original release receipt and constrained FOD
build graph, with direct installed-output checks as above. This does not assert
reproducible-build attestation or independently recompute the whole native build.

## Actual services chain and disposition

The selected built configuration and E3's existing residency receipt bind
services drv `0cwgkvga191fc9kxs6g8kgd79fnhn2bf` to actual current/booted services
output `/nix/store/44b2rh8f1lzqb4kihz5gqaq8jh951cyk-nixos-system-vpsadmin-services-26.05pre-git`.
This diagnosis reuses that captured exact-system/root/closure proof; it made no
new guest call. Both native package outputs are in its saved actual closure.
The recorded complete graph reaches them through the newadmin container and
its system units. The actual built nginx configuration
`/nix/store/7x9kbzv88hzwqdq2q0hbia728mih995n-nginx.conf` names frontend5y1 as
its root; the actual built BFF unit `l4fcqsz8kihgxypcfwyg46gdvmg75qcf` names
`nb19.../bin/vpsadmin-webui-bff` as `ExecStart`.
[Dependency/service/output proof](dependencies-service-output-proof.json) and
[native NAR/reference records](native-output-nars.json) preserve these edges.

The bounded source-to-native-output chain is complete under ordinary Nix store
and recorded build provenance; exact e468 source identity can be stated
**independently of embedded metadata**. It does not make metadata clean, establish
standalone binary equivalence, or prove normal app/TLS/login behavior. E3's
remaining app-flow acceptance is separate and is not asserted by this receipt.

Smallest proposed disposition: qualified manual development testing of these
identified native artifacts with missing embedded revision disclosed, conditional
on lead/architect acceptance and E3's normal flow checks. Preserve running state
and honest unknown metadata. No source/provider fix or rebuild is needed merely
to change the displayed revision. Clean-release/default-readiness claims remain
withheld. If a future clean-release build is required, the existing package seam
is a genuinely Git-backed flake input carrying trustworthy `self.rev`; the
installed provider currently hardcodes path worktree overrides, so any change
to that input route needs a separate architect/lead brief and affected checks.
Never edit build-info, inject a label as a false clean revision, or weaken the
resolver. No such implementation is authorized or performed here.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
