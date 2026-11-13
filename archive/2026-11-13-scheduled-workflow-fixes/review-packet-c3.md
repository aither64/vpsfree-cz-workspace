# C3 final review packet

Independent final review of completed, committed provider and two consumers.
All three worktrees/indexes are clean; quick checks pass. Lead independently
verified HEAD, merge-base, complete one-commit series, diffstats and whitespace.
No long C3 acceptance has run. Owner reports and raw diffs are in
[evidence-c3.md](evidence-c3.md) and [evidence-b2.md](evidence-b2.md).

## Requested behavior and scope

The user rejects transitive inputs anywhere in generated commit messages and
requests corrected confctl in both named configuration repositories. Guarded
messages must describe only explicit logical input selections: title, revision
summaries and Git logs. If a valid guarded update changes only dependencies,
emit only `inputs: update <sorted requested names>` without invented revision
changes or dependency detail. Keep complete ancestry checks, callbacks, results,
installation, selected aliases, ordinary hooks and file-backed message transport.
`--no-changelog` remains authoritative; direct Nixpkgs calls already use it.

The first uncommitted C3 log-only filter retained descendant summaries and was
superseded before commit. It is not final source or accepted runtime evidence.
No new CLI option, Setter change, repo-name heuristic or consumer sweep.
Provider integration precedes both pins; user merge/run approval and later
explicit adoption request are recorded in plan/state.

## Exact complete final ranges

All paths beneath
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/`.

| Repository | Base | Final head | Complete series |
| --- | --- | --- | --- |
| confctl | `4c636b40b53b143fda6d9cad9332ce8b7b86bdb8` | `ff5e017780a35fb97b549db2a51b570193867c3b` | One: inputs: scope guarded commit messages to selected inputs |
| vpsadminos-org-configuration | `8306d29d09f1939d1f92d44b5a5e241429b40c2e` | `69edee80f3ca49515f1ac562dfb3a0c5dbd960d5` | One: ci: use selected-input confctl commit messages |
| vpsfree-cz-configuration | `454c94c4eb1315f74e23b2126187c2a27eb3868a` | `07a85cae5fdb4525e4ce2cca28a05a0888be8e0c` | One: ci: scope automated input update messages |

Provider: five files,172 additions/5 deletions, mostly focused additions in
existing specs. Two source files and eight-line existing-doc clarification.
Each consumer: one `CONFCTL_FLAKE` replacement,1 addition/1 deletion; no command,
flag, action, hook, authority, schedule, manual event or configuration lock change.
All three feature heads published with exact remote proofs in owner receipts.

No migrations in any range; no schema/runtime API/persistent-format changes.
Merged C1/B1/C2 history is protected and remains ancestral. Provider has no
dependency stream. Org's unmerged6874f605 tool pin was consolidated into69edee80
above merged8306; old/new source differs only by final provider hash. vpsFree's
one additive tool pin preserves mergedB1 and automated default updates through454c.
No obsolete approach is committed in these final series. Reviewer must assess
these whole-history/migration/update-stream conclusions independently.

## Owning interface, documentation and compatibility

Owner is Inputs::CommitMessage, called by guarded Inputs::Updater with optional
internal selected_inputs. Nil/default manual and Setter behavior stay intact;
true original empty changes remain errors. GuardedUpdate's full callback/result
is not filtered. Relevant callers and six bounded consumer dispositions are in
design.md C3; only both named configuration committing OS calls need adoption.
Existing custom-message callers do not generate confctl messages.

Operators reach reference/how-to `docs/flake-inputs.md` from confctl README.
The short paragraph documents lasting selected-message, title-only fallback,
no-changelog and complete-graph-validation semantics. Lead directly applied the
required writing pass; owner checked factual fidelity. Individual history,
source/input identities and rollout evidence stay in session records. No docs
move, new runbook, upgrade retirement or navigation change. Each workflow owns
its immutable CLI pin. Recovery is additive reverts, with merged C2 transport
retained; no machine rollout, schema conversion or coordinated service update.

## Quick evidence and held acceptance

- Provider changed final specs:41 examples/0 failures; four-file RuboCop/syntax,
 50 tracked Nix format checks and ordinary commit hooks pass. Unchanged prior
 guard/graph/CLI/manual/Setter scope retains passing evidence from107 examples,
 explicitly limited where superseded assertions were changed.
- Org inverse pin-only byte/YAML comparison, all five shell bodies, whitespace
 and ordinary hooks pass; actions unchanged.
- vpsFree inverse pin-only comparison, YAML, seven shell bodies, locked
 actionlint1.7.12, whitespace and ordinary hooks pass under freshly prepared
 Ruby3.4.11 native bundle; old B1 native cache not activated.

After review, owner1 runs full repository checks and actual packaged mixed-input
selection/full-guard rejection proof under a fresh watcher. Source specs alone
are not packaged acceptance. Both final master workflows then need fresh runs,
actual generated message inspection and final check/push proof. No old-event
reruns or hosted success claims at these successors yet.

## Assignment

Reviewer0 retains saved gpt-6.1-sol/xhigh/read_only, thread
01a1d53b-f8ca-7383-8a79-41928077c6df. All four lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility. Conservative
high risk because this changes generated default-publication messages adjacent
to ancestry enforcement and is consumed across repositories. Keep review read-only
and return the report to lead for persistence. No nested reviewer or checks.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-scheduled-workflow-fixes/)
