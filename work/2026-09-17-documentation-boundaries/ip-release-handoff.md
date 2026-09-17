# Handoff: reorganize IP release documentation

For the owner of session `2026-09-09-ip-release-mechanism`.

The user requested this handoff and explicitly excluded your session from the
documentation-policy implementation. That implementation has not edited your
tracking files, project branches, worktrees or development cluster. This handoff
does not grant additional deployment, integration, reset or cleanup permission.

## Goal

Apply the shared `dev-session-documentation` placement rule to the existing IP
release documentation. Preserve technical meaning and all compatibility and
recovery requirements. This is a documentation reorganization, not a change to
IP release behavior or a reason to rerun deployment operations.

Read the updated installed skill and the runtime's
[documentation guide](https://github.com/aither64/dev-workspace/blob/master/docs/dev-sessions.md#documentation-during-development).
An existing conversation may still hold older skill text in its context.

## Source and destination map

The assessment used vpsAdmin commit
`35e400de26d3cca2be079c1d426d8658d6a1fa13`. Re-read your current files before editing;
the line references below describe that revision, not a constraint on later work.

| Source material | Destination |
| --- | --- |
| `docs/ip-release.md`: campaign actions, membership, atomicity, failure outcomes, retry rules, member privacy and WebUI behavior | Keep in the campaign feature guide. Transaction rollback is application behavior. |
| `docs/ip-release.md`, lines 260–277: required charge provenance, protection of accounting evidence during account teardown, populated-network invariants | Put the lasting rules with general IP ownership/accounting documentation, linking from the campaign guide. Separate them from the legacy-data reconciliation steps in the same passage. |
| `docs/ip-release.md`, lines 282–289: asynchronous disownership, transaction-state metadata and WebUI disown/remove completion | Keep with general ownership/API behavior and cross-link from campaigns; avoid duplicating the explanation already in `docs/ip-locking.md`. |
| `docs/ip-release.md`, lines 218–271 and 291–294: schema/writer ordering, older transaction draining, legacy accounting audit and software rollback restrictions | Extract upgrade guidance for the actual supported predecessor/target schema or versions. Put repeatable diagnosis/reconciliation procedures in operations docs when they have continuing use. |
| `docs/ip-release.md`, lines 209–216: unmerged status, earlier branch schemas and resetting disposable databases | Move to session development/review records. These statements should not become permanent feature instructions. Retain any independently applicable API/UI compatibility requirement in upgrade guidance. |
| `docs/ip-release.md`, lines 279–281 and 291–293: concrete vpsFree.cz overlay rollout and removal | Put site steps in the session rollout record or owning configuration documentation. Keep the generic registry/template compatibility requirement discoverable with notification or upgrade guidance. |
| `docs/ip-locking.md`, lines 43–46: writer participation and rollout imperative | Keep the reservation-protocol invariant in the subsystem guide; link its transition requirements to upgrade guidance. |

The existing `ip-locking.md` is the natural starting point for general ownership
and accounting rules. Retitle or split it only if the resulting scope makes that
useful; no new directory or fixed file bundle is required. Name any upgrade guide
for the actual transition and state its applicability. Do not invent a release
number, or move a supported upgrade's only instructions into a private session.

The ownership/accounting prerequisite also affects ordinary IP and network
operations. Make those requirements discoverable without requiring readers to
start from the campaign feature page.

## Preserve the operational requirements

When splitting mixed passages, retain the requirements to coordinate all
participating API/supervisor writers, finish older in-flight work, freeze
network-semantic changes and registration where required, and preserve the
appropriate restrictions during software rollback. Preserve schema/API/WebUI
and notification-registry ordering and API discovery requirements.

Retain the prohibition on guessing charge provenance from current network
locations, the need to reconcile accounting history, and the fact that non-null
charge provenance does not establish a historically correct resource type.
Keep the SQL audit where its diagnostic or upgrade context is explained.

Preserve pending-chain recovery requirements, ownership/quota behavior on
transaction failure, additive history retention and the inability of software
rollback to recover already redistributed addresses. Reconcile wording with
current code and supported deployment assumptions before moving it.

## Index, review and handoff

Rename the documentation index entry from "IP release campaigns and rollout" to
"IP release campaigns". Link operations/upgrade guidance from the appropriate
index or subsystem page and update moved anchors and repository references.

Check that a reader can understand the feature without knowing the branch's
review-cluster or deployment status. Independently check that an operator can
find every prerequisite and recovery restriction for a supported upgrade.
Review the source/destination map for omissions and contradictory duplicates.

Use the existing English writing, commit and mandatory-review workflow. Validate
Markdown links and the changed documentation against the implementation; do not
add tests that match prose or reset/deploy a cluster merely to validate this
reorganization. Record the new document paths and any remaining applicability
uncertainty in your own session state. Follow your session's existing deployment,
integration and lifecycle authorization.
