# I1 catalog prompt evidence

Ready for acceptance. Only `config/agent-teams.nix` instruction strings changed.
Commit `6d9e28a585c30a497d86c963cb9666b04cb317c6`, parent
`acd8262f07ae3781f36b10c13e1bb924cc62c75b` (I0). Package comparison baseline
`8fe5976e926e7df0c3edca920618ff872abcc526`; catalog content was unchanged by I0.
Owned diff: 1 file, 12 insertions, 9 deletions. Exclusive commit/index window
released after successful commit and clean feature worktree/index. Capacity available.

Changed common lead accountability, delegated triage/acceptance/owner execution,
verified-roster design fallback and concrete observer duplication guidance. No
settings, schema, runtime behavior, fixture or test source changed. No design
deviations. Existing role prompts constrain length to 4096 bytes and pin several
phrases; final wording preserves those assertions and design meaning.

## Checks

All checks ran in `worktrees/2026-11-25-team-lead-delegation/workspace` against the
final committed catalog content, before commit. No source change followed them.

- `nix-instantiate --parse config/agent-teams.nix >/dev/null`: pass.
- `nix-instantiate --eval --strict --json config/agent-teams.nix`: pass.
- `git diff --check -- config/agent-teams.nix`: pass.
- Existing pure catalog jq predicate in `flake.nix`'s `agent-team-policy` check:
  extracted unchanged and run directly against strict evaluated JSON: exit 0,
  `true`. This avoids building the runtime package. All pinned phrases, roles,
  policy values and nonempty/at-most-4096-byte instruction constraints pass.
- Baseline `git show 8fe5976e926e7df0c3edca920618ff872abcc526:config/agent-teams.nix`
  was evaluated from a temporary file with the same strict JSON command. Python
  recursively removed only dictionary keys named `instructions` from old/new
  JSON, preserving all other keys/list order/values, and asserted deep equality:
  pass. All 8 presets, schema 6, models/efforts/access, purposes, capacity 9,
  routing, lifecycle, work policy, utilities and descriptions are identical.
- Four distinct lead mode prompts remain. UTF-8 byte counts: Full-team 4087,
  Lead-designed 4063, Lead and reviewer 2817, Solo 2595; observer 4021.
- Hook inspection: no declared hook framework, configured core.hooksPath or active
  non-sample repository hooks found. Ordinary commit used no hook bypass.

Reproducible existing catalog predicate invocation (Python):

```python
catalog = subprocess.check_output([
    'nix-instantiate', '--eval', '--strict', '--json', 'config/agent-teams.nix'])
flake = Path('flake.nix').read_text()
start = flake.index('        agent-team-policy =')
match = re.search(r"/bin/jq -e '(.*?)' \"\$catalog\"", flake[start:], re.S)
subprocess.run(['jq', '-e', match.group(1)], input=catalog, check=True)
```

No broad runtime/package build, deployed-package metadata/native-config check or
long integration test was run; those unaffected consumer outputs were not claimed
as verified. No new exact-text tests were introduced.

## Semantic scenarios

Read final evaluated prompts against accepted D; all pass:

| Scenario | Final instruction effect |
| --- | --- |
| Full-team unclear diagnosis | Triage ends at assignable question/owner/acceptance; delegate uncertainty and specialist investigation. |
| Completed package lacks evidence | Return gap/failure to owner; assembly may be delegated with capacity; lead checks completeness. |
| Unchanged passing checks | No duplicate specialist checks; additional execution needs changed inputs, contradiction or required unrun coverage, with reason/owner. |
| Busy, unready, blocked or inaccessible member | Does not establish absence; identity/access failures are resolved/reported without takeover. |
| Small direct brief | Relaxes document ceremony while retaining execution ownership. |
| Solo / Lead and reviewer | Existing lead investigation/design/application-edit instructions remain; review stays independent. |
| Lead-designed | Existing substantive lead design remains; delegated execution and acceptance stopping rules apply. |
| Approval/safety actions and writing | Lead retains approvals, repository/machine ownership/freshness, mutation drivers and required writing; owner prepares operations/checks/evidence/fixes. |
| Retained prompts | Retain settings/prompts/mode and escalate conflicts; no saved snapshot refresh or roster mutation. |
| Observer concern | Requires concrete work/ownership/missing reason from existing evidence; recognizes acceptance/mode/safety/writing/blockers; clocks/idle/ready alone prove neither duplication nor capacity. |

## Consumer and documentation routing

Already-inspected concrete consumer: `flake.nix:31` imports this catalog as
`teamConfig`; `flake.nix:59` passes it into the selected extension's
`lib.mkPackage`. `flake.nix:199` defines the `agent-team-policy` consumer check,
which reads exported `${package}/share/dev-workspace/agent-teams.json` and
`${package}/share/dev-workspace/package.json` at lines 205-206. Direct catalog
assertions pass; package export/build verification is outside I1 and unclaimed.

Topic -> reader/class -> authoritative home -> evidence:

- Delegation/acceptance/owner execution -> future team members, reusable contract
  -> `docs/agent-teams.md` plus concise AGENTS/verification routes -> I0 owns the
  accepted D documentation package and confirmed no semantic mismatch on I1 diff.
- Future selected role prompts -> catalog consumers -> `config/agent-teams.nix`
  -> this commit, strict evaluation, invariant comparison and semantic scenarios.
- Exact execution/review limits -> lead/reviewer, temporary evidence -> this file
  and lead-owned plan/state/review packet -> commands/results above.

No separate project documentation is useful for this string-only package;
reusable prose is I0's assigned deliverable. Shared instructions apply when read;
catalog prompt rollout requires a later authorized package deployment and does
not rewrite retained members. This package did not push/deploy/merge/reconfigure.

History: one logical I1 commit after I0; no superseded approach commits, repeated
pin/update stream or obsolete transitional source retained. No migrations,
persisted-state/API/protocol changes, or merged/released/deployed/externally
consumed migration lineage. Lead/P own complete branch packet and independent
review invocation; independent final review remains outstanding at I1 handoff.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-team-lead-delegation/
