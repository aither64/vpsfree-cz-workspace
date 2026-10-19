# Native fixture and browser verification review

Related independent review turn after frozen source edits, quick checks and
commits. Retain reviewer0 (gpt-6.1-sol/xhigh/read_only), independent eligible
saved review-purpose member; no overrides/fallback. Review the affected general,
architecture/repetition, scope/proportionality and risk/compatibility lanes.
Overall risk remains high: the fixture proves model-action isolation, actual
native protocol dispatch/cancellation/persistence and release/deployment gates.
Read the mandatory skill and all four references, workspace AGENTS and routed
procedures, and affected repository AGENTS. Perform review directly, no nested
agents, application/ref writes, Nix workaround, long tests, live calls, deployment
or lifecycle mutations. Read-only focused checks are permitted.

Outcome: optional custom session name under Options, otherwise model-generated
prompt name with bounded deterministic failure fallback. User explicitly chose
model naming, action file/network tools disabled, questions immediately rejected
and pure clock allowed. No binary/model metadata/custom-provider substitution,
Codex patch, literal zero-tool claim or forced serving transport change.
Trusted local host operator; untrusted remote clients; normal model inference
network transport is outside the forbidden model-action network boundary.

Read plan.md, state.md, design.md (especially Native fixture transport decision),
recovery-review.md and review.md. Carry forward unaffected production review
conclusions; this is a changed verification transport boundary, not a request
for a rubber stamp. Inspect exact fixture-provider.diff and fixture-runtime.diff
and the complete branch-inventory.md plus all exact final/incoming diffs.

Current clean bases/heads:
- codex-web 4c170393a96ed0a6ac2e43488d073f6fcab36132 ->
  8db6adfd9511e95db2b8941edee69bfcba6d13ae.
- dev-workspace 924c0ec28c41dd8b56aaf17f2212b302ca614899 ->
  d05e75270a9bed417d07e9be8bc082c906f6846a.
- extension 8f8d8ecf5031c40d3e4a4ee2e9425721fc035800 ->
  2e3733ade1bac712f0b852d1960a681e5bca5076.
- workspace origin/master1fa9c982b866a305bd1451f2c32f6d387d2dc1a3 ->
  f5d30e291929bdf771f0d3842b84db1f08640131; own shared-master basead539340.
All under worktrees/2026-10-03-automatic-session-slugs/{project}.
Require explicit complete-history and no-migrations conclusions. Provider
fixture follow-ups are folded into its owning utility commit8db; browser fixes
folded into frontendea317560; separate runtime d05e7527 fixes the inherited
7-line event-recording test race (production team-runtime bytes unchanged).
Runtime deployed4ef298b and extension ancestors through399c3302 retained exact.
Existing deployed maintenance/storage policy lineage remains supported.
No incoming database/state-root/namespace migration or transitional schema.

Production provider17Go files + restriction policy equal packagedca exactly;
runtime changes since42 are only two tests. Runtime imports provider via Go and
flake, extension runtime lib.mkPackage, workspace extension lib.mkPackage with
site/team/cluster settings. Consumer pins currently retain packagedca/42/2e/f5;
following native proof the existing owning dependency units will receive exact
new hashes, same public sources/vendor tree, no new interface. Inspect actual pins
and disclose this remaining mechanical refresh; do not claim unbuilt new heads.

Native fixture corrections: nft block separators; typed empty control environment
(the old null failed TOML decoding); synthetic private auth.json because pinned
server ignores environment auth; 0.2s sentinel MCP startup budgets versus default
30s in a5s control; bounded8KiB stderr and64HTTP diagnostics; permitted provider
plainGET positive probe404; valid GET /v1/responses WebSocket upgrades only426,
case-insensitive Connection/Upgrade plus version13/strict16-byte base64 key;
plain/malformed/unrelated requests refused. Real decoded POSTs establish inference
and full model/tool/instruction evidence. Counters alone/426 alone do not pass.
Retired features.responses_websockets[_v2] removed only from synthetic fixture.
HTTP/SSE coverage limits are explicit: successful WS frames/continuation caches/
reconnects/hostile WS delivery are untested. Later positive live model canary uses
unchanged serving transport and must yield model naming, not deterministic fallback.
Public helper/deadlines/actions/egress/persistence controls are unchanged.

Creation browser: network-before reset can cause Chromium TCP replay. Count the
single actual native fetch call at the application boundary; every observed wire
POST must retain frozen exact body/ID. Preserve reset/reload/ambiguous acceptance
and separate-tab recovery assertions. Capture actual current catalog at legacy
acknowledgement after earlier scenarios advance it; preserve mismatch/explicit
ack/settings/security/storage assertions. Existing corrected full runtime race
924passactions/1skip/0fail and actual team Chromium26.89s passed. Creation remains
pending until its final full actual run; native has never passed.

Quick parent checks: owning Nix profile,TMPDIR=/tmp,GOWORK=off,-mod=readonly,
-tag codex_integration selector containing14top groups incl handshake/diagnostic/
client restrictions,95test-and-subtest passes,0fail/skips,6.4s commandwall;
/tmp/automatic-session-slugs-http-fallback-quick.jsonl. JS node--check passed.
gofmt/whitespace clean; undeclared hook frameworks, normal file-based commits,
no bypass. Tree-preserving interactive consolidation verified both tree hashes.
Full provider race476passactions/3skips, old-source compatibility3selected tests,
complete package/actualhostVM and normalCI passed the unchanged production tree;
no claim that skipped CI hostVM ran. Evidence/failed attempt logs in verification.md.

Owning docs codex-web/docs/reference.md (main writing pass) explicitly explain
supported fallback and limits; README links reference. Runtime feature contract
is docs/session-preparations.md, browser fixture test/README.md. Accepted design
rationale/test-only temporary states belong to this session; rollout.md is prepared
only. New deployment remains gated on native proof, creation browser and exact
final package/CI. Forward-only user-profile recovery; no system config/default
merge/stop/archive/delete approval.

Report concrete findings by severity/lane with source/commit references, whole
branch history/no-migrations conclusions and residual gaps. Send report to native
lead; parent records it and owns remediation/acceptance. Do not edit tracking.
Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/
