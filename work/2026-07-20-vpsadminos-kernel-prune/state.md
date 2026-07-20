# 2026-07-20-vpsadminos-kernel-prune

## Repositories

- `vpsadminos`
  - base: `origin/staging` at `702155fb91effd7102a92b568f684c7b0d948b1f`
  - branch: `2026-07-20-vpsadminos-kernel-prune`
  - worktree: `worktrees/2026-07-20-vpsadminos-kernel-prune/vpsadminos`

## Status

Implementation committed and pushed. Quick verification, mandatory standalone
review, and full builds of both retained kernel CI toplevels passed. Branch CI
is queued awaiting a self-hosted runner.

## Commands run

- Verified `bin/dev-session current` and matching
  `VPSFREE_DEV_SESSION_SLUG`.
- Fetched `repos/vpsadminos.git` from its SSH origin.
- Read the workspace and repository `AGENTS.md` files and the mandatory change
  review skill.
- Inspected kernel definitions, livepatch and eBPF registries, module behavior,
  tests, history, downstream configuration references, and retained kernel
  source fixes.
- Created the dedicated vpsadminos feature branch and worktree from current
  `origin/staging` with `bin/dev-session worktree add`.
- Evaluated `.#lib.kernelVersions`, both retained kernel CI toplevels, and the
  proactive-swap QEMU package.
- Ran `./test-runner.sh ls 'ebpf-livepatch'` and
  `./test-runner.sh test 'ebpf-livepatch'`.
- Evaluated kernel livepatch and eBPF selections for 6.12.48 and 6.12.95 with
  a direct Nix expression.
- Committed both changes through installed Overcommit hooks from `nix develop`.
- Ran `nix develop --command overcommit --run` on the committed head.
- Ran the mandatory fresh-context change review with exactly one standalone
  reviewer after all intended commits and quick checks.
- Ran `nix flake check` on the feature head and on a clean temporary worktree
  at the exact staging base, then removed the temporary worktree.
- Pushed the feature branch to the SSH origin.
- Built both retained kernel CI toplevels with `nix build --no-link`.
- Started monitoring GitHub Actions run `29780892771` for the pushed head.

## Results

- The current registry contains eleven kernels; nine will be removed, leaving
  6.12.48 and 6.12.95.
- `os/configs/proactive-swap-qemu.nix` directly defaults to removed 6.12.81 and
  must move to 6.12.95.
- No real livepatch or BPF LSM program is used only by removed kernels. The
  cumulative patch and both active guards remain needed by retained 6.12.48.
- Examples are explicitly retained per user direction.
- Exclusive `untilKernel = "6.12.89"` preserves ptrace guard coverage through
  6.12.88.
- Commit `2df4dd49e` prunes kernels and updates the proactive-swap QEMU default.
- Commit `bb3b2eeac` makes eBPF `untilKernel` exclusive and updates coverage.
- `flake.lib.kernelVersions` evaluates to `["6.12.48","6.12.95"]`.
- Both retained kernel CI toplevel derivations and the proactive-swap QEMU
  derivation evaluate successfully.
- Mitigation evaluation results:
  - 6.12.48: cumulative kernel livepatch, `ptrace_mm_guard`, and
    `cifs_spnego_guard`.
  - 6.12.95: no kernel livepatch and `cifs_spnego_guard`.
- The targeted eBPF livepatch suite passed: 30 examples, 0 failures.
- Full Overcommit passed: Nixfmt and RuboCop are green.
- Both retained CI toplevels built successfully. The 6.12.48 build compiled the
  cumulative livepatch with kpatch, found the expected changed functions, and
  produced `livepatch_1.ko`; this confirms that the patch must be retained.
- Feature head `bb3b2eeac9d52e14261e8a2076ae6704725ce206` is pushed to
  `origin/2026-07-20-vpsadminos-kernel-prune`.
- GitHub Actions run `29780892771` targets the exact feature head. Its first job
  remains queued because no self-hosted runner has accepted it yet.
- The first ambient-shell commit attempt was blocked because `nixfmt` was not
  on `PATH`; rerunning inside the documented Nix development shell passed. The
  existing durable note
  `notes/vpsadminos/2026-06-14-overcommit-missing-ambient-shell.md` covers this
  behavior.
- One direct Nix mitigation-selection expression initially had a shell-quoting
  syntax error; the corrected expression evaluated successfully.

## Mandatory change review

- Result: no Blocking, Important, or Advisory findings.
- The reviewer confirmed that both commits are focused, the requested kernel
  set and exclusive bound semantics are correct, examples and required
  mitigations remain, vpsAdmin treats the field as opaque evidence metadata,
  and the independent targeted suite passes 30 examples.
- Residual gaps after post-review validation: the proactive-swap QEMU output
  was evaluated but not booted; fleet runtime kernels must still be checked
  before a downstream pin advances; an unknown external consumer could have
  assumed the historical bound was inclusive.
- `nix flake check` stops before affected outputs because the existing
  `overlays.all` output is a list and the generic checker requires overlay
  functions. The exact failure reproduces at base `702155fb9`, so it is not a
  branch regression. Direct output evaluations and targeted tests are used
  instead. A durable note is in
  `notes/vpsadminos/2026-07-20-flake-check-overlay-list.md`.

## Open questions

None.

## Cleanup

- Remove the initiative worktree after integration or abandonment; keep the
  feature branch unless the user requests deletion.
