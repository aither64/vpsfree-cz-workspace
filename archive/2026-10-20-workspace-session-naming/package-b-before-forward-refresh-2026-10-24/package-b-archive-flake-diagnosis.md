# Archive VM failure at B 4c6b9f1

Read-only diagnosis of `verification-dev-workspace-flake.log` and the failed
derivation at B `4c6b9f177d5b205b21b45880c6ac1bc3c403eef6`, with A
`4300c40b6406161afc74c124c40155f28a557032`. No test, build, model request or live
runtime operation was executed. No application source changed.

## Observed failure

The immediate failure is page initialization, before archive submission:

- Log `:8927`: browser phase `open page`, no recorded page errors; the session
  page, static assets and `/codex/assets/conversation.js` return HTTP 200. The
  recorded list contains no operation-status response or archive POST.
- Log `:9032–9033`: Playwright's 30-second `waitForResponse` times out at
  `test/archive_lifecycle_browser.cjs:31`. That predicate waits for the initial
  GET `/api/sessions/<slug>/operation`; confirmation and POST start only later,
  at helper `:46–55`. The failed-run immutable helper
  `/nix/store/b2grg67qrpxsvjr1d2f6klrrfbd6c56m-archive_lifecycle_browser.cjs`
  is byte-identical to the inspected source.
- Log `:9062`: the browser command exits 1. Log `:9093–9098`: the diagnostic
  search prints no archive journal. No archive worker failure or data loss is
  established; the test had not exercised archive/revive yet.

`portal/internal/web/static/app.js:1211` awaits the conversation module before
binding page controls; its initial operation read is at `:3776`.
`codex-web/conversation/assets/conversation.js:1–10` statically imports other
modules. None of those child-module responses appears in the browser's ten
recorded responses. This narrows the visible progress to module loading/page
initialization, but does not prove exactly where execution stalled. The saved
events record response headers, not request start, body completion, import
resolution, browser console diagnostics or timing. An HTTP 200 alone does not
prove complete transfer/evaluation.

## Earlier portal stop timeout

The SIGKILL at log `:7518–7525` occurred while package registration restarted
the service. The `2min 51.100s` text is the service's reported wall lifetime;
the journal shows the stop request at 17:27:12 and forced termination at
17:29:42 (`:9082–9089`). It is not the browser's archive timeout.

The replacement portal listened at `:7614`; registration completed at `:7609`,
service readiness checks and setup completed by `:7650`, and explicit CLI
session/worktree setup succeeded at `:7690` and `:7728`. The later browser
received the page and assets. Similar registration stop timeouts appear in the
concurrent recovery and creation VMs (`:7469`, `:7753`). The shutdown delay is
real, but these records do not establish it caused the later browser stall.
Its underlying cause is outside the evidence available here.

## Baseline and naming attribution

Read-only Git comparison from B base
`bf6d4b0c49600c15e17fe71248807ef43424e932` to exact failing B confirms no changes
to the archive browser helper, archive VM, `static/app.js`, session template,
lifecycle target/operation code or `libexec/workspace-host`. The base used A
`ea64ef57fdd2`; its `conversation/` tree is unchanged through final A4300.
A's production changes are confined to `codex/ephemeral.go`; other A changes
are tests and documentation.

The archive fixture creates an explicit slug with
`dev-session start ... --as-is --no-codex --no-attach`
(`nix/tests/session-archive-lifecycle.nix`, `fixture` function), and the browser
fails before any lifecycle mutation. Automatic naming was not exercised in
this path. There is no source/evidence basis for changing the naming fix to
address this failure. Unchanged source alone does not prove the baseline VM
would pass or that broader packaging/environment effects are impossible.

## Missing evidence and smallest next step

The failed output path
`/nix/store/g0vycq0s2lapq54qnm14pycaxdjxfbp5-vm-test-run-dev-workspace-session-archive-lifecycle`
exists but is empty. No matching retained failed-build temporary directory was
present. The fixture only prints service journals/archive journals on failure;
it did not retain a browser trace, network completion timings or screenshot.
No defensible exact cause or behavioral correction follows from these records.
Slow scheduling/import transfer and browser/module failure remain hypotheses.

Smallest useful follow-up for the lead/implementer decision: improve bounded
failure diagnostics in the existing `test/archive_lifecycle_browser.cjs` only.
Record monotonic times for request start, response headers, request finish and
failure; include resource type and path, bounded console errors, pending paths,
document readiness and available resource timings. Record `page.goto` completion
separately from the operation response. Bound failure-time page evaluation so
an unresponsive page cannot hide the original error. Retain a small trace or
screenshot in the existing VM output if those records are insufficient.
Do not record credentials, authorization headers or response bodies with user
content. Preserve the operation-read readiness assertion and archive semantics.

After the required review gate, the watcher can run the targeted
`nix build --no-link --print-build-logs .#checks.x86_64-linux.session-archive-lifecycle`
with these diagnostics. This would collect missing evidence; a timeout increase
or unchanged blind rerun is not a demonstrated fix. Any product change should
follow the resulting causal evidence, through the lead.

## Other outcomes in this full-flake run

`verification-packages-result.json` records collection exit 0 (21.324s), A flake
exit 0 (51.977s), and B flake exit 1 (920.303s). The creation VM completed only
its installation subtest at full-flake log `:7933`, then began the first custom
provider/attachment/follow-up scenario at `:7934`. Its final retained line is
`:7945`; no scenario completion or native naming success/failure is recorded.
No creation acceptance or native-naming result may be inferred from this run.
