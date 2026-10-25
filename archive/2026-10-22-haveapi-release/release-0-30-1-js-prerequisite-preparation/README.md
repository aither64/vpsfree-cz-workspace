# JS prerequisite inventory, preparation only

Both bounded same-session caches expose native URL keys for all 214 locked
packages applicable to Linux/x64/glibc. The owning patch lock has 239 external
records, including 25 inactive platform records. All external records are exact
matches to the prior successful profile setup; only local package version fields
changed from 0.30.0 to 0.30.1. Current input copies and full records are retained
here. Architect0 owns the supported setup design; this inventory authorizes no
installation or compiler action.

The tighter candidate cache is
`haveapi-client-example-profiles/clients/js/test/tmp/profile-npm-cache` under
this session's worktree group. Its prior normal locked `npm ci --ignore-scripts`
succeeded, and today's native `npm cache ls` reports exactly 214 keys. The second
declared cache, `haveapi-dependency-refresh/clients/js/test/tmp/npm-cache`, has
249 keys and also matches all 214 applicable URLs. No other-session or ambient
cache was searched. Before/after byte, size, mode and mtime inventories match for
both caches; their 430 and 501 files remain unchanged.

The selected tools are retained Node 24.21.0 and npm 11.19.0. Their exact binaries,
source, derivations, outputs and complete retained input graph are bound in
`selected-native-inputs.json`. Native cache listing was invoked through the exact
Node binary and selected npm CLI, offline, with empty own configs, update checking
disabled, and logs directed to a new absent session directory. npm's installed
source shows that `logs-max=0` still invokes log cleanup; the absent log directory
prevented touching retained logs. Neither absent log directory was created.

TypeScript is exactly 6.0.3, resolved from
`https://registry.npmjs.org/typescript/-/typescript-6.0.3.tgz`, integrity
`sha512-y2TvuxSZPDyQakkFRPZHKFm+KKVqIisdg9/CZwm9ftvKXLP8NRWj38/ODjNbr43SsoXqNuAisEf1GdCxqWcdBw==`.
Its URL key exists in both caches. Its retained installed package declares no
runtime dependencies or install lifecycle hooks and contains no native `.node`
files. The two retained installed copies have equal package/compiler hashes.
Those are inspection facts; no installed files may be copied into the patch.

`npm cache ls` proves native key presence, not freshly exported archive bytes or
full archive integrity. No private cache format was decoded, repaired, merged or
seeded. A later authorized native offline install must read its normal cache and
validate every selected original against the owning lock integrity. A cache miss
or integrity failure stops; no online fallback or alternate version is prepared.
No missing official locked URL was observed at the native key level.

`setup-command-candidate.json` records a disabled ordinary offline `npm ci`
candidate in the actual owning JS directory. It is input to architect0's brief
and lead routing, including explicit cache-write boundaries. It is not an
executable grant or an approved driver. No setup watcher, install, pack, build,
compiler, test, application require, network or Git command ran in this step.
Only session evidence/config files were written. Existing source, locks, dist,
native environments and accepted acceptance packets were left unchanged.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
