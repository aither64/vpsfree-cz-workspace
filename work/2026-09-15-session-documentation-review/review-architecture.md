# Architecture and repetition review

## Findings

No Blocking, Important, or Advisory findings.

The implementation preserves the existing ownership and package boundaries.
I found no new duplicated runtime policy, hidden interface, or broken consumer
that requires remediation.

## Reviewed series

Reviewed the packet, plan/state, verification notes, local repository rules,
individual commits, final diffs, and relevant unchanged consumers.

| Repository | Base | Head | Commits |
| --- | --- | --- | --- |
| dev-workspace | `227bcfc1b989407582d3b022f8b388ac29972c16` | `9a1b16464e45d722110b448a79315a0f3ce134aa` | `b485d5d`, `9a1b164` |
| vpsfree-dev-workspace | `08d691cfd239260ce5bf7c269a44a49ce8de41e7` | `c6afe2905506fba0b8e372e0436b570f5597f8bd` | `dbf7a9b`, `c6afe29` |
| workspace | `d4382e7143b88e95bf093c8508c2867ff35160a1` | `7353127dc22275f24f1f92e5782fb34840dd0e49` | `9e7f55c`, `7353127` |

Reviewer lane: architecture and repetition, standalone, gpt-6-astra / xhigh.

## Architecture and consumer checks

- The generic runtime owns the authoring skill. The extension adds review and
  handoff requirements, while the workspace names local destinations. Their
  guidance agrees on task ownership, proportionate documentation, preserving
  uncertainty, and keeping operational instructions separate from execution
  authorization. Repeated summaries serve these distinct instruction entry
  points; the generic guide remains their shared reference.
- In runtime commit `b485d5d`, `nix/workspace-portal.nix:58` declares the built-in
  entry once. The combined skill map drives validation, schema-1 catalog
  generation, and package links. Name collisions fail during evaluation.
  Installation and rollback continue through the existing
  `libexec/workspace-host:742` reconciliation path.
- The actual extension consumer is `vpsfree-dev-workspace/flake.nix:73`. Both
  its predecessor and feature revisions derive extension skills from their
  own directories. None of the five existing skills collides with the new
  built-in. The extension pin and workspace pin select the exact reviewed
  provider and extension heads; their lockfiles agree.
- Repository-wide Nix reference searches also found the configuration
  repository's host-module consumer. At recorded remote master `b792c50e`, its
  `devWorkspace` lock pins `e9ed544bf66ba8be07b4fca27aede6e6fd1bfe0a` and
  `cluster/cz.vpsfree/machines/aitherdev/config.nix` imports `nixosModules.host`.
  The host module and host-path definitions have no diff between that runtime
  pin and the reviewed head. This documentation rollout does not require a
  configuration pin update.
- Runtime commit `9a1b164` shares exact-template seeding in
  `libexec/dev-session:3644`. It does not introduce a general migration layer.
  Current templates retain required markers; explicit predecessor templates
  preserve old bytes. Fork recovery continues to use the current template and
  its existing package-transition gate. Independent predecessor fixtures cover
  the supported recovery contract.

## Focused verification

Ran both commands from the runtime worktree through
`nix shell --inputs-from . nixpkgs#ruby -c ruby`:

- `test/dev_session_test.rb -n
  '/test_goal_seeding_|test_creation_retry_preserves_previous_tracking/'`:
  4 runs, 34 assertions, no failures or errors.
- `test/workspace_host_test.rb -n
  '/test_link_install_reconciles_extension_links_across_full_core_and_legacy_rollback|test_switch_refuses_an_unfinished_session_creation|test_switch_allows_a_legacy_journal_only_creation_for_safe_retry|test_switch_refuses_an_unfinished_session_fork/'`:
  4 runs, 25 assertions, no failures or errors.

## Residual gaps

Full Nix package builds, final-head CI, and live activation/discoverability
remain the coordinator's planned post-review checks. This review did not
deploy or alter a package generation. The focused tests validate behavior at
the Ruby boundary; they do not replace validation of the built catalog and
installed skill. Future model adherence to the writing guidance remains an
editorial concern assessed through ordinary reviews.
