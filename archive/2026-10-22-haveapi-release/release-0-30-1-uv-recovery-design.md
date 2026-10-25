# Native uv recovery for the stopped 0.30.1 metadata target

Bounded design, 2026-10-24; execution requires lead acceptance and a new attempt
grant. Owner1 owns input qualification and the shadow/cache package; owner0 alone
resumes the maintained version target. No product code, dependency requirement,
Python support range, backend or Makefile change is proposed.

## Frozen failure and inputs

Preserve `release-0-30-1-version-preparation-20261024T110000Z/`, especially
`stage1-stop-handoff.md`, `stage1-stop-effects.json`, actual
`maintained-make-version.stderr` and the stopped 775-file inventory.

- HEAD: `8591394e13144431b27ecb366aae2b7b77a94e2c`; pre-version tree:
  `80804b1c0c3ed33fc4b086673dbc3618a789cd4f`; index and refs unchanged.
- One `make version VERSION=0.30.1` attempt stopped at `uv lock`, leaving exactly
  twelve intended version-only paths changed. All-775 stopped-source digest:
  `6e2ea94976248bd6667f016707dda89146a2e01c57199c5d87893495a3d1076e`.
- Python lock remains
  `6722cfb5ef72b4dcbe11e6e2331bd9927327ad11b05e6b6480c5dfb8a4b96e62`;
  Rust lock remains
  `7f51e5ea00157f4d215355acec5d95c2a8bcbb7d4600c5b34f5e1a338acbc1e4`.
  Root `7c48d2c2...`, tool-root `450de01a...`, CHANGELOG and all other tracked
  files are unchanged; use the stop receipt's full hashes as guards.
- Stderr reports missing offline Ruff 0.17.1 registry data in the
  `python_full_version >= '3.15'` resolution split. This does not establish an
  incompatible Python requirement. Preserve `requires-python = '>=3.11'` and
  both existing resolution markers.

Owner1's bounded same-session inventory found six bookkeeping/interpreter files
in the failed cache, no usable registry/simple/wheel entries, no alternate
qualified own cache and no original payloads for the 26 external packages.
Receipt: `release-0-30-1-uv-recovery-inputs/inventory-result.json`, SHA-256
`0a4f80405ef7af640b9b0a06de9db48e37e325e70f882bf63414a2e9406dc6fd`;
inventory manifest SHA-256
`7330175516a0aa8f2278de6002caa9fff37bec86b3f79d080af8abc10021faa0`.
The architect relies on that report, without duplicating cache inventory.

## Native shadow proof, then offline resume

Use native uv to populate a **new session-owned cache** while resolving a shadow
of the exact current Python project. Then produce an offline native shadow lock
and prove its only change is the local project version. Keep the live patch
frozen throughout preparation.

Exact tools:

```text
/nix/store/07gw2d21ivy19hgjj8wmyqhf338gqzdj-uv-0.13.1/bin/uv
/nix/store/bp3dz5ss8bbk5nwg03pvp39fngkydidv-python3-3.11.17/bin/python3
```

Installed `uv help lock` confirms existing locks supply resolution preferences;
`--upgrade` discards them. Preferences are not an exact-graph guarantee, so the
comparison below is mandatory. `--dry-run` resolves without writing the lock;
`--offline` uses only local data. Both flags are native to this selected binary.

After lead grants owner1 preparation:

1. Bind stopped source, original lock, tool digests and complete declared input
   graph. Make a fresh session shadow of the tracked Python project, including
   current 0.30.1 pyproject and unchanged original 0.30.0 lock. Copy source bytes,
   not an environment/cache. Record all inputs; never edit the copied lock.
2. In the shadow, run one explicitly online
   `uv lock --dry-run --no-build --no-python-downloads --no-config` with exact
   Python, new `UV_CACHE_DIR` and canonical `https://pypi.org/simple` default index.
   No upgrade/refresh, alternative index/find-links, constraints/overrides or
   Python-range options. Clear inherited uv/pip/index/venv/backend overrides;
   preserve declared TLS trust. This may write only new cache/evidence and must
   leave the shadow lock unchanged. Network scope is defined below.
3. Run native `uv lock --offline --no-build --no-python-downloads --no-config`
   against that same original lock/project/cache. Retain actual output lock,
   full stdout/stderr and exit; the dry-run summary alone is insufficient.
4. Require equality after normalizing **only** local `haveapi-client` version
   0.30.1 back to 0.30.0. All 26 external package records match in full: versions,
   sources, edges/markers, wheel/sdist URLs, hashes, sizes and upload metadata.
   Top-level lock version/revision, Python range/splits, project requirements and
   every other field remain exact. Require the ordinary textual diff to be just
   the local version line too. A TOML parser may compare, never emit/repair a lock.
5. Freeze cache/input inventories, shadow output/digests and launcher binding;
   yield command-free. No sync, install, compiler, test, venv or `make version`
   belongs to owner1's shadow step.

The universal lock covers all 26 records, including inactive-platform entries;
23 expected Linux-active packages are not the acceptance set. `--no-build`
blocks third-party sdist builds but explicitly allows first-party/editable backend
work. Here project metadata is static and its bundled backend is supported;
do not claim the flag alone forbids every backend operation. Unexpected
third-party building/backend resolution is a stop.

No private cache encoding, MessagePack editing, fragment merging, invented local
index or unpacked-wheel substitution for registry metadata. Upstream explicitly
says direct cache modification is unsafe. Only native uv writes the new cache;
the original failed cache remains intact. No ambient/home/other-session cache
access or cleanup. Existing data cannot currently seed an offline-only recovery.

## Explicit warm-up network boundary

The proposed grant permits only normal HTTPS GET/HEAD/range reads with TLS
verification, in the shadow preparation step:

- Canonical `https://pypi.org/simple/<normalized-name>/` metadata for the 26
  original lock names. Listings may mention other versions; that is not
  permission to select upgrades or download their payloads.
- PEP 658/714 `.metadata` sidecars for exact locked-version artifacts from
  official `files.pythonhosted.org`; validate advertised metadata hashes where
  supplied and retain URL/digest provenance.
- Where necessary, reads of exact original locked wheel/sdist URLs on that host.
  Complete payloads must match original lock hash/size. Range reads are metadata
  acquisition, not proof of a full payload hash. No sdist execution/build.

Names: anyio, ast-serialize, attrs, certifi, cffi, colorama, h11, httpcore, httpx,
idna, iniconfig, librt, mypy, mypy-extensions, outcome, packaging, pathspec,
pluggy, pycparser, pygments, pytest, ruff, sniffio, sortedcontainers, trio and
typing-extensions. Exact versions/artifact URLs come from the original lock.

No registry writes/auth changes, SDK/Git fetch, Python/tool download, Nix
realization, new backend package, alternate index or unrelated package. Native
uv has no per-URL allowlist flag: retain native request diagnostics and enforce
or report scope through existing supported execution controls; do not pretend a
CLI flag enforces an allowlist. An unexpected package/version payload request,
resolution failure or graph/hash drift stops for lead assessment. No fallback
install, speculative retry or pruning of newly observed artifact fields.

## Existing bundled backend is sufficient

The exact project declares only `uv_build>=0.13.0,<0.14` with backend `uv_build`;
selected uv 0.13.1 satisfies this unchanged requirement. Its native
`build-backend --help` exposes PEP 517/660 hooks. `uv help build` documents direct
bundled execution unless `--force-pep517` is requested; lock help identifies the
bundled backend as part of the uv executable.

Upstream 0.13.1 `check_direct_build` checks backend name, the single normalized
uv-build requirement, compatible version range and relevant exact constraints.
`uv-dispatch` invokes the compiled backend using uv's version. Current project
metadata is static, with no backend-path/extra build requirement. Keep injected
incompatible build constraints and force-PEP517 overrides absent. Later approved
build/editable work uses native uv; this recovery does not introduce
`python -m build`, standalone generic-Linux backend or disabled build isolation.

Source output `/nix/store/333bc8b8hy5hi5daspz9znrfb1rr1dnp-source` is absent.
That does not prevent using the qualified binary's compiled backend. Owner1's
retained full graph binds uv derivation
`6d86y4rv2glbbzkj7y90d3qq2i488v6z-uv-0.13.1.drv`, source derivation
`5knqg1f7k1gsj95rklcrxs6g2ajj4rng-source.drv`, source output and NAR hash.
No source fetch/realization or separate uv_build package is needed for the Ruff
metadata miss. This is source-supported selection, not an executed backend test.

## Owner0's one new attempt

Require successful offline shadow proof and an explicit new-attempt grant before
one more `make version VERSION=0.30.1`. Preserve the original failure and its
one-attempt marker. Create a new attempt receipt/launcher binding; do not reset
the marker or invoke the original pre-version-only driver unchanged.

Preflight proves all 775 stopped-source bytes, the partial12 digest, owning
branch/HEAD, empty index, unchanged refs/root/tool/Rust/Python locks and CHANGELOG.
Owner1 is command-free; exact cache/tool/runtime inputs match the shadow proof.
The launcher may select the proven new own cache and supported safety/config
controls, but retains `UV_OFFLINE=1`, exact Python and
`UV_PYTHON_DOWNLOADS=never`. No hidden online fallback on the patch. Rebind the
guard to the partial state; the original guard expects pre-version source.

Keep normal Makefile/Rust environment. Existing substitutions are idempotent;
repeating them on the twelve 0.30.1 files is intentional, with no reset/revert.
Native uv must produce the approved shadow lock bytes, then the target updates
remaining gemspec/example requirements and tracked Rust lock. Select an existing
own temporary directory instead of absent `/build`, recording this session-only
environment correction.

Afterward prove only the accepted 18 version paths/fields differ from original
source, with root/tool locks and external Python/Rust graphs preserved. Capture
all source/head/index/refs evidence. Only then apply the lead's approved CHANGELOG
with the actual preparation date and yield stable19 state for planned setup,
quicks and final review. A failure preserves effects and stops; no automatic
retry/lock repair/publication. Cache preparation does not expand product review
scope; existing metadata-only candidate gates remain.

## Read-only evidence

Accepted [version facts](release-version-sensitive-verification.md),
[integration brief](integration-backport-release-preparation.md), immutable stop
receipts, actual pyproject/lock, selected uv help, and repository Python
CONTRIBUTING guidance. Versioned official sources:

- [Bundled backend](https://github.com/astral-sh/uv/blob/0.13.1/docs/concepts/build-backend.md).
- [Cache safety](https://github.com/astral-sh/uv/blob/0.13.1/docs/concepts/cache.md).
- [Selection predicate](https://github.com/astral-sh/uv/blob/0.13.1/crates/uv-build-backend/src/metadata.rs#L257).
- [Native dispatch](https://github.com/astral-sh/uv/blob/0.13.1/crates/uv-dispatch/src/lib.rs#L676).

Only source/documentation/help reads occurred. The official website returned
403; its versioned official GitHub documentation was readable. No lock, cache,
application, environment or registry mutation occurred during design.
