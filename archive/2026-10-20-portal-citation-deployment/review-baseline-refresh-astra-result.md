# Baseline refresh: final Astra review

**Accepted. No remaining Blocking or Important technical findings.** I accept
the four exact committed ranges below across the general, architecture/repetition,
scope/proportionality, and risk/compatibility lanes. Their complete histories
satisfy the final consolidation requirement, preserve the supported deployed
baseline, and contain **no migrations**.

This completes the independent final source/history review for the refreshed
candidate and permits the planned verification and artifact-preparation work to
proceed under its existing authorization. It does not certify unbuilt artifacts
or authorize activation, integration, reservations or lifecycle changes.

## Verified reviewer and provenance

Reviewer: standalone native thread `01a159bd-c577-7f01-900f-e41294b22209`,
catalog role `lead_reviewed/reviewer`. I verified the actual current native turn
context before acceptance:

- Turn: `01a159d2-cada-7a10-8c0d-158f086b62d4`.
- Context timestamp: `2026-10-20T14:59:09.643Z`.
- Model: **`gpt-6-astra`**.
- Reasoning effort: **`xhigh`**.

The mandatory-change-review skill authorized the standalone fallback after
supported resume of earlier child reviewer
`01a15993-33e0-7d90-ba31-544f1ef95871` refused because its multi-agent parent was
unloaded. This was the procedure's native-availability fallback, not a
user-requested team creation or model substitution.

My initial Astra turn performed substantial direct source and history
inspection. The intervening Sol/xhigh turn produced the qualified technical
assessment in [review-baseline-refresh-result.md](review-baseline-refresh-result.md).
I read that report as advisory evidence, retained my initial inspection, and
independently reassessed the relevant source, composition and history evidence
in this verified Astra turn. This report supplies the final decision and resolves
the prior model qualification; the earlier report remains unchanged as evidence.
Its attribution of fallback authorization to the user is corrected here.

The installed role, mandatory review skill, all four lane references, workspace
procedures and affected repository instructions were read during this continuous
review. Overall risk remains high because the complete branches include
cross-project contracts, provider routing, lifecycle recovery and deployment
selections. The client's earlier interruption is not a technical finding.

## Exact accepted histories

I rechecked all four heads, clean worktrees, complete ordered series, merge bases
against locally available `origin/master`, and equality between the saved final
diffs and Git's current complete diffs. No fetch or ref mutation was performed.

| Repository | Base | Accepted final head | Complete ordered series |
| --- | --- | --- | --- |
| codex-web | `c064ce09cfcea8d8af6bf676635a53cd823f772c` | `8c616f768b38179754f5b3bf4f974906ee9f1a8e` | `641907f`, `f3633de`, `df4835b`, `9a8c5fd`, `8c616f7` |
| dev-workspace | `ea3f9d36397e8c2c846bd456e51385d73a3a358a` | `f92f63c76194555a6f3f320e0ddbe03300ff71d7` | `75efa1e`, `34b967d`, `8d23955`, `532c066`, `96e7520`, `f92f63c` |
| workspace | `650495d6bea856c75c5d717526c9a888f7f2fcf6` | `fe1a94f5832317f1133135854827fe14effd8c8d` | `0723c3f`, `05e1b67`, `e6058bb`, `bdd0200`, `fe1a94f` |
| vpsfree-cz-configuration | `6e79db5ab5e3b4e35ba3db1c1c8b94c4b833abd2` | `e43cc01f4cb596206d4fc686ae42df2f2d42dad3` | `e43cc01f` |

Workspace's first four commits are shared coordination history; its feature
delta above shared master `bdd020058fa0d74abd009b946199b3e9c824fdf0` is the single
runtime pin. The independently reviewable functional changes remain separated,
their tests/documentation accompany the behavior they support, and the
configuration update retains its generated confctl message.

**Whole-branch history and consolidation: accepted.** Runtime selects the
provider once in `75efa1e`, across `flake.nix`, `flake.lock`, `portal/go.mod`,
`portal/go.sum` and `nix/workspace-portal.nix`. Later functional commits do not
edit those files. Workspace has one runtime selection in `fe1a94f`; configuration
has one generated selection in `e43cc01f`. Provider adds Goldmark once in its
citation commit and leaves its flake lock unchanged. There are no remaining
repeated dependency-selection streams or superseded pin iterations.

No obsolete unmerged citation approach, fixup-only citation commit, unused
branch-only compatibility path or transitional migration remains. The inherited
provider fixes and presentation changes belong to the supported deployed
baseline. The archive adapter supports existing journals and receipts. Retaining
those functional boundaries is justified; development deployment has not been
used to retain redundant dependency pins. No further consolidation is required.

## Baseline preservation and technical assessment

The initial Astra inspection independently matched all 502 tracked blobs of
runtime `6865e00bd91457ff5b84a568ab25572295484ff2` to the recorded installed source
`/nix/store/l6c7fgir4jyaylmyj8f4g8nj5q5w34g2-source`, with no mismatches. In this
turn I reverified exact functional patch equality after excluding only the five
dependency-selection files:

| Original functional commit | Reconstructed commit | Result |
| --- | --- | --- |
| `0aef1e2` optional questions | `34b967d` | Identical |
| `eeff83f` archive recovery | `8d23955` | Identical |
| `d68f88a` naming-provider routing | `532c066` | Identical |
| `6865e00` question forms and receipt dismissal | `96e7520` | Identical |

The original runtime `6865e00` and provider `9a8c5fd` remain reachable through
retained local and remote `2026-10-19-browser-optional-questions-before-navigation`
refs. The final runtime tree is
`db627ba6b4821b876513e3bf9624055e23b213ed`, matching the saved desired tree.
The provider citation patch has the same patch content as accepted `4b73d71`,
excluding only Git index/hunk-location metadata. Its parent includes both
`df4835b` and `9a8c5fd`.

I independently assessed the following composition boundaries:

- The absent-delivery-identity guard requires an actual matching pending attempt.
  A digest without a client ID cannot dereference an absent attempt or prevent
  subsequent transcript/receipt reconciliation. The positive acknowledgement
  path retains the saved attempt identity.
- The compact question views share one controller and draft. Choice/note fields
  preserve the complete draft string, and an older browser's changed string
  takes precedence when structured fields disagree. Uncertain delivery retries
  the exact saved message and ID. Collapse/navigation do not submit; receipt
  dismissal persists before hiding the notification.
- Citation repair retains completed pending rows that age out of the newest
  page and preserves traversal progress. It updates presentation without
  rewriting raw text, question identity or delivery digests. I ran an additional
  in-memory composition check through newest-page aging, repair, repeated
  ID-less-message refresh, copied citation links and subsequent question
  submission. The stored draft and composed answer survived, and no refresh
  submitted a message.
- Both production clients consume the same citation contract and question
  controller. The portal uses the provider's Go spans through
  `TransformTranscript`, its existing Markdown renderer/sanitizer, and shared
  copy helpers. The generic client uses DOM text and link construction. The
  repository browser fixture serves the new imported citation module.

These checks support the earlier B1 and R1–R3 resolutions. The protocol corpus
entries, pending-row regression, fixture route and consolidated dependency stream
are all retained. The unaffected conclusions from [review.md](review.md) and
[review-followup-result.md](review-followup-result.md) remain valid.

**Architecture and scope: accepted.** Parsing, source recovery and shared browser
behavior remain owned by codex-web. The portal's adapter is narrow and does not
duplicate citation lookup or question state. The newly inherited mechanisms
preserve concrete deployed functionality; they add no speculative framework or
unrequested execution path. Project references and portal/lifecycle documentation
describe supported behavior, while rollout identities remain in session records.

**Risk and compatibility: accepted.** Existing opaque-conversation authorization,
trusted cwd/thread selection, origin/capability checks and message retry
boundaries remain intact. Citation destinations are HTTP(S) without credentials;
source URLs are not fetched by the server. Rendering retains the established
sanitization and DOM boundaries. The unchanged inherited lifecycle/provider
patches retain their ownership and generation checks. I found no new
authorization, data-loss, destructive-operation or rendering-security defect in
the refreshed composition.

## Pins and no-migration conclusion

Runtime's Go module and flake select provider
`8c616f768b38179754f5b3bf4f974906ee9f1a8e`. Workspace and configuration select
runtime `f92f63c76194555a6f3f320e0ddbe03300ff71d7`. Client and runtime content
hashes agree across their corresponding lock nodes. Only the expected
client/runtime nodes change; extension
`767dfd587e346168e1443e65ccdb67ce748f3fe3` and native Codex inputs remain
unchanged. Runtime retains the packet's vendor hash
`sha256-kesZAvELuNuBdQp3hogKQUWSipYzK0AskG8OonRSjbc=`.

**No migrations; migration lineage accepted.** The complete ranges introduce no
database migrations, durable server-state schema versions, conversation
conversions, runtime contract versions or Codex upgrades. Archive recovery
continues to use existing schema-2/schema-4 journals and schema-3 cleanup
receipts. Browser question records retain schema 1 with optional choice/note
fields and a complete draft readable by older clients. Citation caches are
ephemeral. No migration version requires merge, release, deployment or
external-use provenance, and no transitional migration needs consolidation.

Optional transcript additions preserve raw messages and permit older clients to
ignore new fields; newer clients retain their raw-text fallback for older
transcripts. No citation data conversion must be reversed on software rollback.
Actual package transitions remain subject to existing generation, ownership and
pending-operation rules. Matching system/profile preparation remains required.

## Verification and acceptance limits

The initial Astra inspection and this turn independently establish source,
history, baseline and composition conclusions. This final turn also passed all
four complete-range `git diff --check` commands and the additional in-memory
composition check described above.

The exact broad command `node --test test/*browser_contract_test.cjs`, using the
recorded Nix Node, passed **75 tests** in this turn. Its seven files include
`paging_browser_contract_test.cjs`. The committed flake explicitly lists six
files and passed **74 tests** in the preceding direct run. Both counts are
correct for their respective commands; the earlier report's count-discrepancy
qualification is resolved. The protocol-corpus coverage check also passed in the
preceding completion, and the relevant source is unchanged.

I rechecked retained CI evidence for the exact accepted heads: client
[39439556309](https://github.com/aither64/codex-web/actions/runs/39439556309)
and runtime
[39439858211](https://github.com/aither64/dev-workspace/actions/runs/39439858211)
are successful. Runtime fast/archive/creation succeeded; host was skipped.
The packet's focused portal and composed-deployment results supplement those
records. I did not launch a long test, live native session, Playwright suite or
build during this review.

No new Advisory finding is raised. The previously recorded limits remain:
direct cache replacement/append/generation and browser retry-timing coverage is
limited, and refreshed generation-bound system/profile artifacts still require
their own preparation and evidence. These do not prevent acceptance of this
source/history review. Earlier artifacts certify only their earlier revisions.

The final decision is **accepted for all four exact ranges and all four review
lanes**, with no remaining model/effort qualification. Only this new report was
written; source, prior reports, refs, session state and deployment state were
left unchanged.
