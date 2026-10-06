# ConfCtl Configuration Update Skill Plan

## Goal

Extract the repeatable process from the `vpsfree-cz-configuration` NixOS
25.11 to 26.05 rollout and turn it into a reusable Codex skill named
`confctl-configuration-update`.

The skill should help future agents update NixOS/nixpkgs channels and related
ConfCtl-managed flake inputs faster while preserving the repository rules:
use ConfCtl input commands for generated input updates, build affected
machines, handle NixOS deprecation warnings, and commit compatibility fixes
in logical steps.

## Affected Components

- `confctl`
  - Repository-owned skill under
    `skills/confctl-configuration-update`
- Workspace tracking:
  - `work/2026-06-05-confctl-configuration-update-skill/plan.md`
  - `work/2026-06-05-confctl-configuration-update-skill/state.md`

No vpsFree production configuration repository is changed by this initiative.

## Source Material

- `work/2026-06-03-nixos-26-05-port/plan.md`
- `work/2026-06-03-nixos-26-05-port/state.md`
- `vpsfree-cz-configuration` branch
  `2026-06-03-nixos-26-05-port`
- `vpsadminos` branch `2026-06-03-nixos-26-05-port`, especially its
  repository-specific `PORTING.md`

## Approach

1. Review prior work notes and commits for the configuration rollout.
2. Create the skill in the `confctl` repository so the process is versioned
   with the tool that owns ConfCtl configuration workflows.
3. Keep the skill focused on configuration repositories that use ConfCtl
   flake channels, especially `vpsfree-cz-configuration`.
4. Include the process for:
   - reading NixOS release notes;
   - preparing workspace plan/state and worktrees;
   - updating the `confctl` input when needed;
   - updating ConfCtl channels/inputs with `confctl inputs ... --commit`,
     generally with `--no-changelog` for noisy inputs;
   - using generated ConfCtl commits for input bumps;
   - building representative and full machine scopes;
   - treating Nix evaluation deprecation warnings as work items;
   - committing compatibility fixes separately with explanatory messages;
   - recording blockers such as missing local secrets or ISO images.
5. Validate the skill with the skill-creator validation script.
6. Commit the skill on a ConfCtl feature branch with repository hooks active.

## Compatibility And Deployment

The skill itself has no runtime compatibility impact. It must, however, encode
the operational rule that future configuration updates are live
infrastructure work and must explicitly consider mixed-version operation,
rollback, persisted state, generated configs, service APIs, and deployment
ordering in each initiative plan.

## Decisions

- Place the skill in the `confctl` repository at
  `skills/confctl-configuration-update` per user direction, rather than in the
  global Codex skills directory.
- Do not add helper scripts initially. The workflow is procedural and depends
  heavily on repository-local ConfCtl commands and target selection.
