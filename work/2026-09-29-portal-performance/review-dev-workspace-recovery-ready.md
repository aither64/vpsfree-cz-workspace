# Review packet: retained ready creation records

## Requested outcome

Independently review the committed archive-recovery correction at dev-workspace
head `e58f8f6` against the September 30 amendment in `design.md`. Determine
whether the candidate adapter safely accepts a normal durable `creation.json`
record only after session creation completed, while continuing to fail closed
for unfinished, malformed, mismatched, unsafe, or competing operation state.

Acceptance requires that recovery remains limited to the named existing
`tracking_committed` archive journal, performs no profile/service/Codex change,
validates rather than repairs creation state, proves the creation goal binding
before root/member proof or executor invocation, and preserves the selected
predecessor as lifecycle executor.

## Initiative and scope

- Initiative: `2026-09-29-portal-performance`
- Plan/state: `work/2026-09-29-portal-performance/{plan,state}.md`
- Design: `work/2026-09-29-portal-performance/design.md`, section
  “Retained ready creation records: September 30 correction”
- Repository/worktree: `dev-workspace` at
  `worktrees/2026-09-29-portal-performance/dev-workspace`
- Previously reviewed recovery head: `fbd7a9e390b563f83d1787e2cddbd516eefeb558`
- Correction head: `e58f8f6` (`session: accept retained ready creation records`)
- Correction diff: `git diff fbd7a9e..e58f8f6 -- libexec/workspace-host test/workspace_host/archive_recovery_test.rb`

The intended commit split is one inseparable correction commit: the adapter
classification/binding change and its focused positive/negative regressions.
The broader recovery implementation and earlier safety remediations remain in
the already-reviewed `4999212` and `fbd7a9e` commits.

## Trigger and evidence

The first authorized packaged recovery attempt for
`2026-09-26-codex-queue-ledger-capacity` failed before any proof helper,
executor, journal mutation, profile change, service change, or Codex mutation:
`conflicting session operation blocks archive recovery`. Evidence is in
`work/2026-09-29-portal-performance/recover-2026-09-26-codex-queue-ledger-capacity.log`.
The exact conflict was the session's retained schema-1 `creation.json` with
`state: ready`; the archive journal remained at `tracking_committed` and the
selected profile remained the predecessor.

## Behavior and boundaries

- `creation.json` is removed from the adapter's unconditional operation-conflict list.
- If absent, the existing legacy/root-only recovery case remains accepted.
- If present, the adapter uses `require_safe_private_file!` and the existing
  `read_private_creation_journal!`, requires `state == ready`, and compares the
  journal `goal_sha256` with the already-read archived manifest creation goal.
- A nil journal goal matches only an absent manifest key; an explicit null
  manifest value is not treated as absence.
- Start, fork, agent-team migration, removal, revive, and every other
  non-archive lifecycle journal remain blockers before proof/executor work.
- No new parser, schema, journal write, force flag, general bypass, browser
  interface, runtime contract, service/profile transition, or Codex operation
  is introduced.

Rejected alternatives: treating every creation record as a conflict; relying
only on the predecessor's creation lock; duplicating creation-schema parsing;
reconciling or deleting the creation record; weakening ordinary switch
preflight; or bypassing lifecycle ownership.

## Verification

Lead-repeated quick checks at `e58f8f6`:

```text
ruby -Itest test/workspace_host_test.rb --name '/recover_archive|normal_switch_still_refuses_journal|candidate_switch_still_refuses_an_unfinished_creation/'
10 runs, 170 assertions, 0 failures, 0 errors, 0 skips
ruby -c libexec/workspace-host
Syntax OK
ruby -c test/workspace_host/archive_recovery_test.rb
Syntax OK
git diff --check
PASS
```

Coverage includes valid retained schema-1 with historical tracking digests,
supported schema-2/3, absent legacy record, legacy null/absent goal, byte
preservation, creating state, malformed JSON, wrong slug, unsafe mode,
goal mismatch, invalid preserved-tracking shape, unknown schema/state,
oversize, symlink, nonregular path, explicit-null manifest goal, and competing
start/fork/migration/removal/revive journals. Existing selected-executor/helper
substitution, retry, and normal switch refusal tests remain passing.

## Risk, lanes, and reviewer

- Risk: **High**, because this changes host lifecycle recovery around persisted
  session state, archive completion, deployment blocking, and mixed-generation
  execution.
- Reviewer: retained `reviewer0`, saved `gpt-6-sol` / xhigh / read-only; no
  model or effort override.
- Lanes: General; Architecture and repetition; Scope and proportionality; Risk
  and compatibility.

Read `/home/aither/.codex/skills/mandatory-change-review/SKILL.md` and all four
selected lane references before reviewing. Inspect the commit and surrounding
creation/archive contracts directly. Report findings by severity and lane;
state clearly if there are no findings and identify residual test or rollout
risks.

## Compatibility, deployment, and consumers

The owning component is `dev-workspace`'s packaged `workspace-host` operator
interface. Its only consumer is the explicitly invoked packaged
`recover-archive --source ... --workspace ... --session ...` bootstrap used
before normal profile switching. The private runtime contract remains byte
compatible with the selected predecessor; the candidate helper is substituted
only into the predecessor-generated `--portal-command` argument.

Current downstream feature pins still point to reviewed pre-correction heads:
`vpsfree-dev-workspace` `02e88f5` pins `fbd7a9e`, and workspace `7a6289a` pins
that extension. They will be mechanically repinned only after this correction
passes review. The selected live profile remains the old package. There are no
database, persisted-format, protocol, or journal-schema migrations, and no
migration version has been merged, released, deployed, or externally consumed.
No additional public documentation change is useful for this correction. The
existing recovery documentation already limits the command to the exact late
archive journal, says it cannot rewrite creation journals, and requires failures
to leave the journal in place. The design amendment owns the private ready-record
validation detail; the implementation is being aligned to that recorded contract.
