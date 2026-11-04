# Affected packaging review

Completed committed followup1ab9853312a95b5448e99fd6f83f846453de17a5..
7cad7ffb3a0a294c30349680e2eb4f80c63a3926, clean WebUI worktree. Same retained
reviewer0 saved Astra/xhigh/read_only, all four lanes applied only to this new
packaging adapter and its interaction with reviewed unpublished SDK mechanism.
No full whole-migration re-review requested. Prior final review/findings/remedies/
history are in webui-final-review-result.md and state. No DB migrations.

User explicitly wants temporary unpublished SDK consumption without releases.
Ordinary clean npm ci/ESM/policy, full BFF58/unit2227/Vitebuild pass. Nix FOD and
canonical lock cmp passed, but actual frontend package failed npmConfigHook:
pinned --map-cache maps registry cache only; --fixup-lockfile requires hash for
every resolved+integrity dependency including local SDK and panics. Failure:
webui-nix-packages.log/result.md. No package pass claimed.

Architect wrote selected correction before implementation in design.md.
Five files: packages/frontend.nix, scripts/check-package-source.mjs and tests,
docs/design/PACKAGING.md and migration worklog. Frontend-only supported
npmConfigHook override delegates all prefetch invocations/failures to upstream.
After successful --map-cache only, existing checker validates actual archive and
manifest/lock/provenance, computes SHA512 and adds exactly canonical SDKresolved
to transient CACHE_MAP_PATH; reject conflict/invalid/missing/tampered input before
write, preserve remote entries and idempotence. Unchanged upstream fixer/offline
npmci then run normally. No copiedhook/Rustpatch/skippedconsistency/cache-index
writer/secondlock/new pipeline.

Quick checks:12sourcechecker tests, Nixparse, selected customfrontend and original
BFFhook evaluation; actual pinned fixer with explicit478remote fixturemap entries
plus checkedlocalSDK passes on disposable canonical lock, byte-identical lock
SHA256585e8f48b194d8165731ca546fb709c94d531ee48224de9fff805416cb8b0f8e.
Docs177/76requirements pass. Fixturemap proof is not actualcache/fullbuild proof.
Previous unrooted6ri cache absent now; eval expects same output/hash but no new
package success inferred. Real Nix graph rerun waits this review. Detailed exact
protectedinput proof in webui-nix-map-fix-receipt.json: original SDK archive,
canonical rootlock/provenance/runtime/BFF/app inputs unchanged, no reinstall.
No generated SDK/G/API behavior/source change, npmDepsHash remains utOpabP...

Read mandatory-change-review skill and allfour references, source plus exact
pinned upstream hook/Rust as useful. Assess correctness/failure propagation,
scope, map/lock trust and frontend-only ownership; do not rubberstamp. Return
concrete severity/lane/file findings, no source edits/build/test/DB/browser or
nested agents. This is affected final review of a new mechanism not covered by
original review; retain all unaffected prior conclusions. Later overall history
consolidates integration fixes while preserving source/evidence, no repeated pin.
No default merge/tag/npmrelease/deploy/session lifecycle authorized.
