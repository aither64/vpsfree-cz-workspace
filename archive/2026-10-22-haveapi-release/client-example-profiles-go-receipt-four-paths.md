# Go profile package source yield

Assigned Go implementation and known-quick checks are complete. Source is yielded
to sole Git owner0; owner2 authorizes hooked commit of these four exact paths as
part of the combined package under the lead conditional four-commit grant,
now satisfied by checker PASS/yield and owner1 command-free readiness. No
additional lead permission gate remains. No Git mutation
was performed by owner2. All operations are terminal and command-free.

Worktree: `haveapi-client-example-profiles`, branch
`2026-10-24-haveapi-client-example-profiles`, HEAD
`4dc0f7e11c494d1a0dc852dabcc312411699fcab`, tree
`a5c78fa77f4647e75d3f485ab12d7657bfcfab01`. Index remains empty;
other owners' source is preserved.

| Owned path | SHA-256 |
| --- | --- |
| clients/go/lib/haveapi/go_client/documentation.rb | 9fc0cb67a8fec31ede747a02e1887e2e86d590410a139e4d5a3a9c42e05afbf2 |
| clients/go/spec/unit/documentation_spec.rb | 5ce62b84cf2f5e577ed9d95e7e0c4c3febd0ed4289c7f317b2f6be924d666f33 |
| clients/go/spec/documentation_profile_check.rb | 6bfc0f4db2304e534ecdf46dceac1f07787a1d7c4dbe8ae12647cb0f328ad704 |
| clients/go/spec/support/documentation_profile_fixture.rb | 8da6183f1f0a84caa123b943060187f3afdf3552a1b666830528c5b2682b3e27 |

The adapter accepts omitted/nil module_version, preserves nil internally and
prints `go get IMPORT@latest`; explicit validation/behavior is retained. It uses
the existing ApiVersion model/resolve/render seam. The separately lead-approved
Resource comparison converts only String/Symbol value_id/value_label to strings;
all other values and type/nullable/resource comparisons remain exact.
No generator, naming allocator, SDK runtime, wire contract or shared schema was
changed by owner2.

Validation:

- Focused unit RSpec: **62 examples, 0 failures** (`unit-02`).
- Mounted real-DSL standalone checker: **exit 0, 2.13 seconds** (`profile-01`).
  Covers complete sibling/action collisions, nested paths/Resource fields,
  metadata guidance, authorized public/privileged/public sample replay, hidden
  actions/defaults, hostile literal escaping, null/omission/false/zero,
  omitted/explicit versions and legacy saved JSON.
- RuboCop: **4 files, no offenses** (`style-02`).
- Syntax: **4 files valid** (`syntax-01`, with changed test/fixture rechecked by
  `syntax-02-unit` and `syntax-02-fixture`); whitespace check passed.

The initial style-only failure is preserved; duplicate regression bodies were
consolidated and two HaveAPI sample DSL blocks explicitly identified for the
RSpec cop. Both the initial and final unit runs passed 62/0. Full argv, timing,
raw output, file identities and evidence hashes are in
[the JSON receipt](client-example-profiles-go-receipt.json) and
`client-example-profiles-go-quick/`.

Commands ran only through owner1's exact prepared `in_bundle.py` go-unit/server/
go-acceptance profiles. Ruby 3.4.11, Bundler 4.0.23, own gem homes and declared
selected tool PATH were verified from its accepted readiness receipts. The
optional dedicated ignored lock's SHA is 9854dbae73d4b299a255042bdb562f4ab56475c950ba0076cdf708e3d4b883c0:
owner1's accepted checksum-only completion from 17738ce7, unchanged nonchecksum
records and all 55 exact archive checksums. Other locks remain 450de01a (root),
cec5e86c (server), 23fa09fd (Go-unit) and 7f51e5ea (Rust).

Product docs are owned by owner0/lead; optional version/latest text, SDK/schema
compatibility assumptions and legacy override facts were supplied. No additional
product doc path was authored here. Existing unsupported Custom/list-input/
scalar-null limitations and required metadata checks remain covered by units.

No Go compilation, generated SDK, live API request, listener, dependency
installation or publication ran in owner2 quick checks. Compiled/rendered program
acceptance still requires committed final independent review and a separate
verification grant; this pure checker is not that acceptance claim. Version and
release actions remain outside this package.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
