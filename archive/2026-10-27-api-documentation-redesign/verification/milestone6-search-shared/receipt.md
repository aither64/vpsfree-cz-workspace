# Milestone 6 search and shared README package

Source-ready on dirty shared head
`266dcb1852c8bac8735af684ce48380d2851a658`. No Git mutation/hooks or
service action. Nine owned paths, 164 additions / 64 removals; exact names and
SHA256 values in `owned-source-sha256.json`.

## Behavior and seams

- Every search form uses exact `Resource...`, retaining accessible version
  labels and normal GET. Existing canonical dotted resource title is unchanged;
  derived same-provider human ancestor labels use ` · `, including Unicode and
  missing-prefix fallback. Index payload/schema/key, extraction, rank/filter,
  cap, URLs and anchors are unchanged. Owner3 consumes existing display_queries
  fixture with the same expected hierarchy.
- Public argless `SharedDocumentationHelpers#render_shared_readme` reads the
  actual packaged `servers/ruby/README.md` through the existing views-relative
  path with with_toc_data/tables/fenced_code_blocks/lax_spacing all true. It
  reuses the neutral shared shell, title HaveAPI internals and private/no-store.
  Owner0 wires /doc, /doc/index[.md], /doc/readme and removes duplicate sidebar
  HaveAPI/readme. Technical aliases and source prose are unchanged.
- Shared route assertions prove byte-equivalent landing main content, actual
  README feature heading/class example/fenced markup, concise breadcrumbs and
  one internal menu; configured neutral Account uses actual cookie fixture but
  performs no token lookup/discovery/authentication or username presentation.
- Authenticated search uses real encrypted docs cookies on synthetic HTTPS
  requests. Member/admin filtering and action/field omission remain asserted,
  including conflicting Basic credentials that must not replace cookie identity.
  Search-index authorization is revalidated through actual token lookups before
  304; permission/key changes still reject stale responses with no index payload.

## Logical history split

`core-C.patch` applies the core anonymous/presentation/README changes from the
current head. `optional-D.patch` adds only three explicit contexts, including
all local fixture setup and helper requires, to those core versions. These are
read-only evidence patches/snapshots, never applied to the active worktree/index.
`history-group-map.json` records exact context/case ownership and references
owner4's separate test_support/documentation_oauth_fixture.rb. Core specs have
no top-level dependency on that optional helper. Former Basic HTML role cases
are removed from C and replaced by actual cookie cases in D, not weakened.

1. search_routes_spec: with OAuth documentation sessions → uses only cookie-user
   accessible parameters and actions while anonymous docs retain their full view.
2. search_index_routes_spec: with OAuth documentation sessions → rechecks cookie
   authentication and permission changes before any 304 response.
3. shared_pages_spec: with documentation OAuth configured → offers a neutral
   Account link without authenticating or describing even with a real session cookie.

## Quick evidence

Owner0 completed the coordinated `make doc` (exit 0; /tmp/haveapi-m6-doc.log).
No simultaneous or duplicate copy was run by owner1. In the prepared root Nix
shell with HAVEAPI_RELEASE_TOOLS_ONLY=1 and server Gemfile:

```sh
cd servers/ruby
export BUNDLE_GEMFILE="$PWD/Gemfile"
bundle exec ruby -I../../clients/ruby/lib -I../../clients/typescript/lib -S rspec \
  spec/documentation/search_spec.rb spec/documentation/search_index_spec.rb \
  spec/documentation/search_routes_spec.rb spec/documentation/search_index_routes_spec.rb \
  spec/documentation/shared_pages_spec.rb --seed 50232 --format progress
```

Final `04-focused.log`: **55 examples, 0 failures**, 1.54 seconds + 1.17 seconds
load. First `03-focused.log` preserves three newly introduced fixture-setup
failures: nested RSpec options returned nil API modules in two contexts, and
Rack::MockRequest did not fill raw HTTP_HOST from an absolute URL. Fixes use
inherited ApiModule constants and explicit synthetic Host, with no production
source or fixture-helper repair.

Final `06-final-lint.log`: seven Ruby files, no offenses. Final source delta
after tests is indentation only. Owned `git diff --check` passed.

All 2,148 protected input/evidence SHA256 values still match the publication
reference; see `protected-inputs-check.json`. No new dependency preparation,
packaging build/extracted gem check, installed snippets, compiler/generated,
performance, browser/HTTP/preview, OAuth provider, Git/hooks or lifecycle work.
Packaging assertions are source-updated/linted; their final execution remains
for the coordinated committed package batch. No active owned commands/watchers.

## Main guide facts

Main owns visible prose. Current technical facts: placeholder Resource...;
canonical resource identity is dotted, optional human search hierarchy uses
middots; internal landing aliases show the real server README and neutral
no-store shell; guides never acquire docs identity; role-filtered searches
require the actual configured documentation OAuth session. Other owner0/3/4
changes and final guide wording remain their own packages.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
