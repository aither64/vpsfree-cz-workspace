# Final branch inventory

### codex-web

Base `57972192e30fe52ab33b867c8fe4d171f59a7fd5`; head `2ea01d5fc5672da25cca8d5b45ce6aa7f7c52b70`. Clean verified worktree.

```text
bf47be996bf39ad06ad15f99368e5b71aea4a3c5 conversation: present transcripts after attachment decoration
2ea01d5fc5672da25cca8d5b45ce6aa7f7c52b70 conversation: distinguish team traffic and quiet history fallback
```

[Complete series](codex-web-series.txt), [final diff](codex-web-final.diff).

```text
 codex/client.go                             |  49 ++++---
 conversation/assets/conversation.css        |  11 ++
 conversation/assets/conversation.js         | 118 ++++++++++++----
 conversation/handler.go                     |  11 +-
 conversation/presentation_test.go           | 172 +++++++++++++++++++++++
 docs/reference.md                           |  46 ++++++-
 test/conversation_browser_contract_test.cjs | 207 ++++++++++++++++++++++++++++
 7 files changed, 568 insertions(+), 46 deletions(-)
```

### dev-workspace

Base `52dcd471186ef874c5c93f4133744195d4815454`; head `3f0eae0071b918c742507bff9f1304d95d698bb7`. Clean verified worktree.

```text
ca56a207044d3f47e6b162284eca525d00bd3757 deps: update shared conversation presentation helpers
df3830a1c14318f25236f0a6201fc838606439a0 team: project full-team names from actual implementer counts
a846b4f4f7087eae441e9d76e7c260b063cb4085 portal: add authorized file downloads and source copy actions
b0ff0625b7434780c8df9a7d39bc8bdf6b6c94d4 portal: keep large artifact catalogs compact and stable
f94b7ce2b77ffac7fdf2d50d211a37a5a6da77fe portal: publish session membership before optional enrichment
df50d909996df8ecaf5b8946daa39e9931e14804 portal: retain member settings through sequential additions
3f0eae0071b918c742507bff9f1304d95d698bb7 portal: present team messages and preserve delivery recovery inline
```

[Complete series](dev-workspace-series.txt), [final diff](dev-workspace-final.diff).

```text
 docs/workspace-portal.md                           |  65 +++++++--
 flake.lock                                         |   8 +-
 flake.nix                                          |   2 +-
 nix/workspace-portal.nix                           |   2 +-
 portal/go.mod                                      |   2 +-
 portal/go.sum                                      |   2 +
 portal/internal/repository/source.go               |  70 ++++++++-
 portal/internal/teamruntime/runtime.go             |  13 ++
 portal/internal/teamruntime/runtime_test.go        |  65 ++++++++-
 portal/internal/web/artifact_tree.go               |  40 ++++++
 portal/internal/web/artifact_tree_test.go          |  22 +++
 portal/internal/web/browser_contract_test.cjs      |   1 +
 .../web/citation_presentation_contract_test.cjs    |  26 ++++
 portal/internal/web/citations_test.go              |  35 +++++
 .../internal/web/index_cluster_contract_test.cjs   |  15 ++
 portal/internal/web/index_loading_test.go          |  40 ++++++
 portal/internal/web/operation_state.go             |   6 +-
 .../web/portal_improvements_browser_test.cjs       | 157 +++++++++++++++++++++
 portal/internal/web/question_browser_test.go       |  35 ++++-
 portal/internal/web/server.go                      | 105 ++++++++++----
 portal/internal/web/server_test.go                 |  20 +++
 portal/internal/web/source_files.go                |  45 +++++-
 portal/internal/web/source_files_browser_test.cjs  |   9 +-
 portal/internal/web/source_files_test.go           |  98 ++++++++++++-
 portal/internal/web/static/app.js                  | 140 +++++++++++++-----
 portal/internal/web/static/source-file.css         |   2 +
 portal/internal/web/static/source-file.js          |  11 ++
 portal/internal/web/static/style.css               |  26 +++-
 portal/internal/web/submission_loss_test.go        |  96 +++++++++++++
 portal/internal/web/team_add_contract_test.cjs     |  36 +++++
 portal/internal/web/team_add_contract_test.go      |  16 +++
 portal/internal/web/templates/details.html         |   6 +-
 portal/internal/web/templates/index.html           |   4 +-
 portal/internal/web/templates/session.html         |  12 +-
 portal/internal/web/templates/source-file.html     |  12 +-
 portal/internal/web/workspace_source_files_test.go |  23 +++
 36 files changed, 1149 insertions(+), 118 deletions(-)
```

### workspace

Base `0ea5682410a38fe19627bc731e13894c1e51db57`; head `d16483d8cb7041fa786312f05af7e118c66f6649`. Clean verified worktree.

```text
52178b3172a7c837d1b3f70afbf773455ac0a6a9 instructions: keep core rules within the discovery limit
66a90bfa1efb272466c9b1cb6d72989c6d57356f teams: default to Full team with implementer-count variants
d16483d8cb7041fa786312f05af7e118c66f6649 inputs: select citation-preserving portal improvements
```

[Complete series](workspace-series.txt), [final diff](workspace-final.diff).

```text
 AGENTS.md                       | 55 ++++++++++++++++---------------------
 config/agent-teams.nix          | 61 +++++++++++++++++++++++++++--------------
 docs/agent-teams.md             | 39 ++++++++++++++++++++------
 flake.lock                      | 16 +++++------
 flake.nix                       | 31 +++++++++++++++++----
 test/agent_instructions_test.rb |  8 +++++-
 6 files changed, 135 insertions(+), 75 deletions(-)
```

## History and migration provenance

No database, manifest, roster, queue, submission-ledger or native protocol schema
migrations. Integrated citation5797219 and runtime af4c853/52dcd47 remain baseline
ancestors, as does workspace citation selection0ea56824. Do not rewrite these
integrated commits. A/B semantic rebase conflict decisions and old/new ranges
are in design.md and their captured range-diffs. They are not assumed equivalent.
C's two source commits are patch-identical after rebase; final pin is fresh.

No superseded feature approaches or fixups remain. B has one final codex-web
update; C has one final nested runtime update. Earlier source heads were published
and consumed by this initiative preparation; external release/deployment was not
established. Exact prior heads retained in session artifacts. No initiative
head was merged or deployed by this session. Reviewer must independently assess
complete histories, update streams and migration lineage.
