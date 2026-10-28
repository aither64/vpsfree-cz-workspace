# Observer guidance rollout

## Authorization and status

User authorized implementation/aitherdev deployment, later approved all three
master integrations with "ok, merge it", and explicitly requested aitherdev
release. Status: deployment verified, all approved final heads integrated and
machine claim released/independently queried as released. Session remains open.

## Machine and source identity

- Physical machine: `cz.vpsfree/machines/aitherdev`.
- Coordination alias: `vpsfree:aitherdev`.
- Workspace: `/home/aither/workspace/ai/vpsfree.cz`.
- Session: `2026-10-28-observer-progress-guidance`.
- Generic runtime: `git@github.com:aither64/dev-workspace.git`, target `master`.
- Site composition: `git@github.com:aither64/vpsfree-cz-workspace.git`, target
  `master`; application is selected from the workspace user profile.
- Host configuration: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`,
  target `master`; role `dev-workspace/devWorkspace` maps to input `devWorkspace`.
- Feature refs in each repository: `2026-10-28-observer-progress-guidance`.

## Predecessor observations

Read before candidate build/activation:

- `/run/current-system` and `/nix/var/nix/profiles/system` both resolve to
  `/nix/store/p1398b7pajwlp4hjq8mqd5j98gk6l1ac-nixos-system-aitherdev-26.05.20261026.718f670`.
- `workspace-host status` selects
  `/nix/store/pq2jwjcv4hbyiwzcam50x6j9fv008qiq-dev-workspace-0.2.0`.
- Selected package catalog digest:
  `3ff7a2129ed39b4d6774466e53060bbff33d2cd2d893aa168c87cb3d64bd6b41`.
- Workspace locked extension:
  `767dfd587e346168e1443e65ccdb67ce748f3fe3`; nested generic runtime:
  `d5d2b39b13a6875a26b218ffaf7b589b9d71a1fb`.
- Direct local portal `GET /healthz` over its configured Unix socket returned
  `{"ok":true}`. Router unit was active, PID 629074. Native app-server socket
  target inode was 18745722 (mtime 1793106868); retain as continuity baseline.
- Exact user units confirmed loaded/active/running: portal
  `workspace-portal@vpsfree-cz.service` PID629079, router
  `workspace-router.service` PID629074, coordinator
  `workspace-coordinator.service` PID629105 and native
  `workspace-codex@vpsfree-cz.service` PID3555077.
- Router health with the exact workspace Host returned ok. Read-only same-session
  `/api/sessions/2026-10-28-observer-progress-guidance/thread` returned root
  `01a181a7-2ddc-7852-a8c7-56c27709c461`, active. No transcript contents copied.
- Naming has no supported read-only inference health endpoint. It is a private
  child boundary, not its own unit; the pre-deployment socket enumeration found
  no naming socket. Static portal health does not prove naming inference. Preserve
  this baseline and distinguish packaged fixture/unchanged-contract evidence from
  live naming output; do not create or rename a live session for this rollout.

These are observations, not a guarantee that shared defaults or selections will
remain unchanged. Recheck the selected generation and machine status before
activation. The installed coordination guide governs retention and release.

## Candidate, verification and activation

All source committed/published, quick checks and no-finding final review passed.
Runtime packaged check passed in 656 seconds; composed workspace default plus
three catalog/instruction/deployment checks passed in 664 seconds. Exact-head
GitHub CI40660885906 passed (creation/fast/archive; host skipped).

The first host-build command omitted --yes and stopped at EOF before building
or activation. Corrected command `nix develop --command confctl build --yes
cz.vpsfree/machines/aitherdev` passed in117 seconds at config
`4715580512a4042bea75cb44167efb42b3618f70`; log
`/tmp/observer-progress-aitherdev-build-yes.log`. No source change or repeated
successful package checks were required.

Prepared generation: `2026-10-28--10-45-33`; retained metadata:
`worktrees/2026-10-28-observer-progress-guidance/vpsfree-cz-configuration/.confctl/generations/cz.vpsfree:machines:aitherdev/2026-10-28--10-45-33/generation.json`.
System toplevel:
`/nix/store/lg62jfx2ym8vyiviwwwa924crnivqk0f-nixos-system-aitherdev-26.05.20261026.718f670`.
Configured auto-rollback output:
`/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb`.
Application candidate:
`/nix/store/pjmi2cz75r9cwynh4lin706jdzlp4xb9-dev-workspace-0.2.0`.

Generation's effective host inputs and sources:

| Input | Revision | Store source |
| --- | --- | --- |
| devWorkspace | 4a002f52c3b55099540aa99708d5fcf29f7b2456 | /nix/store/ixq3yxn5fhy2nag60myidy616a9p25vb-source |
| home-manager | c47b2cc64a629f8e075de52e4742de688f930dc6 | /nix/store/qh7n70gsg3rmvyn5zi1x1vhnwbrnm5wx-source |
| llm-agents | ea188d2f072e0ec8d5b71245e228803672801a22 | /nix/store/dyw4sx7rn0bhj9kyb3s1r58vsmh9vwj8-source |
| nixpkgs (nixpkgsStable) | 718f670e845328e9c2cecdd832835712b2cbd065 | /nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source |

The matching input/toplevel/auto_rollback symlinks remain in the generation
directory. Complete lock graphs and package derivation/output roots are below.
Build/copy is outside machine ownership. Hold the exact claim for activation
and effect verification. Do not reboot.

Copy preparation passed: `nix develop --command confctl deploy --copy-only
--generation 2026-10-28--10-45-33 --yes cz.vpsfree/machines/aitherdev switch`,
exit0 before ownership. Selection and both predecessor system paths remained
unchanged before acquisition.

Machine claim `0fe3d47f-e906-4d9d-ba9f-eab117b0f58e` acquired held at
2026-10-28T09:48:46Z; exact owner `0b362121-f6e1-4a1e-ab67-715f964c6a06`,
resource `machine:vpsfree:aitherdev`, no repository resource. Fresh authoritative
status checked before activation. Root launched the ordinary confctl driver in
user unit `observer-progress-system-0fe3d47f.service`; verification utility only
observes that unit/log. Command selects exact G with --yes --dry-activate-first
--no-reboot and leaves auto-rollback/health checks enabled. System driver completed
active/exited, Result=success, ExecMainStatus=0 in about37 seconds (09:49:32Z to
09:50:09Z). Full journal `/tmp/observer-progress-system-activation.log`; status
`/tmp/observer-progress-system-activation.status`. Journal reports trying
activation, switch and two passing health checks. Lead verified both
`/run/current-system` and `/nix/var/nix/profiles/system` equal the exact built
toplevel above, and `systemctl is-system-running` returned running.

After system verification, root launched ordinary `/home/aither/bin/workspace-host
switch --source WORKSPACE_FEATURE_WORKTREE` once in
`observer-progress-profile-0fe3d47f.service`, passing exact session/claim identity.
Fresh monitor could not finish its `dev-session current` check during the active
profile transition (20-second timeout), so it did not inspect the unit. Lead used
the monitor skill's visible parent fallback against the existing unit only,
without retrying the driver. CLI availability recovered after completion;
`dev-session current` and both markers again matched the exact binding. No
application edit or daemon-forcing workaround was needed.

Profile unit completed active/exited, Result=success, ExecMainStatus=0 at
09:53:12Z (started09:51:29Z). Full journal
`/tmp/observer-progress-profile-activation.log`; terminal status
`/tmp/observer-progress-profile-activation.status`. Ordinary selection reported
exact expected package `/nix/store/pjmi2cz75r9cwynh4lin706jdzlp4xb9-dev-workspace-0.2.0`.
Protocol and local semantic observation contracts passed during normal switch.
Both activation units are terminal with MainPID=0 and exit0; no unfinished
driver effects remain.

Post-selection lead acceptance:

- Selected profile exactly equals the built application candidate; both system
  paths still equal the built toplevel. Full reviewed source/input graphs and
  output roots are retained in this receipt.
- Portal/router/coordinator loaded and active/running (PIDs884838/884300/884851).
  Native Codex stays at PID3555077, socket inode18745722/device64769, matching
  predecessor. Same root thread01a181a7-2ddc-7852-a8c7-56c27709c461 reads active;
  ordinary ongoing communication continues. Router and direct portal health ok.
- Installed catalog digest
  495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7. Observer
  stock is1798 bytes/hash c7593c1d8dc796b2ae1abed89c56b55232e7b26db7ac309331e616f853aceb82,
  matching reviewed source. Maximum role instructions4063/4096. Utility policy
  remains Luna/low/full_access/never.
- A naturally scheduled same-session check completed at09:53:54Z with observer
  available, no warning/concern or unavailable error. Its stock instructions
  refreshed to the reviewed hash on the same thread
  01a181a7-4262-7561-ba40-459c6ae9b979, retaining Sol/xhigh/read_only. No manual
  roster reconfiguration or synthetic inference/session was used. This proves
  installation/refresh/check transport, not a measured false-positive rate.
- Naming socket filesystem entries appeared after selection but no listening
  naming socket matched the exact workspace prefix. No supported read-only
  end-to-end naming probe exists. Preserve the earlier limit: static health and
  fixture/contract checks do not prove future naming model output. No naming
  source, provider or native version changed; no new naming failure is attributed
  to this rollout and no live session was created/renamed for evidence.

Machine claim remains held; integration has no approval.

## Recovery and release

Preserve confctl auto-rollback and generation metadata. Verify both live system
and published system profile after activation. Preserve workspace package roots
and ordinary forward-recovery journals; do not force daemon restart, roll back
the workspace or reset state. Any unfinished or uncertain mutation retains the
machine claim until reconciled.

After separately approved integration, record fresh remote ancestry proof for
the complete deployed source lineage, inspect authoritative status for this
session's exact claim, release and verify the released state. No background or
session lifecycle action is authorized by rollout completion.

Release completed at2026-10-28T10:23:18Z after fresh deployed-lineage/effect proof.
Normal owner release returned machine claim0fe3d47f-e906-4d9d-ba9f-eab117b0f58e
revision2/state released; separate authoritative claim-status query confirmed
the same owner/resource/released state. No repository claim remains held. No
unfinished activation or Git commands remain. Later deployment requires fresh
machine ownership. No archive/delete/stop/finalize/cleanup command was invoked.

## Final candidate source and complete input graphs
Committed source heads before review/build: runtime `4a002f52c3b55099540aa99708d5fcf29f7b2456`; workspace `f10e7e530e1dba252e11d587667c3051118ee206`; configuration `4715580512a4042bea75cb44167efb42b3618f70`. All feature worktrees were clean. These graphs bind the candidate inputs; build output identities and final activation proof follow separately.

### workspace
Complete committed lock: `f10e7e530e1dba252e11d587667c3051118ee206:flake.lock`; Git blob `a4edc3dc07e09591138ef76f997bad9ea1cf04b3`; SHA-256 `83a02a292b812773d0fdaa2992570751e0f2e93623bb3b2626bee5e93febd402`. Root node `root`.
| Node | Locked identity | Input edges (arrays are follows paths) |
| --- | --- | --- |
| `bun2nix` | `{"lastModified":1790001035,"narHash":"sha256-1/SLBjSYBzDdDhvLQ83wrzBakyS/xNGgtxHGNuveOEQ=","owner":"Mic92","repo":"bun2nix","rev":"07a5bfc8ac36c5370199343fa620b69f63186e33","type":"github"}` | `{"flake-parts":["vpsfree-dev-workspace","dev-workspace","llm-agents","flake-parts"],"nixpkgs":["vpsfree-dev-workspace","dev-workspace","llm-agents","nixpkgs"],"systems":["vpsfree-dev-workspace","dev-workspace","llm-agents","systems"],"treefmt-nix":["vpsfree-dev-workspace","dev-workspace","llm-agents","treefmt-nix"]}` |
| `codex-web` | `{"lastModified":1793126110,"narHash":"sha256-ud0d214cykppfBEGo6lmyW1Z1g75R6Q2SbgpwIeTM2I=","owner":"aither64","repo":"codex-web","rev":"58300182763a01de7248ddf7c6cb9a4f0c6216cb","type":"github"}` | `{}` |
| `dev-workspace` | `{"lastModified":1793178004,"narHash":"sha256-dYrIZBVInRfXYg3p0BjMxqgTQ8saZnd7eEn0Hcq7wNI=","owner":"aither64","repo":"dev-workspace","rev":"4a002f52c3b55099540aa99708d5fcf29f7b2456","type":"github"}` | `{"codex-web":"codex-web","llm-agents":"llm-agents","nixpkgs":"nixpkgs_2"}` |
| `devcluster-vpsadmin` | `{"lastModified":1790686487,"narHash":"sha256-R8Fi7PyyMGsdx8804NLNng/RWkJ1Io9si43N9ClUm18=","owner":"vpsfreecz","repo":"vpsadmin","rev":"5c76e3290481b297dcd0baa76d246133f0353d8f","type":"github"}` | `{"nixpkgs":["vpsfree-dev-workspace","devcluster-vpsadmin","vpsadminos","nixpkgs"],"vpsadminos":["vpsfree-dev-workspace","devcluster-vpsadminos"]}` |
| `devcluster-vpsadminWebui` | `{"lastModified":1790685797,"narHash":"sha256-/lP+kojPzRPQiiBbuHZB6zNG86+1TySxWmHOBS7hWgo=","owner":"vpsfreecz","repo":"vpsadmin-webui","rev":"534caa83a5f97d2b40b4a126886649b14dc9e8d3","type":"github"}` | `{"nixpkgs":["vpsfree-dev-workspace","devcluster-vpsadminos","nixpkgs"],"vpsadmin":["vpsfree-dev-workspace","devcluster-vpsadmin"]}` |
| `devcluster-vpsadminos` | `{"lastModified":1789205372,"narHash":"sha256-fbKoi1+fQOAduD7cE1gnYtPQfoqK6VnbThnoDIOmlrw=","owner":"vpsfreecz","repo":"vpsadminos","rev":"15802517e2d92dda4ddc07ebac3d1d7ea087b430","type":"github"}` | `{"impermanence":"impermanence","netlinkrb":"netlinkrb","nixpkgs":"nixpkgs_4","nixpkgsUnstable":"nixpkgsUnstable","ruby-lxc":"ruby-lxc"}` |
| `devcluster-vpsf-status` | `{"lastModified":1788260265,"narHash":"sha256-4iun0P87K5kKG2vYi6Beio/1iWlHmNYFjD8Hlg2qGgk=","owner":"vpsfreecz","repo":"vpsf-status","rev":"587cd65bb02e6dddea7f6b6409e42a15f36ab4fb","type":"github"}` | `{"nixpkgs":["vpsfree-dev-workspace","devcluster-vpsadminos","nixpkgs"],"vpsadmin":["vpsfree-dev-workspace","devcluster-vpsadmin"],"vpsadminos":["vpsfree-dev-workspace","devcluster-vpsadminos"]}` |
| `flake-parts` | `{"lastModified":1790898470,"narHash":"sha256-zTwuwezD0w3hpga6a6P8emidzAZFyWqlNeRBlpWOOl8=","owner":"hercules-ci","repo":"flake-parts","rev":"024633cd702b10285db5cb19b40ad48d2399ba60","type":"github"}` | `{"nixpkgs-lib":["vpsfree-dev-workspace","dev-workspace","llm-agents","nixpkgs"]}` |
| `home-manager` | `{"lastModified":1768598210,"narHash":"sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=","owner":"nix-community","repo":"home-manager","rev":"c47b2cc64a629f8e075de52e4742de688f930dc6","type":"github"}` | `{"nixpkgs":["vpsfree-dev-workspace","devcluster-vpsadminos","impermanence","nixpkgs"]}` |
| `home-manager_2` | `{"lastModified":1768598210,"narHash":"sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=","owner":"nix-community","repo":"home-manager","rev":"c47b2cc64a629f8e075de52e4742de688f930dc6","type":"github"}` | `{"nixpkgs":["vpsfree-dev-workspace","kb-runtime","vpsadmin","vpsadminos","impermanence","nixpkgs"]}` |
| `impermanence` | `{"lastModified":1769548169,"narHash":"sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y=","owner":"nix-community","repo":"impermanence","rev":"7b1d382faf603b6d264f58627330f9faa5cba149","type":"github"}` | `{"home-manager":"home-manager","nixpkgs":"nixpkgs_3"}` |
| `impermanence_2` | `{"lastModified":1769548169,"narHash":"sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y=","owner":"nix-community","repo":"impermanence","rev":"7b1d382faf603b6d264f58627330f9faa5cba149","type":"github"}` | `{"home-manager":"home-manager_2","nixpkgs":"nixpkgs_5"}` |
| `kb-runtime` | `{"lastModified":1791888937,"narHash":"sha256-qofeqqWiqmPgY54qW7objZAq8iwDmLzLbzBTSYs0xLs=","owner":"vpsfreecz","repo":"vpsfree-kb-contracts","rev":"ce2c8cd9358c3636e5d39343e595df813a0b197f","type":"github"}` | `{"nixpkgs":["vpsfree-dev-workspace","kb-runtime","vpsadminos","nixpkgs"],"toolsNixpkgs":"toolsNixpkgs","vpsadmin":"vpsadmin","vpsadminos":["vpsfree-dev-workspace","kb-runtime","vpsadmin","vpsadminos"],"vpsfStatus":"vpsfStatus"}` |
| `llm-agents` | `{"lastModified":1792920017,"narHash":"sha256-a4mZGtaldWR0DIsFbLgj9DI/5lVGbKDgQ6tbb2vWPfo=","owner":"numtide","repo":"llm-agents.nix","rev":"ea188d2f072e0ec8d5b71245e228803672801a22","type":"github"}` | `{"bun2nix":"bun2nix","flake-parts":"flake-parts","nixpkgs":"nixpkgs","systems":"systems","treefmt-nix":"treefmt-nix"}` |
| `netlinkrb` | `{"lastModified":1562850306,"narHash":"sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=","owner":"vpsfreecz","repo":"netlinkrb","rev":"d9de53d843d2586ffa5b7b404887fa801c697ddf","type":"github"}` | `{}` |
| `netlinkrb_2` | `{"lastModified":1562850306,"narHash":"sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=","owner":"vpsfreecz","repo":"netlinkrb","rev":"d9de53d843d2586ffa5b7b404887fa801c697ddf","type":"github"}` | `{}` |
| `nixpkgs` | `{"lastModified":1792116957,"narHash":"sha256-EjZqHKObBfIOeHZnMRVV87HB3pPq/WBkmRJWyFxmZu8=","owner":"NixOS","repo":"nixpkgs","rev":"f20cd90e28fe0403873f473b29e42662cd86e8c4","type":"github"}` | `{}` |
| `nixpkgsUnstable` | `{"lastModified":1789006805,"narHash":"sha256-xB8mKMOx1IA9vTDNLmJZ6n4wCMq/cuWBBOzGCRnqxrU=","owner":"NixOS","repo":"nixpkgs","rev":"8ce4ef6cb6f871616146b9fe26d2a5ae594e94fe","type":"github"}` | `{}` |
| `nixpkgsUnstable_2` | `{"lastModified":1788179007,"narHash":"sha256-hn1oU2rue2SYK8dAr8+WNZWtbsz1S2W5mnHlSEuh3bo=","owner":"NixOS","repo":"nixpkgs","rev":"34ab99075ac4f7e40cf037eef32cb1c360bb85e9","type":"github"}` | `{}` |
| `nixpkgs_2` | `{"lastModified":1788405554,"narHash":"sha256-r2f1oUwixlgq9zOdYLqJLfS/lWBT60/IITjhTKI59JU=","owner":"NixOS","repo":"nixpkgs","rev":"a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4","type":"github"}` | `{}` |
| `nixpkgs_3` | `{"lastModified":1768564909,"narHash":"sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=","owner":"nixos","repo":"nixpkgs","rev":"e4bae1bd10c9c57b2cf517953ab70060a828ee6f","type":"github"}` | `{}` |
| `nixpkgs_4` | `{"lastModified":1789114715,"narHash":"sha256-ugpsyk3NM2s87vXfUiIIiibbJ4Pp0JPS5p/3mfs+q+c=","owner":"NixOS","repo":"nixpkgs","rev":"21a67dc470149f337cecafbe965d8d252a390518","type":"github"}` | `{}` |
| `nixpkgs_5` | `{"lastModified":1768564909,"narHash":"sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=","owner":"nixos","repo":"nixpkgs","rev":"e4bae1bd10c9c57b2cf517953ab70060a828ee6f","type":"github"}` | `{}` |
| `nixpkgs_6` | `{"lastModified":1788187754,"narHash":"sha256-bu1QxmXKmPuvBLN7bHP355OV9Qo13x9WCiRDH62CqRM=","owner":"NixOS","repo":"nixpkgs","rev":"5dfba6236110080a54247d6460bc2ff5dda939cc","type":"github"}` | `{}` |
| `nixpkgs_7` | `{"lastModified":1789009968,"narHash":"sha256-GB16oaxpsrnGNnGIE+0uYBqMRzB9X6FYDUvjvnJAYew=","owner":"NixOS","repo":"nixpkgs","rev":"d58a46e3bc02d91ebe04667f8397752a749c0024","type":"github"}` | `{}` |
| `root` | `{}` | `{"nixpkgs":["vpsfree-dev-workspace","nixpkgs"],"vpsfree-dev-workspace":"vpsfree-dev-workspace"}` |
| `ruby-lxc` | `{"lastModified":1780499941,"narHash":"sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=","owner":"vpsfreecz","repo":"ruby-lxc","rev":"004bf35eb90d41ba60b347b5b1e73d868a4f95d9","type":"github"}` | `{}` |
| `ruby-lxc_2` | `{"lastModified":1780499941,"narHash":"sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=","owner":"vpsfreecz","repo":"ruby-lxc","rev":"004bf35eb90d41ba60b347b5b1e73d868a4f95d9","type":"github"}` | `{}` |
| `systems` | `{"lastModified":1791244623,"narHash":"sha256-uuanbkFk8a313Zfrxdcz8Us/yQtaxNnKJtX8v0ZPpd8=","owner":"nix-systems","repo":"default","rev":"d36eeed142f88b5a636f2e3856a53c61654cf29b","type":"github"}` | `{}` |
| `toolsNixpkgs` | `{"lastModified":1783522502,"narHash":"sha256-iffAls3iaNTyJC2faYcUXSI+Gp02cDjYl+MygxKl2GI=","owner":"NixOS","repo":"nixpkgs","rev":"0bb7ec54c8483066ec9d7720e780a5caa71f8612","type":"github"}` | `{}` |
| `treefmt-nix` | `{"lastModified":1791885023,"narHash":"sha256-C3alQ2MEt0zVrUSho5NUDo3jmhbff72++bfwoqT9Omo=","owner":"numtide","repo":"treefmt-nix","rev":"0d6d739a833ba9a9c93034862e4a7b061a062a1c","type":"github"}` | `{"nixpkgs":["vpsfree-dev-workspace","dev-workspace","llm-agents","nixpkgs"]}` |
| `vpsadmin` | `{"lastModified":1791728853,"narHash":"sha256-3YDInHVVj5ke4aL8fjCYsNOK6S/r5W3LidG96V2/81g=","owner":"vpsfreecz","repo":"vpsadmin","rev":"939159f27b5d627930281d5fac0c0aa9ba53bfc7","type":"github"}` | `{"nixpkgs":["vpsfree-dev-workspace","kb-runtime","vpsadmin","vpsadminos","nixpkgs"],"vpsadminos":"vpsadminos"}` |
| `vpsadminos` | `{"lastModified":1788379445,"narHash":"sha256-mDLxNpbfUmo2FRXW5MJWJ8WqKLINUru6nVHB7zN4bVo=","owner":"vpsfreecz","repo":"vpsadminos","rev":"6bdf458fd9105379860234ff33d352e55844f08f","type":"github"}` | `{"impermanence":"impermanence_2","netlinkrb":"netlinkrb_2","nixpkgs":"nixpkgs_6","nixpkgsUnstable":"nixpkgsUnstable_2","ruby-lxc":"ruby-lxc_2"}` |
| `vpsfStatus` | `{"lastModified":1783669700,"narHash":"sha256-fiaFXRCldKuaiEFNO+TSvzrgYOCW8xOsEjDRND97Pss=","owner":"vpsfreecz","repo":"vpsf-status","rev":"29853c364e2fa072152d2de4f17e57f1e802b9f3","type":"github"}` | `{"nixpkgs":["vpsfree-dev-workspace","kb-runtime","nixpkgs"],"vpsadmin":["vpsfree-dev-workspace","kb-runtime","vpsadmin"],"vpsadminos":["vpsfree-dev-workspace","kb-runtime","vpsadminos"]}` |
| `vpsfree-dev-workspace` | `{"lastModified":1792016982,"narHash":"sha256-om/+qNfQw6y74gjdzXfVG5AbHOQGysMefFZiqR92KP4=","owner":"vpsfreecz","repo":"dev-workspace","rev":"767dfd587e346168e1443e65ccdb67ce748f3fe3","type":"github"}` | `{"dev-workspace":"dev-workspace","devcluster-vpsadmin":"devcluster-vpsadmin","devcluster-vpsadminWebui":"devcluster-vpsadminWebui","devcluster-vpsadminos":"devcluster-vpsadminos","devcluster-vpsf-status":"devcluster-vpsf-status","kb-runtime":"kb-runtime","nixpkgs":"nixpkgs_7"}` |

### vpsfree-cz-configuration
Complete committed lock: `4715580512a4042bea75cb44167efb42b3618f70:flake.lock`; Git blob `ff75bd0490c2dd8365c81b6c41ead5d2b54515e2`; SHA-256 `c278bd3baa2f2454180498a92577e4d8ab4a807165ff2b3c0eb08d165af329ca`. Root node `root`.
| Node | Locked identity | Input edges (arrays are follows paths) |
| --- | --- | --- |
| `bun2nix` | `{"lastModified":1790001035,"narHash":"sha256-1/SLBjSYBzDdDhvLQ83wrzBakyS/xNGgtxHGNuveOEQ=","owner":"Mic92","repo":"bun2nix","rev":"07a5bfc8ac36c5370199343fa620b69f63186e33","type":"github"}` | `{"flake-parts":["devWorkspace","llm-agents","flake-parts"],"nixpkgs":["devWorkspace","llm-agents","nixpkgs"],"systems":["devWorkspace","llm-agents","systems"],"treefmt-nix":["devWorkspace","llm-agents","treefmt-nix"]}` |
| `bun2nix_2` | `{"lastModified":1790001035,"narHash":"sha256-1/SLBjSYBzDdDhvLQ83wrzBakyS/xNGgtxHGNuveOEQ=","owner":"Mic92","repo":"bun2nix","rev":"07a5bfc8ac36c5370199343fa620b69f63186e33","type":"github"}` | `{"flake-parts":["llm-agents","flake-parts"],"nixpkgs":["llm-agents","nixpkgs"],"systems":["llm-agents","systems"],"treefmt-nix":["llm-agents","treefmt-nix"]}` |
| `codex-web` | `{"lastModified":1793126110,"narHash":"sha256-ud0d214cykppfBEGo6lmyW1Z1g75R6Q2SbgpwIeTM2I=","owner":"aither64","repo":"codex-web","rev":"58300182763a01de7248ddf7c6cb9a4f0c6216cb","type":"github"}` | `{}` |
| `confctl` | `{"lastModified":1784400083,"narHash":"sha256-gh1tmTv8aAO1OA3HX2NEYnRALMK2i666Lxey8hxD0QM=","owner":"vpsfreecz","repo":"confctl","rev":"7bee58a52372b95c2198ce3f2a719807a3c2c66b","type":"github"}` | `{"nixpkgs":["confctl","vpsadminos","nixpkgs"],"vpsadminos":"vpsadminos"}` |
| `devWorkspace` | `{"lastModified":1793178004,"narHash":"sha256-dYrIZBVInRfXYg3p0BjMxqgTQ8saZnd7eEn0Hcq7wNI=","owner":"aither64","repo":"dev-workspace","rev":"4a002f52c3b55099540aa99708d5fcf29f7b2456","type":"github"}` | `{"codex-web":"codex-web","llm-agents":"llm-agents","nixpkgs":"nixpkgs_4"}` |
| `flake-parts` | `{"lastModified":1790898470,"narHash":"sha256-zTwuwezD0w3hpga6a6P8emidzAZFyWqlNeRBlpWOOl8=","owner":"hercules-ci","repo":"flake-parts","rev":"024633cd702b10285db5cb19b40ad48d2399ba60","type":"github"}` | `{"nixpkgs-lib":["devWorkspace","llm-agents","nixpkgs"]}` |
| `flake-parts_2` | `{"lastModified":1790898470,"narHash":"sha256-zTwuwezD0w3hpga6a6P8emidzAZFyWqlNeRBlpWOOl8=","owner":"hercules-ci","repo":"flake-parts","rev":"024633cd702b10285db5cb19b40ad48d2399ba60","type":"github"}` | `{"nixpkgs-lib":["llm-agents","nixpkgs"]}` |
| `home-manager` | `{"lastModified":1768598210,"narHash":"sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=","owner":"nix-community","repo":"home-manager","rev":"c47b2cc64a629f8e075de52e4742de688f930dc6","type":"github"}` | `{"nixpkgs":["confctl","vpsadminos","impermanence","nixpkgs"]}` |
| `home-manager_2` | `{"lastModified":1780361225,"narHash":"sha256-wnV9ttf4fPWNonBIQmvlrSlNpQYgx5HgWWd007mwIFA=","owner":"nix-community","repo":"home-manager","rev":"e28654b71096e08c019d4861ca26acb646f583d8","type":"github"}` | `{"nixpkgs":["nixpkgsStable"]}` |
| `home-manager_3` | `{"lastModified":1768598210,"narHash":"sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=","owner":"nix-community","repo":"home-manager","rev":"c47b2cc64a629f8e075de52e4742de688f930dc6","type":"github"}` | `{"nixpkgs":["vpsadminosOsStaging","impermanence","nixpkgs"]}` |
| `home-manager_4` | `{"lastModified":1768598210,"narHash":"sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=","owner":"nix-community","repo":"home-manager","rev":"c47b2cc64a629f8e075de52e4742de688f930dc6","type":"github"}` | `{"nixpkgs":["vpsadminosProduction","impermanence","nixpkgs"]}` |
| `home-manager_5` | `{"lastModified":1768598210,"narHash":"sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=","owner":"nix-community","repo":"home-manager","rev":"c47b2cc64a629f8e075de52e4742de688f930dc6","type":"github"}` | `{"nixpkgs":["vpsadminosStaging","impermanence","nixpkgs"]}` |
| `home-manager_6` | `{"lastModified":1768598210,"narHash":"sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=","owner":"nix-community","repo":"home-manager","rev":"c47b2cc64a629f8e075de52e4742de688f930dc6","type":"github"}` | `{"nixpkgs":["vpsfStatus","vpsadmin","vpsadminos","impermanence","nixpkgs"]}` |
| `impermanence` | `{"lastModified":1769548169,"narHash":"sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y=","owner":"nix-community","repo":"impermanence","rev":"7b1d382faf603b6d264f58627330f9faa5cba149","type":"github"}` | `{"home-manager":"home-manager","nixpkgs":"nixpkgs"}` |
| `impermanence_2` | `{"lastModified":1792739756,"narHash":"sha256-s0TeXWG5Ci75Y/Hzon0Z7NrN/fG773Rc54/z6oPFszQ=","owner":"nix-community","repo":"impermanence","rev":"fa627f4c8b8e92f58f58a73d99ee4e1304e64eb2","type":"github"}` | `{"home-manager":"home-manager_3","nixpkgs":"nixpkgs_6"}` |
| `impermanence_3` | `{"lastModified":1769548169,"narHash":"sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y=","owner":"nix-community","repo":"impermanence","rev":"7b1d382faf603b6d264f58627330f9faa5cba149","type":"github"}` | `{"home-manager":"home-manager_4","nixpkgs":"nixpkgs_7"}` |
| `impermanence_4` | `{"lastModified":1792739756,"narHash":"sha256-s0TeXWG5Ci75Y/Hzon0Z7NrN/fG773Rc54/z6oPFszQ=","owner":"nix-community","repo":"impermanence","rev":"fa627f4c8b8e92f58f58a73d99ee4e1304e64eb2","type":"github"}` | `{"home-manager":"home-manager_5","nixpkgs":"nixpkgs_8"}` |
| `impermanence_5` | `{"lastModified":1769548169,"narHash":"sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y=","owner":"nix-community","repo":"impermanence","rev":"7b1d382faf603b6d264f58627330f9faa5cba149","type":"github"}` | `{"home-manager":"home-manager_6","nixpkgs":"nixpkgs_9"}` |
| `llm-agents` | `{"lastModified":1792920017,"narHash":"sha256-a4mZGtaldWR0DIsFbLgj9DI/5lVGbKDgQ6tbb2vWPfo=","owner":"numtide","repo":"llm-agents.nix","rev":"ea188d2f072e0ec8d5b71245e228803672801a22","type":"github"}` | `{"bun2nix":"bun2nix","flake-parts":"flake-parts","nixpkgs":"nixpkgs_3","systems":"systems","treefmt-nix":"treefmt-nix"}` |
| `llm-agents_2` | `{"lastModified":1792920017,"narHash":"sha256-a4mZGtaldWR0DIsFbLgj9DI/5lVGbKDgQ6tbb2vWPfo=","owner":"numtide","repo":"llm-agents.nix","rev":"ea188d2f072e0ec8d5b71245e228803672801a22","type":"github"}` | `{"bun2nix":"bun2nix_2","flake-parts":"flake-parts_2","nixpkgs":"nixpkgs_5","systems":"systems_2","treefmt-nix":"treefmt-nix_2"}` |
| `netlinkrb` | `{"lastModified":1562850306,"narHash":"sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=","owner":"vpsfreecz","repo":"netlinkrb","rev":"d9de53d843d2586ffa5b7b404887fa801c697ddf","type":"github"}` | `{}` |
| `netlinkrb_2` | `{"lastModified":1562850306,"narHash":"sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=","owner":"vpsfreecz","repo":"netlinkrb","rev":"d9de53d843d2586ffa5b7b404887fa801c697ddf","type":"github"}` | `{}` |
| `netlinkrb_3` | `{"lastModified":1562850306,"narHash":"sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=","owner":"vpsfreecz","repo":"netlinkrb","rev":"d9de53d843d2586ffa5b7b404887fa801c697ddf","type":"github"}` | `{}` |
| `netlinkrb_4` | `{"lastModified":1562850306,"narHash":"sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=","owner":"vpsfreecz","repo":"netlinkrb","rev":"d9de53d843d2586ffa5b7b404887fa801c697ddf","type":"github"}` | `{}` |
| `netlinkrb_5` | `{"lastModified":1562850306,"narHash":"sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=","owner":"vpsfreecz","repo":"netlinkrb","rev":"d9de53d843d2586ffa5b7b404887fa801c697ddf","type":"github"}` | `{}` |
| `nixpkgs` | `{"lastModified":1768564909,"narHash":"sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=","owner":"nixos","repo":"nixpkgs","rev":"e4bae1bd10c9c57b2cf517953ab70060a828ee6f","type":"github"}` | `{}` |
| `nixpkgsProduction` | `{"lastModified":1793015021,"narHash":"sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=","owner":"NixOS","repo":"nixpkgs","rev":"718f670e845328e9c2cecdd832835712b2cbd065","type":"github"}` | `{}` |
| `nixpkgsStable` | `{"lastModified":1793015021,"narHash":"sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=","owner":"NixOS","repo":"nixpkgs","rev":"718f670e845328e9c2cecdd832835712b2cbd065","type":"github"}` | `{}` |
| `nixpkgsStaging` | `{"lastModified":1793015021,"narHash":"sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=","owner":"NixOS","repo":"nixpkgs","rev":"718f670e845328e9c2cecdd832835712b2cbd065","type":"github"}` | `{}` |
| `nixpkgsUnstable` | `{"lastModified":1781074563,"narHash":"sha256-md8WlXOlfnIeHeOScMTTHFyf2d6iaTwPl2apR5EQ3P4=","owner":"NixOS","repo":"nixpkgs","rev":"9ae611a455b90cf061d8f332b977e387bda8e1ca","type":"github"}` | `{}` |
| `nixpkgsUnstable_2` | `{"lastModified":1792773339,"narHash":"sha256-rZLrzrC6i+jnTAlvPZHogKDulY7WWDEv9hJeHieO7Zw=","owner":"NixOS","repo":"nixpkgs","rev":"3ec636362e1816bc2f0888fa0fa2c69f1bc9e504","type":"github"}` | `{}` |
| `nixpkgsUnstable_3` | `{"lastModified":1786106723,"narHash":"sha256-zDSUbpoeo/9ZmD2+wXnzxoo1+uhL8vxc0b8yuYMKYq0=","owner":"NixOS","repo":"nixpkgs","rev":"f13ff45afd1bb73e640eaa08a7066dbed07e3238","type":"github"}` | `{}` |
| `nixpkgs_10` | `{"lastModified":1786089803,"narHash":"sha256-ZuvZfVW2tB5tXYEcpcfhVXB3N4OhdZLOqOviy4OD4b4=","owner":"NixOS","repo":"nixpkgs","rev":"ee48b147c18c7de1e6ec97dc74792be42724bed1","type":"github"}` | `{}` |
| `nixpkgs_2` | `{"lastModified":1780902259,"narHash":"sha256-q8yYEC5f1mFlQO9RGna4LTc9QrcvWunX6FYp83munkQ=","owner":"NixOS","repo":"nixpkgs","rev":"bd0ff2d3eac24699c3664d5966b9ef36f388e2ca","type":"github"}` | `{}` |
| `nixpkgs_3` | `{"lastModified":1792116957,"narHash":"sha256-EjZqHKObBfIOeHZnMRVV87HB3pPq/WBkmRJWyFxmZu8=","owner":"NixOS","repo":"nixpkgs","rev":"f20cd90e28fe0403873f473b29e42662cd86e8c4","type":"github"}` | `{}` |
| `nixpkgs_4` | `{"lastModified":1788405554,"narHash":"sha256-r2f1oUwixlgq9zOdYLqJLfS/lWBT60/IITjhTKI59JU=","owner":"NixOS","repo":"nixpkgs","rev":"a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4","type":"github"}` | `{}` |
| `nixpkgs_5` | `{"lastModified":1792116957,"narHash":"sha256-EjZqHKObBfIOeHZnMRVV87HB3pPq/WBkmRJWyFxmZu8=","owner":"NixOS","repo":"nixpkgs","rev":"f20cd90e28fe0403873f473b29e42662cd86e8c4","type":"github"}` | `{}` |
| `nixpkgs_6` | `{"lastModified":1768564909,"narHash":"sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=","owner":"nixos","repo":"nixpkgs","rev":"e4bae1bd10c9c57b2cf517953ab70060a828ee6f","type":"github"}` | `{}` |
| `nixpkgs_7` | `{"lastModified":1768564909,"narHash":"sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=","owner":"nixos","repo":"nixpkgs","rev":"e4bae1bd10c9c57b2cf517953ab70060a828ee6f","type":"github"}` | `{}` |
| `nixpkgs_8` | `{"lastModified":1768564909,"narHash":"sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=","owner":"nixos","repo":"nixpkgs","rev":"e4bae1bd10c9c57b2cf517953ab70060a828ee6f","type":"github"}` | `{}` |
| `nixpkgs_9` | `{"lastModified":1768564909,"narHash":"sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=","owner":"nixos","repo":"nixpkgs","rev":"e4bae1bd10c9c57b2cf517953ab70060a828ee6f","type":"github"}` | `{}` |
| `root` | `{}` | `{"confctl":"confctl","devWorkspace":"devWorkspace","home-manager":"home-manager_2","llm-agents":"llm-agents_2","nixpkgs":["nixpkgsStable"],"nixpkgsProduction":"nixpkgsProduction","nixpkgsStable":"nixpkgsStable","nixpkgsStaging":"nixpkgsStaging","nixpkgsUnstable":"nixpkgsUnstable_2","vpsadminProduction":"vpsadminProduction","vpsadminServices":"vpsadminServices","vpsadminStaging":"vpsadminStaging","vpsadminWebui":"vpsadminWebui","vpsadminosOsStaging":"vpsadminosOsStaging","vpsadminosProduction":"vpsadminosProduction","vpsadminosStaging":"vpsadminosStaging","vpsfStatus":"vpsfStatus","vpsfreeNotificationTemplates":"vpsfreeNotificationTemplates","vpsfreeWeb":"vpsfreeWeb"}` |
| `ruby-lxc` | `{"lastModified":1780499941,"narHash":"sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=","owner":"vpsfreecz","repo":"ruby-lxc","rev":"004bf35eb90d41ba60b347b5b1e73d868a4f95d9","type":"github"}` | `{}` |
| `ruby-lxc_2` | `{"lastModified":1780499941,"narHash":"sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=","owner":"vpsfreecz","repo":"ruby-lxc","rev":"004bf35eb90d41ba60b347b5b1e73d868a4f95d9","type":"github"}` | `{}` |
| `ruby-lxc_3` | `{"lastModified":1780499941,"narHash":"sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=","owner":"vpsfreecz","repo":"ruby-lxc","rev":"004bf35eb90d41ba60b347b5b1e73d868a4f95d9","type":"github"}` | `{}` |
| `ruby-lxc_4` | `{"lastModified":1780499941,"narHash":"sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=","owner":"vpsfreecz","repo":"ruby-lxc","rev":"004bf35eb90d41ba60b347b5b1e73d868a4f95d9","type":"github"}` | `{}` |
| `ruby-lxc_5` | `{"lastModified":1780499941,"narHash":"sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=","owner":"vpsfreecz","repo":"ruby-lxc","rev":"004bf35eb90d41ba60b347b5b1e73d868a4f95d9","type":"github"}` | `{}` |
| `systems` | `{"lastModified":1791244623,"narHash":"sha256-uuanbkFk8a313Zfrxdcz8Us/yQtaxNnKJtX8v0ZPpd8=","owner":"nix-systems","repo":"default","rev":"d36eeed142f88b5a636f2e3856a53c61654cf29b","type":"github"}` | `{}` |
| `systems_2` | `{"lastModified":1791244623,"narHash":"sha256-uuanbkFk8a313Zfrxdcz8Us/yQtaxNnKJtX8v0ZPpd8=","owner":"nix-systems","repo":"default","rev":"d36eeed142f88b5a636f2e3856a53c61654cf29b","type":"github"}` | `{}` |
| `treefmt-nix` | `{"lastModified":1791885023,"narHash":"sha256-C3alQ2MEt0zVrUSho5NUDo3jmhbff72++bfwoqT9Omo=","owner":"numtide","repo":"treefmt-nix","rev":"0d6d739a833ba9a9c93034862e4a7b061a062a1c","type":"github"}` | `{"nixpkgs":["devWorkspace","llm-agents","nixpkgs"]}` |
| `treefmt-nix_2` | `{"lastModified":1791885023,"narHash":"sha256-C3alQ2MEt0zVrUSho5NUDo3jmhbff72++bfwoqT9Omo=","owner":"numtide","repo":"treefmt-nix","rev":"0d6d739a833ba9a9c93034862e4a7b061a062a1c","type":"github"}` | `{"nixpkgs":["llm-agents","nixpkgs"]}` |
| `vpsadmin` | `{"lastModified":1785850721,"narHash":"sha256-5MfntVa4kDeE1MjIAIMDlGk3X7fJ6BzS7GWW0mCEwuk=","owner":"vpsfreecz","repo":"vpsadmin","rev":"3f9b68adb97b7f43df929a85fc172d9d11e15211","type":"github"}` | `{"nixpkgs":["vpsfStatus","vpsadmin","vpsadminos","nixpkgs"],"vpsadminos":"vpsadminos_2"}` |
| `vpsadminProduction` | `{"lastModified":1792321599,"narHash":"sha256-U0py4ENShmTqcwZDUn11GABUnE0BhVnTM1EXylJmcMc=","owner":"vpsfreecz","repo":"vpsadmin","rev":"ff730be468e366ee346dc6d02dc0fe57c3f8677c","type":"github"}` | `{"nixpkgs":["nixpkgsProduction"],"vpsadminos":["vpsadminosProduction"]}` |
| `vpsadminServices` | `{"lastModified":1791879729,"narHash":"sha256-o6HXcW1DX+R+pI5T9g9SsG8E0Pc1ljLzX4RxPGYsomM=","owner":"vpsfreecz","repo":"vpsadmin","rev":"4a21dd25b23de9832166def98526f410416b651e","type":"github"}` | `{"nixpkgs":["nixpkgsStable"],"vpsadminos":["vpsadminosStaging"]}` |
| `vpsadminStaging` | `{"lastModified":1792321599,"narHash":"sha256-U0py4ENShmTqcwZDUn11GABUnE0BhVnTM1EXylJmcMc=","owner":"vpsfreecz","repo":"vpsadmin","rev":"ff730be468e366ee346dc6d02dc0fe57c3f8677c","type":"github"}` | `{"nixpkgs":["nixpkgsStaging"],"vpsadminos":["vpsadminosStaging"]}` |
| `vpsadminWebui` | `{"lastModified":1793157831,"narHash":"sha256-BPY81SY6Ma3Lrt7cdZSiaNkAU2GrWeTubdbfR7n+8TU=","owner":"vpsfreecz","repo":"vpsadmin-webui","rev":"606a02c19f328c69298dd30780c805211fb5cb27","type":"github"}` | `{"nixpkgs":["nixpkgsStable"],"vpsadmin":["vpsadminServices"]}` |
| `vpsadminos` | `{"lastModified":1781261055,"narHash":"sha256-Y7FLO10JwU3bo0j6dRHboubKAP8VRxxnaiD2NshG+Kc=","owner":"vpsfreecz","repo":"vpsadminos","rev":"6f9b2c755143197bd9c3452e1c0121b22e978c4d","type":"github"}` | `{"impermanence":"impermanence","netlinkrb":"netlinkrb","nixpkgs":"nixpkgs_2","nixpkgsUnstable":"nixpkgsUnstable","ruby-lxc":"ruby-lxc"}` |
| `vpsadminosOsStaging` | `{"lastModified":1793088973,"narHash":"sha256-HRAKzl1PywAm/AVo64V1PXOg5xD2i+Z1oMdrC/aG9Mk=","owner":"vpsfreecz","repo":"vpsadminos","rev":"f4e55a13d7d2f5c1b61737f0300ec8a535ef02f1","type":"github"}` | `{"impermanence":"impermanence_2","netlinkrb":"netlinkrb_2","nixpkgs":["nixpkgsStable"],"nixpkgsUnstable":["nixpkgsUnstable"],"ruby-lxc":"ruby-lxc_2"}` |
| `vpsadminosProduction` | `{"lastModified":1792347366,"narHash":"sha256-jyXAH3nUkocJj+KQKINbJ0UnDCmuln4EvYRw/1KtXFE=","owner":"vpsfreecz","repo":"vpsadminos","rev":"2abbe3cc1c102a4b39022d3f73ef4a432ad4d616","type":"github"}` | `{"impermanence":"impermanence_3","netlinkrb":"netlinkrb_3","nixpkgs":["nixpkgsProduction"],"nixpkgsUnstable":["nixpkgsUnstable"],"ruby-lxc":"ruby-lxc_3"}` |
| `vpsadminosStaging` | `{"lastModified":1793088973,"narHash":"sha256-HRAKzl1PywAm/AVo64V1PXOg5xD2i+Z1oMdrC/aG9Mk=","owner":"vpsfreecz","repo":"vpsadminos","rev":"f4e55a13d7d2f5c1b61737f0300ec8a535ef02f1","type":"github"}` | `{"impermanence":"impermanence_4","netlinkrb":"netlinkrb_4","nixpkgs":["nixpkgsStaging"],"nixpkgsUnstable":["nixpkgsUnstable"],"ruby-lxc":"ruby-lxc_4"}` |
| `vpsadminos_2` | `{"lastModified":1786260915,"narHash":"sha256-Xd+DyVC+Gkv6+1oSsxb8VfE3DtVCHx90vmKvuFuhYbY=","owner":"vpsfreecz","repo":"vpsadminos","rev":"837baf04054c6ee0e71d288b8870ac42a6990c38","type":"github"}` | `{"impermanence":"impermanence_5","netlinkrb":"netlinkrb_5","nixpkgs":"nixpkgs_10","nixpkgsUnstable":"nixpkgsUnstable_3","ruby-lxc":"ruby-lxc_5"}` |
| `vpsfStatus` | `{"lastModified":1788260265,"narHash":"sha256-4iun0P87K5kKG2vYi6Beio/1iWlHmNYFjD8Hlg2qGgk=","owner":"vpsfreecz","repo":"vpsf-status","rev":"587cd65bb02e6dddea7f6b6409e42a15f36ab4fb","type":"github"}` | `{"nixpkgs":["nixpkgsStable"],"vpsadmin":"vpsadmin","vpsadminos":["vpsfStatus","vpsadmin","vpsadminos"]}` |
| `vpsfreeNotificationTemplates` | `{"lastModified":1790168321,"narHash":"sha256-tVRZNlK2iOcorDkw5bK/10e911ILS7VY5uMExH91NQ4=","owner":"vpsfreecz","repo":"vpsfree-notification-templates","rev":"2cfd218d9152888feea4109f064459078ea9f76e","type":"github"}` | `{"vpsadmin":["vpsadminServices"]}` |
| `vpsfreeWeb` | `{"lastModified":1791740386,"narHash":"sha256-/3QHdhSzFlEc7YqWZDjnVxIeS4n1OdImicvgUZjBGew=","owner":"vpsfreecz","repo":"web","rev":"307635a96bc3532af51ff5d08206d920704eee00","type":"github"}` | `{}` |

## Successful package build receipts

### runtime package/check outputs
| Derivation | Outputs |
| --- | --- |
| `/nix/store/mwzwshp0sscxd25c2j55m4qrq4xcrb7n-dev-workspace-0.2.0.drv` | `{"out": "/nix/store/ynh458fkyzs33kaxgpf36a52yn210c49-dev-workspace-0.2.0"}` |
Retained indirect Nix root: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-28-observer-progress-guidance/roots/runtime-package`.

### workspace package/check outputs
| Derivation | Outputs |
| --- | --- |
| `/nix/store/4c7xg1lxpv48a6rydfbfp9rjp69ax548-dev-workspace-0.2.0.drv` | `{"out": "/nix/store/pjmi2cz75r9cwynh4lin706jdzlp4xb9-dev-workspace-0.2.0"}` |
| `/nix/store/i10cfmjrlifbjbar6wv2a6dp5awfhpdw-workspace-agent-team-policy-tests.drv` | `{"out": "/nix/store/935nhx5fpxq9lxdv5z8qp3jicmgvxzhx-workspace-agent-team-policy-tests"}` |
| `/nix/store/q6fhal3788z0bp4028j6ldfkischyyhf-workspace-agent-instructions-tests.drv` | `{"out": "/nix/store/fiq0dfzmpd996yb8i7r123wwx5lsabks-workspace-agent-instructions-tests"}` |
| `/nix/store/fsgk7y3iqzq20qcgxbwwf8pbfnwkqc34-dev-workspace-deployment-contract-tests.drv` | `{"out": "/nix/store/8x0vs3scdpjfi6acygrqc65rkc0kszb1-dev-workspace-deployment-contract-tests"}` |
Retained indirect Nix root: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-28-observer-progress-guidance/roots/workspace-package`.

## Fresh remote lineage status before integration approval
2026-10-28T09:59:53.265293+00:00; source refs obtained by SSH ls-remote immediately before these local object ancestry checks.
| Repository | Deployed/final feature | Fresh remote master | Feature ancestor of master |
| --- | --- | --- | --- |
| workspace | `f10e7e530e1dba252e11d587667c3051118ee206` | `ecf12834bcded12d29090db52972fbaf9e8eb37f` | No |
| dev-workspace | `4a002f52c3b55099540aa99708d5fcf29f7b2456` | `d5d2b39b13a6875a26b218ffaf7b589b9d71a1fb` | No |
| vpsfree-cz-configuration | `4715580512a4042bea75cb44167efb42b3618f70` | `2cf292f465cee8b969d53f8c96f937b021ecb4a6` | No |
All three exact features remain unmerged. No equivalence replacement or refreshed history exists. Machine claim remains held because integration evidence is missing, despite verified deployment and settled drivers. Do not release or close this session before the applicable prerequisites and explicit lifecycle direction.

## Accepted workspace history refresh before integration

User approved all three master targets ("ok, merge it"). Workspace only: old reviewed/deployed c85ca1e46..f10e7e530 was refreshed to60ed89b75..6e131813e after three tracking-only baseline commits. Exact deployed old head is retained locally/remotely by recoveryref2026-10-28-observer-progress-guidance-workspace-deployed. Independent reviewer0 accepted the schema1 mapping in [review.md](review.md): equal ordered patch IDs/range-diff, reconstructed complete source map, unchanged full input graph and all4 successful derivations/output identities. No new build/deployment required. f10e7 is not literally merged; use accepted equivalent successor plus fresh post-merge remote proof. Runtime4a002f52 and configuration47155805 remain unchanged.

## Final approved integration and pre-release proof

2026-10-28T10:23:17.040698+00:00 fresh parallel SSH ls-remote proves runtime master4a002f52c3b55099540aa99708d5fcf29f7b2456, configuration master4715580512a4042bea75cb44167efb42b3618f70, workspace master6e131813ed455b2335a9287be760877d3242fd9d. Each equals the registered final feature head and ancestry checks pass. Runtime/config deployed commits are literally integrated; workspace deployed f10e7 is a NONANCESTOR with independently accepted equivalent successor6e131, schema1 receipt in review.md. Original full source/input graph and all4 exact successful derivations/output identities carry forward.

Serial ff-only integration used repository claims129b9a59-6b6f-441e-afce-3ba7dda066db (runtime),2663bfcd-3751-49b3-891f-a337e834c3f2 (config) and8f86debc-cbeb-49dc-8eeb-5292ba0eadbe (workspace), all explicitly released and verified. Config automatic/explicit post-merge hooks passed. Shared workspace took dev-session-tracking.lock nonblocking after its claim and retained it through fresh checks/merge/push/remote proof; unrelated logical index entries/flags were byte-identical before/after, SHA2567058b2d47e378492a2145e9a43fa47364bec28141506ac0f93c6bdaaeb77e3e8. No branch/ref/worktree deleted.

Pre-release deployment/effect proof refreshed: exact system live/profile lg62jfx2... and exact application pjmi2cz... paths remain as above; portal routing healthy. Both deployment units active/exited Resultsuccess/ExecMainStatus0/MainPID0, no unfinished Git or deployment commands. Authoritative claim0fe3d47f-e906-4d9d-ba9f-eab117b0f58e is held by exact owner0b362121-f6e1-4a1e-ab67-715f964c6a06 for machine:vpsfree:aitherdev. User separately requested release aitherdev. Release prerequisites now met; release immediately, before CI waiting or cleanup.
