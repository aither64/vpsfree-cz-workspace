# codex-web dependency handoff

Published feature preparation is complete. This is not combined final review,
native acceptance, deployment or default integration.

- Canonical repository: `git@github.com:aither64/codex-web.git`
- Feature ref: `refs/heads/2026-10-24-workspace-session-ui`
- Preservation base: `8b60554bc10c2a6bcbf9732a8b77ad959c317036`
- Published final head: `975746f40fe99c77689ede064197772e2cc25c18`
- Final tree: `83ccb29c909db3f5acec1e15cdf8f6d7ab8e8082`
- Fresh SSH remote master remains the preservation base. Feature target was
  absent; publication used its exact absent-ref lease, then fresh SSH remote
  verification matched the final head. Own worktree and index are clean.
- Git/index/publication window released. No default branch was pushed.

## Complete history and source mapping

| Logical unit | Commit |
| --- | --- |
| Entire published native retry/proof source delta | `643898a4e010269ce8ea3f6b730eb0a7288f9e93` |
| Explicit prompted API, shared runner, catalogs/provenance, native selectors and docs | `a2036cf9fbb8dd4d0b3fc67516f98af86753e460` |
| Exact wrapped capacity predicate and proof/raw-error regressions | `b5bef65adf40ec1b0199352edd5cf2666d1fc426` |
| Separate disposable two-binary state fixture and guide | `975746f40fe99c77689ede064197772e2cc25c18` |

Source range `872c7ad3962f9fa9b17358244e27f3e3fac59fc5..801099102ef9af4a82c1f3853c53d6b442ecd4dc`
was imported onto the current preservation baseline, not selected as an old pin
or substituted wholesale. Original source commit and import have identical
stable patch ID `3922626df4b8d48127ebd5889187ef56d44f0a7c`. The original source
commit is not a literal ancestor of the final feature; its delta was imported.
Subsequent API/capacity work is substantive and does not claim whole-branch
patch equivalence. The authoritative current-session source intake found all
24 source snapshots identical to the published blobs, with no unpublished
unfinished source: [intake](../naming-source-intake/20261025T163000Z/intake.md),
SHA256 `51ffd5670f6915da2b9d29a2f19209b6178d10a2f0ba5b044b1ceba011534818`.

Full evidence: [history](final-history.txt), [final diff](final-base-to-head.diff),
[source range comparison](source-range-diff.txt), [13 changed paths](final-changed-paths.txt),
[history/migration inventory](history-migration-inventory.json),
[baseline preservation](baseline-preservation.json), and
[publication proof](publication-preflight-and-proof.json).

There are no new or rewritten migrations, no dependency pin changes and no
repeated/superseded pin stream in this series. Existing merged SQLite storage,
admission/delivery, module dependencies and submission guide are preserved.
`client.go`, `turn_state.go`, `go.mod`, `go.sum`, `flake.nix` and `flake.lock`
remain byte-identical to the base. New native state fixtures are not production
migrations. Existing SQL equality does not prove native reader/write compatibility.
The independent reviewer still owes the combined whole-history/migration conclusion.

## Consumer receipt

Canonical module lookup through the Go proxy/checksum service resolved:

```text
github.com/aither64/codex-web v0.0.0-20261025170722-975746f40fe9 h1:2JhpRICwnTUC+EhxaTxVeh0/a5DycGX8f+6vcUhsmkg=
github.com/aither64/codex-web v0.0.0-20261025170722-975746f40fe9/go.mod h1:z4to20c2m2G4k2YusCQCw3g7z1g63EugO4dmjTgo+dM=
```

The lookup's origin is the exact published final head. Receipt:
[go-module-download.json](go-module-download.json). No worktree module file was
changed by that lookup.

Public additions are `Client.RunPromptedEphemeralTurn(ctx, EphemeralTurnOptions)`
returning the existing result, `CanRetryEphemeralTurn(err)` imported from the
source, and `IsCapacityFailure(code, message)`. Prompted naming supports only
Luna/low on raw 0.164 and shares the bounded private runner/sink. Fixed settings
remain defense in depth; native tools can remain available. Prompt instructions
are not tool-effect isolation. Strict `RunEphemeralTurn` remains supported on
0.163, with its native empty-tool/absent-handler assertions retained.

The capacity helper accepts typed `serverOverloaded`, or only `other` with the
exact full reported wrapped capacity text. It does not normalize text, change
raw failure fields, authorize fresh execution, reset budgets or add a scheduler.
Runtime owner1 projects positive classification only into its existing retry
policy input and keeps all normal continuation/admission rules.

Reuse canonical catalogs; no artificial bytes or duplicate JSON resources:

| Resource | Bytes | SHA256 |
| --- | --- | --- |
| `codex/testdata/ephemeral-models.json` | 472072 | `943ca7fe1d19ed019054158303f0dbbd80b3bef43b3aa425a71aa7cb3fb52c2b` |
| `codex/ephemeral_luna_models.json` | 62680 | `049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1` |

The strict original provenance is unchanged; separate prompted provenance and
the revised helper reproduce/verify both releases. Equal content hashes cannot
identify a native release or establish its tool-isolation behavior.

## Exact native and input provenance

[final-source-input-graph.json](final-source-input-graph.json) contains the full
library lock graph, module identities, source mapping, preservation and hashes
for the complete retained prerequisite derivation/input/source receipts.

- Frozen llm-agents: `ea188d2f072e0ec8d5b71245e228803672801a22`.
- Raw Codex 0.164 source: `6aaac694803004a63c6f393d153c96d22521a6b9`;
  source NAR `sha256-iib2+qQcGewC4Ga8cA80sInDJpzdSxDJP0y1DDOouI4=`.
- Exact executable:
  `/nix/store/16f481b2zzvyvr2ycw51sm51b3f0508f-codex-0.164.0/libexec/codex/bin/codex`;
  SHA256 `d2af1cd0ea4187d413c237e80204e94ffcd5c7d8142840a662156b89750f54ae`.
- Derivation: `/nix/store/w0byl70npn8n740k0cqv0nca24kakn6i-codex-0.164.0.drv`.
- Existing stock daemon store patch remains in the EA recipe; no custom patch
  or new Rust build was made. Conditional older-version webpki patch is absent.
  Stock patch/postPatch touch neither schema, catalogs nor tool router.
- Raw prerequisite roots and full graph receipts remain in
  [native0164-prerequisite](../native0164-prerequisite/). Final runtime assembly
  and actual executable/launch equality are consumer/rollout gates.

## Executed checks and limits

The parent-owned final short-TMPDIR batch passed once: full untagged `go test
-mod=readonly ./... -count=1 -timeout=180s` in 29 seconds, then the enumerated
non-native tagged helpers in 8 seconds. Native opt-in environment was absent.
The tagged stage compiled all tagged source but executed only state fixture
file/hash/snapshot helpers, prompted schema observation, and the exact existing
base-instruction/tool/schema/registry/persistence/SQLite/overload-advice helpers.
It did not run an App Server, native upgrade, namespace campaign or provider canary.

All 136 final committed files and both flake files matched the passing manifest
before/after: SHA256 `bb6792edaf72b18df8dc842a977ea912b6de48aae1fdf18ede7b91160d925ef7`.
[final-tested-tree.json](final-tested-tree.json) additionally proves the exact
committed tree has the same complete path inventory and bytes, without extras.
Final batch: [result](final-quick-tmp-v2-watcher-result.md),
[environment](go-nix-env-naming-tmp-v2.log), [untagged log](go-all-naming-tmp-v2.log),
[tagged log](go-tagged-helpers-naming-tmp-v2.log), and corresponding exit receipts.
Owned short TMPDIR `/tmp/cw.krSzRe` is recorded in
[go-owned-tmpdir-v2.txt](go-owned-tmpdir-v2.txt) and retained; no cleanup occurred.

Other executed evidence: exact raw 0.164 generated schema/request corpus PASS;
call-site coverage PASS; 55 fixed restriction/config checks PASS for exact
0.163 and 0.164 sources; catalog reproduction/identity PASS for both; changed
Python parsing, gofmt and whitespace checks PASS. All 109 browser contracts
passed on unchanged browser source and remain applicable. No declared hook
framework or active commit hook was found; ordinary hooks were not bypassed.
All four commits used temporary message files.

The initial missing-GCC failure and later 109-byte Unix socket path failure
are preserved with source-supported diagnoses. The corrected batch entered the
declared Nix stdenv/Go/GCC environment with CGO enabled, then used a new private
short TMPDIR. No assertion, skip, timeout, source or SQLite workaround was used.
See [socket diagnosis](unix-socket-path-diagnosis.md) and earlier
[0.164 evidence](../codex-web-0164/compatibility-evidence.md).

Main-agent prose pass final hashes:

- `docs/reference.md`: `7425ca593194490a64567d2d3feaf29ed72c810bc0a816112c0823ad62ce6037`
- `skills/update-codex-web/SKILL.md`: `74238fa1eff0b37118700a43bf8febc56b6b8aeeccfb5c5cf584a1d046496a06`

Next: owner1 selects this exact dependency with raw EA 0.164, regenerates the
module/vendor inputs and aligns prompted naming/capacity/runtime prerequisites.
The parent completes intended consumers and combined independent final review
before longer native/state/managed-child/real-provider acceptance and any
rollout. No default integration, native patch, machine claim, activation,
lifecycle action or source-session ownership was adopted here.

[Stable session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/)
