# Capacity review C1 closure

C1 is closed by lead direct inspection under mandatory-change-review step 9.
The immutable reviewer report [review-capacity.md](review-capacity.md) remains
unchanged and applies to c218..18432f0c. This record binds its requested narrow
correction to final d1872f5defe01f02e05ac6ce083541789f1222f6,
tree9b2bfb74eb395f6596e010ef5f1378bba1da9f5d.

The exact delta is two Ruby paths,79+/8-: the retry guard now shares the existing
policy lstat/Dir.children JSON-presence traversal. Missing roots and empty or
lock/tmp-only trees remain absence; root/nested ordinary inventory failures and
non-directory roots refuse. No payload parsing, state/schema/API change, new
collector or unrelated inventory change. Existing policy behavior and diagnostic
remain unchanged. The new inspection diagnostic received the lead prose pass.

Lead read the complete committed two-file delta and focused test evidence.
Disposable uid1000 chmod tests establish original glob false absence with retained
schema2. Corrected focused tests fail before the change and pass afterward:
15tests/309assertions,0failures/errors/skips,0.671304s; Ruby syntax passes.
Tests cover preparation, candidate activation/self-activation, preserved bytes
and refusal before profile/quiesce/config effects. Lead independently recomputed
the green and two causal-red log hashes, all matching the receipt.

Lead independently verified final tree equals tested committed fixup6adec2f8,
original three commits are '=' in range-diff, and only the owning fourth commit
changed. Old18432 and fixup refs remain retained; no obsolete fixup remains.
All Go/other source inputs are unchanged, so no unrelated large check was repeated.
Lead recomputed final source NAR at
/nix/store/0n40ixj1a26p7pzgajkk2fpkdx6mq9wd-source:
sha256-nF+KHafhk8wwmkzXVoBo5jB1aqUirf2cI3MVgirG8QM=.
Active ordinary source root,676file/mode proof and unchanged full lock graph are
bound by [capacity-managed-turn-inventory-fix-receipt.json](capacity-managed-turn-inventory-fix-receipt.json).

No requested design/compatibility boundary expanded; no automatic reviewer rerun
is required for this correction. The capacity/affected-fixture source-review gate
is clear, while native reader, package/CI, service-cleanup VM and deployment proof
remain outstanding. The newly authorized machine-claims feature is separate and
needs completed commits, quick checks and its own affected final review. No long
test, publication, integration, deployment or lifecycle approval follows this
closure. Session remains open.
