# Revision provenance

The accepted global rule/JVB-label policy supersedes the earlier published
SMS-only policy. Old head: `f725dd3f407b0e5b82c9f9c1ad7720bbc7b14b68`.
Base: `b66c929bb7c202ad31bd8994a691ade14c40ebf0`.

Read-only origin fetch during this work item confirmed master remains the base
and the remote feature still points to the old head. The old head is not an
ancestor of origin/master. Only local and origin feature refs contain it.
GitHub PR lookup for this branch in all states returned no pull requests;
scoped Actions lookup returned no runs. No session merge, release, deployment,
consumer-pin update or live notification occurred. This establishes known
session/repository provenance, not a live fleet audit or proof against unknown
external consumers. There are no migrations or persisted-format versions.

Workspace Git rules permit rewriting an unmerged feature during development.
Replace the owning metadata/alert-policy commit and replay the accepted CPU
change, retaining two clean commits and old objects/evidence. Inspect complete
history and final diff independently. After verification/review/builds, refresh
origin and push only the feature with an exact lease on the old head. If the
remote expectation or merge status changes, stop and reconcile before writing.
User subsequently authorized verified integration into vpsfree-cz-configuration/master
and retained deployment personally. No deployment is authorized.

Lead inspected the separate local master b6e650ad: it is an ancestor of freshly
fetched origin/master b66c929b, dated 2026-09-15. It is simply a stale local
ref, not divergent unpublished feature history. It remains untouched; target
integration uses a new detached checkout of origin/master. No rebase is needed
while the remote target remains b66c929b.
