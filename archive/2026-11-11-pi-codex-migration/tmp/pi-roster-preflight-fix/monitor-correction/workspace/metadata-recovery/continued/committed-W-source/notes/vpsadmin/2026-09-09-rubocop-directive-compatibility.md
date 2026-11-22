# RuboCop directives across component shells

During work/2026-09-09-ip-release-mechanism, API-shell RuboCop autocorrection
rewrote an RSpec/AnyInstance suppression to `rubocop:disable-next`. The root
Overcommit shell has an older RuboCop that does not understand that directive,
so the commit hook failed despite the API lint passing.

Use an inline `# rubocop:disable RSpec/AnyInstance` on the affected call, supported
by both versions, and run root hooks before committing. Verified by successful
hooks on the final prerequisite/API/WebUI series. Avoid rerunning API autocorrect
over these directives without checking the root tool's output.
