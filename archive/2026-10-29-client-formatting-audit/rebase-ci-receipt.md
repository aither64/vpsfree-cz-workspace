# Rebased exact-head CI receipt

Base: `c79645e0d43885c26cdc4129cbac96fdd5a13b07`. Published/tested head: `7edb003dd5d5a058b3308510bb8a5f60387ad654`. All eleven workflows completed successfully.

| Workflow | Run | Conclusion |
| --- | --- | --- |
| RuboCop | [41038382988](https://github.com/vpsfreecz/haveapi/actions/runs/41038382988) | success |
| clients/go RSpec | [41038382986](https://github.com/vpsfreecz/haveapi/actions/runs/41038382986) | success |
| clients/js tests | [41038382973](https://github.com/vpsfreecz/haveapi/actions/runs/41038382973) | success |
| clients/php PHPUnit | [41038383148](https://github.com/vpsfreecz/haveapi/actions/runs/41038383148) | success |
| clients/python | [41038383009](https://github.com/vpsfreecz/haveapi/actions/runs/41038383009) | success |
| clients/ruby RSpec | [41038383093](https://github.com/vpsfreecz/haveapi/actions/runs/41038383093) | success |
| clients/rust | [41038382977](https://github.com/vpsfreecz/haveapi/actions/runs/41038382977) | success |
| i18n health | [41038383075](https://github.com/vpsfreecz/haveapi/actions/runs/41038383075) | success |
| release | [41038382962](https://github.com/vpsfreecz/haveapi/actions/runs/41038382962) | success |
| servers/ruby RSpec | [41038383113](https://github.com/vpsfreecz/haveapi/actions/runs/41038383113) | success |
| servers/ruby performance | [41038383004](https://github.com/vpsfreecz/haveapi/actions/runs/41038383004) | success |

The release build/test/retained-artifact job succeeded; publishing was skipped. Existing workflow covers full make test, release tests/build, extracted TypeScript generator smoke against the supported runtime, npm smoke and Python package smoke. PHP source syntax8.0/formatter/PHPUnit, Rust features/Clippy/generated acceptance, Ruby client/server and endpoint performance all passed on this head. Old-head CI is retained as history only.

Retained release artifact `release-41038382962`, ID`12969666315`, digest`sha256:6782a327326ef1837e0fab692cb5d6866f74cd36f99230bb45ce15a8264c5bc8`; downloaded archive hash independently matches. Manifest SHA256`63ed90e5e73954ac92c419e4d4f563c488fd5c4fc2968150f6d39fce2ed1996c`, source exact tested head, package version`0.31.0`, Prettier`3.9.10`. Raw archive/manifest/full tools and ten dependency-lock graphs retained locally under ci-logs/ and authoritatively by the release run.

## Review and remote proof

[Affected review](rebase-review.md) reports no findings; original unchanged review conclusions retained. [Rebase proof](rebase-master.md) has exact old/new ranges, all ten equal patches, binary feature-diff equality and independent reconstructed final tree. No source conflict/adaptation/migration. Native hooks stayed enabled.

Explicit lease expected old feature d6c2748a; push succeeded. Superseded active same-branch runs inspected: zero; no run canceled. Post-CI SSH proof: feature exactly7edb003d, master exactlyc79645e0; project index/worktree clean, diff-check pass. Portal comparison refreshed to current master base and head. No merge, publication, deployment, resource claim or lifecycle action. No verification process remains running.
