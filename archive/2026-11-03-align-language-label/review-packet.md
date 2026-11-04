# Final review packet

User asks to align the settings dropdown Language label with Theme/controls in
HaveAPI servers/ruby generated HTML docs. Acceptance: shared left edge, preserved
label association, native select submission, translations and other controls.
Session 2026-11-03-align-language-label; plan.md/state.md and
implementation-result.md in this directory provide scope/evidence.

Repository git@github.com:vpsfreecz/haveapi.git, target master.
Worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-align-language-label/haveapi
Base f29c1e4675bc1f79641faa619b8c68ecec923c71
Head b606b4b3c32bf05779c05babeaa1c31a33dee6fa
Complete series: b606b4b3 servers/ruby: align documentation language label.
Complete diff: documentation.css, 1 insertion/1 deletion; inspect full range.
No superseded approaches, follow-up commits, dependency/pin streams or migrations.
No release, deployment or external consumption of this feature.
One commit is the complete inseparable cosmetic correction.

Quick evidence: make doc; language_settings_spec 9 examples, no failures;
root-bundle RuboCop servers/ruby 206 files clean; git diff --check; all required
Overcommit pre-commit/commit-message hooks passed, clean worktree. See result.
No browser geometry check: ambient tooling absent, no dependency expansion.

Low risk: local reversible CSS, no persistence, API/protocol/client/config/pin
changes. Normal docs asset delivery; no deployment performed or authorized.
Non-goals: other menu redesign, JS/markup/prose/translations, new test harness,
API behavior, releases or deployment/integration.
Docs checked: README.md, doc/en/documentation-ui.md, repository instructions and
shared brand template. No lasting docs change useful for this margin correction.
Owner is HaveAPI HTML documentation renderer; this changes internal styling,
no shared interface.

Selected reviewer0, saved gpt-6.1-sol/xhigh and read_only, ready and independent.
Apply mandatory-change-review general and architecture lanes. Independently
conclude whole-branch history/migration disposition, no repeated update streams
if confirmed, and list any findings by severity.
