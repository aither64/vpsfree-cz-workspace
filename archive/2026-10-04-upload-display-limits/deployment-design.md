# Upload limits: deployment and integration brief

Prepared by architect0 (retained GPT-6 Astra / xhigh). Commands below are for the
coordinating lead/operator; none were executed for this brief. This assignment
writes only this file. The latest lead instruction records authorization to
deploy aitherdev through vpsfree-cz-configuration and then integrate the affected
default branches. State/plan/portal updates and execution belong to that lead.

## Exact scope and dependency selection

| Component | Before | Required after |
| --- | --- | --- |
| codex-web/master | `32775fa7fdd9bc9b41aef74b7f195e5c3bc0f8d5` | Reviewed `3d07cf60cfde5d117a181a9bdb6d90a5860f6f0c` |
| dev-workspace/master | `6a972b9ab01077611b2c60e0fc726c185e050315` | Reviewed `3edc605d81a30a4d49560426e0128b388b856493`, already pinning the provider above |
| Consuming workspace | Base `e5ba1912b74e0bad6d47a61b629100931aa53e52`; nested runtime `6a972b9` | One explicit nested-runtime override plus its generated lock change |
| Configuration | Base `9c5fafb9df6bb33d635e7eb8f1f2638dfb1cbfe4`; `devWorkspace` at `924c0ec28c41dd8b56aaf17f2212b302ca614899` | Channel `dev-workspace`, role/input `devWorkspace`, at `3edc605` |
| vpsFree extension | Root-selected `cd81e83f91a552eb0138e58cb76312784a2988df` | **Exactly unchanged; no extension branch, commit or integration** |

The extension's cached origin/master is only
`e1bb5cf3ad37c5ef31445a68ab85f53db2858777`. The selected `cd81e83` contains
another initiative's unmerged storage-profile changes (four files, including
acceptance code). Replacing it with master would remove installed behavior;
carrying it into master would integrate someone else's work. Preserve its exact
revision and override only its runtime in the consuming workspace `flake.nix`:

```nix
inputs.vpsfree-dev-workspace.inputs.dev-workspace.url =
  "github:aither64/dev-workspace/3edc605d81a30a4d49560426e0128b388b856493";
```

Keep the existing extension URL, site configuration, team configuration,
provider catalog and other inputs. Generate the lock with Nix; inspect the
resolved graph for extension `cd81e83`, runtime `3edc605`, provider `3d07cf6`.
No extension repository is affected by this rollout. The override deliberately
fixes runtime selection at the consumer; later extension updates must account
for that explicit override rather than assuming their runtime pin takes effect.

## Host/application contract and drift

The system configuration imports `devWorkspace.nixosModules.host` and uses its
`lib.mkCodexPackage` for system Codex. It owns nginx, TLS/authentication and the
host socket/group setup. The complete user application comes from the consuming
workspace's `packages.x86_64-linux.default`, which composes the generic runtime,
the preserved extension, site settings and retained team policy. Installing
the generic runtime or extension directly would omit the required composition.

`bin/check-dev-workspace-deployment` must pass using the two feature worktrees.
It compares root `.dev-workspace.json` with aitherdev's site hostname, aliases
and wildcard, and compares exact GitHub runtime identities selected by
`vpsfree-dev-workspace/dev-workspace` and `devWorkspace`. It does not prove a
build, live deployment, provider compatibility or session idleness.

Inspected `924c0ec..3edc605`: host module, host paths and Codex assembly helper
(`nix/host-module.nix`, `nix/host-paths.nix`, `nix/codex-package.nix`) are
unchanged. Generic flake lock drift is the codex-web input; generic nixpkgs and
llm-agents pins do not change in that range. The flake also adds model-catalog
plumbing for the application, not the host module. The broader runtime history
includes preparation/naming and maintenance-aware cluster policy already present
in application base `6a972b9`. Do not treat the old *host input* as proof that
the installed application predates those changes.

The live read-only snapshot during design was:

- Application: `/nix/store/s7y4bgq7iw0idkv5japb538kfwphk4nf-dev-workspace-0.2.0`.
- Active Codex: `/nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0`.
- System: `/nix/store/4wa4aiamhn1cm63j7gsaiqdqfn0f9ign-nixos-system-aitherdev-26.05.20261001.4feb8eb`.

Refresh these observations before execution. A narrow source diff does not
prove a narrow change from the currently running system closure. Inspect the
build and dry-activation service/package delta; investigate unrelated changes,
unexpected kernel builds or required reboot rather than silently folding them
into this upload rollout. Preserve CA/password/TLS state, host identity,
firewall, provider state and all generation roots. No namespace migration is
planned.

## Preparation and review gate

Use only the initiative worktrees. The lead has created configuration/workspace
worktrees; configuration post-checkout encountered missing Overcommit gems.
Restore the declared `nix develop` environment and hooks before generated
commits. Do not bypass hooks or recreate an already-created worktree.

The expected additional commits are one consuming-workspace dependency override
and one confctl-generated configuration pin commit. Recommend the
mandatory-change-review skill's **mechanical dependency-only exemption** if the
final diffs contain only those input selections and their necessary generated
lock entries. The unchanged application/provider heads already passed final
review. This planning artifact does not trigger another review. Record the
exemption rationale and inspect full base-to-head diffs/history anyway.

Do not extend the exemption to new host/module logic, provider changes,
lifecycle workarounds or unreviewed application code. If those become necessary,
refer the scope change through the lead and use final review at High risk with
general, architecture, scope and risk/compatibility lanes before long checks.
No extension history is to be integrated. There are no new migrations.

## Prepared operator sequence

These shell variables describe the established worktree layout. Resolve final
heads and store outputs into the rollout record before activation.

```sh
deploy_slug=2026-10-04-upload-display-limits
deploy_root=/home/aither/workspace/ai/vpsfree.cz
deploy_workspace="$deploy_root/worktrees/$deploy_slug/workspace"
deploy_configuration="$deploy_root/worktrees/$deploy_slug/vpsfree-cz-configuration"
deploy_host=cz.vpsfree/machines/aitherdev
deploy_runtime=3edc605d81a30a4d49560426e0128b388b856493
```

1. **Prepare exact pins and commit.** Fetch/compare the affected refs under the
   normal Git procedure; preserve the reviewed application/provider heads when
   no upstream drift requires rebasing. Add the override above in the workspace
   feature tree, then refresh that input's lock. The configuration channel owns
   its pin; retain confctl's generated commit history/message:

   ```sh
   cd "$deploy_workspace"
   nix flake lock
   git diff -- flake.nix flake.lock

   cd "$deploy_configuration"
   nix develop --command confctl inputs channel ls
   nix develop --command confctl inputs channel set --commit \
     dev-workspace devWorkspace "$deploy_runtime"
   ```

   `nix flake lock` reconciles the changed explicit URL while retaining unrelated
   locks; do not run an unrestricted update. Reject unexpected lock movement.
   Commit only owned workspace pin files using its normal hook/message procedure.
   Confirm config still changes only `devWorkspace` and its expected transitive
   provider lock. Capture the four exact final feature heads, diff inventories
   and comparison records before deployment/integration.

2. **Validate and build both outputs before switching either.** Run the deployment
   contract against committed sources, inspect package metadata/provider catalog,
   and run relevant workspace/extension composition checks. Long checks/builds
   belong to a fresh installed-policy verification watcher; it does not deploy.
   Previously passed generic runtime/provider checks remain valid for unchanged
   heads; the new consuming package and host configuration still require builds.

   ```sh
   nix develop "$deploy_configuration" --command ruby \
     "$deploy_workspace/bin/check-dev-workspace-deployment" \
     --workspace-root "$deploy_workspace" \
     --configuration-root "$deploy_configuration"
   nix build --no-link --print-out-paths "$deploy_workspace#default"
   cd "$deploy_configuration"
   nix develop --command confctl build "$deploy_host"
   ```

   Record candidate application output and confctl's exact built generation.
   Source commits, lock graph and generated output must stay fixed through
   deployment. Any subsequent source/head change invalidates that association.

3. **Dry-activate, inspect, then switch the host.** Use the same configuration
   worktree and built host generation, keeping prompts/health checks enabled:

   ```sh
   nix develop --command confctl deploy "$deploy_host" dry-activate
   # Inspect the complete dry-activation delta before the next command.
   nix develop --command confctl deploy "$deploy_host" switch
   ```

   Verify confctl completion, active `/run/current-system`, nginx and portal
   endpoint access before changing the user package. Do not deploy other hosts,
   rotate credentials, register a replacement workspace or change system inputs
   merely to install the portal. If the host result is uncertain, establish the
   active generation before another activation attempt.

4. **Switch the consuming user package when threads are idle.** Refresh
   `workspace-host status`, selected profile link, source HEADs and trusted
   session identity. The switch's exclusive transition lock and current-generation
   guard remain authoritative. It refuses unfinished archive/removal/revive,
   creation/fork/start/team-migration operations; proves runtime-authority
   compatibility; checks each retained cluster's schema, policy, tracking limit
   and provider adoption; validates Codex and registration semantics; then
   quiesces native clients and requires idle root/member threads before selecting
   the profile. Activation repeats critical checks.

   Cluster expectations are schema 1, transition policy 3 and tracking limit
   8,388,608 bytes, with explicit recorded socket identity. Preserve retained
   disks/maintenance receipts and the extension's providers. Let the supported
   switch perform its checks; do not invoke private adoption/lifecycle helpers,
   infer missing ownership or reset a cluster to get past a refusal. An unrelated
   session/journal blocker goes back to its owner; this deployment does not
   authorize archiving, deleting, stopping or recovering that session.

   The coordinator's own active turn also blocks quiescence. Let it and other
   member turns finish naturally. A detached launcher may wait on read-only
   `workspace-portal thread require-idle` for the verified thread/socket/cwd and
   `workspace-portal team require-idle` for this retained roster, then execute
   the switch once. The switch still checks all registered sessions and may
   refuse another busy session. Do not loop the mutating switch, interrupt turns
   or suppress its idle check. The lead must yield its turn for this gate to pass.

   The authorized switch command is:

   ```sh
   /home/aither/bin/workspace-host switch --source "$deploy_workspace"
   ```

   Launch the lead-prepared guarded script through a named transient user unit,
   not `nohup ... &`; command-tool cleanup can kill the latter before it logs.
   The script must verify the expected predecessor profile and source heads,
   verify the bound session, wait for natural idleness as above, preserve full
   output and atomically publish the switch exit status. Example launcher shape:

   ```sh
   systemd-run --user --unit=upload-display-limits-switch-20261004-1 \
     --property=Type=exec \
     --setenv=PATH=/home/aither/bin:/run/current-system/sw/bin \
     --setenv=DEV_SESSION_SLUG=2026-10-04-upload-display-limits \
     --setenv=DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
     /run/current-system/sw/bin/bash \
     "$deploy_root/work/$deploy_slug/switch-once.sh"
   ```

   This script is to be prepared by the lead; it is not supplied or launched by
   this brief. A fresh utility watcher observes that existing unit/log/status
   file and does not launch, retry or approve deployment. Check `Result` and
   `ExecMainStatus` with `systemctl --user show`, alongside actual profile and
   service state; a missing status file proves neither success nor failure.

5. **Verify the actual deployment, then integrate.** Require selected application
   output equal to the built candidate and healthy `workspace-router.service`,
   `workspace-portal@vpsfree-cz.service` and `workspace-codex@vpsfree-cz.service`.
   Compare retained root/member thread IDs, roster settings, tmux session
   identities, workspace registration and cluster ownership with pre-switch
   evidence. Successful terminal quiescence/restoration may change client PIDs;
   it must not replace sessions or conversations. Retain all package/Codex roots.

   Read-only commands include:

   ```sh
   /home/aither/bin/workspace-host status
   readlink -f /run/current-system
   systemctl --user show workspace-router.service \
     workspace-portal@vpsfree-cz.service workspace-codex@vpsfree-cz.service \
     -p ActiveState -p SubState -p ExecMainStatus
   ```

## Browser acceptance without creating production work

Compare deployed static JS/CSS responses and cache-version URLs to the exact
candidate/reviewed sources. Check authenticated access and TLS using the normal
browser or secret-safe existing credential mechanism; never put passwords in
argv, logs, notes or artifact URLs. Do not disable TLS verification to claim
successful deployment.

Use the existing Chromium `test/creation_browser.cjs` local HTTP fixture with
the reviewed runtime and provider, or a loopback fixture serving captured exact
deployed assets. Require the browser prerequisites documented in `test/README.md`.
Use isolated browser storage and synthetic endpoints/files. Verify 50 selections,
full byte summary/completion count, rejected file 51, reload/recovery, desktop
1280px and narrow 375px creation layout, reachable actions and unchanged 12rem
conversation cap. Match asset hashes to the deployed candidate so the evidence
does not accidentally exercise a stale worktree or cached script.

Do not point that fixture at the production API. Opening the live New session
page runs code that POSTs a draft scope, and `GET /uploads/s-<slug>` can initialize
or adopt a scope. Therefore neither is a strictly read-only upload probe. If
using a browser to inspect production markup, disable page scripts or intercept
all application requests and allow only the intended static reads. Existing
backend 50-file tests plus proven deployed package identity establish server
limit provenance without creating a real session, sending prompts, uploading
real files or deleting synthetic production state.

## Recovery and integration completion

Before profile selection, a refused switch leaves the predecessor selected and
restores any quiesced terminal clients. After the candidate profile is selected,
recovery is **forward-only**: preserve pending state, determine the selected
profile and unit outcome, then retry the same supported switch or deploy a
corrected newer package. Do not call `workspace-host rollback`, select an older
profile manually or remove journals. `--from-candidate` is only the documented
recovery entry for a selected command unable to parse valid persisted state;
it is not part of this normal rollout or a bypass for busy sessions.

Old readers still reject unfinished >10-attachment preparations. Normal
completion/terminal compaction is a data-compatibility prerequisite, not
permission to downgrade. Preserve browser drafts and unresolved uploads for
the compatible reader. Host recovery is separate: a retained known-compatible
system generation may repair host substrate failure, but must not be used to
roll back the application, lose deployment SSH access or change credential/state
contracts without checking them first.

After deployment acceptance, integrate in dependency order:
**codex-web/master → dev-workspace/master → configuration/master → workspace/master**.
The final two pins are independent once their dependencies are published; this
order leaves the consuming workspace last. Fetch and check fast-forward ancestry
immediately before each integration. Use fresh temporary target worktrees for
the three independent projects; integrate the workspace feature with
`git merge --ff-only` from the shared root master, preserving its existing
tracking/index changes. Root origin was behind local master when assigned;
account for that existing series rather than resetting or force-pushing it.

Before each merge, save `dev-session worktree capture-comparison
2026-10-04-upload-display-limits <repository> --as-is` at the exact final head
for `codex-web`, `dev-workspace`, `vpsfree-cz-configuration` and `workspace`.
If a rebase changes a head, prove patch equivalence, refresh dependent pins and
relevant checks, and recapture comparisons. Do not claim a changed package was
deployed merely because an equivalent branch was merged; record source and
output correspondence. Capture remote master ancestry after pushes and retain
feature refs. The extension's master and `cd81e83` pin remain untouched.

Expected final result: host and consuming application resolve the same runtime
`3edc605`/provider `3d07cf6`, deployed assets show the reviewed 50-file behavior,
existing sessions/clusters remain intact, and the four exact final heads are
integrated. Session lifecycle/archival remains outside this authorization.
