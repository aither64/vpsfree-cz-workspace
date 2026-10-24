# Status dependency-updater follow-up

The first post-review C batch passed HaveAPI, Terraform and vpsAdminOS. Status
stopped at its Go dependency update with exit 255; no publication command ran.
This follow-up fixes that pre-existing workflow defect separately from the
guard adoption. Source/pin and the full guard policy remain unchanged.

## Diagnosis and retained effects

Original branch range:
`587cd65bb02e6dddea7f6b6409e42a15f36ab4fb..7641e48787281d29cdd0df95f7ee06555c73fac6`.
The `Update Go dependencies` shell block is byte-identical at both revisions
(SHA-256 `c6afcced5f52035926160c0ccababc549fa1005a3173cfff9704a9332109754d`).
It embeds the computed SRI hash in a `/`-delimited Perl program. Base64 `/`
characters become Perl syntax, producing the observed unknown regexp modifiers
and unterminated quote. In addition, its placeholder replacement matches only
a flat assignment; the actual package's conditional default/override expression
matches neither old replacement. Fixing only the delimiter would leave that
second defect.

The failed operation is
`/tmp/flake-update-guard-2026-10-24-C-postreview-1/project-vpsf-status/receipt.json`.
Its failed step is `020-workflow-step-03.stderr`; the corresponding extracted
script is `step-03.sh`. The failed group 3252040 has no remaining processes.
The checkout has local HEAD `c3b0970fdfc20b8aeaf24c9e8677db4104a43eb5`, one accepted
flake update on top of the reviewed feature, a clean index, and only unstaged
`go.mod`/`go.sum` changes (64 insertions, 72 deletions). `nix/package.nix` is
unchanged. The external push URL remains
`disabled://nonpublishing-verification`. No failed-checkout cleanup or retry was
performed. The source script's EXIT trap removed its temporary build log, so
the original computed hash is no longer available; the retained Perl errors
and unchanged conditional assignment establish the cause without inventing it.
[Failure evidence hashes](package-c-status-failure-evidence.json) bind the
receipt, stderr, unchanged original workflow block and process reconciliation.

## Bounded correction

Only the two hash-setting workflow lines change. They call
`perl tools/set-vendor-hash.pl <hash|--fake> nix/package.nix`. The setter validates
SHA-256 SRI shape, treats the value as data, updates exactly one supported
default assignment and retains the `vpsadminGoClientSource` override. Flat and
the current conditional layouts are supported. Invalid values, unknown layouts
and multiple assignments fail before writing the file. The owning helper's
comments explain the data/syntax boundary and override preservation; no new
operator procedure or public feature contract is needed.
Perl is declared in the development shell because the regression invokes it;
the old shell resolved only the host's `/run/current-system/sw/bin/perl`.
The updated shell selects packaged Perl 5.42.0. This adds no package runtime
dependency or flake input.

`tools/vendor_hash_test.go` exercises nine table cases plus the actual current
package layout. It covers slash/plus characters, fake-to-real and real-to-fake,
conditional override preservation, malformed/code-containing values, unsupported
expressions and multiple assignments with unchanged-file assertions. The normal
`go test ./...` picks up these regressions.

## Checks and next action

Completed in the repository's declared Nix shell:

```sh
nix develop --no-write-lock-file -c bash -c 'gofmt -w tools/vendor_hash_test.go && perl -c tools/set-vendor-hash.pl && go test ./tools -v'
nix develop --no-write-lock-file -c bash -c 'go test ./... && nix shell --inputs-from . nixpkgs#actionlint nixpkgs#shellcheck -c actionlint .github/workflows/update-dependencies.yml'
```

Both returned 0. Root Go tests took 9.572 seconds; config 0.018 seconds; tools
0.225 seconds. Actionlint 1.7.12 with ShellCheck 0.11.0 found no issues.
`git diff --check` passed. Official upstream SSH tag lists were rechecked:
checkout latest `v7.0.1` is `3d3c42e5aac5ba805825da76410c181273ba90b1`;
install-nix latest `31.11.3` is `75c75c31ebece974e48ebc36b4ad125bd97bd97b`.
The already selected compatible refs remain unchanged; original compatibility
evidence is in [package-c-actions.json](package-c-actions.json).

After declaring Perl, the following passed again using the packaged binary:

```sh
nix develop --no-write-lock-file -c bash -c 'command -v perl && go test -count=1 ./tools && go test ./...'
```

The uncached helper tests took 0.212 seconds; the complete Go run reported root
9.812 seconds, config 0.015 seconds and tools 0.214 seconds. Ordinary
`nix develop --no-write-lock-file -c make hooks` installed the required Lefthook
pre-commit hook successfully.

The lead completed the direct helper diagnostic/comment pass with no edits.
Required Lefthook gofmt and i18n checks passed on commit
`521c5b627a845e2f2e7378b309b1ea8f86f3d13d`, following adoption `7641e487...`.
The worktree is clean. [Complete fix inventory](package-c-status-fix-inventory.json)
records both commits, all final paths and exact source hashes.

Publication is held for the lead's sequencing decision: existing self-hosted
integration CI triggers on the new Go test and `flake.nix`, while new long runs
are gated on final affected review. The lead also selected a final provider
packaging successor, not yet published; once it is reported final, consolidate
one successor pin into each owning C adoption while retaining this independent
status bug fix separately. Then review the completed fix/repin deliverable.

After review, use new follow-up manifest/driver filenames and a new root bound
to final provider P and all final heads for the live status pattern. Preserve
the original driver, manifest, review report and all completed attempt hashes.
No runtime dependencies, locks, migrations, formats or deployment configuration
change in this fix. No default integration, deployment, machine ownership or
session lifecycle action is authorized.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
