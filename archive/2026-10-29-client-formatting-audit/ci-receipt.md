# Final CI and package receipt

Tested and SSH-published feature head: `d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038`. Inherited base: `ae46cf27a9afb6558d386c293cec7231dd6c423d`. Ten owned logical commits. Final project index/worktree clean; all ten exact-head workflows completed successfully.

| Workflow | Run | Conclusion |
| --- | --- | --- |
| RuboCop | [40972318736](https://github.com/vpsfreecz/haveapi/actions/runs/40972318736) | success |
| clients/go RSpec | [40972318993](https://github.com/vpsfreecz/haveapi/actions/runs/40972318993) | success |
| clients/js tests | [40972319039](https://github.com/vpsfreecz/haveapi/actions/runs/40972319039) | success |
| clients/php PHPUnit | [40972318898](https://github.com/vpsfreecz/haveapi/actions/runs/40972318898) | success |
| clients/python | [40972318812](https://github.com/vpsfreecz/haveapi/actions/runs/40972318812) | success |
| clients/rust | [40972319003](https://github.com/vpsfreecz/haveapi/actions/runs/40972319003) | success |
| i18n health | [40972318911](https://github.com/vpsfreecz/haveapi/actions/runs/40972318911) | success |
| release | [40972318951](https://github.com/vpsfreecz/haveapi/actions/runs/40972318951) | success |
| servers/ruby RSpec | [40972319188](https://github.com/vpsfreecz/haveapi/actions/runs/40972319188) | success |
| servers/ruby performance | [40972318827](https://github.com/vpsfreecz/haveapi/actions/runs/40972318827) | success |

## Coverage and retained package evidence

PHP workflow explicitly passed actual PHP8.0 shipped-source syntax, locked fixer and PHPUnit8.3/8.4. Rust passed native formatting, runtime feature tests/Clippy and generated protocol acceptance. Release build job executed its maintained-package step successfully (not skipped), covering release tests, build-only packaging/extracted TypeScript smoke, full make test, npm smoke and Python package smoke. Artifact retention succeeded. Publish approved artifacts job was skipped on this feature branch.

Retained artifact: `release-40972318951`, ID`12941067574`, 1235304bytes, digest`sha256:bdd28aa49b3abe4196405171984ebaf94bca0182763cf1b6ce3f949d71664efe`. Downloaded archive digest independently matched that metadata. Manifest source matches exact tested head; shared package version remains`0.31.0`.

Release manifest SHA256: `4edf33b7495132e45b743db00f7641976a754b81f1fd299e8ec5ecd91fdf6b05`. Full manifest and archive are local disposable supporting artifacts in ci-logs/, with the authoritative retained artifact on [release run](https://github.com/vpsfreecz/haveapi/actions/runs/40972318951).

Recorded tools:
- prettier: `3.9.10`
- node: `v24.21.0`
- npm: `11.19.0`
- ruby: `ruby 3.4.11 (2026-09-23 revision 592f1ffdb3) +PRISM [x86_64-linux]`
- go: `go version go1.26.10 linux/amd64`
- rustfmt: `rustfmt 1.10.0`
- rustc: `rustc 1.99.0 (b940084d7 2026-09-28) (built from a source tarball)`
- cargo: `cargo 1.99.0 (5f94df478 2026-08-27)`
- python: `Python 3.11.17`
- uv: `uv 0.13.4 (x86_64-unknown-linux-gnu)`
- composer: `Composer version 2.10.3 2026-08-27 13:34:23`

The manifest retains complete resolved inputs for all ten actual library/application locks:
- `Gemfile.lock`
- `servers/ruby/Gemfile.lock`
- `clients/ruby/Gemfile.lock`
- `clients/go/Gemfile.lock`
- `clients/rust/Gemfile.lock`
- `clients/typescript/Gemfile.lock`
- `clients/rust/runtime/Cargo.lock`
- `clients/js/package-lock.json`
- `clients/php/composer.lock`
- `clients/python/uv.lock`

## Review and lineage

[Independent review](review.md) completed all four lanes. Only R1Important was found, directly verified with a focused regression and folded into its owning release commit. [History receipt](history-consolidation.md) binds original reviewed/fixed/new ranges, all nine unchanged patches, exact accepted delta and identical fixed/final tree. No database migrations, redundant pins or remaining findings.

Post-CI SSH evidence: feature ref still equals the exact tested head; remote master still`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`, selected redesign-example-instructions still`ae46cf27a9afb6558d386c293cec7231dd6c423d`. Portal comparison captured default merge-basef6e5c375 -> finald6c2748a. Own initial-base comparison is in [branch inventory](branch-inventory.md).

Implementation/checks/review are done on the user-selected unmerged redesign base. Later transplant/rebase onto approved integrated redesign lineage and separate HaveAPI master merge approval remain. No package publication, deployment or session lifecycle action was performed. No verification command remains running.
