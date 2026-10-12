# Final HaveAPI 0.29.9 release review

Outcome: release the accepted missing-documentation fix on the supported 0.29
line. User explicitly approved HaveAPI/master merge and release on 2026-10-12.
Master fix ed88e2a is now integrated. Backport delivery is committed and pushed.

Session 2026-10-11-diagnose-vpsadmin-api-exception; workspace /home/aither/workspace/ai/vpsfree.cz; retained reviewer0 Astra/xhigh/read-only,
ready and independent; no override/fallback. Verify exact binding first.
Read workspace AGENTS.md and routed procedures, release worktree AGENTS.md,
mandatory-change-review skill and all four lane references. Cover general,
architecture/repetition, scope/proportionality, risk/compatibility directly;
no nested reviewers, source edits or long/write-producing tests.

Repository HaveAPI, worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-diagnose-vpsadmin-api-exception/haveapi-release, feature branch 2026-10-11-diagnose-vpsadmin-api-exception-haveapi-0.29.
Target origin/haveapi-0.29. Base 22fae15809b37e66ffea53a1162544e6321d09ab; head 784e113c216b16586c482e710ee4a0e0a04e6f8e.
Complete series:
b2dd423cb326ac7192bb95a8d42232db52f417ac servers/ruby: ship shared documentation in release gems
4b781a01f13476ba28432cfa7bafa0ecebd83926 ci: update shared Ruby workflow actions
784e113c216b16586c482e710ee4a0e0a04e6f8e Version 0.29.9

Final diff: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-11-diagnose-vpsadmin-api-exception/release-final.diff. Plan/state/design under /home/aither/workspace/ai/vpsfree.cz/work/2026-10-11-diagnose-vpsadmin-api-exception.

Functional b2dd423 cherry-picks 8053a22 with provenance; runtime/tests/build
apply cleanly. The release branch predates separate instruction procedures,
so two modify/delete documentation conflicts were resolved by preserving its
inline AGENTS layout and transferring only the new build/test instructions.
Mechanical 4b781a0 cherry-picks ed88e2a action majors with provenance. Workflows
are byte-identical to reviewed master files, whose latest official action
versions and actionlint were already checked. Version/changelog metadata is
separate (784e113), generated with normal make version VERSION=0.29.9.

No superseded approaches/fixups/unused compatibility paths. One shared version
stream, one update of each workflow action; no repeated pins or lock streams.
No migrations/schema/persisted-state changes anywhere in this complete series;
merge/release/deployment/external-use migration provenance is inapplicable.
Require explicit whole-branch history, consolidation and migration conclusions.

Acceptance: make release generates all five shared docs before packaging;
direct Rake build rejects absent/empty docs; clean Bundler evaluation works;
extracted framework serves all three documentation URLs and asserts its source
location. Child preserves resolved Gem paths across unbundled env, even with
empty original gem home. Missing JSON file ->404/no mail; EACCES->500/mail.
Existing public action/client protocol, database, daemon, NixOS options and
rollback state unchanged. Old/new API nodes interoperate; no node coordination.
Risk high conservatively for public error behavior and irreversible publication.
Owner HaveAPI; actual consumer vpsAdmin source ~>0.29.6, package0.29.8; planned
consumer update after publication. No downstream code or deployment in this
release review. User handles deployment. PHP mirror synchronization is a separate
repository operation required by normal release procedure, to be prepared before
its own master integration approval; unchanged PHP API merely shares version.

Quick checks at this exact versioned tree before metadata commit: 20 focused
examples,0 failures (3.42s); five Ruby files lint clean; Ruby syntax clean;
normal Overcommit hooks passed for all three commits; diff --check passes and
checkout is clean. Version metadata is consistent and registry latest0.29.8;
0.29.9 tag unused. Logs: release-quick-checks.log, release-version-commit.log.
Previously reviewed master has full355 specs and seven exact-head CI passes.
Long release checks remain deliberately pending: full server suite, make release,
actual dist gem extraction/route and registry artifact checks, exact release CI.
Do not treat master's results as the release branch's full verification.

Documentation checked/changed: inline AGENTS build/release guidance and
CHANGELOG Ruby-server section; temporary rollout evidence stays in session.
No client behavior added, no extra changelog component claims. JS npm install
reported17 preexisting dependency audit warnings; no dependency metadata updated.
Review all findings by severity with concrete paths/lines/commits, residual gaps.
