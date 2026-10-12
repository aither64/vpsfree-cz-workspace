# Independent final review

Reviewer: retained `reviewer0`, native thread
`01a13084-9461-7121-8f22-b3d5f06c2591`, review turn
`01a1309e-fcd4-7771-a38b-2cc0f98d49b4`. Saved and actual native turn settings
confirmed as GPT-6 Astra/xhigh, read-only. No fallback or nested reviewer.
Completed general, architecture/repetition, scope/proportionality and
risk/compatibility lanes.

Reviewed base `8e4da52c55f1d4396547630d1d4de518f8255619` through
`a33c499f0117c189213a9cc70113f7906965f53f`, including both full commits and
the complete final diff, consumers, tests and documentation. Report delivered
to the lead through the session-bound team tool.

## Findings

Blocking: none.

Important: `selectedMachines` consumed confctl's carrier-expanded inventory
without excluding carried copies. Selecting node19 produced four identical
`machine-mail-node19.prg.vpsfree.cz` receiver names: the ordinary node plus
copies on brq/apu, build and prg/apu. Alertmanager requires unique receiver names.
The synthetic `mapAttrsToList` fixture hid this behavior. Aitherdev has no
carried copies and its initial policy was unaffected.

Requested narrow fix: filter `carrier == null`, then exercise actual pinned
confctl carrier expansion and require unique mail receivers plus host,
management and node-subject routes. Reviewer explicitly classified this as a
narrow correction inside the reviewed design: direct focused verification and
folding into the owning commit are sufficient; no automatic review rerun.

Advisory: no additional findings.

## Independent evidence and limits

- The reviewer independently evaluated real cluster metadata with an in-memory
  node19 selection and proved four expanded copies/duplicate receiver names.
- Base, supporting-refactor and final default configurations were identical
  with no selected machines. Both offline route scripts and inert `amtool`
  config checks passed in the reviewer environment, as did recipient assertions,
  shell syntax and whitespace checks.
- Full flake derivation reevaluation was blocked by the read-only sandbox's
  Nix daemon restriction. After successful route reruns the amtool store path
  disappeared, so the duplicate case was established through receiver counts
  and upstream validation, not a claimed local rejection.
- Actual delivery, runtime daytime activation, repeats, inhibition and loaded
  replicas remain unverified. Both Alertmanager replicas need the new routes;
  old replicas can continue team delivery. Rollback reads existing state.

## History, migration and stream conclusions

The two commits form a coherent supporting refactor and feature/tests/docs.
No obsolete approaches, fixup iterations or unnecessary compatibility layers
remain in the reviewed series; commit split and messages are appropriate.

No migrations, schemas or persisted-format changes; no transitional migrations.
Neither feature commit was merged, released, deployed or externally consumed.

No dependency, channel/input, lockfile or generated-artifact update streams
changed, and no repeated streams or superseded pins require consolidation.

## Lead reconciliation

The Important finding is accepted. The implementation now filters ordinary
records, and the recipient fixture uses the actual pinned confctl library over
real metadata, including existing boot-server carriers. It asserts that carried
copies exist while each selected-node receiver/identity route appears once.
Both focused checks and active hooks passed after the correction. The fix was
folded into feature head `b17dbea2cb1b9bf93714c929da776a4d4a6618f8`, retaining
the unchanged supporting commit. The lead inspected the full series and
correction diff and refreshed the final inventory. The Important finding is
resolved; no rerun is required under the reviewer's narrow-fix conclusion.
