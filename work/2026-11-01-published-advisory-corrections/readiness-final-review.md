# Affected readiness-helper final review

No Blocking, Important or Advisory finding was established. The committed helper correction satisfies the bounded readiness contract and is suitable for the held legacy retry and refreshed strict KB check. Those runtime checks remain pending; this review does not claim they passed.

## Reviewer and scope

Reviewer0, retained independent review-purpose/read_only member, native thread 01a19801-1fc5-70e3-ba37-8c0952a89392; saved gpt-6.1-sol/xhigh on codex-lb, no override/fallback or authorship. Session current printed 2026-11-01-published-advisory-corrections from its tracking directory; both DEV_SESSION identity variables were absent and the trusted binding matched.

Applied mandatory-change-review with general/history, architecture/repetition, scope/proportionality and risk/compatibility lanes. Overall package risk remains High; the affected delta is test-readiness observation with bounded error/deadline/caller implications. Read readiness-review.md in full, owning guidance, actual helper/callers, installed HaveAPI source/formatter and supplied quick/equivalence receipts. Unchanged skill/procedure reads were reused as allowed.

No broad API/UI/client/modern rereview, nested agent, source/session-file write, test/build, fetch, remote mutation, production request, integration, deployment or lifecycle action was performed. This text is returned for the lead to persist as readiness-final-review.md. Earlier final-review.md, refresh-review.md and review-reconciliation.md retain their separate scopes and findings/dispositions.

## Exact reviewed ranges and histories

vpsadmin, target master:
097226b22edf8b59f80b5dfaa55265e9d0cac633..
0111e97768982701a30634c2277c1c364230067a.

Complete series:
1. 9415cf2855a3f9caef6ab68dc7df8405ed9f3ef8 — api: support guarded advisory corrections and lifecycle actions.
2. 0111e97768982701a30634c2277c1c364230067a — webui: manage advisory corrections, retraction and deletion.

Actual merge base and local submitted HEAD match this range; worktree/index were clean. The affected comparison is 4cf556e56b522722db18ebf1f1bb5859523e8b4c..0111e97768982701a30634c2277c1c364230067a. I independently verified that its sole changed path is tests/runner/extensions/vpsadmin_services.rb (+13/-2), and that B's complete binary patch is equal after replay. The full refreshed file inventory has the previously accepted endpoint inventory plus this helper; no unrelated source was introduced.

KB, target master:
ce2c8cd9358c3636e5d39343e595df813a0b197f..
fd9267bf43009a567e4b958aaec296bf0a60a8ee.

Complete series: one commit fd9267bf43009a567e4b958aaec296bf0a60a8ee, Pin KB contracts to expanded advisory management. Actual merge base/HEAD match and worktree/index were clean.

## Scope, implementation and compatibility

The real legacy attempt on 4cf failed before Playwright at wait_for_vpsadmin_api. I inspected its retained native trace and service shell log: curl completed successfully and returned the healthy HaveAPI page headed API versions, while the previous helper searched for API description. This supports repairing the observation instead of altering product behavior or extending timeouts. No browser coverage follows from that failed readiness attempt.

The correction stays in the existing machine helper and uses the same host, unauthenticated observation and caller interface. The method still returns true on readiness, uses the same default timeout, computes the same deadline and remaining.ceil curl budget, sleeps one second after an unready successful HTTP response, and propagates wait_until_succeeds/curl exceptions. No rescue now hides execution errors; only JSON::ParserError becomes an unready response.

The installed HaveAPI 0.32.1 server.rb root OPTIONS branch explicitly supports describe=versions without authentication and returns versions/default through OutputFormatter.format(true, ret). The inspected formatter produces the successful status/response envelope; the JSON formatter serializes it conventionally. The helper accepts that exact public contract: true status, Hash response, versions Array and a nonempty String default included in it. Non-JSON, wrong top-level/response shape, false/string status, absent/empty/wrong-type default and default/version disagreement do not falsely report readiness.

The request is identical to the existing services-up.nix API-response check. That test separately retains HTML-documentation assertions, so removing an HTML literal from the general readiness probe does not erase owning documentation coverage. Search of actual callers shows broad use of this shared services machine method, including webui and storage/network/VPS suites; none requires an HTML return value or changed parameters. The helper remains an observation that the API serves valid version metadata, not a new deep-health or authorization test.

This is the smallest conventional response to the observed failure. Local shape checks at this external response boundary are justified; no generic validator, retry framework or duplicated product policy was added. The repeated curl/version assertion in services-up is small test glue with its own assertions, not a drift-prone security/persistence rule needing extraction. No product runtime, public mutation contract, authorization, announcement/mail or persistent-state behavior changes.

## Source/input and pin proof

Independently compared Git blob/mode graphs:

- The entire API subtree is equal between 4cf and 0111.
- Relative to runtime-tested c8efabeb01ccca66b19425ee429e834d23cf3688, all tracked entries are equal except the accepted api/spec/api/covered_endpoints.yml additions and this readiness helper.
- The inventory adds only security_advisory#delete and security_advisory#retract.
- Submitted final tree is 6b7fb42661283d0fed026c2c138fa477a7f1f34c.
- Metadata binds final source store /nix/store/4kh885r4mb21dh0pnmjm8lysmw37v19a-source to 0111; its helper bytes equal the committed helper.
- The full committed flake.lock graph equals runtime-tested c8ef and the saved final metadata graph.
- Saved original/final API shell derivation JSON is byte-equal, SHA256 30d5a1bd662c539f4e091713b4d9ab2ab35b32095622d2c350cab8690de2bd2d.

The retained reuse receipt separately binds actual full/core environment observations and their effective Gemfile.lock identities. This preserves old test evidence for its actual inputs; source equality alone is not presented as new execution of final-source acceptance.

Independently parsed the complete KB before/after lock graph and all source pins. Only the vpsadmin lock node changes. All unrelated nodes, root follows and selected-node input edges remain equal; explicit vpsadminos remains 6bdf458fd9105379860234ff33d352e55844f08f. All five pin locations select 0111e97768982701a30634c2277c1c364230067a, narHash sha256-CkMxT20JI+V02lLCmazwaQyxRYEhubxS8fe7O+nNkM0=. Four source files are byte-equal after substituting the selected revision, preserving capture/page provenance/assets/content. The full KB range remains five pin files, +8/-8.

## Whole-branch and migration conclusions

The refreshed API series remains two logical behavior/UI commits with supporting verification corrections folded into their owner. No obsolete unmerged implementation, transitional compatibility approach or redundant fixup commit remains. There is no repeated dependency/input stream in the feature range. The earlier source heads remain evidence refs, not a claim that an old deployed commit was literally merged.

The KB has one logical vpsadmin pin stream consolidated into one final commit; no intermediate pin update remains. No retention boundary requires additional obsolete updates.

NO MIGRATIONS in either complete reviewed range. No schema/seed/migration version or persisted format is introduced by this successor. There are no intermediate migration versions to preserve for merge/release/deployment/external consumption. Client 0b771120 and modern 1c8478bc are unchanged and outside this affected review.

## Verification limits and next gate

Owner receipts report scoped syntax/RuboCop/diff checks, normal hooks and direct-method checks against the actual extension/native libraries. I inspected the temporary check source: it covers valid metadata, fourteen malformed/error/default/version cases, timeout class/message and curl-error propagation without introducing permanent harness infrastructure. I did not execute it or any suite.

The actual changed helper still needs the real legacy advisory retry, and the exact final KB pin needs its strict check. Previous failed readiness attempts provide zero Playwright acceptance evidence. Existing API/client/modern results remain bound to their recorded tested heads/derivations/environments; this review neither broadens those claims nor requires unchanged long suites merely to repeat them.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
