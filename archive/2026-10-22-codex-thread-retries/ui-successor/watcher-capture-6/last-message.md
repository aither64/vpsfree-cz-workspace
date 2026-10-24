**Result: incomplete.** The capture operation did not start. I attempted the launch once with explicit `--sandbox danger-full-access --ask-for-approval never`; Codex rejected the command syntax with exit status 2 before running the wrapper. I did not retry.

- Revisions and trees matched the brief; both worktrees were clean.
- The session identity, catalog digest, utility identity, and pinned full-access policy matched.
- The attempted command was `codex --sandbox danger-full-access --ask-for-approval never exec -- bash ui-successor/capture-attempt-6.sh` from the tracking directory; elapsed time was 0.2 seconds.
- Output: `error: unexpected argument 'ui-successor/capture-attempt-6.sh' found`
- The wrapper did not create capture logs or `result.json`; no capture process remains running.