# Native cleanup fixture confirmation correction

The bounded lead-assigned correction is committed locally as
`52ed98c988c011ff4c3127b25e0930fd6fb77eb3`, tree
`4b299131feba1f8f64ac2dba675d40d542bb98ae`, parent
`ee3f1fdd0d3585a8f4fa9b952169d692e9fa3d5f`. Runtime index and worktree were
clean after the ordinary Nix-shell, temporary-message-file commit. No hook
framework is declared; Git hooks/config were inspected and none were bypassed.
The complete staged diff was inspected. Only
`nix/tests/session-archive-lifecycle.nix` changed: 11 insertions, 3 deletions.

## Cause and preserved contract

Exact EE3 Check41533913313 retained `runtime-ci-ee3f1fdd/all-jobs.log`, lines
15663–15679, shows `printf "yes\n" | dev-session delete ... --as-is --force`
failed with `requires an interactive terminal confirmation`. The fixture's
`machine.fail` accepted that unrelated failure, then the ordinary removal
journal read failed ENOENT. All 13 retained SHA256SUMS entries were verified.
Full log SHA256 is
`eb6b62177cc51f2e081469614e09934cf6adf05f7146a4810e323001c234e676`.

CLI confirmation precedes lifecycle lock/runner entry. With authorization,
ordinary deletion durably prepares its removal journal, advances to
`thread_retired`, then publishes the matching service prelude before attempting
strict service shutdown. An uncertain stop retains both records and supporting
files. A independently confirmed this ordering read-only. Product confirmation,
cleanup, retry, receipt, API and schema semantics are unchanged.

The fixture now uses util-linux `script --quiet --return --command` to give the
CLI a real terminal and propagate its exit status. Delete and its original-force
retry receive `yes`. The related new automatic-archive fixture's stop receives
its exact slug. Existing real-PTY confirmation precedent is
`test/dev_session/lifecycle_commands_test.rb`'s
`test_lifecycle_confirmation_uses_a_real_terminal_before_taking_the_lock`.
No generic harness or historical `archive_acceptance.py` helper was added or used.

The failed delete must now report the intended registered-service shutdown
verification refusal. Its ordinary journal must remain `thread_retired` with
force; its prelude must remain `services_pending`, operation `delete`, with the
same operation ID and force. Original worktree/supporting-file preservation,
restored invocation, original command retry, actual native stop/unload, retired
registry transfer and active-registry removal assertions remain intact.

## Quick checks

All checks used the repository's pinned Nix environment or its pinned Nixpkgs
tools. No native VM, product build, package check campaign or CI polling ran.

- `nix-instantiate --parse nix/tests/session-archive-lifecycle.nix`: pass.
- Nix-evaluated actual fixture testScript compiled as Python: pass.
- Pinned NixOS driver type prelude, machine type hint and actual evaluated
  script: `ty check --extra-search-path NIXPKGS/nixos/lib/test-driver/src` and
  `ruff check --select F`: both pass, matching driver checks.
- Three harmless probes execute the exact evaluated fixture command wrappers:
  child stdin is a TTY, delete answer is `yes`, exit 1 and exit 0 propagate, and
  stop receives its exact slug. All pass. These probes do not invoke lifecycle
  commands. Disposable check source is `cli-fixture-confirmation-quick.py`.
- `ruby test/dev_session_test.rb --name '/\Atest_(delete_requires_confirmation_in_noninteractive_cli|delete_uses_a_simple_interactive_confirmation|lifecycle_confirmation_uses_a_real_terminal_before_taking_the_lock|stop_requires_an_interactive_exact_slug_confirmation)\z/'`:
  4 tests, 21 assertions, zero failures/errors/skips in 0.329629 seconds.
- Final staged/committed whitespace, owned-path inventory and cleanliness: pass.

The first direct component-file Ruby invocation failed before assertions because
its `NullTmux` support is loaded by the declared aggregate suite. The corrected
aggregate-loader command above passes; no product or test-support change was
needed. No second broad test campaign ran.

Fixture blob: `92f161ca0869ac11fa8671b39fd0ebb5a3004f73`.
Fixture SHA256: `e68adb83a4a4c4a422ba98a4356fec677cc25bee7f9ad35fab52c792ee94e2fb`.
Evaluated script SHA256: `91843d7d0a61d7984af2bfc0bf3f7ad2c1771049283191cc4abca051826c2cf6`.

## Handoff and limits

Runtime Git lane returned to lead; no unfinished command effects. Explicit old
EE3 ref is
`refs/heads/2026-11-02-session-temporary-service-cleanup-runtime-ee3-before-cli-confirmation`.
Suggested eventual consolidation is into owning dependent EE3 commit, as shown
by the fixture's path history. No rebase, fold or publication was performed.
No migration or consumption boundary changed. Pins and artifacts remain held
at their historical EE3 scope. Native cleanup acceptance is still outstanding;
lead coordinates source acceptance, final history and any later exact native run.
No product documentation update is useful for this fixture-only correction.

## Local history consolidation

Lead directly inspected and accepted the narrow correction, then authorized its
local fold before A's separate capacity-retry work. Ordinary Nix-shell interactive
rebase folded only `52ed98c9` into dependent EE3; the owning message stayed
unchanged. No source edits or repeated checks ran during consolidation.

Final local head is `5b4b711748343f4ffe88b96c50d88a9f98eeb04d`, tree
`4b299131feba1f8f64ac2dba675d40d542bb98ae`, exactly equal to the fixup tree.
Base remains `c2182254d29c4175c3e9fe4267e5a92dd1da6b79`. Full final series:

1. UI `19dd03b79a2997098934afafbe70c63b978c1ca7`.
2. Core `f7add7cea8a836810d32688ef2d1cf4cc011af19`.
3. Dependent `5b4b711748343f4ffe88b96c50d88a9f98eeb04d`.

Old reviewed range is `c2182254..ee3f1fdd`; new range is
`c2182254..5b4b7117`. [Full range-diff](cli-fixture-fold-range-diff.txt) shows
UI/core `=` with identical hashes; dependent-only correction is exactly
[the accepted fixture delta](cli-fixture-fold-accepted-delta.patch), 11+/3-.
Old EE3 ref above remains, and exact fixup is retained at
`refs/heads/2026-11-02-session-temporary-service-cleanup-cli-confirmation-52ed98c9`.
No migration, schema, compatibility or external consumption boundary changed.

Ordinary exact local Git metadata identifies source
`/nix/store/rb2v6x010g84y50821bbk8bd3q1ifpjf-source`, with independently hashed
NAR `sha256-l3YwtKW6POMz3WAH+Rf8WQ8BE/5GhYLNudAhJLgilww=` matching metadata.
It is retained by the session-local indirect root
`cli-fixture-fold-retained-source`. [Metadata](cli-fixture-fold-source-metadata.json)
binds exact final head. All nine lock nodes/fields/edges and source/checkout lock
bytes equal EE3; lock SHA256 is
`fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955`.

Source/index were clean at lane return, and no owned operation remains. No push,
pin change, build, native/CI execution, deployment or live lifecycle action.
This local history/source proof supplies no future long-check result. Lead owns
final intended-source review after the separately requested capacity deliverable.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
