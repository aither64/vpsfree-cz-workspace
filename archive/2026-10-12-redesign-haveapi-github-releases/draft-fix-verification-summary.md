# Corrected patch and master fix: verification

Exact tested source heads:
- Release: 7fb218e28a86ab1d27de74ccb92c2a45063a4f78, VERSION 0.29.11.
- Master fix: 526648131af45df68c25ac0042a52f22c7a81df5, VERSION 0.29.0.

Retained reviewer0 accepted both complete ranges, all four lanes, final history
and no migrations before these longer checks (draft-fix-review.md).
Fresh Luna/low utility /root/draft_fix_verification_watcher used validated session
identity and installed full-access/approvals-never policy, owned the related
batch to terminal completion, about 1m55s. No retries/cancellations or active run.

Wrapper, local checks and both CI watchers exited 0. Lead inspected all statuses,
component counts, exact-head CI receipts and local manifest identity. Counts:
release helper 26; server 365; Ruby client 47; Go generator 9 examples; JS43tests;
PHP51tests/144assertions. All passed. Dependencies, i18n health, clean packaging,
npm tarball smoke check, manifest/checksum verification and actual loading of all
three extracted Ruby libraries passed. Final quick suites also passed with run
ID=123; whole Ruby lint found no offenses in 244 release /243 master files.

Local manifest: source 7fb218e, version0.29.11, run_id local, SHA256
129f0c85fd503a19eb51036765ab1d5543dda841cb7ff17ff5f6ddd661516745.
This is a local verification build, not the future tag run's artifact set.
Old local0.29.10 and original tag0.29.10 files are separately preserved.
Generated PHP test cache removed; both tracked worktrees are clean.

| Candidate | Workflow | Run | Result |
| --- | --- | --- | --- |
| release | servers/ruby RSpec | [39300962975](https://github.com/vpsfreecz/haveapi/actions/runs/39300962975) | success |
| release | RuboCop | [39300962911](https://github.com/vpsfreecz/haveapi/actions/runs/39300962911) | success |
| release | i18n health | [39300962762](https://github.com/vpsfreecz/haveapi/actions/runs/39300962762) | success |
| release | clients/php PHPUnit | [39300962962](https://github.com/vpsfreecz/haveapi/actions/runs/39300962962) | success |
| release | clients/ruby RSpec | [39300963121](https://github.com/vpsfreecz/haveapi/actions/runs/39300963121) | success |
| release | clients/js tests | [39300962729](https://github.com/vpsfreecz/haveapi/actions/runs/39300962729) | success |
| release | clients/go RSpec | [39300962759](https://github.com/vpsfreecz/haveapi/actions/runs/39300962759) | success |
| release | release | [39300962818](https://github.com/vpsfreecz/haveapi/actions/runs/39300962818) | success |
| master | release | [39300938032](https://github.com/vpsfreecz/haveapi/actions/runs/39300938032) | success |
| master | RuboCop | [39300937855](https://github.com/vpsfreecz/haveapi/actions/runs/39300937855) | success |

Both release workflows were safe branch builds with publication skipped; no
new master/release integration or tag was pushed. Fresh SSH checks confirm
feature refs at the tested heads, master at c14e7d3, haveapi-0.29 at b27a031,
and no v0.29.11 tag. Actual registry OIDC, PHP key use and Packagist indexing
remain first-publication checks; a failure after some destinations accept files
can leave a partial release. Use exact retained originals for recovery.

Evidence: draft-fix-verification-wrapper.log/status,
draft-fix-release-verification.log/status, both draft-fix-*-ci-watch.log/status,
both draft-fix-*-ci-results.json and per-run logs. Final diffs remain byte-identical
to independently reviewed hashes in draft-fix-review-packet.md.
