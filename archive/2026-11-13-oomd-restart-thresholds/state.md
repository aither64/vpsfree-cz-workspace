---
lifecycle: archived
---

# 2026-11-13-oomd-restart-thresholds

## Status

- Phase: configuration integrated; task complete with full-build limitation
  recorded. No deployment was requested. Session remains open.
- Integrated `08d68a85f24a95b70b2d806f995f04b236e4d89a` into remote
  `vpsfree-cz-configuration/master`, verified by fresh `git ls-remote` equality
  for master and retained feature ref. Node25 overrides are 4 restart hits and
  1.5x median; [focused config evidence](implementation.md#package-v-focused-canonical-json-verification)
  proves inherited verbose=true.
- Session identity verified by
  `dev-session current` and both environment markers.
- Retained Full-team roster verified; architect0 owns design and implementer0
  will own the narrow configuration package. No team changes.

## Phase checklist

- [x] Current thresholds and node-local design settled
- [x] Configuration committed and quick checks passed
- [x] Independent final review
- [x] Required build attempted; external initrd key absent; focused canonical JSON validation passed
- [x] Operator deployment excluded by explicit user scope
- [x] Explicit repository integration approval and integration

## Packages

| Package / deliverable | Owner | Dependencies / acceptance | Status / next evidence |
| --- | --- | --- | --- |
| D: current settings, semantics and design.md | architect0 | Node25 only; identify exact values and lower load threshold; compatible options and rollback | Accepted 21:08 UTC; [brief](design.md) |
| I: node-local configuration and evidence | implementer0 | Accepted D; hooks, quick checks, focused commit and full review packet | Accepted 21:16 UTC; [evidence](implementation.md), head 08d68a85; mutation window released |
| R: independent final review | reviewer0 | Complete committed range, quick checks passed; four lanes | Accepted 21:20 UTC; no findings, [report](review.md) |
| P: clean merge target and hook/environment preparation | implementer0 | I accepted and capacity reconfirmed; no merge/claim/build; preserve final head | Accepted 21:20 UTC; [prepared commands](implementation.md#package-p-integration-preparation), window released |
| B: required node25 configuration build | fresh runtime watcher | Accepted final R; exact source/input graph and node selector | --yes operation failed after 32.621s on absent external initrd key; no build output |
| V: shortest faithful merged-JSON check after external-secret blocker | architect0 design, implementer0 execution | Canonical activationScript string-context projection, unique direct etc/run/JSON derivation edges; no fake secret/source change/full-build claim | Passed 21:32 UTC; exact 4/1.5/true JSON asserted through real derivation graph |
| M: approved fast-forward integration | lead | Review/quick checks/V passed; full-build external-secret limit recorded; fresh target and hooks | Merged/pushed/remote-verified 21:33 UTC; claim released and status verified |

## Next actions

No further configuration implementation/integration work remains. Operator may
build/deploy the merged configuration in its secrets environment. No deployment,
live behavior verification or session lifecycle cleanup is part of this task.

## Integration approval

User explicitly instructed "merge it when done" in this conversation after
clarifying configuration-only scope in `vpsfree-cz-configuration`. Approval covers
that repository's `master` target and the node25-only settings change (4 hits,
1.5x median). Lead acknowledged the repository/target and post-check sequencing.
No deployment or lifecycle action is authorized by this approval.

## Documentation

- [Plan](plan.md), accepted architect-owned [design](design.md).

## Repositories

- Expected configuration worktree:
  `worktrees/2026-11-13-oomd-restart-thresholds/vpsfree-cz-configuration`.
- Implementer created branch/worktree from fresh origin/master
  `1a948a872f84bdb4643926b357cf15534de1d313`, which advanced beyond the design
  reference with production pin updates. Architect confirmed current-pin
  semantics before commit: vpsadminosProduction
  `c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62`, relevant threshold/configuration
  sources byte-identical, with an unrelated oomd queued-miss race fix.
- Published final feature head: `08d68a85f24a95b70b2d806f995f04b236e4d89a`;
  one commit, node25 config only, five additions; clean worktree. Quick checks
  and actual declared hooks passed; no push-triggered CI applies.
- Exact same final head now remote master; no rebase or equivalent-successor
  substitution was needed. Feature ref/worktree retained and clean. Temporary
  clean detached integration checkout removed after claim release; no session
  archival/deletion/stop or service cleanup.

## Commands run

- `dev-session current`: exact bound slug; environment agrees.
- `dev-session team list ... --as-is`: retained design, implementation and review
  members have expected settings/access.
- Architect assignment first encountered session command contention; exact
  stable-ID retry was accepted without changing settings.

## Results

- Architect source findings: configuration origin/master
  `d0674cc68ed2cb1c71606caa50fe31227ea3521a`, pinned vpsadminos
  `2abbe3cc1c102a4b39022d3f73ef4a432ad4d616`; node25 has no overrides.
- Defaults: 15-second interval, 8 restart hits, 40 stop hits, load multiplier
  2.0. Host activation is 1-minute load at least multiplier times its rolling
  median (up to 5760 samples / 24 hours). Hits accumulate/decay; inactive rounds
  skip both hits and misses.
- User explicitly selected node-local multiplier 1.5 with restart hits 4,
  superseding the initial 1.8 proposal. User informed of the 25% threshold
  reduction.
- Lower host activation can also accumulate unchanged stop score sooner;
  restart success does not reset that score. Daemon restart resets in-memory
  scores and preserves the saved /run host-load history. Source defaults have
  not yet been certified against the running node.
- Read-only SSH baseline attempt to `root@node25.prg.vpsfree.cz` with batch
  authentication was refused (`Permission denied (publickey,password)`), exit
  255. No remote command ran and no machine mutation/claim was made. User then
  clarified that no node access is expected and this task is configuration-only.
  No further access/deployment work is needed; the refusal is not a task blocker.
- Initial tracking commit: `c2c2ed7f9a187b234af70cf8e5e31b01277791ae`.
- Final review: reviewer0 / gpt-6.1-sol / saved xhigh / four lanes / high due
  host behavior. Exact 1a948a87..08d68a85 range passed with no findings, obsolete
  history, migrations or repeated input streams. Documentation placement and
  preservation passed. No fallback or rerun.
- Build watcher launch verified: operation
  `b67eb7d4-fabb-4d5f-8500-478e0e6f40dc`, exact final head/input identity,
  selected package `/nix/store/22x45q9snm46qw95c1zjsbavifv9fki9-dev-workspace-0.2.0`,
  catalog `f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`,
  Luna/low/full_access, utility thread `01a1d6c8-f42d-70d0-81e7-bbf91b1bde20`,
  native turn receipt `01a1d6c8-fee5-7603-a2dd-f504ce1df597`.
- Initial build operation exited 1 after 12 seconds at confctl's default
  `Continue? [y/N]` prompt (EOF); no node build ran, no output receipt. Lead
  inspected [full log](node25-build.log) and pinned `confctl build --help`, which
  documents `-y/--yes`. No source failure or changed inputs. New fresh watcher
  `c708889a-2291-4444-a2d2-deb85b119331` runs the same command with `build --yes`;
  complete log [node25-build-yes.log](node25-build-yes.log).
- Corrected operation `c708889a-2291-4444-a2d2-deb85b119331` exited 1 after
  32.621s forcing node25 toplevel because
  `/secrets/nodes/initrd/ssh_host_ed25519_key` is absent. Lead inspected the
  complete terminal excerpt. All operation-owned work ended, no kernel/build
  output or machine mutation. This is the known external-secret requirement in
  [existing note](../../notes/vpsfree-cz-configuration/2026-07-13-confctl-node-build-initrd-secret.md).
  Do not retry unchanged or fabricate a key. Architect owns bounded alternative
  verification design; required full build remains recorded as unsuccessful.
- V canonical projection passed (~13s) without external secret. Unique actual
  graph: `/nix/store/1vaqc8lp512dxm3s6h8637rkm98zdl1n-etc.drv` →
  `/nix/store/zigk4rk1fmfsn8yrk19jvzf8nif0if48-sv-osctl-oomd-run.drv` →
  `/nix/store/qm4n2dlld168534ajiwdwdxnc2n5cfb3-osctl-oomd-config.json.drv`.
  Exact structured JSON value is `{"load_multiplier":1.5,"restart_hits":4,"verbose":true}`,
  including type and no-extra-key assertions. Canonical output path
  `/nix/store/vp9ybgilck71psx049hspq1xn1mi9c2n-osctl-oomd-config.json` is not realized;
  no claim of complete node/leaf build. Final source unchanged and clean.
- Lead accepts this bounded actual-config validation alongside successful quick
  checks and independent review; full build was attempted and its unrelated
  external-secret limitation remains explicit. No source/check weakening or fake
  key. Proceed with user-approved configuration integration.
- Integration used the prepared pinned shell and active hooks, clean target at
  reviewed base, one-commit final range and exact fresh remote base. Ordinary
  fast-forward merge and non-force SSH push passed; fresh remote master and
  feature both equal exact final head. No uncertain command effects remain.
- Repository claim `9104d9b4-38ab-4549-a22a-ad10d8136277` held only for fresh
  target/feature checks, merge/hooks, push and remote proof, 21:32:31–21:33:15 UTC.
  Released before records/temporary-checkout removal; authoritative claim-status
  confirms `released`. No machine reservation was acquired.
- CLI routing detail: selected `workspace-host coordination` supports status
  only and refused acquire without effects; authoritative selected guide's
  `dev-session coordination acquire/release/claim-status` worked. No duplicate
  claim or repository mutation arose from the refusal.
- Verification sequencing clarification accepted: pinned confctl does not expose
  full evaluated module config publicly. Avoid reconstructing its private
  evaluator. Parse/format/diff/hooks are quick pre-review checks; inspect the
  actual generated oomd JSON after the required post-review node25 build.

## Open questions

- Deployment/live verification belongs to the operator, outside this task; do
  not claim running values verified.
- Full-node build cannot pass without the external initrd key; focused canonical
  merged-JSON check passed. This residual operator build limitation is explicit,
  not an unresolved source defect or claimed successful build/deployment.

## Cleanup

No services or machine reservations created; repository merge claim released.
Feature branch/worktree retained, temporary detached merge checkout removed
cleanly. Preserve unrelated shared checkout/index changes. Session remains open;
no archival, deletion, stop or delayed cleanup was requested or scheduled.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-oomd-restart-thresholds/
