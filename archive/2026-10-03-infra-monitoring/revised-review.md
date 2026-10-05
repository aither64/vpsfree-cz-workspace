# Final revised independent review

Disposition: **no Blocking, Important or Advisory findings**. Mandatory final
whole-branch review is complete; the central configuration build gate is open.
Earlier R1 is closed by independently inspected non-vacuous 20%/19% root-mount
warning assertions. The revised global boundary was independently reviewed,
not inherited from the historical SMS-only review.

## Identity and exact evidence

Reviewer0, retained purpose review, read_only, gpt-6.1-sol/xhigh,
thread 01a1021a-42ed-7e62-9bc2-43fbd84c6a48. Saved live roster settings verified;
no model/effort override, fallback or nested agents. Before file access, current
matched 2026-10-03-infra-monitoring from tracking; both environment markers were
absent, accepted under exact trusted workspace/session binding.

Base/merge base b66c929bb7c202ad31bd8994a691ade14c40ebf0. Complete series:

1. f53354dec1596bf665c80f85c557a9b05755805a — restrict critical filesystem alerts by type.
2. 657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da — apply staging CPU policy to playground.

Final tree c3a20ba419ff6bc8e2b3ed2a6d4600087d143af9. Reviewer independently
compared actual full diff with revised-final.diff: byte-identical, SHA256
4955b9e0cd56b89c64d5cca6a108b9a602cea5656c1a1e00dfd2e063bfe8fc42.
Checkout/index including untracked clean and HEAD/tree unchanged at reporting.

Read workspace/repository AGENTS and applicable procedures, mandatory review
skill and all four lane references in full, packet/plan/state/design/report,
job inventory/provenance, implementation/full inventory/diff, real production
consumers, fixtures, pass/failure/static/hook/consolidation/range evidence.
Risk classification High because monitoring behavior, label identities,
mixed versions, HA deduplication and rollback have operational effects.
No edits, hooks/tests/builds, commits/ref changes, push/integration/deployment,
lifecycle or cleanup were performed by reviewer. This lead record preserves
the complete substantive conclusions of the team report.

## General lane

No findings. common.nix:228 adds only the exact vm|physical numerator matcher;
removing it reproduces base byte-for-byte. Eligibility is type-based on any job,
including absent/unrecognized jobs; VPS/missing/empty/unknown/vmx excluded.
Denominator/vector matching, device/fstype/type identity, percentage VALUE,
selected mounts, <=10%, five-minute hold and labels are preserved. Warning
<20%/five minutes and separate node rootfs fatal <=5%/five minutes unchanged.
Entire alerter equals base; independently supplied critical/fatal alerts still
route normally to email/Telegram/both SMS receivers.

nodes.nix:75–147 has exactly the four accepted CPU edits. stg/pgnd use 50m for
warning >80% and vpsAdminOS critical >90%; other/missing locations remain 10m.
Boot age >3600, averaging, actual location and other policies remain. Source,
CPU fixtures and check-registration patch equal the prior accepted CPU patch.

Fixtures cover positive/negative type and job cases, absent/unrecognized job
positives, mount/threshold/hold boundaries, default denominator matching,
multiple identities, full labels/annotations and original values. Warnings
include VPS/missing types and selected 20/19% cases. CPU coverage includes
locations/OS/cores/boot/timing and unexpected outputs. Project monitoring docs
accurately explain behavior/identity/HA/rollback, are linked by mkdocs, and
keep durable guidance in the owner and individual rollout in session records.
Both commits explain final behavior and are independently reviewable.

## Architecture and repetition lane

No findings. modules/cluster/default.nix owns the finite validated machineType
contract; containers default VPS, others physical, with three explicit VMs.
Pinned confctl propagates metadata without provider/pin change. Four existing
constructors append authoritative type after custom labels, preserving other
precedence and shared node/ZFS/IPMI identities including type=node.

The existing JVB constructor adds one vps literal to the user-confirmed
homogeneous fleet. Real Meet data stays unchanged; all eleven paired 9100/9700
groups and alias/type/project are checked for both monitors. No parallel
registry/schema/runtime inference/framework; docs require reconsidering the
classification when inventory changes. Common rule owns global policy once;
tiny label assignments fit distinct existing constructors. Fixtures use actual
modules/rules/Meet data rather than a second policy implementation.

## Scope and proportionality lane

No findings. Production matches the superseding global policy and confirmed
bridge labels plus accepted separate CPU policy. Alerter (alerter/default.nix),
infra/Meet rules, Meet data and locks equal base. No generalized compatibility
mechanism, fallback, suppression route, dependency churn or unused path remains.
Tests delegate evaluator/route semantics to promtool/amtool. Their size is
justified by target constructors, excluded classification and timing/identity
risks; no alternative evaluator was built.

## Risk and compatibility lane

No findings. Validated configuration/authoritative labels control type, with no
untrusted inference, credentials/privilege/authentication/destructive boundary,
protocol/API/client/CLI/Terraform or persisted format change. New labels change
series/unaggregated-alert identities and can reset pending/rate windows. Old
monitors can still emit VPS criticals; differing label sets cannot be assumed
HA-deduplicated. Both monitors need labels/rule together, and active alerts may
resolve normally. Docs record these consequences accurately.

No coordinated exporter/node/VM/JVB update. Alertmanager is unchanged and needs
no alerter-first policy step. State remains rollback-readable; monitor rollback
restores previous eligibility/labels/CPU without deleting TSDB. Alertmanager
alone cannot recreate an absent Prometheus alert. Missing/unknown type exclusion
is an explicitly accepted boundary.

## Complete history and migration conclusions

Exactly base -> f53354de -> 657cc0a8. First introduces final global policy
directly with metadata/labels/checks/docs; second only independent CPU policy.
Superseded SMS approach and fixups were folded into the owning unmerged commit.
No obsolete/transitional approaches, redundant dependencies, interim job/unless
logic, unused compatibility paths or tidy/fixup commits remain. Old published
f725 is outside new ancestry pending lead publication. Known repository/session
provenance: old history unmerged, no session release/deploy/pin/integration;
unknown external consumption not audited. Separate stale local master preserved.

**No migrations**. No migration versions, schema/seed changes or persistent
format transitions exist. No transitional lineage/predecessor reconciliation
is needed. Alert identity transitions are operational, not schema migration.

## Verification and residual limits

All four checks passed on exactly the final tree (recorded pre-consolidation
HEAD does not change tested bytes): focused config+CPU 6.760s, adjacent
autostart/process-count 2.929s. Initial revision failure was two broad warning
assertion queries including missing-job VM; only those selectors were narrowed
and the real rerun passed. Static and both final active-hook evidence passed;
reviewer did not execute checks.

Full both-monitor/both-alerter builds still required; historical SMS builds
cannot verify this revision and focused fixtures do not evaluate every fleet
configuration path. Offline routing covers selection, not transport delivery,
activation/repeat timers or executed inhibition. No live scrape/reload/fleet
state or unknown-consumer audit; bridge classification relies on explicit user
confirmation and current inventory. Future filesystem target constructors must
supply intended type or this critical rule intentionally excludes them; warning/
fatal behavior remains the accepted boundary. Review does not establish live
operational readiness. Lead owns builds/publication/approved default merge;
user owns deployment. Session stays open.
