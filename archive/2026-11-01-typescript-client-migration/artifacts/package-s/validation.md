# Package S accepted candidate

## Final provenance-only refresh

Current stable published SDK head is
`99ee06654ef956a09b52749f4cd02d1435362087`, on the same original SDK base
`e5786f69b7c223c3bb5b1de99b7f97186eec368a`. Its only source-tree difference
from accepted `b650f21` is the HaveAPI revision in `tools/generator.json`:
`172c752e` becomes `eea3ae5e82c3db23d5f5bc9f1a5e7784117c4e1b`.
The generator feature was rebased from `209a7ac0..172c752e` onto current
`391b0190..eea3ae5e`; the generator owner's range-diff proves one identical
patch. Independent source-tree comparison found no generator/Ruby/JS/version/
flake input changes. Generator source SHA256 remains
`ea539499207e09c7e1835733115aeca73db3175963b817c95a621baf45da330b`.

Offline regeneration `--check` and the source-refusal test passed against the
exact new pin; see `refresh-provenance-check.log` (one test, zero failures,
about 16.5 seconds for the source-refusal test). All 675 generated source files,
the manifest, all 1,352 built files, dependencies, compiler/build/checker/consumer
inputs and installed runtime are unchanged. Their accepted verification below
remains bound to those exact graphs; no build/type/runtime suite was repeated.

Final archive: `candidate-99ee066/vpsadmin-typescript-client-0.3.0.tgz`.

- SHA256:
  `f3bb42d0392fb738f5c70fe1415cc8742ab943a31c2ed2a85af5ccbd385d831f`.
- npm integrity:
  `sha512-6Q74ddIgGzeav9mvPubc33g5Sd+Ni7ZOLtKnNVzP/sW1Cxmw59nLiib50H27HBYc0UgoVfjlxuqH0WmX7hR3jw==`.
- Existing release receipt verified:
  `candidate-99ee066/receipt.json`.
- `candidate-99ee066/inputs.json` records exact source/build and all 1,360
  archive-entry hashes, old/new source and generator identities, affected check
  and accepted earlier integration/CI evidence. Only
  `package/tools/generator.json` differs from the accepted `b650f21` archive.
  No rebuilt or modified payload module is hidden by this provenance refresh.

Both older candidate directories/receipts remain unchanged. Local refs
`2026-11-01-typescript-client-migration-reviewed-383e855` and
`2026-11-01-typescript-client-migration-reviewed-b650f21` retain the old exact
reviewed heads. SDK feature publication used the explicit old-`b650f21` lease
and its remote ref was verified at exact `99ee066`; the local worktree is clean.
Fresh SDK `origin/main` remained the original base. Canonical HaveAPI remote
advertised exact `eea3ae5e` before the push. No further SDK source change is
planned without coordination.

Exact new SDK CI run
[41336140990](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/41336140990)
was queued when handed to the lead's shared watcher coordinator. Earlier run
41334654904 passed on exact `b650f21` and remains retained. No tag, npm
publication, default-branch integration or deployment was performed. W received
the final immutable archive and equivalence evidence; distribution approval and
the final registry dependency lock remain separate work.

## Accepted implementation and integration checkpoint

Final stable SDK source:
`b650f21fa83c314b3c21aaf62f0d9dda2b08befd`, one consolidated commit from
`e5786f69b7c223c3bb5b1de99b7f97186eec368a`. Generator:
`172c752ef65792de177279956917259d2c3f9b37`. API export:
`610a96f8ce523afbcd3e4374a70047dbe3264b0d`. Source/provenance and original
reviewed range are in [review-packet.md](review-packet.md) and
[schema-capture.md](schema-capture.md).

Reviewer0 completed the original G+S final review; the lead directly verified
the requested R1 strict-selector remedy and accepted A1 internal descriptor
simplification. The initial reviewed G/S heads were `7cffd0b6`/`383e855`;
the directly inspected final heads are `172c752e`/`b650f21`. No public IO,
migrations or persistence contracts changed. Source amendments consolidated
the same unpublished update stream; old review/candidate evidence was retained.

The fixed source batch `regenerate-fixed-quick.log` passed in about 74 seconds:
offline regenerate and check, build, TS6 source and consumer checking, TS5.9
Bundler consumer, 13 client/release tests and one source-refusal test. Generated
module bytes changed internally for A1, so these affected checks were rerun.
All 675 ownership hashes and recorded tooling/source hashes agree.

Immutable archive:
`candidate-b650f21/vpsadmin-typescript-client-0.3.0.tgz`, 337,415 bytes.

- SHA256:
  `8907e6bcfb013df86b9d1600db42ba724b2300a1cb866ebf05e2019aa24c537c`.
- npm integrity:
  `sha512-3GUpjTRa6hYPiIBRzumFM/MQ/tOu49yVvAW7o2CECSrZ/Ic5vObtwF0EqVT7wNDXPOVMfph+54eEZAM59Utngg==`.
- Existing release-tool receipt: `candidate-b650f21/receipt.json`.
- Complete source/tool/generator/lock and 1,352 built-file graph:
  `candidate-b650f21/inputs.json`. Each built file was compared with its exact
  archive entry; no rebuild or pack scripts ran while preparing the archive.
- Original candidate and receipt: `candidate-383e855/`, preserved unchanged.

Post-review integration passed without retry or repack. In
`archive-validation.log`, the exact retained archive passed ESM completeness,
TS6 and TS5.9 strict consumers, executor spies and actual installed HaveAPI
0.32.0 transport/decoding against the owned loopback HTTP fixture in about
13.92 seconds. The fixture covers mounted root/action OPTIONS, namespaces,
false/zero values, metadata override and canonical row metadata, raw receipts,
denied/malformed envelopes and local-input no-send behavior. Existing receipt
verification passed before and after the check. No harness processes remain.

Related generator integration also passed: `generator-runtime.log`, 11 wire
sends, 28 documentation snippets and 44 requests, about 26.37 seconds. Both
checks used the installed HaveAPI 0.32.0 runtime bundle SHA256
`9285eab56e435ee86a501a24808e15496d44521881a032090003a1108511f016`.

Package-owner reconciliation verified the unchanged clean SDK head and archive
receipt again after acceptance. Fresh SSH fetch found SDK `origin/main` still
at the exact original base `e5786f69`; no rebase was needed. Feature branch
publication completed over SSH at exact `b650f21` on
`origin/2026-11-01-typescript-client-migration`; the local checkout remains clean.
Canonical HaveAPI remote advertised exact generator feature head `172c752e`,
independently checked before SDK push. The generator owner also explicitly
fetched that remote ref and proved its exact head. HaveAPI default advanced from
the feature's original base `209a7ac0` to `391b0190` through three disjoint
commits; that newer default is not substituted for the reviewed/tested pin.
SDK CI run [41334654904](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/41334654904)
was in progress at this checkpoint on exact `b650f21`; monitoring is coordinated
by the lead through the shared utility slot. The SDK remains unpublished on npm;
no tag, merge or deployment has run. WebUI must use the exact candidate for its pilot until a separately
authorized distribution path resolves its final dependency lock.
