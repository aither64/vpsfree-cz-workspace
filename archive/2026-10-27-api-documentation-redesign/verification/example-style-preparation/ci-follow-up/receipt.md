# Example-style CI follow-up

One exact-head/branch/push metadata observation: 2026-10-29T18:24:13.348937+00:00 through 2026-10-29T18:24:14.306098+00:00 (0.958219s), exit 0.

Head `6e09dac83b8ba3478fbf3c2232c6a6a05c3fdb00`; tree `f20fa20c109d1f7e73ee4f8cc1b6019a21e6f000`; branch `2026-10-27-api-documentation-redesign-example-style`.

All 11 attempt-1 runs completed: 10 success, one release failure. Success rows below are status-level evidence only; their logs, runtime counts, artifacts and graphs were not inspected. No workflow waited on or queried twice.

| Workflow | Run | Attempt | Outcome |
| --- | --- | --- | --- |
| RuboCop | 40928914241 | 1 | success |
| clients/php PHPUnit | 40928913907 | 1 | success |
| clients/ruby RSpec | 40928914072 | 1 | success |
| clients/python | 40928913939 | 1 | success |
| release | 40928914008 | 1 | failure |
| i18n health | 40928913988 | 1 | success |
| clients/js tests | 40928913965 | 1 | success |
| clients/go RSpec | 40928914048 | 1 | success |
| servers/ruby RSpec | 40928914084 | 1 | success |
| clients/rust | 40928914079 | 1 | success |
| servers/ruby performance | 40928914037 | 1 | success |

## Actual release failure

Original attempt 1, job `123641808217`, failed `Test and build maintained packages`. Exact checkout head is present in the original log. The release command runs `make release-deps`, `make release-test`, `make release`, then `make test`.

The last command stopped in `make test-typescript`: 63 examples, 2 failures, seed 26875. Both update/change cases in `clients/typescript/spec/unit/documentation_performance_spec.rb:53` expect `runtime.authenticate('basic'`, while accepted candidate `documentation.rb:162` emits `runtime.authenticate("basic", ...)`. This is a stale quote-specific assertion in an unchanged performance spec after the approved renderer style change. No source/test correction or local execution was performed.

The raw log shows 236/0 release specs, 928/0 server specs, 67/0 Ruby client and 101/0 Go client before the TypeScript failure. These counts describe that completed release job only. `make test` exited 2; retained-artifact upload, verification and summary were skipped. No completed style release-artifact proof is claimed.

Raw job log: `release-attempt1-failed-job.raw.log`, 215744 bytes, SHA256 `111028f6b0ce2b0f4991dcdf5b6b0bf8b1f9ecacbf331a183343b3d0a3e94116`. Line-numbered failure context is in normalized log lines 2314–2339. The initial gh log capture refused terminal escape sequences; its error is retained. Explicit raw-output capture then succeeded with `--allow-escape-sequences`, writing bytes to file and stripping ANSI only for inspection. No CI operation or status query was retried.

Failure reported to main (`d176a0df-b124-4ea7-a15f-0840170663fe`) before receipt prose; same-session original owner1 notified (`b82d4e71-73c5-476a-98c4-e3f22f85ca22`). No fix assignment was issued.

## Preservation and release

Canonical tracking `dev-session current` exited 0 with the exact bound slug; both identity environment variables were absent. Earlier workspace-root failure remains recorded and had no source/network effects.

Before/after both worktrees: all 908 tracked file bytes/modes each, HEAD/tree, refs, logical staged entries/flags, clean tracked status and the 8 selected top-level packaged Markdown docs each are identical. The earlier publication receipt retains its separate all-11-doc verification; this snapshot did not repeat that full inventory. The record hashes are retained in preservation-before/after.json. Commands wrote only this ignored evidence directory; no source, index, refs, locks, protected inputs, roots or older evidence was modified. No additional full protected-input/root sweep is claimed by this bounded assessment.

All subprocess/tool handles completed. No watcher or utility was needed; no read-only sourcehold was acquired. Any own utility/sourcehold capacity is explicitly RELEASED; no active or uncertain owned operation remains. No CI rerun/dispatch/cancel, source fix/check, local test/build/measurement, deployment, preview, peer, service or lifecycle action occurred. OAuth/consumer operations are independent. Original direct f6→fb07 result retains 8 PASS / 6 INCONCLUSIVE, unchanged.

No project documentation change is useful for a read-only CI status assessment.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
