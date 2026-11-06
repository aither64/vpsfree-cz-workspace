# Final committed-deliverable review packet

Ready for independent final review; no long system build started.

## Request, scope and acceptance

User requested locating the old NixOS mx2 backup MX branch, copying it into this
workspace, rebasing it onto current default branches, and suggesting how to verify
it before replacing CentOS 6. Import preserves mail behavior and identities;
only current module option spelling and formatting may change. No production
access, deployments, integration, new testing framework or mail-policy redesign.

Session: `2026-11-01-mx2-nixos-migration`, workspace
`/home/aither/workspace/ai/vpsfree.cz`. Plan/state/design in the matching `work/`
directory. One repository: `vpsfree-cz-configuration`; feature worktree under
`worktrees/2026-11-01-mx2-nixos-migration/vpsfree-cz-configuration`.

Acceptance is honest recovery/rebase with clean source preservation, bounded
compatibility edits, quick checks and required targeted build after review.
This is not a claim that the inherited server is ready for production.

## Historical range and migration inventory

Original source `/home/aither/workspace/vpsfree.cz/vpsfree-cz-configuration`:
old base `0bcc165f13059782bf686da39a3a9b5698b10275`, head
`40411d67ee97cea800bcccd89b0473432b4502c4`.

- `be8435d1d4f3e656af1d7d090d867797d2713a66`: add mx2 host configuration.
- `40411d67ee97cea800bcccd89b0473432b4502c4`: add deployment cache;
  exact patch already upstream as `17ac0d2b842a88ae7f7b76b1651f36d984dadb2c`.

Preserve original source/import ref. Drop redundant cache commit from replay.
No database/schema migrations and no repeated dependency/input update streams.
Existing mx2 deployment history is unknown; publication is not deployment proof.
Persisted mail queue/Postgrey state and identity compatibility still matter.

## Risk, lanes and reviewer

High: SMTP/security policy, host configuration and durable mail queue implications.
One retained independent reviewer `reviewer0`, `gpt-6.1-sol` / `xhigh`, read-only;
verify ready identity/settings in live same-session roster before assignment.
Lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
Read mandatory-change-review skill and every selected lane reference. Review
complete final base-to-head series, final diff and migration provenance; explicit
history and repeated-update conclusions required. No nested reviewers.

## Known assumptions and proposal

See architect-owned [design.md](design.md) for full provenance and six staged
verification steps. Original host identity, target, container placement, admin
keys, stateVersion and mail policy are preserved, not verified production facts.
No branch-specific unmerged dependency: consume current default inputs unchanged.
A modern option name `inputs.channels` replaces `swpins.channels`.

Known inherited gaps: transport maps do not authorize relay; no explicit relay
recipient directory, TLS setup or enabled milter; public/internal IPv6 differs.
Inspect effective configuration and independently assess findings. Proposed tests
cover controlled SMTP normal/denied delivery, deferred queue persistence and
recovery, greylisting/DNSBL/TLS/milter failures, then separately authorized
preproduction and queue-safe cutover/rollback. No runtime tests have happened.

## Documentation placement

No new reusable operator procedure or supported runtime behavior is implemented.
Design and import evidence are session proposal/findings, appropriately kept
here; project config rationale only where needed. No receipts committed in
configuration repository. Production shortcomings must be disclosed in handoff.

## Final range, quick checks and consolidation

Final base `c040c14cdbacc07998700b524996a89306188d7f`, final head
`e4c1ac0c5ae7426fb019b79ba936b30ce63e6e6c`. Complete final series:
one commit `e4c1ac0c5ae7426fb019b79ba936b30ce63e6e6c`,
`cluster: add mx2.vpsfree.cz`.

Final diff: five paths, 94 additions: cluster import, mx2 config/module,
public toms SSH key and container placement. Original host patch was 68 additions;
extra lines are RFC formatting. Only functional adaptation is channel option
rename. No final cache delta, superseded pin stream, intermediate migration or
additional source change. Inspect full diff directly from final range above.

Quick checks passed: `nixfmt --check`, `nix-instantiate --parse` on all five paths,
working/index `git diff --check`; confctl inventory finds exactly one mx2 with
NixOS, expected hostname/ID/channels; targeted toplevel drvPath evaluation passes.
Normal Overcommit Nixfmt pre-commit and commit-msg hooks passed; TextWidth
advisory only, <=80-column workspace rule met. Clean final worktree. Dirty
precommit derivation path was recorded as preliminary evidence, not final build.
All intended source changes committed. Publication/provenance writeup in progress;
no additional source changes planned. Long build command after review:
`nix develop -c confctl build cz.vpsfree/containers/mx2`.

Full unchanged input graph in `input-graph.json`; active nixpkgsStable 718f670e,
vpsadminosOsStaging b45b27b4, confctl 7bee58a5. No input/lock changes.

 Historical hook mismatch
required normal replay on current default instead of executing hooks on old
source lacking `.overcommit.yml`; no hook bypass. Verify recovery/equivalence
in import-rebase.md and source-before/after comparison.
