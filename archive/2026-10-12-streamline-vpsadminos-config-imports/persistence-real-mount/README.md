# Supplemental real-mount verification

Prepared session-only checks for the reviewed persistence helper. They use
real util-linux commands inside a new mapped-root user namespace and private
mount namespace. No NixOS account allocation takes place: the marker establishes
whether the unchanged activation failure guard allows control to proceed.

The caller supplies a snippet freshly evaluated from the final reviewed head.
The wrapper copies it into a session-owned `run.*` directory, records hashes,
and creates the namespace before executing any mounts. The inner script refuses
its parent's namespace IDs, requires UID 0 inside the new user namespace and
private propagation, and verifies that mount tools are executables rather than
shell command doubles. All created files and mount destinations are below that
owned run directory. Namespace exit releases its private mounts; evidence and
fixture directories are retained. There is no sudo, host mount change, network,
build, account repair or guest deletion.

`adapt.py` verifies that the input's literal function equals the frozen raw
module's function. It changes only the two generated call source/target
arguments. Reversing those replacements must reproduce every input byte,
including the parent-shell `if ! ...; then ... exit 1` failure form. Each case
records this proof and the input/helper hashes next to its adapted snippet.

Seven cases cover fresh non-root tmpfs backing, restrictive existing metadata
and payloads, repeat activation with one mountinfo entry per destination,
missing root-backed storage, an intentional `/` source, conflicting live binds,
and deterministic preparation failure on a read-only tmpfs. Successful cases
require real source/destination identity before accepting the control-flow
marker. Failure cases require nonzero exit and no marker. Root-source refusal
cases require the original backing-guard diagnostic. Existing mounts and
payloads must retain their identity and content.

The lead explicitly authorized only read-only root probes: `/`, and a unique
absent `/vpsadminos-persistence-<run token>` child, checked before and after.
Those are sources, never created directories or mount destinations. Guard-case
destinations are prebound to different disposable tmpfs directories; the
unchanged matching-source check provides a second refusal before any source
preparation or root binding if the backing guard unexpectedly passes. Such a
result fails and stops the run. This avoids treating the workspace's separate
mount as unavailable storage or inventing a pathname durability rule.

Parent-only execution after final-head evaluation, from the vpsadminos worktree:

```sh
nix develop --profile result/config-imports-dev-shell --command \
  bash -c 'nix eval --impure --raw --file tests/nixos-container-persistence-eval.nix --apply "checks: checks.shellFixture" > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/persistence-real-mount/final-head-snippet.sh'

bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/persistence-real-mount/run.sh \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/persistence-real-mount/final-head-snippet.sh
```

Record the evaluated Git head separately with the invocation. The wrapper prints
the evidence directory and preserves `run.log`, overall `status`, input hashes,
per-case logs/statuses/provenance, metadata/payload checks, and mountinfo. A
nonzero wrapper status is a failed or unavailable gate, not proof of runtime
preservation. These supplemental checks do not replace reviewed-head image
tests for UID/GID, machine-id and payload ownership across boot and restart.

Only Bash syntax and static adaptation checks were run by the implementer.
Real namespace/mount execution remains parent-owned and pending.
