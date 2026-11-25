# Sysctl fixture: use an actual write failure

Implementer0, 2026-10-22. Implementer2 reports the focused native run at
`895870606179f0c1170ad92a5fdc49eb2d6d1bbf` completed with six examples passing
and two failures: the custom check succeeded after the supposed unknown-key
failure injection. This is consistent with the exact procps source contract.
The failed run does not show a product error-handling defect.

## Exact source and semantics

The generated service uses
`/nix/store/hr00izqgyfszlknsph42b42chvh7ln8r-procps-4.0.6`.
Its derivation is
`/nix/store/z0wyx3l556rcrl7v7bhmivbp5rz09f44-procps-4.0.6.drv`, version
4.0.6, with no patches. Its source derivation
`kjc54xax7vmlfmkkdxjfn3xaww40wbyi-procps-ng-4.0.6.tar.xz.drv` records
`sha256-Z76m+8OkKlNaAjDJ6JHl3ftNnTlCLUZWWimQ0azhUhY=`.
The [upstream release archive](https://downloads.sourceforge.net/project/procps-ng/Production/procps-ng-4.0.6.tar.xz)
downloaded read-only for this investigation matches that exact hash.

Verified release-source paths and line references:

- `src/sysctl.c:1024-1027`: `--system` sets `IgnoreError = true`.
- `src/sysctl.c:565-570`: a nonexistent key failing `stat()` returns success
  when `IgnoreError` is set; `598-621` likewise ignores an `ENOENT` open race.
  Therefore `kernel.vpsadminos_sysctl_test_missing=1` cannot force failure.
- `man/sysctl.8:54-55` describes ignoring unknown keys for `--ignore`;
  the source above proves that `--system` enables this automatically.
- `src/sysctl.c:623-628`: an existing key's stream write/close failure emits
  `setting key "..."` and returns `EXIT_FAILURE`, independently of
  `IgnoreError`. `local/fileutils.c:19-29` detects both prior stream error and
  failed close/flush. `src/sysctl.c:715-745` ORs write results, and `1069-1073`
  ORs that result into the process exit status for `--system`.

The verified guest kernel is 6.12.113, as recorded in
[the existing kernel identity receipt](generic-sysctl-v2-guest-identity.log).
At its pinned Linux source `1dfea587406b7dd79973831d1677fb2418e5e9aa`:

- `kernel/printk/sysctl.c:32-37` maps the existing writable integer key
  `kernel.printk_ratelimit` to `proc_dointvec_jiffies`.
- `kernel/sysctl.c:1323-1327` delegates that handler to `do_proc_dointvec`;
  its parser at `510-519` calls `proc_get_long` before conversion/storage.
  `proc_get_long:364-365` rejects the first character of `invalid` with
  `-EINVAL`. The handler returns the error without replacing the integer.
- `fs/proc/proc_sysctl.c:595-611,619-621` propagates the handler error to the
  write. Procps therefore returns nonzero for this write, even with `--system`.

No sysctl write was executed to prove this on the host. Source proof establishes
the expected error path; the corrected guest scenario still requires execution.
Extracted release files are retained as `procps-4.0.6-src-sysctl.c`,
`procps-4.0.6-local-fileutils.c` and `procps-4.0.6-man-sysctl.8` in this session.

## Narrow fixture correction and checks

Only `tests/suite/system/sysctl.nix` changed in this package:

- The failing managed file writes `vm.vfs_cache_pressure=113`, then
  `kernel.printk_ratelimit=invalid`.
- The failed explicit retry appends the same invalid-value assignment.
- The log assertion checks the existing-key write diagnostic and the service's
  `Unable to apply sysctl configuration` message.

The earlier valid rate-limit assignment remains 12 in `60-nixos.conf`.
Procps appends settings in order (`settinglist_add:201-215`), applies sorted
files, and writes every explicit entry rather than deduplicating repeated
keys. The subsequent invalid assignment leaves 12 intact; the partial-write
expectations of rate 12 and cache pressure 113 therefore remain appropriate.
Normal examples, retries, marker checks and no-retry observations are unchanged.

Nixfmt, parse, whitespace, actual full fixture graph rendering, and rendered
Ruby syntax passed (exit 0, `Syntax OK`):
[quick-check log](generic-sysctl-i0-invalid-value-quick.log).
The render used the same command as the
[initial receipt](generic-sysctl-i0-verification.md), producing
`generic-sysctl-test-invalid-value.rb`. The corrected fixture SHA-256 is
`974690e33b6ec9428c7a6f8c74b4006dc975bc20df37e137a75a3c6493fb1be7`.

Implementer2 owns all Git operations and the independent literal-source
canonicalization correction. No VM rerun, build, source/ref mutation outside
this fixture, or production action was performed by implementer0. The combined
committed correction requires fresh final review before another native run.
