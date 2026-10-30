# Provisional documentation contract

Status: superseded by source-checked working-tree documentation in
docs/containers/datasets.md and docs/os/{updates,testing}.md. Source/quick-check
binding is recorded in documentation-checks.json. The draft below preserves the
earlier owner contract; it does not claim a fixed-head VM or recovery pass.

Owner0 supplied this contract while reader/import/GC source and unit tests were
still in progress. It is a draft for the assigned project docs, not a verified
implementation or runtime acceptance statement. Final source call points and
unit results must be checked before applying it. No product documentation or
source scope is expanded by this draft.

## Dataset behavior: docs/containers/datasets.md

An impermanent NixOS container creates a new temporary root dataset on container
start or restart. Persistent backing data survives that replacement. Its live
root is the temporary dataset's `private` directory; the base dataset remains
available for persistent data. A daemon replacement or userspace activation
preserves the existing run identity, mounts and temporary data rather than
starting a new container run.

The runtime configuration records the complete dataset selection and cleanup
policy before container start. Saving that selection does not depend on CPU
topology or scheduler assignment. This preserves the existing YAML fields and
format; no migration or coordinated node update is required.

## Legacy import and refusal: docs/os/updates.md

Older daemons can leave a saved base-dataset selection and disabled temporary
cleanup even while an impermanent guest runs from a temporary root. During pool
import, the reader can repair that narrow case only when the saved run identity,
existing GC ownership and authenticated live root all agree. The repair retains
the run ID and unrelated saved fields, updates the selected temporary dataset
and cleanup policy, and leaves GC ownership bytes unchanged. Already-correct
impermanent and supported custom-boot selections are validated without rewriting
their metadata.

Missing, empty, malformed, foreign, conflicting, ambiguous or changed evidence
prevents recovery. The container is omitted from management rather than assigned
a guessed root. The running workload and live storage remain untouched; the
import reports the unmanaged container and inhibits temporary dataset retirement
for that pool instance. Collection resumes only after a successful fresh import
has authenticated its containers. No manual hold-release or ownership rebuilding
command is introduced.

The inhibition applies to periodic and manual pruning and queued explicit frees.
Registered GC ownership rows remain intact. Queue handling, new registration,
saving and normal shutdown remain functional. A refused free without an existing
registered row has no durable automatic retry guarantee, and datasets already
in the trash bin are outside this safeguard.

Repaired metadata uses the existing on-disk format and is readable by older
daemons. Rolling software back loses the new authenticated recovery and import
refusal safeguard. Normal daemon/userspace replacement does not require a
coordinated update of all nodes. Operator visibility wording and any supported
intervention steps still need final source confirmation; do not invent a
recovery command or advise deleting live storage to clear a refusal.

## Diagnostic purpose: docs/os/testing.md

The opt-in first-switch fixture captures raw runtime/GC configuration, process
birth and root/mount/ZFS identities, markers and sysctl observations around the
first userspace activation. It preserves original errors and native cleanup and
stops before the ordinary repeat/restart matrix after successful capture. It
does not replace the full upgrade continuity tests or certify their later phases.

The diagnostic-only target override remains exact846bb and requires explicit
diagnostic opt-in. Ordinary upgrade targets remain the tested checkout. Frozen
source/lock equality alone does not establish an identical binary graph or guest
image. The first captured run proved stale saved selection before activation;
its recorder failed on an empty-file read after pool import, so it established
no post-switch root/data/API or recovery assertion. These execution details
remain in session evidence, not lasting project behavior documentation.

## Remaining source checks

- Bind the final writer/reader install/authentication call points and retained
  process-identity lifetime to the accepted implementation.
- Confirm exact valid custom-boot selector and no-write behavior.
- Confirm GC common retirement sink covers periodic/manual prune and queued free,
  import inhibit lifetime and actual reporting wording.
- Check unit evidence and old-format/rollback semantics; keep integration results
  and unresolved post-capture facts in session records.
- Apply only settled behavior to the three assigned project pages. Fold docs and
  diagnostic helper fix into their logical owner under the later lead Git window.
