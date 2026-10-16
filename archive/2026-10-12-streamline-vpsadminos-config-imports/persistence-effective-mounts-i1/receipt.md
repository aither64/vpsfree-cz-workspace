# I1: fresh directory ownership and complete mode


## Sandbox correction checkpoint

The parent's normal I1 evaluation passed0. Its original shell build passed
fresh/existing/matching and failure cases, including new chown/chmod failures,
then standard Nix filter-syscalls refused chmod2775 in the pure setgid_parent
setup. The parent's installed manual diagnosis records that setuid/setgid
creation is blocked. This establishes a test-environment restriction, not a
production helper failure. Original sandbox-diagnosis/log/status remain in
../effective-mounts-i1-quick/; attempt-1-sandbox/ preserves the complete previous
I1 source/evidence checkpoint and copies of those records.

Only the shell harness changed at this checkpoint: remove setgid_parent
selection/setup/inherited-mode recording/assertions. No original scenario,
numeric fresh-only chown/full-mode check, ordinary real chmod, created/chown/
chmod equality or failure-negative assertion was removed. No SGID double,
capability skip or sandbox setting was added. Four raw modules and the actual
VM SGID control are byte-identical to the prior frozen hashes. Guide and index
remain untouched. All prepared static checks pass again; no Nix evaluation,
harness, runtime, staging, commit or ref operation was launched by this member.

Current shell SHA256: `f9d38be0b3c40dcdc088bdcaab83843e145e4d2d1a0e50034e8344d814a14987`.
Incremental sandbox-correction.patch SHA256: `92671d5340ace706030e4593ac6114a19e014d9a398df8ff1ea23d9df31bec62`.
Current six-path source/inverse hashes appear below. Parent owns focused actual
thirty-call execution against its already evaluated unchanged raw snippets and
all remaining acceptance checks. Previously prepared focused-inputs/ bytes are
unchanged and remain a literal-helper composition fallback, not new evaluation.

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
all previous mount/payload assertions. Injected chown/chmod failure cases
require nonzero activation and no allocator marker. Pure tests check exact
numeric0:0/full-mode00755 requests and use actual ordinary chmod; they make
no SGID inheritance or actual root-ownership claim. Creating SGID metadata is
forbidden by the standard Nix syscall filter, so that proof belongs to the
unchanged registered VM fresh-ancestor control.

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
`1bc9e466ee99ac5eb646aab31c431797d4f6740bb87a9f37c2fbf1b112738e42`. inverse.patch SHA256: `96f92bfd6895be973fc75cc6c850827248e129ccb0bdaded8011906f02d0518e`.
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
