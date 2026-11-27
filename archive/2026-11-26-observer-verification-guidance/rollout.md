# Observer guidance rollout

## Latest delivery acceptance — 2026-11-27, generation6j

**The observer change is already installed and healthy.** All seven observer roles
in `/nix/store/6j7rpx2j176blr46602kzzpb8ycm1mwp-dev-workspace-0.2.0` contain exactly
the reviewed 4,087-byte text, SHA256
`6057ebc7639a99651ae5ca4b70d85f8761537cdf3bfa43beedfc020ee793d011`.
Catalog digest is the reviewed
`4ae58b06cf34c345d952f2ce0288a78d739c5ee06584292062220a217e7f7922`.
This supersedes the earlier4d gap and conditional alignment/build proposal.
No new source change, build, deployment, machine claim or bridge audit is needed.

One pure evaluation of immutable published workspace root
`0d24fd5596e65ae1e918e9441142d1e11bf418ec` returned exactly the installed deriver
`/nix/store/ifpsi7200wia0v0dcr091kgamq4w62wd-dev-workspace-0.2.0.drv`, exit0,
without building. This establishes independently reproducible integrated source
for the installed artifact. It does **not** identify the original historical
root Git commit used by the other deployment; metadata does not publish that
commit, and none is inferred from an embedded skill source. Lead owns fresh
remote-head and feature ancestry evidence and final acceptance.

Both live system and system profile resolve to
`/nix/store/akwb3y9nqydy9nj4iv5crsk9kycnb6yd-nixos-system-aitherdev-26.05.20261121.94c3211`.
Clean effective configuration is
`a3af000f116bca48dd59b9fd3f0ca46fd433a640`, with host runtime
`bbe27c6ffb5f367e7be9a4ce45bffdf34185854f`. Public embedded site source is
`/nix/store/cjnqvrqb039j4in8nb20rmzb62kn672q-source`, narHash
`sha256-1Czt0OMylhDnPPB2+OF4lKYmApCgLCIJPR/l3pbp7Xs=`. Its reviewed catalog blob
is `e87fc582aca4e9113d7abd4f663f2f6b9f3012b6`. Complete embedded source graph
(38 nodes) is checks/current-6j7-embedded-source-input-graph.json, SHA256
`d7c34d963d38a25880ba869615cb6aee72681ef6d145420c9ceb8a450aedff76`.
It names runtimebbe matching the host, extensionbf12 and codex-web2547. Full
revision/content-hash/follows data remains in that graph; effective host input
metadata is checks/current-6j7-effective-host-inputs.json. The embedded graph
scope is kept separate from the derivation proof above.

Minimal current-generation checks passed: authenticated HTTPS healthz200
`{"ok":true}`, existing session page200, active/running portal/router/coordinator,
Codex and tmux units. The exact native binary remains
`/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/bin/codex`;
app-server socket target is unchanged and tmux remains PID1917. The Codex service
wrapper PID changed with intervening deployment; no unchanged-process claim is
made. All retained roster native thread IDs, saved settings and prompt hashes
are identical to November26. Current conversation/team access succeeded; no new
session/naming trial was created. Existing observer0 retains its saved4,021-byte
prompt by design; newly selected observers receive the installed4,087-byte role.
HTTPS credentials stayed in process memory and are absent from evidence.

Evidence: checks/current-6j7-observer-delivery.json,
checks/current-6j7-source-derivation.log, checks/current-6j7-http.json,
checks/current-6j7-health-continuity.log and
checks/current-6j7-roster-identities.json. No peer records/transcripts, private
helpers, lifecycle/recovery operations or source/build/claim mutations were used.
The earlier unused claim remains released; there is no new session-owned
activation or unfinished command effect. Earlier spsm was never selected by this
session. Architect's final design addendum and lead acceptance choose existing
delivery acceptance; no further optional verification is required. Session stays
open. This update records evidence only and triggers no new automatic review.

## Earlier checkpoint — 2026-11-27, superseded4d generation

**The feature is not deployed in the current installed catalog.** All seven
observer-bearing presets in `/nix/store/4d0iy6lkl1jq9nngi9mkf3mb2ydj6vxi-dev-workspace-0.2.0/share/dev-workspace/agent-teams.json`
still contain the old 4,021-byte instructions; none equals the reviewed 4,087-byte
text. Installed instruction SHA256 is
`94fe948392735f3341b6e58deb02edfd78356259fda47ca3226f968f202180ff` and catalog
digest remains `1184a2cf511b6e77ff7afe12433027abe06e8bb0b897f39cffc26efd443d1a7c`.
Direct result: checks/current-2026-11-27-observer-verification.json. No successful
successor deployment, ancestry or current-generation health claim is made.

The current package derivation is
`/nix/store/pd7m1g0nwcn8lii6xwj3fc5zy41bh72q-dev-workspace-0.2.0.drv`.
Both current live system and system profile resolve to
`/nix/store/k79k3l35lnhfikw65zwnacag112w7z9p-nixos-system-aitherdev-26.05.20261121.94c3211`.
Live confctl metadata names clean configuration
`109d789f0a4ee875f8bd27a0b72ea76c38ee234a` and effective host runtime
`f3bd843f9858b87cef66d0949706f8af16ba9b13`.

The package's public extension catalog identifies embedded update-codex site
source `/nix/store/dnk49kl0n97d2h078dnh87m3k3gzadqj-source`, narHash
`sha256-IhqJKl/OwdCbg0Mvx80uJuZo/KzXlFCv0SyeoYj7N4E=`. Its catalog source blob
`d1af7ba23bf0277cac8be4d9749576566fd1e850` differs from reviewed844 source blob
`e87fc582aca4e9113d7abd4f663f2f6b9f3012b6`. Its complete embedded source lock graph
is checks/current-2026-11-27-input-graph.json (38 nodes), SHA256
`eaebc1bd5aac5a1cbab2bbf26c981e27b6abe367ef9f327e359051a499cbda6c`.
That embedded graph names runtimee310, extensionbf12 and codex-web2547; it is
**not asserted to be the effective package or host graph**. Current metadata
publishes no exact root application Git commit, so none is inferred from this
skill-source reference. No peer-session records/transcripts were read.

Lead reports queued machine claim `4ace1db8-6721-45f6-99fd-06624bd570db` was
granted after the baseline changed, then released unused; released revision3
verified at11:01:44UTC. This session attempted no activation and owns no unfinished
command effects. Accepted candidate spsm below was never selected by this session
and is stale against the new baseline. Own source worktree remains clean at844.

Smallest remaining gap: prepare a compatible application package for the current
generation that contains exactly the reviewed observer guidance, then perform the
lead-owned activation and fresh verification under new ownership. This checkpoint
performs no new preparation, build, switch, claim mutation, source edit or broad
successor review. Health/continuity work was not expanded after the decisive
installed-prompt failure. Prior health evidence below belongs to November26,
not the current4d generation. Lead owns the next scope/transition decision.

## Historical preparation — 2026-11-26

Status: application build and composition checks passed; ready for lead activation.
No activation or machine claim by implementer0. Lead owns acceptance, activation driver and claim release.
User authorized deployment through vpsfree-cz-configuration. No system build,
configuration pin change, source edit, new test/harness or team reconfiguration.

## Exact source, inputs and machine

Reviewed/merged application source: workspace
`844ac4dbf768ebced1d27d208f4d5ebaf8b82deb`, one commit over reviewed base
`bbfaf615b7c1406fc028a486330efda9fb35cb04`. Canonical origin
`git@github.com:aither64/vpsfree-cz-workspace.git`, target `refs/heads/master`.
Lead's state.md records exact remote equality and released integration claim;
there is no refreshed history or migration. Fresh deployment-lineage acceptance
and final claim proof remain lead-owned.

Immutable application source: `/nix/store/l9qqkxnnnvi2wbazxdrxymiflxhbqhyx-source`,
narHash `sha256-8kzc3lS+913JgUwO5kSNyWA3xGj+QYNxOeSbio8g3+8=`. Exact Git flake:
`git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-26-observer-verification-guidance/workspace?rev=844ac4dbf768ebced1d27d208f4d5ebaf8b82deb`.

Actual deployed configuration: clean revision
`3637ae47905dff5762e43dfd0c6e3b9a7f9a8444`, recorded by
`/etc/confctl/configuration-info.json`. Its immutable source is
`/nix/store/mljg4lgkv01ss3mg9b8b8w0qninyr3fv-source`, narHash
`sha256-ccBSZysNxYcHJw39nHpifVnQ15POoTVehVWofgph0nE=`. Source flake.nix/lock
bytes match that exact canonical Git revision. Its devWorkspace input and live
`/etc/confctl/inputs-info.json` both select the application's runtime
`2a1d58df7c3bb845da4d286ef38989bae01da4a0`. Lead accepted this effective-host
proof; no system rebuild is needed.

The newly registered configuration branch/worktree instead starts at
`1e43e2e18c85cf1fc63f31327d1f8e5eb953eab8` and locks an older runtime. It is
unchanged and supplies writable cwd-local tooling and registered machine metadata;
it is not represented as deployed source. The actual deployed immutable source
supplies the configuration environment and contract-check authority. Machine
config/site files compared between these sources are identical. No pin or
configuration branch was moved to hide the distinction.

Configuration canonical origin is
`git@github.com:vpsfreecz/vpsfree-cz-configuration.git`; selector
`cz.vpsfree/machines/aitherdev`, adapter `confctl`. Selected profile policy targets
`machine:github.com/vpsfreecz/vpsfree-cz-configuration:cz.vpsfree/machines/aitherdev`;
`machine:vpsfree:aitherdev` is its legacy bridge. Lead will acquire a fresh schema-2
machine-only claim using registered repository `vpsfree-cz-configuration`, inspect
authoritative held status and verify-machine once before activation. Claim
transport is `dev-session coordination`, not workspace-host acquire.

Complete immutable input graph receipts, including every lock node, follows edge,
revision and content hash:

| Source | Complete graph | Lock SHA256 |
| --- | --- | --- |
| Application, 38 nodes | checks/workspace-deployed-input-graph.json and checks/workspace-exact-deployment-metadata.json | e2a11c7851138e5532796764073b5c43aad6c053524dc0fa18f548412bc6f733 |
| Deployed configuration, 67 nodes | checks/configuration-deployed-input-graph.json and checks/deployed-configuration-metadata.json | 1924df90f2b576ceb1181f689c3d236ecb8f3f8b8d591cd4b3fed65bf539d477 |

Application root inputs: nixpkgs follows vpsfree-dev-workspace/nixpkgs; extension
`vpsfreecz/dev-workspace@bf12ac71a8a00b1581eed5352f99c1b2daaeff5b`, narHash
`sha256-hlCQCMgmNe8qa1fbujQiWduylaOVla9rz0jtOy22LV8=`. Its direct nested runtime
is `aither64/dev-workspace@2a1d58df7c3bb845da4d286ef38989bae01da4a0`, narHash
`sha256-mzRZ4p7PCqhWldMNqWNBU6dR6tmLLVRuzLGEIH++MVc=`. Runtime codex-web is
`aither64/codex-web@2547d535eefd4154afef4125ea0fb76e5894a8b6`, narHash
`sha256-rLBeHQVPUfmqPw0tMjkenkp+BA0Xi2VX/iMz+4wiT9c=`. All pins remain unchanged.
The configuration channel is dev-workspace, role/input devWorkspace. This package
does not deploy new configuration content or claim the existing deployed config
revision is newly integrated.

## Current and prepared generation

- Old profile link: `/home/aither/.local/state/dev-workspaces/profile` →
  `profile-295-link` →
  `/nix/store/3y9ns5h3raj9zszrwcr5pgvf9gng8q4b-dev-workspace-0.2.0`.
- Old package derivation:
  `/nix/store/v73s88chsa19a35lln0d4jyra7w3ajz2-dev-workspace-0.2.0.drv`.
- Both live `/run/current-system` and system profile
  `/nix/var/nix/profiles/system` resolve to
  `/nix/store/z16l3iq5sa5l1f8mb4wqiyd9b7n8i3iv-nixos-system-aitherdev-26.05.20261121.94c3211`.
- Candidate derivation:
  `/nix/store/ysj7g2lqhwp6s6r9x3w987y1vgv3nabh-dev-workspace-0.2.0.drv`.
- Built candidate output:
  `/nix/store/spsm07acm7c5frfhjmy1na79jc4hipg4-dev-workspace-0.2.0`.

Pure evaluation of exact Git844 and the ordinary real-worktree source returns
the identical complete candidate derivation. An exact dry run of the driver's
ordinary `nix build --no-link --print-out-paths SOURCE` source form confirms the
same drv/output (no build). Nix labels the sparse working source dirty despite
clean Git tracked status/diff-index; this warning is recorded and candidate
equivalence is independently established. Build uses the immutable Git revision;
the supported ordinary switch uses the real directory because --source is
File.realpath'd by the selected driver. A Git URL is not a switch directory;
a plain Nix-store source is not a derivation. Receipts:
checks/deployment-source-equivalence.json and checks/switch-source-dry-run.json.

## Settled configuration environment and commands

Use this writable CWD for every shell entry:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-26-observer-verification-guidance/vpsfree-cz-configuration`.
The immutable configuration flake is explicitly
`path:/nix/store/mljg4lgkv01ss3mg9b8b8w0qninyr3fv-source`.
Its declared tools shell checks `$PWD/Gemfile` and bootstraps local .gems/.bundle;
Gemfile matches deployed3637, while Gemfile.lock is the retained checkout's own
tooling lock. The tracked configuration stays clean. Exact confctl source:
`/nix/store/zh2jpdp1hcllnb761v1n61z2yykdkamq-source`; config shell derivation
`/nix/store/zr4kz39wbwypw25dn1d4ff05mvbnh9m8-nix-shell.drv`.

Existing cross-repository check **passed, exit 0** in that environment:

```sh
nix develop path:/nix/store/mljg4lgkv01ss3mg9b8b8w0qninyr3fv-source --no-write-lock-file --no-update-lock-file --command ruby /nix/store/l9qqkxnnnvi2wbazxdrxymiflxhbqhyx-source/bin/check-dev-workspace-deployment --workspace-root /nix/store/l9qqkxnnnvi2wbazxdrxymiflxhbqhyx-source --configuration-root /nix/store/mljg4lgkv01ss3mg9b8b8w0qninyr3fv-source
```

It reports the canonical portal hostname and matching runtime2a1d. Log:
checks/deployment-contract-passed.log. Reviewed prompt/catalog/whitespace checks
are reused; the proven unrelated AGENTS size failure is unchanged and is not
rerun or described as green.

First actual application build, under the fresh watcher:

```sh
nix develop path:/nix/store/mljg4lgkv01ss3mg9b8b8w0qninyr3fv-source --no-write-lock-file --no-update-lock-file --command nix build --no-link --print-out-paths --no-update-lock-file 'git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-26-observer-verification-guidance/workspace?rev=844ac4dbf768ebced1d27d208f4d5ebaf8b82deb#default'
```

Lead-only prepared activation (same CWD; CLAIM_UUID is the exact held claim):

```sh
nix develop path:/nix/store/mljg4lgkv01ss3mg9b8b8w0qninyr3fv-source --no-write-lock-file --no-update-lock-file --command env -u GEM_HOME -u GEM_PATH DEV_SESSION_SLUG=2026-11-26-observer-verification-guidance DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz DEV_WORKSPACE_CLAIM_ID=CLAIM_UUID workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-26-observer-verification-guidance/workspace
```

Config shell Ruby is 3.4.12; packaged host Ruby is 3.4.9. Removing project
GEM_HOME/GEM_PATH only for the runtime CLI avoids loading an incompatible local
native json gem. The same command prefix with `workspace-host status` succeeds;
ordinary Git/hooks keep their unmodified project environment. Existing explanation:
notes/dev-workspace/2026-11-25-coordination-cli-nix-gems.md. No hook was bypassed.
The initial ambient post-checkout error required no registration retry or repair.

## Watch policy, receipts and bounded corrections

Selected policy package is the old profile3y9 above. Validated catalog schema6,
digest `1184a2cf511b6e77ff7afe12433027abe06e8bb0b897f39cffc26efd443d1a7c`;
execution_access full_access. Verification utility is GPT-6 Luna/low, max concurrent
1, lifetime operation. Native identity
`dw_c699c3bf36ffc569cca1d7f83580bf68e6fffbb536cfad0d`, configuration
`share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml`, explicitly
danger-full-access/never. Policy receipt: checks/build-watcher-policy.json.
Fresh native utilities use fork_turns none with exact model/effort under the
corresponding inherited full-access/never executor; they are not roster changes.
Parent stays active and owns diagnosis and acceptance.

- First utility `/root/observer_package_build`, operation
  `60115c91-20de-4ead-a2f0-5b6cab10f90a`: source metadata succeeded; shell entry
  failed because plain store source lacked path: syntax. No application build.
  All cells/sessions completed; checks/application-build-result.json.
- Second utility `/root/observer_package_build_corrected`, operation
  `4e758ebe-20a0-4354-a42e-8e716b8b2720`: shell entry failed from workspace CWD
  because tools mode requires ./Gemfile. No application build. All cells/sessions
  completed; checks/application-build-corrected-result.json.
- Full shell/CWD/source/driver diagnosis then established using existing source,
  cheap evaluations, actual checker and read-only status. No source changes,
  assertion weakening, new launcher or broader suites.
- Current utility `/root/observer_application_build`, operation
  `65ca1c37-7dab-490a-a8ab-edb46d71621c`: first actual application build.
  **Passed, exit 0**, 87.543 seconds, 2026-11-26 16:51:42–16:53:10 UTC.
  Exact expected drv/output above. Complete log checks/application-build-final.log;
  result checks/application-build-final-result.json. Only operation-owned cell
  and command session61912 completed; no running or uncertain command effects.

## Application lineage and candidate acceptance

Lead supplied fresh SSH remote-default equality for application844ac, runtime2a1d,
extensionbf12 and codex-web2547 (full exact revisions above). Configuration default
is1e43; unchanged running-host baseline3637 is **not its ancestor** (merge-base
exit1). Nothing here repairs or integrates that old configuration history.

The candidate derivation was independently evaluated outside the config shell
and is identical to the built artifact under it. Its 6,087 recursive derivation
requisites contain neither deployed configuration source3637 nor the configuration
tooling shell. Those supply only the current-host reference and tool environment;
they are not newly deployed application inputs. Receipts:
checks/application-artifact-lineage.json, checks/candidate-root-derivation.json and
checks/candidate-derivation-requisites.txt. No system/config artifact is deployed.

Candidate composition check passed: installed catalog specification exactly equals
reviewed pure evaluation; only seven observer instruction values change, 4,087
UTF-8 bytes and identical full observer roles. Generated catalog/team digests and
native configuration identities change as expected; new catalog digest
`4ae58b06cf34c345d952f2ce0288a78d739c5ee06584292062220a217e7f7922`.
Model inventory, all other settings/roles and non-agent package metadata remain
unchanged. Native executable remains Codex0.165.0 at exact path below; native
capacity stays9. Raw host/coordination driver, coordination contract, machine
policy and Pi model/provider definitions are byte-identical to predecessor.
Thus no new native launch or live-switch policy is introduced. Full result:
checks/candidate-composition-comparison.json.

## Acceptance, health and continuity

Predeployment receipts checks/predeploy-identities.json and
checks/predeploy-http.json record profile/system/native socket identities,
active portal/router/coordinator/Codex/tmux units, authenticated HTTPS healthz200
`{"ok":true}` and session page200. HTTPS uses configured public CA
`/var/lib/dev-workspaces/public/ca.pem`; credentials stay inside process memory.
No token/password is printed, stored in these receipts or added to commands.

Active native Codex resolves to
`/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/bin/codex`.
Baseline Codex service MainPID3138515, tmux service MainPID1917; app-server socket
`/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock` points to
`/tmp/codex-daemon-1000/bced879de15a05f23836072b53ea2860aa13a982415f07bf83ab93a6ee8c9ea6`.
Candidate executable/capacity/launch policy comparison passed as above. After
lead activation, verify exact candidate/profile equality,
unchanged system paths, installed observer4087 bytes/seven identical roles and
other catalog values preserved; service/HTTPS/session/roster/conversation and
native/tmux continuity. Check naming through existing status/access without
creating a session. Retained observer prompts stay unchanged by design. Predeployment roster hashes
and native thread/settings identities are in checks/predeploy-roster-identities.json;
observer0 retains4,021 bytes, trimmed SHA256
`9a013a6f45f526c3250c4445c1fed4675240082d3320cc28bc6d1df8530382e4`.

Compatibility refusal or uncertain effects require the original source/candidate,
claim and journal to stay held for forward recovery. No older-package rollback,
forced restart, receipt edits, replacement operation or lifecycle action.
Lead releases only after authoritative exact-owned-claim status, settled effects,
verified deployment and fresh proof of complete deployed feature lineage integrated
into approved remote defaults. Do not wait for separate UI acceptance. Record
release/result in this rollout; release leaves the session open.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-26-observer-verification-guidance/>

## Lead acceptance and reservation

Lead accepted completed preparation/build at the exact candidate above.
No additional source review, build rerun or broader checks are needed for these
unchanged inputs. Both source worktrees remain clean; predecessor profile is
still3y9. Machine-only schema2 claim `4ace1db8-6721-45f6-99fd-06624bd570db`
returned **waiting**, sequence527 at2026-11-26T16:56:34Z, for exact configured
vpsfree-cz-configuration/cz.vpsfree/machines/aitherdev/confctl binding at1e43.
The session owns no machine and has not activated the package. No independent
work remains; resume on grant after authoritative held-status/freshness checks.


## Lead final acceptance and fresh remote lineage

Lead accepts implementer0's final current6j delivery receipt and architect0's
no-mutation route. Exact installed4087-byte/seven-role text, matching catalog,
minimal health/continuity and no-build reproducibility proof satisfy delivery.
No further source, review, build, activation, claim or historical recovery work
is required. The original historical deployment Git head is not asserted.

Fresh SSH refs/heads/master ancestry reads at acceptance:

| Repository | Source | Fresh default head | Ancestor result |
| --- | --- | --- | --- |
| aither64/vpsfree-cz-workspace | original feature844ac4dbf768ebced1d27d208f4d5ebaf8b82deb and reproducible root0d24fd5596e65ae1e918e9441142d1e11bf418ec | 0d24fd5596e65ae1e918e9441142d1e11bf418ec | Both exit0 |
| aither64/dev-workspace | bbe27c6ffb5f367e7be9a4ce45bffdf34185854f | bbe27c6ffb5f367e7be9a4ce45bffdf34185854f | exit0 |
| vpsfreecz/dev-workspace | bf12ac71a8a00b1581eed5352f99c1b2daaeff5b | 39e7a09eb6afbf14fc5a6b6bea74fd1c0a568b55 | exit0 |
| aither64/codex-web | 2547d535eefd4154afef4125ea0fb76e5894a8b6 | 2547d535eefd4154afef4125ea0fb76e5894a8b6 | exit0 |
| vpsfreecz/vpsfree-cz-configuration, unchanged registered head | 1e43e2e18c85cf1fc63f31327d1f8e5eb953eab8 | dc1449bd244d5c601dadf99444b56d7d1eb844b9 | exit0 |

The existing host sourcea3af000f116bca48dd59b9fd3f0ca46fd433a640 is NOT an
ancestor of configuration defaultdc1449bd... (exit1). Do not call it merged or
newly deployed by this session. This session introduced no configuration feature
content; its unchanged registered head is integrated. The application artifact
is independently reproducible from integrated root0d24, whose declared inputs
are retained above. No system switch/host lineage repair is part of observer
delivery.

Both owned claims are released; the queued machine claim was unused and released
before stale-preparation repair. No deployment by that claim, no unfinished or
uncertain own effects, and no new ownership acquired for the already delivered
feature. Session stays open. Existing saved observer0 remains old4021; deployed
new selections use reviewed4087 by design.
