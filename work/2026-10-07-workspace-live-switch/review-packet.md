# Final committed-deliverable review packet

This is the original committed review snapshot. [state.md](state.md) records
the findings, narrow fixture corrections, followup general/risk review, final
published heads and subsequent verification. The production patch remained
unchanged; each final branch retains one coherent commit and no migrations.

Outcome: workspace portal/tooling and catalog changes should switch without
requiring all Codex threads idle when native launch semantics are unchanged.
User accepted one idle bootstrap cutover and authorized deploying aitherdev
and merging dev-workspace, workspace, and configuration to master.

Initiative: 2026-10-07-workspace-live-switch; threadless, no retained roster.
Read plan.md, design.md, state.md here. Worktrees share the slug:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-07-workspace-live-switch/

Complete branch inventory:
- dev-workspace base 9f999f7f713557b261a3d6d1597f8372eabf6518;
  head 89bf67949e98c148ee17fc7816885bd890054bb8; single functional commit
  host: preserve Codex during compatible workspace switches.
- workspace base 9efbe8edd756a679ce239f4737566ee8df4c4483;
  head 1856956e2c5c6a6e2addb589afcff1b3bfbeef89; single runtime selection.
- vpsfree-cz-configuration base 23412037590f1d31b85a53410946a18b36db8bc8;
  head 2a3a56da82a4435c660e1bc9b92553089b17cb47; generated confctl pin.
All branches published and clean. Inspect complete git log and base-to-head
diff for each. No superseded approaches or fixups in the committed series.
No migrations: existing marker, pending, roster and journal schemas retained;
additive runtime capability only. Nothing deployed from these branches yet.
Tests, docs and report routing stay with the host change because safe live
switching requires the stable report dispatcher and bootstrap policy together.
Downstream generated selections are separate commits in their repositories.

Risk: high, host package transitions and mixed generations. Review all four
lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
Selected standalone reviewer: gpt-6-astra/xhigh, read-only, installed default
lead_reviewed reviewer. Catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd,
matching native role dw_34bb6a768d6175719d13cda28b7adc221b586314b3fc5167.
Fallback reason: team list refuses because this initiative has no lead thread.
Native policy name and saved model/effort verified against installed metadata.

Quick checks passed in generic nix develop: 126 Ruby host tests, 1018
assertions; 3 report-binding tests, 18 assertions; Go cmd/workspace-portal,
internal/teamruntime, internal/agentteams, internal/web; explicit native
integration tag compiles with no test execution. git diff --check passes.
Configuration Overcommit installed: Nixfmt and commit-message hooks passed
(generated confctl message width warning retained as required).
Downstream bin/check-dev-workspace-deployment passed exact selected revision.
Long packaged and native integration checks have not started.

Owning component: generic dev-workspace owns transition decision, additive
capability and internal helper CLI. Consumers: composed vpsFree extension
0ff827df13e82dfab4b536ff29979280f264e8f5 through workspace nested override,
and configuration devWorkspace input/channel for host module. Both select the
same new runtime, with siblings and extension unchanged. codex-web is pinned
3d07cf60cfde and not modified. Read representative wrapper/portal contracts at
these revisions. Local host operator trusted; concurrency, state integrity,
remote authorization and exact session identity remain protected.

Documentation: generic docs/workspace-portal.md and docs/codex-package.md
explain immutable launch provenance, live eligibility, one bootstrap restart,
profile dispatcher and forward recovery. Exact rollout lives in this session.
No member-facing KB changes. Application remains a separate user profile;
host system configuration does not install it. Host deploy first, guarded
candidate application switch next; never interrupt unrelated threads to force
cutover. No changes to archive/delete/suspend policy, rosters, native Codex
implementation or default branch topology. No rollback to an older package.

Acceptance includes busy-compatible switch, catalog-only update, candidate
binary/launch mismatches, missing markers, legacy bootstrap, custom profiles,
forward failure/retry. The explicitly tagged native fixture will verify running
lead/member turns, queued-message identity and approvals/questions across a
client reconnect using temporary state and a loopback synthetic model provider.
Independent review must explicitly conclude whole-branch history and migration
lineage, including no migrations. Do not run long integration or deploy.
