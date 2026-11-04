# Prepared WebUI fast-forward critical section

Preparation is complete; execution remains with the parent after required final
CI and W's exact-final Nix inspection are accepted. No claim has been submitted.

- Canonical repository: `git@github.com:vpsfreecz/vpsadmin-webui.git`.
- Registered resource: `vpsadmin-webui`, target `main`.
- Verified main: `1c8478bceb3943645ec06ccde895ee4b0985873f`.
- Published feature: `670cf286daf9bddb65594035507ca112a9e6d397`.
- Clean detached target: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui-integration-670cf286-627241b4`.
- Fresh request: `webui-040-670-integration-claim-request-unsubmitted.json`, ID `4467e296-5399-45e5-b073-52d5e5baeed5`, one repository and no machines.
- Native registered comparison captured exact `1c8478bc..670cf286`, exit 0.

The configured author and committer in the feature and target are Jakub Skokan
`<jakub.skokan@havefun.cz>`. Pinned Git is 2.54.0; SSH is OpenSSH 10.5p1.
`core.hooksPath` is unset, the common hook directory has no active non-sample
hooks, and neither checkout declares a hook framework. No trust override,
hook bypass, dependencies, build or tests were needed for target preparation.
Recheck those facts if any relevant input changes.

After the parent accepts all conditions and releases execution:

```sh
dev-session coordination acquire 2026-11-01-typescript-client-migration --as-is --request /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-040-670-integration-claim-request-unsubmitted.json --json
dev-session coordination claim-status 2026-11-01-typescript-client-migration --as-is --id 4467e296-5399-45e5-b073-52d5e5baeed5 --json
```

Act only on authoritative `held` status for this exact request. A queued request
owns nothing. Before merging, verify the bound session, exact feature head/tree,
clean target and empty target index, detached target HEAD at the verified main,
and fresh authoritative SSH main/feature refs. Verify the final PR126 identity
and accepted review/check receipts. Do not depend on stale tracking refs.

Keep the held section to those fresh checks, normal merge/hooks, non-force SSH
push and remote proof, then release:

```sh
/nix/store/b1wn5clix1mz4vpfih7x9cnj9qfh7c6h-git-2.54.0/bin/git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui-integration-670cf286-627241b4 merge --ff-only 670cf286daf9bddb65594035507ca112a9e6d397
GIT_SSH_COMMAND=/nix/store/43zp0r021jgfnxpp2zmvm59ivfl85w3k-openssh-10.5p1/bin/ssh /nix/store/b1wn5clix1mz4vpfih7x9cnj9qfh7c6h-git-2.54.0/bin/git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui-integration-670cf286-627241b4 push --no-follow-tags origin HEAD:refs/heads/main
GIT_SSH_COMMAND=/nix/store/43zp0r021jgfnxpp2zmvm59ivfl85w3k-openssh-10.5p1/bin/ssh /nix/store/b1wn5clix1mz4vpfih7x9cnj9qfh7c6h-git-2.54.0/bin/git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui-integration-670cf286-627241b4 ls-remote --heads origin refs/heads/main refs/heads/dev/typescript-client-migration
dev-session coordination release 2026-11-01-typescript-client-migration --as-is --id 4467e296-5399-45e5-b073-52d5e5baeed5 --json
dev-session coordination claim-status 2026-11-01-typescript-client-migration --as-is --id 4467e296-5399-45e5-b073-52d5e5baeed5 --json
```

Inspect normal hook outcomes before pushing, including post-merge hooks even if
Git exits zero. Verify target HEAD/tree/clean index and remote main at exact670
after the push. Never use force or create a merge commit. Reconcile an uncertain
push through authoritative refs before release. A moved main, changed feature,
dirty target, failed hook or non-fast-forward result stops this attempt; inspect
effects, release when safe, and repair outside the claim. Do not wait for
operator input or CI while holding a known-safe repository claim.

Release and verify the resulting state before records, CI monitoring or cleanup.
This request does not cover configuration master, machines or production. Keep
the old4ed and revieweddb90 recovery refs and all original receipts. No preview,
cluster, machine release, target removal or session lifecycle action is included.
