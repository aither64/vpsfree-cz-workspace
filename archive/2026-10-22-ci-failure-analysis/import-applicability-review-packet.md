# Focused import applicability: final review packet

Final committed isolated head: `36965e88b8ac71a547b2672f12d472d4c33ea46b`.
Tree: `6699cbd7ea4a58633d7a150f683543415a148286`. Clean index/worktree.
Quick specs, syntax/style and normal commit hooks pass; all intended changes
are committed. Normal hooks retain72-column preference warnings; lines conform
to the repository80-column maximum. Compared with old04a2, exactly seven paths
change, +230/-35, as the focused correction described below.
Complete base-to-head diff:42 files, +1884/-3951.

Final complete range, oldest first:

1. `0d649b80f67a262830682d1651cc748d752e1d42` — writer persistence.
2. `450da920081a1c2765b340b1279102ebe9c6b596` — reader/import/GC safety v2.
3. `e00ee7027c9ccfd7b0f29a99f651a2a019beb34a` — hotplug health checks.
4. `43ff36ab23c5cf9b2e8444e7b3bea03a71869342` — production transition regression.
5. `36965e88b8ac71a547b2672f12d472d4c33ea46b` — retirement/policy.

Writer is unchanged; later three owners are exact patch replays. Reader is the
sole changed owner, advanced to v2. Author/date/message preservation and full
range comparisons are in implementer0's final report/repair records. All hooks
ran normally; the first health cherry-pick was followed by an ordinary exact
message amend to run hooks before final replay. No intermediate fixup ships.

## Outcome and boundary

The user selected a minimal correction after learning that enabling impermanence
on an ordinary already-running NixOS container caused the reviewed importer to
require a temporary-root GC owner. Next-start configuration does not change the
current run's root. Accept a proven ordinary base-root run without rewriting its
saved runtime state, inventing ownership or inhibiting reclamation. Missing GC
ownership alone must never authorize temporary-root adoption.

Design: design.md:5206. Source owner: implementer0. Repository: vpsadminos,
isolated checkout `worktrees/2026-10-22-ci-failure-analysis/vpsadminos-import-applicability`.
Base remains `e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854`. Prior reviewed head:
`04a2d2696bb4bcc7602221008a5c5096ede98046`; report minimal-final-review.md.
The primary checkout remains at that old head until accepted promotion.

The correction belongs to the authenticated legacy-reader owner. Preserve the
writer and later health/regression/retirement owners, fold this repair into the
reader, and retain the exact dated old-head backup. No fixup commit should ship.
The implementation report supplies native range/tree/diff comparisons and the
new complete inventory. Earlier obsolete diagnostic/recorder history remains
excluded and preserved in historical refs.

## Acceptance and compatibility

- Complete saved base selection with cleanup false, no same-run temporary owner
  and no overlapping GC owner permits a base candidate check. It does not prove
  the run is ordinary until held live-root/process/ZFS/private identity passes.
- Reuse the held-identity preparation, final rechecks and publication path;
  preserve existing stale repair and correct temporary-root authentication.
- Explicit absent GC snapshots are allowed only for the base case with empty
  in-memory ownership; file appearance/disappearance or changed evidence refuses.
  Strict missing-file behavior remains the default for temporary recovery.
- Permit legitimate base clones without relaxing temporary origin restrictions.
- Preserve YAML/run ID/GC bytes for the ordinary case and retain rollback,
  publication and pool retirement fencing on genuine failure.
- Reverse-toggle dispatch is unchanged; no new management API, schema, framework,
  runner contract, input/pin change, restoration campaign or degraded-state API.

No migrations: no schema/YAML/run-ID version change, and no migration was merged,
released, deployed or externally consumed in this feature range. Older readers
retain their existing readability and lose the new protections on rollback.
No coordinated node update is required. There are no repeated dependency,
channel, kernel, gem or generated-artifact update streams; upstream lock remains
the selected base's lock. Verify these conclusions independently.

Owning implementation is in run_configuration.rb and narrow garbage_collector.rb
snapshot support; pool.rb has a contextual comment. Existing run-configuration
and GC specs cover the new cases; the existing pool specs remain a caller check.
No shared framework API or external test-runner consumer changes.

Lasting explanations are the relevant paragraphs of docs/os/updates.md and
docs/containers/datasets.md. The lead supplied and audited this minimal prose.
Session-specific rollout limits remain here and in state.md, not project docs.

## Checks and limits

Corrected cached Ruby invocation passed reader/pool/GC focused specs:
113 examples, 0 failures, seed58689, 1.68s examples plus0.399s load, after the
single lint correction. Log: repair/import-applicability-spec-4.log.
Five changed Ruby files passed syntax and RuboCop (style-2.log); diff whitespace
check passed. Prior spec-3 also passed before the control-flow lint correction.
The invocation uses isolated source and an
existing primary libosctl native extension; no compile/install/Nix occurred.
Two earlier bootstrap failures before examples remain in spec-1/spec-2 logs
(missing OsCtl initialization, then libosctl/native load path).
The final implementation report supplies normal-hook results, exact commands,
the final committed source identity and remaining gaps.

Native catalog evaluation and v1/v2 VMs remain blocked by earlier 1/4/8-GiB
discovery OOMs. No packaged-source/real-kernel/ZFS/runtime acceptance is claimed.
No fresh Nix query, build, fetch, capacity campaign, retry, push, broad CI, merge,
deployment or cleanup is selected by this packet or review.

## Independent review

Use mandatory-change-review SKILL.md and all four references directly: general,
architecture/repetition, scope/proportionality, risk/compatibility. Risk is High
because persisted run selection and host dataset retirement are involved.
Selected retained reviewer0: gpt-6.1-sol/xhigh/read_only, no settings override or
nested reviewers. Review the committed deliverable, focused changed behavior and
full final five-owner inventory/history/migration conclusions, reusing unchanged
prior review evidence where appropriate. Do not reopen excluded work or demand a
new framework/VM campaign. Report concrete findings and residual verification
limits; a source review is not runtime or publication approval.
