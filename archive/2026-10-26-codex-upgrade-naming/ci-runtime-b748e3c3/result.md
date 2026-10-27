# Final runtime automatic CI

The existing automatic [Check run 40547732709](https://github.com/aither64/dev-workspace/actions/runs/40547732709)
completed successfully at exact published head
`b748e3c3cf5711980cc46608ee27f517b95e5c7d`.

| Job | Job ID | Conclusion | Started UTC | Completed UTC |
| --- | --- | --- | --- | --- |
| archive | 122342779703 | success | 17:08:32 | 17:22:54 |
| fast | 122342780132 | success | 17:08:31 | 17:22:18 |
| creation | 122342780245 | success | 17:08:30 | 17:23:47 |
| host | 122342782382 | skipped (expected) | 17:08:28 | 17:08:28 |

All times are on 2026-10-27. This result is for the final `b748` input;
earlier `7dfee3` profile/CI failures remain separate historical evidence.

After owner2 reported final profile success, bounded assessment success and
actual settlement/free, implementer3 made one read-only `gh run view` capture
using `gh` from the runtime's pinned Nixpkgs. The raw response is `final-run.json`;
`capture.meta.json` records the full argv, CWD, start/end timestamps and true
exit `0`. Stderr is retained in `capture.stderr`. The capture took 3.672 seconds,
17:25:31.453314–17:25:35.125285 UTC.

Original inline handle `63451` returned final exit `0` with no remaining session
ID. No watcher was launched because the run was terminal. No operation remains
running or uncertain; the sole utility slot is free. There was no dispatch,
rerun, cancellation or additional test. Lead and owner1 received the exact
result and settlement. Corrected-target deployment authorization remains with
the lead's separate package.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-codex-upgrade-naming/>
