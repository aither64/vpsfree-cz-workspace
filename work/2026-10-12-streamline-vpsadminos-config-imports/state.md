---
lifecycle: active
---

# 2026-10-12-streamline-vpsadminos-config-imports

## Status

- Phase: implementation preparation; user authorized the accepted plan on
  2026-10-14 with "Implement the plan".
- Architect0 is recording the accepted brief; implementer0 will own source edits.
- Lead owns KB candidates, session records, and verification/review coordination.
- No merge or production publication approval has been given.
- Investigation established selection was automated at image creation only.
- Source checked at upstream `staging` revision
  `1150e37b1cc997b1728f2fda806a3433ef55b798` (2026-10-13).

## Phase checklist

- [x] Verify exact session identity and inspect retained Full-team roster.
- [x] Trace upstream module exports and stable/unstable guest templates.
- [x] Record findings and source/deployment limits.
- [x] Resolve session metadata and complete architect-owned read-only design.
- [x] Settle grouped release keys, retained underscores, release-aware modern
  stable exports, explicit unstable, and six KB candidates.
- [ ] Record design and commit substantive initial plan/state.
- [ ] Implement source changes and KB candidates; pass quick checks and commit.
- [ ] Independent final committed-deliverable and whole-branch review.
- [ ] Four image integration cases, monitored by fresh utility watcher.
- [ ] Publish feature branch and prepare/verify guarded KB staging bundle.
- [ ] Explicit integration/publication approvals and execution (not authorized).

## Next actions

Commit initial plan/state, create the same-session feature worktree, and assign
implementer0 after design.md is written. Prepare all-page KB source snapshots
and six candidates while application work proceeds. Retain lifecycle active.

## Documentation

Design and verification brief: `design.md` (architect-owned, being recorded).
Planned project guest guide and six bilingual KB candidates are substantive
deliverables and will be included in final review.

## Repositories

- `repos/vpsadminos.git`: read-only inspection plus fetch of upstream `staging`.
- No feature branches or worktrees created or registered.

## Commands run

- `dev-session current`: exact bound slug; both environment markers match.
- `dev-session team list 2026-10-12-streamline-vpsadminos-config-imports --as-is`:
  architect0 (Astra/xhigh, workspace_write), implementer0 (Sol/xhigh,
  workspace_write), reviewer0 (Sol/xhigh, read_only); all ready.
- Architect assignment through `dev-session team assign ... --message-stdin`
  refused: `explicit ordinary tracking is required; repair unresolved metadata
  offline`. The manifest is schema 2 with creation still `creating`; the inspected
  runtime source requires schema 1 at this guard. No metadata rewrite attempted.
- `git ls-remote --symref origin HEAD` confirmed default branch `staging`;
  `git fetch origin staging` refreshed the inspected source.
- `git show` / `git grep` traced the files below. No tests or builds run.

## Results

- `os/lib/nixos-container/stable/{minimal,impermanence}.nix` derives
  `container_<release>` from `lib.trivial.release` at template build time.
- `os/lib/nixos-container/template-flake.nix` writes that choice as a literal
  flake module import. The generated flake does not compute it again when the
  guest changes its nixpkgs input. Configuration is copied only when absent.
- Unstable templates explicitly select `containerUnstable`.
- `flake.nix:245-255` exports fixed modules for releases 22.11 through 26.05;
  `container` and `containerStable` directly alias the latest stable module,
  rather than dispatching by the guest nixpkgs release.
- `os/lib/nixos-container/vpsadminos.nix` always fails an assertion asking the
  user to choose the stable or unstable file; it is not an automatic selector.
- A concrete incompatibility: the 25.11 module sets
  `services.resolved.fallbackDns`, while 26.05 sets
  `services.resolved.settings.Resolve.FallbackDNS`.
- A future selector would remove the manual release-specific module change for
  upgrades. Its design and unstable handling remain follow-up work; no
  implementation or architectural review was completed.

## Open questions

- Which versions of these image templates are deployed in the live image
  repository, and which import style existing VPSes retain, were not inspected.
- Earlier delegation refusal is resolved: manifest schema 1, creation ready,
  matching retained root/roster; architect planning turns succeeded. No manual
  metadata rewrite or roster change was made by this lead.

## Cleanup

Session remains open and lifecycle active. No lifecycle action or production
deployment is authorized. Preserve unrelated shared workspace changes and index.
