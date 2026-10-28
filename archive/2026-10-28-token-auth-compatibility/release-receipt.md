# HaveAPI 0.31.2 release receipt

Requested: fix documentation compatibility, integrate master, backport 0.31,
and publish a patch release. Initial user request supplies merge/publication
authorization. Preserve protected GitHub approval; no registry writes before
candidate validation and retained-artifact inspection.

Master source: 2f5156262baaf137800c17a9321e617c2b5df1d5, integrated at 08:45 UTC.
Master review: review-master.md; all four lanes, no findings/migrations.
Source quick checks: 77 Go examples/0 failures; pure mounted profile passed.
Broader check: 30 server examples/0 failures.
CI: Go matrix 40658113568, performance 40658113525, lint 40658113520,
i18n 40658113538 all successful on exact master source head.

Backport base: d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42 (v0.31.1).
Expected next version: 0.31.2, no existing tag observed. Implementer0 preparing
provenance-preserving cherry-pick and separate metadata commit. Final head,
review/checks, integration, tag, workflow/artifacts and publication outcomes pending.

The existing workflow tests/builds every maintained component, uploads retained
artifacts, verifies the manifest and pauses at protected release environment.
After inspecting that exact candidate, lead can approve using existing explicit
user direction. The authenticated GitHub identity is the configured required
reviewer aither64, and prevent_self_review=false. Only then does the workflow
publish gems/npm/PyPI, synchronize PHP master/tag and finalize GitHub release.
No infrastructure deployment or downstream configuration changes are in scope.
Session remains open.

Backport source committed: 5a016f080bf39c184f71f6b15f904fc165448d6f.
Lead range-diff 2fc2b8f8..2f515626 versus d49cfa3f..5a016f08
shows source equivalence; only commit message adds required cherry-pick trailer.
Quick checks repeated: 77/0, pure mounted profile passed, four-file lint/diff
passed. Native release dependency/doc/input preparation passed in ~154s; ten
local locks retained. Shared version/changelog metadata preparation pending final
release-check/commit. Main-agent user-facing writing applied before commit and
actual changelog inspected, preserving exact technical facts.

Final candidate: 819bba5110e089465535ecd71ca2eb37a7d39caa (metadata), source
5a016f080bf39c184f71f6b15f904fc165448d6f on d49cfa3f. Clean/published
feature 2026-10-28-token-auth-compatibility-0.31. Full diff 22 files +97/-18,
all source changes equivalent and all 17 generated metadata paths contain only
0.31.1 -> 0.31.2 replacements, plus reviewed changelog. make release-check
reports metadata/prepared inputs valid. Final metadata lint 10 files/0 offenses
and mounted profile script pass at 0.31.2. All hooks active/passing.

Independent reviewer0 assigned final complete release range; fresh Luna/low
utility /root/release_candidate_watch observes exact existing runs listed in
release-candidate-runs.json. No duplicate local all-component build. Integration
claim request d3a67997-bcf8-436b-ac9c-5f29a07af4db prepared, not acquired.

Final release review passed without findings (review-release.md), exact range
d49cfa3f..819bba51. All-component candidate build/test workflow 40660354757
completed success; build-only publish job correctly skipped. Rust CI passed.
Only performance 40660354784 still running. Initial CI watcher returned early
with incomplete status; no local gh watch process remained. Lead continued exact
existing run observation with minimal-output gh run watch, no relaunch/retry.
Annotated v0.31.2 prepared locally at 819bba51; not pushed/publication not started.

All 11 candidate CI workflows passed on 819bba51. Release branch integration
complete 09:04 UTC: remote haveapi-0.31=819bba5110e089465535ecd71ca2eb37a7d39caa;
annotated v0.31.2 object 815c033be8cfca22822d0b2f80c022e959c5d0c4 peels to
same head. Branch/tag atomic SSH push, fresh remote proof. Short merge claim
d3a67997-bcf8-436b-ac9c-5f29a07af4db released and resulting state verified.
Tagged candidate build and protected publication pending.

Tagged build 40661462796 succeeded (job 122725246582), branch build-only
40661462440 also success. Utility stopped at protected publication boundary.
Artifact ID 12804711465, release-40661462796, 1,108,198 bytes, not expired.
Downloaded to release-artifacts; existing native verifier with GITHUB_RUN_ID=
40661462796 passed exact source/version/run identity, complete file set, retained
checksums, package inspection and dependency locks. Manifest SHA-256
4ba5e7dba199b1d92d28f23f9d080b4331adacf39fb9d398838a99733ce1b8b9.
Manifest records 11 files, 12 tool versions and 10 dependency locks. Release
notes inspected and match reviewed changelog. Protected environment release
24722193856 permits current configured reviewer approval. Initial user request
authorizes publication; lead approving only this verified retained candidate.

## Final publication and destination verification

Protected approval succeeded, deployment receipt 7381398498. Tagged workflow
40661462796/publication job 122728549971 completed success; publication ran
09:15:09–09:20:15 UTC (~5m09s job duration). The utility's earlier 15-minute
escalation label was inaccurate and superseded by authoritative job timestamps;
no timeout/retry/cancel occurred. Watcher finished, no operation left running.

Public non-draft/non-prerelease release published at 2026-10-28T09:20:14Z:
https://github.com/vpsfreecz/haveapi/releases/tag/v0.31.2
12 uploaded assets: 11 manifest-listed payloads/notes plus the manifest. Public
GitHub asset SHA256 digests individually match all retained files and manifest
SHA256 4ba5e7dba199b1d92d28f23f9d080b4331adacf39fb9d398838a99733ce1b8b9.

Lead reused existing read-only Publisher methods in the top-level Nix shell:
all five gem_present? checks verified exact name/version/platform/SHA256;
npm_present? verified identity/SHA512 integrity; pypi_files verified both exact
Python filenames/SHA256 against the tagged retained manifest. Every public read
returned HTTP200 on its first attempt. No upload/retry/rebuild was performed.

PHP remote master and peeled v0.31.2 both equal
52cf471406593edd42db32a6b61156522318dac9 (annotated tag object
a29305a514a5b507cb82f321b54d6bc2dde0591a). Public commit message records
HaveAPI-Source: 819bba5110e089465535ecd71ca2eb37a7d39caa. The successful
publisher checked exact PHP snapshot content as part of synchronization.
Packagist public p2 metadata indexes haveapi/client 0.31.2 with both source/dist
reference 52cf471406593edd42db32a6b61156522318dac9; indexing verified separately
from mirror push.

Fresh final SSH proof: master 2f5156262baaf137800c17a9321e617c2b5df1d5;
haveapi-0.31 and peeled v0.31.2 both 819bba5110e089465535ecd71ca2eb37a7d39caa.
Both registered feature heads integrated exactly into approved configured
targets. Both feature checkouts clean; both repository claims released and no
machine reservations. No deployment, lifecycle action or branch deletion.
Requested release work complete; session remains open.
