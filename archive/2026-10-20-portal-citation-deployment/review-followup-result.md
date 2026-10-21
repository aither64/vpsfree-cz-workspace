# Final citation review follow-up

Reviewer: `/root/citation_review`, same independent
`gpt-6-astra` / `xhigh` role. Scope: affected general/history and
risk/compatibility concerns from [the original review](review.md).
The original unaffected architecture, scope, security and consumer conclusions
remain applicable.

**No remaining Blocking or Important findings in the reviewed changes.**
B1 and R1–R3 are resolved. The exact heads below are accepted for the planned
long verification and artifact preparation. This does not certify unbuilt
artifacts or authorize activation or master integration.

## Finding dispositions

| Finding | Disposition | Evidence |
| --- | --- | --- |
| B1: missing protocol corpus entries | Resolved | The corpus now includes the citation worker's two request shapes. The required coverage check passes independently. |
| R1: pending rows lose refresh after leaving newest page | Resolved | Completed citation-pending rows now use the existing history repair path. An in-progress repair target survives subsequent newest refreshes. The new regression passes. |
| R2: missing fixture asset route | Resolved | The repository browser fixture serves `citations.js`. The original handler reproduction now returns HTTP 200 for the versioned request. |
| R3: repeated runtime client pins | Resolved | All five runtime selection files change once, in `2773026`; later functional commits contain no additional pin edits. |

The R1 change stays within the original behavior boundary. It extends the
existing repair eligibility predicate to unresolved citations, while retaining
thread checks, cursor recovery, repair throttling and row merging. Keeping an
existing repair target prevents a newest refresh from resetting progress before
the traversal reaches the target. The regression exercises a completed row
leaving the newest page, an intermediate history page, another newest refresh,
discovery of the target, continued source resolution and preservation of the
previously loaded rows.

The B1 examples match the implementation: trusted thread/turn IDs, a limit of 32,
descending order, `itemsView: notLoaded` for turn listing, and opaque continuation
cursors. They add coverage for existing passive APIs, without changing the
supported native protocol or broadening browser authority.

## Exact reviewed histories

| Repository | Base | Final head | Complete commit sequence |
| --- | --- | --- | --- |
| codex-web | `c064ce09cfcea8d8af6bf676635a53cd823f772c` | `4b73d71140d1fc6ba5e43f7144bad45d7c48af9f` | `641907f`, `f3633de`, `4b73d71` |
| dev-workspace | `ea3f9d36397e8c2c846bd456e51385d73a3a358a` | `52f87e18e21b0e878f1255326d72cfdff61f4e09` | `2773026`, `1284b52`, `4e1cc3c`, `935a087`, `52f87e1` |
| workspace | `650495d6bea856c75c5d717526c9a888f7f2fcf6` | `bbd090ee96c8a093082941f36e25cc42241d20ed` | `0723c3f`, `05e1b67`, `e6058bb`, `bdd0200`, `bbd090e` |
| vpsfree-cz-configuration | `6e79db5ab5e3b4e35ba3db1c1c8b94c4b833abd2` | `39949743c01e3bd03a39219e55c4165619bdffac` | `3994974` |

All four worktrees matched these heads and were clean. I inspected the complete
series, their final differences and the changes since the original review.
The workspace range deliberately includes coordination records already on
shared local master `bdd02005`; its feature delta above that master is the
single final runtime pin.

The runtime's dependency selection is consolidated into one first commit across
`flake.nix`, `flake.lock`, `portal/go.mod`, `portal/go.sum`, and
`nix/workspace-portal.nix`. I independently compared the reconstructed
functional patches with their originals, excluding those five selection files:

- `0aef1e2` → `1284b52`: exact functional diff equality.
- `eeff83f` → `4e1cc3c`: exact diff equality.
- `d68f88a` → `935a087`: exact diff equality.

The final runtime tree is
`e3adf583107d8e7b367a11ffae6a67ec57ca9ea8`, matching the saved desired tree.
Compared with the originally reviewed runtime, only the five updated selection
files and the R2 fixture route differ. The original deployed runtime commit
`d68f88a` remains reachable through retained feature/review refs; the original
provider boundary `f3633de` remains reachable as well. Supported optional
questions, archive recovery and provider routing are preserved.

The shared provider's citation fixes are folded into its citation commit.
Its earlier `flake.nix` edit adds a question test command; it is not another
dependency selection. The provider has one Goldmark dependency addition.
Workspace has one final runtime-selection update, and configuration has one
generated confctl update with its generated message retained.

**History conclusion:** all repeated dependency streams identified in the
reviewed ranges are consolidated. No obsolete unmerged approach, superseded pin
iteration, fixup-only commit, or branch-only migration path remains.

## Pins, migrations and remaining verification

The runtime selects codex-web
`4b73d71140d1fc6ba5e43f7144bad45d7c48af9f` through both its Go module and flake.
Workspace's nested runtime selection and configuration's `devWorkspace` both
select `52f87e18e21b0e878f1255326d72cfdff61f4e09`, with matching content hashes
and matching transitive codex-web hashes. The workspace extension remains
`767dfd587e346168e1443e65ccdb67ce748f3fe3`; unrelated lock identities are
preserved. The existing system/profile deployment split remains intact.

**No migrations.** No persisted-state version, native Codex version, raw
conversation format, server-state schema or rollback format changed in this
follow-up. The original no-migration conclusion and retained archive-format
compatibility remain valid; no migration provenance inventory is required.

Independent checks in this follow-up:

- Exact heads, cleanliness, complete histories, functional patch equality,
  final runtime tree identity and selection-file edit inventory.
- `git diff --check` over every complete final range.
- Citation browser contract script, using the recorded Nix Node: passed.
- Original R2 fixture-handler reproduction: both the conversation module and
  `/citations.js?v=1` return HTTP 200.
- `nix develop --command python3 ../codex-web/test/codex_protocol_contract.py
  --coverage-only ../codex-web/codex/client.go`, from dev-workspace: passed.

The follow-up packet also reports passing 74 shared browser contracts, focused
portal checks, the composed deployment check and client CI run `39435851092`.
Those reported results supplement the independent checks above. No long suite,
source edit, activation, merge or artifact build was performed by this reviewer.
The original residual cache-invalidation/browser-timing coverage limits remain;
the planned package, native integration and aitherdev preparation checks still
need their own exact-revision evidence.
