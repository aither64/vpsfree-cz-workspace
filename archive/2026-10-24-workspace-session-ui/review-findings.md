# Final review findings (preliminary, verbatim evidence)

Reviewer: retained reviewer0, gpt-6.1-sol/xhigh; all four lanes.
Reviewed range b3a6eb2fc0b41cf0cb965bf4c39991815d9df734..5293cf5b3d6752e804223833a1bb9d484e55b759.

From reviewer milestone/finding report:

> Concrete Blocking finding (risk/general) in 74a55c8b: retrying a legacy
> outside-buffer UNKNOWN attempt by submitting identical text/attachments,
> followed by uploads.clear() storage failure, calls messageDispatcher.hold(id)
> unconditionally. hold() rewrites it to failed despite attempt.retry=true,
> enabling Discard unsent and deleting its only original recovery record even
> though an earlier page may already have delivered it. Nix quick reproduction
> using shipped composer fixture: seed retained unknown send record; make
> uploads.clear throw; submit same draft => ordered entry
> {retry:true,state:'failed'}, zero new HTTP; discardFailedMessage => ordered
> entries 0, records.has(originalID)=false, pending original false. Preserve
> uncertainty for recovered IDs when capture/detachment fails; only provably
> fresh never-dispatched IDs may become failed/editable/discardable.

> Also confirmed Important orphan on edited failed-message ordered-write
> failure: new attempt remains outside buffer, reload yields 2 pending IDs/1
> ordered entry and original Retry makes zero calls.

Lead accepts both findings. Assigned implementer1 narrow source/quick regression
fixes; long tests held. Final full report pending. Narrow requested fixes will be
inspected and checked under mandatory-review step 9; new design/contract would
require affected-lane rerun. No automatic rubber-stamp rerun for direct fixes.
