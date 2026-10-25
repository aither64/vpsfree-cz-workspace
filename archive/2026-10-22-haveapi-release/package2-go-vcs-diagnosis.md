# Go documentation fixture VCS-stamping diagnosis

Read-only application diagnosis by implementer2, 2026-10-22. Session current and
both environment bindings match `2026-10-22-haveapi-release` in the bound workspace.
Lead authorized known-quick native probes and this new diagnosis record only.
No application/Git mutation, listener, package build/install, generated-client
acceptance retry or ambient temporary-directory cleanup was performed.

## Exact failed execution

Final independently reviewed/published feature head:
`48543f8cd254eb0fc087931a5dc98ea730fd94af`.
Retained evidence: `python-login-verification.log`, `.exit` and `-result.json`.
The visible parent-monitor fallback ran for 168.83 seconds, exit 1. Final artifact
build/verification and both wheel/sdist installed dynamic acceptance runs completed;
Go bundle/preflight passed. The first Go build failed with repeated:

```text
error obtaining VCS status: exit status 128
  Use -buildvcs=false to disable VCS stamping.
```

`clients/go/spec/documentation_acceptance.rb:56` runs:

```text
go build -o <temporary-root>/bin ./cmd/...
```

Its working directory is `<temporary-root>/consumer`. The fixture creates a
standalone consumer `go.mod` and a generated SDK referenced by a local replace.
Neither is a Git repository. `Dir.mktmpdir` follows Nix's `TMPDIR`, here
`/tmp/nix-shell.<suffix>/haveapi-go-documentation-*`. Temporary files are removed
by the block on failure, so there is no retained failed SDK to inspect.

## Concrete cause

An ambient **empty `/tmp/.git` directory** exists, uid 1000, mode 0755. It has no
HEAD/config/objects/refs. This record makes no ownership claim; it was inspected
read-only and left untouched. Native `git -C /tmp rev-parse --show-toplevel` fails
with exit 128, "not a git repository".

The selected Nix Go is 1.26.9:
`/nix/store/bbqjsl8fzayd8c2i63skp7hybysvwr03-go-1.26.9`.
Its `cmd/go/internal/vcs/vcs.go#FromDir` finds VCS markers by parent-directory
stat. Go recognizes `/tmp/.git` as a repository marker without first requiring
Git to accept it. Default buildvcs=auto then calls `gitStatus`, which runs
`git status --porcelain` in `/tmp` and returns the observed exit 128. The temporary
module and package both appear beneath this same marker to Go's parent scan.

No GIT_DIR, GIT_WORK_TREE, GIT_INDEX_FILE, GIT_CEILING_DIRECTORIES or
GIT_DISCOVERY_ACROSS_FILESYSTEM override was present in either the Nix shell or
the dedicated acceptance bundle. GOFLAGS was absent. This is not a generated SDK
compile error or a malformed real consumer module.

## Known-quick native reproduction

A disposable standalone `example.test/vcs-probe` module with `go 1.20` and
`package main; func main() {}` was created beneath Nix TMPDIR. No SDK or listener
was created. The probe used the harness's GOWORK=off, GOPROXY=off, GOSUMDB=off and
GOTOOLCHAIN=local environment and dedicated Ruby bundle.

| Probe | Result |
| --- | --- |
| `git status --porcelain` from temporary consumer | exit 128, not a Git repository |
| `go build -n -x -o <temp>/probe .` | exit 1; trace: `cd /tmp`, `git status --porcelain`, exact VCS error |
| Same command with PWD explicitly set to the consumer | same exit 1 and `/tmp` Git status trace |
| `go build -n -buildvcs=false -o <temp>/probe .` | exit 0; ordinary compile/link plan emitted |

`-n` prints the compiler plan without running the compiler/linker. These probes
were known-quick, invoked no HTTP listener and performed no package dependency
or toolchain download. Every probe's owned temporary directory was removed by
its ordinary temporary-directory context. No process remains active.

## Smallest proposed correction, pending grant

Add **`-buildvcs=false` only to the documentation acceptance consumer's `go build`
command** in `clients/go/spec/documentation_acceptance.rb`. Explain the fixture
contract beside it or in `clients/go/docs/documentation.md`: generated temporary
consumers have no source-repository history to stamp. Their source/artifact identity
is supplied by the retained parent verification receipt, not accidental ancestor
Git metadata. A valid ambient ancestor Git repository could otherwise silently
stamp unrelated history, even without this failure.

This preserves actual snippet imports, generated SDK source, module replacement,
compiler/type checking, execution, HTTP fixture and all product behavior. Do not
change the generator, renderer, SDK schema/go.mod output, global GOFLAGS, ambient
Git directories or release/package build policy. Do not initialize synthetic Git
history or broadly clear environment as a substitute for explicit fixture policy.

Proposed focused regression: use an owner-created temporary root with an empty
`.git` ancestor and a tiny consumer module, run the harness-selected build command
in native dry-run mode, and require success without VCS discovery; include the
baseline no-flag negative control proving this exact condition. Keep it listener-
free and compiler-free. Required syntax/style/preflight checks follow a source
grant. Full Go rendered compile/run remains a separate authorized acceptance run
after the resulting intended changes/review gate. Exact application paths would
be the Go acceptance runner, its focused regression if added, and a short owning
fixture explanation; impl0 retains all Git/index/hooks.

No source change has been made. No new product contract or compatibility change
is proposed; only explicit build metadata policy for disposable generated fixtures.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
