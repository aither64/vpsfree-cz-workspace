# Independent final review: upgrade cleanup and policy

Reviewer0, retained gpt-6.1-sol/xhigh/read_only; all four mandatory review lanes.
This records the returned review of the completed cleanup deliverable only,
not whole-branch readiness. Reviewer performed no writes, tests, Nix, probes,
scans, restoration, Git mutations or other operations. Lead saved this report.

## Important: removal-commit provenance

Reviewed commit `8fb5782ff630deee79d0cdbb7eee55abc459464f` omits required
retirement and validation provenance. See `docs/os/testing.md:300-306` and
`docs/os/patch-series-policy.md:90-98`, especially 97.

The message describes deleted cases and the retained impermanence case's future
removal condition, but records neither the decision/evidence confirming
retirement of the September matrix nor validation performed. Passing width
hooks does not supply either item. Session design/receipt already provide the
truthful rationale and checks: record the accepted decision superseding those
rollout scenarios, retained equivalent-old-state boundary, static
deletion/catalog/script-equality and Nixfmt/hooks results, and unrun native
discovery/VM limits. Configured-source evidence is distinct from live inventory
and from proof that inherited state disappeared.

No Blocking or additional source/policy correctness finding was established.
Message-only correction can be verified by lead with exact tree equality and
normal hooks; no fresh full review or extra tests/framework/restoration needed.

## Source and scope conclusions

Reviewer verified current `2026-10-22-ci-failure-analysis` against trusted
binding; both DEV_SESSION variables were absent. Worktree:
`worktrees/2026-10-22-ci-failure-analysis/vpsadminos`.
Base `f74629fa4046089e2c53d0cb0e3ba7ef5b178e82`; reviewed head above;
tree `70e412f6846a426673de778ea77d4d3b02a06da2`. Parent/head/tree match;
checkout/index clean.

Reviewer read skill/all four references, packet, plan/state/design, repository
AGENTS/patch-series policy, changed source/docs, parent consumers and final
amend evidence. Independent read-only Git/object comparisons establish:

- Exactly 33 exclusive retired files plus retained-fixture rename; sole
  remaining upgrade file `impermanence-from-2abbe3cc1c10.nix`.
- Retained template body byte-identical after native-name normalization;
  complete testScript attribute unchanged, 16,955 bytes, SHA256
  `b949f3fc408e31daa78fcf15d46016fe424ccceafb33096c9e821579be9e78e4`.
- Full immutable baseline, stable target/profile, framework/inputs, cgroup
  instances, tags, attempts, assertions, payload and cleanup behavior preserved.
- Catalog exactly template rename plus both optional-block removals; other
  ordinary/current-kernel/cgroup/livepatch selections unchanged.
- Exclusive helper consumers removed; no surviving old case/template/gate/helper
  references found. Shared framework resolves cases using caller suitePath;
  API, exports and runner unchanged.
- Focused explanation retained under new name; full unrelated livepatch docs
  suffix exact.
- Policy/header/AGENTS implement selected names, full baseline, purpose, target
  and evidence-based removal rules. Retained case says retirement evidence is
  not established and protects old saved/running state and rollback/restoration.
- Reviewed final amend.log: Nixfmt and all message hooks pass, producer/reader 0,
  no width warnings; maximum message width 70. Provenance omission remains.

Cleanup, catalog/doc retirement and policy applied to retained case form one
coherent scoped owner. No new abstraction/checker/registry/alias or broad
consumer change. Removed/renamed test identities are intentional and documented.
No production-state, deployment-order or rollback implementation change, and no
coordinated node update.

## History, migrations and repeated streams

Scoped one-commit history has no internal fixup/WIP or superseded implementation
stage. Message-only predecessor is not an extra shipping ancestor. Provenance
finding above remains.

Full earlier branch still has nine commits. `50a796f28` (DHCP diagnostic),
`247c091e6` (first-switch diagnostic), `a1c4dc932` (historical opt-in) are
superseded and need consolidation before later whole-branch readiness.
Production-origin behavior from `a2e4c0971` remains under new identity. Review
does not select consolidation or reopen earlier recorder/runtime work, and
does not declare the whole branch ready.

No migrations: no database schema, persisted format, runtime state or migration
lineage change. Existing writer/import/GC behavior and units remain; no
intermediate migration or external state boundary removed.

No repeated dependency/channel/input/kernel-pin/generated-artifact update
stream. Package changes no pin/lock/generated metadata; earlier distinct
immutable fixture roles are not repin iterations. No redundant stream retained.

## Verification limits and disposition

Native discovery/VMs unrun. Discovery is an accepted disclosed gap for this
proportional deletion/byte-exact script rename, not PASS or another finding.
No new tests/framework/native proof required for source review. Earlier runtime
and whole-branch limits remain.

Scoped review complete with one Important commit-provenance finding open at
reviewed head. Publication held by prior CI restriction. No branch/runtime
readiness, merge, deploy, historical boot, restore, cleanup or lifecycle authority.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/

## Lead disposition after review

Resolved by message-only amendment to
`07e31b96befb3afe2e8898065fe85a9d0b842611`. Lead inspected the full message:
retirement decision/configuration evidence, retained support boundary, actual
validation and unrun discovery/VM limits are now explicit. Tree remains exactly
`70e412f6846a426673de778ea77d4d3b02a06da2`; direct old/new diff exits 0,
worktree/index clean, parent/earlier eight commits and authorship unchanged.
Final provenance-amend-2.log records all normal hooks passing without warnings,
producer/reader 0. No source change or new design; skill step 9 permits direct
verification without another reviewer turn. Scoped finding closed; prior
whole-branch readiness and publication restrictions remain.
