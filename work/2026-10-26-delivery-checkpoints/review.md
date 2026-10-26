# Independent final review

## Findings

**Blocking — expanded lead instructions make the composed catalog invalid.**
`workspace/config/agent-teams.nix:13`, commit `098324dbe`, appends delivery
guidance to every lead prompt. Evaluating the final catalog produces **4,731
bytes** for each Full-team lead (`delegated` through `delegated_6`) and **4,457
bytes** for `lead_designed`. The runtime's existing
`portal/internal/agentteams/catalog.go:603` accepts role instructions only up to
4,096 bytes; `validTeam` applies that rule to the lead and catalog decoding
rejects an invalid team. `agentteams.LoadInstalled` therefore rejects this
catalog, and configured portal construction fails at
`portal/internal/web/server.go:423`. This affects the entire composed catalog,
not just selecting those presets.

Shorten the concatenated lead instructions, preferably removing repetition and
keeping the new checkpoint concise. Preserve the existing persisted instruction
limit. Recheck every evaluated role against 4,096 bytes before the composed
build. A strict Nix evaluation by itself does not validate this runtime contract.
This is a general/risk-compatibility finding within the supported package
boundary, not additional hardening.

Evidence (quick, read-only evaluation in the workspace feature worktree):

```sh
nix-instantiate --eval --strict --json --expr \
  'let c = import ./config/agent-teams.nix; in builtins.mapAttrs (_: t: builtins.mapAttrs (_: r: builtins.stringLength r.instructions) t.roles) c.teams'
```

No other Blocking or Important findings identified.

## Scope and architecture

Reviewed the accepted outcome in the packet, plan and design before detailed
implementation. The runtime change is 10 files, +583/-71, including focused tests
and 53 documentation lines; site policy is four files, +52/-9, followed by one
mechanical runtime selection update. The mechanisms correspond to the requested
scope: ordinary Git statistics, existing activity counters, same-session log
paths, scheduled stock-policy compatibility and concern resolution. There is no
new timing service, test framework, approval workflow or general roster
migration. Existing provider ownership and the site/runtime boundary are sound.
No disproportionate subsystem or unnecessary hardening found. Commit times alone
do not establish recorded working time, so this review does not infer it from
session age.

## Whole-branch history, migrations and update streams

- Runtime: reviewed the complete merge-base-to-head range
  `120c7b9c4a55c63d168b0859099a6829505bbcdf..f8b94441a6b5066973a72284955b793b301c60ac`.
  It contains one focused behavior/tests/docs commit. No obsolete branch
  approaches, transitional shims or separate follow-up fixes remain.
- Workspace: reviewed feature commits `098324dbe2d7d80d4879cbb717c9d01274a5fe7f`
  and `f34fec1303139dd91a8faeaba97f6c2dce775276` above shared master
  `32c42e3edf4925acf48628b29fff8852720feb45`. Also checked the full series from
  remote merge base `08d241e2dcaa7f6a8b12dc7d9d407074bda8ab2d`: the additional
  `32c42e3ed` commit contains only this initiative's initial tracking records.
  Policy and mechanical pin are independently reviewable. No obsolete history
  remains.
- **No migrations.** Optional progress-state fields retain schema 1. There is
  no intermediate schema lineage to consolidate. Per the supplied provenance,
  none of the new behavior/state has been merged, released, deployed or
  externally consumed.
- **No repeated update streams.** The only runtime pin update selects
  `f8b94441a6b5066973a72284955b793b301c60ac` in `f34fec130`; the extension
  revision/content hash, sibling inputs and input topology are unchanged.
  No redundant pin commits need consolidation.

## Compatibility and verification limits

The generic runtime owns evidence collection and progress state; the site
catalog is the concrete consumer selecting this runtime. State fields are
optional, and old readers ignore/drop them. Old observer packages retain their
earlier concern semantics; the supported rollout is forward. Exact released
stock instructions receive the scheduled-turn update, while saved custom
instructions, model, effort and access remain retained. Existing session
identity checks, pending-send identity, active-work scheduling and owned-turn
timeout paths remain intact. This change does not select a host package or
authorize configuration integration/deployment.

Reviewed focused tests and the reported quick-check evidence; independently
ran whitespace checks for both ranges and the catalog-length evaluation above.
No long tests, source edits, other-session inspection or nested agents were
used. The composed build remains pending and must follow the Blocking fix.

Residual limits: activity counters are explicit lower bounds, concern-resolution
evidence remains model judgment, and a truncated/incomplete initial evidence
packet conservatively prevents on-track settlement even when the observer could
inspect additional sources itself. The existing restart quiet-success test
still uses the old evidence-free result, so it establishes quiet settlement,
not successful on-track acceptance under the new rules. These do not warrant
new infrastructure or broader scope for this change.

Reviewer: fresh standalone `/root/delivery_review`, catalog-selected
`gpt-6.1-sol` / `xhigh`; fallback required because this tracking-only initiative
has no managed lead thread or eligible retained reviewer. Risk: high for optional
persisted state and scheduled-policy compatibility. Lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility. Read the
mandatory-change-review skill and all four lane references in full.
