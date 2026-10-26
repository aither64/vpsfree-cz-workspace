# Existing adapter behavior relevant to performance gates

Read-only source evidence recorded 2026-10-25 at HaveAPI
`b85ec364057f536940d689b09e612512ffffaf82`. Prepared server bundle resolves
ActiveRecord/ActiveModel/ActiveSupport 8.1.4 and sqlite3 2.10.1
(`servers/ruby/Gemfile.lock:33-39,224`). No runtime query measurement has been
performed for this finding.

## Default association includes use a mismatched reflection key

- `servers/ruby/lib/haveapi/model_adapters/active_record.rb:160` looks up
  `self.class.model.reflections[p.name.to_sym]` when deriving default includes.
- Prepared ActiveRecord 8.1.4's
  `.gems/gems/activerecord-8.1.4/lib/active_record/reflection.rb:78-79` defines
  `reflections` as `normalized_reflections.stringify_keys`; its comment at line
  76 shows string keys.
- `with_includes` combines explicit includes with those defaults at adapter
  lines 28-42. Without explicit includes, missing defaults can leave association
  reads to issue one query per returned row. This is a source-based diagnosis of
  possible existing N+1 work; exact runtime counts still require calibration.

The lead retains this as baseline characterization. This performance-suite
package does not change production adapter behavior. Hard fixed-query gates use
scalar pagination and explicit direct/nested `_meta.includes` lanes. An optional
unresolved-association lane must record its measured existing linear query count
rather than assert constant work or conceal it with fixture-side preload logic.

## Preserve authorization work while measuring SQL

Adapter lines 365-370 instantiate the associated Show context and call
`authorized?` and `show_prepared?` for each associated row. Fixture authorization
must preserve those checks without introducing its own per-row `find` query.
Associated Show execution is not part of this serialization path. Query capture
must cover actual uncached request SQL, excluding schema/seeding/setup.

## Pagination size boundary

`servers/ruby/lib/haveapi/actions/paginable.rb:3,14` caps validated `limit` at
1,000. Weekly 1,024-row coverage therefore needs an unpaginated list lane or an
explicit pagination cap; it must not silently benchmark a rejected page request.

Evidence was obtained through source/lockfile reads and numbered excerpts only.
No source edits, connection changes, query experiments, tests or installs were
performed. Architect owns the final scenario contract; lead owns tracking.
