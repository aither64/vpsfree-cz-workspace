# Final consumer adoption and PHP mirror review

Session 2026-10-11-diagnose-vpsadmin-api-exception, workspace /home/aither/workspace/ai/vpsfree.cz; plan/design/state under /home/aither/workspace/ai/vpsfree.cz/work/2026-10-11-diagnose-vpsadmin-api-exception.
Requested outcome: consume published HaveAPI0.29.9 in vpsAdmin packages, guard
packaged documentation in services-up, update only configuration vpsadmin
channel/role, and prepare the normal PHP mirror's shared metadata. User owns
deployment. User approved HaveAPI/master and release, not these master targets.
All intended changes committed/pushed, worktrees clean, quick checks pass.
No long integration/host builds started; run them after this final review.

Retained reviewer0 Astra/xhigh/read-only, same independent reviewer, ready;
no model/effort overrides or fallback. Verify exact session binding. Read
workspace AGENTS/procedure routes, each local AGENTS (PHP has none), mandatory
review skill and all four lane references. Review all general, architecture,
scope and risk/compatibility lanes directly; no source edits, nested reviewers,
long tests or write-producing builds. Include explicit complete history,
consolidation and migration conclusions for each branch.

## vpsadmin
Worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-diagnose-vpsadmin-api-exception/vpsadmin
Base 8a50010f46ad134e132394f2159d031601c17778
Head 7d911899d0d3d335546f6b3676b2eb46a291764d
Feature branch 2026-10-11-diagnose-vpsadmin-api-exception; target master.
Complete series:
4d53979a35e0a362e0aa9ae99fbf8e1acd12d755 tests: check packaged API shared documentation
7d911899d0d3d335546f6b3676b2eb46a291764d packages: update HaveAPI to 0.29.9

Final diff: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-11-diagnose-vpsadmin-api-exception/vpsadmin-final.diff
## vpsfree-cz-configuration
Worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-diagnose-vpsadmin-api-exception/vpsfree-cz-configuration
Base e65ef2c4cd179dac2d96cfdfe6d6c6967f08d566
Head ad9830a53a34f169197ecb7a919b08a98a4493fd
Feature branch 2026-10-11-diagnose-vpsadmin-api-exception; target master.
Complete series:
ad9830a53a34f169197ecb7a919b08a98a4493fd inputs: set vpsadminServices to 7d911899

Final diff: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-11-diagnose-vpsadmin-api-exception/vpsfree-cz-configuration-final.diff
## haveapi-client-php
Worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-diagnose-vpsadmin-api-exception/haveapi-client-php
Base 0f5f9dad0ff445bdd36c776390ce4c8e8415444e
Head 7fa4e35a9d9cb462320a4b2f2786bf84b8e024f2
Feature branch 2026-10-11-diagnose-vpsadmin-api-exception; target master.
Complete series:
7fa4e35a9d9cb462320a4b2f2786bf84b8e024f2 Version 0.29.9

Final diff: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-11-diagnose-vpsadmin-api-exception/haveapi-client-php-final.diff

Commit rationale: vpsAdmin smoke test + testing procedure in one supporting
commit; separate source requirements/generated three package closures in one
HaveAPI update stream. Exactly one dependency update to0.29.9, no transitive
gem version changes. Config is one normal confctl-generated lock update;
message preserved including width warning under repository exception. PHP is
mechanical metadata-only (no standalone content review required), but its
whole-branch history is included. No superseded approaches/fixups/intermediate
pins or unused compatibility paths. No migrations/schema/persisted-state edits
in any feature series; migration merge/release/deployment/external-use
provenance inapplicable. No repeated update streams within these branches.

Owner/actual consumer pins: HaveAPI provider's master ed88e2a and supported
release784e113/v0.29.9 integrated, all three Ruby gems accepted by RubyGems.
Downloaded server SHA256 a0797067cf871a42402f917f1919a3db624d8e1e9cfb632daf7e64c2ae0061a4,
byte-identical to release build and independently extracted/routes checked.
Release365 specs,20 focused and seven exact-head CI workflows passed.
vpsAdmin API/client/download_mounter/outage utility source constraints now
~>0.29.9; package closures use HaveAPI server/client0.29.9 with regenerated
RubyGems hashes. No first-party gem versions/build IDs/uploads.
Smoke URLs are /doc/json-schema, /doc/protocol.md, /doc/create-client.md.
They assert expected headings and exact HTTP200 through the running packaged
API using existing retry helper; no synthetic source checkout or new API spec
partition. CI selection unchanged: package paths intentionally select full CI.

Configuration channel map: channels.vpsadmin.vpsadmin=vpsadminServices;
input follows nixpkgsStable/vpsadminosStaging. Normal confctl inputs channel
set --commit vpsadmin vpsadmin 7d911899... updates only the vpsadminServices
locked node, from b4ef8535a629ee8c9cd753afecdb05e0895d0eea to7d911899d0d3d335546f6b3676b2eb46a291764d.
Other lock nodes/follows/original URL fields unchanged; no manual edits.
The prior-pinned b4ef853..vpsAdmin base8a500 includes four already-merged
upstream mechanical dependency commits only: c4d9b50f4,81f1f1aab,6c706c285,
8a50010f4. No migrations, schema, runtime logic or Nix module edits in that
upstream gap. Inspect actual consumer configuration/API hosts as relevant.
Record previous pin for user rollback; no deployment/dry-activation attempted.

PHP mirror's35 tracked source files synchronized from release clients/php.
Only composer.json and src/Client.php version lines0.29.8->0.29.9 differ;
PHP runtime unchanged. Feature7fa4e35 pushed; master integration/tag deferred
until explicit named-repository approval. JavaScript npm publication is blocked
by existing authentication401; user was asked to refresh login. This does not
block Ruby API adoption; don't describe entire component release as complete.

Quick evidence: vpsAdmin Nix parse and extracted Ruby testScript syntax pass;
normal Overcommit Nixfmt/MigrationSpecs/API+WebUI i18n/Ruby lint/commit hooks
pass for both commits, diff --check clean. Root bundle-exec leaked activation
into child Bundix/API hooks; documented plain rake and plain Git in Nix work
without hook bypass. Metadata diff exactly limited to HaveAPI versions/hash
and requirements. Config normal hooks/semantic lock audit/diff --check pass.
PHP JSON version and PHP syntax pass; no hook framework declared. Fresh fetch
confirms all branches descend current origin/master; comparisons captured.

Docs: vpsAdmin docs/agent-instructions/testing.md now explains services-up's
package documentation checks, linked from repository AGENTS. Provider build
contract guidance already integrated. Config behavior is unchanged channel
selection, so its existing operations guidance was checked rather than copied.
Individual rollout/recovery/exact pins remain session-owned. Inspect placement
and scope. No WebUI behavior, KB labels/screenshots or client protocol changes.

Conservative risk high for live package adoption/deployment ordering; no state
conversion, incompatible API action/client/daemon protocol, new NixOS options,
node coordination or schema migration. Publish provider before consumer closure
and pin; API instances may roll independently; rollback restores previous
source/channel without state conversion. Master integration and deployment
remain gated as stated. Long services-up test, API host builds and downstream
exact-head CI remain pending; don't infer readiness from HaveAPI-only evidence.
Return findings by severity with paths/lines/commits, explicit whole-branch
history/migration/consolidation conclusions and residual verification gaps.
