# I1: fresh directory ownership and complete mode

Frozen, unstaged on reviewed base `bf74af0b76accdf844ad6ffbea75db6c409f386e`,
tree `822fe1de775fb57c592d8cef884ff016695a6ac2`. Verified current session and
retained roster18: implementer0, gpt-6.1-sol, xhigh, workspace_write, ready;
both identity environment variables absent. Read current workspace and product
guidance, unchanged accepted design (SHA256
c80fea979d8fe48c48d98b78a81b21dd8ea596e31d0c45e8eda296abdb1382b9), and the
Astra final I1 finding. This implements the lead's bounded accepted root:root
0755 decision; no new metadata policy or design deviation.

## Source and tests

Only six assigned paths changed. Each of four self-contained raw helpers adds
the same comment and two explicitly checked commands after successful mkdir:
`chown 0:0 -- "$path" || return 1`, then
`chmod 00755 -- "$path" || return 1`. Existing directories/symlinks return
before those commands; recursion, ordinary callbacks and all mount/allocation
logic stay byte-identical. Every newly created level is normalized, never
recursively and never by repairing pre-existing contents. New metadata-command
failure propagates through the existing explicit activation exit.

GNU coreutils manual27.5 documents that directory SGID can be inherited by
mkdir0755 and retained by chmod0755, while the five-digit00755 explicitly
clears it. Exact installed documentation excerpt is retained in
coreutils-directory-mode-semantics.txt. Pinned activation-script.nix supplies
coreutils on activation PATH (26.05 excerpt lines84-94); no dependency change.

The focused shell test adds a checked numeric0:0 command double because a
normal nonroot build sandbox cannot establish real root ownership. Successful
helper mkdir calls record only freshly created paths; chown/complete-mode
requests must refer to that list. Actual chmod still runs. Positive cases
compare the created/chown/chmod call lists, retaining existing metadata and
all previous mount/payload assertions. The SGID-parent case records inherited
2755 before normalization, expects final755, and preserves the existing
parent's full owner/group/mode/inode, following its directory alias where
needed. Injected chown/chmod failure cases require nonzero activation and no
allocator marker. These cases are prepared, not executed here.

The existing `fresh-ancestor-26.05` script provisions only the controlled
absent source's parent before first boot as0:1234:2775. The child remains absent
until the candidate creates it; the unchanged actual child assertion requires
0:0:755. A fresh-ancestor-only snapshot field compares the parent's complete
metadata/inode with its preboot value across all live switches and restart.
Group1234 is fixture directory metadata, not an account ID. Exact fresh and all
adoption/failure variants retain their definitions, accounts, maps, data,
software/stateVersion, store-copy/profile setup and readiness requirements.
No fixture definition, source path or extra test variant changed. Choosing the
ancestor control keeps unrelated payload-source parents outside the SGID setup.

## Exact inventory and static evidence

original/ and original-sha256.json preserve all six source bytes/hashes before
editing. frozen-sha256.json records current hashes. source-comparison.txt
proves removing the three helper lines restores all raw files byte-for-byte,
and removing only the fresh-ancestor condition/three suite blocks restores the
original suite. All four adapter blocks are equal; latest stable equals26.05.
Only six assigned paths are dirty, index is empty and the lead guide is
byte-identical to HEAD. source.patch SHA256:
`c7d2de0fcb7ad9c64be9e005ace46f108789d6aa08f1dc2897b9f81909b9a36f`. inverse.patch SHA256: `b877b8387553e22eba4f8cab6dc3d7707932d4b8c78120c946f171e4e51134e2`.
The inverse patch passes read-only applicability and whitespace checks.

Passed approved static checks, recorded in static-checks.log/.json:
prepared nixfmt; five Nix parsers; Bash syntax of shell and static helper;
prepared Ruby3.4.9 syntax of combined static suite; whitespace; inverse patch
check; empty index; stable/latest equality. The Ruby template includes all
conditional bodies with inert Nix values; it is not an evaluated script.
No command double case, real chown/chmod/mount, Nix evaluation/build, VM/runtime,
hook run, staging, commit, ref or lifecycle action was executed.

## Focused parent commands

The retained thirty actual release/layout snippets were copied into
focused-inputs/ with only the exact literal helper substituted. The early
mount files are byte-copied. focused-inputs-receipt.json records source/current
hashes and inverse byte equality for each substitution;60 Bash syntax checks
passed. This is exact composition using prior evaluated tuples, not fresh Nix
evaluation or runtime evidence. No previous artifacts were changed.

Parent-owned execution through the declared rooted environment/watcher:

```sh
nix develop --profile result/config-imports-dev-shell --command bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/persistence-effective-mounts-i1/focused-shell-checks.sh
nix develop --profile result/config-imports-dev-shell --command overcommit --run
```

For actual final generated Ruby, the existing exports.nix script export remains
applicable (parent evaluation only); syntax-check the resulting twelve scripts,
especially fresh-ancestor-26.05. The source conditional emits SGID setup and
its snapshot assertion only for that one existing script. No member evaluation
or runtime was launched. Parent owns final-head normal check/template policy,
review/folding and fresh-ancestor runtime acceptance; current static evidence
makes no actual ownership or guest acceptance claim.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-12-streamline-vpsadminos-config-imports/
