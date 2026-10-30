# Portable Ruby validator fallback assertion

Committed sidecar `266dcb1852c8bac8735af684ce48380d2851a658`, tree `cd482cb5b5dddf58dd97a68bde32af7baa1fe12d`, above reviewed/published
`35c1fb964735639c0873aacf078e18569f05f9bc`. The exact delta is one line in
`servers/ruby/spec/documentation/validators_spec.rb`; committed bytes equal the
checked bytes. Source/index are clean. All 2148 protected current
input/evidence hashes remain unchanged. No application or package input changed.

Ruby3.2/3.3 CI reported the accepted Ruby fallback as escaped hash rockets,
while the test expected Ruby3.4's symbol-key display. The test now compares
`CGI.escapeHTML({ extra: false }.inspect)`. It retains the complete runtime
fallback, false value, escaping, Additional details and Ruby value labels.
No renderer behavior, fixture, workflow or dependency was changed.

Focused declared-Nix validator suite: 11 examples, zero failures, seed18544;
scoped lint: one file clean. Actual ordinary pre-commit HaveapiI18n/RuboCop and
all commit-message hooks passed without warnings. `quick.log`,
`commit.final.log`, exact `one-path.patch`, temp message, checked hash and
`result.json` retain evidence. No older Ruby was installed locally; the next
published CI matrix must prove the actual3.2/3.3 result. Nix substituted missing
paths of the declared shell; no component install/resolution or lock change ran.

The first temp-message preparation failed its own width assertion before
writing/staging. A subsequent mistakenly-started commit passed empty-index hooks
then exited128 for missing message file; HEAD/index were inspected unchanged
and reported before known local message correction. `commit.log` retains that
failed attempt. It is separate from the successful committed hooks and tests.
No successful check was rerun to hide a product failure.

No push/fold/rebase, preview/API/browser/TLS/private/peer/default merge/release or
lifecycle action occurred. All prior failing CI/source/review receipts remain
untouched. No command or watcher remains active; source/Git/utility ownership
is released to lead for the separately owned final-history continuation.
