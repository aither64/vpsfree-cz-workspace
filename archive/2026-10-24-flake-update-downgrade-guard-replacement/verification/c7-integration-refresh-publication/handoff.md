# Refreshed consumer feature publication

Both exact independently reviewed feature heads are published over canonical SSH.
The lead received each remote proof immediately. No claim or default integration
was performed by implementer0. Provider `822c0e35dbe2549111912f539116b4225dfd3035`
and all reviewed source trees and locks remain unchanged.

| Repository | Published feature head | Target observed before and after feature publication | Clean reviewed tree |
| --- | --- | --- | --- |
| HaveAPI | `39909094649b1d14a23f00615775ca7136acf4fd` | `1103a3a14b1dc6dec17fc4859df80220a54f111d` | `60ca6e54445da84bc0e6549a7a172a5dbddb07a0` |
| vpsFree configuration | `25258cd3f483f0116dbab35c7acf89b16eff4bbc` | `bec5556f6c60414e482550dd735321ebe3c3703b` | `31a86081ee586a0e6e08dad67b7539744ed0cf73` |

Each publication freshly fetched the canonical bare clone's master and feature
refs and independently observed SSH HEAD/master/feature. The old feature leases
were respectively `c7bfc1aa5af956b6057be8e623f9035c00ccb268` and
`5f0f4466adb175ed4fcac9b6d5c8909e87a1fec1`. Both exact-lease pushes used ordinary
Git in the repository's declared Nix shell, with required hooks left enabled, and
exited zero. Fresh remote feature equality and clean source HEAD/tree/index were
proved afterward. Full commands, stdout/stderr, source diff and remote proofs
are in each adjacent `receipt.json` and its referenced files.

The complete final feature series is one adoption commit per repository, with
literal parent equal to the target in the table. Their old reviewed ranges,
backup refs, equal stable patch IDs, range-diffs and complete reconstruction are
retained under `integration-preparation-c7/`. The independent final refresh review
is `review-integration-refresh-report.md`, SHA256
`f55e7a94a6bbb5778e6958f2379d9e1ecba395d92c538a7d6f773cd618bd7a2a`:
no findings, no migrations, no obsolete history and no new runtime gate. Earlier
runtime receipts remain historical component/input evidence; these publications
do not turn equivalent successors into executions of the earlier source.

The lead accepted the fresh watcher-owned dependency/hook preparation, exit zero
in 89.206 seconds. The retained status JSON's `status: running` field is stale;
its `finished: true`, `exit_status: 0` and `process_running: false` agree with the
complete aggregate and lead acceptance. The original receipt is preserved.

Prepared target paths for the lead's fresh-check/claim/ordinary fast-forward
integration are:

- `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/integration-haveapi`
- `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/integration-vpsfree-cz-configuration`

The owner did not reread those targets during concurrent lead-owned integration.
The lead must perform its own final fresh target/feature/cleanliness checks under
the ordinary short claim procedure. The earlier command plan remains in
`integration-preparation-c7/owned2-integration-plan.md`; its preparation/publication
pending notes describe that earlier checkpoint and are superseded by this receipt.

One bounded post-publication branch CI snapshot was taken for each repository,
without waiting or polling again. Exact HaveAPI head `39909094` had five completed
successes: i18n health `40127852320`, servers/ruby RSpec `40127852333`, RuboCop
`40127852448`, clients/js tests `40127852408` and clients/python `40127852286`.
clients/rust `40127852329` and release `40127852269` were in progress. No exact-head
failure or superseded queued/in-progress feature run was observed; no cancellation
was requested. HaveAPI's `doc/**` Ruby path filter applies to the changed guide;
the observed Ruby run is recorded directly rather than inferred from that filter.

No exact feature-head vpsFree CI run was observed. Its daily updater has schedule
and workflow-dispatch triggers, with no push trigger; absence is not a successful
workflow result. No workflow was dispatched. Full returned run records, source
cleanliness, literal-parent/full-series and full-index binary-diff equality are
in `final-ci-source-disposition.json`. The two active HaveAPI jobs were left intact;
their eventual result is outside this bounded observation.

No additional runtime, package suite, cache, VM, source change, default mutation,
cleanup or lifecycle action was performed. Diagnosis/fix ownership is retained.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
