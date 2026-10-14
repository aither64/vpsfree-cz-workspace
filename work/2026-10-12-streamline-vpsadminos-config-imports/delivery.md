# Delivery status

The import feature is implemented and its original revision independently
reviewed and published. Runtime testing exposed an independent impermanence
identity failure; complete persistence acceptance remains unmet. A committed
diagnostic refinement and prescribed review fixes are published. Neither branch is integrated;
no production host, guest or KB change has been made.

## Result

Stable guests import `vpsadminos.nixosModules.containerStable`; `container` is
the same selector. Both select from the guest evaluator's nixpkgs release.
Exact imports use `vpsadminos.nixosModules.containers."26.05"`, or
`containers.${nixpkgs.lib.trivial.release}`. Eight release keys and all old
underscore aliases are available. Legacy configuration aliases keep their
latest-stable behavior. Unstable remains explicit; unknown releases fail early.

Stable ordinary/impermanence templates use the selector. Existing guest files
are not rewritten. Guest nixpkgs pins, stateVersion and compatibility settings
remain unchanged by the import migration. No host coordination or data migration
is required. The owning guide is `vpsadminos/docs/containers/nixos.md`.

## Published branches

Both use branch `2026-10-12-streamline-vpsadminos-config-imports`:

- vpsadminos: `4a40154539bf6dc73d391c30326af255b4dc15b2`, one logical v2 commit
  above `1150e37b1cc997b1728f2fda806a3433ef55b798`, 13 paths.
- vpsfree-kb-contracts: `2d11b2cc8445a695e7862af18ca0a70598afb38b`, one narrow
  declarative annotation companion above `ce2c8cd9358c3636e5d39343e595df813a0b197f`,
  three paths. No new controls, checker logic, screenshots or managed pages.

## Verification

Passed: real NixOS 24.11/25.11/26.05 evaluations, all eight raw-file/alias
comparisons, caller-library selection, old stateVersion, legacy/unstable and
unknown-release paths; four generated flakes/locks at final committed head;
standalone files and exact KB consumers; formatting, hooks, MkDocs, annotation
tests and strict contract repository checks. Published v1 RSpec and companion Check
passed. The source image workflow failed three impermanence variants; ordinary
variants passed. Final v2 generated-lock verification passed. Fresh v2 hosted
CI started automatically; cancellation of superseded v1 core CI was requested.

Final independent review found no source defect. Requested dataset annotations
and the validation paragraph in the source commit message are fixed and checked.
The source message amendment preserved its tree. Full-corpus KB checking still
fails on two unchanged IP-address pages; the same counts/discovery differences
are reproduced in the baseline. All six candidate pages match their counts,
discoveries, source guards and manifests. No full-corpus pass is claimed.

Runtime attempt 1 failed before boot on missing host revision metadata; attempt
2 corrected metadata but hit the Unix socket path limit. Attempt 3 uses the
existing runner configuration route with truthful published host metadata and a
short uniquely owned state directory. Its stable ordinary case passed all fifteen tests, including rebuild and restart.
The local impermanence case was cancelled after the hosted failures arrived;
it is incomplete, and the two local unstable cases did not run. No local VM
remains. Hosted ordinary cases passed; all three impermanence cases failed.
Logs and exact limits are in `verification-results.md` and `state.md`.

## KB release and next action

Six complete bilingual NixOS, Impermanence and User Data candidates, guarded
snapshots and schema-5 manifests are committed in the workspace at `2784facf`
and annotation remediation `63d9495a`. They remain local review candidates.
Staging belongs to another session with a pending release and is untouched.
Publication needs ordinary staging ownership, fresh source-drift checks, public
availability of the new exports on the default source and approval of the exact
staged pages. No merge or production publication approval has been given.

Resolve the pending prerequisite scope decision, complete runtime verification
and reconcile CI before declaring readiness. Then
integration requires explicit direction for vpsadminos/staging and
vpsfree-kb-contracts/master. Session remains active and open.

Artifact registration is refused because a retained ready creation journal
exists. Records remain linked locally; no private finalization or cleanup was
used to bypass that refusal.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-12-streamline-vpsadminos-config-imports/

## Discovered independent impermanence defect

All three hosted impermanence cases rebuild and restart, then lose the allocated
UID under the adversarial fixture. Raw compatibility files and explicit unstable
behavior are unchanged. Source shows the stage-2 proc guard and a separate
activation specialfs snippet without an ordering edge before legacy users.
The allocator should restore IDs from persisted /var/lib/nixos, so removing the
challenge or setting fixed IDs would mask the defect. Numeric maps/mount state
still need clearer runtime evidence. The diagnostic refinement is published as
`4a40154539bf6dc73d391c30326af255b4dc15b2`. Affected review found no Blocking
issue; both prescribed Important fixes and final lock checks passed. The concrete
[prerequisite proposal](impermanence-prerequisite-proposal.md)
is unverified and awaits the user's include/defer decision. No raw change is authorized
under the accepted boundary. Import functionality passes, but complete
impermanence identity acceptance is unmet; branch readiness is not claimed.
