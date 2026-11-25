# REACT-R1 narrow remediation and final local source

The lead accepted retained reviewer0's Important finding at frozen5ffdb67d:
a synchronous PUT could succeed, but a mismatched/absent summary or a subsequent
403 read was classified as ordinary failure and removed the durable generation.
The draft remained dirty and replay became possible. The original completed
independent report has only R1; the lead owns direct step9 closure, with no
confirmation-only reviewer round requested.

## Final committed boundary

Base `88ac13b89d6421c914cd57e18153de1fee6fc7b7`; final head `bbd820a65536564756484f6dd037f10224901b35`;
tree `90de7b671745233b8da012aa9d2b13d2e1b25332`. Worktree/index clean. Final complete series:

- `c255afdbe8f8563b08b2234f4873ec307d478bcb deps: select the generated incident escalation SDK candidate`
- `de21ab1a5e2f00f7d18b30b3dce5521ceb431266 vps: show selected incident escalation status and settings`
- `bbd820a65536564756484f6dd037f10224901b35 docs: record shared incident UI checks and synthetic captures`

Only VpsIncidentSettingsForm.tsx and its new locks integration test differ from
frozen5ff. The fix is folded into owning application de21ab1a; dependency c255afdb
is unchanged. Evidence successor bbd820a6 has the same runtime/dependency files
as de21ab1a. No obsolete fixup or repeated dependency stream remains; no migrations.
Original5ff is retained at dev/incident-escalation-before-react-r1-5ffdb67d; the
pre-fold02223f91 ref/tree, raw ranges and original review packet remain intact.
Consolidation preserves the tested pre-fold tree exactly.

The existing MissingActionStateError wraps every verification failure after an
accepted synchronous write. Its message remains the existing translated
incidentEscalation.verifyError. A successful read must match requested VPS id,
selected type and all existing raw settings checks. The guard settles ambiguous
failures into the SAME persisted uncertainty generation, so existing replay gates
and drafts remain. Before-write rejection, async receipts, shared lock policy,
API, choices, localization and all unrelated source are unchanged.

## Focused evidence

The new test uses the actual generated SDK/XHR fixture and real
useLocalMutationLocks acquisition/settlement/persistence. Only VPS preflight and
context plumbing are mocked. Cases cover mismatch, absent selected summary,
authoritative HTTP403 read, matching values for another VPS, and exact success.
Pending generation is captured during readback; failure preserves that exact id
and durable marker. Confirm stays disabled, ordinary release cannot remove it,
a second durable acquire refuses replay and no extra HTTP request occurs.
Success releases the guard and refreshes only after exact verification.

- First fixture run failed at unexpected OPTIONS discovery because the test
  omitted explicit HaveAPI config. Its receipt remains r1-negative-before.log.
  Corrected configuration follows existing SDK fixtures, without weakening
  assertions or changing runtime.
- Correct negative-before at original runtime: r1-negative-lock-before.log,
  exit1, first mismatch guard is undefined; bail1 means other cases were not run.
- Fixed-after: r1-positive-lock.log, exit0, five cases passed/10.36s.
- Initial remaining batch stopped at typecheck TS7053/57.5s in the new mock key
  annotation. No chained tests/audits ran; r1-affected-checks.log remains failed.
- The annotation-only correction emits byte-identical JavaScript under installed
  TypeScript, bound in r1-test-type-equivalence.json; no five-case repeat.
- Fresh resumed batch r1-resume-checks.log:exit0/85s. Application types,
  VpsIncident.test.tsx + vpsIncidentEscalation.test.ts (34 cases), lint:patterns,
  UI strings, structural/component contracts, mutation audit and cheap Nix
  source-contents all pass. No new structural exception,226mutations/no warnings.

Current Nix source-contents derivation, built successfully in that resumed batch:
`/nix/store/chg6pj3s551b4anmf7wb9x4wkj6gicn6-vpsadmin-webui-source-contents.drv`.
Final CLEAN committed source evaluates the SAME derivation. Frozen5ff's earlier
gi2gz derivation is retained only for frozen5ff and is not current-source proof.
This is not a frontend/BFF build, browser or real backend certification.

Exact final runtime/test hashes are in r1-final-history-inputs.json. Runtime hash
matches the five-case passing source; test hash matches its type-erasure receipt.
The resumed batch used these final source bytes. See r1-tested-input.json,
r1-resume-tested-input.json, r1-reviewed-to-final.range-diff, r1-fold.range-diff,
r1-final.diff and r1-final-feature.diff. All old media bytes remain identical.

Normal Nix Git author/committer identity verified; no hook bypass. No operation-
owned process/watcher/tool session remains. No full suite/build/browser/BFF/guest/
image/server/CI dispatch, publication, merge, deployment or lifecycle action.
Publication remains held for lead's inspected closure/source release. After that,
perform fresh SSH main/actual feature lease, authorized feature push and PR115
update, then observe automatic exact-final CI without duplicate local suites.
The temporary SDK candidate still requires a published registry artifact before
future WebUI merge. Existing old screenshots remain historical synthetic evidence.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
