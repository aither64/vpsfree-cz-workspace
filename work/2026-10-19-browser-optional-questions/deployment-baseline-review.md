# Deployment baseline refresh review

No findings in the affected general/history and risk/compatibility lanes at
configuration **`316a071cd6cc3dd090661edac5a0e8d0d927d2c5`**. The baseline
changes aitherdev's system inputs, so fresh system build and deployment
verification remain required.

Reviewer: standalone thread `01a158b3-36f1-79d1-ac68-59669f3edd1a`.
The final turn's native context confirms `gpt-6-astra` / `xhigh`, matching the
assigned catalog `ffaf9deb` review-purpose fallback. This conclusion uses the
original independent inspection and the restored settings; it does not adopt
a conclusion from the interrupted default-model resume. The original reviewer
`/root/optional_questions_review` remains independent, but its internal identity
was rejected by the available direct app-server interface and the parent
collaboration follow-up interface was unavailable. No roster change was made.
Risk is High because host inputs, deployment ordering and recovery are involved.

This report supplements
[archive-repair-followup-review.md](archive-repair-followup-review.md).
Its unchanged runtime, UI and workspace conclusions remain retained. I read the
mandatory review skill and both assigned lane references, workspace instructions,
applicable Git, deployment, verification, lifecycle and documentation procedures,
configuration instructions, and the configuration's aitherdev operations guide.
The packet is [deployment-baseline-review-packet.md](deployment-baseline-review-packet.md);
the individual rollout remains [rollout.md](rollout.md).

The reviewed configuration range is
`e646cf61dff7557c16ee2534ae5b809efa6a2d94..316a071cd6cc3dd090661edac5a0e8d0d927d2c5`.
Its complete feature series contains exactly one commit:
`316a071c inputs: set devWorkspace to 1395387f`.
I inspected the actual commit message and final diff and independently repeated
the range comparison with the previously reviewed
`7ffa98a5761e001ed22b70fa24eecc21ff8c58ca..2127f78c6aac40b9bab9b4f1dc74cb732ffc42b6`.
Git range-diff reports equality; both patches have stable patch ID
`8d6bb97d68fd25d9816f105b029ad4a545117d69`.

The final feature diff changes only `flake.lock`: `devWorkspace` selects
`1395387ff02729256ba52cc7c9ded74397cbe1a6`, with its expected transitive
codex-web selection at `641907fb3afa2977050fe61331f9a3411c091245`.
The generated commit message retains the actual `6ab3b48f` runtime predecessor
and useful changelog. The final configuration and workspace runtime locked
identities, including narHash, match; their recursively resolved runtime inputs
also match. The workspace's exact nested URL and configuration's channel-managed
input retain their established original-reference forms.

I checked all four worktree heads, cleanliness, bases and complete series against
[deployment-final-inventory.json](deployment-final-inventory.json):

| Repository | Base | Final head |
| --- | --- | --- |
| codex-web | `c064ce09cfcea8d8af6bf676635a53cd823f772c` | `641907fb3afa2977050fe61331f9a3411c091245` |
| dev-workspace | `ea3f9d36397e8c2c846bd456e51385d73a3a358a` | `1395387ff02729256ba52cc7c9ded74397cbe1a6` |
| workspace | `f95413431bcff60fd087399a54aeba8a475837b6` | `0383f0bc057e81b6a96acef6ede63ab95e7522bc` |
| vpsfree-cz-configuration | `e646cf61dff7557c16ee2534ae5b809efa6a2d94` | `316a071cd6cc3dd090661edac5a0e8d0d927d2c5` |

Whole-series conclusion: the retained runtime series has the optional-question
commit `1afca4ab` followed by the separate archive repair `1395387f`; codex-web
has one feature commit, and each downstream has one final pin commit. No obsolete
implementation iteration, fixup series, or repeated/superseded pin stream remains
in these final feature ranges. The three incoming baseline commits are already
upstream history and update distinct channel/input groups; they are not redundant
feature pin iterations. No initiative activation consumed an intermediate
configuration, so no deployed intermediate configuration boundary needs retaining.

**No migrations.** The configuration refresh adds no database, journal, sidecar,
session-format or protocol migration. The prior full-deliverable migration
conclusion remains valid; there is no new migration lineage or intermediate
schema to preserve.

I inspected the actual incoming diffs from `7ffa98a5` through `e646cf61`:

| Incoming commit | Lock changes |
| --- | --- |
| `fdab039b74dbfff8268a3ed59568ad181b560a13` | `nixpkgsProduction`, `nixpkgsStable`, `nixpkgsStaging`: `8ce73368` to `f3a73bcf5d1c5b75a66cf35a48957e30d41d647a` |
| `5bbccc7c5b47bae0c4dfbd460180df578916fd07` | `nixpkgsUnstable`: `fe132422` to `09063bd1f2b36fd9fd793c36dfade7bd40a93dfc` |
| `e646cf61dff7557c16ee2534ae5b809efa6a2d94` | `vpsadminosOsStaging`, `vpsadminosStaging`: `87fc13aa` to `f4bac6b493a507fb80b0935e703ac6568095b236` |

Only those six nodes' locked identities change. Node sets, original references
and input relationships are preserved. The old-to-new feature-head difference
is exactly this baseline delta.

Aitherdev's `cluster/cz.vpsfree/machines/aitherdev/module.nix:7` selects
`nixos-stable`, home-manager, llm-agents and dev-workspace.
`flake.nix:122` maps `nixos-stable` to `nixpkgsStable`; home-manager also follows
that input. Therefore the baseline refresh affects the host package/module
evaluation and potentially service activation. Its unstable and vpsAdminOS
staging channels are not selected by aitherdev. This rollout does not require
coordinated deployment of other nodes.

The runtime, workspace, extension `767dfd58`, codex-web and llm-agents selections
remain unchanged. Existing runtime/package/CI evidence is reusable only for its
unchanged source and input identities. It does not prove the new aitherdev system
derivation or its activation. Even a tree-equivalent configuration refresh would
require exact-commit preparation because confctl embeds `self.rev`; here the
system's nixpkgs input also changes. The host Codex assembly uses host packages,
so final artifact and live checks must still confirm Codex `0.163.0`.

The remaining verification boundary is:

- Build/copy and inspect the system from exact configuration `316a071c` in its
  Nix environment, with current baseline and ownership checks. Prepare matching
  system/profile snapshots with fresh checksummed evidence and applicable
  approval records.
- Perform dry activation through the supported adapter under initiative
  reservation `90fb300f-69f5-41e4-a04a-7762125cd713`, immediately before the
  no-reboot system switch. Keep successful system activation before profile
  selection.
- Verify system/profile identities, portal and question assets, Codex `0.163.0`,
  and existing conversation/terminal continuity. Preserve reservation ownership
  through acceptance.
- Preserve failed attempts and artifacts. Reconcile uncertain effects; application
  recovery remains forward-only through the supported path.

The failed preparation log reports that the configuration source lacked its
current remote baseline, before activation. Recorded recovery evidence reports
both authorized archives exiting zero, cleared journals/sidecars and synced
tracking. I also compared the retained live-worktree before/after snapshots;
they are identical. These are recovery results, not verification of the refreshed
system.

Independent read-only checks included `git diff --check` across the inventory,
history/range-diff and stable patch-ID comparison, and semantic lock inspection.
The packet separately reports the matching deployment-contract check and normal
Nix-shell hooks passing. No long tests, builds, recovery, deployment, commits,
application-source changes or nested agents were performed by this reviewer.
Only this report was written. Supported operational documentation already covers
the exact-source preparation, ownership, ordering and recovery requirements.
No finding prevents the remaining verification from proceeding; deployment
success and default-branch readiness are not established by this review.
