# Actual deployed511 source and package lineage

**PASS, read-only.** Guest `/run/current-system` and the applied envelope both
identify `xlwlsjk1g7l392r5ks7lhpa32lnqp1ar`; applied pending is null. Canonical
vpsAdmin is clean at59d762308c87328fbae5e6829fd2a6750181be6d/tree86cb6727, with
full effective+packaged lock3f0fefc45195191e905bfa73b455a27d5540a59d2fda002eb5142f3351c01131.
This binds the parent-authoritative public update0 to installed code. E3 owns
route/logging/OAuth/protected client/config/restart/browser acceptance separately;
this receipt does not claim those operations or gate E3.

Actual applied services system:
`/nix/store/xlwlsjk1g7l392r5ks7lhpa32lnqp1ar-nixos-system-vpsadmin-services-26.05pre-git`,
deriver `/nix/store/pyssp4xnwg3rhsv9aklyxx4jq59mzcjq-nixos-system-vpsadmin-services-26.05pre-git.drv`.
Applied source configuration is
`/nix/store/x83skc93f5wlrdb94yjj6p3zi7h80xxa-os-test-vpsadmin-devcluster-2026-10-24-vpsadmin-haveapi-upgrade.json`;
its recorded SHA256 isf709c2378032a9ae50349fec05e1ed4082cd0d1f571e9b2c79e3fea9c7fd1093.
E3's [applied observation](../../../devcluster/m8-runtime/applied-services.json)
and [public status](../../../devcluster/m8-runtime/public-status-after-parent.json)
are reused; public status was running/ready with React2e32. Applied and selected
configuration remain distinct concepts; direct read-only guest system proof
matches this actual applied system. Observations have exact UTC timestamps.

Actual API is
`/nix/store/4g69p9i4578sqpnwpyrbw4gz2irkiiy3-vpsadmin-api-59d762308c87328fbae5e6829fd2a6750181be6d`,
deriverzzba29wal0cbcqf8yv8kibh3xv3jy30i. Its system API unit selects this path.
RubyEnvxxgpk5r6anlpwzzdcdldzbngmq9wv8q9 and wrappedRuby0flh63hi1biav1nlizj0knrs1y9x5sd0
use actual native Ruby3.4.9/Bundler2.7.2. The five HaveAPI511 actual outputs differ
from isolated test outputs and are proved independently:

| Gem | Actual installed output prefix |
| --- | --- |
| Server | pmjxjvwknc0n3ihjcbgp253hhi4169qq |
| Ruby client | 7afr9ps53j3lb2z7pq0qv65dhg6yplwa |
| Go generator | vdxg0v90qvj5h7f5rdm8mqmvv9knk5hy |
| Rust generator | fqm281nblalpg9abcq26s31q66dxyar2 |
| TypeScript generator | 6m5rhgdsi6rf9qml2259ykm8j4jn2jfj |

Full paths/derivers are in [actual five-gem graph](five-gem-graph.json).
All five select exact5114746f3a9f87e91c704147c0d99dd4f0d32f02/tree5b9c52,
same FOD8lq and normalhash090cwkg4i8r8s1nwlx1yf73v62i05dxwsd4ah1da9y54kk2gj0by.
Their complete shared checkout/cache bytes/modes/links agree across13,356overlaps;
only two designated indexes absent; Gitobjects/HEAD/nested metadata/CLI retained.
[Actual output boundary](actual-five-output-boundary.json).

The actual deployed wrapper was executed read-only on the host: all five loaded
library paths and real nested specs, Fiddle, frozen3f0f lock activation (declares
Bundler4.0.23, actual2.7.2),13docs/assets and nine source library hashes pass.
No fetch/restaging/runtime shim. Canonical CSS7c4ba935… and JSff3530e2… match.
[Actual installed proof](actual-installed-package-proof.json).
Read-only public services SSH independently checked29guest file hashes: actual
wrapper, frozen lock, five specs, libraries and assets all match those host
outputs. [Guest immutable file binding](guest-installed-hashes.json).
Guest Ruby execution is not claimed: earlier stdin/argument transport attempts
produced no parseable proof and their diagnostics remain private. No credential
or product failure is inferred from that receipt framing.

The normal source filter excludes218tracked paths belowtests directories. All
2,955retained input bytes/modes/links equal canonical59d. Actual installed API and
plugin source matches1,858tracked files, accounting for seven exact interpreter
line substitutions with all remaining bytes equal. Installed API revision file
is59d; runtime config/plugin symlinks retain normal install behavior and private
config values were not inspected. Build-only byni source output is currently
absent; no cause or rebuild is claimed. Its exact derivation, existing filtered
input and actual installed files establish the recorded lineage.
[Source binding](source-lineage.json), [canonical identity](canonical-source.json),
[API unit binding](system-api-unit-binding.json).

Complete deployed system graph6205nodes and closure1482paths are retained privately
outside tracking, with exact paths/SHA256 references in
[graph receipt](five-gem-graph.json), [closure receipt](actual-package-paths.json)
and [private evidence manifest](private-evidence-manifest.json). No duplicate E3
graph campaign ran. Guest persistent applied GC root resolves exactlyxlwl;
existing host result-config and maintenance roots retain this applied closure.
[Root binding](roots-binding.json). No roots were added, changed or removed.

Isolated acceptance APIgz0d/config1wdy/34passes keep their test labels. They are
not presented as these actual native outputs. Source comparison and focused
actual output/load/hash checks prove deployed identities. No rebuild, test,
HTTP/browser request, source edit, guest/config/restart/provider/client mutation,
CI, cleanup, default integration or lifecycle action occurred. All read commands
ended; no source writer remains. Remaining live acceptance belongs to E3/lead
under existing dev-deployment authorization.

Raw argv/environment/socket/updater/applied/status/graph and failed-probe data
are0600 in dedicated0700 `/tmp/vpsadmin-m8-a0-diagnostics-k7onkp4a`, outside
portal-served tracking; only redacted facts and hash references are here.
[Compact final summary](summary.json).

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
