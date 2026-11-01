# Lead design and verification brief

The existing codex-work row is the sole live status surface. Resolve its label
from focused activity and the existing otherTeamWork result. An idle focused
member with other work shows only the peer summary; automatic and explicit waits
keep their own explanation first, then append peer work with “ · ”. A failed or
stale peer observation uses the existing unavailable message in the same slot.
Active work and idle without peers retain their ordinary labels. Use this same
resolved label for tab title/aria text; preserve the existing attention predicate.

Keep codex-work-label full in DOM text, title and accessible label. Use nowrap,
min-width zero and ellipsis for shrinking text. Counts may shrink with ellipsis
and full title; keep time unwrapped and unshrunk. Remove the extra paragraph,
lookup, update and CSS. Visibility must still cover a peer summary when current
idle timing has no stateSinceMs, as the paragraph previously did. Avoid adding
another polling/read path. Existing team-data filtering and stale thresholds
remain authoritative.

The runtime owns display logic and guide text. Composed workspace/configuration
consume one published exact head; no API/schema migration or provider change.
Update asset query versions so returning browsers load the new layout. Deploy
the matching composition/host contract under current package transition rules,
using forward recovery and keeping native/tmux running when identity matches.

Acceptance: one row at 1280/420px for one or many peers and all focused wait
states; full hover/accessible values despite clipping; timer stays visible;
explicit request remains first; stale teams cannot assert current work; selector,
membership removal, completion and hidden-tab polling retain their contracts.
Quick syntax/pure-browser/focused Go checks precede committed independent review;
actual Chromium/Firefox, Nix builds and CI follow review before live acceptance.
