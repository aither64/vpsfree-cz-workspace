# Follow-up verification and deployment

Implemented and deployed on 2026-09-12 to aitherdev through the normal user
profile switch. All four feature branches remain open and unmerged.

## Exact deployed source

| Project | Feature head |
| --- | --- |
| codex-web | de83e9c72dec6cb5ff8ec13d5b0b21ed60148117 |
| dev-workspace | 820277e6cc3aa7ff9acb0396feb3314e7f84996a |
| vpsfree-dev-workspace | ee9c55b3c25fd0b0002b3ce4796167d27378cd3a |
| workspace | 082c4c920f80ac8ef882bb59647bada4324094ce |

Profile 30: `/nix/store/8a2c8nbpkfig5vc71jl5ir4wbxpxqkpr-dev-workspace-0.2.0`.
Profile 29 remains available as the previous deployed package. Codex 0.154.0 is
unchanged. Router, portal, Codex and tmux user services are active. No system
configuration or default branch was changed for deployment.

`workspace-host switch --source <initiative>/workspace` passed its ordinary
package-generation, runtime/cluster and Codex contract preflights. The live
portal executable and all four repository heads matched the candidate.

## Reviews and local verification

All four mandatory review lanes used fresh gpt-5.6-sol reviewers with xhigh
reasoning. Every Blocking and Important finding is resolved; two bounded API/
retention advisories are accepted with reasons in follow-up-review-reconciliation.md.
The unmerged runtime series was reconstructed into dependency order and proved
source-identical to the reviewed fixes. Its final tree is
`19a507d97a5cce1a51490807a7ddf4fab853d550`. Intermediate backend stages compile;
cache, durable restore and batching stages pass focused race tests.

Quick checks passed before long integration: provider Go/shared contracts,
runtime full Go suite with GOWORK=off, browser units, seven packaged editor tests,
fifteen strict-CSP Chromium component checks, and committed-range whitespace
checks in all four projects. Component checks cover bounded mounted editors,
lazy syntax assets, split/unified/full-file syntax, old/new anchors and hidden
context, Back/Forward, immutable branch identity, file-version normalization,
clipboard, statistics/status, responsive layout and read-only behavior.

The generic runtime, organization and site workspace each pass
`nix flake check --print-build-logs`. The generic host-module idempotency VM passed
in 193.93 seconds using a substituted kernel. The exact final site package also
builds successfully. Runtime Ruby suites report 296 runs/2,979 assertions and
73 runs/438 assertions, with 12 and 3 declared environment-dependent skips;
organization migration reports 43 runs/825 assertions with 1 skip. There are no
failing checks. No local kernel build was needed.

## Conversation browser acceptance

The exact packaged application and its real HTTP handlers passed isolated
Firefox 155/Selenium 4.40 acceptance in 15.90 seconds with controlled Codex RPC.
The test submitted two steers through the actual composer, verified immediate
receipts and same-tab reload without resending, rejected same-text/wrong-ID and
same-ID/wrong-digest observations, and retired only exact canonical matches.
Three deliberate acknowledgement failures plus reload did not resurrect the
receipts, and the actual acknowledgement retry cleared both attempts.

Native clipboard tests preserved original Markdown; denied clipboard access
showed an accessible recoverable error. SVG copy/check icons and labels passed.
The completed turn showed "Waiting for instructions" and advancing waiting time.
This check used a 1440x1000 desktop viewport and a controlled RPC authority;
responsive repository checks are separate. The private fixture/processes were
removed. Curated results and three screenshots are in artifacts/follow-up/.

## Live service measurements

The same deployed service was measured directly and through authenticated HTTPS
with certificate verification. All requests returned 200. These are request
measurements, not complete browser-load or cold-OS-cache claims.

| Operation | Samples per transport | Direct | HTTPS |
| --- | ---: | ---: | ---: |
| Health | 3 | 2.14 ms | 541.37 ms |
| Registered repository state | 5 | 24.98 ms | 429.20 ms |
| Four repository states | 3 | 28.53 ms | 438.61 ms |
| Four initial histories | 1 | 87.02 ms | 1,016.09 ms |
| Branch and first file preview | 1 | 102.12 ms | 402.99 ms |
| First commit open | 1 | 78.58 ms | 388.14 ms |
| Repeated commit open | 2 | 18.28 ms | 384.19 ms |
| Four visible files | 1 | 70.68 ms | 356.37 ms |

Values are medians where multiple samples exist. Registered metadata improved
from the recorded 615.8 ms direct baseline to 24.98 ms, a 95.94% reduction, exceeding
the 75% target. HTTPS authentication/proxy/TLS overhead remains visible even for
health; this is not a 95.94% improvement in total user-perceived page loading.
The complete observations and exact executable are in follow-up-latency-results.json.

Authenticated live smoke verifies TLS, unauthenticated 401, healthy service,
Messages default, counters, the new worker and copy/waiting assets with no-store
headers, and the exact existing conversation identity. No live conversation
messages or Git refs were changed by these checks.

## CI

All final feature-head workflows passed:

- [codex-web 34707084076](https://github.com/aither64/codex-web/actions/runs/34707084076)
- [dev-workspace 34708694751](https://github.com/aither64/dev-workspace/actions/runs/34708694751)
- [organization 34708731240](https://github.com/vpsfreecz/dev-workspace/actions/runs/34708731240),
  including the development-cluster check, completed 17:46:55 UTC.

The site workspace has no matching Actions workflow. No superseded queued or
running feature-head workflow remains.

## Compatibility and limits

The new fields, endpoints and private exact-comparison descriptors are additive;
canonical session/lifecycle formats and authentication are unchanged. Native Git
remains the Git implementation. CodeMirror and maintained Shiki 4.4.3 are bundled
locally; no CDN, WASM, eval or diff2html is used. Private comparison descriptors
have no automatic expiry; missing Git objects produce an explicit unavailable
view and are not fetched or retained solely for links. Preview limits remain
512 KiB/12,000 logical lines, with bounded editors and syntax-worker resources.
The follow-up did not perform a live rollback or interrupt another session.

## Live repository browser

Actual Chromium acceptance passed against the live HTTPS portal and shipped
handlers. It verifies two repository columns, branch comparisons with syntax
colors, frozen URLs, full-file Before, a cold reload at old-L25, native full-hash
clipboard copying, the complete commit message, Unified, read-only editors,
a 390x844 viewport, and zero page errors or CSP violations. Root visually inspected
the desktop diff, full-file anchored line and mobile screenshots. The full commit
message is scrollable on short screens; the diff retains its own available area.

Two harness errors were diagnosed before acceptance: the generic .repo-grid
selector also matched Clusters, and the chosen newly added Go file had no Before
version. The corrected test scopes the repository panel and selected file, and
uses modified server.go. Neither failure required a product change. The retained
script is follow-up-live-browser.cjs and results are in
artifacts/follow-up/live-browser-results.json.

## Cleanup and handoff

The detached reconstruction worktree and private conversation authority were
removed cleanly. After acceptance, root removed 22 remaining owned temporary
files/directories and GC roots, including ignored node_modules/dist, after
checking that no fixture/browser process remained. Curated evidence is retained
here. All four registered feature worktrees are clean and remain available, as
do their branches and the installed profile. The initiative stays active and
open for user review; no integration or archival was performed.
