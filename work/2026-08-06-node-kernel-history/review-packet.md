# Mandatory review packet: observed livepatch lifecycle

## Requested outcome

Review the final committed cross-repository series for correctness, focused
history, architecture, compatibility, deployment safety, tests, and alignment
with `plan.md`. The change must:

- keep availability and transition-only observations out of public history;
- create `applied` only when a patch is newly observed loaded, enabled, and
  stable, with an inferred report interval rather than a manufactured exact
  timestamp;
- create `removed` when an effective patch disappears;
- keep stable boot state from creating a redundant lifecycle row;
- migrate only safely identifiable legacy history and preserve ambiguous data;
- expose only applied/removed/null lifecycle actions compatibly;
- render compact inferred times without hiding the full interval from mouse,
  keyboard, or assistive-technology users;
- avoid any new vpsAdminOS completion-marker service or protocol; and
- keep the kernel-version-specific livepatch test unchanged as release
  certification, not claim that it is a generic test for future kernels.

The standalone reviewer must perform the review directly and must not spawn
nested reviewers or subagents.

## Initiative context

- slug: `2026-08-06-node-kernel-history`
- plan: `work/2026-08-06-node-kernel-history/plan.md`
- state: `work/2026-08-06-node-kernel-history/state.md`

## Repositories and revisions

### vpsadmin

- worktree:
  `worktrees/2026-08-06-node-kernel-history/vpsadmin`
- base: `92bba722b16d8f1e68e183f7041be1d44a17db7d`
- head: `bc6eb8e20f9cc4fa7b9c9f22650bc2cd235fc33d`
- commits:
  - `5c3e59a95` — `api: record observed livepatch lifecycle`
  - `01af411e3` — `webui: label effective livepatch lifecycle`
  - `32035b72c` — `webui: simplify inferred version timestamps`
  - `bc6eb8e20` — `tests: cover compact history tooltip in browser`

### vpsadminos

- worktree:
  `worktrees/2026-08-06-node-kernel-history/vpsadminos`
- base/head: `008aa4605ec263397bf46bd9fe915a01be1670a6`
- expected feature diff: empty

### vpsfree-cz-configuration

- worktree:
  `worktrees/2026-08-06-node-kernel-history/vpsfree-cz-configuration`
- base: `d6f1c5d1`
- head: `157eea17eb8249d22fff214016723cdf324cb92f`
- commits:
  - `40242970` — generated production vpsAdminOS pin to `008aa460`
  - `53e0664a` — generated vpsAdmin role pins to `bc6eb8e2`
  - `157eea17` — deployment and rollback runbook

### vpsadmin-kb-captures

- worktree:
  `worktrees/2026-08-06-node-kernel-history/vpsadmin-kb-captures`
- base: `7248a8b`
- head: `c3c1eb5c0d544149432417d3d92a64b653b75411`
- commit:
  - `c3c1eb5` — exact vpsAdmin contract/flake pin

All branches are pushed. The configuration worktree contains untracked local
`.bin/` and `.bundle/` development caches; they are not part of any commit.

## Commit-split rationale

- The API commit keeps the recorder behavior, nullable action schema, one-way
  data correction, public resource contract, generated API locales, and direct
  specs together because they form one deployable lifecycle contract. The
  migration and behavior cannot be deployed independently without an invalid
  model/schema combination.
- The lifecycle-label WebUI change is separate from the cross-table timestamp
  renderer. Each can be reviewed and reverted independently.
- The timestamp commit includes its PHP helper, styling, generated Czech
  catalog, and helper-level regressions. Those translations belong to the same
  visible behavior; the final Czech corrections were folded into this owning
  commit instead of retained as a feature-branch fixup.
- The expensive real-browser fixture/spec is separate from the production
  renderer so the behavior diff remains focused and the VM coverage is clear.
- Generated `confctl` pin commits remain separate and exactly generated. The
  operator runbook is a distinct documentation commit.
- The capture repository's flake URL/lock and two contract revision fields are
  one indivisible exact-revision pin; it changes no semantic control or PNG.

No unrelated implementation is deliberately bundled.

## Exact dependency/configuration pins

- `vpsadminosOsStaging`, `vpsadminosStaging`, and
  `vpsadminosProduction` resolve to
  `008aa4605ec263397bf46bd9fe915a01be1670a6`.
- `vpsadminStaging`, `vpsadminServices`, and `vpsadminProduction` resolve to
  `bc6eb8e20f9cc4fa7b9c9f22650bc2cd235fc33d`.
- The capture contract and flake pin the same final vpsAdmin revision.
- vpsAdmin itself retains its default vpsAdminOS input
  `31b3dff4306cce8904ac45630a931a7b72d36507`; the history design has no
  vpsAdminOS source dependency. Production configuration independently selects
  `008aa460` for the actual livepatch release.

## Quick verification

- `nix develop .#api -c bundle exec rspec
  spec/models/operations/node/record_kernel_evidence_spec.rb
  spec/api/resources/node_kernel_evidence_spec.rb
  spec/api/resources/node_kernel_history_spec.rb`: 41 examples, 0 failures.
- Migration specs, run separately because their helper replaces the schema:
  5 examples, 0 failures.
- `nix develop .#libnodectld -c bundle exec rspec
  spec/nodectld/system_probes/security_evidence_spec.rb`: 7 examples,
  0 failures.
- `nix develop .#webui -c vendor/bin/phpunit
  tests/Regression/NodeEvidencePagesTest.php`: 13 tests, 73 assertions.
- API i18n generation, WebUI `locales-update`, and WebUI `locales-health`
  passed. The final Overcommit run also passed those checks, Nixfmt,
  migration specs, PHP CS Fixer, RuboCop, and API i18n.
- `git diff --check` passes. vpsAdminOS is byte-clean against its base and
  `tests/suite/kernel/livepatch-6.12.95.nix` is unchanged.
- Configuration hooks/Nixfmt, exact six-input assertions, and
  `nix shell nixpkgs#mkdocs -c mkdocs build --strict` passed.
- `nix develop -c bin/check` in the capture repository passed: 39 controls,
  29 paths, 32 capture concepts, 65 bindings, 9 exceptions, 15 tests, and
  118 PNG variants.
- Final-head GitHub workflows are still running. No long VM integration test
  has been started for this final design before this review.

## Compatibility and deployment assumptions

- Existing reporters already provide loaded/enabled/transition. The optional
  `verified_at` field remains accepted but is ignored for lifecycle timing, so
  mixed reporter/API versions require no protocol bump or coordinated node
  update.
- The action column is nullable and the internal event enum is appended. Old
  public event numbers and `event_type=livepatch` remain stable.
- The corrective data migration preserves evidence and ambiguous rows but is
  intentionally one-way. Old supervisors are quiesced across the API migration
  so they cannot recreate availability-only public rows.
- New WebUI code is backward compatible with null actions; old WebUI code uses
  its generic livepatch label for new public rows.
- No node reboot or vpsAdminOS rollout is required for the history semantics.
  Revision `008aa460` is deployed independently because it contains the actual
  cumulative patch release.
- Production deployment and production KB writes remain outside the authorized
  task.

## Known residual test scope

- The Playwright admin-cluster example and configuration host builds are the
  priority long checks after the review gate.
- The version-specific vpsAdminOS VM test depends on pinned historical kpatch
  artifacts that were previously unavailable from this workstation. Its hash
  guards must not be weakened or bypassed.
