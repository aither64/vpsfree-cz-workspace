# Final HaveAPI master review packet

Requested outcome: fix Go token documentation String/Symbol wire-name false
mismatch, integrate master, then backport 0.31 and release next patch. This
review covers the complete committed master fix milestone only.

Session 2026-10-28-token-auth-compatibility; records plan.md/state.md/design.md;
worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-token-auth-compatibility/haveapi.
Repository git@github.com:vpsfreecz/haveapi.git, target master.
Base 2fc2b8f86c71a6062434bb60a24e174b20c1a520.
Head 2f5156262baaf137800c17a9321e617c2b5df1d5.
Complete series: one commit, clients/go: match String and Symbol token transport names.
Final diff: 4 files, 73 additions/1 deletion, all under clients/go.
Read actual git diff and series. Functional comparator and its regression tests
are inseparable, no release metadata in this commit. No obsolete approaches,
follow-up fix commits, repeated input/dependency/generated streams, or migrations
(merged/released/deployed/externally consumed inventory empty).

Acceptance: exact supported String/Symbol names match both directions; actual
automatic mounted profile proves saved JSON String versus live Symbol and emits
SetExistingTokenAuth. Different header/query names independently, unsupported
scalar names and missing provider/descriptor remain rejected. Basic/OAuth2
unchanged. Non-goals: actual request auth, global copying/defaults, other renderers,
SDK regeneration, downstream pins/deployment, general validation framework.

Quick evidence: pre-fix 77 examples/8 expected failures and mounted check reproduces
original warning; fixed focused unit suite 77 examples/0 failures; pure mounted
profile check passed; RuboCop 4 files/0 offenses after formatting correction;
git diff --check passed and clean committed worktree. Logs go-unit-red.log,
go-profile-red.log, go-quick-green.log, go-lint-green.log in session. Hooks enabled.

Documentation: local code comment explains JSON String/Symbol boundary; existing
client guide inspected. No separate public guide needed for internal matching
correction. Later patch CHANGELOG is separate milestone. No dependencies/pins
change. Owner is HaveAPI Go generator documentation adapter; consumers are mounted
HaveAPI documentation profiles in Ruby server (real fixture test), generated SDK
runtime is unchanged. No state/protocol/schema/CLI/Terraform changes; independent
upgrade/rollback safe. No deployment in this session.

Risk high conservatively for auth metadata compatibility; actual request
authentication untouched. Lanes: general; architecture and repetition; scope and
proportionality; risk and compatibility. Selected retained independent reviewer0,
gpt-6.1-sol/xhigh, ready/read_only, thread 01a1819c-2087-7e82-ba00-70dedf8cdf0d.
Read /home/aither/.codex/skills/mandatory-change-review/SKILL.md and all four
applicable references, repository/workspace guidance. Perform review yourself,
no nested reviewers. Assess scope first and explicit whole-history/migration
conclusion, including no migrations and no repeated update streams. Return findings
with severity or no findings plus residual gaps. Write review-master.md in session.

Pre-publication message-only amendment: original unpushed 26dbf899 replaced by
2f515626 solely to wrap commit body for Overcommit. Lead git diff --quiet confirms
identical source trees. Review final message/head above. Final hooks pass.
