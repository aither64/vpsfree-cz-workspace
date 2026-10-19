# Native inventory acceptance correction

Follow up on the same coherent change and original/delta reviews. Read
mandatory-change-review SKILL.md and all four lane references; assess only the
affected test-observation mechanism, retaining the prior production conclusions.
Remain read-only; no long checks, nested agents, or source edits.

Runtime worktree is worktrees/2026-10-19-session-creation-end-to-end/dev-workspace.
Base remains 7ceb6b943c7fa6e6db2b42b1fc2d9732c6413e03; current committed head
a0799a622610db0eadd0e94a31d0bcd06d75cfd3. Series remains three logical commits:
98ae6b3 journal reader, dd9581d suite/CI/docs, a0799a6 retirement discovery.
No migrations, changed product code since your delta review, obsolete approaches,
or repeated pin streams. Current diff against fdfec51 is review-inventory.diff.

Actual immutable VM at fdfec51 passed explicit default-provider custom solo
creation, attachment delivery, notifications and completed follow-up. Automatic
naming/inherited-provider sensitive team creation and follow-up also reached
ready, and native reads verified both retained member IDs/providers/settings.
Then the complete-inventory assertion failed: thread/list omitted both
unassigned headless members. Full evidence creation-rooted-acceptance.log;
exit 1 after 549 seconds. No acceptance, deployment or integration is claimed.

Pinned native source rust-v0.163.0 state/src/runtime/threads.rs passes
include_empty_preview=false for ordinary listings, true only for spawn-relation
queries. Retained independent members have a developer bootstrap but no user
preview. This explains the missing list rows; source/cwd/provider checks on
member metadata already passed in the product's own bootstrap proof.

The test now preserves ordinary listing's root presence/no-foreign-ID check,
verifies each member's actual cwd and saved project ID, and independently queries
the pinned native SQLite database read-only for every active ID at the exact
destination cwd. That set must exactly equal the root and distinct retained IDs,
including any orphan starts. It discovers exactly one state_*.sqlite in the
disposable native home and opens URI mode=ro; no database writes or native patch.
This is a fixture-only observation of pinned 0.163.0 persistence, not a new
product interface or supported mixed-version database reader. An incompatible
native upgrade intentionally requires updating its acceptance fixture.

Quick checks: diff whitespace, Node syntax, Python AST, Nix parse passed in the
declared Nix shell; driver derivation evaluation passed. Same read-only query
successfully inventories this initiative's actual native cwd on stock 0.163.0.
Original rooted package remains retained. No integration test of this changed
observation has started. Assess whether complete-identity acceptance is sound
and proportional, and persist final-review-inventory.md with findings or explicit
acceptance of this delta. Whole-process required matrix remains unchanged.
