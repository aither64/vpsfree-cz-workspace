# Go documentation consumer VCS correction: final source receipt

Bounded lead-owned three-file harness correction after the first actual Go
consumer build failed on ancestor VCS discovery. Implementer2 owns source,
regression, documentation and focused verification; implementer0 owns serialized
Git/index/hooks. Lead directly accepted exact source/test/prose and owner yield.
No generator, renderer, product runtime, API, dependency or lock change.

## Cause and correction

A disposable Go consumer can discover an unrelated ancestor Git directory and
fail VCS status discovery before compilation. Its generated test programs have
no source repository history to stamp. The harness now builds that consumer with
explicit -buildvcs=false, retaining the tested HaveAPI source/artifact identities
in the existing verification receipts rather than ambient repository metadata.
No global GOFLAGS, ambient /tmp/.git or other caller Git state is modified.

The existing build argv is owned by one small harness-only build_command method.
The actual acceptance and the new native dry-run check consume the same argv.
The check creates its own invalid Git ancestor and minimal consumer, uses -n/-x
without running a compiler, and proves the flagged plan succeeds without Git
status discovery. Its same-argv unflagged control must fail VCS discovery at that
exact owned ancestor. Offline/toolchain constraints remain unchanged. No skip,
automatic install, listener, generated SDK or full acceptance is involved.

Exact three application paths:

- clients/go/spec/documentation_acceptance.rb
- clients/go/spec/documentation_build_check.rb
- clients/go/docs/documentation.md

Owner receipt package2-go-vcs-fix-receipt.md retains full commands and yielded
SHA-256. All three contents matched those hashes before staging. Native positive
and unflagged negative controls passed, dedicated activated-bundle preflight
passed, both Ruby syntax checks passed, style inspected two files with zero
offenses, tracked/new-file whitespace checks clean. Lead prose wording preserved.
No owner broader check was repeated by implementer0.

## Commit, history and review boundary

Exact three paths committed as temporary fixup fa409240. Mandatory I18n/RuboCop
and message hooks passed without bypass (advisory width warnings only, <=80).
Fold into existing Go owning purpose only, keeping 22 meaningful subjects and
exact final one-line Version 0.30.0. First ten hashes and released maintenance
provenance stay unchanged. No new dependency/channel/generated stream; one
cumulative JS payload and separate metadata stream remain as reviewed.

Fresh pre-fold SSH fetch/ls-remote: master a32b15e379f44fc6dae4b15ef4ec17a142e5f465,
feature 48543f8cd254eb0fc087931a5dc98ea730fd94af. No push or shared default mutation.
Full new exports use go-vcs-final-* only; original source reviews, execution
receipts, CI and artifacts remain untouched. No migrations or product contract
change. Same reviewer general/architecture/scope gate is required before a new
actual Go compile/run acceptance. This dry-run does not prove full acceptance.

## Prior verification and artifact identity

Both installed dynamic wheel/sdist/npm acceptance and independent Rust dev/MSRV
acceptance passed at exact 48543f8c, not the later final commit. The original
Rust execution remains bound to its 915.38-second run and retained generated
Cargo/source/tool evidence. The 310 tracked repository input inventory is
rust-documentation-inputs-48543f8c.json; final blob equivalence proof is exported
separately. Input equality is not a claim of literal execution at the new head.
Exact tool/Nix/input graphs remain in the original MSRV/readiness and execution
receipts; no Rust rerun requested or performed here.

All 12 exact 48543 dist entries, including .gitignore, are preserved in
verified-core-artifacts-48543f8c. Before/copy/after SHA equality and manifest source
proof are in its -sha256.json and -preservation.json. dist is literally empty.
Earlier 08345b2/27b4/ee150 artifacts, failed Go logs, successful dynamic/Rust logs,
refs and source receipts are retained. No cleanup, install, artifact build, long
retry or feature push performed. Final-head artifacts/Go acceptance/new CI remain
future lead-authorized work after review.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/

## Final exact identity and clean handoff

Base `a32b15e379f44fc6dae4b15ef4ec17a142e5f465`; prior reviewed/verified head `48543f8cd254eb0fc087931a5dc98ea730fd94af`;
final head `3fb91caf783eaeacf49bf3647b8409d536339d71`; final tree `8698b4a7b707b2c165877931071d31505f346370`.
Prefold `fa409240308cde895d6d02a0f45c934faec91be1` tree and complete binary base-to-head diff equal
final. No rebase conflict or source decision. All 22 purpose subjects/order
remain; first ten hashes exact. Twenty-one stable patch IDs remain equal, only
Go owning purpose changes. Exact three Go paths comprise the semantic delta.
Final metadata patch is unchanged, exact last one-line `Version 0.30.0`.
All rewritten logical commits ran mandatory declared amendment hooks using
message files without bypass. Full-range whitespace/state proof follows.

All 310 recorded tracked Rust inputs match their original mode/type/blob at
48543 and final. Original inventory SHA and every old/final object are exported
in go-vcs-final-rust-input-equivalence.json. flake.nix/flake.lock blobs also match;
original immutable tool graphs remain retained separately. This source-input
proof preserves the identity boundary and does not relabel old execution as a
literal final-head run. No Rust test, compiler or actual Go acceptance rerun.

Complete final series:

- `b3a6a0b1 release: include the Rust generator in shared releases`
- `5b5f0c25 servers/ruby: validate structured API examples`
- `dda40adb servers/ruby: syntax-check generated client examples`
- `9c4c8a7c servers/ruby: render nested PHP example values`
- `878509d5 release: cover Rust publication and publisher setup`
- `1e810107 release: update PyPA publishing action to v1.14.3`
- `f50c540d servers/ruby: remove unmaintained filesystem examples`
- `4337f1a6 servers/ruby: add request-local client documentation context`
- `b495832d servers/ruby: render filtered client documentation panels`
- `593fac92 clients/js: add Node 24 types for documentation acceptance`
- `cb21d5ce clients/go: render SDK documentation from saved profiles`
- `7c106a0d clients/rust: render SDK documentation from saved profiles`
- `1b508c48 clients/js: add typed action lookup`
- `ed0e4f2e servers/ruby: document maintained dynamic clients`
- `77e74892 servers/ruby: ship supported highlighting and accessible tabs`
- `731653ca servers/ruby: prepare and package client documentation`
- `9e456de1 clients/php: reap the native fixture process`
- `857d5a89 servers/ruby: retain dynamic acceptance failure evidence`
- `5b7f68d1 clients/python: resolve described routes from API origin`
- `397286a5 clients/js: resolve described routes from API origin`
- `9c0cd9b4 clients/js: regenerate the client bundle and declarations`
- `3fb91caf Version 0.30.0`

Full new exports: go-vcs-final-identity.json, series.txt, diff.patch, names.txt,
stat.txt, status.txt, commit-map.json, prior/fold range-diff, semantic-delta.patch/
semantic-names.txt, before.json/before-series.txt/before-diff.patch, Rust input
proof and this receipt. Original review/verification/CI/artifact files untouched.
No migrations or new update stream. Final review general+architecture+scope and
lead-authorized final-head artifact/Go/CI completion remain separate gates.

Final required hooks all passed, including final I18n/Python/PHP/Ruby checks. Full-range whitespace clean; metadata patch and exact last message unchanged. Full stream disposition table is go-vcs-final-streams.md. Fresh pre-fold target remains a32b15e, feature48543; exact portal comparison captured final3fb91caf.

All three owner paths tracked clean, index empty; known generated PHPcache/__pycache__ preserved. No Git/source/hook/setup/test/install command pending; source/Git/hooks yielded to lead now for same-reviewer general+architecture+scope review. Dist is literally empty, old artifacts/logs/refs and the original310 inventory untouched. No Rust rerun, full Go acceptance, build, push, CI launch or workflow edit. Lead's later build-only release dispatch planning creates no action here.
