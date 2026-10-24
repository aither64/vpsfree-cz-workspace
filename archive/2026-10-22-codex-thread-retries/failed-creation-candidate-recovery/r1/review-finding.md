# Early Important R1: historical same-slug removal selected as current

Reviewer0 to lead, frozen B8e9186132efc0636d6bcaaccf663dad43a799bf4. General/risk. Remaining review lanes/history continue on unchanged source; no reviewer execution.

`libexec/dev-session:6297–6326` `failed_creation_delete_removal` selects every completed same-slug removal without binding it to the failed request/root/receipt. With no live removal journal, a legitimately reused slug has older completed recovery and current tracking. Selecting old recovery makes `failed_creation_delete_context:6186–6189` reject “tracking has a conflicting location” before ordinary deletion. Two older removals produce permanent ambiguity instead.

Slug reuse and prior removal epochs are supported by the existing receipt/preparation model; the new schema3 Go consumer fixture deliberately records prior same-slug history. An exact authorized failed direct request on a reused slug cannot use the recovery route, so its package-switch blocker remains.

Requested narrow correction: distinguish current in-progress/completed operation using exact current request/private provenance; never treat any historical same-slug completion as current. Add public-entry reused-slug/prior-history coverage and preserve prior recovery bytes, current-operation replay and no-absence-inference guarantees.

Lead disposition: fix Important R1. Owner0 diagnosis/remedy in isolated exact8e tree, uncommitted only; owner1 sole Git and isolated worktree preparation. Main remains frozen for reviewer to complete. Architect clarifies existing-field binding, no schema/phase/contract expansion. Focused direct step9 verification planned unless implementation expands the assessed boundary. No long verification, pins, live deletion or deployment released.
