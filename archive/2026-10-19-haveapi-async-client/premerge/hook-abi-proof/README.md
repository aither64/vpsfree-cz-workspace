# Prepared real-shell ABI proof

**Prepared only; not run.** Execute once through a fresh authorized Luna/low watcher
after the correction is committed, quick checked, independently reviewed, and the
lead explicitly releases this operation. No watcher is currently owned here.

The [current generation readback](current-generation.json) binds this prepared
operation to selected package `ad0s75irvrbj6pz6qk1zf7v9sy4l1qyp` and its unchanged
Ruby 3.4.9 / API 3.4.0. The script refuses a different selected profile or wrapper
interpreter before creating the disposable snapshot. The earlier `i144xnc9...`
diagnosis remains historical and unchanged.

The architect's [verification brief](../../design.md) separates two proofs:
owner0's actual coordinator regression establishes interpreter selection; this
independent operation establishes that the real declared HaveAPI shell and native
gems work with that selection. It calls no coordinator engine or private helper,
uses no ledger, and prepares no job or package activation.

## Exact operation

From the workspace, replace `REVIEWED_CORRECTION_SHA` with the full committed
dev-workspace correction SHA accepted by the lead:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-haveapi-async-client/premerge/hook-abi-proof/run.sh REVIEWED_CORRECTION_SHA
```

The script requires the existing session binding and exact committed HaveAPI
`19c20c90cc957d4225ece50a92e190855f252710`. Its single Nix operation is:

```sh
env -u GEM_HOME -u GEM_PATH -u BUNDLE_GEMFILE -u BUNDLE_PATH -u BUNDLE_APP_CONFIG -u BUNDLER_VERSION \
  HAVEAPI_RELEASE_TOOLS_ONLY=0 nix develop "path:$snapshot" --command ruby -e "$validation_and_assertions" \
  PATH GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_PATH BUNDLE_APP_CONFIG BUNDLER_VERSION NIX_SSL_CERT_FILE SSL_CERT_FILE
```

The explicit `path:` reference selects the archive directory directly and avoids
Nix inferring an ancestor Git source. The ordinary repository shellHook is enabled;
no separate dependency install,
fallback, or retry is added. The prefix of `validate.rb` is the
unchanged coordinator validation program; the script compares it with the frozen
candidate's committed source before Nix runs. Following assertions check the real
interpreter, load the native libraries, and emit a bounded ABI receipt. The
candidate source and validation program hashes are retained. No interpreter shim,
new execution framework, dependency-install override, or alternate ABI is used.

## Snapshot and dependencies

The operation archives the exact HaveAPI commit into a new `/tmp` directory
outside all checkouts. It checks that Git cannot resolve a parent checkout there,
so the normal shellHook's repository-root fallback selects the disposable source.
It copies the existing matching 3.3 `.gems` from the diagnosed retained source
using `cp -a --reflink=auto`; this makes independent files, with copy-on-write
extents when supported, rather than shared hardlinks. It refuses copied symlinks
that escape the disposable gem home. It compares the seed Gemfile with the
committed snapshot Gemfile, then copies the seed's ignored, shell-generated
Gemfile.lock. This lock is external dependency-environment evidence, not a
committed product file. Its exact SHA-256 is
`450de01a459fd59f8237065094ee4bf59d1263049af14244a768b29b7f2ebfc5`;
both copies must match before Nix and remain unchanged afterward. No live gem-home
symlink, mount, retained-source write, or shared
native-library rebuild is allowed.

Using this seed avoids an unnecessary fresh dependency compilation. The normal
shellHook still runs `gem install` and `bundle install` and may update only the
disposable copy. A fresh install into an empty disposable gem home would preserve
the same boundary but would take longer; this prepared operation has no fallback
or retry that switches recipes. Stop and report if the seeded operation fails.

## Acceptance and evidence

- Host Ruby remains the exact selected coordinator Ruby 3.4.9 / API 3.4.0.
- Nix-selected repository Ruby is 3.3.10 / API 3.3.0, using snapshot-local gems.
- `Bundler.setup` and Overcommit 0.73.0 load; JSON, Racc, Prism, and BigDecimal
  native libraries load and have complete extension metadata.
- Exactly one environment marker contains only declared keys, with nonempty PATH
  and the disposable GEM_HOME. No full environment or credentials are recorded.
- Every committed product path, original seed native file, original dependency
  lock, and copied dependency lock retains its before-operation hash. HaveAPI,
  WebUI, candidate source, selected runtime,
  configuration, ledger, and the existing verification receipts are untouched.

The script retains its new `/tmp` directory, `run.log`, `run.exit`, source archive,
candidate source copy, `baseline.json`, host Ruby facts, `validation.log`, and
`result.json` on success. Failure stops at the first failing stage; the exit/log
and available partial evidence remain. The watcher reports exact command, refs,
hashes, result, elapsed time, and any missing evidence; no retry or repair is
authorized. This is environment verification only, with no new product-test or
merge/deployment claim. No cleanup, session lifecycle action, or artifact
registration is part of this script.

The original operation failed before Nix because it assumed the ignored root
Gemfile.lock was included in the committed archive. Its snapshot
`/tmp/2026-10-19-haveapi-async-client-hook-abi.QLZpM1` and watcher logs under
`/tmp/2026-10-19-haveapi-async-client-abi-watcher.749opogw` remain unchanged.
The explicit dependency-lock copy above corrects that fixture setup. This updated
recipe is prepared only and requires a new authorized watcher; it has not run.

The next operation reached Nix input resolution, where automatic Git discovery
selected `git+file:///tmp` and failed before ABI validation. Its snapshot
`/tmp/2026-10-19-haveapi-async-client-hook-abi.FkLhD1` and watcher logs under
`/tmp/2026-10-19-haveapi-async-client-abi-watcher-seeded.0psmb1rd` remain unchanged.
The explicit `path:` source argument corrects that fixture resolution without
changing Git metadata or flake inputs. This further correction is not yet run.
