---
lifecycle: active
---

# 2026-10-12-redesign-haveapi-github-releases

## Status

- Phase: proposal prepared from repository and registry inspection.
- No application implementation, release-doc edit, independent final review,
  deployment or package publication has occurred.
- Session remains active and open for follow-up.

## Phase checklist

- [x] Verify thread/session identity and retained roster.
- [x] Investigate maintained components, existing releases and publishing support.
- [x] Write proposed design and verification brief.
- [ ] Implement release workflow, helpers and repository documentation.
- [ ] Pass quick checks and commit the complete deliverable.
- [ ] Obtain retained independent final review and whole-branch history review.
- [ ] Run longer verification and a safe build-only workflow.
- [ ] Configure publishing integrations and obtain approval for a real release.
- [ ] Integrate explicitly approved repository/target branches.

## Next actions

- Discuss the proposed release flow, then implement it in a session-owned HaveAPI
  worktree. No project worktree or development branch has been created yet.

## Documentation

- [Proposed design](design.md): scope, artifacts, approvals, compatibility,
  implementation boundaries, recovery and acceptance criteria.
- Repository documentation inspected: README, AGENTS.md,
  `doc/agent-instructions/{development,releases}.md` and Go client README.
- Planned release-documentation edits are recorded in [plan.md](plan.md).

## Repositories

- Canonical HaveAPI clone: `/home/aither/workspace/ai/vpsfree.cz/repos/haveapi.git`.
- Inspected fetched `origin/master`:
  `06865bb847a564fe20e59ea6d72856c2f01a82e3`, VERSION `0.29.0`.
- Inspected fetched `origin/haveapi-0.29`:
  `784e113c216b16586c482e710ee4a0e0a04e6f8e`, VERSION `0.29.9`.
- PHP destination `master`: `7fa4e35a9d9cb462320a4b2f2786bf84b8e024f2`;
  `v0.29.9` tag ref: `51e53ad224a2920792e78a08315eea42ad107327`.
- No feature branch is registered and no merge approval has been given.

## Commands run

- `dev-session current`: exact bound slug; both environment markers agree.
- `dev-session team list <slug> --as-is`: `lead_reviewed`; lead Sol/xhigh;
  ready reviewer0 Astra/xhigh, read-only. No assignment sent for routine planning.
- Fetched HaveAPI origin over SSH; inspected files and refs through the bare clone.
- Read PHP destination heads/tags with `git ls-remote` over SSH.
- Queried public RubyGems and npm metadata without authentication.
- Read official RubyGems/npm trusted-publishing and GitHub/Packagist guidance.

## Results

- Ruby server `haveapi`, Ruby client `haveapi-client` and Go generator
  `haveapi-go-client` are gems. JavaScript `haveapi-client` is an npm package.
- All three gem registries and npm `latest` report `0.29.9`; PHP has the same tag.
- PHP publication is currently a separate manual repository synchronization.
- Shared server docs are already required in the packaged gem and covered by
  packaging specs on both inspected branches.
- npm `repository.url` still points to `haveapi-client-js`; it must identify
  `vpsfreecz/haveapi` for the proposed trusted-publishing flow.
- The default Nix shell has Ruby/Node/PHP but lacks Go needed by generator tests.
- No test/build was run: this turn investigates and proposes, without code edits.

## Open questions

- Account-side trusted publisher settings, protected-environment reviewers,
  PHP deploy-key access and current Packagist hook configuration are unverified.
- Publication cannot be atomic across registries. Artifact retention and verified
  recovery are required; missing credentials/configuration must fail visibly.
- Source dependency locks are incomplete, so repeat builds are not yet guaranteed
  to be byte-identical. Publication retries should use retained artifacts.

## Cleanup

- No cluster, staging, build output or temporary project checkout was created.
- Unrelated shared-workspace changes were preserved; stage only this session's
  plan, state, design and portal manifest for the initial coordination commit.
