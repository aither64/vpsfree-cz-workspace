# Package C final R handoff

Current consolidated source/CI/real-workflow handoff: [package-c-final-handoff.md](package-c-final-handoff.md). All five complete C workflows now passed; the records below preserve earlier checkpoints.

Final runtime follow-up: the lead's final R batch passed HaveAPI, Terraform and
vpsAdminOS, then status stopped safely at its Go metrics route test. IRC was not
launched in that batch. [Diagnosis and preserved effects](package-c-status-r-followup.md)
record an accepted, locally committed test-only compatibility correction
`d4c816bbf7ad22b9b2dcb424c1f316b1d0b6c6aa`, now independently reviewed with
no findings and published by normal fast-forward push. It supersedes the status
head in the original R snapshot table below; [fresh proof](package-c-status-metrics-publication.json)
and [CI snapshot](package-c-status-metrics-ci.json) record its exact current state. Eight focused tests pass on each of the pinned and candidate
Prometheus graphs; only app_routes_test.go changes.
The publication and earlier source/check evidence below remain unchanged.

All five exact reviewed R consumer heads are published over SSH. Fresh default
and feature lease checks matched the reviewed bases and published P heads.
Every ordinary declared-shell push returned 0, its fresh remote proof equals
the reviewed head, and all five worktrees remain clean. Provider R was published
first and verified before each consumer push. No default integration, deployment,
machine claim or lifecycle action occurred. Runtime verification remains owned
by the lead; this handoff does not claim the real updater/race/VM gates passed.

| Project | Unchanged base | Published reviewed head | Commits |
| --- | --- | --- | --- |
| haveapi | `67fcd34ba506264a5c7ee2e8e18a88d221c6f469` | `baec8e58e11a4868a6c713e70d406709bb94c152` | 1 |
| terraform-provider-vpsadmin | `2a2c1055302f86f8e250f1d7e4c331d62012efe8` | `f835d63b14931712129771792039f645cf6a3305` | 1 |
| vpsadminos | `e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854` | `d86ea84e653e09bb1d47e21f6b219406c5462906` | 1 |
| vpsf-status | `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb` | `6b5e8a6089926112bfbb63a45413b886ee56e549` | 2 |
| vpsfree-irc-bot | `94ac4eb5a7caf0456fff7df86a44cae198463276` | `5b68640fdf0d52bbf5786c886d37d62db595e1a9` | 1 |

The common provider is
`github:vpsfreecz/confctl/5436d3d7c36d3d5174eab3c44e3578830749d3db#confctl`.
Each adoption contains one final workflow pin and shared-document link. Status
retains its independent vendor-hash correction as its second commit, with the
exact patch sandbox-tested at `589f233`. All five original lockfiles remain
byte-identical to their bases. There are no migrations, runtime input changes,
persisted format transitions, redundant pin commits or deployed state boundaries.

The independent [final R review](review-r-report.md) passed general and
architecture lanes, all eight complete histories/pins and no-migrations scope
with no findings. Original 7ba/P/Q ranges, reports, manifests and failed attempts
remain unchanged. [The R branch inventory](package-c-r-branches.json) and
`review-r-c/` preserve complete series, final path/diff inventories, range-diffs,
backup refs and exact published P lease heads. That inventory intentionally
retains its prereview local-publication status; the current publication proof
is [package-c-r-publication.json](package-c-r-publication.json).

## Checks and publication

The R fixture command in each project's declared environment was:

```sh
nix develop --no-write-lock-file -c python3 \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-r-fixtures.py PROJECT
```

All 40 scenarios passed (HaveAPI 9, Terraform 9, vpsAdminOS 6, status 7, IRC 9),
covering rejection/error publication stops, follows metadata, explicit package
environment, baseline preservation and committed-blob final validation. Actual
shared resolver checks run within the fixtures; guard responses are mocked.
Final status helper tests passed and Nix evaluation confirmed checks enabled
with Go 1.26.5 plus Perl 5.42.0 in effective native inputs. All five workflows
passed actionlint 1.7.12/ShellCheck 0.11 and `git diff --check`. Required ordinary
Overcommit/Lefthook hooks passed for final history creation; Terraform declares
no hook framework. Raw evidence is in `package-c-r-quick-*.log` and
`package-c-r-commit-*.log`, with status prerequisite receipts linked below.

After canonical SSH fetches and fresh exact target/feature checks, the push
command in each worktree was:

```sh
nix develop --no-write-lock-file -c git push \
  --force-with-lease=refs/heads/SLUG:EXACT_P_HEAD origin HEAD:refs/heads/SLUG
```

All five returned 0; exact arguments, P leases, fresh remote default/head proofs,
lock blobs, hashes and logs are retained in
[the publication receipt](package-c-r-publication.json). Imported action upstream
refs/compatibility evidence remains [package-c-actions.json](package-c-actions.json).
All five final portal comparisons were captured in
[package-c-r-comparisons.json](package-c-r-comparisons.json). IRC's first capture
was refused by another short session writer; its identical retry succeeded.
No source/ref repair or hook bypass was needed.

One immediate [CI snapshot](package-c-r-publication-ci.json), without waiting,
rerunning or dispatching, recorded:

- HaveAPI Ruby 40102844869: success.
- Terraform Go 40102865906: success.
- Status i18n 40102931079: success; Integration 40102931080: in progress.
- IRC RSpec 40102965672: in progress.
- vpsAdminOS: no matching push-triggered run.

No superseded queued/in-progress same-branch run existed, so none was cancelled.
Current-head and completed runs were preserved. Pending runs remain verification
limits, not successful evidence.

## Actual prior status CI failure

The prior P status Integration run 40099932120 failed at published
`c8869b8f274dd840539a94da30d19d355cd623c1`. Its downloaded native test artifact
12562134149 explicitly shows the new tools checkPhase failing to execute `perl`
from PATH. The package derivation failed 1; dependent service/system/testJSON
builds then failed before VM startup. This establishes the actual failure cause
from logs, beyond the earlier static diagnosis. No CI rerun or dispatch was used.

The [diagnosis](package-c-status-prior-p-ci-diagnosis.json),
[exact excerpt](package-c-status-prior-p-ci-excerpt.txt), complete run/artifact
metadata and hashed files under `verification/status-ci-p-40099932120/` retain
that evidence. The reviewed `nativeCheckInputs = [ perl ]` addition is folded
into the owning independent fix; the
[actual sandbox package pass](package-c-status-native-check-verification.json)
at `589f233` verifies the correction, and `git range-diff` proves the exact patch
is retained as final `6b5e8a6`. Its runtime closure has no Perl. A complete final
status workflow pattern and final CI are still separate gates.

## Prepared final runtime packet

The [R verification brief](package-c-r-verification-brief.md) binds the exact
[manifest](package-c-r-verification-manifest.json),
[driver](package-c-r-post-review.py), [real Git race](package-c-r-git-race.py)
and reviewed source/lock hashes. Python AST/JSON, all six source trees and file
blobs/content hashes, extracted Bash syntax, no external updater push and no
unresolved expressions passed static preflight. The root is
`/tmp/flake-update-guard-2026-10-24-provider-r-1`; startup retains an owned package
out-link. The lead supplies frozen `review-r-report.md` and launches serialized
fresh Luna operations. GitHub R source NAR/package/check derivation/recursive
inputs must match `verification/local-R-identities.json`; any mismatch stops and
reports. Exact local R197 already covers both actual package/caller/hook cases
when these identities match; no duplicate two-probe run is needed.

All seven complete real nonpublishing updater patterns, actual Git target
movement/fresh-baseline fixture and the supported singleton Terraform
`workflows` VM (eight ordered examples, native networking) remain in the final
plan. No C runtime watcher or live/VM command was launched by implementer0.
No active C command, claim or uncertain mutation remains.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
