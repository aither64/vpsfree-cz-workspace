# Baseline refresh: independent committed review

**No new Blocking or Important technical findings.** The final histories are
consolidated, the supported deployed baseline is preserved, and there are no
migrations. The earlier B1 and R1–R3 dispositions remain supported by the final
source. The source assessment supports proceeding to preparation of the refreshed
artifacts, subject to the reviewer-settings qualification below. It does not
certify unbuilt artifacts or authorize activation or integration.

## Reviewer provenance and qualification

Native reviewer thread: `01a159bd-c577-7f01-900f-e41294b22209`. I read the installed
`lead_reviewed/reviewer-xhigh.toml`, the mandatory-change-review skill and all four
lane references. The review covers general, architecture/repetition,
scope/proportionality, and risk/compatibility concerns. Overall risk remains
high because the complete branches include provider routing, lifecycle recovery,
cross-project contracts and deployment selections.

The user explicitly authorized this standalone replacement because earlier
reviewer thread `01a15993-33e0-7d90-ba31-544f1ef95871` could not be resumed with its
multi-agent parent unloaded. No parent was resumed or reset, and no team or nested
agent was created. The original reports remain retained.

The native turn contexts establish `gpt-6-astra/xhigh` for the initial review
turn and `gpt-6.1-sol/xhigh` for this resumed completion turn, in the same native
thread. This differs from the requested catalog model for the resumed work.
Consequently, this report records a completed technical assessment but **does
not certify that the complete refreshed final review was performed under the
required Astra settings**. The coordinator must reconcile that review-policy
requirement before treating this report as an unqualified mandatory-review
acceptance. No alternative model was silently approved here. The earlier client
interruption and the parent's premature account-blocker declaration are not
product findings.

Only this report was written. Source, refs, tracking state, session ownership and
deployment state were left untouched.

## Exact final histories

I checked the complete base-to-head lists, commit messages, final differences,
saved inventory/diffs and relevant implementation, tests and documentation. All
four worktrees matched the following heads and were clean at the final check.
Each recorded base matched the merge base with the locally available
`origin/master`; no fetch or branch mutation was performed.

| Repository | Base | Final head | Complete ordered series |
| --- | --- | --- | --- |
| codex-web | `c064ce09cfcea8d8af6bf676635a53cd823f772c` | `8c616f768b38179754f5b3bf4f974906ee9f1a8e` | `641907f`, `f3633de`, `df4835b`, `9a8c5fd`, `8c616f7` |
| dev-workspace | `ea3f9d36397e8c2c846bd456e51385d73a3a358a` | `f92f63c76194555a6f3f320e0ddbe03300ff71d7` | `75efa1e`, `34b967d`, `8d23955`, `532c066`, `96e7520`, `f92f63c` |
| workspace | `650495d6bea856c75c5d717526c9a888f7f2fcf6` | `fe1a94f5832317f1133135854827fe14effd8c8d` | `0723c3f`, `05e1b67`, `e6058bb`, `bdd0200`, `fe1a94f` |
| vpsfree-cz-configuration | `6e79db5ab5e3b4e35ba3db1c1c8b94c4b833abd2` | `e43cc01f4cb596206d4fc686ae42df2f2d42dad3` | `e43cc01f` |

The saved `*-baseline-refresh.diff` artifacts equal Git's current complete final
diffs. Workspace's first four commits are coordination records already on shared
master `bdd020058fa0d74abd009b946199b3e9c824fdf0`; its feature delta is the one
final runtime-selection commit.

The source commits have distinct purposes: optional questions, provider routing,
deployed question fixes/presentation, archive recovery, and citations. Supporting
tests and documentation follow their behavior. The runtime dependency selection
is separated from its functional commits. Configuration retains its generated
confctl commit message.

## Supported baseline and composition

I independently compared all 502 tracked files of runtime
`6865e00bd91457ff5b84a568ab25572295484ff2` with the recorded installed source
`/nix/store/l6c7fgir4jyaylmyj8f4g8nj5q5w34g2-source` by Git blob identity. There
were no mismatches. This corroborates the installed-baseline comparison; it is
not a new observation or certification of the currently selected profile.

The rebuilt runtime retains the functional patches exactly, excluding only the
five dependency-selection files:

- `0aef1e2` → `34b967d`: optional-question integration.
- `eeff83f` → `8d23955`: archive recovery.
- `d68f88a` → `532c066`: naming-provider routing.
- `6865e00` → `96e7520`: compact question forms and receipt dismissal.

All four comparisons produced identical functional diffs. The final runtime
tree is `db627ba6b4821b876513e3bf9624055e23b213ed`, exactly matching
`refreshed-desired-tree.txt`. Original deployed runtime and provider refs remain
reachable through their retained local and remote feature refs.

The provider's citation patch has the same patch content as accepted commit
`4b73d71`, after removing Git index and hunk-position metadata. Its new parent
includes both deployed provider changes, `df4835b` and `9a8c5fd`. No citation
behavior was lost during that rebase. B1's two passive request corpus examples,
R1's pending-row repair and regression, and R2's `citations.js` fixture route
remain present. The original unaffected conclusions in `review.md` and
`review-followup-result.md` remain justified.

The newly inherited absent-identity fix requires a real pending answer attempt
and an explicit matching message ID before acknowledgement. Ordinary native
messages with a digest and no client ID therefore do not dereference an absent
attempt or abort refresh. The regression also checks that a genuine attempt is
still acknowledged.

The compact controller continues to own both inline and pinned views. Choice and
note compose into the complete draft; navigation and collapse do not submit.
Uncertain sends retain their exact saved envelope and attempt ID. Extra structured
draft fields are optional: a complete draft edited by an older browser takes
precedence when the structured fields no longer agree. Focus handling is bounded
to disappearing question controls. The receipt cross retains an accessible name,
persistent dismissal and the original retry rules.

Citations and questions share transcript entry identity without replacing raw
text or delivery digests. Both clients feed merged history into the same question
controller. Pending citations retain their refresh and repair paths after a
completed message leaves the newest page. Portal asset selections advance from
conversation v16/app v46 to v17/v47; the question controller import remains v2,
with its matching deployed styles.

## Whole-branch consolidation conclusion

I independently grouped dependency updates by their logical stream:

| Stream | Final disposition |
| --- | --- |
| Provider Goldmark dependency | One addition in `8c616f7`; no repeated selection. Provider `flake.lock` is unchanged. |
| Runtime codex-web selection | One update in `75efa1e` across `flake.nix`, `flake.lock`, `portal/go.mod`, `portal/go.sum` and `nix/workspace-portal.nix`. No later functional commit edits these files. |
| Workspace nested runtime selection | One final update in `fe1a94f`, including the transitive client lock. |
| Configuration devWorkspace selection | One generated update in `e43cc01f`, including the transitive client lock. |

**All repeated dependency-selection streams are consolidated.** No superseded
pin commit needs to remain in these final series. The original deployed source
refs preserve exact supported revisions separately; deployment is not being used
as an exemption for redundant pin history.

**No obsolete unmerged approach, citation fixup iteration, abandoned compatibility
path or transitional migration remains in the reviewed final histories.** The
retained provider fix `df4835b` and form change `9a8c5fd` are part of the supported
deployed provider baseline. The archive-recovery adapter supports existing
journals/receipts and remains required behavior. These are not abandoned citation
iterations to remove during consolidation. No further history consolidation is
required by this technical assessment.

## Architecture, compatibility and migrations

The shared provider owns source extraction, code-aware parsing, UTF-8 spans,
passive source recovery, DOM links and copied Markdown. The generic mounted UI
and reference application consume that contract; the portal uses its pinned Go
module, browser imports and `TransformTranscript` presenter. The repository
browser fixture is another verified asset consumer. The portal adds presentation
through its existing Markdown renderer and sanitizer rather than duplicating
source lookup. The new question presentation likewise remains in the shared
controller.

HTTP authority resolution, origin checks, trusted thread/cwd selection and
capabilities retain their existing boundaries. Source URLs are restricted to
HTTP(S) without credentials, DOM output uses text/attribute APIs, and portal
output passes through the existing sanitizer. No server-side source URL fetch is
introduced. The lifecycle and provider-routing patches are preserved exactly;
I found no new authority, destructive-operation or sanitization regression in
their composition with citations.

The runtime's Go module and flake both select client
`8c616f768b38179754f5b3bf4f974906ee9f1a8e`. Workspace and configuration both
select runtime `f92f63c76194555a6f3f320e0ddbe03300ff71d7`. The three client lock
records agree on `sha256-8pXTWRdYQnaV8BKa4uf1SWSEPGXnmI1LOG0eo9inuSU=`;
workspace and configuration agree on runtime content hash
`sha256-MNqWrRADCq4DRxdr38uxWD/69MeAPRK8FnHwKWhBUxU=`. The runtime declares
vendor hash `sha256-kesZAvELuNuBdQp3hogKQUWSipYzK0AskG8OonRSjbc=`.
Only the expected client/runtime lock nodes change. The workspace extension
remains `767dfd587e346168e1443e65ccdb67ce748f3fe3`, and native Codex inputs are
unchanged.

**No migrations.** There are no new migration files or versions, database schema
changes, durable server-state formats, conversation rewrites, runtime contract
versions or native Codex upgrades in these complete ranges. The inherited archive
recovery uses the existing schema-2/schema-4 journals and schema-3 cleanup
receipts. The question controller keeps browser record schema 1 with optional
extra fields and an older-browser-readable complete draft. Citation caches are
ephemeral. There are consequently no migration versions requiring merge,
release, deployment or external-use provenance, and no unsound intermediate
migration lineage to consolidate.

Older transcript clients can ignore additive citation/question fields; newer
clients receiving older transcripts retain the raw-text fallback. Software
rollback does not require reversing a citation conversion. Package-generation,
ownership and pending-journal rules still govern any actual switch or recovery.
The system/profile deployment split and need for matching reviewed source remain
unchanged.

The shared reference and portal guide describe the resulting supported behavior;
archive and preparation guides retain the relevant operational contracts.
Individual rollout identities and stale snapshots remain in session records.
No additional feature-documentation change was needed for the baseline refresh.

## Verification and remaining limits

Independent checks in this review:

- Exact heads, clean worktrees, locally available merge bases, complete series,
  saved-diff equality and `git diff --check` for all four ranges.
- All 502 deployed-baseline blob identities, reconstructed functional patch
  equality, citation patch equality, final runtime tree and retained refs.
- Dependency-selection commit inventory, final module/lock alignment and
  preservation of unrelated lock nodes.
- The shared flake's six Node browser contract files using the recorded Nix
  Node executable: **74 tests passed, zero failed**. This includes the new
  absent-identity regression and citation repair regression.
- The actual protocol corpus coverage command using installed Nix Python with
  `jsonschema`: passed. A first attempt with ambient Python lacked that module;
  the installed Nix environment resolved it without a source change.

Evidence correction: the packet says 75 shared Node contracts. The exact committed
flake command reports 74 passing tests. I use the directly observed count; this
does not establish a missing regression or a product defect.

I inspected the retained final CI results: client run
[39439556309](https://github.com/aither64/codex-web/actions/runs/39439556309)
completed successfully at `8c616f768b38179754f5b3bf4f974906ee9f1a8e`; runtime run
[39439858211](https://github.com/aither64/dev-workspace/actions/runs/39439858211)
completed successfully at `f92f63c76194555a6f3f320e0ddbe03300ff71d7`, with
fast/archive/creation successful and host skipped. These are retained CI result
records, not a new suite launched by this reviewer. The packet also reports
focused portal and composed-deployment checks; those were inspected in context
but not rerun here.

The earlier residual limits remain: direct cache replacement/append/generation
coverage and browser retry-timing coverage are limited. The updated rendered
question/browser acceptance test was inspected, but I did not launch Playwright
or a live native session. No long test, build, artifact preparation, activation
or integration was performed. The original preparations prove their old exact
revisions only; refreshed generation-bound system/profile preparations remain
required. Resolve the reviewer-settings qualification before recording an
unqualified mandatory-review acceptance, then continue the existing preparation
workflow for these exact heads.
