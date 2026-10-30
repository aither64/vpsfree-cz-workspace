# Prepared installed-snippet commands (NOT EXECUTED)

Expected final server/harness binding from lead:
`cefe8c5d43277dbaba35632b5239d95a1959cf1e`, tree
`7af42033e378e354a035e9eb99b6c78d85a11d84`.
Artifacts retain their actual source `a06b0cfa2abd7560f10cb58ebe99d8eb3f10b8f9`.
The source comparison of905blobs proves only the accepted CSS change; no program,
fixture, renderer, package source or dependency declaration changed. Reverify
that binding at launch; do not retag/relabel artifacts or rerun covered CI.

A fresh retained Luna/low native watcher launches the related two-run batch
only after main's final execution grant. Binding check stays outside Nix.
The parent owns diagnosis; stop at first nonzero, preserve all output, no retry.
Expected a few minutes (two installs plus TypeScript compilation and the harness's actual extracted panels); count/timing are unverified,
not acceptance claims. Reassess at10minutes with actual stage/process rather
than killing for silence or expanding scope. The fixture is localhost-only,
synthetic API credentials/challenge; no live docs/provider OAuth or TLS.

```sh
cd /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign
dev-session current
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi
env -u RUBYOPT -u RUBYLIB -u BUNDLE_BIN_PATH -u BUNDLE_GEMFILE \
  -u BUNDLE_PATH -u BUNDLE_FROZEN -u BUNDLE_LOCKFILE -u BUNDLER_SETUP \
  -u RUBYGEMS_GEMDEPS -u GEM_HOME -u GEM_PATH \
  -u LD_LIBRARY_PATH -u LD_PRELOAD \
  HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --no-write-lock-file --command bash -euc '
    export BUNDLE_GEMFILE="$PWD/servers/ruby/Gemfile"
    cd servers/ruby
    bundle exec ruby spec/client_examples/dynamic_acceptance.rb \
      --npm-artifact /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/postreview-artifacts-a06b0cfa-20261028/release-40745814145/haveapi-client-0.31.0.tgz \
      --python-artifact /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/postreview-artifacts-a06b0cfa-20261028/release-40745814145/haveapi_client-0.31.0-py3-none-any.whl \
      --typescript /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi/clients/js/node_modules/typescript/bin/tsc \
      --node-types /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi/clients/js/node_modules/@types \
      --output /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/installed-dynamic-cefe8c5d-20261028/wheel
    bundle exec ruby spec/client_examples/dynamic_acceptance.rb \
      --npm-artifact /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/postreview-artifacts-a06b0cfa-20261028/release-40745814145/haveapi-client-0.31.0.tgz \
      --python-artifact /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/postreview-artifacts-a06b0cfa-20261028/release-40745814145/haveapi_client-0.31.0.tar.gz \
      --typescript /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi/clients/js/node_modules/typescript/bin/tsc \
      --node-types /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi/clients/js/node_modules/@types \
      --output /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/installed-dynamic-cefe8c5d-20261028/sdist
  '
```

Both output directories are new/uncreated. The existing harness owns isolated
npm/uv installation, temp consumer, disposable Ruby Rack/WEBrick fixture and
its normal ensure cleanup. It extracts explicit **thorough** panels only for
JavaScript callback/async, TypeScript callback/async and Python sync/async from
overview/authentication/selected nested resource HTML. It checks strict installed
package declarations, discovery/auth/challenge, exact request values and error
results. No installed simple-program equivalence is asserted.

Prepared inputs (static proof, no loading): root/server bundle and selected
Ruby3.4.11 bundled gems present; JSON2.21.2; compiler6.0.3/@types-node24.19.2;
Python3.11.17 interpreter exists. No missing selected-platform gemspec. Foreign
sqliteplatform specs in the multi-platform lock are not local requirements.
Root Nix supplies Node24.21.0/npm11.19.0/uv0.13.4 per retained prepared-input
and CI tool evidence; actual launch must retain its observed executable/version
identities. CI server lock differs from local only io-console0.9.5 versus0.9.4
and checksum, recorded exactly in ci-local-server-lock.diff; no graph repair.
Isolated npm xmlhttprequest and Python httpx/anyio dependencies/build backend
resolution remain the harness's actual runtime input to record at execution.
No package index reachability or fresh installation was tested in this static grant.
