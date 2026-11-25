# Workspace tracking-baseline refresh

Owner: implementer0. Complete for lead acceptance: own workspace feature is clean,
published and mechanically equivalent to deployed `30b74dc3`. No product build
or test was rerun. Root owns independent mechanical-review reuse acceptance,
actual default integration, fresh remote lineage proof and machine release.

## Exact source and authority boundary

Repository `git@github.com:aither64/vpsfree-cz-workspace.git`, target `master`.
Own branch `2026-11-25-archive-failure-investigation`, own sparse worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-archive-failure-investigation/workspace`.
Exact session identity/environment and saved implementation-purpose write access
were reverified. Applicable workspace/repository instructions and Git, verification,
commit, tracking/documentation guidance apply; no hook framework or active custom
hook is declared/present and no hook was bypassed.

| Range | Base | Head |
| --- | --- | --- |
| Old reviewed/deployed G selection | `e7b876f69aca4554d52a3ac19ed097263847ad43` | `30b74dc3278728ab36197e0d2ef2cf76c66cf791` |
| Refreshed final selection | `97bf6db040d35ac10be0a5a9302ecb5c4c037df7` | `f1741f4982a3bfef710fc3837f8929b3fa4d8f76` |

Fresh origin/master remained `e7b876f6`; shared master was already `97bf6db0`.
They were linear, so fresh authoritative shared master was selected. No shared
branch/index mutation was performed. The lead had already reconciled its stopped
preflight and released its repository claim before this package. This owner
acquired no repository/machine claim and performed no integration or activation.
User approval scope remains with the lead; clean equivalence does not expand it.

The baseline change is one tracking-only archive commit, touching only work/ and
archive/ paths. Complete nontracking tree entries (paths, modes, types, blobs)
are identical to old base, including app source, AGENTS/instructions and inputs.
There are107 diff paths with rename coalescing,108 changed raw tree entries;
these counts describe the same tracking-only change.

Before retaining/republishing inherited tracking, the authoritative registry
`/home/aither/.local/state/dev-workspaces/sensitive-sessions/vpsfree.cz-8a2a555cb2f65b33`
was verified present and the exact marker
`2026-11-25-exception-root-cause.json` absent. The source is ordinary under the
runtime's immutable sensitivity contract. The retained source manifest also has
no sensitivity marker. Only task-relevant metadata was read; no foreign session,
tracking source, branch, worktree, runtime, team or lifecycle was modified.

## Whole-branch history, preservation and reconstruction

The entire fresh-base-to-head series is one commit:
`f1741f4982a3bfef710fc3837f8929b3fa4d8f76 inputs: select archive preparation fix`.
Final diff is only `flake.nix` and `flake.lock`,5 insertions/5 deletions.
The original pin commit message/content was retained by a clean rebase.
No migrations, fixups, intermediate pin stream, obsolete final approach or new
compatibility path. No migration was merged/released/deployed/externally consumed.
Original independent review is [review.md](review.md); the existing G reuse
certificate in [mechanical-refresh-review.md](mechanical-refresh-review.md) binds
the old G range. Root now owns extending that certificate to this exact successor.

The old deployed head is preserved both locally and over SSH as
`refs/heads/2026-11-25-archive-failure-investigation-deployed-workspace-30b74dc3`.
Its exact ref value is `30b74dc3278728ab36197e0d2ef2cf76c66cf791`.
The refreshed feature was published with an explicit lease expecting that old30
head. Fresh `git ls-remote --heads` verified both exact remote heads. Old30 is a
retained deployed predecessor, not a commit claimed literally merged by the new
successor. Equivalent integrated lineage requires the lead's later certificate
and fresh remote ancestry proof after actual integration.

- `git range-diff e7b876f6..30b74dc3 97bf6db0..f1741f49`: one `=` commit.
- Old/new complete binary patches are byte-identical; SHA256
  `0c795deb1430774873776c762fe3739ac434607d9e0c5a8db5710c24fc212818`.
- Both stable patch IDs: `3a3e8dcf13db76da2ba49e602f41c2e616ba76b6`.
- Independently loaded fresh97 into a disposable index and applied old30's patch.
  Expected and final trees both `c82c27b5d7d8f59ef6dcb01a4f91278f92aabc48`.
- The supplied read-only verifier independently reconstructs every final tracked
  path/mode/blob in memory from fresh97 plus only the old pin paths, compares
  the complete tree and exact binary patch, and verifies one final commit.

Reproducible bounded read-only command, after inspecting the script:

```sh
python3 /tmp/archive-workspace-refresh-bhjdii1l/verify-readonly.py
```

Script SHA256 `44605c535169a53bc3121583df6f04ec3d8893b059f609525c5658f2d3f05477`.
Owner result `read-only-proof.json` in the same directory, SHA256
`51b990316be40916955009cb55f7e77a0021dd1531ac98463184111e52933bd4`.
The verifier performs only Git/object reads, Nix derivation reads and in-memory
comparison; it writes neither Git metadata/index nor source/runtime state.
The earlier disposable-index proof, patches and preflight are retained there too.

## Exact artifact and complete-input reuse

Own sparse patterns remain `/*`, `!/work/`, `!/archive/`; all tracking entries
retain skip-worktree and ordinary `git status` is clean. Nix evaluation used
this existing sparse source worktree, without importing tracking through a new
immutable full checkout. Both metadata evaluations exited0. Nix emitted dirty-tree
and ignored cache-busy warnings while ordinary Git status stayed clean; no cache,
source or index workaround was used, and exact artifact/full-input comparisons
below resolved the source identity. No build/test command was launched.

| Artifact | Exactly unchanged derivation | Exactly unchanged output |
| --- | --- | --- |
| composed app | `/nix/store/m9pdsbnrrlwkyhp87d3cic5am7c10rbs-dev-workspace-0.2.0.drv` | `/nix/store/apjaqip0xj9cy297z2wmb8hmfqn2c8x1-dev-workspace-0.2.0` |
| composition | `/nix/store/26hx1kp1xlmsklpx2zmz991m6qj3krn7-workspace-pi-runtime-composition-tests.drv` | `/nix/store/nxf02z6jccv47rzwzkl5gx3zadq67jya-workspace-pi-runtime-composition-tests` |

Full workspace lock bytes equal deployed30 and originally tested1827; SHA256
`f411b1b56173b128a85d4c18a17869d12d9eca4add6ba1b2a843ab8b6c426919`.
The verifier also compares every parsed node/root/input/follows field to E's frozen
complete D graph receipt. Runtime remains exactf6, extensionbf12ac71a8a00b1581eed5352f99c1b2daaeff5b
and codex-web2547d535eefd4154afef4125ea0fb76e5894a8b6, with all sibling/site/native
contracts and source graph unchanged. Runtime source remains
`/nix/store/hh81k6nk1r1x0jhi0v8a1l9d53jr0h4n-source`.

Current full app AND composition derivation JSON objects were compared field by
field to E's original `target-derivations.json`: all inputs, source references,
args/builder/env/name/outputs/system/version are exactly equal. Canonical selected
full-derivation JSON SHA256
`48008632d77f09f41a907a1390e3b333c05afe439b5d57a58c4ba13b8f522eab`.
Raw final metadata is `final-app-eval.json` and `final-composition-eval.json` in
the operation directory. This is exact derivation AND complete-input reuse,
not tree-only reuse. E's passed four-target record and output NARs remain in
[verification-evidence.md](verification-evidence.md); no test rerun is justified.
The previously deployed selected app is literally the same apja output.

## Existing final-head comparison receipt

The ordinary explicit capture requested97..f174, but the same final head already
had an immutable first comparison. Its verified saved pair is:

- base `e7b876f69aca4554d52a3ac19ed097263847ad43`;
- head `f1741f4982a3bfef710fc3837f8929b3fa4d8f76`;
- label `Merge base with locally available origin/master`, no warning;
- savedAt `2026-11-25T16:20:33.936624911Z`.

Existing proof:
`/home/aither/.local/state/dev-workspaces/portal/vpsfree.cz-8a2a555cb2f65b33/repository-comparisons/234ae1648ad02667c1e325198ec845b3/f1741f4982a3bfef710fc3837f8929b3fa4d8f76.json`,
SHA256 `262ee43b8557ef14ec529a4cb24caf3cf53f85a4ae868a9b6342b93a2029ef56`.
Schema/own slug/repository ID/final head were validated through the ordinary
portal store metadata/source. Receipt has no caller field; do not invent whether
its original writer was CLI or automatic browser/status observation. It captures
the final exact head including the tracking-only baseline and pin commit.
The explicit different-base refusal preserved it; no overwrite/private repair,
recreated capture, extra commit or lifecycle helper was used. Final-head capture
is present; new pin certificate/review range remains exact97..f174 above.

## Delivery

Ready for root's bounded independent verifier/certificate and approved actual
workspace master integration. Source/head/inputs are settled and SSH-published;
no scope deviation or unresolved product gap. No applicable workspace branch CI
workflow exists under the retained D/G inventory. No shared master/index, core
runtime/config target, claim, deployment, foreign session or lifecycle mutation.
Capacity for one next package after acceptance; no queued work.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-archive-failure-investigation/
