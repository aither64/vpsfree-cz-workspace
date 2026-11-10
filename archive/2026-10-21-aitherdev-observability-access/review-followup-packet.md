# Focused final-review follow-up: actual omfile creation permissions

Session2026-10-21-aitherdev-observability-access; worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-21-aitherdev-observability-access/vpsfree-cz-configuration.
Base 38e7c837893695999e588a73f5d2a0088b8257b1; frozen head d07b4251172020472b21e8830e92b023849d543f; clean tree, intended changes committed.
Complete updated series ready-series.txt and full ready.diff. Exact delta from
previous tested head 5d910028d32ce9305dc8161c51b3ed17ec4179bb: logger-permission-fix.diff and .range-diff.
Prior full four-lane review review.md at072f7e01 remains authoritative for unchanged
components. Reviewer0 retained gpt-6.1-sol/xhigh independent/read-only; no overrides.

## Reason and scope

Actual VM found expected file but new dirs root:root0700/current root:root0640,
so positive SSH reader predicate failed. Globals did not control RainerScript
remote omfile action. Architect approved minimal explicit6 per-action owner/group/
mode fields; keep legacy local messages defaults and Umask, destination/template,
inputs, pipe, HUP/rotation and accepted read-only boundary unchanged. See design.md
clarification and logger-permission-diagnosis.md. Scope is four files+35/-7:
production action params/comment, quick assertion/syntax stub, stronger VM fresh
creation assertions, contextual prose clarification (lead checked).

## Evidence and acceptance

Native mapped real-GID probe01/02 PASS: globals reproduce incorrect metadata;
explicit action gives ALL fresh dirs UID0/GID1000750 and files0640; localmessages
same group0640; markers/exporter retained. Probe02 DISTINCT pipeGID200 remains0640.
Existing-metadata probePASS: preexisting0700/0600 GID0 metadata remains unchanged
when action appends, preserving separate historical reconciliation requirement.
Logs logger-permission-probe-01/02.log, logger-existing-metadata-probe.log.
Quick finalhead nix build --no-write-lock-file --no-link
.#checks.x86_64-linux.log-reader-access PASS, including eval assertions, pinned
rsyslog syntax, generated NixOS logrotate validation and helper AST; Nixfmt,
Python VM AST, whitespace and required hooks passed. Group substitution ONLY in
syntaxcheck is explicit; actual group behavior separately probed and final VM
remains authority. New VM asserts absent fresh tree, every ancestor group/mode,
SSH positive reads, localmessages/pipe modes, rotation/HUP/writedenial.
No long tests after committed production correction until this focused review.

## Earlier narrow test corrections (unchanged production)

Lead inspected original A1 assertion split, explicit h2c/ENOENT403 proxy fixture
corrections, and logger RFC5424/persistent consumer/socket-quiesce/readiness/
bounded-diagnostic fixture corrections. Proofs review-a1.*, verification-fixture-fix.*,
verification-status-fix.*, logger-fixture-fix.* preserve each delta. These correct
reviewed test setup, don't weaken boundary assertions or introduce new design.
Do not rerun a whole unrelated review solely for these focused fixes.

## Required review lanes/conclusions

Reassess affected GENERAL and RISK+COMPATIBILITY lanes for production permission
placement, security semantics, existing metadata, pipe/localmessages/rotation,
probes/tests/docs and rollback. Reuse prior unaffected architecture and scope
conclusions: same components, native mechanism and package boundaries, no new
abstraction/framework. Deliberate legacy versus action-specific declarations are
required native contexts and implement the same accepted policy.

Inspect updated complete two-commit series (loggerbd54b28c, proxyd07b4251) and
explicitly update whole-history/no-obsolete-approach/no repeated streams/no
migrations conclusion. Fixes folded into owning unpublished commits; no branch
version merged/released/deployed/published/externally consumed. No dependency
pins/schema/logformat migrations. No production ops or root key removal.

Read mandatory-change-review skill and applicable lane refs/guidance; do review
directly/read-only, no nested agents, long tests, Git/source mutations, production
requests or credential operations. Save report review-followup.md in this session.
Report concrete severity/lane/file:line evidence and residual longVM/hostbuild/live
acceptance limits. If unrelated serious issue found, report it; don't rubberstamp.
