# Risk and compatibility review

## Result

No Blocking, Important, or Advisory findings.

Reviewed the complete committed series:

- dev-workspace `e9ed544bf66ba8be07b4fca27aede6e6fd1bfe0a..df21f2ea8fe27efdb2cb8c0330fa31acd0f3a933`
- vpsfree-dev-workspace `916223fce1c5b7b78578ca8a16aaaa472c68b08c..89a03581b13056fa83114e592f2e2993e6a87887`
- workspace `f523eddf3e1d1cdebf445992318247030e11c7f3..1e01e557cac5527666d5b1e35fa52fadcdbb81af`

The implementation changes browser presentation and focus ownership only. It
does not change authentication, authorization, origin validation, session or
thread identity, request payloads, answer encoding, upload transport,
persisted state, schemas, operation journals, host commands, or lifecycle
behavior. Untrusted question content continues to be inserted with
`textContent`; the existing exact-origin and conversation/upload authorization
boundaries are unchanged. Moving the existing Interrupt element retains its
original listener and client call rather than introducing another mutation
path.

The composer remains mounted while hidden, so prompt drafts, attachment state,
and in-progress uploads are not converted or discarded. Pending snapshots
remain server-authoritative. Replacement preserves only local focus and draft
state keyed to the existing request and question identities; response failure,
disconnection, retry, automatic resolution, and successful removal do not add
partially committed application state.

The downstream dependency chain selects the exact reviewed runtime commit.
After excluding the expected revision, timestamp, and NAR hash fields, the
organization and site lock files are unchanged. All three feature revisions are
available from their SSH remotes. The shared codex-web revision and every
unrelated input remain pinned as before.

Deployment and rollback remain compatible. The session template is unchanged,
the existing generic `[hidden]` CSS rule supports the new JavaScript, and the
new CSS is cosmetic when paired temporarily with the old JavaScript. Existing
open pages may retain the previous presentation until reload, but both asset
generations use the unchanged server contracts. The portal applies
`Cache-Control: no-store` to responses, so a reload obtains the active profile's
assets. No persisted format is written, and the retained previous profile can
therefore be selected without migration or coordinated node updates. The
existing `workspace-host switch --source` generation, lifecycle, and
concurrency checks remain the applicable deployment controls; this change does
not alter them or require a system configuration change.

## Residual risks and test gaps

- The packaged long checks, feature CI reconciliation, profile switch, deployed
  asset-hash/health checks, and live browser smoke test remain pending by design
  until mandatory review reconciliation. They should be completed before the
  deployment is accepted.
- The Playwright regression uses the real portal server, TLS, CSP, SSE and
  upload handlers but controls thread and pending responses. It therefore does
  not exercise a live Codex App Server during this change. The residual risk is
  limited because no request schema, submission encoding, or provider revision
  changed.
- Old/new CSS and JavaScript combinations are reasoned from the unchanged
  template, the generic `[hidden]` rule, and no-store response policy rather
  than exercised as a separate automated rollback test. A mismatched pair can
  at most retain the prior composer layout or lose the new header cosmetics;
  it does not change data or mutation semantics.

## Evidence inspected

- `portal/internal/web/static/app.js`: composer/question/plan priority,
  Interrupt relocation, response focus recovery, and pending replacement.
- `portal/internal/web/static/style.css` and
  `portal/internal/web/templates/session.html`: hidden behavior, unchanged DOM
  contract, and responsive question layout.
- `portal/internal/web/question_browser_test.go` and
  `portal/internal/web/question_browser_test.cjs`, plus the recorded passing
  Chromium output: repeated snapshots, multiple blocking and asynchronous
  questions, failures, disconnect/retry, uploads, plans, Interrupt, focus, and
  constrained viewports.
- `portal/internal/web/server.go` and existing server tests: no-store headers,
  CSP, and exact-origin mutation protection.
- Both downstream `flake.nix`/`flake.lock` diffs, commit ancestry, clean
  worktrees, remote feature heads, and normalized lock-file comparisons.
