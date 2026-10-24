Result: **failed**, exit 1. The single authorized operation completed; nothing remains running. No retry or diagnosis performed.

- **Tested B:** `5e342788c7178ac1cb93c25591bdc42a83386c6b` (tree `ed95652b08dc7a5d3e2a54745974a0431bed1bc2`); clean before run.
- **Command:** `bash capture-attempt-2.sh`, from the canonical tracking directory; elapsed **12.961 s**.
- **Receipt and logs:** [result.json](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/ui-successor/capture-attempt-2/result.json), [stdout.log](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/ui-successor/capture-attempt-2/stdout.log), [stderr.log](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/ui-successor/capture-attempt-2/stderr.log).
- **Failure evidence:** assertion `notice update shifted a scrolled-up message`; fixture also recorded HTTP 503 responses. Images: `failure-desktop.png` and `capacity-desktop.png` under `capture-attempt-2/screenshots/`.

The released packet gave A as `f86290673d752c77b56c70228c3d26aced75e177`; the executed fixture reports B’s failure.