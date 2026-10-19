# Creation acceptance observations

A complete browser/native creation test can miss a settings reset if every
scenario selects the host default. In the session-creation initiative, the
packaged suite passed at 814568f, but live fork creation submitted high effort
and later reported the host default xhigh. Select a different root effort and
check both the saved roster and native thread after a real follow-up. A fork
has no initial destination message to restore settings after terminal startup.
Retain failed live evidence even when receipt readiness and conversation use pass.

For authenticated live browser checks, establish credential access before
launching Chromium. A local read of the root-owned portal password failed with
EACCES before the driver's cleanup scope and left the browser alive. The test
now reads privately through the already verified root SSH target, keeps the
value only in process memory, and starts Chromium afterward. Verify the actual
read method without printing the credential. Use a known verified SSH target;
short host aliases can have a different known-host identity.

Run Ruby session selectors through test/dev_session_test.rb. Its split files
share fixture constants loaded by that entrypoint; running a split file directly
can produce NameError before any relevant assertion. The corrected focused run
for fork and terminal-provider behavior passed 26 tests/275 assertions in 10.815s.

Existing conversation settings live in a modal popup. A packaged test initially
waited for the hidden effort selector and timed out after all creation/fork/plan
checks passed. Open Edit Codex settings, select the value, and click Save before
checking native settings. A selection alone changes the dialog draft. Assert the
real settings POST and the effective native value; do not force a hidden control.

Evidence: work/2026-10-19-session-creation-end-to-end/state.md, live fork artifacts
and creation-ci-814-evidence/. The final correction passed independent review, the complete packaged suite
at ea650c34, and actual default/alternate/team/fork/plan creation with completed
follow-ups and saved/native settings proofs.

Systemd template links alone do not repair package switching: systemctl may
leave a direct `workspace-codex-provider@NAME.service` instance alias and its
`default.target.wants` entry pointing into an old Nix store package. A dangling
instance shadows a valid stable-profile template and reports LoadState=not-found.
The bounded live repair replaced those exact aliases with stable profile/local
template links, then daemon-reloaded and started the worker; its original
provider operation completed. Runtime host activation now repairs existing
managed aliases and enablement links, with collected-package regression coverage.
The final packaged VM passed the seeded collected-package regression; actual
post-activation instance and enablement links resolve to the selected package.

Root conversation clients explicitly override conversationPath to
`/api/sessions/SLUG`; retained-member clients use `/codex/conversations/...`.
The full36006b0 browser test saved settings successfully (POST200 and rendered
xhigh) but incorrectly waited for the other route. Preserve actual request logs
and check the client construction before asserting network paths.

For an archive-extracted flake below /tmp, use an explicit `path:/tmp/DIRECTORY`
URI. An unrelated /tmp/.git makes `.#...` search upward and try invalid
`git+file:///tmp`; that setup error occurs before build and proves nothing
about the browser regression. Leave the foreign Git entry untouched.

An accepted plan preserves its raw text and hash, while the derived initial
CLI goal strips ASCII boundary whitespace through normalizedCreationGoal. A live
proof incorrectly expected the raw trailing newline in the derived goal. Compare
the exact canonical derived goal and journal hash separately from the captured
raw plan/hash; the read-only correction then passed against the same fixture.

Normal dev-session deletion requires a real interactive terminal. Piping a yes
answer fails before lifecycle admission. For explicitly authorized disposable
fixture cleanup, use a PTY, verify the exact session prompt, and answer normally;
do not replace the confirmation with a private helper or force flag.
