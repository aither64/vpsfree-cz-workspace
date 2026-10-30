---
lifecycle: archived
---

# 2026-10-29-haveapi-security-review

## Status

- Second corrected-head re-audit is complete against exact published head
  `aee093cd3387c261570067e58b7f1e16029e3619`, tree
  `295f884f0b2a8257883e82197fad3d8821c251ca`, direct parent
  `a3f522e509faaf9da34d9e87c7f7e9246c76bd6c`.
- All seven unchanged VULN-01 through VULN-04 exploit cases reached their fake
  local clients but created no marker. The positive contracts preserve exact
  argv/request JSON and visible hostile response text while commenting every
  physical response line. No remaining or new security issue was locally
  confirmed in this bounded pass.
- Corrected-head independent re-audit is complete against exact published head
  `ddf836fbb33ec6f920c3edfd9a4a53c2c2eb494b`, tree
  `30efb19e02a756036771767745a9858fe968f95b`, direct parent
  `ae46cf27a9afb6558d386c293cec7231dd6c423d`.
- The four original VULN-01/VULN-02 exploit cases no longer create markers, and
  the corrected renderers preserve exact argv/JSON semantics. No security
  regression introduced by the direct-parent shell-safety patch was confirmed.
- Two additional Medium findings were locally confirmed at the intermediate
  corrected head `ddf836fb`:
  a pre-existing Ruby CLI-help example injection (VULN-03), and a pre-existing
  mixed request/response shell block whose one-click copy exposure was introduced
  by the original documentation redesign (VULN-04).
- Independent solo audit complete at exact published head
  `ae46cf27a9afb6558d386c293cec7231dd6c423d` (tree
  `27dcf148f9b03867a3dfc65a29c76e77a87682ec`) against base
  `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`.
- Two Medium security findings are locally confirmed. Both are pre-existing
  shell-injection flaws in executable documentation examples; neither was
  introduced by the audited five-commit range.
- No introduced security regression was confirmed in the requested server
  documentation, OAuth/session, authorization/filtering, cache/browser/parser,
  or generated-client boundaries.
- HaveAPI tracked source is unchanged in all three worktrees. Four original untracked
  evidence files remain below `VULN-01`/`VULN-02`; four corrected-head evidence
  files exist below `VULN-03`/`VULN-04` in the re-audit worktree.
- No fix, commit, publication, merge, deployment, or lifecycle action was
  performed. This session remains active and open as requested.

## Phase checklist

- [x] Session/thread/provider/model/effort verification
- [x] Scope, design, and verification brief
- [x] Exact-head isolated worktree and repository instructions
- [x] Five-commit change and trust-boundary analysis
- [x] Local validation of material leads
- [x] Findings/coverage reconciliation and handoff
- [x] Deployment (confirmed out of scope; not performed)
- [x] Readiness for use (audit report and local reproductions available)
- [x] Corrected-head exact-source worktree and delta inventory
- [x] Original four PoCs rerun and positive literal-preservation checks
- [x] Adjacent CLI-help formatter lead disposition
- [x] Corrected-head findings, coverage, cleanliness, and peer handoff
- [x] Second corrected-head exact-source worktree and eight-path inventory
- [x] VULN-01 through VULN-04 unchanged-PoC disposition
- [x] Response visibility/inertness, argv/JSON and Copy contract checks
- [x] Final findings, coverage, cleanliness, and peer handoff

## Historical findings and final disposition

1. **Medium — VULN-01: Ruby CLI documentation examples permit shell
   injection.** `ruby_cli.rb` emits the request-derived base URL and version as
   unquoted shell tokens and wraps request values in unescaped single quotes.
   Both a request value and base URL executed synthetic marker-file payloads
   through a temporary fake `haveapi-cli`. Classification: pre-existing at the
   comparison base. **Verified fixed at `aee093cd`.** Evidence: HaveAPI worktree
   `vulnerabilities/VULN-01/{report.md,poc_spec.rb}`.
2. **Medium — VULN-02: curl documentation examples permit shell injection.**
   `curl.rb` puts JSON in a double-quoted shell token, leaving command
   substitutions active, and ad hoc single-quotes URLs without escaping quote
   breakouts. Both paths executed synthetic marker-file payloads through a
   temporary fake `curl`. Classification: pre-existing at the comparison base.
   **Verified fixed at `aee093cd`.** Evidence: HaveAPI worktree
   `vulnerabilities/VULN-02/{report.md,poc_spec.rb}`.
3. **Medium — VULN-03: Ruby CLI help examples permit shell injection.**
   `clients/ruby/lib/haveapi/cli/example_formatter.rb` inserts remote action
   example values into a copyable command with ad hoc double quotes, leaving
   command substitution active. A fake `haveapi-cli` PoC executed the marker
   payload. Classification: pre-existing and unchanged from the original base
   through `ddf836fb`. **Verified fixed at `aee093cd`.** Evidence: re-audit worktree
   `vulnerabilities/VULN-03/{README.md,poc_spec.rb}`.
4. **Medium — VULN-04: copied shell examples execute response sample data.**
   The documentation combines executable Ruby CLI/curl requests with raw
   response transcripts, and the Copy control copies the complete block. Both
   real renderer paths executed response-value substitutions with fake local
   clients. Classification: the unsafe renderer sinks predate the comparison
   base; commit `51073383` introduced the one-click whole-block copy exposure.
   The first shell-safety fix did not address it; **verified fixed at
   `aee093cd`.** Evidence: re-audit
   worktree `vulnerabilities/VULN-04/{README.md,poc_spec.rb}`.

## Audited range and history

- Base is an ancestor of head; the range contains exactly five commits:
  - `51073383f063abbc24bf19ca669b9b6e46bb9555` — core documentation redesign
  - `78ab264add97495aa38ffb33800f16cc9870838d` — optional documentation OAuth
  - `2f6c18a80f3a5f8ce46449ff81183b100b60f34c` — performance contracts
  - `1b264e25a73a0ab9bca5f847bd52254f74e0931c` — client-example formatting
  - `ae46cf27a9afb6558d386c293cec7231dd6c423d` — formatting instructions
- Final range diff: 149 files, 11,757 insertions, 1,313 deletions; no database
  migration or persisted-state transition.
- `git blame` places the VULN-01 sinks in 2016/2024 commits and the VULN-02
  request sinks in 2016/2024 commits. The base-to-head diff changes token-login
  formatting but leaves the confirmed general request/base-URL sinks intact.
- Corrected head `ddf836fb` is one commit above `ae46cf27`; its four-path diff is
  207 insertions and 22 deletions. It changes the CLI/curl request renderers,
  adds focused shell specs, and documents complete-token encoding. There are no
  migrations or persisted-state changes.
- VULN-03 command/value construction dates to 2014 with later mechanical edits
  and is byte-identical between `f6e5c375` and `ddf836fb`. VULN-04's Ruby CLI
  and curl response sinks date to 2016, while its whole-block Copy control was
  added by `51073383` in the originally audited range.
- Final corrected range `ddf836fb..aee093cd` contains two commits and eight
  changed paths (268 insertions, 23 deletions). `a3f522e5` fixes client CLI-help
  token encoding; `aee093cd` makes Ruby CLI/curl response transcripts physical-
  line shell comments. There are no migrations or persisted-state changes.

## Coverage

- Documentation dispatch, root/version routing, slashless redirects, selector
  and search parsing, controlled errors, shared documentation, and no-store
  behavior.
- Optional documentation OAuth configuration, fixed HTTPS endpoints, PKCE and
  state, encrypted/purpose-bound cookies, origin and logout CSRF enforcement,
  bounded transport, explicit cookie-token validation, token conflicts, and
  ordinary API credential isolation.
- Per-version/current-user cleanup, hooks/locale restoration, authorization and
  parameter/example filtering, anonymous-versus-authenticated policy, and
  request-local context ownership.
- HTML/template/JSON/script escaping, hostile Host/login/sample values,
  highlighter-worker output, clipboard behavior, inert search-index parsing,
  content-derived search keys, ETag/key checks, and Cookie/Authorization/locale
  cache variation.
- JavaScript, TypeScript, Python, PHP, Ruby, CLI, curl, raw HTTP, Go and Rust
  example literal generation; full-snapshot versus current authorized action
  checks; parameter/schema compatibility; prototype-sensitive keys; finite and
  exact numeric limits; path/input/output shapes; error branches and formatting.
- Corrected-head coverage additionally traced every newly encoded CLI/curl
  dynamic token, exact argv order and values, JSON round trips, initialization
  and authentication examples, the Ruby client CLI-help formatter, the shared
  request/response composition path, and the browser Copy control's exact
  `textContent` selection.

## Verification evidence

- `make doc`: passed; generated documentation left tracked source unchanged.
- Initial targeted security run: 256 examples, 254 passed and two compiler
  checks failed only because fresh `clients/js/node_modules/typescript` was
  absent. After the repository-declared JavaScript dependency preparation, the
  identical targeted run passed: **256 examples, 0 failures**.
- Finding command from `servers/ruby`:
  `bundle exec rspec ../../vulnerabilities/VULN-01/poc_spec.rb ../../vulnerabilities/VULN-02/poc_spec.rb`:
  **4 examples, 0 failures**. The fake executables prevented network access and
  each case verified an injected marker file.
- `make test-documentation`: **395 examples, 0 failures**; bundled highlighter
  languages/fallbacks, tabs/accessibility, clipboard preservation, shared
  search display, strict projection, and lazy cache loading all passed.
- `make test-documentation-generated`: **19 examples, 0 failures**.
- `make test-typescript`: **63 examples, 0 failures**.
- `make test-rust-unit`: **161 examples, 0 failures**.
- `make test-go-cli`: **92 examples, 0 failures**.
- At `ddf836fb`, the unchanged original VULN-01/VULN-02 specs produced the
  expected **4 examples, 4 failures**: every failure was `ENOENT` for the marker
  after the fake client command ran, proving all four old exploit payloads were
  inert.
- Corrected renderer shell/syntax/detail/presentation specs: **43 examples, 0
  failures**, including exact NUL-delimited argv and parsed JSON preservation.
- VULN-03 from `clients/ruby`: **1 example, 0 failures**; the fake CLI marker was
  created from the displayed help example value.
- VULN-04 from `servers/ruby`: **2 examples, 0 failures**; response substitutions
  from both the Ruby CLI table and curl JSON transcript created markers.
- The first corrected-head `make test-documentation` stopped before tests because
  this fresh worktree lacked ignored JavaScript dependencies (`gulp` missing).
  After the declared `npm install --no-audit --no-fund`, the identical target
  passed: **404 examples, 0 failures**, with all highlighter, tabs, clipboard,
  search/projection, and lazy-cache asset checks passing.
- At `aee093cd`, unchanged VULN-01/VULN-02/VULN-04 server PoCs produced the
  expected **6 examples, 6 failures**, and unchanged VULN-03 produced the
  expected **1 example, 1 failure**. Every failure was `ENOENT` for the expected
  marker file after the fake executable ran; no payload executed.
- Final client CLI formatter regression spec: **3 examples, 0 failures**,
  including exact fake-executable argv for hostile action/resource/option/value
  tokens.
- Final server shell/syntax/detail/presentation/HTML specs: **54 examples, 0
  failures**, including LF/CRLF/bare-CR normalization, substitutions, backticks,
  separators, terminal backslashes, success/error transcripts, exact argv and
  parsed JSON.
- Final `make test-documentation`: **409 examples, 0 failures**. Highlighter,
  tabs/accessibility and real Copy/clipboard asset checks all passed; the copied
  transcript remains byte-identical to the visible complete safe block.
- `git diff --check` passed for `ddf836fb..aee093cd`; all six changed Ruby files
  passed `ruby -c` and RuboCop reported **6 files inspected, no offenses**.
- All checks used declared Nix/component environments. Environment setup fetched
  Nix caches and language packages only; no target/live/API/devcluster request
  was made and no credential was accessed.

## Identity and workspace evidence

- `dev-session current` repeatedly returned the bound slug
  `2026-10-29-haveapi-security-review`; the thread-bound absolute workspace and
  both `DEV_SESSION_*` values matched.
- Retained collaboration preset is solo with no team members.
- Native session metadata reports provider `openai`; native turn context reports
  model `gpt-daybreak-blue-latest` and effort `xhigh`. The refreshed local login
  reports `Logged in using ChatGPT`. No configured/native identity mismatch.
- Registered worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-29-haveapi-security-review/haveapi`,
  branch `2026-10-29-haveapi-security-review`, exact requested head/tree.
- Ordinary hooks were signed after the initial registered checkout encountered
  the repository's changed Overcommit signature. The declared server Ruby shell
  did not expose `overcommit`; the installed Overcommit executable signed the
  unchanged hook configuration successfully.
- Registered corrected-head worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-29-haveapi-security-review/haveapi-reaudit`,
  branch `2026-10-29-haveapi-security-reaudit`, exact `ddf836fb` tree
  `30efb19e`. Its unchanged Overcommit configuration was signed with the same
  installed tool after the checkout signature gate.
- Registered final corrected-head worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-29-haveapi-security-review/haveapi-reaudit2`,
  branch `2026-10-30-haveapi-security-reaudit`, exact `aee093cd` tree
  `295f884f`. Its unchanged Overcommit configuration was signed through the
  ordinary signature gate.

## Limits

- No external/live/devcluster request, real identity-provider exchange,
  credentialed request, production proxy/cache/browser matrix, or deployment was
  exercised. OAuth transport and browser behavior were tested with local
  synthetic doubles and repository asset helpers.
- The review followed the changed documentation/authentication/client-example
  boundary and related unchanged code. It was not a broad audit of unrelated
  HaveAPI subsystems, third-party dependencies, or deployed application policy.
- Anonymous documentation intentionally exposes the complete declaration set;
  authenticated documentation applies account filtering. That documented policy
  was assessed as policy, not treated as an authorization bypass.

## Next action

- Deliberately share the final no-finding re-audit result, evidence and limits
  with the approved owning session. No further source change is recommended from
  this bounded audit. This audit session itself remains open.
- Final re-audit result was sent to the approved owning session as message
  `b113b706-73fe-49f4-9bb7-69dd3c0d616c`; authoritative communication history
  reports `delivered`.

## Separate runtime-improvement session

- At the user's explicit request, created the separate Full-team session
  `2026-10-29-cross-session-communication-authorization` to assess and implement
  authoritative bidirectional communication-grant propagation. Its stored
  provider selection is Snajpa `codex-lb`, its `delegated` roster has the lead,
  architect, two implementers, reviewer, and observer ready, and its initial
  brief contains the observed failure, proposed design, security boundaries, and
  end-to-end acceptance cases.
- Stable portal:
  <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-29-cross-session-communication-authorization/>
- This does not grant that session access to this audit session's private
  records, worktree, transcript, or evidence and did not alter this completed
  HaveAPI corrected-head re-audit.

## Documentation and review policy

- No project documentation change is useful for this read-only audit. The
  session plan/design/state and untracked finding reports hold the rationale and
  evidence.
- Findings/evidence are audit records rather than application deliverables, so
  the automatic nested mandatory-change-review workflow does not apply.

## Cleanup

- All three HaveAPI worktrees have clean tracked source. The only untracked files are
  the eight intended reports/PoCs below their respective `vulnerabilities/`
  directories in the first two worktrees; the final corrected-head worktree has
  no untracked audit artifact because it produced no finding.
- All owned `make`, RSpec, npm, Nix, Rust and Go check processes exited. Unrelated
  processes belonging to other sessions were observed but not accessed or
  changed.
- No temporary fake executable or marker survived its RSpec temporary
  directory. Dependency directories and component-local ignored bundles remain
  as ordinary local test-environment state.
- Session must remain open. No archive/delete/stop or delayed cleanup is
  authorized.
