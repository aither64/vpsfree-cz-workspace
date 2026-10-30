# Milestone 5 search, neutral headers and detail metadata

Source-ready package on dirty shared feature head
`898df315add307ce5d3013ab62ae12834b64a13f`; no commit or hooks run.
Owner0/3/4 changes remain outside this package. The 12 owned paths below
are the complete commit scope (238 insertions, 13 deletions at readiness).

Resource search titles use full dotted machine paths. A derived
`resource_label` joins existing same-provider ancestor labels with ` / `;
missing prefix records fall back to their machine segment. Resource context
omits an identical primary name and the duplicated leaf label. Action and
parameter titles retain their names, complete resource context, and existing
provider/direction/type/label details. Native rendering and browser rendering
consume shared `display_queries` expectations in the existing index fixture;
its serialized index and existing query/ranking expectations are unchanged.
The placeholder is the exact requested `...`; accessible version labels stay.
No index schema/key, permissions, matching/rank, cap or URL change.

Neutral successful HTML explicitly sets `Cache-Control: private, no-store`.
Existing guide/alias and mounted route loops assert it; 404/error paths are
outside the agreed repair. Shared specs also cover owner0's single-heading
index, one internal menu, concise breadcrumbs, escaped configured/actual-host
identity and single-version neutral Account link without discovery/auth.

`ClientExample.detail_levels(*values)` accepts only `:simple` or
`:simple, :thorough`, retaining a frozen copy. The reader inherits the nearest
explicit declaration and otherwise returns the frozen legacy pair. HTTP and
CLI declare simple; curl inherits HTTP. Context, direct rendering, existing
panel generation/IDs and renderer registry are unchanged. Metadata forwarding
and control wrapper belong to owner0; selection/persistence behavior to owner3.

## Focused evidence

Final command, root repository Nix shell (no dependency refresh):

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --command bash -euc '
  bundle exec rubocop servers/ruby/lib/haveapi/client_example.rb servers/ruby/lib/haveapi/client_examples/http.rb servers/ruby/lib/haveapi/client_examples/ruby_cli.rb servers/ruby/lib/haveapi/documentation_search.rb servers/ruby/lib/haveapi/shared_documentation_helpers.rb servers/ruby/spec/client_examples/presentation_spec.rb servers/ruby/spec/documentation/search_spec.rb servers/ruby/spec/documentation/search_routes_spec.rb servers/ruby/spec/documentation/shared_pages_spec.rb
  make doc
  cd servers/ruby
  export BUNDLE_GEMFILE="$PWD/Gemfile"
  bundle exec ruby -I../../clients/ruby/lib -I../../clients/typescript/lib -S rspec spec/documentation/search_spec.rb spec/documentation/search_index_spec.rb spec/documentation/search_routes_spec.rb spec/documentation/search_index_routes_spec.rb spec/documentation/shared_pages_spec.rb spec/client_examples/presentation_spec.rb --seed 50232 --format progress
'
```

Final log: `05-final-focused-lint.log`, exit 0. Nine Ruby files lint clean;
**61 examples, 0 failures**, seed 50232, 1.43 seconds examples + 1.15 seconds
load. Owned-path `git diff --check` also passed. First-run log retains two
corrected test-only mistakes: Unicode expected order and a prohibited name
setter after mount. Lint corrections are retained in separate logs. No broad
integration, generators, compiler, packaging, performance, browser, HTTP,
dependency preparation, Git mutation, hooks or OAuth work ran.
No active owned process/watcher remains.

## Guide facts and review boundary

Main owns final prose. Relevant lasting facts: nested resource search displays
full machine identity and available ancestor labels; detail control is offered
only for declared multiple levels; choosing a single-level client does not
replace the saved preference; custom renderer authors can declare detail_levels,
with inherited/frozen two-level compatibility default. Neutral success headers
now agree with the existing ordinary-documentation private/no-store statement.
Main should reconcile `doc/documentation-ui.md` and renderer extension guidance
in `doc/client-examples.md`; no additional project prose authored here.

## Owned source hashes

- `servers/ruby/lib/haveapi/client_example.rb`: `ec7bbe9630f45b2a39e9cc431dae6be9f100155685916df24e6e030bcac2db48`
- `servers/ruby/lib/haveapi/client_examples/http.rb`: `53eba4eb9d8a37695274c13ded0e424d91c747c5660475e0dddc5a8880037c41`
- `servers/ruby/lib/haveapi/client_examples/ruby_cli.rb`: `6572cbf2f83242f389c231b11a826d20844265227e105c90069a445f6f45cf43`
- `servers/ruby/lib/haveapi/documentation_search.rb`: `1d659809c44314f7dd55da02ea7ebfc5427dad527d30bee0c8e4a4cc8b32ea9f`
- `servers/ruby/lib/haveapi/shared_documentation_helpers.rb`: `a43c191aaf40de61fd8d0181276026c5ed2cba4b89f1c9f906f13b5da7402437`
- `servers/ruby/lib/haveapi/views/documentation/search_form.erb`: `6cc0dbfff41b575d5f03de01c88c698f9fe4505e6cf8f5035f50d344952023c3`
- `servers/ruby/lib/haveapi/views/documentation/search_results.erb`: `2801c9bbefb03ea3c07b14fe632a0d9e924b1a935b03e4bcb8757a86fa7f4c07`
- `servers/ruby/spec/client_examples/presentation_spec.rb`: `40249b32c854868149e3694149afe6f2bd30de931bcdf49700a7a3d120bcfc81`
- `servers/ruby/spec/documentation/fixtures/search_index.json`: `7bb76232373ecfb9b2d79d0a6b8b1d31e83b6a8019f31097fe1d6e83bd62d1ba`
- `servers/ruby/spec/documentation/search_routes_spec.rb`: `780854148729db44681d29c7dac7a7606db78c44c95668a9e9582187329cbe07`
- `servers/ruby/spec/documentation/search_spec.rb`: `b366861ed293ca9d7862e00225392e7df95246e8063d74fa32d63f5e035191d2`
- `servers/ruby/spec/documentation/shared_pages_spec.rb`: `1c31ca38075bae949ac80d7b48f2411eb856230ecd08a04abf7e11656ece1314`
