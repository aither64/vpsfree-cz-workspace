Independent final follow-up review of completed, committed work. Read mandatory-change-review SKILL.md and all four lane references. Perform review yourself, read-only; no nested agents, edits, deployment, merges or long checks. Keep model/effort/policy from your retained identity.

User directed earlier that discovered lock-contention problems must have their root causes identified and fixed, then explicitly requested aitherdev deployment and "merge and release". The three reviewed branches were integrated and aitherdev claim released after verified deployment/lineage. New automatically triggered master CI 40229910427 at exact b974f2f3 passed creation, fast and host, but archive VM failed at immediate worktree_add after native session start: another dev-session command is changing the slug. No rerun has been attempted. Failed log and master-merge-ci-findings.md retain evidence, including an unresolved separate portal shutdown timeout; do not assume this fix proves that timeout's cause or the historical holder PID.

Source: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-archive-unmanaged-files-investigation/dev-workspace
Tracking: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-25-archive-unmanaged-files-investigation
Read applicable source/workspace guidance and design.md's post-merge worktree follow-up, state.md, failure logs and quick evidence.

Overall risk high: session synchronization and concurrent mutations. All four lanes apply. Trusted local operator boundary remains; no hostile-root filesystem framework is introduced.

Complete unmerged range base b974f2f3f83792a494610d1ea03f3d69e97bc1a4 to head b75a6a1065449743b6a3c2f859b44bc32fefdc40
2a58cf4937d035dd8688aaae92d9e997c3efdb63 worktree: wait for portal readers during registration
b75a6a1065449743b6a3c2f859b44bc32fefdc40 test: initialize explicit scope in native worktree fixture

The prior four commits are already merged, deployed and externally consumed; preserve their history. New range has one bounded implementation/docs/Go boundary regression commit and one independently reviewable native test fixture correction. No migrations, new persisted formats, lock files, protocols, dependency pins or generated update streams. No superseded unmerged approach exists.

Implementation: worktree_add alone enables an optional private wait_for_readers flag through with_slug_lock/with_host_lock. Initial EX/NB failure may probe SH/NB. Successful shared access allows waiting for EX; a stable exclusive writer still returns existing busy error. Actual checks/mutations remain after EX. Other callers retain defaults. No generic retry, global lifecycle lease or new shared-state authority. Assess flock upgrade/concurrency behavior and whether this scope is proportionate.

New Go/Ruby boundary test holds the actual portal queue/reconcile SH admission, identifies its device/inode against Ruby waiting, proves no checkout mutation before EX, unrelated registration while waiting, and real Git checkout completion after release. Writer EX remains refused. Only absent tmux/native external effects are injected; Runner, flock, metadata and Git are real.

Quick results: pre-fix deterministic portal-reader test fails with exact busy error and writer case passes. After fix full new test passes. Related Go creation/name/plan/new tests pass, 4.473s; source syntax/whitespace pass. Focused Ruby worktree/observer/writer tests: 9/134 pass. Broader Ruby selection initially 44/781 with 1 existing native fixture error: exact b974 baseline reproduces missing portal manifest; fixture correction now passes native tmux test 1/44. Initial malformed baseline filter ran zero tests and is not evidence; corrected-filter log is the real baseline proof. Logs named worktree-contention-before/after/quick/ruby and worktree-native-fixture-*. No long tests started since these two commits.

Current consumer pins: config/master6428e280 and workspace/master9c4c97cd both runtimeb974; unchanged extension767dfd58/codexweb8b60554b. Selected package bhi44p5i remains the previously verified artifact. A future pin/deploy will use exact reviewed/published follow-up head and normal preparation/claims/system-first ordering. Review content/history, compatibility, root-cause evidence limitations, and documentation. Do not grant user approval or claim deployment/CI complete. Require explicit whole-range history/repeated-stream/migration conclusion in report.
