# Go query expectations: final source handoff

Final head `b64fb25bea8d8222fb3263b99956c0b61438a859`, tree `05384a632290653cb4560c7451b3897acd5956c8`; base
`a32b15e379f44fc6dae4b15ef4ec17a142e5f465`. Prior reviewed/executed head `ee67d27419c48d27a01c83a29114adf9a82062ba`.
All intended source is committed; tracked source clean, index empty, no command
pending. Git/source/hooks yielded to lead for the same retained reviewer's
general, architecture and scope gate. No Go acceptance retry or push performed.

## Accepted bounded correction

Lead directly accepted owner2's exact two harness paths, inline comment and
fixture-only diagnostics. Existing generated Go SDK query booleans encode false
as string0 and true as string1. The exact expectation now matches that contract;
nullable name remains an empty string, integer zero remains string0 and unused
fields remain absent. Full parsed-query hash equality is retained. WEBrick's
request-owned raw query is captured, and mismatch diagnostics include expected,
actual parsed and raw query values from the deterministic fixture. No product
tracing, body/header/token logging or production behavior was added.

The existing pure checker now feeds real in-memory `WEBrick::HTTPRequest` through
the actual harness `serve` and private `verify` methods. One exact query passes;
eight mutations must fail with useful parsed/raw diagnostics. Existing seven body
positives and52 body negatives remain. No listener, generator or compiler starts.
No runtime/SDK/renderer/schema/default/dependency/generated payload/project docs
change; the adjacent comment is the useful lasting explanation.

Owner evidence: `package2-go-query-fix-receipt.md` and its linked diagnosis.
Focused7 body positives/52 negatives plus1 query positive/8 negatives pass;
Ruby syntax2 OK, style2 zero offenses, whitespace clear. Only formatting blank
lines followed the focused run, and owner inspected final diff. Both exact yield
SHA-256 values matched before staging and after consolidation:

- `c6a9521990dfe7d4b07b46097ec99588f4529d008789ed7f66973e82cf6e3453` — acceptance harness
- `05fa6dc66a006174202e038f6d4851bfce37ecc09aef619606550168225ee13f` — native verifier check

No owner broader check was repeated. These controls establish fixture assertion
fidelity; actual Go network/authentication/state execution remains unproven.
The earlier failed query's actual raw capture was not retained. Constructed
native controls are not mislabeled as that failed run's capture.

## Hooked commits and history

Only the exact2 paths were staged and committed through a temporary message file
as fixup `d4a3b4137e3a80eb5f04a3140a3dd55dc6aa401e`. Top-level tools-only Nix,
mandatory I18n/RuboCop/message hooks passed without bypass. Advisory message
width warning was below the80-column requirement. The fixup was autosquashed
only into the existing Go source purpose. All12 rewritten logical commits ran
declared amendment hooks through temporary message files; final metadata hooks
included I18n/PythonChecks/PhpCsFixer/RuboCop, all passing.

Exactly22 purposes remain, with first10 hashes identical and21 other raw diffs
and stable patch IDs equal. Last metadata patch/message unchanged, exact
one-line `Version 0.30.0`. Released maintenance patches and `-x` provenance remain.
Pre-fold d4a3b413 tree and complete binary base-to-head diff equal final. No
conflict/source decision occurred. Whole-range whitespace clean. Old ee67→final
semantic delta is precisely the2 accepted harness files. No migrations, schema
or persisted format conversion; prior full-branch conclusion remains applicable.

Full streams are in `go-query-final-streams.md`: no new dependency/channel/lock,
generated payload or metadata stream. One cumulative JS generated update follows
both source purposes; coherent shared metadata remains separate and last.
Original reviewed refs, records, failures and successful execution evidence are
preserved; local retained refs bind reviewed ee67 and pre-fold d4a3b413.
Fresh SSH pre-fold mastera32b15e/featureee67 proof is in remote.txt. No push.
Portal comparison captured exact final base/head.

## Inputs, prior execution and artifacts

`go-query-final-input-equivalence.json` compares complete750-entry ee67 and final
trees:748 mode/type/blob identities unchanged, only2 existing harness blobs
changed. Entire server/JS/Python/Rust/Ruby-client/workflow/release-tool sources
and tracked toolchain/config inputs match. All9 live dependency locks match the
actual retained ee67 artifact manifest. Original749-entry3fb91 baseline and its
full prior equivalence proof remain untouched. No toolchain change or install.

`go-query-final-rust-input-equivalence.json` proves all310 original tracked Rust
inputs from actual48543 and both flake inputs match final. Successful915.38s
Rust dev/MSRV execution and generated Cargo/source/tool graphs retain actual48543
identity. Dynamic installed npm/wheel/sdist success retains actual3fb91 identity.
No dynamic/Rust rerun or false final-head execution claim.

The actual ee67 run remains exit1 after27.4s: final artifacts/manifest and all16
Go programs compiled, with object/empty/omitted/list/failure/association execution
passing before query assertion failure. Previous output, fixtures/results and
CI records remain exact historical evidence. Final artifact rebuild/verification,
actual full Go16 compile/run and selected final-head CI remain lead-authorized
completion work after the independent final gate.

All12 exactee67 artifacts including hidden `.gitignore` are preserved in
`verified-core-artifacts-ee67d274/`; manifest source and all before/copy/source/
preserved SHA-256 values match. Dist remains literally empty. Known unrelated
PHP result cache and release Python cache remain untouched. No cleanup/default/
tag/releasebranch/registry/deployment/session lifecycle action occurred.

## Complete final series

- `b3a6a0b10ab06c83177136023ab9614aa3204b2d` release: include the Rust generator in shared releases
- `5b5f0c25da55b1df0b14ba16a9a6d3732bccbb28` servers/ruby: validate structured API examples
- `dda40adbad834456f3470e811aff8c873d30acef` servers/ruby: syntax-check generated client examples
- `9c4c8a7c1a56caff6cd1b852f8bfb16afd7ccaaa` servers/ruby: render nested PHP example values
- `878509d5ff4ddf07d5e18341b9c3f5b9c18d9a09` release: cover Rust publication and publisher setup
- `1e810107d798186d57dc05524b78031a3ab7a6a7` release: update PyPA publishing action to v1.14.3
- `f50c540da1008e848d78586530b11d574ec08dbc` servers/ruby: remove unmaintained filesystem examples
- `4337f1a60021c2bab2cd1dd704764bb9d093b622` servers/ruby: add request-local client documentation context
- `b495832dd760e796c0eee61dc8e38ba542af3ba3` servers/ruby: render filtered client documentation panels
- `593fac92f825ffbfb39ae99f065974c48cd43c6b` clients/js: add Node 24 types for documentation acceptance
- `47c54cb06b70d97d42b0b4e6b6d033fb3cfa9d7a` clients/go: render SDK documentation from saved profiles
- `8dbf66acffe5613d93b5c00e91c4b5d5935982bb` clients/rust: render SDK documentation from saved profiles
- `1651a94888207bcede6d839359715d2e4e01f68e` clients/js: add typed action lookup
- `822eaa5a4cfb30c56bbd9fc14afa1e2c50c0841b` servers/ruby: document maintained dynamic clients
- `514a62b19744f56f1f767d71c0b25b2fd8905ab9` servers/ruby: ship supported highlighting and accessible tabs
- `60b24cb806a8f6eb1b6f8f6cb1cce41d9525cd81` servers/ruby: prepare and package client documentation
- `8cf1b9cd82692ca50ce1b5c2575933be19132c24` clients/php: reap the native fixture process
- `48fb0ce8816f2f06cfccac0c2eec333cab3f629b` servers/ruby: retain dynamic acceptance failure evidence
- `74a91e8dee502390860ee2c211ec0e68b67ba69f` clients/python: resolve described routes from API origin
- `150bc74e4dbb87ba1d6b6e0a1cb7032c8bcda9fa` clients/js: resolve described routes from API origin
- `4ee83c0f44200ec5fb1f36f438b971ba24c9c331` clients/js: regenerate the client bundle and declarations
- `b64fb25bea8d8222fb3263b99956c0b61438a859` Version 0.30.0

## Evidence and handoff

All new exports use `go-query-final-*`: receipt, identity, fullseries/diff/names/
stat/status, commit map, old→new and pre-fold range-diffs, empty fold-tree diff,
exact semantic delta/names, update streams, remote proof, before/pre-fold ranges,
complete750 input proof and separate original310 Rust proof. Commit/fold hook
logs retain exact mandatory results. Earlier files were not overwritten.

No active Git/source/hooks/dependency/test/install/build/compile command remains.
Source/index clean and ownership yielded to lead for the same retained reviewer
general+architecture+scope gate. No broad check, build, acceptance retry, artifact
operation beyond prior authorized preservation, feature push or CI action here.
Lead owns shared state reconciliation and final execution; session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
