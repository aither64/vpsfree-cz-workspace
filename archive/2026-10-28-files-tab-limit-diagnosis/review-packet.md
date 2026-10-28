# Final review packet: lazy Files browsing

All intended runtime and dependent pin changes are committed, published and
quick-checked. No long verification, integration or activation has been launched.
Review under `~/.codex/skills/mandatory-change-review/SKILL.md` and all four lane
references: general, architecture, scope, risk/compatibility. Overall risk is
high because this adds a remotely requested confined filesystem API, paired
browser compatibility and live application/host deployment selection.

Reviewer: retained `reviewer0`, read-only, `gpt-6.1-sol` / `xhigh`; unchanged
saved settings. Lead verified ready review-purpose status before assignment.

## Request and boundaries

User requested diagnosis of an empty Files tab, then inventory of large session
trees, chose collapsed lazy directories and alphabetical pages, and finally
said "Implement the plan". Implement bounded immediate-directory browsing;
do not clean inventoried sessions or raise recursive limits. No integration or
activation approval exists. Preserve current deployed features and native Codex.

See `plan.md`, architect-owned `design.md`, `state.md`, `implementer0-result.md`,
`rollout-preparation.md` and `browser-smoke-preparation.md` in this directory.
The initial tracking commit is e54e6c3386af2310a5c3b7021031710042ae69bc.

## Exact ranges and complete history

All worktrees are under
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-files-tab-limit-diagnosis/`;
all feature branches are `2026-10-28-files-tab-limit-diagnosis`.

| Repository | Review base | Final head | Task diff |
| --- | --- | --- | --- |
| dev-workspace | f199947c4c0d2c5d96f4f663053ff5a592946ef4 deployed dependency; remote target4a002f52c3b55099540aa99708d5fcf29f7b2456 | 617235fce02ac7095d258c73575bb8a64696b6d1 | 14files,+1140/-92 |
| workspace | current shared master668291226733ffdb18fe94588078994af02a8594; initial/remote6e131813ed455b2335a9287be760877d3242fd9d | 388d27e3be1e57178558f0171850c02926135c99 | 2files,+5/-5 |
| vpsfree-cz-configuration | 2d6837f0b9582bbd812ecccf6cd59b5685029e0a | f6f8a2f746302328e45217c15529b8c82e3a40f2 | 1file,+3/-3 |

Runtime full remote4a002f52-to-head series is seven linear commits:

1. cc106266345ebe5e3332561c7143947bc1415b69 — communication grants/delivery.
2. e9153e614e44766d0f0efd6721b34b7bf2f4c14a — communication transcript display.
3. d0a9c5f6dc38220bed45d0d7ef631768ad538203 — explicit retry proof retention.
4. fd9128a1c2dd81202c9b09b76e640e816f020524 — pending-send drop behavior.
5. f9d8e4fe7d0dddab7d323e14f1019b12552a15fa — session settings tabs.
6. f199947c4c0d2c5d96f4f663053ff5a592946ef4 — durable messages in transcript.
7. 617235fce02ac7095d258c73575bb8a64696b6d1 — task-owned lazy Files browsing.

The first six are unchanged published/deployed dependencies, not authored in
this task. Full target-to-head net:53files,+3746/-154. Review the full range and
its persistence/interaction implications; no independent predecessor review or
integration approval is asserted. The inherited range changes reporting policy
1→2 and communication persistence policy1, although it has no DB migrations or
input updates. Do not call the whole branch persistence-neutral. Preserve this
deployed history intact rather than rewriting it as task cleanup.

Workspace's task range is one pin commit atop existing shared master. Its full
remote6e131813-to-head range has ten inherited shared-master commits plus that
pin; complete series is listed in `rollout-preparation.md`. The inherited range
is coordination/session evidence and notes, already on shared master; it is not
new application source authored here. Inventory that distinction without reading
another session's private records/worktrees/transcripts or claiming predecessor
review. The actual shared-master integration delta is only the runtime pin.
Use canonical Git objects/current own worktrees; never enter peer worktrees.

Configuration has one generated confctl channel update. Each task-owned pin
stream is exactly one final update. There are no task fixups/superseded approaches
or transitional migrations. Require your independent explicit whole-series,
pin-consolidation and migration conclusions, including no migrations where true.

## Interfaces, verification and consumers

New `/api/sessions/<slug>/directory?path=` returns direct file/directory entries
and a compact scoped generation-bound continuation. Limits are200 entries,
256KiB encoded response,4KiB cursor,4-second/4-slot server reads and2 concurrent
browser reads. Dirs first, bytewise names; each page scans one immediate
directory with a<=201-entry heap. No descendants, persistent cache or total count.
409 detects changed directories. Collapse/refresh/page/hide cancellation cannot
clear selected file merely because its path is absent from a loaded subset.

Confinement, ignored-file visibility, work/archive selection, legacy recursive
endpoint, direct file links and preview/download guards remain supported.
Old browser uses old endpoint; new browser never recursively falls back. Assets
advance together. No Files persistence, schema, protocol or native upgrade.
Runtime is generic owner; composed workspace browser and host consume its exact
source via existing nested input/channel paths. Pin diffs preserve extension,
Codex, codex-web, all unrelated nodes/edges/follows and native wrapper inputs.

Runtime docs: `docs/workspace-portal.md` Files and Session directory API. Lead
applied the writing skill to visible copy before commit. Existing configuration
operations docs describe host-first/user-profile deployment and forward recovery;
routine pin changes need no extra reusable documentation. Dated rollout evidence
stays here. No source cleanup, new framework or shared cursor cache is intended.

Quick checks passed in Nix shell: focused session tests1.630s, repository0.029s,
web/API/browser/assets16.925s, Node syntax and diff whitespace. Exact commands
and fixture isolation are in `implementer0-result.md`. New directory fixtures
cover5001 children, byte boundaries, races, invalid paths/cursors, descriptors,
slots/deadlines and cancellation. Configuration hooks passed Nixfmt and message
checks; generated message preserved despite TextWidth warning. Workspace/runtime
declare no hook framework. Both downstream locks pass
`bin/check-dev-workspace-deployment` at617235fc and share exact narHash
`sha256-ZYW7q9Q1TetTecOhzNop8U5UExuVUmFQQhb3KvPWdr8=`.

Long verification after review: full Go suite, runtime package, composed default
package, deployment-contract package, aitherdev confctl build, disposable native
Chromium smoke and exact-head automatic CI run40723188384. Watchers launch/observe
these; no full-suite or live-browser success is claimed yet. Review may identify
necessary changes; implementers retain fix ownership. Do not start long checks
or perform nested review/delegation yourself.

## Operational limits and report

Existing selected package/runtime/native/source/system paths and complete input
graphs are in `rollout-preparation.md`. Package recovery is forward-only. Actual
deployment requires fresh machine ownership and user authorization; integration
requires explicit named repository/target approval, including inherited runtime
lineage if it remains outside remote master. No lifecycle action authorized.

Write your independent report to this session's `review.md` and report to lead.
Start with findings/severity and exact references; state remaining gaps. No
application edits. Do not accept this packet's conclusions without inspection.
