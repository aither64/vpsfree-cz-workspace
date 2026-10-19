# Private PID namespace implementation

Team assignment from implementer0 to lead:

PID-namespace persistence-barrier implementation complete and FROZEN. Same-session current verified as 2026-10-03-automatic-session-slugs; both DEV_SESSION identity variables absent, matching trusted workspace binding. Read accepted full persistence supplement/amendment and provider instructions; reused unchanged full applicable workspace procedures/documentation/handoff guidance.

ONLY edited worktrees/2026-10-03-automatic-session-slugs/codex-web/codex/ephemeral_integration_test.go, on parent-reported clean provider1be5ba65da7d2e2876804cb809b1fe398bdd50a7. SHA-256 bf56fbc326707bdc5feb7ecc26e7c02fe3ec2a4a5ea6182a44a3769897ab75d1 (before parent gofmt). No production/helper/policy/API/model/catalog/pin/docs/tracking or managed-file changes; no Git commands.

Concrete boundary: existing clone/reexec now also uses CLONE_NEWPID. Outer captures PID-namespace identity; child requires internal marker, PID1/PPID0, different well-formed identity, recursive MS_PRIVATE then fresh proc with NOSUID/NODEV/NOEXEC, proc/self=1 and matching proc/1 namespace. Stored nonzero owner is revalidated before native starts and EVERY namespace-wide SIGKILL. No marker-only trust, host fallback, process scans or wildcard background reaper.

Stop fences diagnostic generation under h.mu, rejects active utility call, drains/holds diagnosticMu, then uses a fixed two-second barrier. It repeatedly sends guarded kill(-1,SIGKILL), accepts ESRCH only as signal absence, and waits for BOTH existing single Cmd.Wait owners through cached result + closed done (readiness cannot consume completion). Only afterward Wait4(-1,WNOHANG|WALL) drains adopted children, retries EINTR, re-signals while pending and accepts ONLY ECHILD. Zero, unexpected direct wait/signal/reap error and deadline—including late ECHILD—fail. No counter/SQLite/helper process starts during kill/reap. Existing restart/final-stop sites reuse this barrier; init exit remains final containment and outer Wait reports failure. Direct normal exit and SIGKILL ExitError are accepted; other results fail.

Persistence order: original ordinary inference/eight eligibility/model/tool assertions unchanged; original denied count captured once after control completion. Ordinary closes; both natives plus descendants positively join; exact same profiles/home/config/catalog restart. Reopen identical ordinary options and persisted thread/read ONLY, requiring exact retained root and completed turn. Check immutable denied count unchanged, insert the unchanged timestamp1 sensitive seeds once, verify exact seeded fields by fixed count queries, take one baseline. No reseed/rebaseline/restore/exclusion or new ordinary turn. Fresh-MCP reconfigure likewise preserves ordinary options and retained read. Existing native deadlines/36 leaves, strict logger/SQL/marker/egress/action gates remain.

New PURE selectors: ^TestEphemeralIntegrationNamespaceOwnershipGuard$ (10 leaves) and ^TestEphemeralIntegrationNamespaceStop$ (11 leaves), or combined ^TestEphemeralIntegrationNamespace(OwnershipGuard|Stop)$. They use finite syscall/time seams, no subprocess: ownership rejection before any signal/reap; owner change; zero versus ECHILD; EINTR/positive reaping; ESRCH versus join; signal/reap/direct-wait/deadline failures; two direct owners before wildcard; reusable cached readiness; late ECHILD. Expected 2 top-level groups/21 leaves, NOT execution evidence.

Parent pending quick command from provider worktree: nix develop /tmp/automatic-session-slugs-codex-web-env -c env TMPDIR=/tmp GOWORK=off go test -mod=readonly -race -tags=codex_integration ./codex -run '^TestEphemeralIntegration' -count=1 -json. No selector-zero claim. I ran ZERO tests/format/Nix/native/VM/network/model processes and did not bypass denied Nix access.

Distinct POST-REVIEW non-model selector: ^TestEphemeralNamespaceOwnershipIntegration$ (not matched by pure prefix). Same proven reexec/proc owner; two ready leaders, one real setsid descendant and adopted orphan; both cached direct waits, >=2 adopted reaps, ECHILD and live PID1; repeats second cycle. TestEphemeralNamespaceOwnedHelper is its internal role selector, fails missing private prerequisites and is NOT a standalone quick check. Fixture-scoped GORACE=atexit_sleep_ms=0 avoids synthetic helper exit-delay interference. Missing clone/mount/ownership/readiness fails, no skips/fallback. Full ^TestEphemeralProtocolIntegration$ remains unchanged post-review native gate with existing exact binary/hash/source/ip/nft/sqlite prerequisites plus new private PID/proc support.

Limits: code is unformatted/uncompiled/unexecuted by member; parent formats/checks then commits/folds and affected independent review precedes non-model ownership control and one meaningful native batch. No ownership or isolation/native/VM pass established. Previous SQL/snapshot writer remains unattributed; strict logs_2.sqlite/logs gate and unanswered logging preference are NOT solved/waived. No new public contract or remaining source gap identified by this authored finite correction, subject to actual checks/kernel capability. Session remains open: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/


## Coordinator quick verification

Parent gofmt/whitespace passed. Owning cached Nix Go1.26.7 with
TMPDIR=/tmp, GOWORK=off, -mod=readonly and -race, tagged pure
^TestEphemeralIntegration selector:14 groups/122 pass events, zero failures
or skips,2.827s. Neither namespace native selector nor model/native fixture ran.
Formatted file SHA fcd317b7aeb411e9f6ea840ac58146e4f34dc4e359989ceffeccfa1004c2120c.
Main reconciled reference.md and applied required English writing guidance.
Owning provider unit amended to de874bc39553f8955cecdfaaeb4216959b40bd3c;
pre-correction1be backup retained. No hook framework declared/bypassed.
Related independent review precedes one meaningful native batch.
