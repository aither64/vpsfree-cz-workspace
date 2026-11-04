# Prepared publication and integration boundaries

Preparation only. No command below has been executed. This packet does not
release publication, CI controls, a repository claim or integration.

Frozen candidate: `db90da33765090f34d74280aad273c4dbfc98090`, tree
`93203cc0d5ef40d0425230abb9cf985a69086ea7`, 36 commits on current server main
`1c8478bceb3943645ec06ccde895ee4b0985873f`.
Current published feature: `4ed519b69c422ea6b4fd0bd7bf490a20fcd6983e`.
Canonical origin: `git@github.com:vpsfreecz/vpsadmin-webui.git`.

## Publication after the lead releases execution

The independent all-lane review, any required remedies and the lead's publication
release must bind the actual final head. Parent finalizes the bilingual body
after its English pass. The draft files are not approved external copy. Preserve
the currently published body and all original review, preview and history
receipts. Confirm the existing recovery ref still names exact old4ed:

`refs/keep/2026-11-01-typescript-client-migration/released-040-pre-rebase-4ed519b6`

Reverify local head/tree/clean index, SSH server main and feature, and PR126's
head/source/base branch/title/body hash. The current PR API reports base63d,
while authoritative server main is1c8478; do not equate them. A newly advanced
main or feature needs reconciliation before overwriting anything. Fetch only
if an unknown new object is needed, without repairing stale tracking refs.

The authorized rebase needs an explicit lease against the verified old server
feature, rather than an ordinary fast-forward push:

```sh
/nix/store/b1wn5clix1mz4vpfih7x9cnj9qfh7c6h-git-2.54.0/bin/git push --no-follow-tags --force-with-lease=refs/heads/dev/typescript-client-migration:4ed519b69c422ea6b4fd0bd7bf490a20fcd6983e origin refs/heads/dev/typescript-client-migration:refs/heads/dev/typescript-client-migration
```

Use canonical SSH with the verified existing SSH executable. Keep hooks enabled.
No bare `--force`, tag write, default-branch write or other branch is included.
If the command fails or its outcome is uncertain, query the exact server ref
and reconcile its effects before retrying or reporting completion.

After verifying the server head, recheck that PR126's old body is unchanged and
update only this PR using the parent-approved final body file:

```sh
/nix/store/2snd6y1sp2w1xp9vybhn9dh6nhba37p1-gh-2.103.2/bin/gh pr edit 126 --repo vpsfreecz/vpsadmin-webui --title 'Use the generated TypeScript client for vpsAdmin API operations' --body-file PARENT_APPROVED_FINAL_BODY_FILE
```

Read the full body back and compare bytes and SHA256. Verify the PR title,
source branch/head, base branch and authoritative server refs. Preserve local
source/tree/index cleanliness and return the serialized Git turn promptly.

After publication, inspect actual same-branch workflow records under the later
execution grant. Cancel only queued or in-progress runs whose head SHA differs
from the newly published final head. Never cancel current-head runs, terminal
runs or another branch's runs. The preparation query found no runs for exact
old4ed, so it establishes no cancellation list or final-head CI result. Parent
owns fresh required CI registration and monitoring through its watcher.

## Fast-forward integration after all conditions pass

The recorded user authorization covers WebUI/main after the requested release,
semantic rebase and all required tests pass. It does not authorize configuration
master integration or production deployment. Final independent review, required
core and three native browser CI projects, exact-final Nix5/output acceptance,
and the final complete-series/input-stream/migration inspection remain conditions.
If remedies change the candidate, refresh the relevant evidence and this packet.

Outside repository ownership, prepare a new clean detached target worktree from
the freshly verified main SHA in this repository, its pinned tools and normal
hook trust. Do not reuse another session's checkout. Do not create it during this
preparation turn. The intended later Git operations are ordinary
`git worktree add --detach TARGET_PATH VERIFIED_MAIN_SHA`, then the merge and
push below from that target. Preserve the feature and recovery refs.

Capture the registered feature comparison after the final head is settled:

```sh
dev-session worktree capture-comparison 2026-11-01-typescript-client-migration vpsadmin-webui --as-is --base 1c8478bceb3943645ec06ccde895ee4b0985873f --head db90da33765090f34d74280aad273c4dbfc98090
```

Those exact arguments are valid only while the verified base/head remain the
same. Do not guess an older base or reuse a comparison after a head change.

Only when review, tests, target preparation and the integration release are
complete, acquire one repository claim for registered `vpsadmin-webui`, with no
machines or other repositories. The draft schema-1 request is prepared separately
and has not been submitted. Read authoritative claim status before acting.
A queued request owns nothing; wait without holding a repository or Git turn.

```sh
dev-session coordination acquire 2026-11-01-typescript-client-migration --as-is --request APPROVED_CLAIM_REQUEST_FILE --json
dev-session coordination claim-status 2026-11-01-typescript-client-migration --as-is --id REQUEST_ID --json
```

Keep the held critical section to fresh exact feature/remote main/clean target
checks, ordinary merge and hooks, non-force SSH push, and authoritative proof:

```sh
git -C TARGET_PATH merge --ff-only db90da33765090f34d74280aad273c4dbfc98090
git -C TARGET_PATH push --no-follow-tags origin HEAD:refs/heads/main
git -C TARGET_PATH ls-remote --heads origin refs/heads/main refs/heads/dev/typescript-client-migration
```

Use the verified pinned Git executable for these commands. A moved main,
non-fast-forward result or hook intervention stops this attempt. Inspect effects,
release a known-safe claim, then reconcile outside ownership. Git can exit zero
after a failing post-merge hook, so inspect hook results before pushing. An
uncertain push needs actual remote reconciliation before release.

After proving exact final HEAD on remote main and its expected feature lineage,
release the claim immediately and verify its released state, before CI, records
or target cleanup. Do not hold it while waiting for results or instructions.

```sh
dev-session coordination release 2026-11-01-typescript-client-migration --as-is --id REQUEST_ID --json
dev-session coordination claim-status 2026-11-01-typescript-client-migration --as-is --id REQUEST_ID --json
```

The running old4ed preview is not an ancestor of this semantic successor. Its
recovery ref and receipts remain intact; merging this successor does not certify
old4ed as literally merged or prove a new deployment. This package does not
change the preview, touch a cluster, release a machine or close the session.
