# Affected final review: Bundler fixture lockfile selection

Retain the completed dependency review and its exact base/range. The only later
content change is a8ea3132e7efe601aaa8965afe648459b3dab5c5, parent
18331877660ed0f736a25b29914756da89df0df9, final tree
9a596258d912ca2075c36ded30d11b3984c656ae. Source/index clean and frozen.

The post-review batch passed documentation and 355 server specs, then the Ruby
client before-suite child exited before readiness. No examples ran. Owner proved
no owned child/listener remained and did not retry. Helper discarded child output;
no-server probes reconstructed its nested Bundler environment. Bundler 4 exports
parent BUNDLE_LOCKFILE. The helper switched only BUNDLE_GEMFILE, causing the server
Gemfile to be compared against the client lock under frozen Bundler. Captured
ProductionError and environment selectors are in verification/dependency-refresh/
ruby-client-nested-bundle-diagnostic.log. Explicit matching server selectors made
Ruby bundle check pass. Go additionally lacks server fixture gems in its declared
component gem home; that is a separate bounded setup prerequisite, not a source
GEM_HOME override or test pass. See ruby-go-paired-lock-diagnostic.log.

Changed two existing env mappings in clients/{ruby,go}/spec/support/test_server.rb:
BUNDLE_LOCKFILE => "#{@gemfile}.lock" alongside the owning BUNDLE_GEMFILE. No startup,
cleanup, runtime client, authentication, protocol, parser or wrapper change.
The small correction uses the lead brief; no separate generalized design needed.
No new public documentation contract: existing server fixture prerequisites remain,
and temporary checkout-specific gem setup is captured in verification records.

Quick checks: Ruby syntax OK for both helpers; native RuboCop two files clean;
normal HaveapiI18n/RuboCop and commit-message hooks passed. No suite/server retry
or Go fixture dependency installation since source correction. Prior Python/
flake/ABI checks retain their unchanged source/dependency inputs.

Complete unmerged range c1823f3d70365b0442d0e2171bdf83bd4c6dbe31..a8ea313...:
1.67ecb6797c2794113b078044395d7a2ed54dfda2: Ruby 3.4 native shell selection.
2.7b7697e5c2dbb82d120cb5fa321d67b489d59a3e: single generated nixpkgs update.
3.18331877660ed0f736a25b29914756da89df0df9: certifi/Ruff pins and version note.
4.a8ea3132e7efe601aaa8965afe648459b3dab5c5: latent baseline fixture assumption
  corrected for Bundler 4. Separate independent test-environment purpose, rather
  than a superseded pin or fixup of behavior introduced by prior three commits.
Complete final diff: seven files, +33/-33. New series/diff fixture-final-series.txt,
fixture-final.diff and two-file fixture-only.diff under verification/dependency-refresh/.
Original three-commit inventories, owner report, review and failed logs preserved.
No repeated update stream, merged-history rewrite, obsolete approach or migrations.
None of these four follow-up commits merged/released/deployed/externally consumed.

Review only affected general and architecture lanes plus complete final history/
migration conclusions. Low risk for two explicit fixture selectors; original
medium-risk toolchain/CA review remains in force without risk-lane repetition.
Retain reviewer0 saved Sol/xhigh/read_only, same session/thread, no overrides or
nesting. Read required lane references and project guidance. No source writes,
setup, live tests, CI or publication. Long continuation follows review: install
server fixture dependencies into ordinary Go gem home with matching frozen server
lock, then Ruby/Go client specs and remaining Python/package/release checks only.
No repeated successful docs/server suite. No merge or release authorization.
