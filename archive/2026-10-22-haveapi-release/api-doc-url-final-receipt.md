# Mounted URL correction and cleanup: final source receipt

Implementer0 owns serialized Git/index/hooks. Actual client implementation belongs
to implementer1(JS) and implementer2(Python), following the architect-owned
api-doc-mounted-url-contract.md and lead grants. Source changes are HaveAPI only.
Lead directly completed user-facing documentation/errors/CHANGELOG prose.
No integration, release branch/tag, registry or deployment permission is implied.

## Trigger, correction and compatibility

All10 CI runs at published27b4f8f8 succeeded (api-doc-ci-status.json). Its local
release/build/full component/package smokes passed, but installed dynamic callback
token-challenge acceptance failed against the actual mounted fixture. That result
is retained as a failure, not relabeled success. Real descriptors already include
the API mount/version; JS and Python duplicated the mount when joining to an API
base. Server routes and emitted descriptors are correct and unchanged.

JS now resolves strict descriptor paths from the origin. Internal async
RequestContext.pathMode distinguishes descriptor flows from existing API-relative
public AsyncClient.request/discovery behavior. Public RequestSpec unchanged;
actions/auth/state share the existing pipeline, URL validation and OAuth trusted
origin exception remain bounded. No prefix heuristic, guessed version or retry.
Python's shared request core explicitly selects descriptor mode at origin root,
validates static route before binding encoded IDs, retains destination origin/
mount restrictions before credentials/transport, and leaves discovery/base
normalization unchanged. Both sync/async facades use this core. State.py,
transport/provider APIs and package/version/lock inputs are unchanged.

Root mounts retain URLs; mounted servers already publish the right contract.
Applications manually fabricating/caching API-relative descriptors must refresh
from actual OPTIONS. Raw JS requests remain API-base-relative. No server upgrade,
coordinated deployment, protocol/schema/database migration or persisted format is
needed. Rollback restores prior packages and their known mounted-path bug; it
cannot undo API actions. Actual installed acceptance remains after final review.

## Independent PHP cleanup and diagnostics

PHP test launcher proof: proc_open String tracked a shell; native stop/reap left
Ruby's listener and inherited pipe alive despite PHPexit0. Changed exactly the
launcher plus actual socket-closure regression to native argv and stderr redirect,
removing nonexistent redirected pipe2 setup. Before/after exact owned PID/starttime
proofs and native cleanup are api-doc-php-launcher-before.json/after.json and
api-doc-php-launcher-receipt.md. Before probe's owned Ruby child required TERM;
after native Ruby PID was reaped/listener closed/remaining_owned[]/cleanup[].
No PHP client/runtime/protocol changes. Lead exact source/prose acceptance retained.

Separate dynamic acceptance diagnostics preserve stdout/stderr before failure,
keep existing-token and challenge logs separate, trace only method/path/status,
and exclude headers/query/body. No server route/description normalization or
fixture simplification. Diagnostic source5/0 specs/style3 accepted; PHP focused
1test/2assertions2.401s/syntax2files/style2 accepted. Both separate source commits
ran declared hooks and will receive same-reviewer affected-lane assessment.

## Owner and final assembled quick evidence

Python exact8 paths committeddef95703: shared request.py, client/core/query tests,
new mounted URL and pure Rack descriptor tests, README/CONTRIBUTING. Owner364
unit+Rack tests passed4.55s; Ruff38 formatted/lint clear; mypy18 source files clear.
No listener/package install or long acceptance. Mandatory PythonChecks/I18n hooks
passed at commit; no bypass.

JS authored exact9 paths committedd59ba3e4: protocol.ts, async/request.ts,
async/client.ts, mounted_paths.spec.cjs, path_construction.spec.js,3 JS docs and
new Rack dynamic_mounted_paths_spec.rb. Generated exact3 paths5b1dd07c came from
npm run build. No manual generated edits. Owner compatibility39/39 (new10 native
mounted cases), async39/39, resources11/11, two emitted type configs +source
check, selected Mocha11/0, actual Rack/diagnostic6/0 and Ruby style/diff pass.
Crossrealm VM fixture artifact was corrected through the real XHR JSON boundary,
without a production runtime deviation or changed actual server paths/responses.
All authored/generated exact-path commit hooks passed.

Necessary assembled quick ran exactly once after owner source yield:

`HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euo pipefail -c 'make test-documentation test-documentation-python; make release-check; git diff --check'`

JS declared build4.55s produced unchanged tracked artifacts; documentation78
examples/0 failures (seed50064,15.42s), highlighter/fallback and keyboard/ARIA tests
passed; explicit native Python5/0 (seed8295,8.03s); metadata valid0.30.0 and diff
whitespace clean. No unaffected native unit suites or long packages repeated.
Final source consolidation is tree-preserving; only required amendment hooks,
metadata/whitespace/state evidence follow, without rerunning these quick suites.

## History and update-stream disposition

Published verified predecessor is27b4f8f895a4e5401357a402187c2a4590699aec,
basea32b15e379f44fc6dae4b15ef4ec17a142e5f465. Original release08345b2 and
review607941c0 proofs remain untouched. New api-doc-url-final-* exports only.
Before consolidation05bf78563d2eb0fa92a64437977dfde0ff153670 tree
fed8aea303bb91eb488c4c4bbc639356a7488c21 includes all intended source and4 lead
CHANGELOG lines. Fresh SSH target check confirmed mastera32b15e and remote feature
27b4f8f8. No remote mutation during preparation.

Retained local session-only refs under refs/dev-session/2026-10-22-haveapi-release/
preserve release-baseline08345b2, doc-reviewed607941c0, verified-core27b4f8f8,
and url-before-consolidation05bf7856. They are not tags/default/release refs and
are not pushed. Exact mapping is api-doc-url-final-before.json.

Keep authored callback helper and mounted URL fix as distinct meaningful source
changes. Consolidate old659ede0f helper generation +new5b1dd07c URL generation into
one final cumulative bundle/declaration commit after both authored features.
No obsolete generated0.30 payload retained solely for earlier feature publication.
Final generated output remains separate from the Version literal delta. PHP
cleanup, diagnostics and Python correction remain separate meaningful purposes.
Four lead-only CHANGELOG lines fold into the exact final Version0.30.0 commit.

Existing Node declaration pin, highlighter pin/build/license, PyPA pin, shared CI
action roles and coherent shared0.30 version/dependency lock streams remain one
update each. No new dependency input/lock/version stream. Three released server
maintenance -x provenance patches retained exactly. No database/state migrations,
no new externally consumed/deployed candidate, no default history rewrite.

## Verification boundary and next action

All new source requires the same retained reviewer affected4 lanes: URL/public
raw-vs-described semantics, origin/credential safety, encoded binding, actual auth/
action/state paths and fixture fidelity; native PHP process cleanup and diagnostic
privacy; full consolidated history/streams/no migrations. This is a real new
runtime contract correction, not automatic reuse of capability-limit review.
No long retry or feature push until that review and lead direction.

Original12 baseline artifacts08345b2 and12 verified-core artifacts27b4 are retained
by lead in separate session directories with SHA inventories; currentdist empty.
No package rebuild or artifact move by implementer0. Prior green CI/old artifacts
cannot validate final source. Installed npm/Python wheel+sdist mounted challenge,
action/state acceptance and exact-head release checks remain after final review.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/

## Final identity, equivalence and source handoff

Final base `a32b15e379f44fc6dae4b15ef4ec17a142e5f465`; head `ee150c8515aae399dc14e0fe9daefeb95a8bb17e`;
tree `fed8aea303bb91eb488c4c4bbc639356a7488c21`. Pre-fold05bf7856 tree and complete binary aggregate diff equal
final. Clean consolidation had no conflicts/source choices.24 intermediate
commits became22 logical commits; first13 exact hashes retained. Original and
new generated updates became one cumulative5-file bundle/declarations commit
`71c22cd8515882906e3d0b24c7a967dc7ba3ed15`, after both authored helper and mounted URL fixes. Final metadata
and4 approved CHANGELOG lines are exact last `Version 0.30.0`, no body.

Every rewritten logical source/metadata commit ran mandatory declared amendment
hooks through temporary message files. All passed, no bypass. Advisory width
warnings do not exceed required80 maximum. No manually edited generated output.
The full27-path delta from prior27b4f8f8 is only accepted cleanup, diagnostics,
Python/JS correction/tests/docs/output and CHANGELOG. No Go/Rust/server route/
fixture semantics/dependency/version input changed in this followup. Three
maintenance exact patch/message/-x provenance commits remain unchanged.

Full22-commit series:

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
- `5ee08c92 servers/ruby: document maintained dynamic clients`
- `8947b16a servers/ruby: ship supported highlighting and accessible tabs`
- `cb41affb servers/ruby: prepare and package client documentation`
- `e503dec6 clients/php: reap the native fixture process`
- `0c33fcc3 servers/ruby: retain dynamic acceptance failure evidence`
- `3b04b728 clients/python: resolve described routes from API origin`
- `d03428a3 clients/js: resolve described routes from API origin`
- `71c22cd8 clients/js: regenerate the client bundle and declarations`
- `ee150c85 Version 0.30.0`

Complete new exports: api-doc-url-final-identity.json, series.txt, diff.patch,
names.txt, stat.txt, status.txt, commit-map.json, range-diff.txt (prior27b4 range),
fold-range-diff.txt (prefold range), semantic-delta.patch/semantic-names.txt,
before.json/before-series.txt/before-diff.patch. Original prior inventories and
review/verification receipts remain untouched. All fixups and intermediate JS
payload revisions removed; independent source/cleanup/diagnostics purposes and
migration lineage preserved. No migrations.

Final metadata check valid0.30.0, full-range whitespace clean. Tracked source clean/index empty; only preserved generated PHPcache/__pycache__ untracked. All owner commands/edits yielded; no source/Git/hooks/install/check operation pending. Exact portal comparison captured basea32b15e/head ee150c85. New stream table api-doc-url-final-streams.md and fresh SSH observation api-doc-url-final-remote.txt complete. Git/index/hooks/source ownership yielded to lead NOW for same-reviewer affected4lane review. No feature push or long retry; currentdist remains empty, prior artifacts untouched.
