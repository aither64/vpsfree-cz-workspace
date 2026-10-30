# Native CI prebuild: source fetches rejected with HTTP 429

Run [40133879811](https://github.com/vpsfreecz/vpsadminos/actions/runs/40133879811),
attempt1, exact head `75836892e5d446d7c1f76411654a4c1809ceb3a0`.
Failed job `Run test suite`, job120996309735. GitHub API metadata was read first.
Selected only native artifact12577327649, `os-test-logs-40133879811-1-native`:
55,941 compressed bytes, SHA256
`7cabade3313d7451ad61e3f22af672f9da394adff81c2d01927d003bd14817e3`,
matching the API digest. Its only members are
`prebuild-20261024-2931410-1htplc/build.log` (176,156 bytes) and `test.log`
(11,078 bytes). Those two members alone were unpacked, as
`prebuild-build.log` and `test.log`. No state/image or other artifact retrieved.

The first causal failures are two fixed-output Linux source archive downloads,
not evaluation errors or runtime assertions:

- `prebuild-build.log:1454–1474`: both fetch derivations start, trying
  `https://github.com/vpsfreecz/linux/archive/<revision>.tar.gz`.
- Lines1553/1556: HTTP429; retries at1/2/4seconds are exhausted at1850–1854.
- Lines1940–1968: archive1dfea587406b7dd79973831d1677fb2418e5e9aa fails;
  lines1969–1997: archivea770f5086fc500ca258852aea1cb3e209a342d2b fails.
- Lines2003–2038: downstream Linux config6.12.113, selftests6.18.49,
  system/test JSON and aggregate prebuild dependency failures. Line2039:
  `Preparation build failed (1)`. There is no VM/runtime result.

The selected revision's official source confirms the identities:
[available-kernels.nix](https://github.com/vpsfreecz/vpsadminos/blob/75836892e5d446d7c1f76411654a4c1809ceb3a0/os/packages/linux/available-kernels.nix#L8)
lines8–11 select6.18.49/a770...; lines47–49 select6.12.113/1dfea... with
flat archive-byte hashes. [packages.nix](https://github.com/vpsfreecz/vpsadminos/blob/75836892e5d446d7c1f76411654a4c1809ceb3a0/os/packages/linux/packages.nix#L13)
lines13–25 construct the GitHub archive URL; both normal and builtin-ZFS paths
use it (line43). [default.nix](https://github.com/vpsfreecz/vpsadminos/blob/75836892e5d446d7c1f76411654a4c1809ceb3a0/os/packages/linux/default.nix#L33)
lines33–36 use `fetchurl` with that pinned byte hash. Exact files are retained
as `source-linux-*.nix`.

Classification: remote dependency-source retrieval/rate limiting during
realization. Cache substitutions elsewhere succeed (e.g.1538–1547). These source
fetchers were selected for building, but this does not establish global cache
absence, a broken substitute service, hash mismatch, compiler failure or any
kernel/test product defect. No evidence identifies the server's rate-limit
scope or proves an alternate endpoint would succeed.

Smallest remedy recommendation for the lead: make these exact pinned archive
outputs available through the existing trusted source/cache publication path,
then verify the fetch-only boundary before another whole-suite selection.
If an owning source change is chosen, keep it confined to the kernel source
fetch route and preserve immutable revisions/integrity; verify any official
codeload/mirror archive against the existing flat hash before adopting it.
Do not blindly replace `fetchurl` with `fetchFromGitHub`: unpacked-tree hashes
and source derivation identities differ. No retry, endpoint probe, cache query,
publication, application edit or build was executed by this investigation.

All artifact download+unpack is243,175bytes; retained logs187,234bytes, well
within128MiB transfer/unpack and16MiB log caps. Three small exact source files
were retrieved separately through the official GitHub contents API. API/run/job
identity was observed; credentials and redirects were not printed.

## Retained file SHA256

- `artifact-12577327649.zip`: `7cabade3313d7451ad61e3f22af672f9da394adff81c2d01927d003bd14817e3` (55941 bytes)
- `artifact-members.txt`: `a3034fa041c2ed6b4003125b3eca16d6ab21ee8a2e6573c5044336060b691fc7` (76 bytes)
- `prebuild-build.log`: `ea50da6549ad12221fc8c47544a45b830debd6020153305fce154302025120f7` (176156 bytes)
- `test.log`: `17f3d3c48d203085a744c851a88f0da41e295080ac40b3ddc50f5b8302654770` (11078 bytes)
- `source-linux-available-kernels.nix`: `2817e6d9327282b269e2b6e360880adbfd956ae2ac7eca3f49c86c1644b64ea5` (3491 bytes)
- `source-linux-default.nix`: `f73337319bad9312ae26d1152fd366317559371a7ac94a554dbbfc94255dac94` (1028 bytes)
- `source-linux-packages.nix`: `1533bc976de1800a9fd769ba42bc17616b11e54e3de6d214c838bed61ad7312e` (2943 bytes)
