# Exact24ec CI coverage assessment

One metadata/jobs observation per listed run, attempt1, all completed at exact
`24ec424c9592951da38584379b43379b0c39f115`. Raw completed logs and artifact listings
are retained alongside; no poll/wait/retry/dispatch/cancellation or local check
ran. Source/index remain clean and2148 protected current input hashes unchanged.

| Workflow/run | Actual completed coverage | Reuse/remaining gap |
| --- | --- | --- |
| Performance40773074063 | All-client214/0; quick d67→24ec14cases PASS | Final all-client covered; direct f6→final still unstarted |
| Server40773074848 | Ruby3.2.11/3.3.12/3.4.11 each896/1; all3 assets pass | Matrix blocked by same test fixture; assets reusable |
| Release40773074364 | Metadata/checks236/0 +Python tooling6/0; make-test896/1 | No final complete build/package artifact; publication skipped |
| Rust40773074124 | Generator units159/15 seed62784 | Runtime/compiler/protocol acceptance skipped |
| JS40773074441 | npm build, compatibility/async/resources/type checks, Mocha50/0 | Actual JS workflow coverage reusable |
| Python40773074309 | Unit362/0 on3.11–3.15; integration61/0,5skipped | Unit/integration coverage reusable; skips retained |
| PHP40773074348 | PHP8.3/8.4 each52tests146assertions | Reusable;8.4 reports1deprecation |
| Go40773074596 | Ruby3.2/3.3/3.4 each100/0 | Adapter unit coverage reusable; no generated Go wire inference |
| Ruby40773074506 | Ruby3.2/3.3/3.4 each67/0 | Client unit coverage reusable |
| i18n40773074182 | rake i18n:health pass | Actual health check reusable |
| RuboCop40773074072 |420files,0offenses | Actual style check reusable |

## Final performance evidence

Artifact performance-40773074063-1 (id12853822745), downloaded once; ZIP digest
matches GitHub metadata:
`db2a64e137fc79fe4f80ee77c9b3807d20053d57658207ec9853badf13818692`.
selection.json/event/runner command select push before
`d67bebcb37f2d4558a97caa208465147da19dbef` → after `24ec424c9592951da38584379b43379b0c39f115`,
quick. Captured default f6 is not the measured baseline. runner.exit0 and
results/report.json status **pass**, all14 classifications pass, no failure or
inconclusive phase. Three baseline/self and five alternating pairs per case,
with pilot/calibration/adjusted evidence retained. This result covers d67→24ec
only; it does not satisfy the still-unstarted required direct f6→final pair.

Both native source manifests match Git exactly; each archived blob/hash/mode
and reported source-file hash was checked: baseline905/final908. Archive hashes
are `e47969682267a86abac3b3b5091cf473b58ecf1dd4fdb5d5959bd12b2c84c006` and
`8d76bba204178c3580a27a3cf6175314a3cab6614378453e5505ea2a7b29f352` respectively, matching the
existing retained exports. Final tree is
288376a727deb3905d2c368150543a6d7cfc0971; d67 tree remains
cd91bf06fd14d297aaa2470844f679f0998d85f9.
Nine actual input hashes and embedded benchmark manifest/lock/shell bytes equal
current final inputs. Budget hash remains57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050;
fixed reference remains b85ec364057f536940d689b09e612512ffffaf82.
Neutral fixture-map canonical digest/harness is
`e77c9353fc486d8f54f3fd7fe7d8515b7e52a3a7dcb767d013ce751ca634f831`; six actual neutral fixture/runner/comparator
hashes equal final source. Report's consumed samples SHA256 verifies as
`881a25d5ce1b777340c8ae3e0f4a3200265741ad83edebd51897e3e2ad4622ef`.
All19 process observations match the exact87-gem weekly calibration, including
io-console0.9.4/JSON2.21.2 and Ruby3.4.11 at the expected immutable7b77 Ruby path.
All recorded loaded-source hashes map to their own selected source; no graph
relaxation is inferred. Worker HTML outputs/counters preserve actual admin/member
identity and authorized overview shapes. CI paths are /home/runner/work/... and
/home/runner/work/_temp/haveapi-benchmark-gems, separately from protected local
inputs; equal gem identities do not identify those directories as the same store.

All-client log parses as210 unique direct records:15registry entries ×7kinds
×simple/thorough, plus registry/profile, real panel/admin-member-admin, resource
and action growth cases,214examples/0failures. Every recorded allocation/call
increment is within+32 (observed maxima1/
0); resource allocations2/4/8 are
[161667.0, 173717.0, 197843.0], action allocations2/4/8 are
[93532.0, 166587.0, 313024.0]; both2.5increment bounds hold.
Exact final spec bytes assert roles, declared group panels, no unrelated renders
and both dimensions. Actual job command runs that exact candidate under the
frozen benchmark shell. Standalone all-client has no separate activated-gem
receipt; do not claim the paired87-gem process receipt was that process.
A benign Nix search-path diagnostic precedes fallback to existing Bash in that
log; the actual214/0 command completed. No local duplicate all-client needed for
this exact source/input contract.

## Concrete failures for narrow owner fixes

Server matrix and release fail solely
servers/ruby/spec/documentation/client_examples_spec.rb:66,
“passes mounted version-aware URLs and stable canonical action data into
renderers”. It stubs Go available?/render without configuring a profile;
new capability query calls context.profile.adapter (go_client.rb:17), yielding
nil. Trace reaches server.rb293/example_panels. This diagnoses a stale fixture
capability boundary; no production backdoor/fallback is proposed here. Preserve
all current URL/schema/sample assertions when adapting that fixture.

Rust159/15:13 documentation_factory_spec unsupported-source cases still expect
“invalid Rust SDK source”; actual error is accepted “invalid Rust API client
source”. Two documentation_performance_spec unavailable-provider cases expect
“authorized Rust SDK profile”; actual says “authorized Rust API client profile”.
All15 observed failures are wording expectations; do not relax work/visibility
checks. Later Rust formatting/compiler/protocol steps were skipped, not passed.
Release stopped in server make-test and retained no new release artifacts.
Existing local focused package proof remains its actual narrow scope, not a
replacement for failed complete release CI.

Server-assets step executes all3 highlighter/tab/documentation Node targets and
reports actual passes. JS workflow includes strict callback/async TypeScript
checks and runtime tests; Python integration is real-server transport coverage.
No standalone generated Go/TypeScript/Rust wire acceptance or supplemental
Python documentation-encoder target is inferred beyond the explicit job commands.
Required uncovered work: narrow fixture/Rust expectation fixes and affected
checks/publication/final head assessment; full package/build; skipped Rust
compiler/protocol and other explicitly required installed/wire acceptance;
single direct f6→final quick. No source edit or execution is authorized by this
assessment. Lead decides next packages and actual scope after fixes.

All original evidence/exports/failures preserved; source/Git/hooks/dependencies,
services/browser/preview/provider/TLS/peer/lifecycle untouched. No active owned
command or utility. Browser capacity was not occupied. Quiet.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
