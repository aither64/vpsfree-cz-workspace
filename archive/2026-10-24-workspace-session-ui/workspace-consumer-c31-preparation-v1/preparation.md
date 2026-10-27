# Frozen workspace c31 repin preparation

Prepared only. No source, index or ref mutation, Git fetch, Nix command, test,
build or publication was performed. The parent has accepted the reviewed c31
source binding; final mv5 vendor/content acceptance and a new parent execution
release remain prerequisites. This package does not supply either gate.

The owned workspace is clean at `ef3227b6b63985dc308bc4a04ac75fa211fb9ab7`, tree
`b86da3d2750c21fff47212aac3a3c8a3d4edb533`, one two-file intermediate pin commit
above canonical `3e72f394a73c33be71fcdc1313d05cc74abb802f`. Static checks bind
the exact raw index, all 620 source files and the complete Git tree's metadata.
The `work/` and `archive/` entries are metadata only: their contents were neither
read nor imported. Shared master metadata remains ef1; shared source/index and
foreign records are outside this package. Client025 and mutable runtime/config
worktrees were not inspected. The earlier ef/44 packet and all retained old
7c refs, bundle and prepared snapshots are frozen inputs, not updated expectations.

The accepted source is `/nix/store/5dg23bacx91xh56nz8i5jv0xl8hyapd6-source`:

- Commit `c31fdd9f6a86f2eb0e6b87001d6892b820bce2fe`, tree
  `6210fb758fcc80948c1ae842cad0f3520b5b189d`.
- Actual locked GitHub owner/repository `aither64/dev-workspace`, epoch
  `1792981600`, NAR `sha256-30kKzkA7kulWE3eBXlaMgG1ym+9lLuU3jdsfMOT5erA=`.
- Parent assessment SHA256
  `3483b16080c9a4732fdd08ecc26df233ef6a51b96af006b3d422a1cc958132f0`;
  actual binding SHA256
  `b57d8762406743d0afc0fcf369c8f2d6ab419e449c4e32b73ab16e5467c9ed50`.

The source lock snapshot equals the full graph in that actual binding. Its
eight locked nodes plus root map exactly into the current composed workspace
graph. `inputs.json` binds their explicit mapping. The predicted semantic final
lock changes only `dev-workspace.locked` and `dev-workspace.original` relative
to ef. It is an assertion input, never a file to copy into flake.lock. The
only intended flake.nix change is the existing nested URL's 44-to-c31 revision.
The resulting base3e72-to-final stream still changes exactly four dependency
nodes: runtime, client025/f5Aj, llm-agents ea188 and its nixpkgs f20. Extension767,
root nixpkgsd58, every other node, edge/follows path, source filtering and all
storage/reliability policy remain exact. No top-level input, extension lock edit,
incidental deduplication, schema or migration is involved.

## Future execution, after parent release

`ready.json` gives literal argv, cwd, environment, hashes, stage receipts and
finite bounds. All phases use the pinned installed Python with `-B`, the bound
Git/Nix entries and the same session environment. No Nix shell/setup/evaluation
is part of this recipe. Sensitive inherited environment values are not logged;
explicit command overrides are limited to optional-lock suppression, nonprompting
Git, Python bytecode suppression and the bound SSH executable with BatchMode,
15-second connection timeout and one connection attempt. PATH and relevant
environment values are guarded; Nix/Git override variables must remain absent.

A new session-owned parent release record must bind the exact package manifest,
c31 target, accepted final vendor receipt path/hash, release message identity and
the phases being released. The absent `parent-release-prepare-update.json` is the
intended first record. `parent-release-consolidate.json` is separate and is supplied
only after the actual update receipts and generated delta have been assessed.
No example record asserts acceptance in advance. These records are additional
evidence; no historical expectation file is changed.

1. Implementer preparation (`prepare`, future only): verify session/current,
   ready saved Sol/xhigh/workspace_write, tools, clean ef tree/index/source,
   hook configuration and frozen inputs. Fresh SSH ls-remote must show default
   exactly3e72 and own published feature exactly7c3. Fetch those exact refs over
   the literal SSH origin with source-only refspecs, `--no-tags` and
   `--no-write-fetch-head`, then repeat the remote gate. No local tracking ref or
   shared master is advanced. A changed default or feature stops for disposition.
   Preserve ef under a new own intermediate ref with an all-zero old-value lease,
   create/verify a thin ef-over3e72 bundle and snapshot the two files/raw index
   before the exact URL substitution. No existing ref or evidence is overwritten.
   The index remains unchanged and only flake.nix is dirty at phase completion.
2. A parent fresh Luna/low utility, max1, executes only `update`. Installed full
   access must be explicit (`danger-full-access`, approval `never`); parent owns
   catalog resolution and launch. The utility runs the frozen operation once,
   without independent edits, changed commands, diagnosis, retries or acceptance.
   The operation guards the prepared URL and fresh SSH refs, then runs exactly:

   ```text
   /run/current-system/sw/bin/nix flake update vpsfree-dev-workspace/dev-workspace
   ```

   It asserts the entire resulting semantic lock, all nine embedded runtime nodes,
   every unrelated source byte/mode and unchanged index/HEAD; retains actual
   generated files and narrow diff; checks whitespace; repeats remote/tool/source
   guards. There is no output build. The utility's CLI/event files are not test or
   update receipts: completion needs `effects-v1/update/summary.json` exit0 plus
   every actual exit/log named in ready.json. The source remains frozen while the
   utility owns the command and receipts. Do not inspect in parallel.
3. After parent assessment releases `consolidate`, verify the exact settled
   generated bytes and preserved ef ref/bundle, repeat fresh remote/session/tool/
   hook/input gates, stage only flake.nix/flake.lock and use normal
   `git commit --amend -F <new owned temporary messagefile>`. This folds ef into
   one final focused pin commit on the same3e72 base. Hooks remain enabled. No hook
   framework or active ordinary hook currently exists; any new declaration,
   active hook or changed hook path stops before staging. Hook installation or
   uncertain verification requires a separate parent-reviewed package.
   Prove clean final head/tree/index, complete one-commit range/diff, ef-to-final
   range-diff, all unrelated Git modes/blobs and committed generated bytes.
   This phase never pushes.

## Effects and failure ownership

Only new owned `effects-v1` receipts, the new ef preservation ref/thin bundle,
the exact nested URL and Nix-generated workspace lock are permitted before
consolidation. Consolidation additionally changes the own feature ref/index for
that one same-base commit. Shared master, remote refs, extension lock, runtime,
configuration, client, roots, old evidence and installed package stay untouched.
Nix may use its ordinary source-fetch cache/store effects; no new GC root,
derivation/output build, hash discovery or store cleanup is requested.

The runner has no default action. Each phase and every log destination is
exclusive-create; an existing effects directory or phase refuses reuse. Local
guard commands are bounded to30s, dev-session to30s, SSH ref gates to90s, fetch
to180s, thin bundle/verification to90s, the scoped update to600s and a normal
commit to120s. A timed-out command receives TERM for its owned process group,
then at most5s before KILL and a further5s join. These finite command bounds are
part of the prepared operation, not authorization to stop any other process.
There are no sleeps, retries, background work or cleanup.

Any mismatch/failure stops. Started/argv/exit/stdout/stderr records, current
head/tree/branch/status, raw-index hash and both actual file snapshots survive
even on partial effects. A Nix failure can leave the URL and a partially changed
lock; an interrupted preservation step can leave an exact owned ref/bundle;
a commit/hook failure can leave staged files or a changed feature head. Report
those actual effects and any running/uncertain command to the parent. Do not
restore, amend again, restart a phase, clean, remove refs or refresh guards.
The parent assesses the exact delta and chooses the next operation.

Later settled-lock crosschecker, mechanical/history assessment and publication
are separately held. No config inspection, CI wait, native/provider/browser/VM,
deployment/default integration, claim, session lifecycle or cleanup follows from
this preparation. Existing update/deployment docs remain authoritative; this
routine selector change needs no new project documentation.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
