# SDK final review: lead record

Original final review completed by retained independent reviewer0, assignment
e1be4e1f-ce62-4512-97f8-b80388735a57. This is a lead digest of the full report
returned in the conversation, not a verbatim reproduction.

Reviewed complete ff876abe17e3301da62c1b6afbda055ec89db9d2..e370b39e2134c1a7e2634698e6911a0f77ad9550,
tree b6d358936f9fd2bbd4606ee8b2a8d3e380e209b8. HIGH/all four lanes, actual
saved gpt-6.1-sol/xhigh/read_only, roster34, thread01a16406-faaa-7cd0-bde3-c20802c18a72,
project01a16406-fa76-7532-9ee4-a890352500df, no overrides/fallback/nested agents.

## Finding and decision

One Important architecture/repetition finding in6adb22b2: Cargo lock restoration
validation duplicated in ci.yml79-93/141-155 and release.yml91-105. Bodies
currently agree, but future identity/integrity fixes can miss publication.
Accepted remedy: one SDK-owned restore helper at all three sites, committed
focused controls, exact existing contract/arguments/credential timing preserved.
OPEN on original reviewed head. Owner3 execution2f6d98ba continuing9eec3256.
Lead inspection and focused checks suffice under mandatory-change-review step9;
contract expansion requires affected-lane review step10. No Blocking, other
Important, or Advisory findings. This report does not accept a future fixed head.

## Independently established conclusions

- Complete three commits92698284/6adb22b2/e370b39e have coherent split: released
  replay/provenance; coordinated Cargo input/workflow/docs; mechanical ownership.
  No obsolete approaches, repeated successive pins/fixups, or superseded history.
  No migrations, data/schema/protocol transition, or transitional lineage.
- All711 live tracked files match blobs. Full diff matchesc16ebee7. All686Rust,
  including8runtime, equal base. Schema/inventory/options/Cargo constraints,
  edition/MSRV/formatter/Nix inputs unchanged. Only3 generated identity fields
  and corresponding capture generator provenance change.
- Official retained manifest54816d85/source1c3/embeddedlockf35d5ad2 and actual
  restored lock agree. Independently reconstructed generator digest9b60df3b
  matches. Schema70f89335 remains unchanged.
- Replay helper belongs to SDK consumer; verifies local fixed manifest/source/
  version/tag/lock/cleancheckout and writes only ignored generator lock.
  Identical regular bytes idempotent; conflict/symlink refused. No silent fetch
  or resolution. HaveAPI retains generator/runtime ownership.
- Ignored retained local Cargo.lock equals base lock. Library Git policy permits
  a native .crate lock. CI owns native resolution once/run and transfers exact
  artifact/SHA/source/run/attempt; publication does not independently resolve.
- Ordinary CI package is before protected approval. Credential-free native
  dry-run candidate is produced AFTER protected job admission, before credential
  acquisition; it is not pre-approval evidence. Candidate/actual native archives
  retained separately, output moved to avoid substitution, actual output kept
  even on failure. Exact identity/dependency/runtime/VCS checks assessed.
  Clean VCS dirty may be absent/false, rejects true. Divergence after upload is
  irreversible and requires registry reconciliation, no automatic retry.
- Bootstrap/OIDC explicit with no fallback. Missing crate and token required for
  bootstrap, lookup uncertainty stops. Credentials confined to native publish.
- Docs/prose/placement explain lasting source ownership/frozen setup/local lock/
  release stages/recovery. No additional issues. No duplicate real-server campaign
  needed under unchanged independently proved schema/Rust/runtime boundary.
- Reviewed environment JSON: reviewerUser4717906/aither64, wait0, preventselfreview
  false, ordinary admins bypass true, custom tag-only v* policy. These do not
  enforce initiator/reviewer separation or prohibit admin bypass. Fresh absence/
  compare/no blind overwrite/readback plan accepted. Repo environments/secrets
  empty, org secret403 => inherited bootstrap UNKNOWN. No values requested/read.
- No default integration authorized or required; feature tag/manual dispatch
  design valid with existing default workflows. No deployment/coordinated update.

## Evidence limits and remaining execution

Owner8setup/generation phases0/92.28s, helper8, regeneration/determinism/format,
18syntax steps, session12lock+4provenance controls assessed, not reviewer-run tests.
No compiler/package/MSRV/hosted CI/upload proof yet. Corrected exact head must
pass default/blocking/docs/MSRV1.95/package with same retained run graph, then
immutable tag/release verification/environment+credential prerequisites/native
candidate/actual publish/independent registry archive/docs.rs observation.

Reviewer ran no tests/network/setup/Git/source/cache/session mutation. Terminal
source-read yield explicit, no command/child/pending operation. Owner3 may fix.
Session remains open; no lifecycle or main integration authority.
