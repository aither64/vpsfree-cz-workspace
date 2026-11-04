# Optional local client development and terminology review

Session2026-11-01-typescript-client-migration, workspace
/home/aither/workspace/ai/vpsfree.cz. Retain independent reviewer0's saved
Astra/xhigh/read_only settings. This is final review after completed commits and
quick checks, before the new isolated install/restore validation. Read current
mandatory-change-review and all four lane references. Apply general/history,
architecture, scope and risk/compatibility to the bounded delta; retain unaffected
earlier migration reviews. Overall migration risk remains HIGH, while this new
milestone changes documentation, diagnostic/test labels and commit wording.
No nested reviewer, source/Git mutation, tests/builds/browser/DB operations.

## User scope

The user wants optional unreleased/local-checkout use of
vpsadmin-typescript-client, while merged code uses a released version. They also
asked to replace the introduced shorthand in this migration's changes and commit
messages with "generated client". The architect-owned brief is design.md section
"Optional local client development and terminology"; plan.md/state.md/backlog.md
record scope and actual progress.

Acceptance: ordinary pinned client build/pack, temporary no-save npm archive
installation, actual entrypoint/peer checks, normal consumer checks and Vite cache
restart, then npm ci restoration. No installer, script framework, Vite alias,
symlink/link lifecycle, persistent local dependency switch, second lock or optional
Nix mode. Regeneration still requires the exact recorded generator HEAD; building
checked-in source does not regenerate or certify provenance. Temporary npm install
may resolve other dependencies. Committed manifest/locks/vendor/provenance remain
untouched. A compatible published dependency remains an explicit pre-merge
prerequisite; none has been selected and publication is not authorized.

## Repositories and committed boundaries

Worktrees are beneath worktrees/2026-11-01-typescript-client-migration/.

| Repository | Prior reviewed/input head | New head | Delta |
| --- | --- | --- | --- |
| haveapi | eea3ae5e82c3db23d5f5bc9f1a5e7784117c4e1b | 52c37027f194ba1141fb7f5e5b6b45828989b126 | clients/typescript/README.md, one introduced phrase plus wrapping |
| vpsadmin-typescript-client | 99ee06654ef956a09b52749f4cd02d1435362087 | e16663a9e7ed1bbd7e25337b824283f635f47395 | README.md, one introduced phrase plus wrapping |
| vpsadmin-webui | published d3d5efbef53af8eb1caec025737dc47ecbc67e96 | 6c755ea2ba78c7ba8b27fe9e9731985903d67ce1 | message-only mapping to30ffc2bc, then15file source/docs commit |

WebUI source parent30ffc2bc5bc8df35fb6bd964eb0fa18fb86900b1 has the exact oldd3d5
treecd6428396126e2d4999eb3a71185425292b1ce1b. Final source commit tree is
5c4f692ca4fbf88ff76374af36aff8511babdf2c. All three worktrees/indexes are clean.

HaveAPI complete foundation base391b0190241cf195a69b06f7297d3e4eebec5a83;
client basee5786f69b7c223c3bb5b1de99b7f97186eec368a;
WebUI base63d484fc070dbee633d32624de545e834d483701. Earlier independent source,
packaging, readiness, final history and CI repair review conclusions remain
retained. Review affected README wording and source/provenance boundaries without
repeating unaffected generated/source audits.

## Source changes and documentation

WebUI has exactly15paths,+216/-80. docs/design/HAVEAPI_CLIENT.md owns the optional
procedure, and PACKAGING.md links it and explains removal of the archive adapter
when a real registry dependency is selected. API_CONTRACTS.md, ARCHITECTURE.md,
REQUIREMENTS.md and the dated migration log receive introduced terminology
corrections; existing heading anchors remain explicit aliases. No unsupported
release version, repin or new package mode is introduced.

Remaining edits are human diagnostics and directly paired test descriptions/
assertions in scripts/check-package-source.{mjs,test.mjs},
scripts/integration/vpsadmin-sdk-contract.{mjs,rb},
src/lib/api/{sdk.test,sdk.wire.test,systemConfig.test,vps.receipts.test}.ts,
src/pages/app/admin/nodes/NodeLifecycleModel.test.ts. Internal filenames, imports,
flags and identifiers remain. Preserve historical quotations, original error
evidence, commands, receipt paths and immutable reviewer reports. Assess that no
validation or failure guard changed while wording did.

The provider README is outside the canonical generator source digest; digest
ea539499207e09c7e1835733115aeca73db3175963b817c95a621baf45da330b and recorded exact
generator revisioneea3 remain unchanged. Client README is inside the old archive,
so the frozen99ee archive honestly retains its older wording. It was not repacked
or relabelled. Current source README is corrected at e166; the final selected
release must contain it. Any separately necessary new candidate would need real
packing/digests/provenance/lock/cache updates, not a source-equality assertion.

Archive remains337414bytes, SHA256
f3bb42d0392fb738f5c70fe1415cc8742ab943a31c2ed2a85af5ccbd385d831f;
rootlock SHA256585e8f48b194d8165731ca546fb709c94d531ee48224de9fff805416cb8b0f8e.
HaveAPI runtime0.32.0, generated client99ee, schema/generator inputs, manifests,
locks, flake/packages and production bindings are unchanged. The archive-specific
Nix adapter remains only because the current committed input is file:; it is not
needed by the optional developer procedure after registry transition.

## Authorized message-only history reconstruction

Exact user request authorizes replacement of the introduced word in our feature
messages, including the published WebUI series. Nine messages/fifteen occurrences
changed; seven messages remained byte-identical. No reorder, consolidation, source
change, base refresh, extra pin update or provider/client history rewrite occurred.
All16 old→new commits retain exact trees/binary patches and raw author AND committer
identity/date/timezone fields. Original publishedd3d5 is retained at
refs/heads/dev/typescript-client-migration-pre-client-terminology. All previous
preservation refs and original reports remain.

Lead independently read actual commit objects, compared every mapped binary
patch/tree/parent and raw identity/date field, and inspected all nine old/new
messages. See webui-client-terminology-lead-proof.json,
webui-client-terminology-original.json and webui-client-terminology-receipt.json
(SHA2569507eb892685bd49f0d7266cfd3fb79064be6c165f34f3b1c995fbb1486302b7),
webui-client-terminology.range-diff and -series.txt. One separate logical source
commit follows that mapping, so real source changes remain reviewable.

Final complete WebUI history has17commits,469files,+14347/-9520. Inventory:
webui-local-client-final-series.txt, webui-local-client-full.diffstat,
webui-local-client-source.diffstat. Explicitly assess whole-branch history under
the prior accepted owner split plus authorized message mapping and this single
follow-up. There remains one generated-client dependency/archive/provenance/Nix
stream. No DB/schema/persisted-format migrations or new consumed-state boundary.
No registry release, default merge or deployment.

## Quick checks and environment finding

Provider/client owners proved normalized one-phrase-only changes, unchanged links,
appropriate wrapping and clean diffs. HaveAPI's mandatory i18n/commit-message hooks
passed; no framework/custom hooks were declared for the client or WebUI. All
commits used verified contributor identity and normal commit-F without bypass.
Lead independently inspected both README diffs and clean states; receipt
client-terminology-readme-acceptance.json.

W source checker12+runner pure7 tests pass19/19; five focused Vitest files pass39/39
(8.47s), scoped8file ESLint, two JavaScript syntax checks, docs audit257routes/
73modules/177documents/76requirements, guide+datedlog Prettier and diff checks pass.
The documented entrypoint/peer snippet passes on the existing installation/runtime
0.32.0. No optional install/restore cycle has run yet.
Four other design documents fail whole-file Prettier identically at unchanged
parent30ffc; unrelated layout was retained. This is an existing formatting limit,
not a claimed whole-file format pass or changed formatting allowance.

Nix development-shell entry failed before the history preparation script/Git
mutation on an unrelated unrealized dependency fixed-output mismatch. No retry or
input repair occurred. Per lead disposition, Git2.54.0, Python3.13.15 and
Node24.21.0/npm11.19 were resolved from already-realized pinned store paths proven
by previous successful receipts. Contributor/hook checks remained intact. Exact
finding/tool identities are in the history receipt; this does not certify the
failed shell realization or excuse missing required hooks.

W source/staged/commit manifests are in w-local-client-commit-receipt.json and
paired source evidence. Committed blobs equal checked source; all worktrees clean.

## Remaining acceptance and limits

After review clearance, run one isolated optional override/restore cycle, using
ordinary npm/build/pack commands and existing Vite/typecheck/focused consumer
checks. Prepare commands only before clearance; no live source worktree install
or new harness. A local packed archive is a disposable development input, not a
new committed candidate or release. Record actual client/peer/archive identity,
protected-file equality, restoration and owned effects. No browser or API/DB
campaign is justified by wording changes.

Earlier review/runtime/package receipts stay bound to their exact inputs.
Literald3d5 Nix5 passed; source/tree equality alone does not certify new final-head
provenance. New-head publication/CI will follow applicable exact-head rules.
Core CI41450042642 passed on d3d5; Playwright41450042371 was cancelled after recorded
assertions. Implementer0 owns bounded read-only diagnosis of those exact logs;
this separate verification gap is not a pass or proof against the new optional
procedure. No affected final browser rerun has been authorized merely by this packet.

Return findings/severity or no findings, explicit scope/architecture/compatibility,
history/equivalence/input-stream and no-migration conclusions. Assess whether the
documented optional workflow is conventional, reproducible in its claimed scope
and honestly restored without loosening release/provenance guards. Save/report
local-client-terminology-review-result.md; if read_only prevents writing, report
the exact text to lead for persistence. Session stays open. No lifecycle action.
