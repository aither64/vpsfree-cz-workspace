# Runner readiness, 2026-11-04

Current AMD job setup proves the old runner version, so overnight job-pickup
readiness is a real risk. Preserve the active campaign. One authorized SSH
inspection stopped at host-key verification before running remote commands;
there were no CI requests, Git mutations, configuration changes or service
actions. The primary feature remains frozen at
`e1751c917f216897292ab0b893727a6e5553a540`.

## Evidence and its limits

- The existing predecessor [watch log](ci-41773470432-watch.log), lines
  217–218, 291–292 and 365–366, warns that runner **2.336.0** cannot run jobs on
  **November 5, 2026**. Each annotation names **Build OS and populate binary
  cache**. This does not identify the current AMD runner's version or the cutoff
  time/timezone.
- The sole watcher's existing [job receipt](ci-e175-amd-runner-readiness-job.json)
  binds job **126712393564**, run **41865572140**, exact head **e1751c9…**, to
  runner **11199 / gh-runner4.int.vpsadminos.org**, label **amd-livepatch**.
  It contains no runner version. Lead reports no warning in the new watch log at
  that checkpoint; absence of an annotation cannot establish the version.
- Subsequently, the sole watcher captured the current AMD-v5 job **126712393762**
  in [the fixed log](ci-e175-amd-runner-version-job-fixed.log). Lines 1–2 directly
  report **2.336.0** at **2026-11-04T16:39:18.5282974Z** and
  **gh-runner4.int.vpsadminos.org** at **16:39:18.5291711Z**. A independently read
  these two fields from the existing file, with no API request. Preserve the
  watcher's original failed CLI capture. Lead/observer also identify the Nov5
  warning in current build check-run **126698786535** annotations; A has not read
  that raw annotation receipt.

## Owning source and update policy

The available canonical bare clone's `refs/remotes/origin/master` is
`ca96c95a1fee04793468785d8323a759615b2b4e`; it was read without fetching.
Its local `master` is older and lacks gh-runner4. Neither ref proves the live
installed generation. There is no repository AGENTS.md in the inspected source.

The owner is **vpsadminos-org-configuration**, machine
**org.vpsadminos/int.gh-runner4**, service **github-runner-runner.service**.
Its [machine configuration](https://github.com/vpsfreecz/vpsadminos-org-configuration/blob/ca96c95a1fee04793468785d8323a759615b2b4e/cluster/org.vpsadminos/int.gh-runner4/config.nix)
imports `configs/gh-runner.nix`, disables default scheduling labels and reserves
`amd-livepatch`. Its `nixos-stable` channel maps to root Nixpkgs, locked at
`da6dc0e7b26060f2f71ce3ef7088fb56ee44fa36` (`nixpkgs_3` in this lock).
The [package recipe](https://github.com/NixOS/nixpkgs/blob/da6dc0e7b26060f2f71ce3ef7088fb56ee44fa36/pkgs/by-name/gi/github-runner/package.nix#L34)
has version **2.338.0**; the inspected owning configuration has no runner-package
override. This is source evidence, without system evaluation or deployment proof.

The pinned [NixOS service module](https://github.com/NixOS/nixpkgs/blob/da6dc0e7b26060f2f71ce3ef7088fb56ee44fa36/nixos/modules/services/continuous-integration/github-runner/service.nix#L164)
registers with `--disableupdate` and starts `${cfg.package}/bin/Runner.Listener`.
A restart uses that same package. Startup also cleans the work directory, so it
cannot be treated as a harmless way to refresh an active runner. The source's
job-active guard coordinates Nix GC; it does not establish deployment safety.

[GitHub's policy](https://docs.github.com/en/actions/reference/runners/self-hosted-runners#runner-software-updates-on-self-hosted-runners)
normally enables self-update, permits disabling it, and requires timely manual
updates when disabled. GitHub can stop assigning jobs when an available update
has not been applied for 30 days, or for a required security update. The official
[latest release](https://github.com/actions/runner/releases/tag/v2.338.2) is
**2.338.2**, with progressive availability. Neither fact establishes this
organization's exact enforced minimum or proves 2.338.0 is insufficient.

## Live inspection boundary

The one ordinary SSH attempt used the confctl transport's root user, exact FQDN,
and `CONFCTL_SSH_CONFIG` if already present, with `BatchMode=yes`, 10-second
connect timeout and strict host-key checking. Terminal SSH exit **255**:
`No ED25519 host key is known for gh-runner4.int.vpsadminos.org`;
`Host key verification failed.` No alternate address, retry or trust repair ran.
Live `/run/current-system`, profile generation, source revision, unit
ActiveState/SubState/MainPID and fixed executable path remain unknown.

At pinned confctl `af164b442100b92b8d93c0d67b315eff982e0180`,
[`MachineControl#ssh_args`](https://github.com/vpsfreecz/confctl/blob/af164b442100b92b8d93c0d67b315eff982e0180/lib/confctl/machine_control.rb#L176)
uses ordinary SSH, root, the configured target and optional
`CONFCTL_SSH_CONFIG` via `ssh -F`. It does not provision host-key trust. No
automatic trusted-host record mechanism is documented in the inspected owning
flake or confctl README/manual. This attempt already honored the optional
configuration route. A verified trusted host-key record through the operator's
existing trust procedure is a prerequisite; no scan or relaxed checking is
proposed.

## Prepared target route, not executed

Commands below require a separately authorized clean configuration checkout at
**ca96c95a…**, its declared pinned Nix environment and resolved live/recovery
identities. No checkout, environment realization, evaluation, build or copy was
performed. Target **2.338.0** is already in that configuration's input recipe;
no input update or 2.338.2 repin is proposed. This normal confctl route builds
the machine's whole NixOS container system, so its live-to-desired diff must be
reviewed before treating the operation as a runner-only change.

The [pinned confctl manual](https://github.com/vpsfreecz/confctl/blob/af164b442100b92b8d93c0d67b315eff982e0180/man/man8/confctl.8.md)
documents build, generation selection, copy-only deployment, switch and automatic
connectivity rollback. Its flake builder selects both outputs below. The machine
key was derived from its published sanitization/SHA256 algorithm, without Nix
evaluation.

Minimal cache-plan preflight, for a fresh utility if root authorizes it:

```sh
nix build --dry-run --no-link --no-write-lock-file --no-update-lock-file \
  --option allow-import-from-derivation false \
  '.#confctl.build.m_org_vpsadminos_int_gh_runner4_5cd15058.toplevel' \
  '.#confctl.build.m_org_vpsadminos_int_gh_runner4_5cd15058.autoRollback'
```

Expected scope is exactly this container system and confctl's rollback helper,
including runner/.NET dependencies. Desired store paths, cache completeness and
closure size are not known. This dry-run must perform no builds; stop for missing
locked inputs, IFD requirements, unexpected kernel/old-Nix work or any planned
build rather than expanding into realization. Root must coordinate uncertain
duration with the existing watcher slot. Only an accepted cache plan and reviewed
system delta can authorize subsequent prebuild/copy:

```sh
confctl build -y 'org.vpsadminos/int.gh-runner4'
# Record exact NEW_GENERATION and both output store paths from that build.
confctl deploy -y --generation "$NEW_GENERATION" --copy-only \
  'org.vpsadminos/int.gh-runner4'
```

Before activation, an operator must fence new assignments to this dedicated
runner, then let the current job finish and verify it is idle. An idle snapshot
alone races queued pickup. No maintenance/drain mechanism is documented in the
inspected owner configuration or confctl deployment instructions; the GC job
marker is insufficient. Root must obtain the exact approved external scheduling
fence/drain procedure, or defer activation until there is no pending work and
new assignment is fenced. A blind service stop/restart is not a drain plan.

Activation needs a held schema-2 machine claim for repository
`vpsadminos-org-configuration`, selector `org.vpsadminos/int.gh-runner4`, adapter
`confctl`, with that committed configuration registered and prepared first.
Read the selected `workspace-host coordination guide`, verify this exact held
mapping, preserve the existing system/profile generation and review dry-activation
effects before the approved switch:

```sh
workspace-host coordination verify-machine \
  2026-11-03-livepatch-fixture-failures --as-is --id "$CLAIM_ID" \
  --repository vpsadminos-org-configuration \
  --selector org.vpsadminos/int.gh-runner4 --json
confctl deploy -y --generation "$NEW_GENERATION" \
  'org.vpsadminos/int.gh-runner4' dry-activate
confctl deploy -y --generation "$NEW_GENERATION" --enable-auto-rollback \
  'org.vpsadminos/int.gh-runner4' switch
confctl health-check -y 'org.vpsadminos/int.gh-runner4'
```

No reboot is required by this route. Automatic rollback guards lost connectivity;
it does not prove runner health or scheduling safety. Recovery through a retained,
verified old confctl build generation is:

```sh
confctl deploy -y --generation "$PREVIOUS_BUILD_GENERATION" \
  'org.vpsadminos/int.gh-runner4' switch
```

That generation and its old store path must be captured before activation; no
numeric offset or guessed generation is acceptable. If the old generation is
unavailable or access/activation becomes uncertain, stop and retain the machine
claim for operator recovery. Verify the selected system/profile and unit, then
restore scheduling only after readiness is established. Preserve all nine
livepatch rows and native acceptance gates. Machine release follows verified
effects and complete integrated deployed lineage; it grants no merge permission.

**Remaining prerequisites:** trusted SSH access; exact live system/profile/source
and prior recovery generation; desired evaluated system/package identities and
cache/diff receipt; a concrete approved assignment fence/drain; and separate
activation authorization/held machine ownership. These commands are preparation,
not an approved or completed deployment.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/)
