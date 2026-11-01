# KB 0.31.0 focused verification — 2026-10-27

**PASS: local mechanics and focused consumer checks.** Lead owns final prose,
commit and independent review. Production/staging writes were not performed.
No project, cluster, provider, source/ref/lock or shared-index mutation occurred.

Identity: ambient `DEV_SESSION_*` variables were both absent; `dev-session
current` from this exact tracking directory matched the trusted thread binding
`2026-10-24-vpsadmin-haveapi-upgrade` / `/home/aither/workspace/ai/vpsfree.cz`.
The live roster retained implementer3 with workspace-write access. Current
routed procedures, canonical KB workflow, installed tool help and previous
`prepare-release.rb`/fixture methods were read. A0 owned the sole watcher slot;
this bounded batch used the monitor skill's visible parent fallback, without a
competing utility or a wait longer than 50 seconds.

## Exact deliverables

| File | SHA-256 |
| --- | --- |
| `kb-candidates/cs/navody/vps/api.txt` | `b309b3ac851711914e7afffe3bf231547b9a5d690e8f1a103307280fef093bd2` |
| `kb-candidates/en/manuals/vps/api.txt` | `562acf4a703c6220f8584371b4cfad48bdac87adcc4ccb1a21503ac3fdf76f41` |
| `kb-release-cs.yml` | `cfcef28e861594d59556feab3505cac4a89f94cd72c8c4a27661f3a461a35722` |
| `kb-release-en.yml` | `8005961122f5e5a90c109e6caac115bc3ef087447b6a822751eb425a1245433d` |

Both candidates equal the saved final lead inputs byte-for-byte. Relative to
the prior 0.30.2 candidates, each changes three version references to 0.31.0,
adds TypeScript to the generated SDK overview/list, and adds the short generated
TypeScript section with the exact SDK 0.1.1/runtime 0.30.2 install pair. Python,
TypeScript and Rust executable snippets are unchanged; authentication through
EOF and the original documentation/login instructions are unchanged. Local
diffs: [CS](kb/cs-candidate.diff), [EN](kb/en-candidate.diff).

`release-changes.yml` now describes the complete release, including generic
0.31.0 and generated SDK dependencies, in informative localized summaries.
The writing skill and both pinned humanizers were applied directly to those
summaries; main article wording was not rewritten here.

Canonical schema-3 full-page guarded `content_replacements` rebuilt the complete
114 Czech + 77 English inventory: **191 unique pages, exactly 2 changed,
189 byte-identical unrelated pages**. Public `kb-contract-manifest --changes`
generated schema-5 manifests: one write each, no media/deletions or fabricated
managed provenance. Installed `KbRelease::Manifest` parsing and candidate
checksum reads pass; original-to-candidate whitespace checks pass. See
[canonical build log](kb/candidate-build.log),
[local inventory/guard receipt](../package-d/release-local-check.json), and
[manifest parser check](kb/manifest-parser-check.json).

## Source guards, history and semantic applicability

Read-only production page-info/content/page-info checks at 19:30:24–25 UTC
agreed before/after and match the original source guards:

| Page | Revision | Original SHA-256 |
| --- | ---: | --- |
| CS `navody:vps:api` | 1783860648 | `8ea88de825d7b3823aee1d4ff8fd2704c9eb2f431cfbb944643927eabde3fd13` |
| EN `manuals:vps:api` | 1777543182 | `8006293f735a7e6f45c04d2d59ad82a003afa4547db1ddb38f380504e1e107d3` |

Originals and source inventory were not refreshed. Source index SHA-256 remains
`87c999835a1015665ed985ce2f85e8f05348ae7f11e7c93625538933af6709d7`.
Evidence: [production source recheck](kb/production-source-recheck.json),
[focused content check](kb/focused-content-check.json).
Before regeneration, the exact prior eight-file bundle from workspace commit
`7d5ac6860e0640f1904014a5d1ecf51ac4af0d48` was preserved with file hashes in
[historical receipt](kb/prior-0.30.2/receipt.json). Earlier Package D histories
remain unchanged. Old consumer checks are not represented as new 0.31.0 checks.

Both final pages retain exactly one `<page>manuals:vps:api</page>` marker.
Installed generation intentionally emits the reciprocal `language_counterpart`
field on English only. Neither page is managed in contract registry reference
`873758fd6aec0c03f50a94600e0ceab97946f255`.
Manual navigation enumeration remains applicable: top-right login concerns
HaveAPI documentation at api.vpsfree.cz, not PHP/React vpsAdmin, so binding it to
`session.login.open` would be false. Introductory WebUI equivalence is explanatory;
CLI/FUSE examples are shell actions. New client paragraphs/install commands
contain no vpsAdmin WebUI-action instruction. No new semantic binding or
screenshot is needed. The previously recorded unrelated annotation baseline
limitation is unchanged; no new all-page annotation-pass claim is made.

## Published artifacts and actual new consumer checks

[Implementer2 facts](release-client-facts.md) and architect acceptance
(`design.md`, 0.31 client distinction) agree: generic Python/npm 0.31.0 is
distinct from generated SDK 0.1.1, whose exact peer is `haveapi-client: 0.30.2`.
No SDK support for runtime 0.31.0, synchronous callback HTTP, or generation by
0.31.0 is asserted. Published archives were downloaded again and verified
against registry integrity and the fact sheet:

| Artifact | SHA-256 |
| --- | --- |
| Python 0.31.0 wheel | `016a08dfe2ca6c629034bb2308267c234a21cb00edda019bd56a206e8c1e1aca` |
| npm generic 0.31.0 | `1f01aea5cd29415013b21cbe763ae5823d6889d8b6a93567916801ac50705af3` |
| npm generated SDK 0.1.1 | `9d262825d1dffb695eaace8029e3e7eb03a44338131602822907632945f566e8` |

- Python 3.12.12: fresh install of that wheel; exact CS/EN snippets syntax-compile
  and run with controlled HTTPX; fake token header, API 7 route/limit query and
  mapping output asserted. Separate async method check passes. Public imports
  and Python >=3.11 remain as documented.
- Node 24.21.0 / TypeScript 6.0.3: fresh generic npm 0.31.0 install; strict
  compilation of both exact snippets and execution of both compiled outputs
  against the published UMD with controlled XHR pass. Prior compiler/types and
  captured public schema were reused as tooling/fixtures, not old result proof.
- Generated SDK: separate clean install of SDK 0.1.1 plus exact runtime 0.30.2,
  no force/legacy-peer flags; `npm ls --all` clean. Strict NodeNext compile and
  actual ESM root import/construction pass for `createClient`,
  `createVpsAdminClient`, `createHaveApiExecutor` and versioned API base. This is
  install/import/type acceptance, not a new authenticated generated action test.
- Installed npm bytes match all 53 generic 0.31.0 files, 1358 SDK files, and all
  53 files of its 0.30.2 peer's verified archive. Rust guidance/snippets are
  unchanged; no Rust compiler rerun was performed.

All ten sequential consumer steps exited 0; retained parent handle 33966 is
complete. Evidence: [commands/results](kb/consumer-status.json),
[raw log](kb/consumer-check.log), [Python result](kb/python-check.json),
[artifact hashes](kb/artifacts.json),
[installed archive comparison](kb/installed-archive-check.json).
No benchmark, generator, browser, live authenticated API or long integration
campaign was run. Archive integrity is not signature verification or complete
source/archive equality. Unchanged earlier link limitations were not rechecked;
this receipt does not assert that every historical article link returns 200.

## Staging and handoff

Read-only `kb-stage status` reports owner `2026-09-13-auth-email`, container up
and that owner's pending EN release. Ordinary staging by this session is
currently unavailable; no claim/start/reset/stop/release/write was attempted.
Rendered staging review and exact production approval remain future lead work.

Lead may commit the two candidates, two manifests, localized changes file,
this compact receipt and the current-pointer addition in `kb-validation.md`.
Originals remain byte-identical and need no new content commit. Full mirrors,
indexes, plans, archives, installs, fixtures and logs remain local evidence.
No staging/production or lifecycle action is implied.

Session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/>.
