# Package P: reusable kernel update process

Owner: implementer0. Accepted design: [design.md](design.md). Package P only;
Linux replay and kernel catalog changes are separate K/R packages.

## Scope and provenance

Repository: `vpsfreecz/vpsadminos`, target `staging`, branch
`2026-11-17-stable-kernel-update`, worktree
`worktrees/2026-11-17-stable-kernel-update/vpsadminos`.
Initial base: `a7d71a54a15496976cb0fccebb8a1b589f24f5e2`.
Six intended paths: `AGENTS.md`, `README.md`, `mkdocs.yml`,
`docs/os/kernel-updates.md`, `skills/update-kernel/SKILL.md`, and
`skills/update-kernel/agents/openai.yaml`.

One logical process/documentation commit; no migrations, schema, runtime,
configuration pin or package catalog changes. No Linux edits, source publication,
release-ref promotion, integration or deployment in P. No historical or externally
consumed migration boundary. Global independent final review remains lead-owned
once K/R are committed and quick checks pass.

## Quick checks

- `nix develop --command python3 <skill-creator>/scripts/quick_validate.py
  skills/update-kernel`: exit 0, "Skill is valid!".
- Generated ordinary UI metadata with skill-creator `generate_openai_yaml.py`.
  Inspected PyYAML-parsed metadata: short description is 25–64 characters,
  default prompt contains `$update-kernel`, automatic invocation remains enabled,
  only ordinary interface fields are present.
- Relative Markdown links resolve. Repository-source paths exist. All shell
  example blocks pass `bash -n`. Native `git rebase -h` confirms `--empty=stop`,
  `--reapply-cherry-picks`, `--onto`, and `--no-update-refs`; Nix prefetch help
  confirms raw-file hashing/JSON interface. Build command matches `os/Makefile`
  and the kernel workflow's version-to-output naming.
- Executed the exact documented stable/unstable `nix eval --json --impure --expr`
  example: exit 0. Stable selected/Linux version `6.12.117`, Linux derivation
  `/nix/store/splppa8hrdg2s5njq2rn8990zr43l6lr-linux-6.12.117.drv`, Linux source
  `/nix/store/irq31a9wf081gvvss97k54x9r4p2wja8-764acbb0ca8c4b60ee5b98f89406b152e992b1d6.tar.gz`,
  built-in and user ZFS source
  `/nix/store/gfbfdram71x5imp44590b04pc0wch182-source`.
- Same expression: unstable selected/Linux version `6.18.49`, derivation
  `/nix/store/jc8n7yv848b9xay2bwc7g0c166mnln56-linux-6.18.49.drv`, Linux source
  `/nix/store/00851ybgngm3ajyaksp34w67pvkzq3y5-a770f5086fc500ca258852aea1cb3e209a342d2b.tar.gz`,
  built-in and user ZFS source
  `/nix/store/zwxj43rfcbl0vamyw42a24g5rsyv80g9-source`.
- `nix eval --raw .#ci-toplevel-kernel-6_12_117.drvPath`: exit 0,
  `/nix/store/878s11516sppcfmnf0b2dw0zgkz3sagr-vpsadminos-system-vpsadminos-26.05.git.a7d71a5-dirty.drv`.
  This checks the documented output interface, not a new target build.
- `nix develop --command make doc`: exit 0 after lead's direct writing pass and
  final line wrapping/rebase-flag change. Build took 0.91 seconds. Existing nav
  notices only: `os/faulted-write-ci-handoff.md` and `os/livepatches/template.md`.
- `git diff --cached --check`: exit 0.

Ambient Python lacked PyYAML for the initial metadata generator call; passing the
explicit skill name allowed generation, and validation ran successfully in the
repository Nix environment where PyYAML is available. No dependency was added.

The optional all-files `nix develop --command overcommit --run` started a broad
Ruby scan unrelated to the six changed paths. Lead directed stopping it and using
ordinary installed commit hooks. SIGINT sent only to verified owned RuboCop PID
359401 and Overcommit PID 357314; tool session 7136 joined with exit 65 and
"Hook run interrupted by user". Both PIDs confirmed absent. No hook bypass and
no product check failure claimed. Normal commit hook result is recorded below.

## Documentation placement and process decisions

| Topic | Reader/class | Authoritative home | Evidence |
| --- | --- | --- | --- |
| Repeatable kernel ports and package selection | Maintainer process | `docs/os/kernel-updates.md` | Current package/build/flake/workflow interfaces inspected; selector example executed |
| Agent discovery and invocation | Agent instructions/UI | `skills/update-kernel/` and AGENTS routing | Skill and metadata validation; README/MkDocs entry links |
| Exact P revisions and results | Session execution evidence | This file | No run-specific inventory or fixed patch count added to project process |

Lead applied the user-facing writing skill directly before commit. Subsequent
changes only wrapped lines and added `--no-update-refs` to the replay example,
preventing inherited Git settings from moving retained refs during a topic rebase.
No design deviation or helper framework was introduced. Actual Linux replay,
archive fetch, new catalog selector and long product checks remain K/R/V work.

## Final P commit and release

Final P head: `46cd1215337a36fbab5b796a956a6cd096ef3384`. Normal `git commit -F <temporary-message-file>`
inside `nix develop`: exit 0, installed pre-commit Nixfmt passed; commit-msg hooks
passed with advisory 72-column body-width warnings (all lines remain within the
required 80-column limit). No bypass. Worktree clean after commit.

The complete P range is the initial base above through this one commit. The
process is usable for K; independent global review and remaining K/R/V acceptance
are still outstanding. implementer0 reports P for lead acceptance and confirms
capacity for a separately dispatched next package. No publication/default
integration or lifecycle action performed.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-17-stable-kernel-update/

## Demonstrated process correction during R

K reported a replay stalling in promisor classification with required parent/old/
current blobs local and no network child. Its successful command-local overrides
disabled only the actual promisor remotes; stored configuration remained unchanged.
The project process now includes conditional diagnosis, safe command interruption
and HEAD/index/done/todo reconciliation, proof of local content, temporary remote
classification override and visible missing-content failure. It does not encode
the incidental transient index lock as a clone-specific requirement.

Lead directly applied the writing skill to this new paragraph. The unpublished P
logical commit was amended from `46cd1215337a36fbab5b796a956a6cd096ef3384` to
`435d83468d7a3089eeb45f171d0ab244748f43b4` under the exclusive OS window; no
catalog pin changed in this step. `quick_validate.py`, `make doc` (1.02 seconds),
staged diff check and ordinary installed commit hooks all passed (exit 0).
Commit message was rewrapped to 72 columns and hooks had no warnings. One final
process commit remains; original receipt above describes its pre-correction head.
