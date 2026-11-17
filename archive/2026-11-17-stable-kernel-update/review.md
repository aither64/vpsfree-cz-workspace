# Final independent review

Outcome: **pass with one Advisory finding**. No Blocking or Important finding.
Source preservation, the process and the catalog are suitable to proceed to the
planned product checks. Compilation, VM qualification and deployment are not
established by this review.

## Finding

**A1 — Advisory, general/documentation lane: carry the partial-clone environment
setting through replay.** In OS commit
`435d83468d7a3089eeb45f171d0ab244748f43b4`,
`docs/os/kernel-updates.md:48` prefixes only the preflight example with
`GIT_NO_LAZY_FETCH=1`. The replay example at line 77 does not set it, while the
continuation guidance at line 95 says to keep it enabled. A shell assignment
before `git cat-file` does not persist for subsequent commands. A maintainer
following these examples in a partial clone can pass the commit-object check
then trigger an implicit large fetch when replay needs an absent blob, contrary
to the documented deliberate-acquisition approach. Explicitly export it for
partial-clone inspection/replay/continuation, or carry it on those commands.
This is a narrow documentation correction; no new helper or framework is needed.
K actually ran the replay with the variable set, so this does not undermine the
completed port and does not block product checks.

## Review identity and scope

Reviewer: retained `reviewer0`, thread
`01a1ea07-46de-7650-b81d-f9ac09c416df`, `gpt-6.1-sol` / `xhigh` / `read_only`.
Verified the live same-session roster and `dev-session current` against the
trusted binding. Both session environment variables were absent, without an
environment conflict. No setting overrides, nested agents or source edits.

Risk: high, because this selects a host kernel carrying container-isolation and
NFS teardown behavior. Read mandatory-change-review and its complete general,
architecture/repetition, scope/proportionality and risk/compatibility lanes, plus
applicable workspace/repository guidance and packet-linked evidence.

Reviewed exact committed ranges:

- OS: `a7d71a54a15496976cb0fccebb8a1b589f24f5e2` to
  `5a59f3059ca6ada368deeeeca6dba5034468be93`, comprising process commit
  `435d83468d7a3089eeb45f171d0ab244748f43b4` and catalog commit
  `5a59f3059ca6ada368deeeeca6dba5034468be93`.
- Old Linux downstream: `d3417611a3b40b7f04a29e558cebac2bf69889d7` to
  `764acbb0ca8c4b60ee5b98f89406b152e992b1d6`.
- New Linux downstream: `b869a5313cbfe7102873d3de318ddb68675146d0` to
  `3bba27296b6f4f4a2b1568d65cea6037368f229b`, all 50 commits in the packet.

Compared the requested dynamic skill/process, complete patch carry, .118 stable
selection and demonstrated process tuning against the final diff and milestones.
The OS change is seven files, +324/-1, with no scripts, registry or new framework.
The Linux +3440/-435 over 113 diff paths is the existing stack transplanted,
not equivalent newly invented scope. Session creation around 15:01 UTC, the
process/replay milestones and final OS commit at 15:41 UTC show concrete
deliverables within roughly 40 elapsed minutes; parallel member time is not
summed. No disproportionate subsystem expansion found. Unrelated baseline stack
defects were not re-audited or made new acceptance gates.

## Independent preservation and package assessment

- Regenerated native range-diff: every ordered old/new pair is `=`. Compared
  all 50 pairs with the evidence table and read raw commit objects: complete
  messages and exact author identity/date match, both ranges are linear and
  no fixup/WIP subject remains. The dated old-head backup is exact. Verified
  ancestry, target tag object/peeled commit, Makefile .117/.118 identities and
  the 680-commit authoritative upstream transition.
- Independently checked all 86,724 paths in the union of old base, old head,
  new upstream and final head. Every one-sided change has exactly the expected
  mode/type/blob or deletion. The 107 downstream-only path entries include the
  source deletion of the printk header rename; this corresponds to the owner's
  106 surviving nonintersecting downstream paths.
- For all seven overlapping files, native `git merge-file --stdout` of the
  old downstream/base/new upstream blobs produced a clean result whose Git blob
  hash exactly equals the final file. Used memory-backed descriptors, without
  writing Git objects or stored clone configuration. Final tree is
  `944e5a57917938df529d6eebb3e30eba40e4afef`, matching the packet's merge-tree
  receipt. This checks source composition beyond counts or patch IDs.
- Directly inspected upstream and downstream diffs and surrounding contracts
  for `fs/nfsd/nfsctl.c`, both memcontrol files, `mm/vmscan.c`, `mm/shmem.c`,
  `mm/swapfile.c` and `include/linux/sunrpc/clnt.h`. User-namespace mount flags,
  rstat/root and reclaim-iterator protections, kmem slab gate, memcg tmpfs
  sizing/ID rendering, swaps reference ownership and RPC cancellation state
  survive. Upstream listener/rpcbind reporting, memcg high-work lifetime,
  jiffies/protection helpers, shmem truncation/seals and interruptible swapoff
  remain present. No port adaptation or semantic collision requiring a new
  owner version was identified. Historical .117 descriptions in preserved
  messages do not claim a new .118 adaptation.
- The actual OS diff changes only stable .117 to .118 and adds the final
  immutable source/hash entry. Every old entry and unstable 6.18.49 selection
  is unchanged. Traced Linux package/module builders, both ZFS modes, common
  bridge patch, version-conditional .109 patch and unchanged ZFS pairing.
  The predecessor has no extra per-version overrides to lose.
- Independently hashed the realized 246,799,115 archive bytes: the catalog's
  `sha256-tXgl0RdF3YigscvXI/tD5QHbujUV+6bVW+KIyESG93U=` is correct. The recorded
  actual package source derivation uses that flat hash and exact final revision.
  Unchanged `flake.lock` independently hashes to
  `114ab5e7079d489770694809739e25a2062ac43965994fa846fba9acd311cb90`.
  Both source worktrees were clean at the exact reviewed heads.

## Whole-history and migration conclusion

No obsolete unmerged approach, interim source pin, repair/fixup commit or
transitional compatibility path remains in either reviewed series. The process
correction was folded into its logical owner. The two OS commits separate the
reusable procedure from the independently reviewable stable catalog update.
All 50 Linux owners retain the established logical split and provenance.

**No migrations** in either range: no database/schema or persisted-format
migration, and no merged/released/deployed/externally consumed transitional
version to preserve. No repeated dependency/channel/input/generated update
stream remains: there is one final stable Linux pin, no ZFS/flake input refresh
and no intermediate repins. The Linux replay is one unchanged maintained
source series, not a redundant dependency-update stream. No further history
consolidation is required for the reviewed result.

## Documentation routing and fidelity

Placement and preservation are appropriate, subject to A1. README and MkDocs
reach the maintained operations guide in the existing `docs/os/` layout;
README remains an entry point. AGENTS and the short skill route agents to that
single authoritative process and the unchanged patch-series policy. Individual
inventories, exact refs, interruptions, results and rollout status stay in the
session records. No fixed patch inventory leaked into reusable documentation.

The guide remains useful after this initiative. Its native Git/Nix examples
match the actual interfaces; independently checked local Markdown destinations
and shell syntax. Owner evidence establishes skill/metadata validation, actual
role evaluation, docs build and ordinary hooks. The guide preserves complete
patch/package accounting, upstream-equivalence proof, semantic conflicts,
archive-byte hashing, selector checks, interrupted-replay reconciliation,
old catalog identities, external-module rebuilding, exact livepatch targets,
pool-feature/rollback limits and separate publication/integration/deployment
authority. It replaces no existing supported upgrade or recovery instructions.
No KB/WebUI binding change applies.

## Compatibility and verification limits

No new userspace/API/protocol or persisted-state contract is introduced by the
downstream port. Same-series rolling operation and recovery through retained OS
generations are a reasonable intended boundary; no coordinated fleet update is
required by this source-preserving change. External modules still need the new
kernel build, and livepatches remain exact-target qualified. Do not enable new
ZFS pool features under this kernel-only scope. Mixed-version deployment and
rollback have not been exercised here.

The source proof and quick checks do **not** establish compilation or runtime
correctness. Exact-target build and focused VM results remain required. The
lead's revised plan to use ordinary feature-push CI avoids duplicate local
builds: inspected `ci.yml`, generated kernel output ownership and the selected
fixtures. Normal CI builds `ci-toplevel`; the lead's derivation receipt equals
explicit `.118` output at
`/nix/store/smzzgsm45k9qiir8sv7wwfrn8z4f4174-vpsadminos-system-vpsadminos-26.05.git.5a59f30.drv`.
The NFS, boot stage-2, module-autoload and ZFS boot-modes cases carry the `ci`
tag. NFS asserts release and source revision; ZFS checks the selected release,
module resolver provenance and known payload through clone/rollback/send/receive
in both modes. Other selected guests follow the normal kernel selection.

This plan is sufficient to proceed; collect the actual run/head/input identities,
selected cases and results before claiming qualification. Inspect failures rather
than blind reruns. No long check was launched by this reviewer. Integration,
maintenance-ref promotion, deployment and lifecycle actions remain unauthorized.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-17-stable-kernel-update/>
