# Follow-up composed build

Expected effort: about 3..7 minutes. Risk: validate the composed portal and
Settings changes with the actual site catalog and packaged checks. Stop after
one successful related batch. Earlier unchanged Ruby derivations may be reused
by Nix; do not start duplicate tests or host VM checks.

After final review, a fresh Luna/low verification utility runs only:

```
nix build --print-build-logs --out-link /home/aither/workspace/ai/vpsfree.cz/work/2026-10-26-progress-oversight/followup-verified .#default .#checks.x86_64-linux.agent-team-policy .#checks.x86_64-linux.agent-instructions .#checks.x86_64-linux.deployment-contract
```

Working directory: initiative workspace worktree. Tested runtime120c7b9c,
workspace9aa2a2a4, final consolidated configuration pin. Preserve exact exit status and complete
log at followup-package.log. Escalate unexpected kernel builds and stop only
that owned build if one starts. No retries, diagnosis, edits, deployment or
nested agents. No generic timeout or cancellation for silence.

A final direct ownership correction in runtime120c7b9c narrows clearing to the
first proven-unsent dispatch; later uncertainty retains its ID. This requires a
new composed package. Preserve reusable completed Nix outputs, cancel the owned
superseded build if still running, and launch the replacement under a fresh
watcher. No unrelated tests or host rebuilds are added.
