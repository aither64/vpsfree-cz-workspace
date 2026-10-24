# Library README and initial Cargo release review

User requested a library-user README inspired by vpsadmin-go-client and Cargo
publication when finished. Main-agent writing pass applied vpsfree-user-facing-writing
and humanizer-en. Compare with the Go repository README at its local bare HEAD.

Committed client delta: 62753f006d7bd3e5befe1033c49a2c630ca3ff02..
bfa960e31fddb49b371c2cf6d26b7886fdf8f57f, README.md only. Working tree/index clean.
HaveAPI remains 9e4c29a0412a25256ce944641f60ba13e9f03c2b, unchanged.
Client worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-rust-client-generator/vpsadmin-rust-client.
Go bare: /home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin-go-client.git.

Risk: low for this documentation delta. General lane only; no runtime/interface/
workflow/auth implementation changes. Prior full review and history addendum
remain applicable; inspect final complete base b67a3ba5eef89b2bd6533050aa8769aaa0574114
through new HEAD and state a history/migration conclusion for the docs follow-up.
Current series: handwritten f88d86a, generated 62753f0, user-requested docs bfa960e.
The docs follow-up is a separately reviewable user request after feature publication;
no repeated pin/generated/provenance updates, fixups or migrations are introduced.
No migrations were merged/released/deployed/externally consumed. Registry release
is upcoming; no default-branch integration is authorized. No source changes or
history rewrite are proposed. Prior reports final-review.md, final-review-delete.md,
final-review-history.md are preserved.

Acceptance: README leads with installation, public async use, authentication,
input updates/null handling, timeouts/errors and blocking usage; links examples
and API docs. Generator capture/inventory/wire encoding details removed from entry
page; maintenance docs retain saved schema/regeneration/release instructions.
Check correctness against committed builders/types/defaults, reader usefulness,
links including packaged/crates.io rendering, and no invented feature support.
Registry/docs.rs URLs intentionally target upcoming authorized 0.1.0 release.
No broad source rereview or long checks. Quick evidence: eight balanced fences,
TOML snippets parse, relative targets exist, complete Rust examples parse with
pinned rustfmt, git whitespace passes. Prior runtime/client/MSRV/integration/CI
all passed. Focused cargo publish --dry-run follows this final committed-doc
review; actual upload requires credentials (currently unavailable). User has
already authorized publication, not default merging. Read-only public crates.io
lookup currently returns 404 for the crate/version; manifest needs no changes.

Reviewer: retained reviewer0, saved gpt-6.1-sol/xhigh/read_only, thread
01a1508b-81fd-7ab2-b787-a7adb733a710. No overrides or subreviewers.
Write report final-review-readme-release.md with actual findings/severities or no
findings, residual gaps, complete-series/migration conclusion. No source/Git,
build/server/registry mutations, tests, long checks, or nested agents.
