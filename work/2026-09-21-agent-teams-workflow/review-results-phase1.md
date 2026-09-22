# Phase 1 mandatory review results

## Review identity and scope

- Reviewer: retained independent `reviewer_xhigh`
- Model and effort: `gpt-5.6-sol`, `xhigh`
- Context: fresh for the first review; retained for relevant reruns
- Risk: high, because the change establishes a versioned cross-project package,
  execution-policy and rollback contract
- Lanes: general, architecture/repetition, scope/proportionality and
  risk/compatibility
- Reviewed ranges: the exact three ranges in `review-packet-phase1.md`

## Findings

### Blocking: generic watcher policy duplicated site choices

The generic `dev-session-monitor` skill and durable guide still mandated
Luna/low. That contradicted the new contract in which concrete watcher model and
effort belong only to the site's pinned utility policy, and caused unmanaged or
other downstream packages to invent the same lineup.

Decision: fix. The generic skill will retain watcher behavior, operation scope,
ownership, fallback and result boundaries, but resolve managed settings from the
pinned utility record. An unmanaged session must have explicit applicable
caller/site policy or visibly use parent monitoring.

### Blocking: unmanaged creation overrode effective Codex configuration

The new generic resolver converted omitted model/effort into the product model
catalog's advertised default and then passed those values explicitly. Codex's
effective configured model may differ from the product-catalog default, so this
violated the promised unmanaged/native path. The portal and guide also retained
obsolete Astra labels.

Decision: fix. Omitted unmanaged settings will remain omitted through native
thread creation; only explicit settings are validated and passed. Generic UI and
documentation will describe native/automatic resolution without naming a site
model. Focused tests will prove omission rather than infer an App Server setting
from `models/list`.

### Important: team and native identities could collide

`team_digest` did not include the team name, so two differently named equal
definitions had the same identity. Native names included catalog/team/role/effort
but not generator/native-adapter identity or the behavior-instruction payload,
so a retained old generation and a new generator revision could reuse a name.

Decision: fix before long verification. Team identity will include the name;
native identity will cover generator, adapter and exact behavioral content, with
regression assertions.

## Other conclusions and residual coverage

The reviewer found the commit split coherent and found no additional security
or authorization defect. Site role/effort combinations, three retained
specialists plus one watcher capacity, behavior-only generated TOMLs, null
package metadata and optional organization forwarding otherwise matched the
packet.

The implementer will also extend forbidden-setting checks to the utility TOML.
Native-adapter parsing, remote model availability, combined downstream pins,
long package checks, catalog registration and live smoke/rollback remain later
gates. No long verification starts until Blocking and Important findings are
resolved and the affected review lanes accept the amended commit.

## Remediation status

All accepted findings are implemented in amended generic commit
`39bfa664298443334d12b08dd42a475eef1c38e4`. Focused Go tests for
`workspacecodex`, `web` and `workspace-portal`, plus canonical validation of the
changed monitor skill, pass on clean head `b5eafc664` under a fresh Luna/low
operation watcher; the final head differs only by the independently evaluated
Nix regression assertion described below.

The retained reviewer reran every affected lane and accepted all original
findings as resolved, with no Blocking or Important finding. It left one
Advisory: metadata/content tests did not independently recompute the native
name, so a future removal of identity from the production name input might have
escaped the test. The implementer fixed that test-only gap in final commit
`39bfa664`; Nix parse, diff and drvPath evaluation pass. Per the review workflow,
this narrow test strengthening does not require another reviewer rerun.

The subsequent long package/check batch passed on exact final generic,
organization and site heads. See `verification-phase1.md` for commands, local
override topology, durations and logs.
