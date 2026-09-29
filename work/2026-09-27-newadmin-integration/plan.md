# 2026-09-27-newadmin-integration

## Goal

I'd like you to review new web interface for vpsAdmin at https://github.com/Kerrycek/clankerdev

I'm interested in overall code quality, architecture, tests. We're looking for best practices, maintainability, etc. Prepare a document describing needed improvements if any.

After review and fixes, we will focus on integration of the new interface into vpsfree-cz-configuration and deploying it to a NixOS VPS, so we're also looking for:

- nixos support for the UI
- configuration of proxy.prg and related parts (vpsfree.cz. dns zone) in vpsfree-cz-configuration
- i suppose that we should add nixos modules like those in repo vpsadmin, subdir nixos/

we will also move the repo to vpsfreecz/ namespace on github, I haven't decided on proper repo name yet... feel free to make suggestions. we're considering newadmin.vpsfree.cz, newui.vpsfree.cz, etc. in the future, it will replace vpsadmin.vpsfree.cz (current webui).

## Deployed-service follow-up (2026-09-29)

The user deployed `newadmin.vpsfree.cz` and observed a browser `frame-src`
violation for `https://console.vpsfree.cz`. Add that exact origin and the
public-API-confirmed `https://goresheat.vpsfree.cz` origin to the site's frame
allowlist; leave the parent page's console connection allowlist empty. The
separate blocked inline-script hash does not match the deployed application's
one allowed inline bootstrap and is not an authorization to widen script CSP.

Replace the three BFF secret values currently supplied through
`/private/vpsadmin-webui.env` with systemd `LoadCredential` and application
startup reads of credential files. This is a direct cutover, with no dual-format
runtime migration path. The operator will supply the exact credential files
under `/private/` before deploying the new generation; preserve the signing
secret and session state to retain login sessions. Keep the already deployed
feature history and default branches intact, and provide explicit file layout,
validation, activation and rollback instructions. The architect owns the
technical brief; the implementer owns code/configuration; the lead coordinates
review, verification and operator handoff. The user deploys.

## Deployment SSH key follow-up (2026-09-29)

Authorize the two public keys in the user-supplied paste for deployment of
`cz.vpsfree/vpsadmin/int.vpsadmin-webui1` as `kerrycze`. The first key already
exists in `data/ssh-keys.nix`; add only the new deploy key there and reference it
from this host's `vpsfconf.admins.kerrycze.publicKeys`. Preserve the existing
key and SSH identity metadata, and do not extend the new key to other machines.
Verify the resulting root authorized keys by evaluating the host and a control
host. The user will deploy the configuration; this task does not activate it.

## OAuth session identity follow-up (2026-09-29)

The deployed WebUI's new OAuth sessions show the UI server's address and Node's
default User-Agent. The edge and private nginx already pass a normalized client
address to the BFF; its server-side authorization-code exchange does not send
that address or an explicit User-Agent to vpsAdmin. Send the BFF's validated
`req.ip` as vpsAdmin's existing `Client-IP` header for that exchange and identify
all outbound BFF OAuth calls with the stable `vpsadmin-webui` User-Agent. The
user chose the WebUI service identity rather than the browser's User-Agent for
new sessions. Do not trust inbound `Client-IP` or raw forwarding headers, change
the API's session contract, or widen proxy trust. Verify spoofing and both IP
families in tests, pin the reviewed WebUI revision through the configuration
channel, and build the affected host. The user deploys and verifies a fresh
login. Existing session rows are unchanged; no migration is needed.

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

- The initial review used a solo policy. The user's deployed-service follow-up
  explicitly activates the already retained design, implementation and review
  members for substantive changes.
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
