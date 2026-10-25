# 0.30.1 release-test compiler prerequisite

Frozen proposal, 2026-10-24. Architect0 owns this contract; lead accepts the
execution packet, owner1 prepares the owning npm dependencies, and owner0 owns
the subsequent maintained release-test continuation. This is dependency setup,
not a product change or a new build campaign. No setup or check was executed by
the architect.

## Decision and supported input boundary

Prepare the existing JS lock with ordinary **offline `npm ci`**, including dev
and platform-applicable optional dependencies, with lifecycle scripts disabled.
Use only an opaque copy of the qualified same-session npm cache. No network is
needed for the proposed attempt; native cache extraction still has to verify
the original payload integrity.

`utils/release/artifacts.rb:276,296` fixes both the compiler executable and its
accepted standard-library realpath to `clients/js/node_modules/typescript` in
the owning checkout. There is no compiler-input ENV seam. The examples at
`utils/release/spec/release_spec.rb:359,365,370` exercise the real compiler for a
valid installed consumer, a missing transitive declaration, and a declaration
escaping the installed package. Their existing `stub_npm_install` extracts the
fixture instead of invoking npm install; Node and TypeScript remain real. Do
not alter that fixture, its guards, or the compiler invocation.

Only the TypeScript package is directly needed by these examples, but there is
no supported single-package locked preparation operation here. The selected
npm 11.19.0 `docs/content/commands/npm-ci.md` explicitly says that `ci` installs
whole projects, cannot add individual dependencies, and never changes the
manifest or lock. Its `lib/commands/ci.js` validates the owning lock before
reifying it with `save: false`. The repository's `Makefile:51` declares precisely
this owning `npm ci` dependency preparation. Select that JS operation alone;
do not run the full `release-deps` target or shell install hooks.

Manual compiler extraction, copied installed `node_modules`, arbitrary global
compiler symlinks, a scratch package/lock, and `npm install typescript --no-save`
are outside this contract. The cache contains original package inputs; it is
not an installed/native closure borrowed from another worktree.

## Frozen evidence and physical inputs

The owning checkout is
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-0-30-1`,
branch `2026-10-22-haveapi-release-0.30.1`, HEAD
`8591394e13144431b27ecb366aae2b7b77a94e2c`.
Its 19 intended metadata/changelog changes remain uncommitted, the index is
empty, and its complete 775-source-file digest is
`e1af270d30ae6800c56556600b016a13dc67dcb49642b8401a5219614ae8baa7`.

Preserve the original stopped evidence under
`release-0-30-1-stage2-tmpdir-recovery-20261024T124000Z/`:

| Evidence | SHA-256 |
| --- | --- |
| `terminal-stopped-receipt.json` | `f390398def757d36cbc2aa5cc2cd062da344a2e52239a9da2b53c9a9c1e79af9` |
| `terminal-evidence-manifest.json` (117 files) | `47e13b16508774f12f9366a595868aff4db3bcf87f6bd6a4ae128be0a9ff1e8b` |

That receipt records release-check PASS (0.631 seconds), followed by
release-test exit 2 (6.614 seconds), 170 Ruby examples / three compiler-path
failures. Python artifact tests were not reached. Owner0 already established
the absent owning node_modules prerequisite; no product defect is inferred.

Owner1's frozen inventory is
[release-0-30-1-js-prerequisite-preparation](release-0-30-1-js-prerequisite-preparation/README.md):

| Evidence | SHA-256 |
| --- | --- |
| `inventory-receipt.json` | `c693b635799d1fa62ab1f5407097971c6fc2c5b66920ffb2b288dd4d4bdec6a9` |
| `files-manifest.json` (20 files) | `91113216d03a19c33305a389f71b83697e5a80af0dbf5ff5e3d041dd25d529be` |
| `owning-graph-and-cache-inventory.json` | `3d77b26838030b58622f5644dbe007d8746d7f4fd9a1c69d42e4dffd6cd85725` |
| `selected-native-inputs.json` | `3d47973bd2d03c2aca34b2e04e88f723ef61fb48ed5f709e612a6b2227dadea4` |
| Owning `clients/js/package.json` | `508559d0003a2040c73720aa995f8cc8cc4a854babcd74153e95f622612a9197` |
| Owning `clients/js/package-lock.json` | `aa480e3357cfef14ba22bc74f1a7ac32e877edc355593f1fa3c0597e4a29560f` |

All 239 external lock records exactly match the qualified profile lock; only
the local root/package version changes from 0.30.0 to 0.30.1. There are 214
Linux/x64/glibc-applicable records and 25 inactive platform records. All 239
retain their original registry.npmjs.org resolved URL and integrity. Keep all
records in the lock; let native npm select the platform. The only lock-declared
install script belongs to inactive Darwin-only fsevents.

Use the already qualified top-level release tools and their complete retained
input graph, not a newly selected component shell:

- Node 24.21.0:
  `/nix/store/j1j9b0w3mhpccdli73ycj5w7nf6fkzqz-nodejs-24.21.0/bin/node`.
- npm 11.19.0 CLI:
  `/nix/store/kwnng131d6nb0k6vlrm2rr6q77m81ikp-nodejs-slim-24.21.0-npm/lib/node_modules/npm/bin/npm-cli.js`.
- TypeScript 6.0.3, exact URL
  `https://registry.npmjs.org/typescript/-/typescript-6.0.3.tgz`, integrity
  `sha512-y2TvuxSZPDyQakkFRPZHKFm+KKVqIisdg9/CZwm9ftvKXLP8NRWj38/ODjNbr43SsoXqNuAisEf1GdCxqWcdBw==`.

The preferred source cache is
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-client-example-profiles/clients/js/test/tmp/profile-npm-cache`.
Owner1's native listing found exactly 214 keys and all 214 applicable resolved
URLs; its 430-file byte/mode/mtime snapshot was unchanged. That is availability
evidence, not a fresh full-payload integrity proof. Do not inspect another cache
or reuse the secondary cache automatically.

## Owner1 setup package

After lead acceptance and the bounded setup grant, bind a one-shot packet to
the exact source, owning inputs, tool graph, inventory and this brief. Reuse
the qualified top-level environment without dependency hooks or new Nix
realization. Use a fresh policy watcher for the uncertain-duration install;
the parent gates its exact payload before execution. Architect runs nothing.

First copy the **whole source cache opaquely**, preserving its ordinary layout,
to the fresh owning destination
`<patch>/clients/js/test/tmp/release-0-30-1-npm-cache`. Compare the copy with the
frozen source inventory before native use. Refuse an existing destination or
unexpected preexisting owning node_modules. No parsing, selective cache
rewrites/merges, private cacache calls, `cache verify` garbage collection, or
source-cache mutation is part of the copy. Normal npm may mutate the copy.

Run the following argv from `<patch>/clients/js`, substituting only the two
exact tool paths above and the recorded new cache/log/config paths:

```text
<node> <npm-cli.js> ci --offline --include=dev --include=optional
  --ignore-scripts --no-audit --no-fund --no-update-notifier
  --cache <patch>/clients/js/test/tmp/release-0-30-1-npm-cache
  --userconfig <new-own-empty-user.npmrc>
  --globalconfig <new-own-empty-global.npmrc>
  --logs-dir <new-own-attempt-logs>
```

This is one command, not line-by-line shell execution. Owner1 records its
literal argv and qualified environment. Keep the normal hoisted install
strategy and peer semantics; remove inherited npm/Node/production-omit
overrides through the prepared environment, without changing HOME or project
configuration. Keep NODE_PATH and NODE_OPTIONS unset. No lifecycle scripts,
application loading, `npm run`, build, pack, compiler, or test command belongs
to setup. `--offline` means no network requests, unlike `--prefer-offline`.

Setup acceptance requires all of the following:

1. Native npm exits successfully with the original lock integrity enforced.
   Its normal extraction checks payload hashes; cache-key presence alone is
   insufficient. Do not suppress warnings or accept integrity failures.
2. The physical dependency inventory matches all 214 applicable locked
   path/version/resolved/integrity records with no extra packages and no missing
   active optional package. Compare native installed metadata/hidden lock to
   the recorded graph; do not edit it. An optional extraction failure can be
   tolerated by npm itself, so exit 0 alone is insufficient here.
3. TypeScript reports package metadata 6.0.3; bin/tsc and the complete compiler
   library are physically inside this owning node_modules. Static path/hash
   inspection is sufficient at setup. No compiler invocation is necessary.
   Normal npm-created .bin links are permitted; borrowed package links are not.
4. The original source cache and all protected source/metadata/locks/inputs,
   prose, hooks, tool roots and **all 47 retained dist outputs** remain exact.
   Retain the 775-file digest, intended 19-path diff, empty index and owner0's
   protected-ref proof. Allow only the new owning node_modules (including its
   native hidden lock), copied cache, and named session logs/config/temp outputs.
   Record before/after evidence; no new source or lock changes are allowed.

The installed npm docs support a selectable opaque cache and guarantee
integrity checking on extraction (`docs/content/commands/npm-cache.md`);
`node_modules/pacote/lib/fetcher.js` uses the requested integrity for cached
tarball reads. These checks use normal npm semantics, not a replacement cache
implementation.

## Failure and conditional official-payload boundary

Any missing/corrupt cache entry, graph discrepancy, unexpected optional omission,
tool/source drift or install failure stops this attempt. Preserve its logs,
partial owning dependencies and copied cache for diagnosis; do not retry,
delete, merge caches, switch versions or silently enable network access.
Lead assesses the concrete result before another attempt.

No missing official payload is currently identified and **no network fetch is
included**. If native evidence later proves one necessary, the smallest new
input scope is only the missing original tarball URL(s) already recorded in
this owning lock, over official registry.npmjs.org HTTPS, with the exact lock
integrity. Owner1 can propose native `npm cache add <exact-resolved-URL>` into
the new cache, then a separately granted offline ci attempt. No latest/tag or
range lookup, lock regeneration, audit, registry configuration/authentication
change, upload or alternate payload is allowed. A demonstrated need for
additional registry metadata must be returned with its exact purpose/endpoint
before broadening that input scope. This contingency is not a fetch grant.

## Owner0 maintained-test continuation

After lead accepts setup proof, owner0 binds a new attempt to the unchanged
source and qualified dependency output, preserving the stopped evidence and
the corrected ordinary temporary-directory boundary. From the owning root,
under the already qualified top-level Ruby/Python/Node environment, run only:

```sh
make release-test
```

The target runs all release Ruby specs, including the three real compiler
examples, then the previously unreached Python artifact tests. Preserve native
output and require both recipes to pass. This is the intended quick compiler
coverage, not a separate compilation campaign. The prior successful
`make release-check` is retained without repetition. No docs, JS build/full
suite, Go/Rust/Cargo/MSRV, CI or package rebuild is added by this recovery.

Recheck the same protected inputs and outputs after the test. A behavioral
failure reopens only its affected diagnosis/check/review boundary; it does not
authorize product edits or a broad verification restart. This prerequisite
adds no API, persisted-state, release metadata, deployment or mixed-version
change. Tags, publication and registry writes remain held. Lead owns state and
next routing; owner0 remains sole Git/source owner.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
