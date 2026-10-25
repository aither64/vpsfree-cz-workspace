# Go request-envelope correction: final source handoff

Final head `ee67d27419c48d27a01c83a29114adf9a82062ba`, tree `2e0d29769aff48b484c1ac331b11255d22abd0ae`; base
`a32b15e379f44fc6dae4b15ef4ec17a142e5f465`. Prior reviewed/executed head `3fb91caf783eaeacf49bf3647b8409d536339d71`.
All intended source is committed, tracked source clean and index empty. No active
Git, source, hook, dependency, test, build or install command remains. Source and
Git ownership are yielded to lead for the same retained reviewer's general,
architecture and scope gate. No actual Go retry or feature push was performed.

## Accepted correction and quick evidence

Lead directly accepted owner2's exact two-file harness-only correction and inline
comment. Actual metadata-bearing SDK actions already send `_meta: {}`; expected
object, hostile and three authenticated bodies now match that established wire
envelope. The actual strict verifier is unchanged. Metadata-free empty/omitted
actions retain exact metadata-free expectations. No generator, renderer, runtime,
API, schema, dependency, lock, generated payload or project documentation change.
The adjacent comment carries the only useful lasting explanation.

Owner2's `package2-go-wire-fix-receipt.md` retains exact command, diagnosis chain
and yield hashes: actual verifier accepts 7 valid bodies and rejects 52 mutations;
both Ruby syntax checks pass, RuboCop inspects two files with zero offenses, and
tracked/new-file whitespace checks pass. All owner commands had exited before
Git ownership transferred. No owner check was repeated by implementer0.

Both yielded SHA-256 values matched before staging and after consolidation:

- `e7b00cea79eda9454f4b3bd45ebf4571cebcda7c418e5a501f60722eff140324` — `clients/go/spec/documentation_acceptance.rb`
- `2f46589e99a712801710a0c8f5f46f25d98cfb9375db45b46cc2cf2c7d1e5946` — `clients/go/spec/documentation_wire_check.rb`

Exact paths were hook-committed as temporary fixup
`ea6d33a902449ec453f0f6536f4e670c91df9151` through a temporary message file in the
top-level tools-only Nix shell. Declared HaveapiI18n/RuboCop and commit-message
hooks passed. Width warnings were advisory; no bypass was used.

## History, equivalence and streams

The fixup was folded only into the existing Go source purpose. The series retains
22 logical purposes, exact first ten hashes and all released maintenance `-x`
provenance. Twenty-one other patches are byte-for-byte and stable-patch-ID equal.
The final metadata patch and exact one-line message `Version 0.30.0` are unchanged
and last. Every rewritten logical commit ran mandatory amendment hooks from a
temporary message file in the declared top-level tools-only Nix shell. Final
metadata hooks include HaveapiI18n, PythonChecks, PhpCsFixer and RuboCop; all pass.

The complete pre-fold `ea6d33a9` tree and binary base-to-head diff equal the final
tree/diff. There was no conflict or source decision during folding. Whole-range
whitespace is clean. Prior reviewed3fb91 → final semantic delta is exactly the
accepted two Go harness/verifier paths. No migrations exist; prior accepted
whole-branch migration conclusion is unchanged by this test-only delta.

`go-wire-final-streams.md` inventories every logical update stream. No new
repeated stream was introduced. The single cumulative generated JS update stays
after its authored features and before coherent final shared version metadata.
Original source refs, reviews, logs, inventories and artifact receipts remain
untouched. Retained local refs preserve reviewed3fb91 and pre-foldea6d33a9.
Fresh SSH pre-fold master was a32b15e and feature3fb91, recorded in
`go-wire-final-remote.txt`; no remote mutation was performed. Portal comparison
was captured explicitly for the final exact base/head.

## Prior execution and complete input identity

`go-wire-final-input-equivalence.json` compares the complete original749-entry
tracked input inventory against final750 entries: 748 mode/type/blob identities
are unchanged, one existing harness changed and one new verifier control was
added. Entire server, JS, Python, Rust, Ruby-client, workflow and release-tool
source groups, plus Nix/toolchain/configuration inputs, match. All nine live
resolved dependency-lock contents match their actual3fb91 artifact manifest.
Original tool identities and manifest SHA are retained in this proof.

Dynamic installed npm/wheel/sdist success and all ten CI successes remain bound
to their actual source3fb91; they are not relabeled as successor-head executions.
`go-wire-final-rust-input-equivalence.json` separately proves all original310
tracked Rust execution inputs from48543 plus flake.nix/flake.lock still match.
Original successful915.38-second dev/MSRV execution and generated tool/Cargo
receipts keep their actual48543 identity. No Rust or dynamic retry was performed.
Final-head artifact rebuild, actual Go compile/run and final-head CI remain
separate lead-authorized completion work after final independent review.

All12 exact3fb91 artifacts, including hidden `.gitignore`, remain retained under
`verified-core-artifacts-3fb91caf/`. Before/copy/source/preserved SHA inventories
and manifest source match; `dist/` remains literally empty. Original failed Go
assertion/compilation logs and successful dynamic/Rust results are preserved.
Unrelated PHP result cache and release Python cache remain untouched.

## Final series

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
- `277c931a1b3fd90c26003634b1ae7df4d1c3e932` clients/go: render SDK documentation from saved profiles
- `c274b1ddce99b97a12645a385424b6cdc97555fe` clients/rust: render SDK documentation from saved profiles
- `8ea86b33bcf730fcbfcf0eb427bde8cd4c2f1cac` clients/js: add typed action lookup
- `cde580bfa9332a43ad996b10e0a9d1d900a2e437` servers/ruby: document maintained dynamic clients
- `76d302a1b1a232bb27d72e018f76d5cccc8ca70a` servers/ruby: ship supported highlighting and accessible tabs
- `360900f558b93e342c3cec8c0a82106f38aee197` servers/ruby: prepare and package client documentation
- `a55709c4f7cfafee78830fe5caf34dbca192b265` clients/php: reap the native fixture process
- `2c4294d2fe58b40cd8c16612fdb78baf4d315218` servers/ruby: retain dynamic acceptance failure evidence
- `668e70af8d65e2f07f53b2500056ff45c3f65b53` clients/python: resolve described routes from API origin
- `01cb7bd8e44ec6a3bb19d12122f8b32bc8cb99d8` clients/js: resolve described routes from API origin
- `7cf39c5ed70217f27000b7e0967e2bc1b312c3ea` clients/js: regenerate the client bundle and declarations
- `ee67d27419c48d27a01c83a29114adf9a82062ba` Version 0.30.0

## Evidence and remaining work

New exports only: `go-wire-final-identity.json`, complete `series.txt`,
`diff.patch`, `names.txt`, `stat.txt`, `status.txt`, `commit-map.json`, old→new
`range-diff.txt`, pre-fold→final `fold-range-diff.txt`, empty
`fold-tree-diff.patch`, exact `semantic-delta.patch`/`semantic-names.txt`, stream
inventory, before/pre-fold snapshots, complete input proof and original Rust
input proof. `go-wire-final-commit-hooks.log` and `go-wire-final-fold-hooks.log`
retain mandatory hook results. Earlier records were not overwritten.

Same retained reviewer general+architecture+scope gate is lead-owned and pending.
No default integration, tag, release branch, registry, session lifecycle,
artifact build/install, workflow launch, publication or long retry occurred.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
