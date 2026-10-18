# Review remediation

Independent reviewer /root/compatibility_review, native 01a148ce-1edc-7e51-b7b5-a66751627bd9, gpt-6-astra/xhigh, behavioral read-only; environment access profile is unrestricted. Original review ranges are in compat-review-heads.json; final report also explicitly covers the committed narrow remediation and regenerated pins in compat-final-heads.json.

Blocking: after durable submit-batch acceptance but before journal phase/receipt publication, jobs can complete before worker restart. Receipt replay changes only the journal; waiting on unchanged ledger revision strands completion forever. The same scheduling dependency exists when consuming a retained pending refresh after its original job has already finished.

Direct fix inside accepted contract: preserve runnable continuation after a phase transition or consumption of pendingRefresh. A subsequent pass observes the resulting jobs/phase before parking at a ledger revision. Unchanged external waits still sleep without redispatch. No additional approval, journal format, native protocol or operation identities. Two regression fixtures complete actual disposable merge workers before replaying original batch/refresh receipts, assert no ledger change, runnable dispatch/continuation, same job identity and one final notice.

Focused verification: four tests / 34 assertions pass (6.71s) covering both replay windows, normal completion, and parking without ledger change. Ruby syntax and diff checks pass. Fold changes into the single unmerged feature commit and regenerate the two final pin streams; preserve original review ranges and report. This directly implements the reviewer's requested narrow crash-recovery fix, so mandatory-change-review step 9 applies without confirmation-only reviewer rerun.

Final published narrow-fix runtime: 543136a0e3be561e010d8b2ccd309f2ad37311a0. Workspace a90022d897bf539f3d5dca39a02d0f0140c6b457; configuration f60ebcddd9df7b224f5cff48b95c7706d25b6e7a. Original review ranges remain in compat-review-heads.json. Final series/diffs in compat-final-* files. Superseded CI 39014378649 cancellation attempted, refused HTTP 403 token scope; current run 39014845298 untouched.
