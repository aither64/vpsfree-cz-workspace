# Portal message delivery recovery

Deployed and verified on aitherdev; all four affected repositories merged into
remote master after live verification. Machine released. Final feature and post-merge CI passed, including creation, archive and host tests.

The original failure saved `submitting` before the input write, so cancellation
could leave an undispatched message permanently uncertain. Admission is now
recorded under the connection writer lock and shared-ledger transaction. Proven
unwritten attempts remain retryable, while a possible write remains uncertain.
Concurrent native-history recovery atomically adopts positive acceptance.
Admitted portal HTTP sends finish receipt recording despite browser disconnect.

The composer warning clears after a successful newer submission and ignores
late feedback from older operations. Unknown original receipts remain visible.
Explicit replacement checks the original first, warns of duplicates and retains
one replacement link. Native Codex and schema 3 remain unchanged.

The installed old browser reproduced the stale warning with simulated delivery
responses. The same installed-browser scenario passed in Chromium and Firefox after deployment.
No message reached the affected original conversation. Installed app.js and
conversation.js match reviewed source bytes; the original conversation/latest
turn and native Codex/tmux PIDs are unchanged.

Documentation: codex-web/docs/reference.md owns delivery evidence;
dev-workspace/docs/workspace-portal.md owns portal recovery.
Exact source revisions: final-heads.json. Review: cancellation-review-report.md
and preceding reports. Rollout: rollout.md. Current progress: state.md.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-portal-send-recovery/

System: /nix/store/n6b9dmmaw83zx80paglrisy0w5rwnfw8-nixos-system-aitherdev-26.05.20261021.da6dc0e
Application: /nix/store/8ph05i3nps8xi1jfs450b16aysc16nvg-dev-workspace-0.2.0
Final exact integrated heads and proofs: integrated-lineage.json.
Refresh an existing portal tab to load the fix. Session remains open; no archival.

Complete verification: candidate-watcher-result.txt records the successful local
build/browser stages before the diagnosed CI creation-lock refusal; the rerun
passed in creation-watcher-result.txt. Full master suite passed in
postmerge-watcher-result.txt. Earlier failures and their diagnoses remain in
state.md. No action is required beyond refreshing an old portal tab.
