# HaveAPI 0.32.1 adoption: final review packet

Clean candidate `0542293102dd1e381d7db785cbccf9a7c65075c9`, tree
`d54d5898c5eba5a45a450ec2613f2d62a1250dba`, is committed and quick-green.
**Source writer released. Stop for lead-assigned retained reviewer0 affected
all-four-lane review at HIGH risk; no publication/integration/long phase yet.**
Session2026-10-24-vpsadmin-haveapi-upgrade, aliasvpsadmin-oauth-client-logs,
worktree `worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-oauth-client-logs`.
A0 design7573 plus runner companion and finite quicks govern this package;
lead accepted CLI literal alignment and applied the context-owning prose pass.

## Complete range and behavior

Actual new base `610a96f8ce523afbcd3e4374a70047dbe3264b0d` to candidate054229 has
**one coherent commit**: `api: adopt HaveAPI 0.32.1 documentation switching`,
authorJakubSkokan<jakub.skokan@havefun.cz>. [Full history](complete-history.txt),
[final diff](final.diff), [stat](final-stat.txt), [commit/authorship](commit.txt),
[exact identity/hash binding](final-proof.json). Ten paths, +54/-50:

- `api/Gemfile`, generated `packages/api/{Gemfile,Gemfile.lock,gemset.nix}`:
  five aligned server/Rubyclient/Go/Rust/TypeScript gems0.32.1 and minimums
  `~> 0.32.1`. Only these specs/constraints/artifact hashes change.
- `api/config/api.rb.example`: literal
  `switch_user_revoke_params: { 'close_sso' => '1' }`, alongside unchanged
  `switch_user: settings.fetch('switch_user', false)`. No new JSON field,
  provider/backend, failure fallback or ordinary logout behavior.
- `tools/api-schema-export/{Gemfile,runner.rb,cli.rb}`: selector/exactpin,
  equality guard/error and help all0.32.1. Exact refusal semantics preserved;
  no widened version layer, exporter or DB execution.
- `docs/api-client-examples.md`, `docs/api-schema-export.md`: same version,
  SSO closure/other authorization tokens remain valid, paired hook/API rollback
  retaining private client config/session key. Lead-authored replacements and
  approved final hashes were applied exactly. Generic fixed3600/no-refresh
  example stays; site-specific renewable900 belongs to E1's operator guide.

The dependency and hook must ship together because0.32.0 rejects the new option;
the exporter must follow the API declaration. These generated/source/doc changes
are one usable adoption, with **one final five-gem dependency stream** and no
repeated pins/fixups/reverts/obsolete transitional approach. PHP/npm/generalclient,
download-mounter/outage-report packages, models, CI workflows and manifests are
untouched. No private credential/config access, rotation or host action.

**NO MIGRATIONS:** no migration/schema paths or new persisted format. Keep
private settings/key on paired hook/API rollback; it restores the old switching
limitation. Defaultfalse remains. Accepted producer semantics keep the map inert
when disabled and add it only to validated switch-user revocation after existing
capability/Origin/CSRF checks; ordinarylogout/authorize/token/state/PKCE semantics
stay unchanged. AssociatedSSO closes; other authorizations' access tokens remain
valid. Actual provider/SSO behavior is producer evidence, not our constructor proof.

## Actual baseline and preserved history

Fresh canonicalSSH readback found ownfeatureclean0f/master610, not expected0f.
The sole upstreambotcommit changes BUNDLED_WITH4.0.23→2.7.2 in API/client/download
locks, no gem/runtime changes. Lead expressly approved ordinary FF of ownfeature
0f→610. Native33415exit0 and actualpostmergehook successmarker verified.
[Baseline](baseline.json), [original drift](upstream-drift.json),
[FF output](baseline-ff.log), [merged provenance](merged-provenance.txt).
The seven accepted/merged0f commits and upstreambotcommit remain literal;
no merged history/default was rewritten. Review base is610; previous review,
source/input/runtime/CI evidence remains scoped to its original heads.
Own same-session refs are preserved except ownfeature's ordinary610→054 advance.
One unrelated shared-clone branch/remote-tracking ref moved concurrently;
metadata-only observation was retained, never changed or investigated by E2.
[Ref reconciliation](proof-inspector-reconciliation.json). Live33d6/private/roots/
recovery refs/original updater3922 remain untouched. No merge claim acquired.

## Release artifacts and finite quick evidence

Actual producer releasev0.32.1/source9efeadf91d894e01d1d4f4a3e3fc64c6309785c7,
workflow41333460242, was supplied by lead. MasterVERSION0.32.0 is producer policy;
we select actual stable/tag gems0.32.1. [Authorized handoff](../haveapi-0321-handoff/published-release.json).
Public manifest SHA25637d48672acfbef768f10bb1b86787880a215056b5dc092e48ee8b6db348abe0d
and all five actual RubyGems bytes match manifest+handoff exactly:
[release binding](release-binding.json), [artifact acquisition](artifact-download.json).
Actual server README/guides/schema/assets and all generator entrypoints inspected;
selected installed library/doc member hashes match all downloaded packages:
[packaged content](artifact-content.json), [installed binding](installed-content-binding.json).

Lead-relayed producer scope: both independent reviews clear,152focused/tagged
release checks pass, conventional isolatedinstall/explicitactivation/require and
154actualHaveAPIloadedfiles/constructors pass19s. No peer files/team access or
duplicate producer installation/test campaign. Our consumer proof is separate:

- **Native18914exit0:** declared API shell, `VPSADMIN_PLUGINS=all`, frozen
  generatedAPIlock,122gem bundle. `bundle check`, requireallfiveentrypoints,
  actualversions/cacheSHA0.32.1 and DocumentationOAuthfalse/true constructors
  with the literalclose_sso mapPASS. Ruby3.4.9/Bundler4.0.23.
  [Actual paths/lock/gems](consumer-load.json), [check source](consumer-load.rb),
  [native output](consumer-quick.log). NoDB/spec/bootstrap loaded or invoked.
- **Native15139/22218/54616exit0:** existing API Gemfilewriter only, targeted
  conservative bundlelock on five names, nativebundix-l/nixfmt. No broad
  rakegem task or wholelock deletion. Unrelated gem specs/dependencies exact;
  gemset changes exactlyfive and nativehashconversion matches the publicbytes.
  API BUNDLED_WITH2.7.2→4.0.23 is nativegeneratedtoolmetadata only. Client/download
  locks remain byteequal610/2.7.2. [Semantic proof](quick-result.json),
  [lock output](targeted-lock.log), [gemset output](targeted-gemset.log).
- **Native84012exit0:** six changed Rubyfile syntaxchecks, gemsetnativeparse,
  scopedAPIconfigRuboCop anddiffcheckPASS. ToolGemfile/runner/help and bothdocs
  reference0.32.1 consistently. [Output](metadata-quick.log).
- **Normal commit25114exit0:** Nixfmt/MigrationSpecs/WebUIi18n/RuboCop/APIi18n
  and commit-message hooksPASS; no hook/signature bypass. One advisory>72bodyline
  meets80columnrule. [Hooks](commit.log). Exacttestedpatch equals committed610..054
  bytes SHA256e5e9b05cfa39f5af827a42074af61d643ad8dec5881b3b0121fa326464d1316b;
  finalsource/indexclean andfullrangediffcheckPASS. [Prose hashes](lead-prose.json).

**User QUICK-ONLY:** no services-up/system/package realization/fullAPI/foundation/
browser/PHP/client suite, schemaexport/DB, realprovider/login or cluster operation.
No longcheckphase follows this quick batch. We do not certify installedservice,
VMorrealprovider behavior from these checks. No implementation test failure or
retry occurred; the baselineguard stopped before edits and resumed after explicit
lead disposition. Native tools downloaded only the five targeted pureRuby gems;
no broad dependency upgrade/build/setup campaign.

## Review and remaining ownership

Retain reviewer0Sol/xhigh/read_only for general,architecture,scope/proportionality,
risk/compatibility atHIGH: exactfiveartifact/input identities, sample/version
contract, bounded toolguards/docs/rollback, fullonecommitnewhistory, one final
update stream and NO MIGRATIONS. Review is required despite quick-only scope.
No feature/default push for054 yet. After accepted review, lead releases normal
publication/integrationpreparation; prior0f merge approval does not silently
cover this follow-up. E1 committedhook/spec waits for final reviewed/published
productSHA before one channelpin. E2 did not edit site/pins.

All package-localfetch/readback/generation/load/quick/commit handles consumed;
sourcewriterreleased. Original89033 alone owns prior0f/master integrationCI41291451427
(last saved8success/oneinprogress/errors0); no addedquery/observer/control here.
Priorfeaturefourgreen/historicalfbd500unexplained remain their original scope.
No claims/defaultmerge/deploy/PR/lifecycle/cleanup authority. Session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
