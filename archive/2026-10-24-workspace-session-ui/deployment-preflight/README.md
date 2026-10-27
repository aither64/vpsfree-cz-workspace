# Deployment preflight evidence

The old rollout inputs and whole-contract assertion below are historical. The
accepted resumed comparison, helper checks, preserved originals and fresh command
forms are in [contract-split-handoff.md](contract-split-handoff.md). Do not run the
old candidate or post command with 9293; use the fresh reviewed/built receipts.

Owner: implementer2. These scripts perform bounded reads and create new receipts
only in this directory. They do not build, copy, claim, activate, select a profile,
send messages, change settings, or invoke lifecycle/cluster operations. The lead
owns activation and the rollout record. Candidate comparison waits for the
lead's explicit successful build/output signal.

`pre-authenticated.json` is the authoritative PRE capture from this package:
native PID 3387667, selected workspace package `8ph05i3nps8xi1jfs450b16aysc16nvg`,
old system `n6b9dmmaw83zx80paglrisy0w5rwnfw8`. Canonical and alias authenticated
health, this session's page/assets, and lead plus six retained-member transcript
GETs all returned 200 with all seven thread IDs matching. The naming child PID
4005731, its owned socket and exact catalog hash were present. This is naming
readiness, not inference evidence. Transcript content and credentials are not
retained. The older `pre-baseline*.json` files preserve initial local-socket
diagnosis; the first has corrected HTTP/transcript status handling in its successor.

The tool process has stale supplementary groups. The configured
`workspace-portal-owner` group includes aither; standard `sg` membership refresh
without a password can read the root-owned group-readable portal password.
Only the HTTP child uses that group. Process identity reads stay in the original
context because changed credentials cannot inspect existing `/proc/PID/exe`.
No permissions/group definitions changed. Local `sudo -n` cannot read root files;
normal host activation uses the configuration owner's independently verified root
SSH route, recorded in `../configuration-preparation/root-ssh-access.log`.

## Refresh before activation

Run from the original member/lead context, not under `sg` around the whole command:

```sh
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/capture.py \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/pre-activation.json
```

The script verifies exact session/environment identity and refreshes native
PID/executable/argv/start/hash, services, selected profile, system/profile/config
identities, immutable marker, registration inventory, retained roster, authenticated
HTTP statuses/hashes/thread identities and naming process/socket/catalog. It never
reads process environments. A fresh receipt filename is required. Any credential
access refusal remains visible as unverified authentication; never waive it.

## Built candidate comparison

The lead supplies the exact built `CANDIDATE` from the workspace owner's output
receipt after its build succeeds. Do not bind this to the superseded e1c head or
rebuild anything. The final workspace source is cbaa7d949eb4e9061cda7ff896dc6d97f2e0c2aa.
Configuration remains eac2877469a3b626f4c0d81f301f9320dae564cb.

```sh
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/compare.py \
  candidate /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/candidate-comparison.json \
  CANDIDATE /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/pre-activation.json
```

This checks the actual composed native launcher and materialized executable
against the launch marker and live process using exact paths, SHA-256 and `cmp`.
It preserves native package/deriver/manifest/resource-helper hashes. It compares
selected/candidate/launch runtime contracts; claims, coordination, integration,
extension and team catalogs; native role config bytes; public candidate
registration output against immutable launch policy/capacity/argv and retained
inventory; and the exact aitherdev machine mapping. Only path churn with identical
content normalizes away. Catalog capacity remains distinct from actual launch
capacity. A mismatch stops; it does not authorize repair or bypass.

Delegate this uncertain-duration registration/tree-hash comparison to the lead's
fresh verification watcher with the exact candidate substituted. No candidate
comparison has been run during preparation. Preserve the workspace owner's output,
deriver, closure, recursive derivation/source graph and flake metadata under
`../workspace-input-preparation/`; preserve the configuration owner's exact
generation/system toplevel/graph separately. This script does not recreate them.

## After lead activation

Refresh with `capture.py` into `post-activation.json`, then compare using the exact
built system toplevel and configuration head from the configuration owner's receipt:

```sh
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/compare.py \
  post /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/post-comparison.json \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/pre-activation.json \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/post-activation.json \
  CANDIDATE SYSTEM_TOPLEVEL CONFIGURATION_HEAD
```

This requires the intended system/profile/config/runtime identities, same native
PID/executable/argv/start/hash and immutable marker, unchanged retained roster,
running services, authenticated health/routing/retained-thread GETs and exact
served app/style hashes from the reviewed source. Naming process/socket/catalog
readiness is required but inference remains separate. The four product behaviors
retain their reviewed exact-source/browser-suite evidence; an HTTP 200 alone does
not establish interactive UI acceptance.

No existing public no-session naming-inference command was found in the selected
portal CLI or routes. Naming inference is part of creation preparation and must
not be called against a real session for this smoke check. The existing managed
naming smoke is a disposable VM fixture, not a live read-only probe; no duplicate
product/naming suite was launched. Ask the lead for a specifically scoped existing
disposable canary only if actual inference must be newly established.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/>
