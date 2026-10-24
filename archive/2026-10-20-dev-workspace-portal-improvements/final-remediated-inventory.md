# Final remediated branch inventory

Independent whole-branch report: [final-review.md](final-review.md). Original
[review packet](review-packet.md) and [inventory](final-inventory.md) retained.
Requested corrections and direct acceptance: [review-remediation.md](review-remediation.md).
All final heads are committed, SSH-published and clean. No default integration,
release or deployment is established by these source publications.

## codex-web

Base `57972192e30fe52ab33b867c8fe4d171f59a7fd5`; head `852e8c51091512bc79ca6c921ef1f5ccc46a9535`.

```text
529524829526f41c628bd54d729241c52395c6b2 conversation: present transcripts after attachment decoration
7fb4ab212ba233b94370eeea131762b729ac2505 conversation: distinguish team traffic and quiet history fallback
852e8c51091512bc79ca6c921ef1f5ccc46a9535 conversation: reconcile inline submission failure notices
```

[Complete series](codex-web-remediated-series.txt), [final diff](codex-web-remediated-final.diff).

```text
 codex/client.go                             |  49 ++--
 conversation/assets/conversation.css        |  11 +
 conversation/assets/conversation.js         | 174 ++++++++++++---
 conversation/handler.go                     |  11 +-
 conversation/presentation_test.go           | 172 ++++++++++++++
 docs/reference.md                           |  51 ++++-
 test/conversation_browser_contract_test.cjs | 333 ++++++++++++++++++++++++++++
 7 files changed, 749 insertions(+), 52 deletions(-)
```

## dev-workspace

Base `52dcd471186ef874c5c93f4133744195d4815454`; head `db25364999aa4bf12b67506662a08e9e464bee33`.

```text
d58b76e2450e51660eb8b024519c800915f86fc0 deps: update shared conversation presentation helpers
2d68be7d961b5970c11626276ac78260ef0a4f10 team: project full-team names from actual implementer counts
347fee120fbf244abb5cf089bcf1e1d8f1712f2d portal: add authorized file downloads and source copy actions
05657be40a96a20e8b0fc44df5bfb23e7ff79696 portal: keep large artifact catalogs compact and stable
6d0789fe6e720be4f788b176bddce5f6f1e37291 portal: publish session membership before optional enrichment
cb3ef38fb9e7c2f1b8b78087b8eae096763bb0e8 portal: retain member settings through sequential additions
b8cded6210bc6f3f3e40d12b5c2fd2abb093afdc portal: present team messages and decorated Markdown
db25364999aa4bf12b67506662a08e9e464bee33 portal: show delivery recovery beside the composer
```

[Complete series](dev-workspace-remediated-series.txt), [final diff](dev-workspace-remediated-final.diff).

```text
 docs/workspace-portal.md                           |  66 ++++++--
 flake.lock                                         |   8 +-
 flake.nix                                          |   2 +-
 nix/workspace-portal.nix                           |   2 +-
 portal/go.mod                                      |   2 +-
 portal/go.sum                                      |   2 +
 portal/internal/repository/source.go               |  70 +++++++-
 portal/internal/teamruntime/runtime.go             |  13 ++
 portal/internal/teamruntime/runtime_test.go        |  65 +++++++-
 portal/internal/web/artifact_tree.go               |  40 +++++
 portal/internal/web/artifact_tree_test.go          |  22 +++
 portal/internal/web/browser_contract_test.cjs      |   1 +
 .../web/citation_presentation_contract_test.cjs    |  26 +++
 portal/internal/web/citations_test.go              |  35 ++++
 .../internal/web/index_cluster_contract_test.cjs   |  15 ++
 portal/internal/web/index_loading_test.go          |  40 +++++
 portal/internal/web/operation_state.go             |   6 +-
 .../web/portal_improvements_browser_test.cjs       | 178 +++++++++++++++++++++
 portal/internal/web/question_browser_test.go       |  45 +++++-
 portal/internal/web/server.go                      | 105 +++++++++---
 portal/internal/web/server_test.go                 |  20 +++
 portal/internal/web/source_files.go                |  45 +++++-
 portal/internal/web/source_files_browser_test.cjs  |   9 +-
 portal/internal/web/source_files_test.go           |  98 +++++++++++-
 portal/internal/web/static/app.js                  | 159 +++++++++++++-----
 portal/internal/web/static/source-file.css         |   2 +
 portal/internal/web/static/source-file.js          |  11 ++
 portal/internal/web/static/style.css               |  26 ++-
 portal/internal/web/submission_loss_test.go        |  96 +++++++++++
 .../web/submission_notice_contract_test.cjs        | 100 ++++++++++++
 .../web/submission_notice_contract_test.go         |  16 ++
 portal/internal/web/team_add_contract_test.cjs     |  36 +++++
 portal/internal/web/team_add_contract_test.go      |  16 ++
 portal/internal/web/templates/details.html         |   6 +-
 portal/internal/web/templates/index.html           |   4 +-
 portal/internal/web/templates/session.html         |  12 +-
 portal/internal/web/templates/source-file.html     |  12 +-
 portal/internal/web/workspace_source_files_test.go |  23 +++
 38 files changed, 1315 insertions(+), 119 deletions(-)
```

## workspace

Base `0ea5682410a38fe19627bc731e13894c1e51db57`; head `3de65bbd0e90f0c3b19e0d64ed925158155647a6`.

```text
52178b3172a7c837d1b3f70afbf773455ac0a6a9 instructions: keep core rules within the discovery limit
66a90bfa1efb272466c9b1cb6d72989c6d57356f teams: default to Full team with implementer-count variants
3de65bbd0e90f0c3b19e0d64ed925158155647a6 inputs: select citation-preserving portal improvements
```

[Complete series](workspace-remediated-series.txt), [final diff](workspace-remediated-final.diff).

```text
 AGENTS.md                       | 55 ++++++++++++++++---------------------
 config/agent-teams.nix          | 61 +++++++++++++++++++++++++++--------------
 docs/agent-teams.md             | 39 ++++++++++++++++++++------
 flake.lock                      | 16 +++++------
 flake.nix                       | 31 +++++++++++++++++----
 test/agent_instructions_test.rb |  8 +++++-
 6 files changed, 135 insertions(+), 75 deletions(-)
```

## History, pins and migration lineage

A has three focused commits: hook/type (with identity-order tests), transcript/
team/HTML/history, delivery recovery. B has eight: one final A pin, team names,
source actions, artifact UI, early index, Add-member retention, presentation/
history, delivery recovery. C has unchanged instruction-size and team source
commits plus one amended final runtime pin. No obsolete iterations/fixups or
intermediate pin churn remain. Tests/CSS/docs follow their owning behavior.

Independent reviewer certified whole reviewed ranges and no migrations across
all three. F1 pure splits reproduce both reviewed trees exactly; lead independently
ran empty diffs. Subsequent changes are bounded F2 notice reconciliation, requested
mechanical pins and diagnosed fixture-only corrections. Direct narrow acceptance
follows mandatory-change-review steps9–10; no new public contract/design requires
rerunning unaffected lanes. No migration/state/protocol source was added later.

One logical A update in B selects852e8c5 across Go/Nix/vendor. One runtime update
in C selectsdb25364 and transitive A852e8c5. Lead independently compared JSON lock
graphs: B changes only codex-web; C only runtime/shared nodes, preserving extension
767dfd5, siblings/follows/root and Codex0.163.0. Integrated citation baselines
5797219 and52dcd47/af4c853, workspace0ea56824 remain ancestors. No feature pin
is retained merely because it was published or used during preparation.

Prior441ebee/2dc2dc7 and reviewed2ea01d5/3f0eae0/d16483d8 retain explicit provenance
in checkpoint/review records. Preparation consumed the earlier heads; external
release/deployment is unestablished. No migrations exist, hence no migration
versions require deployment/external-use guards or transitional lineage retention.

Feature integration remains explicitly unapproved. Before an approved merge,
recheck final refs/baselines, complete-series scope and exact verification inputs.
