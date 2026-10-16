# Live acceptance preparation inventory: 6e1d9a19

**UNRUN. Static preparation passed; no live acceptance has been executed.**

This packet adapts `live-native-bb9e6291/` only for the published runtime and
consumer revisions supplied by the lead. No product, branch, pin, dependency,
persistent format or migration changed. Review, VM/CI, activation, artifact
registration and eventual execution remain lead-owned.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>

## Bound identity and source provenance

`dev-session current` from the bound tracking directory returned
`2026-10-14-i-d-like-the-dev-workspace`. Both session environment markers were
absent, matching the trusted thread binding. The same-session saved roster
revision 17 confirmed implementer0 ready with workspace_write, Sol/xhigh.
Workspace session/documentation/verification guidance, runtime AGENTS and the
documentation/handoff skills were read or reused. The lead retains state and
portal-manifest ownership.

- Runtime: `6e1d9a191724d376cad2a71f234f0e4d1c01f36f`.
- Workspace: `0a9d232e74209da2c2f53358e5f2807f34074055`.
- Configuration: `45fa9962df83b9bec65523ae6ee7d19b63bb03ea`.
- Predecessor runtime: `bb9e6291bec10227c961c36559fba406938f1eaa`.

All three source identities exist as local Git commit objects. The registered
runtime remains exactly 6e1d9a19 with a clean worktree. These source identities
are not evidence of remote preparation or activation.

## Exact adaptation

`adaptation.patch` compares the five copied files against the predecessor:

- `run.sh`: only the new bundle directory.
- `live-check.cjs`: only the fresh disposable-profile prefix.
- `expected.json`: only the exact runtime source revision; asset hashes unchanged.
- `run_live.py`: byte-identical; no patch hunk.
- `README.md`: new revision, proof filename, supplied consumer provenance and
  explicit unrun/static-only status.

`asset-comparison.json` independently compares Git object bytes for the shipped
browser client, worker and shared store at both full runtime revisions. All
three are identical. `provenance.json` records the exact consumer heads rather
than inheriting or guessing downstream pins.

`preserved-prior-bundle.sha256` covers all 14 predecessor files;
`preserved-live-bundles.sha256` covers all 39 existing prior live-bundle files.
Every digest was checked after preparation. No prior bundle, run or sealed
source/review/probe evidence was written.

## Packet files

- Executable inputs: `run.sh`, `run_live.py`, `live-check.cjs`, `expected.json`.
- Instructions and identity: `README.md`, `inventory.md`, `provenance.json`,
  `asset-comparison.json`.
- Adaptation/preservation: `adaptation.patch`, `preserved-prior-bundle.sha256`,
  `preserved-live-bundles.sha256`.
- Static evidence: `preparation-checks.log`, `preparation-checks.status`,
  `preparation-summary.json`.
- Manifests: `harness-sha256.txt` covers all four executable inputs;
  `preparation-artifacts.sha256` covers every packet file except itself.

There is no `run/`, browser profile, credentials file or final preparation proof
in this packet.

## Static checks and reproduction

Source the cached declared environment; do not invoke the Nix daemon:

```sh
source /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/runtime-dev-env.sh
cd /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/live-native-6e1d9a19
bash -n run.sh
node --check live-check.cjs
python3 -c 'import ast; ast.parse(open("run_live.py").read())'
sha256sum --quiet -c harness-sha256.txt
sha256sum --quiet -c preparation-artifacts.sha256
```

`preparation-checks.status` is 0. The log also records pinned Playwright module
resolution, local Chromium/Firefox/Xvfb executable presence, unchanged runner and
browser behavior, committed-asset digest checks, exact-source/worktree checks,
and old bundle preservation. These are static checks; none starts a browser or
display, invokes SSH/HTTPS, reads credentials or contacts a provider. Declared
Node is v24.19.0 and Python is 3.13.15. Playwright is 1.59.1 with the already
pinned browser bundle. The rooted Xvfb executable is present, without launch.

The default `profile-prepared.json` still covers e414ed3 rather than 6e1d9a19.
The unchanged exact-revision fence therefore refuses that proof. The planned
`profile-prepared-6e1d9a19.json` does not exist and was not manufactured.

## Future lead command, only after authorized activation

Use the genuine final preparation record, then run through the lead's fresh
verification watcher or its visible fallback:

```sh
LIVE_PROFILE_PREPARED=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/profile-prepared-6e1d9a19.json bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/live-native-6e1d9a19/run.sh
```

The lead may supply a different genuine actual record under this tracking root
via the existing `LIVE_PROFILE_PREPARED`. Never edit stale coverage or expected
source values to bypass the fence. A changed selected runtime requires fresh
matching preparation.

## Retained behavior and limits

The unchanged preparation/package/served-asset fences run before Enable,
before Test and after the zero-tab window. Deferred origin-scoped credentials
remain in memory only. Fresh headed browsers use normal Firefox push preferences
and native shipped Enable/Test/Disable. The test is delayed ten seconds, then
all portal tabs close for eighteen seconds with about:blank active.

Provider acceptance, worker receipt and browser notification records remain
separate evidence. No physical or macOS display, notification click or fully
quit-browser claim is made. Exit 0 means diagnostics completed, not delivery
success. There is no mock, fixture API, endpoint rewrite or transport override.

Only exact-owned display/browser resources may be cleaned. Uncertain cleanup
retains the private mode-0700 profile and mode-0600 recovery manifest for explicit
lead recovery; no retry or general cleanup is added. No live operation, host,
queue, reservation, lifecycle, source or pin mutation occurred during preparation.
