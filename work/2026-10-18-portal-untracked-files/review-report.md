# Final independent review: portal untracked-file access

## Findings

### Blocking — global Git exclusions do not protect newly readable files

Originating lanes: risk/compatibility and general.

Affected commit: `4218c6d3d3edda587118e6053585b9e3d511aea2`.
Location: `dev-workspace/portal/internal/repository/source.go:149`, through
`portal/internal/repository/review.go:170`.

The new untracked-file authorization invokes `ls-files --others
--exclude-standard` through `ReviewReader.git`. That helper removes inherited
Git settings and sets `GIT_CONFIG_GLOBAL=/dev/null` and
`GIT_CONFIG_NOSYSTEM=1`. Consequently, an ordinary global configuration entry
such as `core.excludesFile = /path/to/ignore` is absent during authorization.
Files excluded by that configured ignore file are admitted and returned to an
authenticated caller who supplies their path. The same shared helper governs
project, shared-workspace and unpublished tracking-file reads.

This violates the user's explicit non-ignored-file boundary. It requires no
hostile local operator, filesystem race or symlink manipulation: a normal
developer configuration and an ordinary untracked private file suffice. The
old source reader rejected the file because it was untracked.

Independent reproduction used a disposable repository and synthetic
`private.env` file. A temporary global Git config selected an exclude file
containing `private.env`. Ordinary Git's identical literal `ls-files` query
returned no entries; the portal helper environment returned
`private.env\0`. A temporary Go test overlay then exercised the real HTTP
handler using the existing web fixture and the configured global exclude:

```text
--- FAIL: TestReviewGlobalIgnorePolicy (0.24s)
GET /api/sessions/example/file?path=private.env&repository=244210e48437b6556980a70249a99369 = 200:
{"path":"private.env","repository":"project","source":"worktree","content":{"text":"synthetic private fixture\n","bytes":26,"kind":"file"}}
FAIL github.com/aither64/dev-workspace/portal/internal/web 0.293s
```

The test expected HTTP 404 and first asserted that ordinary Git excluded the
fixture. It ran through the repository's Nix shell with `-mod=readonly` and an
absent `DEV_WORKSPACES_CODEX_PROVIDERS` fixture path. The overlay and temporary
repositories were removed; no application or test source was modified.

Required correction: preserve Git's effective exclusion policy for the new
authorization, including configured global exclusions, while retaining the
other bounded/sanitized Git execution safeguards. Add a regression covering
this normal global `core.excludesFile` configuration. Keep tracked files and
explicitly published artifacts readable under their existing rules. Refresh
the two consumer pins after committing the correction.

No other findings.

## Reviewed scope and evidence

The review covered general, architecture/repetition, scope/proportionality,
and risk/compatibility. Assigned standalone fallback reviewer:
`/root/final_review`, `gpt-6-astra` / `xhigh`; no nested delegation.

Inspected the complete commit series and final diff for:

| Repository | Base | Head | Commits |
| --- | --- | --- | --- |
| dev-workspace | `679273d5369a20b68888397c27c813cece48d59f` | `4218c6d3d3edda587118e6053585b9e3d511aea2` | 1 |
| workspace | `07b9d0a6a883a9af5d5ea7541d22f77c1fac9468` | `23e59bac42b68c3e3a2908f89be002a0439eef29` | 1 |
| vpsfree-cz-configuration | `647a3723a1095c6f5c5af44c81031105ee6d648c` | `d30fc508454b89d82a8dc13c147057caa95d882d` | 1 |

All worktrees were clean and at these exact heads. Every listed base is an
ancestor of its head. The runtime diff passed `git diff --check`.

The implementation retains exact literal path membership, the existing Git
mode checks, repository registration/branch/common-directory validation,
session lookup, no-symlink confined regular-file opens, bounded previews and
no-store responses. Artifact listing, preview and download retain publication
requirements. Unpublished tracking reads use the actual active/archive root.
Archived project reads still use final-commit blobs. The tests exercise the
malformed catalog regression, unpublished tracking reads, local ignore rules,
special files, literal names, preview bounds and archive lookup.

Ownership is appropriate: the generic runtime owns this behavior and the
source viewer keeps the existing routes, fields and source strings. No new
abstraction or cross-project duplication was introduced. The README links the
updated portal guide; the guide describes the supported file and publication
contracts rather than an individual rollout.

Consumer inspection confirmed the workspace calls the site extension's
`lib.mkPackage`, with its existing nested runtime override; configuration maps
the `dev-workspace` channel to `devWorkspace`, which aitherdev selects for the
host module and Codex package helper. Only the runtime node changed in each
lock. Both consumers select the exact runtime head above and the same NAR hash,
`sha256-YOm34Of8ssD4zgNICUT6ZZQwZdLYhTmJgUJMJxM+BnY=`. The site extension and
other lock nodes are unchanged.

## History, repeated updates and migrations

The complete histories are focused: one runtime behavior commit with its
tests/documentation, one workspace runtime-selection commit, and one generated
configuration channel update. These independently reviewable changes are
correctly separated. Commit messages match the applicable conventions,
including the generated configuration-message exception.

No obsolete branch approach or redundant follow-up commit remains. There are
no repeated dependency/pin update streams within any branch; no consolidation
is currently required. The two matching consumer selections serve distinct
deployment inputs and are not redundant history.

**No migrations.** No persisted format, schema or lifecycle journal changed,
and there is no branch migration lineage to consolidate. The packet records
that none of these feature heads has been merged, released or deployed.
Older software retains readable state and narrower source access. The change
does not require coordinated fleet updates. Package recovery remains subject
to the existing forward-only transition policy.

## Remaining verification and disposition

The packet's focused Source/WorkspaceSource and browser checks passed before
review. The added independent negative probe exposes a missing policy case;
the final deliverable is therefore not ready for long integration testing or
deployment until the blocking finding is fixed.

After correction, the lead should run focused exclusion/reader checks and
update both pins, then follow the mandatory-review remediation rules. Packaged
checks, builds, CI, composed deployment validation and live acceptance remain
pending. Live acceptance still needs the original Rust design link plus a
disposable non-ignored file and ignored sibling. The aitherdev reservation and
separate default-branch integration approval remain external execution gates.
