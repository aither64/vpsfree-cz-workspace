# vpsAdmin documentation format

## Goal and scope

Recommend a replacement for ikiwiki under vpsAdmin `docs/`. The user needs a
place to write documentation without building or publishing a site and allows
removal of obsolete material. This turn prepares a proposal; implementation is
a follow-up.

## Affected repositories

- `vpsadmin`: docs, root README documentation link, and AGENTS docs entry.
- Coordination workspace: this initiative's plan and state only.

## Proposed approach

Use ordinary Markdown with a hand-maintained `docs/README.md` topic index.
Keep the existing layout where useful, use `.md` extensions and explicit
relative links, and replace ikiwiki directives with headings and fenced code
blocks. Explanations should be understandable without a renderer.

Initial content: overview, transactions, object lifetimes, plugins, Czech
translation conventions, and storage (overview, branching, downloads, and other
substantive operations). Keep `i18n-cs.md` at its current path and preserve
`LICENSE`. Consolidate tiny operation stubs into a storage overview. Add new
subdirectories when there is actual material to put there.

### Content disposition

- Refresh the overview, transactions, lifetimes, plugins, storage, branching,
  and download explanations against current source. Useful concepts are mixed
  with old names, assumptions, or unimplemented plans.
- Remove release/upgrade procedures under `releases/` (v2.0 through v3.0.0)
  and one-off scripts after checking for current consumers and any supported
  recovery requirement. Git history retains the originals.
- Remove OpenVZ-specific VPS dataset instructions, the old console page and
  `vzctl` patch, and old shaping guide. Write current topic guides from current
  code when useful; retain component responsibilities in the overview.
- Replace `index.mdwn` with the README index. Remove `Makefile`, `local.css`,
  and the `.mdwn`-specific `docs/.editorconfig`. Update root README and AGENTS
  pointers and check repository-wide references before deleting or moving.

## Decisions

- Recommendation: plain Markdown now. No generator configuration, publishing
  pipeline, theme, or build dependencies are needed for the stated purpose.
- MkDocs can be added when rendering becomes useful: it accepts regular
  Markdown, relative `.md` links, and README index files. Reference:
  <https://www.mkdocs.org/user-guide/writing-your-docs/>.
- Remove obsolete documents based on content and implementation, rather than
  age alone. Do not create a second in-tree historical archive.

## Compatibility and deployment

Documentation-only: no database, persisted data, API/client, daemon protocol,
Nix module, runtime compatibility, or coordinated machine changes. Update all
in-repository links; external links to removed source paths may break.
Removing the ikiwiki recipe retires that repository build/deploy workflow but
does not alter an existing hosted site. Site changes are outside this request.
Git history or a revert can restore source without altering application state.

## Documentation

Readers are developers and operators. Current project explanations belong in
`vpsadmin/docs/`, linked from README and AGENTS. Member task guides remain in
the knowledge bases; site-specific deployment procedures belong in their
configuration repository. Apply the user-facing writing skill to finished
vpsAdmin prose before implementation commits.

## Verification

Proposal: inspect fetched upstream docs, representative current code, and
MkDocs documentation. Implementation: verify retained technical claims,
Markdown links and anchors, index coverage, removal of ikiwiki syntax, obsolete
path references, and whitespace. Run repository hooks and mandatory review of
committed docs changes. VM tests are unnecessary for docs-only changes.
