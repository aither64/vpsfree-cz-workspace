# P4 native SDK component evidence

Owner: implementer5, retained Sol/xhigh/workspace_write. Sole executing package;
prior P4-NATIVE-PURE accepted at `11888bcb6e37eaffe1cc0f3c99b92b4ccdf34e11`.
Committed and reported for lead acceptance at
`aec5bea24c6a1bf18dd5c7941617286c869e4c7d`. Main writing pass and exclusive index
window are closed. No current index ownership, active process, other executing/
parked package or next package queue. Capacity available with P4 fixes retained.
No push, activation or lifecycle action.

## Scope and source

The lead released only `pi-runtime/src/native-retry.mjs`,
`test/pi_runtime/native-retry.mjs`, and a narrow `docs/pi-providers.md` amendment.
Actual starting utility/B2 base was
`4c0bd9a0f97c15de76d45e8c5fe54a31ef7afce2`. Shared feature HEAD at final check was
`3872155b55688742355b8dc16b88584f4cb5a303`; it is the exact final commit parent.
Branch/worktree remain `2026-11-11-pi-codex-migration` / its registered D checkout.
No existing worker, Go runtime, transport, schema or controller file was edited.

The leaf exports `createNativeRetryRouting`, with actual SDK/ModelRuntime/
SessionManager, immutable policy/runtime/handle, trusted retry/failure/effect
adapters and existing `syncHistoryPrefix` injection. `attach` selects a private
public virtual model. `beginInput` requires exact full SubmissionRef, generation,
fixed original deadline and admission callback. Exported-Go type casing and
the native lower-camel witness/state projection match the saved brief and owner1/
architect1 clarification. SDK results contain only model/thinkingLevel, no state.

The component proves current public branch/user/failed-response/state identity,
then appends the exported native state entry, independently reopens and compares
the full new entry/parent/state/branch, and synchronizes file/directory before
returning the next physical target. Private provider retry zero, finite native
retry settings, virtual selection and compaction disabled are rechecked. No
host redispatch, new input ID, second ledger or private SDK method is introduced.

## Exact checked inputs

| Path/input | SHA-256 or immutable identity |
| --- | --- |
| `pi-runtime/src/native-retry.mjs` | `7262c5937beefa22c2c44d672ca9378f1d747c2190581b0762a620e6aae99eeb` |
| `test/pi_runtime/native-retry.mjs` | `0c7d66d18bb9915b5bcbda9a18a73739bdbe45fca6548029dd0974edba2e7bf2` |
| Final `docs/pi-providers.md` after main prose pass | `2f572ba5dc15cbe65a3c8163e221a69c56c5c387b30307402b54ec0933016fa0` |
| Existing `pi-runtime/src/persistence.mjs` | `041d8c607c276097033e699e8d3af5dc474d144742ab2a0b80ac6d5ef215c38f` |
| Existing `test/pi_runtime/package-api.mjs` | `43dccd59a1b24fb39fa2ca4d8fd32c086d096a8ec1b026475929d94a48994f0b` |
| Pinned Pi | `/nix/store/9hf2a7rz231w2pn50s4jlmrgs4007xc5-pi-1.5.2` |
| Pi source | `a22b888a58fe55b668cc45b80749ec88d4eb4ddc` |
| Node | `/nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node` |

Both new modules passed pinned Node `--check`. Owned tracked whitespace check
passed. No broad suite or Nix build/install was needed for these independent
public SDK modules. Source and fixture together are 430 lines before commit.

## Finite native fixture

Executed in D, with `PI_OFFLINE=1` and the exact Pi output above:

```sh
env PI_PROBE_PACKAGE=/nix/store/9hf2a7rz231w2pn50s4jlmrgs4007xc5-pi-1.5.2 PI_OFFLINE=1 \
  /nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node \
  --test test/pi_runtime/native-retry.mjs
```

Final result: exit 0, 19/19 tests, five top-level tests, about eight seconds.
Complete local log `/tmp/p4-native-sdk-final.log`; fresh Luna/low watcher
`native_sdk_final_watch`, tool session 80676, terminal and joined. No owned work
remains running. Installed watcher policy came from
`/nix/store/9hr3ppqzzwb12x51vwjasw8hq0ka7dab-dev-workspace-0.2.0`, schema6 catalog
`f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`, explicit
danger-full-access/approval never utility TOML. Each uncertain run used a fresh
watcher, with no watcher edits, diagnosis or retries.

| Boundary | Observed evidence |
| --- | --- |
| Public native retry | Physical calls A,A,B; one original user; prefix effect once; one gate; two state entries (initial zero plus hop1), no returned-state duplicate |
| History and selection | B receives exactly the same completed tool result as A; native assistant observations identify A and B; selected virtual model stays separate; global provider/model defaults unset |
| Cumulative budget | A,A,B,B, effects prefix/later once; second gate stops at original budget1; two state entries remain; C never called after successful B tool continuation |
| Partial/failed effects | Text, thinking and failed tool-call responses hold before gate; unsafe effect never runs; pending effect holds; paired-history insertion after observation holds before charge/target |
| Identity/state/cancellation | Wrong receipt/generation hold before physical call; malformed latest native state holds; cancellation makes no next call |
| Attribution/authority | Quota and unsupported exact code stop before gate; missing effect certifier holds before physical call; absent fixed deadline rejects before prompt; gate loss holds; textual refusal has no native retry or gate |
| Charge uncertainty | Sync failure leaves a persisted prospective row but only the initial verified charge, holds before B, never refunds/replays |
| Process death | Owned children exit73 before charge and74 after charge; A,A only, one user, one/two states respectively; fresh component refuses original operation resume |

Only two fake implementations/three physical targets are used. Credentials are
owned fake keys under temporary fixture roots; no real account/auth/model/network
request occurred. Host admission and effect evidence are explicitly fake SDK-only
fixtures. They do not prove production original Accepted/current-generation/
effect authority. Local logs and temporary `pi-native-retry-*` histories are
disposable review artifacts, not tracked source or live session histories.

## Failed attempts and correction provenance

The first finite run exited1 (~5s, `/tmp/p4-native-sdk-first.log`). Its happy path
stopped after the first A tool prefix, so earlier superficial no-B fault outcomes
were rejected as evidence. Native persisted messages omit optional live undefined
properties. Complete public persisted-representation comparisons now follow the
existing worker witness convention, while routing-state comparisons remain exact.
A fresh happy-only check then passed A,A,B (~3s,
`/tmp/p4-native-sdk-charge.log`, session84763 terminal).

The next finite run exited1 (~7s, `/tmp/p4-native-sdk-finite.log`): happy, budget
and both real crash cases passed; one fault assertion counted its deliberately
injected malformed state as a verified charge. Component behavior held before B.
The fixture now distinguishes all persisted state entries from verified charges,
and each fault separately asserts its exact reached boundary. Final passing
evidence above supersedes those failed assertions without erasing the failures.
All earlier watcher cells/sessions were terminal; no command was repeated merely
to repair notification delivery.

## Holds, documentation, and history

The supported component boundary is documented in `docs/pi-providers.md`, linked
from the existing provider documentation structure. The lead's main prose pass
closed before commit. The source compiler/decider remains separately documented; host PlanNext is
unchanged and Accepted still forbids host redispatch.

Production still requires the authoritative original durable receipt, current
generation/effects, trusted original retry deadline, native retry transport and
schema3 routing writer/controller integration plus physical-route attribution/
retry-disable support. Owner1 confirms current activeInput lacks full original
SubmissionRef/deadline and public external-effect authority. No deadline is derived
from acknowledgement lifetime or B1 callback timeout. No production registration,
automatic fallback, Daybreak entitlement or live readiness is claimed.

This leaf adds no database migration, host mapping schema change or conversion.
Native schema1 branch charges exist only in owned fixtures; no live data was
written. One logical source commit contains this package;
whole-branch consolidation/review remains lead-owned. No merge/deploy/lifecycle or
session cleanup authorization is inferred.

## Final commit and ownership receipt

- Parent: `3872155b55688742355b8dc16b88584f4cb5a303`.
- Head: `aec5bea24c6a1bf18dd5c7941617286c869e4c7d`.
- Exact committed inventory: added `pi-runtime/src/native-retry.mjs` (248 lines),
  added `test/pi_runtime/native-retry.mjs` (182), modified `docs/pi-providers.md`
  (+45); three paths and 475 inserted lines, no peer content.
- Fresh bound current/env and own retained roster verified; branch, exact parent
  and empty index verified before adding exact paths. Committed parent helper
  bytes match the successful check inputs above. Source hashes stayed unchanged.
- Lead prose changed only public-SDK/error-pair wording: prior technical doc hash
  `d9f543ccee4e02c7c75655e38462be1b9f0333777e3c4893f284e31e0fe05870` became the
  final doc hash in the table. APIs/fields/error strings/holds stayed intact.
- Staged, committed and current hashes matched the final table for all three
  paths; staged whitespace check passed. Normal `git commit -F` used a temporary
  message file, with no hook bypass; no hook framework or active hook was declared.
- Commit command completed exit0; post-index empty and owned three paths clean.
  Window released immediately through report ID
  `9c5591a5-41a2-4a6d-948f-b1356bd32f1a`. No unchanged SDK rerun for prose/index.
- Final passing tests bind the exact now-committed code bytes, with prior failed
  attempts preserved above. No remaining package check failure; mandatory combined
  review and production integration remain lead-owned separate gates.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
