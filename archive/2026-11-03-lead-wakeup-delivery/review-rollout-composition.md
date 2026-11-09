# Final deployment-composition review: W/C

## Findings

No new Blocking, Important or Advisory findings.

Earlier R1–R4 closures remain applicable within their reviewed source boundary. R5 remains explicitly deferred; this composition review does not claim that its optional diagnostic change was implemented.

## Identity, scope and reviewed sources

Reviewer: retained reviewer0, saved gpt-6.1-sol/xhigh/read_only; no overrides, fallback, nested reviewers or subagents.

Before reading session records, dev-session current from the exact bound tracking directory printed `2026-11-03-lead-wakeup-delivery`. Both shell markers were absent and the trusted developer binding matched the exact slug and absolute workspace.

I read the mandatory-change-review skill and all four lane references, applicable workspace and repository instructions/procedures, current packet, rollout design, implementation-c evidence and selected coordination-guide snapshot. General, architecture/repetition, scope/proportionality and risk/compatibility all apply.

Reviewed complete committed ranges:
- W: `12a3df65467c7c460cae5e0a3cd8dca60138288e..c51f4bdddba82e693f41eb79fac1776751c8c23c`, tree `ce0705dd01bcd81dbfeb5c13bead47b5c7dd6f43`.
- C: `f4069909b55fbed907cb658f350ec6a59f97e05a..83bc2113154698972ba8f68a8723058c093b4365`, tree `9f2e25f8f3c9cd702ea190bfeccf76793bfbd083`.

Both worktrees were clean at these heads, including the final read-only recheck. Each stated base is the actual merge base.

I verified review-rollout-runtime.md SHA256 `7607fed52b5fd6eec5566ff749035b32fce0b9347cd6b9d5186828e749de2945` and reused its completed component review for R `58e87f9d3ccc1aac262b29f587a1d0553257a554`. I did not repeat the unchanged runtime audit or infer whole-package equivalence to925.

This is final review of completed W/C source and composition after quick checks, before long artifact verification. The unresolved external invoker is a later operational prerequisite, not evidence that these source deliverables are unfinished.

## Scope and generated-lock semantics

The current change is proportionate to the deployment direction: four source files across two repositories select the reviewed runtime and retain the already reviewed monitoring guidance. It adds no functional module, public API, framework, schema, supervisor, timer, polling driver or tooling workaround.

I inspected both complete diffs and independently compared parsed locks with their exact bases.

W changes only:
- `flake.nix:8`: the existing direct nested `vpsfree-dev-workspace.inputs.dev-workspace.url`.
- That runtime node's locked revision, NAR and timestamp, plus its original exact revision in flake.lock.
- The separately committed owned verification guidance.

All 34 other W lock nodes, root mapping, input edges and follows paths are unchanged. Extension `f8da821e3c76e26e73aa9d89a712eab0e0faa319` and NAR `sha256-U5y/TEny6nsyXWNlCMktmxTZhpVO0QY4kOo/qgwsapM=` remain. No top-level runtime input, extension-lock rewrite or dependency deduplication appears.

C changes only `devWorkspace.locked.lastModified`, `narHash` and `rev` in flake.lock. All 63 other lock nodes, the root mapping, original input selector and follows/input edges remain unchanged.

Both selected runtime nodes are exactly:
- type github, owner aither64, repository dev-workspace;
- revision `58e87f9d3ccc1aac262b29f587a1d0553257a554`;
- NAR `sha256-oSIqoC8obbx1cNg7DPOFJfXxJm+tUJwLm4Y8cDv9JfI=`.

I checked C's actual patch against configuration.patch and its lock SHA256 against the packet: `4e6a7c9eb51c60543778d19aac5f44217158e0be6c710d45b2986f3ce1df74e3`.

## Actual consumers and ownership

W remains the application-package owner. `workspace/flake.nix:54–72` calls the extension's mkPackage with the existing site/team, coordination, integration and machineIdentityConfig, and exposes that composed package. It does not select the generic runtime's default package as a substitute.

I inspected the actually pinned extension f8 source. Its mkPackage delegates to its dev-workspace input, retains the supplied team and machine identity configuration, and installs the existing protocol-1 confctl adapter through organization tools. The direct nested R input therefore reaches the intended provider while preserving the extension and site composition.

C's channel mapping is unchanged at `vpsfree-cz-configuration/flake.nix:134–136`: channel dev-workspace, role devWorkspace, root input devWorkspace. The aitherdev module includes that channel. Its config resolves `inputsInfo.devWorkspace.input` (`cluster/cz.vpsfree/machines/aitherdev/config.nix:16`) and imports that input's `nixosModules.host` (`106`).

This is the host-substrate path. The R host module's system package is the substrate reconciler; it does not install W's composed workspace application. The existing standalone system Codex packaging in C is not a replacement for the composed user-profile package. Actual built native/output identities still need artifact verification.

The source preserves site hostname, alias and wildcard. I read the checker implementation and its tests: it resolves the intended runtime paths and compares exact GitHub revision identity plus site registration. The independent lock audit additionally confirms matching NARs and preservation of the surrounding graphs. The checker is source/composition evidence, not a build or live-health proof.

## Physical/profile identity, ordering and recovery

W's `config/machine-identity.nix:2–15` retains:
- repository origin `github.com/vpsfreecz/vpsfree-cz-configuration`;
- selector/name `cz.vpsfree/machines/aitherdev`;
- the legacy `machine:vpsfree:aitherdev` bridge to that same structured profile identity.

C's canonical SSH origin matches that repository, and its module declares the exact standalone aitherdev machine under that selector. Existing coordination configuration retains adapter confctl and the same machine mapping. No source mapping/alias change is bundled in these pins.

I inspected f8's actual confctl adapter resolution contract. It resolves the committed configuration revision and exact selector through confctl metadata, returns the actual name and optional shared-lock label, and rejects a different name. That supports the intended common physical/profile identity; the final held typed binding must still be verified against the actual committed deployment batch before activation. This review does not substitute static source inspection for that action-time check.

Host-first followed by the composed user-profile switch is consistent with the source interfaces. R preserves the selected public3bb runtime obligations, including managed-turn proof, registered-service lifecycle and typed machine claims/identity. The newer host substrate can precede the application selection; no source change requires adding the application to the system configuration.

The policy2-to3 MCP change still requires the selected workspace-host command's ordinary native-idle admission. Identical Codex bytes do not waive it. The external-shell handoff documented in design.md:975 onward preserves normal checks; a registered service starts immediately and is not an after-turn dispatch guarantee.

The rollout correctly leaves the external invoker and command/status/log handoff pending before any claim or activation. No new delayed driver, forced stop, private lifecycle helper or legacy job is justified by that gap.

The selected coordination guide and design preserve the necessary operation boundaries:
- build and copy prepared artifacts before machine ownership where supported;
- retain an atomic, session-owned application output root and an exact named confctl generation with source/input/DRV/NAR identities;
- acquire only the exact schema2 physical machine claim near activation, then check held ownership, current committed mapping and predecessor profile token;
- use ordinary named-generation dry-activate/switch with health checks and auto-rollback, and verify both running-system and system-profile identities;
- select W only through the selected workspace-host's ordinary compatibility, transition, idle and registration checks;
- retain original target/journal/claim and recover forward after partial or uncertain selection.

I also checked the pinned adapter's retained-generation and recovery behavior: generation metadata and artifact identity are compared; activation preserves auto-rollback; final success requires both live system links; matching links alone do not certify an interrupted activation or rollback completed. The ordinary manual confctl path must likewise retain actual command/effect evidence. No retained adapter receipt is fabricated by this review.

A preselection refusal is distinct from a selected forward target. Reverting to925, deleting retained state or directly editing profile links is not a supported recovery. System auto-rollback does not authorize downgrading the application profile or prove that remote effects ended.

Machine release remains conditional on verified deployment/effects and fresh evidence that the complete deployed R/W/C lineage is integrated into approved remote defaults. Integration requires separate explicit repository/target approval. Session completion, review and machine release grant no archival, deletion, stopping or cleanup permission.

## Complete history and consolidation

I independently inspected W's entire base-to-head series:
1. `e19a92678d03609452106eaa909a547d2644d489` — owned guidance, +17/-5.
2. `c51f4bdddba82e693f41eb79fac1776751c8c23c` — runtime selection, flake.nix plus generated lock, +5/-5.

The complete W diff is three files, +22/-10. The guidance and dependency selection are independently reviewable and correctly separated. I recomputed old adabd..a595 and new12a..e19 guidance stable patch IDs; both are `01452f19880095667380a968894e4d3c0777744b`. Current guidance SHA256 matches `76aba9ddaa801ce803ab5c8e1e7aeda38a516dffd98ec2e47faa9c04352bf00b`.

The historical64-commit prefix is outside current12a..W ownership and is not retroactively approved here.

C's complete owned series is one generated commit:
`83bc2113154698972ba8f68a8723058c093b4365`, flake.lock only, +3/-3. Its generated message retains the exact3bb..R history, including both coherent R commits. The generated-message width exception applies; rewriting it is unnecessary.

I independently checked C's earlier registered2fe..freshf406 delta: it is the single public vpsadminServices lock update to `b83b26e1ba1c8e869ae3ffbcb5801ed071c3844e`. It is preserved as baseline provenance, not included or erased as an owned deployment change.

Both complete owned series are coherent. No obsolete approach, superseded pin, fixup or abandoned compatibility path remains. There is one final runtime selection per consumer: W's nested input and C's channel role. These are necessary separate consumer updates, not redundant successive pins. There are no repeated update streams requiring further consolidation and no retained intermediate-pin exception.

## Migrations and persisted-state lineage

No database migrations or seeds in either W/C range. Neither range introduces a persisted-format change, transitional reader, migration guard or new state consumer API.

The pins select the exact R already reviewed for its direct final private monitor schema1 and preservation of current public managed-turn, service, recovery, submission and typed-claim obligations. These existing public baseline formats remain supported obligations; older925 acceptance cannot justify dropping them.

Known monitor state provenance remains disposable/CI usage, with no known live persistent consumer. I did not inspect peer/private state or claim global absence. No evidence requires retaining an intermediate W/C pin or branch-iteration migration. Migration/state lineage and history consolidation are sound for these exact ranges.

## Verification evidence and limits

The packet reports W deployment-contract tests4/19 passing in1.294s, Nix parsing/whitespace success, and unchanged-guidance tests10/217. I inspected the actual checker/test source and independently confirmed the retained guidance patch and final lock semantics.

I read C's actual command/status and hook logs. The ordinary pinned confctl channel set --commit completed in24.184s; Nixfmt/pre-commit and commit-message hooks passed, with only the documented generated-width warnings. Post-pin inputs ls exited0. No hook bypass or toolchain/source workaround appears.

The single final deployment-checker status records exit0 in12.229s, exact Wc51/C83 heads and cleanBeforeAndAfter. Its actual output identifies the canonical workspace hostname and R58. I did not rerun it.

These checks do not establish final package/system outputs or live usability. Outstanding acceptance includes:
- new composed managed W package and exact named aitherdev system generation, rooted and bound to complete source/input/output identities;
- current R verification inventory29, including14 Ruby shards/10 suites and aggregate, plus applicable composed/configuration checks;
- all11 native scenarios against the final composed candidate and actual pinned native executable;
- applicable exact-source CI, built startup/claim/catalog/native contracts and live host/profile/monitor acceptance.

Old925/a595 managed build, native11, runtime28, composed6 and CI positives stay attached to their old inputs. R component CI41871232953 was reported running; I did not inspect CI or treat it as W/C composition acceptance.

The documented trusted cell/tool-session reporting limitation and unverified fresh pre-bootstrap/surviving-cell archive boundaries remain. No global cell quiescence or new native archival capability is proved by pins, checker success or this review.

## Disposition

Final all-four-lane review of completed W/C source and deployment composition is complete with no new findings. Runtime review is reused only for its exact R component. Later artifact and live gates remain explicit; review grants no execution, activation, integration, deployment, profile selection or session lifecycle permission.

Read-only constraints preserved: no files written, tests/builds/probes/native/push/CI/claims/host/profile/deployment/default/lifecycle actions run, and no peer-session access. Full Markdown is sent to the lead for verbatim persistence as review-rollout-composition.md; original reports remain intact.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/
