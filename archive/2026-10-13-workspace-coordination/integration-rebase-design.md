Extend the dated helper with optional, independently reviewed patch-equivalence evidence. Keep preparation, approval, submission, execution and recovery in the selected runtime. Append the change after `aadaa171`; preserve the original integration plan and create a new plan for the remaining configuration and workspace merges.

This is a design report for the parent to retain as `integration-rebase-design.md`. No files, session state or repositories were changed, and no agents were spawned.

The inspected evidence supports this bounded extension:

- Runtime and extension merge receipts report `succeeded`, with exact remote heads `a10af6c4` and `c697acc7`.
- Configuration now has `abc0dae8` and `9a481ba1` above `8bf9da9c`. Its saved range-diff matches the runtime’s canonical command byte for byte; both commits compare equal.
- The old-to-new configuration tree difference contains only the upstream staging input update. Aitherdev’s declared channels exclude those staging channels.
- The selected package’s coordination engine files match the inspected runtime source byte for byte.
- The previous helper was consumed by successful live workers. Its historical boundary must remain visible.

**The receipt contract should stay small.**

Add optional `lineageEvidence` to the CLI’s accepted plan keys. Its value is an array of ordinary evidence references:

```json
{
  "lineageEvidence": [
    {
      "kind": "review",
      "path": "work/2026-10-13-workspace-coordination/configuration-lineage-preapproval.json",
      "sha256": "<receipt SHA-256>"
    }
  ]
}
```

An omitted field retains the existing ancestry-only behavior. Read it with a default empty array; do not insert defaults into the plan before calculating its digest.

Each referenced receipt uses these exact fields:

```json
{
  "schema": 1,
  "ownerId": "55e83d75-cb96-417a-9308-11d3caf22dcd",
  "reservationId": "d114323d-806c-479f-b7a4-8c1a08afb45b",
  "mapping": {
    "repository": "vpsfree-cz-configuration",
    "target": "refs/heads/master",
    "from": "fbbda8e90f44270eadc38c482b2f33a743e6252c",
    "fromBase": "0e394507395c04a6c11fd6d25c8284621061c140",
    "to": "9a481ba1c69a0f22a7e84e3353d676911df2271e",
    "toBase": "8bf9da9c3be811b3e5666ccd4177c9c63e537171",
    "relation": "patch_equivalent"
  },
  "decision": "accepted",
  "reviewer": "<actual independent reviewer identity>",
  "artifacts": [
    {
      "kind": "range_diff",
      "path": "<session artifact>",
      "sha256": "<SHA-256>"
    },
    {
      "kind": "verification",
      "path": "<session artifact>",
      "sha256": "<SHA-256>"
    },
    {
      "kind": "migration_review",
      "path": "<session artifact>",
      "sha256": "<SHA-256>"
    }
  ]
}
```

The mapping deliberately has **no `approvalId`**. This is a dated pre-approval review receipt, not a canonical finish receipt. Accept only `patch_equivalent`; material replacements remain outside this extension.

Require the receipt reference and all three artifact references to appear, unchanged, in `plan.evidence`. That carries their checksums into ordinary prepared snapshots and subsequent runtime validation. Keep the receipt within the runtime’s existing bounded JSON parser. Do not create another artifact store or receipt journal.

**The helper should validate the exception at its existing ancestry gate.**

In [the helper library](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination/workspace/lib/bootstrap_merge_2026_10_13.rb:51), retain the current user-direction, deployment-condition, registration and exact-head checks. Separate the final ancestry test so a nonancestor head requires one matching validated receipt.

For each supplied receipt:

1. Validate its reference and every artifact with the selected engine’s `lineage_evidence`. Require exact receipt/mapping keys, schema 1, the current owner and reservation, accepted decision, and a nonblank reviewer identity. Require exactly one artifact of each prescribed kind.

2. Bind `repository` and `target` to the existing frozen inventory and current registration. Bind `from` to that repository’s `deploymentEvidence.sourceHeads` value and `to` to its exact final registered head. Confirm the reservation contains applied, owned deployment coverage for `from` under that repository/target.

3. Require four full commit hashes resolving in the canonical owned repository. Require each base to precede its respective head, nonempty ranges, and `from` not ancestral to `to`. Reject duplicate, conflicting, unused or intermediate mappings. Every nonancestor repository needs exactly one mapping; ancestral repositories need none.

4. Call the selected engine’s `ordered_patch_ids` for both exact ranges and require identical ordered arrays. Its existing merge-commit refusal and patch semantics remain authoritative. Do not reproduce that algorithm.

5. Regenerate the range-diff using the same invocation as ordinary lineage validation:

   ```text
   git range-diff --no-color --creation-factor=80 FROM_BASE..FROM TO_BASE..TO
   ```

   Use the engine’s bounded capture/digest facility and require the digest to match the frozen `range_diff` artifact.

The independent reviewer must assess the complete ranges and recorded original base; matching arbitrary suffixes is insufficient. The existing corrected inventory establishes the original configuration base.

The relevant existing runtime methods are [here](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination/dev-workspace/libexec/workspace-coordination-execution.rb:458). Do not call `validate_replacements` prematurely, manufacture an approval, or monkeypatch its requirements.

After `prepare_merge` returns, add one operation-specific check: if this repository has a lineage mapping, its snapshot must contain the mapped repository, target and final head, with both `comparisonBase` and `expectedRemoteHead` equal to `toBase`. Otherwise refuse before publishing the helper bundle. Apply the same immutable-field check when loading that bundle for execution.

This closes an important gap: preparation must not approve a shorter or different range after another target advance. Avoid comparing `toBase` to today’s remote head on completed execution retries; successful integration necessarily advances that head.

Preserve receipt-aware retry ordering. In particular, do not add eager live snapshot validation before ordinary approval/submission receipt retrieval. Keep generation, lifecycle, reservation and supervised-exclusion checks, owner-only claims, independent workers and reconciliation unchanged.

**Keep pre-approval review and eventual finish proof distinct.**

There are three different identities:

| Identity | Meaning |
|---|---|
| Preparation request UUID | Identifies the helper preparation request |
| Bundle `approvalId` | Request UUID used for the ordinary `approve` mutation |
| Submitted job’s `approvalId` | Actual approval record UUID generated by the engine |

The eventual canonical finish mapping needs the **third** value. The bundle’s misleadingly named field is not that approval record.

After successful configuration submission, obtain the actual approval ID from the retained job. Before constructing a separate canonical receipt, verify:

- the approval belongs to this owner and is a merge approval for configuration/master;
- its `reviewedSnapshot` resolves to the retained merge snapshot;
- that snapshot binds `to`, `toBase` and the expected target;
- its source records the unchanged user direction.

Create a new canonical receipt at a new path, adding that actual `approvalId` to the exact reviewed mapping. Its outer replacement entry adds the ordinary checksummed `evidence` reference. Leave the pre-approval receipt and its hash unchanged.

The independent review should explicitly cover this deterministic post-submission binding. If it does not, obtain the reviewer’s confirmation before describing the completed mapping as independently accepted. A generated UUID does not require renewed user merge authorization.

Preparing this evidence does not authorize calling `finish`. Ordinary finish still checks integration, current final heads, cumulative deployed revisions, live identities and explicit completion. This design establishes the latest configuration rebase mapping only; it does not certify every historical deployment in the reservation.

**Use a new frozen plan and retain the consumed history.**

Create, for example, `bootstrap-integration-remaining-plan.json`. Preserve the existing four-repository inventory shape and unchanged source quote. Retain runtime/extension heads, select configuration `9a481ba1`, and freeze the final workspace head after the new helper commit and review.

Include the new lineage receipt, final review, verification and application-equivalence evidence. Preserve:

- `bootstrap-integration-plan.json`;
- every accepted preparation/execution request and immutable bundle;
- successful runtime/extension job and attempt receipts;
- the configuration refusal and existing range-diff;
- deployed sources, roots and published predecessor refs.

Use fresh preparation UUIDs for configuration and workspace. Do not pair an old execution request with the new plan: the existing `planId` binding should reject that.

Append one focused workspace commit containing the CLI allowance, validation, focused tests and dated-procedure update. Keep `aadaa171` as the live-consumed predecessor; do not fold this extension into it. No runtime, extension, input-pin, queue or installed-interface change is needed.

Prove that the final workspace application derivation remains:

```text
/nix/store/67hrxj2dfimf4dphv4xhbwdfkmcfkhf8-dev-workspace-0.2.0.drv
```

Retain the selected package, profile token and coordination catalog bindings. If the derivation changes, stop this source-only route and investigate before accepting the existing deployment as sufficient.

**Verification should concentrate on the new admission boundary.**

Before final review, run syntax checks, applicable hooks and complete-range `git diff --check`. Extend the existing private-Git helper fixture using the actual selected Engine/Worker:

- A deployed feature rebased over unrelated upstream work refuses without lineage evidence and succeeds with the exact accepted receipt. Preparation needs no pre-existing merge approval.
- Changed patches, reordered or omitted commits, and merge-containing ranges refuse. Exercise invalid bases and stale prepared `comparisonBase`.
- Wrong owner/reservation/repository/target/head, unused or conflicting mappings, missing review fields, altered receipt/artifacts, and noncanonical range-diff bytes refuse before approval or job admission.
- The new plan cannot consume an old plan’s request/bundle. Existing ancestry-only plans retain their behavior.
- Approval-only interruption and completed execution retry preserve one ordinary approval/job. Reservation and deployment history remain unchanged.
- In the private fixture, the pre-approval receipt cannot satisfy canonical replacement validation. A separately constructed canonical receipt using the actual job approval ID can satisfy it after integration.

Do not stub `ordered_patch_ids` or `lineage_evidence`. Reuse existing worker/recovery tests rather than duplicating the coordinator’s suite.

For configuration `9a481ba1`, retain the complete two-commit inventory, both exact ranges, ordered patch IDs, canonical range-diff and explicit no-migration conclusion. Verify the final lock preserves `devWorkspace=a10af6c4` and contains only the inherited staging changes beyond deployed `fbbda8e9`. Run the deployment composition check against the final workspace/configuration pair.

After review, perform the scoped build-only aitherdev verification through the configuration’s Nix environment. Compare its evaluated inputs and system output with the deployed build, explaining any metadata-only difference. Keep activation outside this work. The saved configuration CI inventory is empty; record applicability honestly rather than treating it as a passed check.

Run affected workspace checks after review. Existing successful systemd interruption evidence can cover unchanged dispatch/reconciliation; repeat it if implementation changes those paths or their validation ordering. Long or uncertain checks belong to the parent’s fresh verification watcher.

**Final review needs all four affected lanes.**

This changes an authorization prerequisite for external Git publication, so classify it high risk. General, architecture/repetition, scope/proportionality, and risk/compatibility all apply. Use the eligible previous independent reviewer under the mandatory-review policy; this design author must not supply the independent acceptance.

Provide the complete final workspace series and configuration series, final diffs, consumed-helper provenance, consolidated pin inventory and explicit no-migration conclusion. Reuse unchanged runtime/extension conclusions and successful integration receipts. The reviewer should explicitly assess the pre-approval/final-receipt distinction, exact-base binding, evidence integrity, retry behavior and unchanged application derivation.

**Execution remains serial and recoverable.**

After review and verification, the parent rechecks live ownership and the supervised exclusion, captures final comparisons, then prepares and executes configuration followed by workspace. Keep the original four-repository authorization; the reviewed clean rebase does not require another permission question.

The configuration preparation refusal created no replacement job according to the supplied evidence; confirm that live before proceeding. There is then nothing to cancel merely because preparation failed.

For later refusal or interruption:

- Preserve all evidence and use the exact saved execution request for an admitted operation.
- A changed baseline requires new verification and a new frozen plan/request, after resolving any existing operation.
- An unclaimed `needs_refresh` job follows ordinary cancellation and fresh preparation.
- Claimed or uncertain effects remain with the original worker/reconciler. Never replace them to escape recovery.
- Generation, ownership, lifecycle or evidence drift stops new admission.

No ledger or worker format changes are introduced. Existing readers and recovery continue consuming ordinary records. An older helper rejects the new optional plan field; preserve it for historical evidence rather than altering its accepted inputs. No coordinated machine update or package rollback is required.

- **Phase:** Design complete; implementation and final acceptance remain.
- **Completed:** Required guidance, source and named evidence inspected; canonical configuration range-diff confirmed.
- **Remaining:** Parent implementation, quick checks, independent review, scoped verification and two coordinated merges.
- **Material limits:** This shell has no bound session; parent must verify live ownership. Finish/release remains unauthorized.
- **Next:** Retain this report and append the focused source-only helper change.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-13-workspace-coordination/)