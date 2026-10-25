# Python rendered login correction: final source receipt

Scope follows api-doc-python-login-contract.md and the lead's bounded execution
grant. Implementer1 owns the renderer, harness and regression source; implementer0
owns the one-line Makefile wiring and all serialized Git/index/hooks. Lead directly
accepted source, visible prose and the guide. No runtime, JS, URL, server schema,
provider default, dependency, version or lock change is included.

## Cause, behavior and regression fidelity

The installed wheel no-token branch failed at reviewed ee150c85 after successful
core/build/package checks. The actual token request requires lifetime. The shared
login field helper excluded it because JS supplies its own lifecycle choice;
Python intentionally forwards caller values to native validation. This is a
renderer input omission. The failed acceptance/logs remain retained as failures.

The shared accessor now returns the advertised request parameters; its existing
JS-facing selection still applies the same exclusions. Python alone merges every
advertised required initial-login field into its prior selection. Lifetime and
required interval therefore use the existing HAVEAPI_AUTH_* JSON environment
convention; optional lifecycle input stays omitted. Existing-token bypass and
challenge-owned continuation token handling are unchanged. No invented initial
or continuation token, schema change, client default or optional interval input.
The harness provides JSON "fixed" as an explicit choice from the unchanged enum.

The supplemental native test consumes real unchanged Rack token metadata and AST
extracts both rendered Python begin_token_login mappings. Native parse/build_request
accepts explicit lifetime at the exact mounted route with no interval; removing it
produces the exact lifetime required-field error before transport. The validator
is real, with no handwritten replacement mapping or network listener. Ordinary
controls cover required interval, existing TokenAuth bypass and continuation-token
exclusion. The new native file stays outside ordinary spec discovery.

Exact six owner paths are recorded in package1-python-login-receipt.md; the seventh
path is Makefile. test-documentation-python invokes dynamic_python_login_spec.rb
beside the existing protocol spec with unchanged prepared Python prerequisites.
No test installs dependencies, skips missing environments or expands CI discovery.

## Accepted checks and hooks

Owner focused checks: 16 examples, zero failures, seed 47466, 3.02 seconds;
RuboCop five Ruby files, no offenses; diff whitespace clean. Source/prose accepted
by lead. No additional factual-fidelity gate delayed the implementation.

Exactly one required assembled command ran after source yield:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euo pipefail -c 'make test-documentation test-documentation-python; make release-check; git diff --check'
```

Passed: 79 documentation examples (seed 18197, 14.03 seconds), both highlighter/
keyboard asset checks, seven native Python examples (seed 49331, 9.12 seconds),
valid shared 0.30.0 metadata and clean whitespace. JS rebuild produced no tracked
change. No owner broader suites, full component/package/build or installed long
acceptance was repeated. Final tree-preserving fold needs only required amendment
hooks and metadata/whitespace/state evidence afterwards.

Exact six-path dynamic fixup bda2376d and one-path orchestration fixup 7792846a
ran declared hooks from temporary message files. All I18n/RuboCop/message hooks
as applicable passed without bypass. Fold them into their existing two purposes,
retain all 22 subjects and exact final one-line Version 0.30.0.

## Artifacts, provenance and verification boundary

All 12 exact ee150c85 dist entries, including .gitignore, are preserved under
verified-core-artifacts-ee150c85. Manifest source verified; before/copy/after hashes
match. Proof and inventory are verified-core-artifacts-ee150c85-preservation.json
and verified-core-artifacts-ee150c85-sha256.json. dist is literally empty. No
artifact, original failed acceptance/log, previous review, worktree or ref cleanup.
Older 08345b2/27b4 artifact sets and receipts remain untouched.

This new required-auth-input correction needs the same reviewer's affected four
lanes after all intended source is committed. Prior URL review does not cover it.
No Python client runtime/JS/server schema/default compatibility change and no
protocol, database, persisted-state or migration change. Deploying corrected docs
needs no runtime upgrade; rollback restores defective examples, not stored state.
No publication/default integration, feature push or long retry authorized here.

Final full history/diff/equivalence/streams and old ee150c85 semantic delta use
NEW challenge-final-* exports only. Prior exact reviewed refs and provenance stay
retained. Lead owns final review assignment, next exact-source artifact build and
installed wheel/sdist challenge acceptance; this receipt claims no such success.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/

## Final identity, consolidation and source handoff

Base `a32b15e379f44fc6dae4b15ef4ec17a142e5f465`; prior reviewed head `ee150c8515aae399dc14e0fe9daefeb95a8bb17e`;
new head `48543f8cd254eb0fc087931a5dc98ea730fd94af`; new tree `d240b01bc06f9a240e08f74452fc2700a795a0f1`.
Prefold `7792846af9f31fb841d637bb4789b45ffd8f41ee` has the same tree and identical complete binary
base-to-head diff. Fold had no source/behavior conflict. All 22 subjects/purposes
retain their order; first 13 hashes stay exact. Only dynamic/orchestration edit
sets change; the other 20 commit edit sets remain identical. The commit map
also records stable patch IDs and raw diff equality so context/index shifts in
later overlapping diagnostics are explicit. Complete prior-to-final source delta
is exactly the seven accepted paths, no runtime/JS/schema/default or generated
change. Final metadata patch/message remains unchanged and exactly last
`Version 0.30.0`, with no body. All rewritten logical commits ran declared
amendment hooks through temporary message files without bypass.

No new dependency/channel/generated update stream. One cumulative JS generated
payload remains after its two authored source features; final version metadata
is separate. Existing Node/highlighter/action pins and shared locks unchanged.
Three maintenance provenance commits and their exact source patches/messages
are retained. No migrations, stored-state/format/protocol or deployment lineage
change. Earlier failed acceptance/build artifact identities remain retained.

New exports only: challenge-final-identity.json, series.txt, diff.patch, names.txt,
stat.txt, status.txt, commit-map.json, range-diff.txt, fold-range-diff.txt,
semantic-delta.patch/semantic-names.txt, before.json/before-series.txt/
before-diff.patch and this receipt. Old ee150 URL receipts are not overwritten.
Retained local session refs preserve ee150 and the full pre-consolidation head.

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
- `4479c930 clients/go: render SDK documentation from saved profiles`
- `d97fc57d clients/rust: render SDK documentation from saved profiles`
- `9dcc036d clients/js: add typed action lookup`
- `9b7d6670 servers/ruby: document maintained dynamic clients`
- `ccf35513 servers/ruby: ship supported highlighting and accessible tabs`
- `94246292 servers/ruby: prepare and package client documentation`
- `1ced32a4 clients/php: reap the native fixture process`
- `95de406f servers/ruby: retain dynamic acceptance failure evidence`
- `cf1bed08 clients/python: resolve described routes from API origin`
- `526fa210 clients/js: resolve described routes from API origin`
- `56ebccfe clients/js: regenerate the client bundle and declarations`
- `48543f8c Version 0.30.0`

Post-fold required hooks all passed, including final I18n/Python/PHP/Ruby checks. Metadata check valid 0.30.0; full-range whitespace clean. Twenty stable patch IDs match the prior reviewed range; only the dynamic and orchestration patches differ. Final stream table is challenge-final-streams.md. Fresh pre-fold SSH target remained a32b15e and remote feature ee150c85, retained in challenge-final-remote.txt. Exact portal comparison captured final base/head.

Tracked source clean/index empty; only preserved generated PHPcache/__pycache__ untracked. All owners yielded source, no command/edit/Git/hook/setup/test/install operation pending. Git/index/hooks/source ownership yielded to lead now for same-reviewer affected four-lane review. Dist stays literally empty and preserved artifacts/logs/refs remain untouched. No push, build, long retry or cleanup action.
