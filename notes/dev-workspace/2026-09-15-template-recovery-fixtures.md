# Session creation recovery fixtures

- Initiative: `work/2026-09-15-session-documentation-review/`.
- Workflow: focused `test/dev_session_test.rb` creation-retry checks.
- Symptoms: a plan-only retry failed with missing state; a complete legacy
  fixture then reached an unsupported `capture` call on `NullTmux`.
- Cause: existing-directory creation retry validates both plan and state, while
  `NullTmux` models inspection rather than full terminal creation.
- Fix: provide both predecessor-template files. Use the suite's established
  deliberate exception at `create_tmux_session` to prove startup reaches the
  intended boundary, then assert the seeded records. Use an appropriate managed
  tmux fixture for tests that need to finish terminal startup.
- Verification: legacy creation recovery and seeding checks passed (4 runs,
  34 assertions) without loosening production recovery rules.
