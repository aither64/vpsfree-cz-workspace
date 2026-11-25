# Package E review evidence

Status: accepted by lead, independent final review found no findings, and the
exact reviewed feature head is published. See [R2](review-policy.md) and the
publication receipt below. Both exclusive Git windows are finished.

## Scope and revisions

User direction: improve the synchronization rule after rejecting unrelated
Go/Rust refresh for the declaration-neutral query fix. Implementation follows
the accepted [A3 brief](design.md#package-a3-gate-client-synchronization-on-declared-contract-changes)
without deviations, additional tooling or an API/client investigation.

- Repository: `vpsfreecz/vpsadmin`, target `master`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-exception-root-cause/vpsadmin`.
- Branch: `2026-11-25-exception-root-cause`.
- Complete branch base: `81e930b25fa3252d7e849aff4819e663cec37b07`.
- E parent / previously reviewed and published API head:
  `da7724abdc080e59820cc4f0812ce1a41b3fc5df`.
- E final head: `6c16d04555e79c7789ac7213da2064c540afc83c`.
- E files: `AGENTS.md` and `docs/api-schema-export.md`, 39 insertions / 12 deletions.
- Full branch diff: four files, 75 insertions / 37 deletions.

Identity was verified with `dev-session current` in the bound session directory.
Both identity environment variables were absent, matching the trusted binding.
The live same-session roster confirms implementer2's saved `workspace_write`,
`gpt-6.1-sol` / `xhigh` and exact thread. No prior package was pending.

## Final behavior and manual checks

Every API task reads the existing authoritative section and first assesses the
complete base-to-head source diff for declaration changes, including indirect
plugin/concern/dynamic declarations. The guide covers resources, actions,
inputs/outputs, requiredness, types, choices, nullability, defaults, routes,
API/protocol versions and relevant metadata.

Manual policy fidelity against both outcomes passed:

- A query-ordering-only change stops after one concise record of exact base/head,
  relevant files and reason. No export, client worktree, generation, comparison
  or refresh is required. Unrelated baseline drift cannot block completion;
  runtime/authorization compatibility assessment and applicable tests remain.
- An action/parameter or plugin/dynamic declaration change enters the existing
  full all-client workflow. Clean-source export, provenance, locks/profile,
  generated ownership, transformations, checks, compatibility/recovery,
  integration approval and separate release/publication rules are retained.
  Concrete uncertainty gets narrow inspection or the smallest focused check.

Reviewed the complete two-file diff and searched the local routes/procedures
with `rg -n 'API.*(task|work)|client.*synchron|behavior-only|unchanged.client|no.change'`.
The prior unconditional client-assessment/export requirement is replaced by
the assessment/stop rule. Contract-changing completion wording is conditional.
The AGENTS route changes only its label and retains its original target.

Commands/results:

```sh
git diff --check
git diff --cached --check
git diff --check da7724abdc080e59820cc4f0812ce1a41b3fc5df..HEAD
rg -n 'generated-client-synchronization|^## Generated client synchronization|\]\((docs/|#)' AGENTS.md docs/api-schema-export.md
test -f docs/api-schema-export.md && test -f docs/agent-instructions/development.md && test -f docs/agent-instructions/localization.md && test -f docs/agent-instructions/testing.md && test -f docs/README.md
nix develop .#vpsadmin --command git commit -F /tmp/exception-root-cause-E-commit-message.txt
git status --short
```

All exited 0. The retained `generated-client-synchronization` heading and both
links to it resolve. All relative AGENTS route/index targets exist. Ordinary
Overcommit pre-commit hooks passed: Nixfmt, MigrationSpecs, VpsadminWebuiI18n
and VpsadminApiI18n; no Ruby files required RuboCop. Commit-message hooks passed
with advisory TextWidth warnings for the subject and two body lines; every
line is within the required 80-character limit. No hook bypass or configuration
change occurred. Final worktree status is empty. No database, schema-export,
client-generation, API-test or long-suite campaign was launched for E.

## Source preservation and existing evidence

The following exact-parent comparison exits 0 with no diff:

```sh
git diff --exit-code da7724abdc080e59820cc4f0812ce1a41b3fc5df HEAD -- api .github flake.nix flake.lock packages nixos tools Gemfile Gemfile.lock .overcommit.yml .git-hooks
git diff --name-status da7724abdc080e59820cc4f0812ce1a41b3fc5df..HEAD
sha256sum api/lib/vpsadmin/api/resources/incident_report.rb api/spec/api/resources/incident_report_spec.rb
```

The changed-path inventory contains only the two E documentation/instruction
files. Relevant API/runtime/spec, dependency, exporter, packaging, CI and hook
inputs remain unchanged. Resource SHA-256 is
`60df1134acd89a5c7f301596270187f218332306614055ef192df1ca6aafe35e`;
spec SHA-256 is
`8a99a06fc82f8b0c6223cf1347fce31696d9aa411d3147ae18d4fcf419abc37e`.
Both equal B's tested/reviewed values. This is source-path preservation evidence,
not whole-tree identity or a claim of new-head runtime execution.

[B's packet](B-review-packet.md), [prior review](review.md), and
[export receipt](B-export-receipt.md) retain their original exact revisions and
input identities. B remains independent owner of API source/CI evidence and
the disclosed existing full-component lint limitation. Reuse passing evidence
only within its demonstrated scope; E does not recertify Nix derivations or
claim CI ran at the documentation head. Unfinished required CI remains explicit.

Contract conclusion for the exact complete base/head above: no declared API
contract change. B's independently reviewed `incident_report.rb` query ordering
correction and request-spec changes preserve declarations; E changes only this
procedure and its route label. No further export/client work is required for
this declaration-neutral branch, and pre-existing client drift is separate scope.

## Complete history, migrations and documentation placement

Complete `81e930b..6c16d045` series:

1. `da7724abdc080e59820cc4f0812ce1a41b3fc5df` —
   `api: qualify incident report detection-time ordering`.
2. `6c16d04555e79c7789ac7213da2064c540afc83c` —
   `docs: gate client synchronization on declared contract changes`.

These are two distinct requested purposes. No obsolete approach, fixup stream,
transitional compatibility path or repeated dependency/generated-input update
stream remains in vpsadmin. No migrations, schema changes or data conversions
exist, hence no merged/released/deployed/externally consumed migration lineage
needs preservation. The API parent and E head are published; neither commit
has been integrated or deployed by E. No integration, default push, deployment
or lifecycle action occurred. R2 independently accepted the complete branch
history and no-migrations conclusion.

| Topic | Readers / class | Authoritative home | Evidence |
| --- | --- | --- | --- |
| Contract assessment and synchronization | Contributors/reviewers; maintained procedure | `vpsadmin/docs/api-schema-export.md#generated-client-synchronization` | Two-outcome fidelity and retained safeguards above |
| Required API route | Repository agents; instruction entry point | `vpsadmin/AGENTS.md` | Label only; original anchor preserved |
| Exact source/check/history receipts | Lead/reviewer; session evidence | This packet and linked B records | Exact parent/head and commands above |

No documentation move or supported recovery path was removed. Exporter operation
instructions are unchanged. No user-facing/KB text or deployment procedure needs
updating. Recovery is an ordinary documentation revert with no data/process
effects. Independent final policy review and feature publication subsequently
completed as recorded below. Integration and deployment remain separate decisions.

## Reviewed feature publication

Lead accepted R2's no-findings result for the exact full branch range and
authorized normal feature publication. Identity and live saved write access were
reverified. The independent documentation commit does not supersede the runtime
fix; the user's explicit instruction retains existing valid runtime CI at
`da7724ab`. No force-push, cancellation, restart or runtime rerun was performed.

Publication commands, all exited 0:

```sh
git fetch origin
git rev-parse origin/master refs/remotes/origin/2026-11-25-exception-root-cause
git merge-base origin/master HEAD
dev-session worktree capture-comparison 2026-11-25-exception-root-cause vpsadmin --as-is
nix develop .#vpsadmin --command git push origin HEAD:refs/heads/2026-11-25-exception-root-cause
git ls-remote --refs origin refs/heads/2026-11-25-exception-root-cause refs/heads/master
git rev-parse HEAD
git status --short
```

Fresh target remained `81e930b25fa3252d7e849aff4819e663cec37b07`; feature remote
was the expected `da7724ab` parent. No rebase or source change was needed.
Comparison capture returned exact base `81e930b25fa3252d7e849aff4819e663cec37b07`
and head `6c16d04555e79c7789ac7213da2064c540afc83c`. Ordinary Nix-shell SSH push
fast-forwarded only the feature ref, without hook bypass. Fresh remote proof:

```text
6c16d04555e79c7789ac7213da2064c540afc83c refs/heads/2026-11-25-exception-root-cause
81e930b25fa3252d7e849aff4819e663cec37b07 refs/heads/master
```

Local HEAD equals the exact reviewed/published head; final worktree status is
empty. No default integration, deployment or lifecycle operation occurred.

One bounded discovery using `gh api --method GET repos/vpsfreecz/vpsadmin/actions/runs`
filtered by exact branch and `head_sha=6c16d04555e79c7789ac7213da2064c540afc83c`
returned the following push runs. Every run has attempt 1 and that exact head:

| Workflow | Workflow ID | Run ID | Discovery status |
| --- | --- | --- | --- |
| API Specs (topic parallel) | 234996228 | [45646717834](https://github.com/vpsfreecz/vpsadmin/actions/runs/45646717834) | queued |
| i18n health | 307073542 | [45646717818](https://github.com/vpsfreecz/vpsadmin/actions/runs/45646717818) | in progress |
| API Migration Specs | 303487942 | [45646718043](https://github.com/vpsfreecz/vpsadmin/actions/runs/45646718043) | completed, success |

These are newly triggered workflow identities, not a new local verification
campaign or a claim of finished runtime coverage. No watcher or duplicate
observation was launched by E. Lead owns the next CI/readiness decision; B's
original unchanged-source evidence and valid existing runs remain intact.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-exception-root-cause/>.
