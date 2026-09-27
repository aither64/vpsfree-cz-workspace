# 2026-09-27-newadmin-integration

## Goal

I'd like you to review new web interface for vpsAdmin at https://github.com/Kerrycek/clankerdev

I'm interested in overall code quality, architecture, tests. We're looking for best practices, maintainability, etc. Prepare a document describing needed improvements if any.

After review and fixes, we will focus on integration of the new interface into vpsfree-cz-configuration and deploying it to a NixOS VPS, so we're also looking for:

- nixos support for the UI
- configuration of proxy.prg and related parts (vpsfree.cz. dns zone) in vpsfree-cz-configuration
- i suppose that we should add nixos modules like those in repo vpsadmin, subdir nixos/

we will also move the repo to vpsfreecz/ namespace on github, I haven't decided on proper repo name yet... feel free to make suggestions. we're considering newadmin.vpsfree.cz, newui.vpsfree.cz, etc. in the future, it will replace vpsadmin.vpsfree.cz (current webui).

## Affected repositories

Current implementation scope and operator decisions are in
[implementation-plan.md](implementation-plan.md). The original review approach
below remains the record of the initial assessment.

The user selected `vpsfreecz/vpsadmin-webui`, one instance on VPS 30431,
`172.16.9.170`, `vpsadmin-webui1.int.vpsfree.cz`, machine
`cz.vpsfree/vpsadmin/int.vpsadmin-webui1`, public `newadmin.vpsfree.cz`.
The user will deploy and will add the implementation team after planning.
Keep the existing OpenStreetMap call; do not recover `UI_REDESIGN.md`.
Use the replacement upstream design handbook. Add English/Czech localization
review against vpsAdmin's guide and require it in the UI repository instructions.
The guide and API compatibility reference will come from a locked `vpsadmin`
flake input, overridden in site configuration to follow `vpsadminServices`
from channel `vpsadmin`.

- `Kerrycek/clankerdev`: primary review target; SSH clone and detached review
  snapshot at `fd290b5ec1b22900e704e8cb990c5ba050af2394`.
- `vpsadmin`: read-only reference for API contracts and NixOS packaging.
- `vpsfree-cz-configuration`: read-only reference for proxy, DNS and deployment.
- `vpsadmin-webui`: canonical adoption repository; current upstream source
  `49c6a51d0b32c4a6d5dd1df426e0bac1d8066115`, new origin still empty.
- `aither64/vpsfree-cz-workspace`: small project-map addition on the session
  feature branch, committed/pushed separately from shared tracking records.

## Approach

Review architecture, representative safety-critical workflows, tests, build and
operational contracts. Produce an evidence-backed report in this session with
prioritized improvements, acceptance criteria and a proposed integration plan.
Run local non-live verification where practical. No application fixes, server
changes, live mutations, repository transfer or default-branch integration are
part of this initial review. Set up a development team before later code work.

## Decisions

- Preserve the existing solo roster for read-only investigation.
- Review immutable revisions; distinguish source findings, locally reproduced
  failures and operational assumptions.
- Naming and hostname suggestions are proposals for user selection.

## Compatibility and deployment

Evaluate browser/BFF/API contracts, OAuth registration and callback origin,
session persistence, upgrades and rollback, coexistence with legacy PHP UI,
reproducible Nix packaging, proxy trust, DNS/TLS ordering and future hostname
cutover. Record minimum supported API capabilities rather than assuming parity.
No database migration or node protocol change is intended by this review.

## Documentation

Audience: maintainers and operators deciding adoption and remediation priorities.
Deliverable: `review.md` here, linked from the session portal. Reusable product
and deployment docs should move to their owning repositories during fixes.

## Testing plan

Inspect declared npm/CI checks, run feasible clean-install static/unit/build
checks without live credentials, and assess mock versus real API coverage.
Use a fresh verification watcher for uncertain or long checks. Do not exercise
live mutation scripts or production endpoints. Proposed NixOS tests remain
future acceptance criteria until packaging exists.
