# Bounded Settings correction verification

Fresh one-operation utility per /home/aither/.codex/skills/dev-session-monitor/SKILL.md; read it and relevant AGENTS. Installed policy Luna/low, danger-full-access/never. Do not spawn CLI watchers or nested agents. No source/tracking edits, diagnosis, retries, deployment or acceptance decisions. Parent reviewed and committed the15-line correction, final independent general/architecture review accepted.

Run these in order once, stop and report on failure. Own the handles; capture full logs under /home/aither/workspace/ai/vpsfree.cz/work/2026-10-28-cross-session-messaging/.

1. bash /tmp/settings-scroll-browser.sh > settings-scroll-browser.log2>&1. It checks runtime HEAD2caa94192dcd058d7ba030d9ef7830a18c0ea0d6 and runs only affected Chromium/Firefox communication/Settings test. Notify parent when done.
2. In /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-cross-session-messaging/workspace, verify HEAD58298dc0ed6f41993c9c3cc9c52db4299ed5ab4e then nix build --json --out-link /tmp/cross-session-settings-scroll-profile .#default > settings-scroll-build.json2> settings-scroll-build.log. Notify parent when done.
3. Observe existing CI40729952642 in aither64/dev-workspace for exact runtime2caa9419 via nix shell nixpkgs#gh -c gh run watch 40729952642 --repo aither64/dev-workspace --exit-status; save settings-scroll-ci.log. Get final run status/jobs JSON. If failure, collect --log-failed without rerun.

Spaces around stdout/stderr redirects must be normal shell syntax; filenames above omit spaces only in prose. Browser expected under1minute, build/CI may take5-25minutes. No quiet timeout. Stop only unexpected local kernel build and escalate. Report stage via parent message after5minutes and result promptly. Actual timestamps/elapsed, exit/status, paths, bounded failure evidence, active handles. Do not sum requested waits.
