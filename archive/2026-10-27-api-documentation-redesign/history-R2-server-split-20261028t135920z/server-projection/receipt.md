# Original-owner optional server integration provenance

Inspected C `d25dd61260a5768552bac5f6a8a201bb4c28d540` and final
`ab5b11188941d1c8c918951cdee162e9aa9f68cf`, tree
`c3c3e04337bcf9669dbb79611d72a65c686af9e0`.
The reported history defect is confirmed statically: C server contains the
optional documentation OAuth integration but the module is introduced in D.
C's documentation helper correctly uses ordinary `authenticated?`; that helper
is outside this projection and unchanged. No load/mount smoke was run here.

## Authoritative C/D bytes before performance E

For owner2's history reconstruction, use **`C-basic/`** as actual C server and
**`C-original/`** as actual restored D server, both at the repository-relative
`servers/ruby/lib/haveapi/server.rb`. These contain no E resource-context cache.

- C Basic SHA-256: `dc4a98da8e8af08105c3da39ec5784f630c40927c770fbe7e0c6501a357d0be8`.
- D restored/pre-E SHA-256: `bccf92fbdef347c0e1c55312358da9eb71db6c3ecf9865339fb56f89d837c317`.
- Exact `C-optional-documentation-oauth-server.patch` SHA-256:
  `dfeb48afca1bcf477d4f990f88a7df86bc5380fb3dbce8a5852e7808acd1e07c`.
- `C-reconstructed/` equals the restored/pre-E bytes after actual
  `patch --batch --fuzz=0 -p1`: no offsets, no fuzz. See `C-patch-replay.log`.

## Full final-server reconstruction proof

The separately supplied `basic/` and `final/` preserve final E cache behavior;
they are **not** the C/D staging bytes. They differ only by the same optional
integration blocks.

- Final Basic SHA-256: `ca1bb6f6b66e4469db86b2e158bf3c13041a09cac4c9f8dd3b83407f09041f98`.
- Current full final SHA-256: `814f1c234565c6aca3fe6393116c9850e4a65d01d6817d055c94c96e407f3410`.
- `optional-documentation-oauth-server.patch` SHA-256:
  `ebc44fe703479c8ff49e9742dc36f97b57cc105a95483074aa86db5f94081bf0`.
- Actual zero-fuzz/no-offset replay into `reconstructed/` equals current final
  bytes. See `patch-replay.log` and `source.sha256`.

## Exact seam inventory and preserved behavior

Each projection requires exactly one match for each of four blocks, in both
C and final sources:

1. `require 'haveapi/documentation_oauth'`.
2. Entire `documentation_oauth(**options)` configuration/accessor method,
   including the zero-argument getter, repeated/after-mount guards and instance
   construction. Removing only the require/helper/mount would leave this seam.
3. `helpers DocumentationOAuth::Helpers` registration.
4. `documentation_oauth&.mount(self, @sinatra)` after ordinary chain setup.

These total 11 lines. There is no separate optional `attr_accessor`, settings
registration or configuration-use reference in this server file. A complete
reference scan found no `documentation_oauth`, `DocumentationOAuth` or its
configuration-error prose remaining in either Basic server. Common
`Sinatra::Cookies`, ordinary provider/authentication hooks and API-server
settings predate or serve the ordinary server and were preserved.

The full-final minus C server difference is the existing request-local
resource-context cache only. Removing the exact same optional blocks from each
leaves identical added/deleted cache lines; both deltas are retained for owner2
to preserve E byte-for-byte. No search/navigation/Basic/provider behavior was
inferred or changed. All four block match counts and hashes are in `proof.json`.

The existing four-partial artifact directory remains authoritative and untouched:
`/tmp/2026-10-27-api-documentation-redesign-auth-history-m4-dr40ijim`.
Its final partials still equal working-tree bytes; their existing restoration
patch remains `c65ea2c5c0f4c4e5c734de9c184a67e1d043faeb2c05fc6b7235d0c145708568`.

The actual feature HEAD/tree/source/index were rechecked clean and unchanged.
Only temporary provenance files and patch replay copies were written. No app
source, Git/hooks, dependency, private-input, HTTP, OAuth/TLS, R1 or lifecycle
work occurred. Owner2 separately owns actual intermediate C/D load/mount proof
and history correction under its lead-granted slot.
