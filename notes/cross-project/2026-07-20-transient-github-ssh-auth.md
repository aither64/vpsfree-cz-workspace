# Transient GitHub SSH authentication failure

Related initiative: `work/2026-07-20-kernel-boot-evidence-history/`.

A lease-protected feature-branch push from a configuration Nix shell failed
with `Permission denied (publickey)` before updating the remote. The worktree
used the required SSH remote and no authentication agent was configured;
ambient `git ls-remote` still succeeded through the normal user key.

Running `git ls-remote` inside the same Nix shell immediately succeeded as
well. Retrying the identical `--force-with-lease` push then passed, with the
expected old remote head proving that the failed attempt changed no ref. When
this symptom occurs, verify the remote and exact lease inside the deployment
shell before retrying; do not weaken the lease or change the remote to HTTPS.
