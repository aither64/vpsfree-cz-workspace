# C3 review input — npm 0.30.2

Current source is a bounded release-identity refresh over the independently
reviewed C package and lead-verified R2 correction. Read the accepted architect
2026-10-26 C3 addendum, session plan/state and original source/migration packet.
New exact two-commit head and quick-check receipt will be filled after completion.

Repository/worktree: vpsfreecz/vpsadmin-webui,
worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui.
Own branch dev/vpsadmin-haveapi-upgrade, target main.
Base 5a2d2bdc3ad7a827038f877d75959916528db844.
Old reviewed/R2-closed range ends014f7b9c9f451d6275af73c4af30a24668b77b7b,
retained exactly at refs/heads/dev/vpsadmin-haveapi-upgrade-reviewed-0301.
Previous original final review head39f8fd7d and R2 diff/67-case checks remain
in preserved receipts. Old final packet/map/series copied to old-reviewed/.

The final dependency stream must introduce exact registry0.30.2 directly from
base with manifest/lock/provenance/normal frontend npm hash and existing source
security checks. Production adapter/test/docs stays in a separate logical
commit, with current docs aligned and a dated0.30.2 record. Preserve carried
source author and both original author dates. Old0.30.1 dependency/source is
review evidence, not an intermediate commit retained in the final series.

Only package dependency/lock, provenance/hash and docs changed from014f7b9c.
`src/`, source-security scripts, all adapter/R2 tests, domain behavior, current
node/member changes, typed E2E union, BFF manifest/lock remain byte-identical.
Package-source guards already derive selection from the provenance record; no
new fetcher, codec, client fallback, pilot/toggle or vendor tarball. All53 npm
packed files match HaveAPI321ce825 source; package.json+bundle versions alone
differ from0.30.1. Installed files match the verified registry archive as well.

No migrations: no schema, persisted format or wire protocol changes. Neither
old reviewed C nor this branch is merged/released/deployed/externally consumed.
No supported consumer boundary requires obsolete pins. Current app/R2 behavior
and original current-main overlap reconciliation preserved; base unchanged after
fresh remote check. PR74 still5dd2333b/PR63 untouched; own remote branch absent.
Source reconstruction from nonancestor old8772bab remains content provenance,
not literal merged ancestry. No pushes, merges, deployment or lifecycle actions.

Overall inherited risk remains high because authenticated request/mutation
boundary is present in the whole branch, though current new delta is version/
provenance/docs only. Lead selects retained reviewer and applicable affected
lanes under mandatory-change-review. Earlier review is evidence for unchanged
source; this refresh needs final exact identity/history acceptance. Preserve
original report rather than claiming upstream bytes/performance already reviewed.

Actual new release provenance is npm0.30.2 at source
321ce8256ad4704efaed04f4f2aa1ea4c2a3b4b8, tagv0.30.2,
.github/workflows/release.yml run40238928168/attempt1; SHA256
e6fc12590ebabd05b09d579cfcd62344bf60dfa0b3b05b3c75d7015e2bd5cbfa.
Npm integrity/attestation/source-file proof in adjacent metadata and Markdown
receipt; source-check behavior does not independently verify signatures/network.
Exact transitive xmlhttprequest1.8.0 and unrelated root/BFF graph preserved.
Root new npm hash sha256-sY3OQDFdisOzhJO4dhwlsjvGxlhog8crhqU3tHcI4IY=.
Setup passed under fresh policy Luna/low watcher in38s; no package build run.

Fresh quick acceptance runs installed declarations plus original adapter/auth/
public/error/abort/timeout tests, R2 uncertainty/shared no-duplicate guards,
package-source tests and full ci:quick, production audit/signatures. Exact results
will follow; do not substitute historic0.30.1 tests for these actual package runs.

After independent committed review: full unit suite, production build, Nix
frontend/provenance/source/package checks and ordinary desktop/mobile browser
fixtures (public overview, authenticated home, renewal/expiry, failures and VPS
action state). None started here. Live API/OAuth and separate server performance
R1 remain independent gaps; npm0.30.2 identity alone is not server acceptance.
Current provenance/package docs and dated work-log are developer-facing English;
no member-facing UI/catalog or BFF text edits.
