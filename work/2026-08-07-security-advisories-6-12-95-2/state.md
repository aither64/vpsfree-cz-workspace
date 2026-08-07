# 2026-08-07-security-advisories-6-12-95-2

## Repositories

- `security-advisories`
  - branch: `2026-08-07-security-advisories-6-12-95-2`
  - worktree:
    `worktrees/2026-08-07-security-advisories-6-12-95-2/security-advisories`
  - base: `origin/2026-07-13-security-advisory-automation` at `5d4138a`

## Status

- Active session slug verified from both `bin/dev-session current` and
  `VPSFREE_DEV_SESSION_SLUG`.
- Coverage source lists 14 assigned CVEs carried by cumulative live patch v2.
- Repository bundle and Overcommit hooks are installed and active.
- All 14 dossiers and reviewed evaluations are committed as one focused commit
  per CVE.
- Quick verification and the mandatory standalone review passed.
- All 14 unpublished vpsAdmin drafts were created, their exact remote
  baselines were committed, and the final read-only readiness checks passed.

## Commands run

- `bin/dev-session current`
- `git --git-dir=repos/security-advisories.git fetch --prune origin`
- `bin/dev-session worktree add 2026-08-07-security-advisories-6-12-95-2 security-advisories --as-is`
- `nix develop -c bundle install`
- `nix develop -c bundle exec overcommit --install`
- `nix develop -c bundle exec overcommit --sign`
- `nix develop -c bundle exec overcommit --run`
- `nix develop -c bin/security-advisory collect`
- `nix develop -c bin/security-advisory evaluate CVE-...` for all 14 CVEs
- `nix develop -c bin/security-advisory validate`
- `nix develop -c bundle exec rubocop --parallel --force-exclusion`
- `nix develop -c bundle exec rspec`
- `nix develop -c bin/security-advisory sync CVE-...` for all 14 CVEs
- `nix develop -c bin/security-advisory sync --apply CVE-...` for all 14 CVEs
- `nix develop -c bin/security-advisory ready CVE-...` for all 14 CVEs
- `git fetch origin --prune`
- `nix develop -c git push --set-upstream origin 2026-08-07-security-advisories-6-12-95-2`
- `nix shell nixpkgs#gh -c gh run watch ... --exit-status`

## Results

- The canonical bare remote already uses the required SSH URL.
- Worktree creation checked out the intended branch and base commit.
- The checkout hook returned exit 78 because the worktree-local locked bundle
  was not installed yet. Installing the locked bundle from `nix develop` and
  then installing/signing Overcommit resolved it.
- Production evidence snapshot collected at `2026-08-07T13:39:40Z`:
  - node-set digest:
    `f434faac03a83c7ba7329214924bdb7561a5c619dd09b9f53a9dd9c660e9092e`
  - evidence digest:
    `15f4ad1aa5b0c7474bc909ce95c64e9e9004672df98400085739efe79b4c34ac`
  - all 12 compute Nodes report booted Linux 6.12.95 and active
    `livepatch_2` patch version `2`; storage Node 161 is excluded by workload.
- Every new evaluation is complete with 12 `mitigated`, one `not_affected`,
  zero `unknown`, and zero `vulnerable` current Nodes.
- Exact live-patch transition times range from
  `2026-08-06T01:30:05Z` to `2026-08-06T02:46:43Z` and are retained in every
  evaluation.
- Quick verification passed:
  - RuboCop: 28 files, no offenses.
  - RSpec: 121 examples, zero failures (seed 59064).
  - dossier validation: 19 dossiers, including all 14 additions.
- Rewritten commits:
  - `e99c446` accepts the exact booted
    vpsAdminOS identity as a fail-closed fallback only for legacy evidence
    lacking a direct Linux source revision.
  - `8d46fde` through `c5355d3` add one focused dossier/evaluation commit per
    CVE, including its corresponding dossier-spec expectations.
- Mandatory review initially found:
  - Blocking: the 14 independently reviewable dossiers were bundled.
  - Important: correction-only commits should be folded into their owners.
- Resolution:
  - rewrote the unpublished branch to the focused series above;
  - folded the clean-identity fallback into `e99c446`;
  - folded all corrected mainline boundaries into their owning CVE commits;
  - retained a final tree byte-for-byte identical to the reviewed fixed tree.
- The same standalone reviewer confirmed both findings resolved with no
  remaining functional, security, compatibility, dossier-content, or history
  findings.
- Post-rewrite verification passed:
  - RuboCop: 28 files, no offenses.
  - RSpec: 121 examples, zero failures (seed 2779).
  - dossier validation: all 19 dossiers.
- Synchronization dry-runs proposed a new draft for every CVE with 12
  `mitigated` compute Nodes and storage Node 161 `not_affected`.
- Applied synchronization created only unpublished `draft` records. Each is at
  content revision 13 and has a committed schema-two submission baseline:

  | CVE | vpsAdmin draft ID |
  | --- | ---: |
  | CVE-2025-37964 | 11 |
  | CVE-2026-53365 | 12 |
  | CVE-2026-64189 | 13 |
  | CVE-2026-64265 | 14 |
  | CVE-2026-64266 | 15 |
  | CVE-2026-64422 | 16 |
  | CVE-2026-64423 | 17 |
  | CVE-2026-64507 | 18 |
  | CVE-2026-64508 | 19 |
  | CVE-2026-64554 | 20 |
  | CVE-2026-64556 | 21 |
  | CVE-2026-64560 | 22 |
  | CVE-2026-64564 | 23 |
  | CVE-2026-64580 | 24 |
- Every `ready` preflight passed after a fresh read-only production evidence
  collection. The active node-set digest remained
  `f434faac03a83c7ba7329214924bdb7561a5c619dd09b9f53a9dd9c660e9092e`,
  with 12 `mitigated`, one `not_affected`, and no blocking Nodes.
- Final post-submission verification passed:
  - RuboCop: 28 files, no offenses.
  - RSpec: 121 examples, zero failures (seed 65004).
  - dossier validation: all 19 dossiers.
- No advisory was published and no notification email was sent.
- The feature branch was pushed at `c0561d8` after confirming that its upstream
  base remained `5d4138a`.
- GitHub Actions passed on the pushed head:
  - RSpec run `31193811917`.
  - RuboCop run `31193811854`.
- An initial push outside `nix develop` was stopped by the pre-push hook because
  its locked Ruby gems were unavailable. Repeating the push inside the project
  shell ran the hook successfully; no hook was bypassed.

## Open questions

- None.

## Cleanup

- Keep the feature branch after merge.
- Remove the initiative worktree only after integration or abandonment.
