# Package B forward-refresh handoff

Published and frozen at `556a6e51b141fa419d620ad0d4ccd629fd2be6f5`.
Quick checks passed on the exact final tree with published client A6e469 and no
module replacement. Await the lead's affected independent review and fresh
long/native/package verification before readiness or deployment. C owner received
this exact head. Main owns shared state, review, watchers and rollout decisions.

- Repository/SSH: `dev-workspace`, `git@github.com:aither64/dev-workspace.git`.
- Own worktree: `worktrees/2026-10-20-workspace-session-naming/dev-workspace`.
- Own feature: `2026-10-20-workspace-session-naming`; clean.
- Fresh remote default/deployed baseline:
  `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734`, ancestor of final head.
- Final checked/committed tree: `cd57256e8a3ce2c7e44e47bcbc8a8ab6e59a0a37`.
- Immutable B source: `/nix/store/mbqjx7k9pcasq39v94fckrb3x32sx2mr-source`;
  NAR `sha256-u79gDHSlc6TQ7aZxymetoPYiEzyB9LIBSF729Ssu1Iw=`.
- Exact A: `6e469863a69c7d35941ca2e15de9514223b58f4f`, module
  `v0.0.0-20261024195456-6e469863a69c`; no replacement.
- Vendor hash: `sha256-HjUyLpUfNyEbNZ3Kx1y4tnFbVcjlQq8bc8yBTluoS/E=`.
- SSH publication used an explicit old-e515 lease; remote exact head and default
  verified. No default merge, claim, activation or lifecycle action occurred.

## Complete series and disposition

Exactly three logical commits above b3:

1. `29d64ff4da4ba7f5e5856418b9049a82f14f8ee6` — one dependency-first stream:
   final A source/lock, Go module/checksums and generated vendor hash (five files).
2. `024f4b0e05e2fa918818610fbeb52acaa45a79e6` — original naming/manual recovery
   source, focused and packaged fixtures, and three owning docs (12 files).
3. `556a6e51b141fa419d620ad0d4ccd629fd2be6f5` — original bounded archive-browser
   diagnostics (one file); adds failure evidence, does not claim a stall fix.

Complete base-to-head diff has 18 paths. Full history, diff and old→new range:
`package-b-forward-final-history.txt`, `package-b-forward-final-diff.txt`,
`package-b-forward-range-diff.txt`. Functional old4c/new024f and archive
olde515/new556a are `=` in range-diff and have equal stable patch IDs.
Original915 attention readiness follow-up is omitted as semantically redundant
with deployed baseline's 2-second explicit-stage/diagnostic implementation.
It is **not literal patch equivalence**. The entire upstream attention test and
its existing fencing/side-effect assertions remain byte-identical to baseline.

All 90 paths changed by the newer baseline outside our feature paths retain
exact baseline blob identities. This includes runtime retry/policy schema-1
capabilities, state/recovery readers and writers, accepted fork/plan recovery,
admission/deletion recovery, cancellation isolation and `LimitNOFILE=524288`.
Only the client node changes in the flake graph; native, sibling/follows,
provider and catalog policy are preserved. All resolved ephemeral Go source files
match immutable A; Luna catalog SHA-256 remains
`049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`.

A separate temporary-index reconstruction from deployed b3 plus original
functional/archive patches and exactly five final dependency blobs produces the
exact final tree. Proof: `package-b-forward-final-proof.json`; input proof:
`package-b-forward-input-proof.json`; final source metadata:
`package-b-forward-flake-metadata.json`.

**No migrations or new persisted schema** occur in this naming delta. Existing
reserved identities/old preparation records remain readable. Preserve the newer
installed retry/policy state capabilities; rollback to the obsolete candidate
would be a downgrade. Old naming e515 is not a literal ancestor of final B; its
functional/archive changes are reconstructed, with redundant915 omitted.

Before mutation, the complete old four-commit history/mbox/diff, pins, refs and
163 same-session review/check/native/build/rollout records were copied into
`package-b-before-forward-refresh-2026-10-24/` with a SHA-256 manifest. This
includes old reviewed ranges and provisional failed-CI evidence. Old naming
heads/builds were never activated by this initiative; previous provisional
consumption was within this initiative, with no known supported external
boundary requiring repeated pins. No evidence was discarded or recertified as
fresh-head acceptance. Earlier intermediate-history details remain in that
preserved handoff and evidence.

## Behavior and documentation

One 30-second context starts before queue admission; two operation slots stay
held through native work, at most two fresh utility calls total, 200ms cancelable
backoff and cleanup. Provider is resolved once; input/model/settings stay fixed.
A fresh call needs the client's proven transient/settled/cleaned accessor plus
one second inference and 250ms cleanup remaining after backoff. Generic success
fallback and attachment-only placeholder are removed. Ultimate failure stops
before base/slug/handoff reservation and reuses saved-input retry/manual controls.

The original source patches apply cleanly atop b3. Owning docs are
`docs/session-preparations.md`, `docs/workspace-portal.md`, and
`docs/codex-package.md`. Main applied its context-owned writing pass to the final
`package-b-forward-docs.patch` and approved unchanged before commit. Newer recovery
sections remain intact. No new UI strings or control styles were introduced.

## Final quick evidence

All commands use the repository Nix environment. Go checks use an absent
session-owned `DEV_WORKSPACES_CODEX_PROVIDERS` path, final A and `-mod=readonly`.
No replacement, provider change, live request or registered test session is used.

- Naming/preparation: `go -C portal test -mod=readonly ./internal/web
  -run '^(TestSessionNam|TestSessionPreparation)' -count=1 -timeout=55s` —
  PASS36.625s package time (51.183s including first compilation).
- Admission/generation/fork: same package with
  `-run '^(TestCreationAdmission|TestCreationRechecksGeneration|TestAcceptedForkSourceSharedLockRefusalAndReceiptRecovery)'
  -count=1 -timeout=20s` — PASS5.963s (20.528s with concurrent compilation).
- `node --test portal/internal/web/attention_browser_test.cjs` — PASS71/71,
  8.269s; upstream synchronization retained.
- Archive and creation browser `node --check`; actual archive helper with the
  session-only fake-Playwright checker — PASS8 success/failure/privacy/bounds
  cases; original hydration failure survives diagnostic timeout/error/serialization.
- Actual Python fixture handler, advice/terminal modes, request counters and
  embedded VM Python syntax — PASS. No listener/native inference.
- `go -C portal test -mod=readonly -overlay=.../package-b-live-naming-overlay.json
  ./internal/web -run '^$' -count=1 -timeout=15s` — PASS0.043s, compile only.
- Exact pin checker, `go mod verify`, no-replacement module identity, Go format,
  Nix fixture parse and staged/final `git diff --check` — PASS.

Commands/logs/results: `package-b-forward-{naming,admission-fork,attention,auxiliary}`
with `.log` and `-result.json`; auxiliary exact script is
`package-b-forward-auxiliary.sh`. `package-b-forward-checked-tree.json` binds the
checks to final tree. Normal commits ran in Nix with ordinary hooks; no framework
or active executable hook is declared, and none was bypassed.

The session-only preservation checker initially guessed an incorrect descriptor
limit; reading the unchanged baseline confirmed524288. Only the evidence script
assertion was corrected; source was unchanged and exact-blob checks already
passed. Final preservation/reconstruction checker passes.

## Remaining gates and exact recipes

Auto-triggered CI `Check` run40128088687 was `in_progress` at the non-waiting
snapshot. No superseded active own-branch run existed, so none was canceled.
No CI wait/trigger/rerun occurred. Snapshot and disposition:
`package-b-forward-ci-{snapshot,disposition}.json`.

`package-b-coverage-inventory.md` distinguishes quick component evidence, pending
Ruby profile capability/collection checks, packaged native creation and the
actual-collector probe's custom-name admission/handoff-only scope. Architect has
rebound `collection-probe-plan.md` to final B and compile-checked unchanged
prototype files. Actual probe and refreshed native/package checks remain with
main after independent review. A green creation VM alone cannot establish a
usable native conversation during collection.

`package-b-live-naming-smoke.md` is rebound to final source/client and cheap
compilation evidence. Discovery uses service `vpsfree-cz` and all-thread descendant
ownership. Main may execute it only after authorized activation under machine
ownership. It calls the actual deployed naming backend with the discovered
selected provider and records useful name/deadline/profile/backend continuity;
it creates no registered session and needs no session lifecycle cleanup. It
bypasses the HTTP/provider-resolution wrapper, so its claim is helper/backend
naming, separate from the packaged creation fixture. No live discovery/inference
was performed for this refresh.

Stable session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/
