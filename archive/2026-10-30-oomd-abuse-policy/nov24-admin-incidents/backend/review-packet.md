# Nov24 backend review packet

Source remains based on integrated4062a8da3314aa7b48170b0d6f441446bad9b207.
Two new admin-only read APIs share SQL projection with bounded optional daily
summary. Exposure membership/count/limit/filter/order/total/page facts are selected
in one statement before presentation; metadata always reports cutoff/read time.
History retains original saved facts and separately derives current native stop
and mail confirmations. No selectors or reconciliation run on reads.

Internal daily rows are flat; API exposure wraps selected VPS/User/Node references
with ordinary unresolved HaveAPI metadata. History retains raw original IDs for
missing/deleted associations. Root-authored EN/CS metadata, validation strings,
text template and feature docs are included. Site template and pure fixture are
separate published7af51cd dependency, tested in the actual shared builder seam.

## Documentation placement

API/policy/daily semantics → developers/operators → existing
`docs/incident-escalation.md` (already linked by docs/README.md). Covers current
versus saved facts, count/history windows, snapshot limit, SMTP/shutdown identity,
null/cap/older producer and compatible rollout/rollback; no schema removal.
Individual run evidence stays here; no deployment receipt in product docs.

## Verification

See checks.json for actual per-invocation commands, results and retained failures.
Core final projection/resource source:18examples0failures/native0/158.136s.
Full mode meaningful cases passed in corrected finite segments; their counts
are overlapping and must not be summed. Final shared pure fixture+actual HTML
and built-in text, six variants:2RSpec examples including endpoint inventory,
0failures/native0/51.059s. No SMTP/live service, browser or VM check.

RuboCop final11owned Ruby files0; normal generated i18n update/health0;
CI selector16runs55assertions0;429eligible API specs exact-once in shared full/core
matrix. New resource spec belongs to vps and model spec foundation.
Actual retained resident Ruby3.4.9/MariaDB11.4.13, not nominalRuby3.4.12 ABI.
Fresh utility preflight identity failures retained; active-parent fallback then
owned native checks and joins. No broad suite or CI-watch campaign.

## History and migrations

Append only after already integrated4062; original four incident purposes and
all supported deployed/public identities remain literal. No obsolete fixup commits
from this work. New purpose commits and full diff will be attached after commit.
No migration/schema/engine/node/recipient change. Consumed20261030180000 remains
SHA2562eec970fb3620ad25f3ac01c06a9eae61af2d208f88184e995c74b8ad2ba2c1e;
obsolete20261115120000 remains absent. No default integration/deployment claim.

Final source/publication: `74c0af3aef3ec9124ca89ce7669ccd9b99633495`, tree
`c2e2de2d3e3a63cc14f122f0f43641cb0898e569`. The two appended purposes are
PHP `73cd5d37b54c8d807752edae722c61876eedbaed`, then API `74c0af3...`.
Both normal-hook commits passed. The full25path diff and original authors/messages
are in full-base-head.patch/history.txt. Full binary diff SHA256
`aa8b57033b1452c0d6668cec392264d19c7076f439f74a3ac53c4c8497503676`.

Clean final API7/protocol2/fullfixture/all6plugins/en export passed once in44.778s:
529actions/156resources/9031parameters. Raw schema/provenance/tooling lock retained
under schema-export. Unchanged exporter/profile/tooling did not require a replay.

Canonical SSH feature publication used independently observed4062 predecessor,
scoped create-only observation refs, immediate identical tuple and explicit lease;
one normal hook-enabled push0 and independent readback prove exact74c0. Immutable
GitHub commit API confirms treec2e2. Master remains4062. Every protected ref before
after push is identical; no default or consumer mutation. Supported comparison
capture binds4062..74c0. One automatic CI exact-head snapshot found five runs
queued/in-progress, no pass inference or followup observer. See receipt.json for
source/history/export/publication/effect and exact handback; independent review,
client synchronization and rollout remain root-owned next phases.
