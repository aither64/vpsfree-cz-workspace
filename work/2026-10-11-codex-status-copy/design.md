# Lead implementation and verification brief

This bounded presentation edit leaves existing activity/team-selection semantics
and backend contracts unchanged. The lead owns design and application edits.

Return compact label and full description from shared presentation. Labels:
Working, Idle, Sleeping (auto), Waiting for team (auto), Approval needed,
Answer needed, In progress, Waiting (reason unknown), Team status unavailable.
For one peer use '<address> is working', '<address> is sleeping (auto)',
'<address> is waiting for team (auto)', or '<address>: in progress'. For several
peers join compact address/state entries with semicolons, top three and +N.
Focused wait/blocking request remains first. Keep full descriptions on row
hover/ARIA and tab hover/ARIA; retain attention, freshness and completed-plan
visibility rules. Do not shorten the separate Team table's activity detail.

Add an aria-hidden middle dot between counts and elapsed time only when both
are nonempty. Preserve a single flex row, label ellipsis and right-side counts.
Tabular numerals remove proportional-digit jitter. A stable right-aligned timer
slot prevents unit transitions from shifting counts. Size for ordinary long
durations and verify timer readability at 420px; retain full error text through
hover/accessibility when space is constrained. Bump JS/CSS asset versions.

Acceptance: short visible/full accessible descriptions; optional separator;
unchanged peer sorting, overflow, freshness and focused-wait precedence; stable
counter positions across ticking digits and seconds/minutes/hours transitions;
no horizontal page overflow at 1280/420px. Quick pure contracts/template checks
precede committed independent review. Chromium/Firefox, packaged composition,
host builds and CI follow review. Verify served assets and native process
continuity after deployment. No migrations or persistent-state changes. Retain
session/branches and wait for new merge approval.
