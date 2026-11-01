# Package B3: released context ownership contract

2026-10-26. Source/quick acceptance complete; ordinary hooks and commit passed.
R1 remains open until committed-source independent review and separately
assigned consumer timing/isolation acceptance. No full GET has run for B3.

Session/environment matched `2026-10-24-vpsadmin-haveapi-upgrade` in
`/home/aither/workspace/ai/vpsfree.cz`. B remained frozen while implementer0
owned A3 history/setup. Explicit lead handoff supplied clean vpsAdmin head
`47946f8c0731ee464f079d955c67b768ec895411`, A
`44393c352fbd5e9247850ed8490f369999553d62`, with no active/uncertain operation.
Only `docs/api-client-examples.md` changed afterward. Profile configuration,
registry hints, SDK identities, full-page consumer test and its selectable
`:documentation_profile` examples remain unchanged.

The current docs paragraph describes released 0.30.2 ownership semantics:
unchanged owned context fields are reused; explicit replacements are copied;
container/string data detaches mutable children of shallow-frozen inputs. Rust
looks up the selected action/provider from request-authorized descriptions.
Context reuse is not a page or authorization cache. The paragraph makes no
latency claim. Lead directly applied the required writing skills and supplied
the exact final paragraph before commit; remaining docs are byte-preserved.

## Actual installed-code identity and bounded ownership

`installed_identity.rb` ran from the effective API Nix/Bundler environment,
not an upstream source checkout. It required the real released gems, used method
source locations and compared SHA256s with expected source at HaveAPI release
tag v0.30.2 / canonical `321ce8256ad4704efaed04f4f2aa1ea4c2a3b4b8`.
Architect artifact-to-source assessment supplies the released artifact boundary.
All four loaded gems (server, Ruby client, Go generator, Rust generator) are
0.30.2. Loaded files:

- Context: `api/.gems/ruby/3.4.0/gems/haveapi-0.30.2/lib/haveapi/documentation_context.rb`,
  SHA256 `f43fa0a9b04b23c0181585b025d09692c591ff875ab494f1cddad9f82295c523`.
- Rust: `api/.gems/ruby/3.4.0/gems/haveapi-rust-client-0.30.2/lib/haveapi/rust_client/documentation.rb`,
  SHA256 `51d2700f81a272c696d3d691c68fff31f967ddc93b5bcabe288265002d5142eb`.

`installed-identity.json` retains the absolute real paths, gem homes/versions,
Ruby executable and version, effective `api/Gemfile.lock` hash
`d9e69553a7a705ed64751e742bcd345de5147d85301f6397db378c12a3055202`, packaged
API lock hash `2777ee2e78970ea4f930150d8dc19155ba03ffc1bbb99e7f1004269bf74276ad`,
flake lock hash `d455fbfe340fc2f87a5c7dd5e7cd068a6c21a19e6aee52f9d3286b5a2b6bbfea`
and complete Nix input graph. This proves the consumer loads the released fix;
it does not itself establish request latency or all authorization behavior.

Eight bounded ownership predicates passed: shallow-frozen child detachment,
caller children stay mutable, unchanged description identity reuse, frozen
parent/derived contexts, explicitly resupplied description is copied, changed
sample input detaches, parent/sibling isolation, and frozen replacement children.
No public-route mount, compiler, request cache or HTTP version page is involved
in that ownership check. Arbitrary non-container/profile reference semantics
are not claimed to be newly deep-frozen.

Initial launcher used the wrong directory to write its evidence script; the
subsequent Ruby invocation found no script and exited before checks. The failed
command ended normally and is preserved as `script-path-failure.log`. The script
was then written at its proper session-local path; no failure was substituted
with a source-tree test and no repository source changed to make it pass.

## Quick verification and deferred gates

The actual installed identity/ownership check passed, followed in the same
API shell by `bundle exec rspec spec/lib/vpsadmin/api/documentation_clients_spec.rb
--tag documentation_profile`: **2 examples, 0 failures**, seed 30413,
16.1s examples / 12.47s load, command exit 0. See `quick.log`. This exercises
real vpsAdmin mounting plus upstream Rust async/blocking initialization and
registry hints. No new consumer copy of renderer logic or broad upstream test
suite was added. Whitespace check passes. The sole repository edit is prose;
ordinary root-shell Git hooks provide the repository's required checks.

No full HTML GET, warmed request, services VM, SDK compilation, upstream provider
edit, deployment, push or merge occurred. The original instrumented baseline
and receipts remain unchanged, including 174 results / 168 code / six Go
limitations, all 17 samples, and 102.376/49.716/139.036s request timings.
Post-review acceptance must bind every role/locale to final head, effective
source/locks/API/plugin shape and compare output, with only the separately
approved Rust Git-to-registry comments allowed. Warm uninstrumented requests
remain separate. None of those pending gates is implied by source adoption.

## History

Pre-doc A3+B head `47946f8c0731ee464f079d955c67b768ec895411` remains at local
feature ref `2026-10-24-vpsadmin-haveapi-upgrade-before-b3-docs`.
`pre-doc-commit.txt` and `docs-delta.diff` preserve this supplied range and the
single-doc change. Earlier `57a53e700132d43589f4e6bcf519f1c7ec3fd2ed`,
`21872fe6ad373e52f66f193ee432f4885376e5a5` and prior evidence remain preserved.
Amend retains B's original author and 2026-10-24T22:19:22+02:00 author date.
A3's exact dependency commit is not modified. No rebase/fetch/default update,
new migration, schema, wire protocol or SDK generation is part of B3. Complete
branch history/range comparisons and final head follow after normal hooks.

## Final exact range and handoff

Base: `b82eeca50cd4dd7bd76728685c7de8aad66e7ba5`. Final A3 remains
`44393c352fbd5e9247850ed8490f369999553d62`; amended B/final head is
`70a2ed54b98d0c2f359a9cc4484452a257a9807b`. B retains original author Jakub Skokan
<jakub.skokan@havefun.cz> and author date 2026-10-24T22:19:22+02:00.
The new commit message matches supported 0.30.2 ownership guidance.

Normal root Nix / plain `git commit --amend -F` exited 0. All declared
pre-commit hooks and every commit-message hook passed without warnings.
`commit.log` retains exact results. Worktree/index clean; no active owned
operation remains. Only docs/api-client-examples.md differs from supplied
47946f8c head; no consumer spec/config/SDK changes.

`handoff-range-diff.txt` proves unchanged A3 and the single-doc B difference;
`reviewed-range-diff.txt` compares the prior reviewed b82eeca50..57a53e700 range
with the final complete range. `final-history.txt`, `final.diff`,
`final-files.txt` retain whole A+B inventory. Prior source/lock/browser pins are
consolidated by A3; no obsolete active pin updates remain. No database migration
or schema path changed in the complete range; therefore no introduced migration
was merged, released, deployed or externally consumed. No deployment occurred.

Independent final affected review must precede full GETs/long tests. R1 is still
open; source adoption, bounded ownership and tagged specs do not close consumer
performance/isolation acceptance. B3 source/Git ownership returns to lead.
