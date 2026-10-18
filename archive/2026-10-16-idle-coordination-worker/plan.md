# Idle coordination workers

Implement durable background continuation for approved coordinated merges and deployments so waiting sessions can end their turns. Background runs wake the retained lead only when action or review is needed. Reservation grants and intermediate progress stay visible in Operations.

## Projects and design

- dev-workspace: background CLI, journal/schema capability, systemd dispatch, restart and generation handover, pause/intervention semantics, native notifications, status and operations documentation.
- workspace: waiting policy, matching nested runtime input, deployment verification.
- vpsfree-cz-configuration: matching dev-workspace/devWorkspace channel pin, aitherdev system build and deployment preparation.
- codex-web: reuse existing native notification transport; no planned changes.

Preserve existing synchronous and --no-wait behavior, approval scope, FIFO scheduling, machine ownership through review, exact integration proofs, and existing uncertain-effect recovery. Background preparation runs outside claims. Continue only existing certified mechanical refreshes; conflicts, stale machine artifacts, changed scope and uncertain effects require intervention.

## Compatibility and rollout

Use versioned background journals while supporting schema-1 manual journals. Unsupported package generations must refuse retained background state. Preserve schema-1 operation ledger, snapshots and worker protocols where possible. The selected compatible generation resumes the exact run; predecessor workers must stop admitting steps after a profile switch. No database migration is planned.

Build aitherdev from cz.vpsfree/machines/aitherdev in the configuration feature branch, through its existing dev-workspace channel and devWorkspace role. Match the workspace nested runtime input, check composed locks, prepare the exact final configuration commit, activate system before workspace user profile under one vpsfree:aitherdev reservation. Never infer default-branch integration approval.

## Verification

Quick Ruby, Go, Nix and JavaScript checks as applicable, then committed whole-branch independent review, then long packaged and native acceptance tests. Cover idle sessions, FIFO contention, per-run notification suppression, pause/resume, retry identity, crashes around submission/delivery/finalization, lifecycle fencing, generation changes and unsupported downgrade.

## Session setup history

The initial managed conversation 2026-10-16-idle-coordination was created but its initial request was refused twice with materialized Codex thread has no initial user request. Its creation journal and retained thread remain untouched. This separate initiative now has its own ready managed owner and notification thread. Startup is resolved without adopting the original initiative.

## Compatible first upgrade with retained manual runs

The completed older initiative left a schema-1 manual run pending. Treating that journal as completed, removing it, or mutating its owner is outside this initiative. Correct our new package capability advertisement instead. No foreign session state or machine ownership changes.

Keep package.json integration exactly {journalSchema: 1, certificationSchema: 1}, the existing manual ABI understood by strict predecessor package readers. Install a separate share/dev-workspace/integration-contract.json with schema 1, journalSchemas [1,2], certificationSchema 1. The new Ruby Store validates the optional schema-1 contract and requires its unique positive-integer journal read set to include the legacy schema 1 and every retained schema. Additional declared reader versions are compatible when the required retained version is included. A predecessor package lacking the file supports only schema 1. Missing or malformed support for a retained schema-2 journal refuses selection, including completed schema-2 journals. The sidecar does not change ledger, journal, snapshot, adapter, or native formats and does not advertise a package.json shape rejected by older Go loaders. Remove the unnecessary unmerged Go allowance for package.json journalSchema 2; no deployed package used that metadata.

This permits ordinary old-to-new profile activation with pending manual runs: the predecessor accepts its unchanged legacy descriptor, and the new executor can resume both journal schemas. Pending old runs remain pending for their owner and are never automatically retried by background continuation. System then profile ordering, reservation/approval guards and forward-only recovery remain unchanged. No bridge generation or foreign repair is required. The former drain instruction is replaced in owning runtime docs.

Verify the exact old Store against a candidate carrying the new sidecar with a real pending manual journal fixture; verify new Store accepts a dual-reader target, refuses legacy-only/malformed contracts for active and completed schema-2 journals, and still accepts legacy targets for schema-1 state. Keep strict Go legacy metadata validation and packaged contract checks. Rebase onto archive runtime 59833652 preserving tracking sync and its package recovery metadata. Resolve only the archive recovery fixture dependency list by including both helpers. Run focused quick checks, commit the completed deliverable and independently review affected compatibility/composition lanes before longer package, systemd, native and consumer builds. Repin published exact final runtime in both consumers through their normal Nix/confctl routes and consolidate each unconsumed pin stream. Existing user authorization continues to cover the same three repository/master targets after live deployment and verification; no new repository or machine action is introduced.
