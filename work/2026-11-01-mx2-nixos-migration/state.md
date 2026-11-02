---
lifecycle: active
---

# mx2 NixOS branch recovery

## Current status

User-requested recovery/rebase and verification proposal delivered. Implementation,
quick checks, independent final review and targeted build passed. **Production
replacement is not ready:** inherited relay policy and firewall prevent public
backup-MX service. No deployment or default-branch integration requested/performed.
Session stays open and active with its unmerged registered feature branch.

## Phase checklist

- [x] Verify exact session identity and retained roster/access.
- [x] Architect investigation/design and dependency boundaries.
- [x] Import exact old branch; preserve original checkout and source ref.
- [x] Replay/rebase on fresh default; bounded current-option/format adaptation.
- [x] Quick checks, normal hooks and complete history inventory.
- [x] Publish feature; verify remote head and unchanged default.
- [x] Independent final review and reconcile advisory findings.
- [x] Targeted system build and verification proposal/handoff.
- [ ] Future: agree/fix operational policy, isolated SMTP runtime verification.
- [ ] Future: approved preproduction, cutover/recovery and integration.

## Repository and exact provenance

| Item | Identity |
| --- | --- |
| Project | vpsfree-cz-configuration |
| Worktree | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-mx2-nixos-migration/vpsfree-cz-configuration` |
| Published branch | `2026-11-01-mx2-nixos-migration` |
| Final head | `e4c1ac0c5ae7426fb019b79ba936b30ce63e6e6c` |
| Fresh remote master/base | `c040c14cdbacc07998700b524996a89306188d7f` |
| Original local branch | `2025-05-30-mx2` at `40411d67ee97cea800bcccd89b0473432b4502c4` |
| Historical source base | `0bcc165f13059782bf686da39a3a9b5698b10275` |
| Preserved canonical source ref | `2026-11-01-mx2-nixos-migration-source` at original local head |

Fresh final `git ls-remote` confirms exact feature head and unchanged master.
Clean final worktree. Source before/after snapshots are identical. Native
registration's true initial base is original imported 40411d67; capture-comparison
records fresh final base/head. One final commit, five paths/94 additions; original
host patch 68 lines plus RFC formatting, `swpins.channels` -> `inputs.channels`.
Already-applied cache commit dropped. No input/lock/deploy/shared-profile changes.
Full provenance and source/input graph bindings: [import-rebase.md](import-rebase.md),
[range-diff.md](range-diff.md). Complete lock recoverable from final committed
flake.lock, blob `ec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86`, SHA-256
`505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a`.

## Checks and build

Quick checks passed: all five Nix files formatted/parsed; working/index/full-range
whitespace; normal Overcommit Nixfmt and commit-msg hooks; exact single-host
inventory and final committed-head toplevel evaluation. Supported deprecated
Postfix config option warning only. Feature CI list empty; only scheduled/manual
updater exists. No push-triggered CI expected/awaited.

Build passed once (exit 0, ~75 seconds), generation `2026-11-02--16-05-55`.
[mx2-build-result.md](mx2-build-result.md) and disposable `mx2-build.log` retain
actual command/output; expected system closure realized:
`/nix/store/yi0wph12csy27bzvwdj7idpd70wpyxd6-nixos-system-mx2-26.05.20261026.718f670`.
Derivation:
`/nix/store/0b88m9lch1bcvzn6iwbp60i7lf7jb5ip-nixos-system-mx2-26.05.20261026.718f670.drv`.
No build/process remains running. No activated/deployed profile or machine claim.

Fresh build utility `mx2_build_watch` used pinned catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`,
`gpt-6-luna` / `low`, operation lifetime/full execution access; matching native
verification_watcher-low.toml from installed package
`/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`.
Separate earlier devshell utility passed in 43s. No retained-member settings changed.

## Independent review

[review.md](review.md), packet [review-packet.md](review-packet.md).
Retained reviewer0, thread `01a19caf-15c8-74a2-baf1-6594cf30d117`,
`gpt-6.1-sol` / `xhigh`, read_only. Exact identity verified; no override/fallback.
High-risk general, architecture/repetition, scope/proportionality and
risk/compatibility lanes after committed quick checks, before long build.
No Blocking/Important findings for preservation scope. Explicit clean final
whole-history conclusion; no migrations or repeated dependency/update streams.
No fix/rerun needed. Lead accepted advisory residuals for import only.

## Production risks and proposed next work

- Empty relay_domains prevents accepting intended public relay recipients.
- Generated firewall has no TCP25 allowance; only SSH/exporter exceptions.
- No inbound TLS configuration; absent milter is fail-open; recipient validity,
  greylisting and DNSBL behavior need explicit comparison with actual CentOS policy.
- Inherited identity/placement/admin key and auto-update tag remain unverified;
  tag is consumed by deploy-infra. Internal/public IPv6 declarations differ.
- CentOS queue/Postgrey state conversion and rollback compatibility untested.
  Retain independent queues and drain accepted mail even after reverting ingress.

Generated mail evidence: [evaluated-mail-config.md](evaluated-mail-config.md).
Architect's [design.md](design.md) gives staged isolated SMTP tests, controlled
preproduction and queue-safe cutover/rollback. Proposed only; no runtime mail or
production query performed. Build success does not establish mail delivery.

## Ownership, records and next action

Architect0 owned investigation/design; implementer0 owned complete import/replay,
hook recovery, source/check/evidence and publication package; reviewer0 remained
independent; lead accepted results and owns tracking/handoff. No independently
needed second package; other retained implementers/settings preserved.

Initial substantive tracking commit `50fc32580`. Historical hook mismatch and
recovery recorded in import evidence and
`notes/vpsfree-cz-configuration/2026-11-02-import-pre-hook-branch.md`.
No hook bypass, source mutation, repository/machine claim or lifecycle action.
Preserve branches, worktree and open session. Next requested work would settle
mail/identity policy and implement isolated runtime checks before replacement.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-mx2-nixos-migration/
