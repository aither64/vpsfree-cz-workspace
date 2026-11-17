# D3 final independent review

Outcome: **pass, no findings** in the affected general,
architecture/repetition, scope/proportionality and risk/compatibility lanes.
The publication-only Linux instructions are consistent with the accepted scope
and preserve the required review, validation, approval and recovery boundaries.

## Identity, scope and exact ranges

Retained reviewer `reviewer0`, thread
`01a1ea07-46de-7650-b81d-f9ac09c416df`, saved `gpt-6.1-sol` / `xhigh` /
`read_only`; verified against the live same-session roster. Session identity
matches `2026-11-17-stable-kernel-update` and the trusted workspace binding;
both environment identity variables were absent. No model/effort overrides,
fallback reviewer, nested agents, source edits, builds, CI actions, ref changes
or lifecycle actions.

High risk applies to the cross-project delivery/completion instructions, not a
new kernel behavior change. Applied mandatory-change-review and all four selected
lane references, with the applicable workspace/repository procedures. Original
[review.md](review.md) remains the Linux source-review authority. This affected
review does not repeat the unchanged 50-patch audit.

Reviewed complete committed histories and final diffs:

- OS: `42baba6117bebcde3d04555a71377381df197925` to
  `f33f5fd10b53232b5670862f832f4ec5ea835e84`. Exactly two logical commits:
  `2352449568afa3b2f5bd500dba3fbed1c1163e0b` (process) and
  `f33f5fd10b53232b5670862f832f4ec5ea835e84` (single stable catalog update).
- Workspace: `066f7b2c431aef53b206e196ce36750bf2649593` to
  `9610ea74a70d4b9b9d0f2d9296ea4908c0d4725b`. Exactly one policy commit,
  changing AGENTS, the Git procedure and the session procedure.
- Linux source remains `3bba27296b6f4f4a2b1568d65cea6037368f229b` on upstream
  `b869a5313cbfe7102873d3de318ddb68675146d0`; D3 changes no Linux source.

The latest scope explicitly calls for Linux version-branch publication, no
automatic downstream tags and uniform instructions. The actual incremental
change is six instruction files: OS +45/-14 and workspace +31/-7. It introduces
no runtime code, metadata/schema, ledger, helper or policy framework. The narrow
implementation and committed/check milestones are proportional to this added
scope. Elapsed waiting for the earlier kernel CI is not D3 implementation time.

## Instruction and compatibility assessment

- The OS runbook owns version naming and publication semantics. AGENTS and the
  skill are concise discovery/contract pointers. The workspace links that
  runbook rather than maintaining a second replay/publication implementation.
- Final version-branch publication follows existing patch-policy review and
  exact-head product validation. Optional dated candidate publication supplies
  the archive needed to register/build/test the candidate, so the ordering has
  no circular dependency and does not waive the final gate.
- Same-head existing branches are accepted only for the exact desired SHA.
  Different-head branches are preserved and investigated; no force-update or
  repoint-to-finish is authorized. Later same-upstream revisions may use the
  existing suffix convention after ref checks. Generic series aliases remain
  untouched without direction.
- The prohibition concerns automatic downstream tags; authoritative upstream
  tag discovery and verification remain required. The OS continues to pin the
  full immutable commit and raw archive-byte hash, independently of a version
  branch's name.
- Publication proof records canonical remote, full branch ref, fresh exact
  remote-head equality, tested Linux SHA and consuming OS revision/hash.
  [The publication receipt](linux-port.md#version-branch-publication-l-publish)
  binds `git@github.com:vpsfreecz/linux.git`,
  `refs/heads/vpsadminos-6.12.118` and the unchanged full source SHA; dated and
  recovery refs are retained, and default/series refs were unchanged.
- The workspace exception is expressly limited to Linux source delivery.
  Cross-references qualify the two universal default-merge completion
  statements. Other repositories still require approved integration of their
  exact final heads into their remote defaults, with no unfinished work.
  General final-review/history requirements continue to apply to Linux.
- The exception does not authorize closing the session or modifying the
  runtime. Its explicit fallback leaves lifecycle state unchanged when an
  installed runtime or retained recovery contract cannot represent publication.
  This is consistent with the lifecycle procedure's retained merge/worker
  proofs and prevents metadata, registration, helper or runtime bypasses.
  No machine-release or retained recovery requirement is changed.

Workspace-master integration still needs its separate explicit approval.
Recorded OS-staging approval and Linux publication approval do not provide that
approval. The canonical staging runbook link will be served by the OS change;
the prepared instruction diff is not evidence that it is already on staging.

## History, migration and evidence continuity

Independently reproduced native OS range-diff for the clean target refresh:

`a7d71a54a15496976cb0fccebb8a1b589f24f5e2..ba7e99b5e3d435826bd387e64f1c1a6ec173169c`
to
`42baba6117bebcde3d04555a71377381df197925..ba6837de511ef9364fa4126e24c91de0251f33ad`:
both logical commits are `=`. The baseline delta changes only the two exporter
dependency files. Compared that prepared range with the final D3 range: only
the three assigned OS instruction files change in the process owner; the catalog
commit remains `=`. Independently checked direct file boundaries and byte equality
of the catalog, flake lock and ZFS patch against the tested head.

Independently reproduced workspace range-diff from the original one-commit
`68eb91f2924b36735bddb791666c7bf38fdf831c` series to the final
`066f7b2c..9610ea74` range: `=`. No tracking files entered the policy commit.
Both final worktrees were clean at the exact assigned heads.

No obsolete branch approach, fixup/repair residue, abandoned README iteration or
transitional path remains in either final history. D3 is folded into the OS
process owner; the catalog stays separately reviewable. **No migrations** in
either range, and no merged/released/deployed/externally consumed transitional
schema requiring retention. No repeated dependency/input/generated update stream
was introduced or left redundant: one final kernel pin remains, and D3 changes
no Linux/ZFS/flake pin. Further consolidation is unnecessary.

Original Advisory A1 is resolved by the retained owned-shell
`export GIT_NO_LAZY_FETCH=1`; D3 preserves that correction and the remaining
replay/accounting/recovery contract.

## Documentation and verification conclusion

Documentation placement, reachability and fidelity pass. The existing README,
MkDocs, AGENTS and skill entry points still lead to the maintained OS process;
workspace Git owns the narrow completion exception and its two callers link it.
Changed local destinations/anchors and shell-block syntax were independently
checked. Source publication, integration and lifecycle are distinguished without
discarding the old backup, validation or rollback constraints. Execution-specific
SHAs, approvals and results remain in session receipts. No fixed patch inventory
or run-specific result was added to reusable project instructions.

Owner evidence reports passing OS skill/docs/hooks and workspace declared Nix
instruction checks (10 tests, 220 assertions). Independently checked diff
whitespace, changed paths, branch-history equivalence and the 16,381-byte
workspace AGENTS discovery limit. No new product tests are needed solely for
these instruction changes.

The completed CI receipt binds the earlier OS head
`ba7e99b5e3d435826bd387e64f1c1a6ec173169c` to 110 expected successful tests,
including the named NFS/boot/module/ZFS cases. Original independent source
review and that verification remain reusable within the proven unchanged
Linux/ZFS derivation, source/config/input and test-source scope. Recorded stable
Linux `3slqrmfmm3jqz8x99rcvi2qr10y3w1dq`, external Linux `61h04f41dsq8sgxj87kiyx5s2hr97chm`
and built-in ZFS `x4468m97719ik8lpjfjmck2gki0znrf8` derivations are unchanged.
The new composed system derivation
`/nix/store/6a560v0f442rchkda1024cvsjnliswdn-vpsadminos-system-vpsadminos-26.05.git.f33f5fd.drv`
is not claimed to be the earlier tested exact OS closure. The unrelated exporter
baseline and source-revision difference remain explicit in the receipt.

No new compatibility or security gap was identified in D3. This pass does not
establish production deployment, mixed-version rollback, livepatch qualification
or lifecycle eligibility, and grants no integration authority.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-17-stable-kernel-update/>
