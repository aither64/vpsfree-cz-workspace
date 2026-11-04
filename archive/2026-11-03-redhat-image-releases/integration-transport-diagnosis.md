# Integration transport diagnosis

Read-only investigation by implementer0, 2026-11-04. Session binding and saved
workspace_write identity matched. No push, claim, config/key/rule mutation,
source/history edit, build/test/CI action or lifecycle action was performed.

## Current observations

Final observation at **09:51:10 UTC**:

- GitHub API staging ref remains `742eb30cb1a8b6766c85e915d26b0400e38244b1`.
- Feature and clean detached merge target both remain
  `54b4313404cea35b58ebb9df951ae75e27c44971`. The local fast-forward is retained.
- Canonical origin is `git@github.com:vpsfreecz/vpsadminos.git`.
- API authenticates `aither64`; repository reports admin/maintain/push permission
  and default branch `staging`.
- Effective staging rules: `[]`. Repository/parent rulesets: `[]`.
  Staging is `protected=false`, protection enforcement off, no required checks
  in its branch-protection metadata. No configured branch-rule refusal is shown.

The lead's original normal push failed with
`remote: fatal error in commit_refs_rules` / `[remote rejected] HEAD -> staging`.
That error does not identify a violated rule. Read-only metadata cannot explain
GitHub's internal rejection, and no general GitHub outage is inferred.

Subsequent ordinary SSH probes consistently failed:

```text
ssh -T ... git@github.com: exit 255
Git origin ls-remote: exit 128
git@github.com: Permission denied (publickey).
```

The final normal-origin SSH probe at **09:49:16 UTC** still failed. A diagnostic
SSH probe to `ssh.github.com:443` at 09:49:15 UTC also returned publickey denial.
It used existing github.com host-key trust with StrictHostKeyChecking=yes;
no host-key acceptance or port/config change was made.

## Key and environment evidence

The shell has no SSH_AUTH_SOCK or agent connection, no GIT_SSH/GIT_SSH_COMMAND
or core.sshCommand override, and no ~/.ssh/config. Effective SSH selects the
normal GitHub endpoint and default Ed25519 identity. Its private file is owned
by UID 1000 with mode 0600. The existing key is usable noninteractively and its
derived public fingerprint matches the .pub file:

`SHA256:38gX47C2LkQgccktDtHa27hPk8wXo3kXLMGUQSnswK0`.

The public `users/aither64/keys` API lists the same fingerprint, key ID 96602366.
The private account-keys API needed an additional scope; no auth refresh was
attempted, and the public metadata was sufficient for fingerprint comparison.
No token or private-key content was printed or saved.

Verbose SSH proves it offers that matching key; GitHub responds with another
`Authentications that can continue: publickey`, without `Server accepts key`.
The server rejects the offer before signing. Thus a missing unlocked agent or
stale public/private file pair does not explain the observed denial. No local
key repair, upload, rule change or global SSH change is supported by evidence.
The precise server/account-side reason and whether it is transient remain
unestablished; both SSH endpoints currently reject the registered key.

## Smallest safe retry preparation

The same reviewed head and ordinary non-force push remain appropriate after
SSH read access recovers. No new source verification or approval gate is added.
Before a fresh claim, in the lead's ready environment, require this bounded
normal-origin read to exit 0 and inspect its returned target:

```sh
timeout 20s git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-redhat-image-releases/vpsadminos-merge-target \
  -c 'core.sshCommand=ssh -o BatchMode=yes -o ConnectTimeout=10 -o ConnectionAttempts=1' \
  ls-remote origin refs/heads/staging
```

A successful `ssh -T` prints `Hi aither64!` but normally exits 1, so use the Git
read's status as the readiness check. Current evidence does **not** pass it.
If access recovers and target is still 742eb30, the lead can take a fresh short
claim, repeat fresh target/source checks, and execute the original normal
`git push origin HEAD:refs/heads/staging`. If the target has moved, reconcile
outside ownership first. Preserve the known local target rather than resetting
or re-merging it. Use fresh SSH remote proof plus API reconciliation for any
uncertain rejection, then release under the normal claim procedure.

If registered-key rejection persists, retain this evidence for provider/account
investigation; do not rotate/upload credentials, disable rules, change runtime,
or switch to an HTTP push based on this diagnosis. No operational repair was
needed or applied locally, and no process from this package remains running.
