# Codex generation retention investigation and proposal

Status: investigation complete; proposal corrected for Nix runtime roots on 2026-10-28. Architect: architect0. Layout counts below are the 2026-10-27 observations.
Initial identity matched `dev-session current`, both environment variables and the trusted binding. On 2026-10-28, `current` from the session directory again matched; both environment markers were absent, so the trusted thread binding established ownership.
Scope: read-only installed state/code, canonical dev-workspace history and Nix source; no implementation, deployment or live cleanup.
The lead accepted the minimal direction below. Plan, state and portal remain lead-owned.

## Findings

`~/.local/state/dev-workspaces/codex/generations/` contains **150 numeric symlinks, 51–200**, with no dangling targets, retaining **six distinct outputs**:

| Output | Links |
| --- | ---: |
| `/nix/store/8vfvwkn3biviq6lmyj1r886fqcd5lkjn-codex-0.154.0` | 1 |
| `/nix/store/5ic3470w8g40xyzqypbdzsvz9y3251ky-codex-0.155.0` | 23 |
| `/nix/store/4mxlhqv9angcqgjw4c067nfpjlxv3d4h-codex-0.159.2` | 4 |
| `/nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0` | 61 |
| `/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0` | 60 |
| `/nix/store/5rm5bizqzrc1sjlpbdnwps2cf16dxys0-codex-package-0.164.0` | 1 |

These are 150 links, not 150 copied packages or disjoint closures. Removing 144 duplicate aliases while retaining each exact output would not release any of these outputs. Closures can share dependencies; reclaimable bytes were not measured.
`codex/current` directly selects the last output above. `nix-store --gc --print-roots` confirms all 150 numeric roots and current are registered roots; this command only listed roots.

The application already uses ordinary `nix-env` generations: `~/.local/state/dev-workspaces/profile -> profile-200-link`, with generations 140, 145, 156, 199 and 200 retained.
Its selected output is `/nix/store/5slsxiy16ifc56qkypx3l6c5ygmyy2vg-dev-workspace-0.2.0`.
Each retained application's `libexec/codex` points to its bundled output: 140/145/156/199 select `jrsm…0.163.0`; 200 selects `5rm5…0.164.0`.
Direct `nix-store --query --references` confirmed `5slsx…` references `5rm5…` and historical application `/nix/store/a335n75hnlpwfzf1bz8xkxgzvgynggd9-dev-workspace-0.2.0` references `jrsm…`.
Thus retained application generations already protect their bundled Codex closures. Four of the six Codex outputs are additional to these five application generations; other roots may also retain them, so this is not a global reclamation estimate.

## Why the custom roots exist

Historical evidence, not reconstructed intent:

- `bc4a6130ca12e35bf3eb5d5517e68982f273eec1`, authored 2026-09-08, introduced user-profile deployment and explicitly said “retains rollback pairs.” Its `libexec/workspace-host` mapped each application generation to the then-adopted Codex, used that mapping during rollback, and removed a failed generation's paired root during compensation.
- That mapping could differ from the application's bundled Codex while adoption was deferred. An independent current root therefore had a real purpose.
- `59c4ba30` (2026-09-21) removed rollback, compensation and paired discard for the forward-only team-runtime cutover. Numeric-root creation remained. Current `workspace-host rollback` still refuses.
- `40838aa2` (2026-10-02) documented complete Codex packaging and retaining dependencies of native daemon copies.
- `7ceb6b943c7fa6e6db2b42b1fc2d9732c6413e03` (2026-10-19) added application-profile collection and explicitly preserved separate Codex roots.

The surviving mapping is therefore historical rollback machinery that also retains runtimes independently of application profiles. No inspected history says standard Nix profiles were impossible; claiming that rationale would be inference.

## Actual implementation and cleanup

Deployed source is `5slsx…/libexec/.workspace-host-wrapped`: activation lines 738–743, reconciliation 2232–2238, roots 3511–3528, obsolete mapping lookup 3558–3561, rollback refusal 1191–1196.
`root_codex` runs `nix-store --realise STORE --add-root PATH --indirect`; `retain_codex_for_generation` uses the application generation number. Portal-only package updates consequently add aliases even when Codex is unchanged.
The installed `workspace-coordination-gc.rb:572–601` uses `nix-env --delete-generations` for the application profile, retaining current, its predecessor, newer generations after legacy rollback, and targets referenced by live coordinator work/recovery.
Supported inspection/application commands are `workspace-host coordination gc --dry-run --json` and `--apply --json`; neither collects `codex/generations`. No supported Codex-generation cleanup CLI was found.
The collector runs as a transient service requested after ledger changes/every five minutes; absence of a permanent timer unit is expected (`workspace-coordination-host.rb`, `dispatch_coordination_collection`).
Installed `nix-gc.service` invokes `nix-collect-garbage` without generation-deletion flags; no `nix-gc.timer` was present. GC does not reclaim rooted closures.

## Can ordinary Nix profiles work?

Yes. Future code could use `nix-env --profile PROFILE --set /nix/store/OUTPUT`, just as the application does. This selects an existing output directly; `nix profile install`, a package composition, or a package manifest is unnecessary.
Nix 2.34.9 [`opSet`](https://github.com/NixOS/nix/blob/2.34.9/src/nix/nix-env/nix-env.cc#L758) handles an opaque output, then calls `createGeneration` and `switchLink`.
[`createGeneration`](https://github.com/NixOS/nix/blob/2.34.9/src/libstore/profiles.cc#L64) reuses the latest generation when its target already matches; otherwise it creates the next `PROFILE-N-link`. It does not globally deduplicate older nonconsecutive selections.
The existing bare numeric `generations/51` links are not that layout and have no corresponding profile selector. Read-only `nix-env --list-generations` on `generations/200` returned none. A normal profile does not itself supply a safe retention policy.

## Related families and ownership

| Family / observed layout | Retention and scope |
| --- | --- |
| Workspace application `dev-workspaces/profile-N-link`: 5 roots | Standard profile, existing reference-aware application collector; already protects bundled Codex. |
| Workspace Codex `codex/current`, `codex/generations/N`: 151 roots | Custom indirect roots; numeric history has no collector. Primary subject. |
| `dev-workspaces/coordination/roots/*`: 135 roots / 46 targets | Operation/preparation/worker ownership; existing collector protects claims, unfinished work and recovery. Not general profile history. |
| `~/.local/state/nix/profiles/profile`: 5 generations, current 90 | Ordinary user's package profile; separate user ownership. `~/.nix-profile` links here. |
| Same directory's `home-manager`: generation 40 | Home Manager owns this standard profile; independent policy. |
| `/nix/var/nix/profiles/system`: 23 generations, current 262 | System deployment/recovery ownership; outside workspace collector. Root channels also retain one generation. |
| Workspace-local `*-N-link` roots: 36 / 20 targets; `/tmp`: 17 / 10; state `verification/`: 4 / 3 | Shell/build verification profiles belong to their creating operation/session. Counts are root-path inventory only; no other session records were opened. No blanket retirement inferred. |
| Confctl `.confctl/generations/...`: 881 root paths / 321 targets | Build/deployment input and output retention, not this Codex mapping; config/operation ownership. 440 `confctl-*` root directories also exist. Counts do not establish staleness. |
| `~/.codex/packages/app-server-daemon/{current,releases,selection-history}` | Native Codex owns selection and copied releases 0.163.0/0.164.0; current selects 0.164.0. Not a Nix profile. No reported GC root resides below `~/.codex`. |

Running executable-path inventory found native copied 0.164.0 and store-based 0.158.0, 0.160.0, 0.160.1 and 0.164.0 processes. Their existence does **not** require custom generation pins: the earlier proposal was overconservative on this point.
On 2026-10-28, `nix store info --json` identified the trusted daemon store running Nix 2.34.9. Read-only `nix-store --gc --print-roots` reported `/proc/156049/exe -> /nix/store/5rm5bizqzrc1sjlpbdnwps2cf16dxys0-codex-package-0.164.0`, `/proc/1687746/exe -> /nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0`, and `/proc/1780764/exe -> /nix/store/k0ddsj4gwrv6asgms0ypvqdknh8slk12-codex-package-0.160.1`. These are snapshot examples, not persistent PID identities.
Nix 2.34.9 [`local-gc.cc:62–160`](https://github.com/NixOS/nix/blob/2.34.9/src/libstore/local-gc.cc#L62) scans Linux `/proc` executable, cwd, fd, maps and environment references, reduces store subpaths to output roots, and [`gc.cc:613–633`](https://github.com/NixOS/nix/blob/2.34.9/src/libstore/gc.cc#L613) marks each root's reference closure alive. Actual root output also included `/proc/1/maps` library roots and `/proc/1/fd/18` for systemd. No raw process environment was printed.
`nix config show` reported `keep-derivations = true`, `keep-outputs = false`; neither disables ordinary reference-closure retention. Linux runtime scanning is built in here, not dependent on an added application pin policy. The observed runtime roots confirm it operates on this host.
An idle **running** process remains covered. A stopped executable selected for a future restart needs persistent selection/profile protection. Copied files outside the store are not themselves Nix roots, but their mapped/open store dependencies are runtime roots while running. Unopened future helpers or restart dependencies need their actual selected package contract accounted for; this is not a reason to retain all historical copies or Codex outputs. The earlier scan of the two copied binaries found no embedded store prefixes, but was not a complete dependency audit.
Source documentation also describes newer upstream in-store daemon selection/root attempts; it must not be substituted for inspection of these actual deployed copied runtimes.

## Recommended smallest change — future work only

Use the existing standard **application profile** as the authoritative history for bundled Codex. Stop creating a Codex root for every application generation and retire redundant numeric history. Let ordinary Nix GC protect running store executables and their closures. Preserve only selected-but-not-running/restart targets and actual pending/recovery outputs not already protected by normal profiles.
A second full Codex history profile is feasible but duplicates application retention and adds synchronization/migration work. It is optional if independent Codex history becomes a product requirement, not needed for this fix.
The existing `codex/current` root can protect independent selection. Additional pins are justified only by a concrete supported selection or pending/recovery contract outside normal profiles, not by a running process or hypothetical future reuse. Do not introduce process pinning, a liveness framework or a second history manager.

Migration must run only under later authorization, with existing package-transition exclusion and writer-generation checks. Account for current selection and actual pending/recovery targets; verify necessary persistent protection before removing numeric roots.
There is no required preserve-all-six or duplicate-only phase. Historical outputs without a supported selected/pending/recovery obligation need no replacement root. Removal of their custom roots allows ordinary Nix GC to decide whether running processes or other roots still retain them; no separate proof that old Codex processes have exited is required.
Pending JSON is evidence, not a GC root. Keep its exact required closures rooted across interrupted activation and retries; app-profile retention must not silently strand an independently selected older Codex.
Do not renumber application generations, rewrite journals, alter launch provenance or restart daemons for migration. Preserve `codex/current/bin/codex` resolution. Existing workspace recovery stays forward-only; native/system rollback has its own compatibility and ownership rules.
Older binaries may recreate numeric roots; retain compatibility on forward retry and do not mix old root writers with new collection. A failed migration must preserve required selection/pending protection, without requiring restoration of unnecessary historical roots.

## Implementation boundaries and acceptance

One bounded implementation package is sufficient: `libexec/workspace-host`, focused existing `test/workspace_host/*` coverage, and `docs/codex-package.md` / `docs/workspace-portal.md`. Remove redundant generation coupling while preserving independent runtime/transition retention. No schema, API, Codex protocol or system configuration change is required by the proposal.
A separately authorized operational package would inventory and retire legacy roots; it must not become live cleanup during implementation. Extend the existing collector/operations guide only if automatic cleanup is explicitly included later.
Quick acceptance: portal-only updates create no new Codex history roots; bundled outputs remain in application references; current selection and pending retries remain protected; running store executables rely on Nix runtime roots; interruption never removes required persistent selection protection.
Longer acceptance, if implementation is authorized: disposable package-transition/recovery coverage with concurrent collection, unchanged-Codex updates and native dependency retention. No long tests or builds were needed or run for this investigation.
Verification limits: source/history, config/store identity, root enumeration, symlink inspection, direct reference queries and process executable identities only. Root-list commands did not run a deletion sweep. No closure-size estimate, global liveness proof, migration rehearsal, tests, application code edit, Git mutation, deployment or lifecycle action.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-codex-profile-generations/

## Accepted implementation and verification brief — 2026-10-31

The user's **“Implement the plan”** authorizes the accepted plan below. This section supersedes the investigation-only status and provisional implementation boundaries above; historical findings remain evidence, not a second implementation option. Architect scope for this update is documentation only. The session identity was reverified through `dev-session current` and the trusted binding, with both environment markers absent.

### Scope and implementation packages

- **implementer0 — runtime:** work from current `dev-workspace` source (planning baseline `origin/master`/selected `6f54d0c7fdb974705c120b3c1ef5372f5897d544`, not stale bare `master` `52dcd471`). In `libexec/workspace-host`, remove both `retain_codex_for_generation` callsites, that helper and dead `generation_codex`; update their test/mock consumers. Keep `codex/current`, ordinary application profiles, pending record format, admission, restart and forward-recovery behavior. Extend `libexec/workspace-coordination-gc.rb` and its existing host entry as needed for the bounded cleanup below. Update focused existing host/collector tests and `docs/codex-package.md` / `docs/coordination-operations.md`.
- **implementer1 — downstream:** prepare the workspace composition and `vpsfree-cz-configuration` pins/checks independently; final exact pins depend on the reviewed, published runtime head. Preserve extension selection, sibling inputs and follows paths. No extension or codex-web source change is required.

There is no new Codex profile/history manager, process pinning, liveness framework, public command, persistent schema, Codex version or protocol change. Nix runtime roots protect running store executables and their reference closures. Normal application/system profiles and `codex/current` protect selected restart targets. Native copied-daemon releases and their selection remain separately owned; do not prune copies or add a copy-retention inventory.

### Collector trigger, safety and migration

Use the **existing coordinator collector**, not deletion inside switch/reconcile. It already provides profile-generation admission, package-switch exclusion, preparation/retention locking, action reporting, retries and periodic dispatch. Existing `workspace-host coordination gc --dry-run --json` previews the migration; `--apply --json` and the normal periodic sweep perform it after successful switch/reconcile leaves no pending transition.

The new action unlinks only recognized positive-numeric symlinks immediately below the ordinary `state/codex/generations` directory, with direct Nix-store output targets. Do not follow a symlinked directory, recurse, or touch unknown names/types/targets; preserve and report unknown layouts. Require a valid `codex/current` root. Preserve that root, normal profiles and every other root family. Capture and revalidate the selected profile identity and exact link target before unlinking; a changed profile/target refuses that mutation, and an already absent link is retry-safe. Remove roots only, never store contents.

Use the host's existing strict pending-record parser. Any valid pending Codex transition skips **only this legacy-root collection** with a preservation reason; malformed pending state fails closed through the existing parser. Collection resumes after ordinary recovery clears pending state. Do not invent additional pending pins: selected package/current and existing prepared-operation protection remain authoritative. This temporary skip during an actual pending operation is not a preserve-all-six or duplicate-only migration phase.

Old writers can recreate numeric roots; existing generation admission excludes them from new package operations, and subsequent sweeps remain idempotent. Keep ordinary forward retry and lifecycle/cluster compatibility gates. Removing redundant roots does not require waiting for old Codex processes to exit; ordinary Nix GC determines remaining liveness. No forced GC or daemon restart is part of root migration. System rollback retains its existing confctl contract; workspace rollback remains unavailable.

### Acceptance and verification

Quick checks use the repository Nix environment, declared hooks and focused existing `test/workspace_host/{profile_transition,agent_team_registration,live_switch,commands_and_locks}_test.rb` / `test/coordination_gc_test.rb` coverage as applicable. Verify:

- Unchanged and changed Codex switches create no numeric roots; selected current/application references remain valid and failed activation retains forward retry behavior.
- Preview makes no root changes; apply removes recognized numeric history, including roots for an older running store Codex, and repeated apply is harmless.
- Current/profile links survive; valid pending state skips only legacy cleanup, clearing it allows retry, and malformed pending state cannot permit deletion.
- Unknown layouts survive; a superseded profile or replaced target cannot be unlinked by a stale action; package-switch/preparation exclusion and concurrent session creation remain supported by existing collector tests.

Commit intended changes and pass quick checks before independent final review. After review, run applicable existing packaged Ruby/profile-transition and collection integration checks under the monitor policy, preserving exact revision/input evidence. Reuse existing coverage for creation during collection and naming failure where valid; do not invent a GC/liveness test campaign. Live acceptance verifies exact system/profile identities, matching runtime composition, portal/router/coordinator health, naming and conversation/tmux continuity, successful reported root retirement after pending settles, and unchanged current/normal profiles. Read-only Nix root output establishes continued runtime protection; no deletion sweep is required for that proof.

### Downstream, deployment and integration

Publish the reviewed runtime feature head. In the workspace feature checkout, set `inputs.vpsfree-dev-workspace.inputs.dev-workspace.url` to that exact revision and generate the lock with `nix flake update vpsfree-dev-workspace/dev-workspace`. In the configuration feature checkout use `confctl inputs channel set --commit dev-workspace devWorkspace EXACT_RUNTIME_SHA`. Inspect semantic lock diffs and run `bin/check-dev-workspace-deployment --workspace-root PATH --configuration-root PATH`. Keep one final logical pin update per consumer.

Review/check the completed downstream changes and prepare exact committed application output and `confctl build cz.vpsfree/machines/aitherdev` before claiming the machine. Under the held **`vpsfree:aitherdev`** claim, perform confctl dry activation and a no-reboot system switch; verify both `/run/current-system` and `/nix/var/nix/profiles/system`. Then run ordinary `workspace-host switch --source COMPOSED_WORKSPACE_WORKTREE`, passing the held `DEV_WORKSPACE_CLAIM_ID` and exact session identity. The application is deployed from its user profile, not by the system pin. Verify migration through the existing collector preview/apply or periodic result and the live acceptance above.

The user's conditional merge direction covers **dev-workspace, workspace and vpsfree-cz-configuration → master after verification**. Integrate runtime first, then its two consumers, with one short repository claim at a time, required hooks, fast-forward-only merge, SSH push and fresh remote ancestry proof. Shared workspace integration also takes the nonblocking tracking lock. Retain complete source/input graphs, exact deployed/final heads and any independently reviewed equivalent-history mapping in existing rollout/review receipts; substantive replacement needs a verified redeployment. Release the physical-machine claim promptly after verified effects and integrated deployed lineage, checking authoritative state before and after release. No separate UI wait or session lifecycle action follows from completion.

There are no remaining product decisions in this brief. Material deviations return through the lead; plan/state/portal and rollout coordination remain lead-owned.
