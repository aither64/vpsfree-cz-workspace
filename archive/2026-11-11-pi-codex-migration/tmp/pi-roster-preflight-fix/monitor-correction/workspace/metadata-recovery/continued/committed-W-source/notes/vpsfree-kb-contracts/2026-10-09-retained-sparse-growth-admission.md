# Retained failed campaigns still consume future disk capacity

A fresh portable verifier campaign can fail admission even when retained images
appear almost empty. Measure allocated blocks separately from apparent lengths.
Unallocated image extents remain possible future growth when ownership completion
is unproved. Existing allocated bytes already reduce the measured free space;
add only the unallocated remainder to the protected reserve.

This initiative retained two earlier runs and both isolation roots. Their tanks
still had approximately64GiB of unallocated growth. A prior48GiB reserve covered
only the two earlier tanks plus16GiB host reserve, so it was obsolete. Fresh
accounting needed approximately80GiB protected reserve before the new campaign's
92GiB future output growth. With166.55GiB free, admission refused before builder
headroom. State/store/daemon scratch shared one filesystem and were counted once.

Package-only preparation can have a separately measured assessment for a small
wrapper plan. Its success does not admit guest construction. Keep builder scratch
unknown unless concrete evidence bounds it; download/NAR sizes do not do so.
Seek additional measured capacity or a separate owned disk-backed filesystem;
never infer cleanup savings from absent processes or incomplete receipts.

Evidence: work/2026-10-05-network-ipv4-left-counter/finish-direct-capacity-blocker5.json.
