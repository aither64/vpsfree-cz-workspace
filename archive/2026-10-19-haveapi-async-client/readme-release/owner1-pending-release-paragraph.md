# Pending release-guide wording

DRAFT ONLY. Owner0 source implementation has been inspected, but focused checks
are still running. Do not insert into project documentation until their pass.
Final main writing/fact pass is required; real retained-tar smoke remains a
post-review gate and is not claimed here.

## Dependency-resolution sentence in release step4

JavaScript build dependencies use `npm ci` with the committed lockfile. Other
components retain their existing dependency resolution; separate complete
release builds are not promised to be byte-identical.

## Paragraph beside local JavaScript packaging

`make version` updates the npm manifest and both root version fields in the
JavaScript lockfile; release checks require the lock's package identity and
versions to agree with `VERSION`. Package inspection validates the exact
`main`/`types` entries, nonempty declarations, README, both async guides and
`LICENSE.txt`, and checks that the standalone bundle matches the packed one.
The npm smoke check installs the retained tarball in a temporary consumer with
install scripts disabled and `NODE_PATH` unset. It imports `haveapi-client` by
package name, checks `Client === CallbackClient` and the version, constructs
both callback and async clients, then compiles a strict TypeScript consumer.
The compiler's file list must resolve the installed package declarations and
standard libraries, without checkout source or declarations.

## Exact implementation evidence, not execution proof

Makefile release-deps uses npm ci --no-audit --no-fund; version updates lock.version
and lock.packages[""].version. artifacts.rb checks both roots' name/version.
inspect_npm enforces exact entry fields, required docs/nonempty declarations and
standalone JS equality. smoke_npm runs npm install --ignore-scripts --no-audit
--no-fund ABS_TGZ in a new temporary consumer, with NODE_PATH unset for install,
CommonJS and compiler. It uses clients/js/node_modules/typescript/bin/tsc with
strict/noEmit/ES2020/CommonJS/node resolution and checks listFiles realpaths are
only the consumer, installed dist/types or pinned compiler standard libraries.
The bounded quick fixtures stub npm installation; a real post-review retained-tar
installation is still required before any pass is claimed for that operation.
