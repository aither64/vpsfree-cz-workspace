---
lifecycle: active
---

# 2026-09-24-session-identity-team-prompts

Merged and deployed. Remaining: confirm a newly portal-created conversation's
first external tool shell follows its trusted session binding when environment
markers are absent. No further code change is currently known.

Implementation and review remediation are committed, deployed, and merged in three
registered feature worktrees under
`worktrees/2026-09-24-session-identity-team-prompts/`. Each branch uses the
initiative slug:

- Generic runtime `88587b083fd6e7829215e54c4f663660bd1f3802`, base
  `1b836baf85e8486e0455ce2a70f9c4423328ac22`.
- Extension skills `e58f98d` and dependency pin
  `8f06fdb52cddf643fa6bc943381425b19fcb1ab8`, base
  `ad13e7fc2a1874a54921bb91d743e4a4851d3c4a`.
- Site workspace `aeb4c7af1770ee0c1367bffadb515f430162def8`, base
  `7787ee79eadd14c2a7623eeb7a6b206b75ad9ee8`.

The catalog is schema 4 with purpose and instructions for named roles. Lead
and member prompts are frozen in direct creation snapshots/rosters, while old
records retain legacy behavior. CLI/portal creation, retry, fork, revive and
idle reconciliation bind the exact session identity without a prompt-only
model turn. The Team tab can offer configured custom roles. Site rules and
extension skills use the trusted thread binding and saved role purposes.

Mandatory consolidated review completed using one fresh standalone reviewer,
`gpt-6-sol`/`xhigh`, because this initiative has no retained team roster. Risk
is high: session ownership and persisted creation/roster contracts change
across three packages. Lanes are general, architecture, scope, and risk. The
review packet is `work/2026-09-24-session-identity-team-prompts/review-packet.md`.
Reviewer findings: Blocking—roster writer could persist data beyond its 256 KiB
read cap after prompt and fork-snapshot expansion; creating-thread recovery
could resume a candidate without its frozen lead policy before first message.
Important—custom role prefixes could collide in address allocation; explicit
`--team` CLI retry re-resolved current catalog prompt text instead of using the
frozen journal. All four were fixed in the amended runtime commit, using the
reviewer's narrow requested behavior. Focused Go packages and Ruby creation
tests pass; Nix flake evaluation passes for generic runtime and site package.
The first generic CI runs failed because its Nix team-catalog fixture still
used schema 3. It is now schema 4; a local `nix flake check --no-build` passes.
The first extension CI run failed because skill policy assertions still named
`reviewerN`; these assertions now check purpose-based selection and pass
locally. A subsequent generic CI run found a site-specific path in a generic
test fixture; the fixture now uses `/workspace`, and its local `generic-source`
Nix check passes. Final-head generic CI run `35931145211` and extension CI run
`35931393354` passed. No re-review was required for these
narrow remediations or fixture updates under the review skill's rerun rule.
Full `nix flake check --print-build-logs` passed on all three final clean
heads under a fresh Luna/low watcher. Extension and site logs are complete in
`work/2026-09-24-session-identity-team-prompts/logs/`; the generic watcher
observed exit 0 and `all checks passed`, but its saved log is truncated.
The aitherdev user-profile switch succeeded to
`/nix/store/361dj4034wlgj4h02qcqn0c9i1pb1gr7-dev-workspace-0.2.0`.
`workspace-host status` reports that package, portal/router/Codex services
are active, the portal returns HTTP 401 without authentication, and the
installed team catalog is schema 4 with the expected lead instructions and
Luna/low watcher. The deployed package was built before the workspace feature
was rebased onto the tracking-only commit `f2cea8b`; `git range-diff` proved
the feature patch identical. The rebased site head passed Nix flake evaluation
and its Ruby instruction tests (4 runs, 48 assertions). The source-check
fixture lesson is in `notes/dev-workspace/2026-09-24-generic-source-fixtures.md`.

All three approved feature heads now equal their remote `master` heads:
generic `88587b083fd6e7829215e54c4f663660bd1f3802`, extension
`8f06fdb52cddf643fa6bc943381425b19fcb1ab8`, and site workspace
`aeb4c7af1770ee0c1367bffadb515f430162def8`. Each was integrated by
fast-forward; feature refs remain. The comparison snapshots were captured at
the final heads. A browser-created first-shell acceptance check is still
unperformed, so the initiative stays active for that feedback. The shared checkout
has unrelated dirty files; only this initiative's paths may be staged.
The current shell has no `DEV_SESSION_SLUG` or `DEV_SESSION_WORKSPACE` and
`dev-session current` found no session, so this is a new initiative. Its
stable portal URL is
`https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-24-session-identity-team-prompts/`.

Approved integration scope: generic `dev-workspace`, `vpsfree-dev-workspace`,
and this coordination workspace to their respective `master` branches. The
approval was the user's explicit “merge to master authorized” in the preceding
plan discussion and covers all three named repositories and `master` targets.
No material scope change has occurred since that approval. Deployment to aitherdev
was also authorized. No configuration repository branch is in scope.
