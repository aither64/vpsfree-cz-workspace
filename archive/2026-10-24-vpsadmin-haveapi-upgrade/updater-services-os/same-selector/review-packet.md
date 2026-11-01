# Corrected OS selection: final source and quick review packet

Historical3fdec package; currentfinald632 requires narrow test/history review after full-suite findings. See [current test-repair packet](test-repair/review-packet.md).

Original status: final review accepted by lead (reviewer0 native01a1912c, all four HIGH lanes, no findings, coherent history and NO MIGRATIONS). Corrected feature publication passed with an exact old-acc lease after remote recovery preservation; [publication receipt](publication/receipt.json). New-design normal flake and installed-flake/runner checks are in progress; no package acceptance or deployment is claimed.

Repository `git@github.com:vpsfreecz/dev-workspace.git`; own worktree `worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsfree-dev-workspace-services-os`; branch `2026-10-24-vpsadmin-haveapi-upgrade-services-os`.

Base **767dfd587e346168e1443e65ccdb67ce748f3fe3** / tree **80181fb9f3805e99734b85edfdbcdd022f5e4b67**. Corrected head **3fdecfbbdd93f92754a0384d0134958c260cf619** / tree **4990ae5d719e4d7cdea8d207660ad26632fb4270**. [Full inventory](final-inventory.json), [complete one-commit history](history.txt), [final diff](final.diff).

## User correction and history

The user requested the same OS selector for creation and updates and explicitly allowed desirable OS upgrades. The lead accepted architect0's final design.md section “2026-10-31: same OS selector for creation and updates”, including the target-proof compatibility disposition. The former services-only applied-input pin is superseded. This review is for changed semantics; the old review/package/native results do not validate this design.

Old published range: `767dfd5..acc495827de81cce0fa7a7cf3f34e9f15c9516b1`, tree `c3fb82f170a9757d5c5e0928cc3381ba90233bdd`. Preserved at `refs/heads/2026-10-24-vpsadmin-haveapi-upgrade-services-os-applied-pin-recovery`; remote feature still selects that old commit. The new local range `767dfd5..3fdecfbbdd93f92754a0384d0134958c260cf619` contains one direct corrected commit, with no old applied-pin/revert/fixup stream. [Old diff](old-published.diff), [old/new delta](old-new.diff), [range comparison](range-diff.txt). This is intentionally **not patch-equivalent** to the old branch. No published ref was rewritten, and no new feature publication is claimed. Old roots, outputs, failures and the held/uninstalled consumer132/package61v remain intact.

No repeated dependency/channel/generated pin stream. **NO MIGRATIONS**: no persisted schema, envelope version or on-disk format change; no migration versions to release/deploy/consume. The intentional compatibility consequence is that an ordinary update of an unproved legacy target now refuses rather than guessing its VM context. Existing recovery is usable only where historical evidence supports it. Another target's proof is insufficient.

## Implementation and invariants

Seven assigned files changed; all105 other tracked entries match the baseline exactly. No nix/test.nix wiring was necessary: the existing source-path argument already separates the export from build inputs. No generic runtime, OSVM, vpsAdmin33d6, consumer configuration, private/auth/client inputs or installed profile changed.

- `vpsadminos_input`, revision/dirty handling, Nix overrides, `compatible_configuration!` and `machine_layout` are byte-identical to the baseline; [guard hashes](unchanged-guards.json). Creation, services, node and all use the same own-worktree-or-locally-fetched-origin/staging selection. There is no implicit fetch or fallback to old inputs.
- A read-only `build-context` action validates the old applied envelope and each requested target's existing proof before credentials/build. `all` needs all actual target proofs. Same-target pending retry uses old applied metadata; conflicting operations refuse. Proved targets may coexist with unproved peers, whose descriptors/proof status remain exact.
- The Nix projection consumes lazy `make-test.config`, validates topology and every non-payload layout field independently, and preserves only the recorded OS export plus host qemu/virtiofsd paths. It then selects new allowed payloads for the requested target(s), carrying untouched descriptors verbatim. Reused NixOS rootDisk.image remains exactly old, including absence. A services projection cannot force a throwing node payload. The final Ruby strict guards remain unchanged.
- Retained start validates current requested layout using the same host-metadata distinction and boots proved applied payloads. Fresh creation and separate maintenance copy-only semantics stay unchanged. Updates keep ordinary copy/switch/API-restart/refresh/proof/promotion ordering; switching does not replace running kernels or retarget virtiofs.
- The private context file is passed only to the Nix build command and removed after that command. Its environment does not escape into later runner/copy commands. New fixed diagnostics go directly to stderr under baseline Ruby verbosity; no private/user values are interpolated.

README and diagnostics use the lead's settled [operator wording](operator-final.md), including legacy proof qualification, candidate/rootDisk and portal retained-start wording. Worktree exports preserve their path, not frozen contents. Technical comments/tests/doc changes all support this one selector/projection behavior.

## Actual quick evidence

All commands used the declared `checks.x86_64-linux.tests` environment, pinned Ruby3.4.9 and the existing runtime contract, with CPU60–63/nice5/Nix1job2cores. Retained840 watcher configuration remains unavailable; the authorized visible owner fallback was used. No full command suite or ordinary long flake/runner check ran for this new source.

| Scope | Actual result and evidence |
| --- | --- |
| Final real Nix projection | PASS: lazyServices, retainedBoot, selectedTargets, absentImagePreserved; ten layout/topology mutations refused. [Final log](final-cli.log) |
| Owning maintenance suite | 34 tests /250 assertions /0 failures/errors/skips, exit0. [Final fast log](final-fast.log) |
| Final cold-start and candidate-payload root guard | 2 tests /21 assertions /0 failures/errors/skips, exit0. [Final fast log](final-fast.log) |
| Final refusal/CLI diagnostic check | 1 test /32 assertions /0 failures/errors/skips, exit0; four proof/conflict variants, exact diagnostics and no build/credential/events. [Final log](final-cli.log) |
| Other scoped passing cases | Selector equality (8 creation/services/node/all × worktree/staging combinations) and failed-build safety passed in [original7 batch](focused-quick-attempt-1.log). Same-target retry with unproved peers, services-only effects and stable credential bytes/modes, and staged all promotion before later copy failure passed after the environment repair in [affected5 batch](affected-quick-attempt-1.log). The later change was only cold-start fixture reset plus candidate-root fixture refinement and explicit diagnostic assertions; no relevant production behavior changed for these retained passes. |
| Syntax/format/hooks | Bash/Ruby syntax and git diff whitespace0; pinned nixfmt1.4.0 format/check0. [Formatter log](nixfmt.log), [precommit guard](precommit.json), [ordinary commit output](commit.log). No declared hook framework or active hooks; no bypass. |

These are scoped results, **not an aggregate green full-suite claim**. The new full command file contains48 methods. Old49-command/old36-maintenance package results are not relabelled. Full ordinary flake and installed-flake/runner checks are held until accepted final review. The new standard Nix-smoke case will evaluate a real services projection, retained host/export/image fields and untouched descriptors after review; pre-review proof uses the actual pure projection function with a throwing fixture, and the full smoke script passed syntax checks only.

Preserved failures and fixes:

1. Initial pure fixture used the repository root's lib instead of the provider outputs; corrected to import the actual provider with root-locked nixpkgs, avoiding upstream source selection. [Attempt1](initial-quick-attempt-1.log).
2. The original maintenance fixture lacked host virtiofsd/qemu fields now required for actual VM context; explicit fixture fields corrected it. [Attempt2](initial-quick-attempt-2.log).
3. Focused7:7 tests/162 assertions/4 failures, exit1, caused by an exported temporary context path leaking after unlink into later commands. Fixed by command-scoped build environment, preserving the original result.
4. Affected5:5 tests/79 assertions/1 failure, exit1. All repaired runtime cases passed; the cold-start fixture accidentally reused its deliberate invalid network. Reset from original applied descriptors fixed that case; no layout assertion was weakened.
5. An unrooted formatter store path became unavailable; normal pinned nix shell restored the formatter for the final format/check. No collector actor was inferred and no storage investigation/collection was performed.

## Requested review and release boundary

Risk HIGH: deployment inputs, target authorization, retained layout/proof, retry and cold-boot compatibility. Lead should assign retained independent reviewer0 Sol/xhigh/read_only all four applicable lanes (general, architecture/repetition, scope/proportionality, risk/compatibility), with explicit whole767..3fdec history/consolidation and NO MIGRATIONS conclusions. Old acc review is historical only.

The owning extension exposes the provider through lib.mkPackage to its consuming workspace; new environment/action seams are internal, with no public CLI flag or state-schema change. Installed provider/flake/maintenance match selected767 except ordinary shebang, as recorded in [baseline proof](baseline.json). Source preparation does not install or select it.

All owned quick operations ended. Source is clean; writer reservation remains only for concrete review findings. No remote publication/ref rewrite, default integration, CI, profile preparation/activation, live cluster query/retry, VM/kernel build, collection/deletion or lifecycle action occurred. Lead/E1 own the next reviewed publication and consumer/activation release. The session stays open.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
