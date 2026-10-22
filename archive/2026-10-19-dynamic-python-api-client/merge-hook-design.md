# HaveAPI merge hook trust blocker

Status: bounded investigation complete; runtime remedy proposed, not authorized or
implemented. The user approved HaveAPI `master` integration only, with **no release**.
This record does not authorize another repository's edits, merge, package selection
or deployment. Architect changed this record only.

## Verified state and cause

Session identity and retained roster were checked against
`2026-10-19-dynamic-python-api-client` in
`/home/aither/workspace/ai/vpsfree.cz`.

- Integration run: `a9c23f6e-036d-4680-b06b-4b27701c0393`.
- Reviewed feature: `c1823f3d70365b0442d0e2171bdf83bd4c6dbe31`.
- Historical target: `c58704a08451a231fdf6c6123437133422af46dc`.
- Selected runtime:
  `/nix/store/1i1g6rp8ind51qqayzpww7cn1xp1k1gq-dev-workspace-0.2.0`.
- Owner's latest evidence supersedes the earlier timing report: normal historical
  signing had already started under the earlier grant before the freeze arrived.
  It completed; the shared configuration signature is now
  `689faa60978769404adfbfa8665fda4599f9813868d38b5fe170cb3d6273711a`.
  `verifySignatures=1`; the exact clean historical target's ordinary post-checkout
  passed. No coordinator retry followed. Trust is frozen.
- Earlier feature signing and ordinary post-checkout passed with signature
  `b60e0548237424002fc3f5930a5c0bf3743f5e7fa671f82d380ae0cf7729a4cb`.
  The latest historical signing replaced that shared configuration value.

Installed `libexec/workspace-coordination-execution.rb:203` always repeats the
retained feature's ordinary checkout when called with prepared hooks.
`prepare_merge`, at line 291, then allocates a fresh UUID historical target and
performs its ordinary checkout at line 313. Both linked worktrees share
`repos/haveapi.git/config`. The preparation cannot progress by alternately signing
one checkout and restarting the whole sequence.

Overcommit 0.73.0, as installed in the retained feature's `.gems`, stores and reads
one configuration signature through forced `git config --local`
(`lib/overcommit/configuration.rb:234,327`); hook signatures do the same
(`lib/overcommit/hook_signer.rb:70,105`). Implementer1 verified that this ignores
`config.worktree` and conditional includes by default. `GIT_CONFIG` plus the
forced local scope errors with exit 129. Signatures are content checksums, not a
multi-version trust store.

`lib/overcommit/configuration_loader.rb:55` loads the working tree's fixed
`.overcommit.yml` plus optional `.overcommit-local.yml`. The inspected CLI exposes
no alternate configuration path. A local overlay does not pin the complete
configuration and tracked plugin bytes across revisions, and creating overlays
would itself change the reviewed effective hooks. It is not an established
configuration-only recovery. No supported installed environment/configuration
surface was found that preserves both exact configurations and all their hooks.

Evidence: [owner recovery](merge-hook-recovery-owner.md),
[lead recovery](merge-hook-recovery.md), and implementer1's same-session diagnosis.
The selected package's `share/dev-workspace/coordination.md` and
`coordination-operations.md` were read. Their referenced `integration.md` is absent
from that package, as reported by the owner; do not invent a recovery command.

## Proposed smallest runtime scope

Prefer **resumable preparation with explicit trust steps**, retaining Overcommit's
normal signing and verification, over introducing a second signature engine.
This is a proposed implementation boundary, not a tested workaround.

1. Retain one preparation identity and target path for the exact owner,
   repository/common Git directory, feature, target baseline, evidence and hook
   environment. Record successful checkout-hook stages durably. On retry, recheck
   those identities and clean trees; do not repeat a completed stage merely
   because a later revision needs explicit trust.
2. Prepare the feature environment and run its ordinary checkout hook. If trust
   is missing, stop with the exact revision/path for normal operator signing.
   Preserve a successful feature stage before starting the historical target.
3. Materialize the stable target without an implicit hook, then perform the
   ordinary explicit checkout hook in the prepared environment. This follows the
   existing retained-source pattern; it must not omit the checkout hook. A failed
   hook remains pending and is retried after explicit historical signing.
4. After the historical hook passes, stop at an explicit final feature-trust
   checkpoint when necessary. The operator signs the exact retained feature using
   the normal CLI. Resume verifies feature trust and proceeds without repeating
   the historical checkout. Never calculate/install trust automatically.
5. Admit the existing merge only with final feature hooks trusted. Before any
   target/default-ref mutation, the worker must fail closed if that required
   trust has changed. The fast-forward's post-merge and pre-push hooks run normally
   in the prepared environment. Verify actual Git hook exit handling in the
   implementation; a successful Git exit alone must not hide failed required hooks.

The demonstrated defect belongs primarily to runtime
`libexec/workspace-coordination-execution.rb`: `retain_commit`, `prepare_merge`,
prepared-hook handling and the worker's merge preflight. Its preparation entry
point/retry caller will need to preserve the same preparation identity. Inspect
that caller only after authorization; its exact source location is not asserted
here. `libexec/workspace-coordination.rb` needs changes only if snapshot/artifact
validation requires an additional bound field. Add focused runtime regression
coverage and update the owning coordination/recovery guide. No HaveAPI client or
hook-source edit is part of this remedy.

Alternative, if authorized implementation shows the staged approach cannot remain
bounded: explicit content-addressed, multi-version trust support in Overcommit or
a reviewed runtime adapter. That is a separate, larger security contract; ordinary
`--worktree` storage alone still cannot handle a target transitioning from old to
new content. Do not implement both approaches or invent dynamic auto-signing.

## Invariants and acceptance

- Preserve every ordinary required hook and signature check; never set
  `OVERCOMMIT_NO_VERIFY`, disable signatures, suppress hooks, rewrite the shared
  trust value automatically, alter reviewed hook files, or use a direct Git
  integration/push around the coordinator.
- Checkpoints prove an exact completed stage, not generic approval or a substitute
  for trust at a later stage. Changed owner/incarnation, source, target baseline,
  dirty tree, hook environment or evidence invalidates affected preparation.
- No merge job/default-ref change before preparation completes. Existing approval,
  queue/claim, remote-baseline, fast-forward and uncertain-push recovery rules stay
  authoritative. Dependencies are prepared outside resource claims.
- A fixture repository with differing old/new Overcommit configurations must
  demonstrate feature hook → historical hook → feature trust → merge/push hooks,
  with signatures enabled throughout and explicit ordinary signing only.
  Prove retry after each trust failure reuses the exact target, successful stages
  are retained, failed stages are not marked successful, and no signatures are
  manufactured by the runtime.
- Negative checks: altered hook/config bytes, changed baseline, wrong owner,
  dirty retained source/target, malformed checkpoint, interrupted publication,
  stale trust before mutation, and failed hooks all refuse or retain recoverable
  state. An unchanged-hook repository still follows the ordinary successful path.
- Run the runtime's required quick checks and independent completed-change review
  before longer integration. No such tests were run for this design investigation.

## Compatibility, deployment and recovery boundary

Keep existing completed snapshots/jobs and their recovery behavior readable.
Prefer additive bounded preparation metadata outside the authoritative ledger;
if safe compatibility requires a version/capability gate, make that explicit
before implementation. A predecessor must not silently treat a partial new
preparation as complete. Retained source/target payloads must survive while that
preparation remains recoverable.

An authorized runtime fix requires its own worktree, repository guidance, review,
package preparation and separately authorized coordinated profile selection.
There is no runtime/default-branch integration authorization in the HaveAPI merge
instruction. Follow the selected package's forward recovery rules rather than
assuming package rollback is allowed. Before selection, leaving the original
package and blocked run untouched is the recovery baseline; after selection,
retain original journal/receipts and recover through supported commands. No ledger
editing, cleanup, signature mutation, retry, release or deployment is authorized
by this document. Lead decides the next grant with the user.
