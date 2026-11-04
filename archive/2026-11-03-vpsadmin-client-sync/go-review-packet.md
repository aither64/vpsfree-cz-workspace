# Go Phase 1 final review packet

Prepared by implementer0 after all intended Go changes were committed and quick
checks passed. Lead assigns retained reviewer0 when available; this packet does
not claim independent acceptance or integration readiness.

## Outcome and exact scope

Refresh vpsadmin-go-client for the accepted current API 7.0 source contract and
prepare release 0.2.0. This package owns only this client. No Phase 2 rules/CI
subsystem, generator/API source edits, WebUI work, integration, tag, publication,
deployment or lifecycle action is included.

- Session: `2026-11-03-vpsadmin-client-sync`; see [plan](plan.md),
  [design](design.md), [state](state.md) and [shared source receipt](source-inputs.md).
- Repository: `git@github.com:vpsfreecz/vpsadmin-go-client.git`, target `master`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-go-client`.
- Branch: `2026-11-03-vpsadmin-client-sync`.
- Base: `134a9e69f9aa6ddec5c94b53744865c6f81ecdd0` (fresh remote master still
  equals base immediately before feature push).
- Final head: `7bc136e1d72f15174229bea2bb7de284174512f2`; feature branch SSH push
  succeeded and `ls-remote` confirmed this exact head. Worktree is clean.
- `gh run list` for this branch returned `[]`; the repository has no workflow.
- Existing annotated release `v0.1.0` peels to base; Go proxy lists that version.
  No new tag or release was created.

## Complete history and disposition

| Commit | Purpose |
| --- | --- |
| `126fa8fd4e7e822a6c573a71128b69c2b1a7010e` | Handwritten finite schema projection, Python tests, public Go OAuth transport-stub tests, Python shell input and cache exclusion |
| `108476028f63ef992c9a4e37269c534719f1c398` | Single generated refresh plus raw/effective schema, exporter/generator locks and exact source/toolchain receipt |
| `7bc136e1d72f15174229bea2bb7de284174512f2` | Release 0.2.0 changelog, current behavior/regeneration README and accurate contributor commands; narrow review correction folded into this owning commit |

This is the complete base-to-head series. No superseded approaches/fixup commits
or intermediate generated/pin updates remain. One generated/input stream occurs
once, in `1084760`; all final inputs and output are together. The handwritten
compatibility step is separate because it is substantive owned behavior; release
prose is independently reviewable. No retained intermediate boundary is needed.
**No migrations** were authored or changed, merged, released, deployed or consumed
by this branch. Migration inventories in the raw exporter receipt are source
evidence, not new migrations.

Inspect the full series and diff with ordinary `git log --reverse BASE..HEAD`,
`git diff --stat BASE..HEAD`, and `git diff BASE..HEAD`. Final diff: 24 files,
218,417 added/19 removed lines; most added lines are two required 3.5 MiB input
snapshots (107,961 lines each). Raw and effective retention is the approved
provenance contract, not handwritten logic. Helper/test/support commit adds 215
lines. Review the snapshots structurally and validate the exact projection.

## Inputs, transformation and ownership

Accepted API source: `942c6eaed41331f823d8e0f670ed239e2b308440`. Generator source:
`1ef9b204ba45bb261d3334be5c555cc1856b713b`, HaveAPI Go/Ruby 0.32.2. This pin is
not an ancestor of current HaveAPI master; it is retained honestly as a source
dependency, with completion handling owned by the lead.

Raw shared export SHA-256:
`d6ec617653913c56e92398a6032aa350118597a0e3f45c599bc92b6071ea0a26`.
Raw provenance SHA-256:
`c85815abd315f53a5ef05f324abe377760293786a13a25b7a127ec804c50e0c1`.
Exporter lock SHA-256:
`62a0e7f65e0755296ea50e3f5efa590f51e8615571a078cf45243f6ca8555f1c`.
Generator component lock SHA-256:
`f75dfbefc8ced373a643517b9a416ac8886695b9ac74e2cf8bd2eabd0be1afc5`.

`schema/source-api-7.0.json`, `schema/provenance.json` and
`schema/tooling.Gemfile.lock` are byte-identical copies of approved shared input.
`tools/prepare-schema` derives `schema/api-7.0.json`, SHA-256
`8953f1d35e3015d3bbc14d8cd7c456982ac57e9a55ecace3d5ce8bc11d4ec31c`.
The only parsed difference is `description.authentication.oauth2.revoke_url`,
from `http://api.test/_auth/oauth2/revoke` to
`https://auth.vpsfree.cz/_auth/oauth2/revoke`. The finite helper rejects any
unexpected envelope/profile/mount/source URL or old endpoint and source/output
aliasing. It preserves raw bytes. `schema/generator.json` binds both hashes,
helper hash, exact change/command/module/package, 95 generator/shared-client/Nix
source hashes, lock identities and generation tool paths/versions.

Generation used Ruby 3.4.11, Bundler 4.0.23, Go 1.26.10 from the pinned HaveAPI
`client-go` Nix environment, frozen isolated component dependencies, and two fresh
output directories. Whole generated module trees were byte-identical. Reconciled
only generated `client/*.go`; preserve handwritten `*_test.go` files and existing
`go.mod` (`go 1.16`). The generator's fresh module omits the existing Go directive;
the receipt explicitly records preserved module metadata.

## Contract and compatibility assessment to verify independently

Output goes from 682 to 684 generated Go files: exactly two action files added,
eight existing files changed, no stale removals. Adds advisory Delete/Destroy and
Retract resource members/action types and `ExpectedState`, its setter and request
map entry on advisory Update, CVE Create/Update/Delete and nested NodeStatus
Create/Update/Delete. New actions also include revision/state inputs.

No existing exported fields or types were removed, and no existing field's type
changed. Added fields can
break unkeyed composite literals of exported structs. Keyed literals still
compile, but input literals or direct field assignments without selection can
send empty `expected_state`, which the server rejects. Setters or
`SelectParameters` select sent fields and omit an unused state guard. Release
0.2.0 and its changelog state both caveats. New actions/state guards require compatible
API deployment/capability checks; a source fixture is not deployment evidence.
No consumer dependencies or runtime packages change.

The raw fixture otherwise yields the same Go output as the previous public
capture outside these advisory additions. Existing `auth_oauth2.go` and
`request.go` are byte-identical to base: production revoke endpoint, explicit
origin trust and clear-on-success behavior stay intact. No trust relaxation or
generated hand edit occurred. Custom inputs remain unsupported by typed structs;
the README's existing limitations table matches the seven raw-schema inputs.

Public owner/interface is the vpsAdmin API contract and exported
`github.com/vpsfreecz/vpsadmin-go-client/client` package. Representative local
consumers are README examples and the external `client_test` package exercising
public OAuth methods. External downstream modules were not changed or claimed
tested. No real API/OAuth request was sent. Rollback can return consumers to
v0.1.0; no persisted state or schema conversion is introduced.

## Verification and documentation

- Shared source owner independently exported from two fresh DB fixtures;
  raw triple matched exactly; source checks and 14 exporter specs passed.
- [go-generation.sh](go-generation.sh) completed twice-to-fresh generation and
  `diff -qr`, exit 0/19 seconds; [full log](go-generation.log).
- [go-quick-checks.sh](go-quick-checks.sh), under the client's declared
  `nix-shell`, completed exit 0/23 seconds: Python 3.13.15, Go 1.26.8, four
  projection tests, OAuth origin/endpoint/success/failure transport-stub tests,
  package compilation, Go formatting and diff whitespace checks.
  [Result](go-quick-checks-result.md), [log](go-quick-checks.log).
- Fresh `/root/go_quick_checks`, `gpt-6-luna`/low with installed verification
  utility policy/config and full access, owned the quick operation; no running
  check remains. Generation/setup utilities were lead-owned and completed.
- Quick tests covered the final code/input tree; only approved prose edits
  followed. Final relative documentation links, commands and whitespace were
  checked after the writing pass. No duplicate tests were run for prose changes.
- Lead directly applied vpsfree-user-facing-writing/humanizer-en to README,
  CHANGELOG and AGENTS draft; all requested narrow edits are committed.
- No hook framework or active hooks exist in this client; normal Git commits
  did not bypass hooks. No PR is required or created.

Changed project documentation explains current OAuth behavior, source/effective
input provenance, exact generation and owned-file replacement, offline checks,
release changes and compatibility limits. Session-specific evidence stays here.
No long Go integration suite exists in this repository or has been run; no
additional package-specific long command is required by its guidance. Any
separate post-review consumer/package verification and released-module fetch
belong to the lead's accepted next batch/publication procedure.

## Requested independent review

Reviewer0 identified an Important general/risk documentation finding while
reviewing base `134a9e69f9aa6ddec5c94b53744865c6f81ecdd0` through original head
`217885c90b08556e563da5ce74c6856d28acdacc`: the original keyed-literal wording
overclaimed runtime compatibility. The lead supplied writing-skill-reviewed
replacement text. Applied it verbatim with existing wrapping/markup, amending
only the owning release/docs commit to final head
`7bc136e1d72f15174229bea2bb7de284174512f2`. Old/new base-to-head ranges retain
the same first two commits; `git range-diff` confirms only the release-note
paragraph changes (CHANGELOG.md, six added/three removed lines). README made no
keyed-literal overclaim and was unchanged. Generated output, helper/tests,
provenance and dependency graphs are identical to the reviewed old head.

Checked `SelectParameters`, `IsParameterSelected` and `makeInputParams` names and
selection behavior directly, and whitespace passed. Per the lead's narrow-fix
direction and mandatory review step 9, no code tests were rerun for this prose
amendment. Explicit old-head feature lease push succeeded; fresh `ls-remote`
confirmed final head and workflow list remained empty, so there were no
superseded CI runs to cancel. Lead owns direct remediation verification and
final review acceptance; this packet does not substitute for that decision.

Overall risk **high**: public generated contract and OAuth credential-destination
compatibility, despite preserved runtime trust code. Proposed retained reviewer:
`reviewer0`, saved `gpt-6.1-sol`/xhigh, selected/verified by lead. Cover general,
architecture/repetition, scope/proportionality and risk/compatibility lanes using
mandatory-change-review and all four lane references. Independently conclude
whole-branch history/consolidation and migration lineage, including “no
migrations”; assess the finite OAuth exception and input/output provenance.
Report concrete findings and verification gaps rather than assuming this
assessment is correct. Lead owns assignment, acceptance and integration approval.
