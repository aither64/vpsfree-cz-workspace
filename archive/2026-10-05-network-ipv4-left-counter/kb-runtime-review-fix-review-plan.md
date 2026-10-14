# Remediation review plan

Preparation for an affected-lane rerun. The original final review covered K93a16d6,
D51aba080 and Ed2079f6. Both findings now have checked committed corrections at
K68aa33b, with exact feature publication and canonical check passing. E pin
refresh is in progress; no new independent certification is claimed here.

The SSH endpoint correction reduces supported update scope: resolve per-machine
host/port before candidate preparation, journaling, build/import or shutdown;
refuse changes while preserving the old ready run and retained trust. Root's
focused inspection and actual trust-boundary/preflight checks apply under
mandatory-change-review step 9.

The artifact correction adds a physical descriptor-lifetime boundary beyond
async cancellation: the writer retains the same flocked open file description
through publication and cleanup, shares it only with the fixed helper, and
closes last without LOCK_UN. Root accepted architect design.md:1998. This new
ownership plumbing requires committed affected-lane review under step 10.

Select the same independent reviewer0, saved gpt-6.1-sol/xhigh/read_only. Overall
risk remains high because interruption can corrupt capture results. General
covers publication, checks and history; architecture covers the narrow descriptor
handoff and consumers; scope covers keeping it inside K without a general lock
framework; risk/compatibility covers safe opens, last-close release, cancellation,
child FD confinement and validator/capture serialization. D's transport and
reconciliation behavior are unchanged and retain their completed review. E's
mechanical K pin refresh must preserve D51 and every unrelated graph; inspect
that composition without reopening unrelated provider behavior.

The final packet must provide actual clean K/E heads, complete base-to-head
series, full binary diffs, source/mode hashes, checked-source-to-final equality,
normal-hook evidence, review-finding dispositions and native quick receipts.
Fold the K correction into its owning unmerged runtime commit; retain the
inherited a50 pin. Consolidate E's repeated input stream while retaining its
independently reviewed provider patch. State explicitly that there are no DB
migrations and no new state/protocol schema, alongside actual default/tag/feature
consumption evidence. Do not infer absence of external consumption.

Required decisive local evidence includes helper death while writer event
processing cannot observe loss, competitor exclusion until final close, normal
helper exit and writer death, no unrelated child FD leak, validator-wrapper
loss, pending lease cancellation, known-loss publication refusal, bilingual
merge, and early endpoint refusal plus real retained-key trust checks. Synthetic
browser/SSH cases do not certify live guests or screenshots.

Only after actual accepted-head review may a superseding bounded K/E package
packet run. Exact D51 CI fast package success is retained; plain D flake check
would add an unrelated host VM. Real standalone tests still require fresh disk,
RAM/shm and nested KVM proof. No activation, default integration, cleanup or
production KB action follows from this plan.
