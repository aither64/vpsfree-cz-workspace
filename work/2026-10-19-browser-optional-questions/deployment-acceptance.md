# Deployment acceptance

Optional-question browser handling and archive recovery fix are deployed on
aitherdev. Independent final reviews and quick/browser/native checks passed;
final runtime CI39397884404 passed fast/archive/creation, with host skipped by
its workflow condition. Refreshed configuration baseline review has no findings.

Final source heads: codex-web641907fb, runtime1395387f, workspace0383f0bc,
configuration316a071c. See deployment-final-inventory.json for exact SHAs,
bases and complete logical commit series. No migrations; no obsolete pin stream.

Both exact prepared operations succeeded/applied under reservation90fb300f:
- systemc5cacc82-e197-4e2b-85bb-fb4733626cbc, attemptcc1f0dc6-45b2-4114-9061-ad797fbc6533;
- profileb004f7a7-f784-42cc-bca6-037ae1f836d1, attempt52c564ca-0d08-49c7-a457-8e2627b85088.

Running system and system profile agree atj98vjl4m, NixOS26.05.20261019.f3a73bc.
Selected application isp4snvm49, exactly the reviewed composed package.
No reboot occurred. The old failed system attempt remains preserved; only its
unclaimed superseded dependent profile job was canceled. No uncertain effect or
replayed deployment remains.

Live verification passed against the local workspace router: session page and
details return200; optional-question panel is present; questions.js and
conversation.js bytes match reviewed codex-web; router/portal services are active;
Codex reports0.163.0; exact own session target/thread identity is unchanged and
interactive. External TLS requires site CA/authentication, so this check used the
local Unix socket. Browser interaction fixtures passed before deployment; no
production test message was sent. No owned tmux pane existed in the before-image,
so no new terminal continuity claim is made. See live-deployment-verification.json.

Authorized September24 andSeptember30 archives completed normally through the
reviewed candidate recovery. Their journals/sidecars are clear; their tracking
and the independently completed October7 archive all report synced. Three live
HaveAPI worktrees exactly match the original HEAD/status/Git pointers/admin inode
snapshots after both recovery and deployment. No live worktree was removed,
recreated, moved or changed. See completed-archive-recovery-proof.json and
live-worktree-after-deployment.json.

A reviewer service-account failure was recovered by resuming the same standalone
reviewer with verified catalog Astra/xhigh settings. An interrupted native resume
selected the default model and was not accepted. The final deployment watcher hit
the same account error; only that utility was stopped and documented parent
monitoring observed the original jobs to success. No application operation was
canceled or replayed for those observer failures.

Ready for use; ready, awaiting merge approval. The session remains active and
reservation90fb300f remains deployed_review for user acceptance. No default
integration, release, closure or roster change was performed or authorized.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-browser-optional-questions/
