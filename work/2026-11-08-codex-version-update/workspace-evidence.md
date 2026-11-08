# Workspace composition evidence

S source and quick checks are complete at SSH-published exact head
`3f813d5862c1a29d8dd34bd78863b5dfba38767a`, selecting accepted R
`71654e18c5558c6b8b5cb3f33bfedced7fab727d`. Single final joint deployment
checker passes against clean configuration head
`ec1ccce401f81d604cd059d159ca6033df07f2a0`. Feature tree is clean. Ready for
lead acceptance and combined final review; no composed build, long check,
activation, merge or deployment was performed. Lead owns acceptance, tracking,
review and deployment. No source deviation or unresolved S blocker.

## Source, publication and complete history

- Repository: `git@github.com:aither64/vpsfree-cz-workspace.git`, target `master`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-08-codex-version-update/workspace`.
- Branch: `2026-11-08-codex-version-update`.
- Registered initial tracking base: `527362b66eb903819ccb13ebb1e62495887195ca`.
- Current shared-master source parent: `8aae9bd4af090260a92ec0296472fadce13c6cd7`.
- Final S: `3f813d5862c1a29d8dd34bd78863b5dfba38767a`.
- Fresh fetched and remotely verified master: `0c112efeb3e88b62ca0d48feb532bab93303735c`.

Rebased onto current shared master before editing and rechecked before each
push; no conflicts. The final brief-owned series is one commit over `8aae9bd4`:
`3f813d586 workspace: select Codex 0.167.0 runtime`. Its final diff contains
only `flake.nix` and generated `flake.lock`, 19 insertions and 19 deletions.

Complete registered-base-to-head series additionally inherits coordination-only
commit `8aae9bd4`; complete remote-default-to-head series also includes initial
tracking `527362b66`. These existing ancestors are coordination context, not S
source changes. Their content was not inspected as peer records. The reviewer
can inspect all three commits from remote base `0c112efeb` while evaluating the
S source diff over parent `8aae9bd4`.

Final force-with-lease push explicitly required prior remote S `64fbbad93`;
`git ls-remote` then verified exact final S and remote master above. Final
`capture-comparison` saved `0c112efeb` → `3f813d586`. No declared workspace CI
workflows exist, and no CI wait was introduced. The workspace declares no hook
framework or active hooks; sample hooks were preserved and none bypassed.

## Final graph and quick checks

Scoped generator: `nix flake update vpsfree-dev-workspace/dev-workspace`.
Semantic inspection passes: 35 nodes, no added/removed node, every edge/follows
path unchanged. Exactly five runtime-subtree identities changed versus source
parent: runtime, codex-web, llm-agents, llm-agents/flake-parts and
llm-agents/nixpkgs. Complete before/after graphs and tested final head are in
[workspace-semantic-graph.json](workspace-semantic-graph.json).

The entire extension node remains unchanged:
`f8da821e3c76e26e73aa9d89a712eab0e0faa319`,
`sha256-U5y/TEny6nsyXWNlCMktmxTZhpVO0QY4kOo/qgwsapM=`.
All six sibling full closures remain unchanged: devcluster-vpsadmin,
devcluster-vpsadminWebui, devcluster-vpsadminos, devcluster-vpsf-status,
kb-runtime and nixpkgs. Root nixpkgs still follows extension nixpkgs. No new
top-level runtime input, lock deduplication or extension-lock edit.

The final single joint checker passed in repository-selected Ruby:

```sh
nix shell --inputs-from . nixpkgs#ruby --command ruby \
  bin/check-dev-workspace-deployment \
  --workspace-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-08-codex-version-update/workspace \
  --configuration-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-08-codex-version-update/vpsfree-cz-configuration
```

Output: `deployment contract passed for vpsfree-cz.workspace.aitherdev.int.vpsfree.cz at 71654e18c5558c6b8b5cb3f33bfedced7fab727d`.
Command exited 0. Implementer2 received the result for C without duplication.
This proves site identity and runtime revision equality. Separate complete
locked-object comparisons also pass for final C/S runtime and llm-agents,
including content hashes; C head was verified exact and clean. Final R's flake
codex-web revision matches its Go pseudo-version and supplied checksum.
`git diff --check` passes. No new tests are useful for this mechanical pin
composition; actual-binary and package checks remain in combined W/R/long lanes.

## Exact evaluated source/output identities

Committed-source `nix eval` succeeded without building; receipt:
[workspace-final-eval.json](workspace-final-eval.json). It evaluates the exact
final Git revision, rather than the earlier dirty/path source.

- Workspace source: `/nix/store/d91g2fc583yi79bqxwwg5i0z5a6sp057-source`.
- Workspace derivation: `/nix/store/ashz8c64xnkvyd3g609ay7jm12wsnr39-dev-workspace-0.2.0.drv`.
- Workspace output: `/nix/store/fyfi9hhgyr2887w5clch7c6djl2005sp-dev-workspace-0.2.0`.
- R source: `/nix/store/hl0gh74z1yyy30xw6wac2l319vqcawkb-source`, `71654e18c5558c6b8b5cb3f33bfedced7fab727d`, `sha256-f5FD3Si1aOYE+qIeyv0gqw56E9IetR4NWDBmpDQa8MU=`.
- llm-agents source: `/nix/store/ib6qj3vlq8fjja2bm5dl2b2sk3nyv8ww-source`, `d960982d3b05c294f3cf98cab3e23798548a0ced`, `sha256-h0CHJMm9bCObkUg2VU1B/QCFWC28eg7YMylnlrTKG2U=`.
- codex-web source: `/nix/store/2y2a7df1yv9aadbb10ykwibx465wb17g-source`, `f78eae3415d20b98503f11e9fe251e3111bfe4da`, `sha256-1QVZzEjeu/cjlcTlGTQyMGIuuPqKZ1YsXtOJV59ZROM=`.
- Extension source: `/nix/store/y01y2bs4mar8zq9s72npz3lrmlsjvasa-source`.
- Upstream Codex: `0.167.0`, `/nix/store/22139ip2k5dfc272a1nv0br2ms0nymbv-codex-0.167.0`, derivation `/nix/store/9rxjqb3nzbf4b9s0bj3h4yl8igm105is-codex-0.167.0.drv`.

Complete selected input graph is the final committed `flake.lock`, duplicated
as exact before/after objects in the graph receipt. R/C retain their independent
native, assembled-package, module/vendor and provider-profile evidence. S does
not infer actual running daemon identity or deployment from evaluated outputs.

## Superseded preparation and consolidation provenance

Initial S range `8aae9bd4` → `64fbbad93ee5fc7521f7e5c52addb72ab1384303`
selected R `c92d539dc2df3236c1928d6fa625ccb08b418c34`. It was published and
quick-checked with C `637103e4efecf5fbd8ec85a7a040fe3baf98b5a1`, never deployed.
Source inspection found R's `nix/workspace-portal.nix:528` `postFixup` still
expected native 0.165.0. Lead assigned R's correction to the selected package's
exact version. R owner published `71654e18`; no native/module/vendor dependency
changed. This was resolved before any composed build or final review.

Lead directed S's owning input commit to be amended, giving final range
`8aae9bd4` → `3f813d586`. Only the runtime URL/locked identity differs from the
first S; complete runtime dependency graph is unchanged. Range-diff is retained
in [workspace-successor-range-diff.txt](workspace-successor-range-diff.txt).
Historical evaluated output `/nix/store/0aj4fk5ffpkf9qnmz7rqz7bldilkplh0-dev-workspace-0.2.0`
was provisional, never built/deployed by S, and is superseded. Original source/
output and graph receipts are retained as `workspace-initial-final-eval.json`
and `workspace-initial-semantic-graph.json`; the earlier dirty path evaluation
is not final build evidence.

One logical runtime-selection stream remains one final source commit. No
superseded input commit remains in the final source series. No migration,
schema, protocol, API or persisted-data format change is added by S; no S
migration was merged, released, deployed or externally consumed. No useful
reusable documentation change is indicated for this pure pin composition.

## Next dependency

Lead acceptance and combined independent final review precede composed output
builds and applicable composition/native checks. Implementer1 received exact
final S for post-review managed-naming harness binding. Final build and activation
must use the current output above. System activation precedes dependent selected
profile activation; integration requires separate explicit user direction.
No claims, activation, default integration or lifecycle actions were performed.
The session remains open and active.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-08-codex-version-update/
