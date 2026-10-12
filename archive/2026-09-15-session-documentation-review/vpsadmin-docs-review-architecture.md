# vpsAdmin documentation directory: architecture review

## Findings

No Blocking, Important, or Advisory findings.

Reviewed the single committed change
`c38839d5be62e9d40d055b23a84844e2037ba4db..f8fb5b3af225f20b40ad16df49d4f4ceca68fcf7`
under the architecture and repetition lane. Read the mandatory review skill,
lane instructions, review packet, initiative plan/state, and repository
`AGENTS.md`. Earlier integrated repository changes were outside this review.

## Assessment and evidence

- The rename remains owned by vpsAdmin's top-level documentation tree. An
  independent Git tree comparison confirmed all 46 relative paths, blobs, and
  modes are preserved, with no tracked top-level `doc/` left. The README entry
  point and both AGENTS pointers now identify `docs/`.
- `docs/Makefile:7` derives its source from the working directory. Its output
  directory, build flags, and publication destination remain unchanged. The
  dry run `make -n -C docs IKIWIKI=ikiwiki` resolves the source to `docs/`.
  Unchanged relative document and asset relationships keep the existing layout.
- `tests/ci-selection.yml:18` updates the existing owning path rule without
  adding another selector, compatibility tree, or duplicated behavior. The
  directory rule also covers scripts, CSS, and the Makefile that the generic
  Markdown rules do not cover. Inspection of `tools/select_ci_tests.rb`, its
  unit suite, and `.github/workflows/ci.yml` confirmed existing precedence and
  fallback behavior remain intact.
- Independent checks using the repository-pinned Ruby passed: all 46 actual
  documentation paths skip integration CI, adding a WebUI login change retains
  the auth tags, and adding `tests/ci-selection.yml` forces full CI. An
  `api/doc/template.erb` path remains outside the root documentation skip rule.
- Repository path searches and inspection of `api/Rakefile:16`, component
  ignores, the flake, and source/component packaging found no remaining
  consumer of the old top-level source path. API YARD's local `doc/` inputs and
  `html_doc` output have separate ownership. Packaging copies the documentation
  with the source tree without selecting its old name.

## Residual risks and verification limits

- The wiki was not rendered or published during review; ikiwiki is absent from
  the ambient environment. The Makefile check was a dry run only. No long
  integration tests or external mutations were performed.
- Unpinned external links or operator commands that name the old repository
  source directory must use `docs/`, as accepted in the plan. The existing
  published documentation destination is unchanged; no redirect or fallback
  directory is introduced.
