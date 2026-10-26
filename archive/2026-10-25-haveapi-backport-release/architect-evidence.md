# Backport investigation evidence

Architect investigation completed 2026-10-25. This is source/history evidence,
not an independent final review or execution test result. The technical brief is
[design.md](design.md). Lead owns state, integration and publication receipts.

## Identity and repository

`dev-session current` returned `2026-10-25-haveapi-backport-release` and both
DEV_SESSION identity variables matched the thread binding. Repository origin is
`git@github.com:vpsfreecz/haveapi.git`; SSH `fetch origin --tags` succeeded.
Master snapshot: `38ecca75edaf797d048fb36c6a50ea7e05eb50a9`.
Maintenance baseline: `1c3c98f0d77e0b23c8da1a8937f25c5799864a3b`.

`git cherry -v origin/haveapi-0.30 origin/master` found 13 existing equivalent
backports and nine missing changes. The 13 are mapped in design.md. Implementer0
subsequently applied the nine in order; the feature log inspected by architect0
contains:

| Upstream source | Feature backport |
| --- | --- |
| `39909094649b1d14a23f00615775ca7136acf4fd` | `17272733cd27429e1ad6ea2eac0da6050816635c` |
| `5003ded2a47db6b1637a3fef2fdd40474ea7de06` | `4c12fc84e7827b97cc8c1faf8a083325c18991ea` |
| `82a7f8880663dfa9d8ad6cd67e981a5842dedf9c` | `5f038aba93c341bab37a687db254cc4849fd61fa` |
| `de799b595d04e880d092b3e5ef47bce2f4587130` | `48ae0d5541b97bb9bae10924b85dc13e0a6146e1` |
| `b85ec364057f536940d689b09e612512ffffaf82` | `8b7abc097db49893da9cc8fa4395648901fec71d` |
| `610da4e3212e66fac026eb94eedb55abf6d3c66a` | `89389777edac5a67f9f8d57e5d042c060c30c1ec` |
| `4e05ca8dc4f6b938814b354996025b0aad91d9c7` | `559c162316cbb23db0d84e969da029ea82354ab9` |
| `e98e704e926961bc6d8e4a12ee15c77c1380e7a8` | `6a4d0ada1ccb2133a34c638db6c48aacb2e16c36` |
| `38ecca75edaf797d048fb36c6a50ea7e05eb50a9` | `b9b971b929edc75ef2f11fb6e541c1e0b52c99e1` |

## Fixed performance reference equivalence

Direct byte comparison of these complete binary diffs returned true:

```sh
git diff --binary b85ec364057f536940d689b09e612512ffffaf82 \
  8b7abc097db49893da9cc8fa4395648901fec71d
git diff --binary 1c3c98f0d77e0b23c8da1a8937f25c5799864a3b^ \
  1c3c98f0d77e0b23c8da1a8937f25c5799864a3b
```

Each diff is 8,350 bytes. This proves the exact mapped reference differs from the
original only by the already published 0.30.1 metadata/changelog transformation.
It does not make the original master SHA a literal ancestor of release history.
The performance adaptation must verify this proof and mapped ancestry before
accepting the exceptional weekly pair; fixed reference and budget data remain
unchanged.

## Remaining work

Package B owns the narrow maintenance-history, own-version dependency and
versioned WebUI-link presentation adaptation. Package C owns 0.30.2 metadata and
artifact preparation. Final review, final-head quick/weekly campaigns, full
component tests, branch CI, maintenance integration and publication verification
remain outside the architect investigation. No database or persisted-state
migration is introduced. No source edits, commits, registry writes, merges,
machine operations or session lifecycle operations were performed by architect0.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-haveapi-backport-release/

## PHP mirror publication and short claims

Operational recommendation requested by the lead on 2026-10-25. Investigation
only; no clone, registration, claim, source edit, publication or protected
environment approval was performed by architect0.

Read workspace `docs/coordination.md` and `workspace-host coordination guide`.
The selected package is
`/nix/store/48011krllhj3428878a8h55sb6x4wky0-dev-workspace-0.2.0`, catalog
`sha256:b79fc86c55e1257ce8959c519eba63e472b0746d10312027e1d4f16d793daa3e`.
The guide requires a registered canonical repository identity and a held claim
for shared-branch mutation, followed by immediate release after remote proof.
Separate clones of the same canonical remote contend for the same resource;
HaveAPI's claim does not cover `haveapi-client-php`.

Read-only GitHub checks establish mirror master
`195f1a4db7699dc4187463dab0f0e029df375e6c`, with message:

```text
Release 0.30.1

HaveAPI-Source: 1c3c98f0d77e0b23c8da1a8937f25c5799864a3b
```

The mirror has no AGENTS.md: its contents request returned 404 and a recursive
tree inventory independently confirmed absence. No mirror release instructions
or hook framework were found. Its README was read; it documents client use,
without another publication procedure. Recheck these facts at preparation time
if master changes. Use canonical SSH origin
`git@github.com:vpsfreecz/haveapi-client-php.git` and session-owned preparation;
never another initiative's checkout.

### Supported boundary

The current HaveAPI public release CLI exposes no PHP-only command or pause at
the mirror mutation. `publish` waits for registry uploads/confirmation before
calling `sync_php`, and performs final registry validation afterward. Acquiring
a claim before approving that unmodified job would hold it through unrelated
waits; trying to acquire based on observed log timing has a race. Neither is an
acceptable short-claim boundary.

The existing, documented matching-destination recovery contract provides a
minimal alternative. The release procedure states that an existing PHP tag must
contain the same snapshot and HaveAPI source commit and that verified matches
are skipped. In `utils/release/publish.rb`, `preflight_php` checks precisely those
conditions; `sync_php` immediately returns when they hold. It does not require
the existing commit to have been created by an earlier workflow attempt.
This supports an operator-prepared exact mirror publication followed by the
unchanged protected workflow. No private Ruby method invocation, forged Actions
environment, modified deploy key, workflow change or registry bypass is needed.

This intentionally publishes PHP before the other registries. It is an actual
authorized partial release, not a dry run or unpublished preparation. The lead
must accept this ordering before execution. The user's all-component .2 release
authorization already covers the mirror destination; no unrelated repository
integration is implied.

### Preparation and exact metadata

1. Finish review and checks of exact HaveAPI candidate C, integrate it into
   `haveapi-0.30` under its own short claim, verify the remote and release that
   claim. Preserve the final annotated HaveAPI `v0.30.2` tag at C.
2. Let the tagged release build finish without approving the protected publishing
   job. Download its original retained Actions artifact and verify the manifest,
   source C, shared version 0.30.2 and file hashes using the public `verify`
   command in the top-level Nix shell. Use the retained
   `haveapi-client-php-0.30.2.tar`; do not substitute a later rebuild or a tar from
   another build, even if source appears equal.
3. Register `haveapi-client-php` for this session with canonical bare clone and
   explicit target/default `master`; the selected package supports this without
   a catalog update. Prepare a session-owned feature commit from the freshly
   fetched, tagged mirror master. Preserve mirror-owned `AGENTS.md` and `.github`
   paths if present. All other tracked files and modes must exactly match the
   retained PHP tar; exclude build outputs and local dependency directories.
4. Use the following exact message shape for both the release commit and its
   annotated `v0.30.2` tag, substituting C's full 40-character HaveAPI SHA:

   ```text
   Release 0.30.2

   HaveAPI-Source: <C>
   ```

   The mirror commit has its own distinct SHA. It need not use the Actions bot's
   author identity; use the actual authorized operator's normal Git identity.
   The helper validates the tagged commit's source line, not an invented
   equivalence to C. Keep the local annotated tag immutable once pushed.
5. Inspect the complete mirror diff/history and prove snapshot equality using
   file paths, bytes and modes, excluding only mirror-owned metadata. Validate
   Composer identity/version `haveapi/client` / `0.30.2`; preserve applicable
   hooks and the existing mechanically generated publication conventions.
   Resolve any validation or hook issues before acquiring ownership.

### Short critical section and continuation

Acquire only the registered `haveapi-client-php` repository and verify its exact
claim is held. Freshly check the remote master against the prepared parent and
the remote tag's absence (or an already matching retained result on recovery).
Fast-forward the clean target to the prepared commit with required hooks, then
push master and the annotated tag atomically and without force. Prove by fresh
remote reads that master and the peeled tag equal the prepared mirror commit,
and that the annotated tag object is the prepared one. Reconfirm the snapshot
and HaveAPI-Source line at those refs. Release and verify the claim's resulting
state immediately, before tracking, CI, Packagist waits or protected approval.

If target state changed, stop and inspect, then release once effects are known;
repair/review outside ownership. A failed or uncertain atomic push requires
remote reconciliation before release. Never delete/move an existing tag or
overwrite unexpected mirror changes.

Before protected approval, verify the immutable HaveAPI tag/artifact identity
and matching mirror state once more. The unmodified `pypi-prepare` and `publish`
commands will each preflight that snapshot/source. Later `sync_php` finds the
same matching tag and returns without a Git mutation, so it needs no held mirror
claim. Registry and final GitHub publication waits therefore hold no repository
claim. Verify the workflow reports the existing PHP tag, and separately verify
Packagist indexing after completion.

If the existing tag is not an exact match, the helper refuses before silently
changing it. Do not approve or retry through that refusal. After the mirror push,
0.30.2 is already published: keep original source/tag/artifacts across a later
registry failure, reconcile every successful upload, and resume only through the
existing failed-job recovery. Any subsequent source/content correction requires
a new patch release; do not replace .2 bytes or tags. No machine reservation or
session lifecycle operation is involved.
