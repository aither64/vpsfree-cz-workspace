# Review remediation

Important finding: timestamp enrichment forced all retained rows dirty and
replaced every message DOM node, risking selection/focus and paging anchors.

Remediation: retain message nodes when their content differs only in timestamp
metadata, and update the timestamp element in place. Grace callbacks patch time
and date presentation without marking message content dirty. Exact-time updates
no longer mark every retained row changed. The legacy grace callback also uses
node-preserving patching. Added Chromium/Firefox assertions for retained message
and text node identity plus selected text across fallback and exact-time updates.

Focused syntax and shipped contract/index tests passed (1.022s). Changes are
folded into the owning timestamp and browser commits. Final source head is
421142e3d356a48ac31d9f1686f8b8fc8179c7bf; no public contract or accepted boundary
was expanded. This is a direct narrow review fix under mandatory-review step 9.
