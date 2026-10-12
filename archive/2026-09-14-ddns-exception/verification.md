# DDNS fix and channel update: merged

The token-only DDNS fix is merged and pushed to both repositories' master
branches. No production deployment was performed.

| Repository | Merged commit | Change |
| --- | --- | --- |
| vpsadmin | `f7a17d6e512f0b11e2c908813eb2e780261e20ae` | Nil-safe administrator check and DDNS/account-state request regressions |
| vpsfree-cz-configuration | `b0bb82d13159ce0da15375acf0483ab58572824a` | Channel vpsadmin / role vpsadmin / input vpsadminServices pinned to that exact fix |

## Local acceptance

- The two new anonymous A/AAAA user-zone request regressions reproduced the
  original `undefined method 'role' for nil` before the runtime fix.
- Final targeted run: **21 examples, 0 failures**, seed 39779; 2m11.6s plus
  11.59s loading. All enabled plugin migrations loaded in the isolated test DB.
- Coverage: A/AAAA updates and unchanged refreshes in active user-owned zones;
  suspended and soft-deleted owner rejection with no record or chain changes;
  existing system-zone and unknown-token behavior; IP parsing, address-family
  checks and operation semantics; authenticated suspended-owner rejection and
  preserved administrator exception through real DNS Update requests.
- Targeted RuboCop passed. All final pre-commit and commit-message hooks passed,
  including API and WebUI i18n health checks.

Run from the vpsAdmin repository using `nix develop .#api`, which enters api/:

```sh
bundle exec rspec spec/api/resources/dns_record_spec.rb \
  spec/models/operations/dns_zone/dynamic_update_spec.rb \
  spec/api/resources/lifecycle_bypass_spec.rb \
  --example DynamicUpdate \
  --example "DNS record owned by a suspended user" --profile 5
```

Two fixture assumptions were corrected before acceptance. A zone without a DNS
server can update without a nonempty transaction chain. Hard-deleted users do
not normally retain live owned zones/tokens: real deletion removes them, whereas
changing only the recorded state leaves an inconsistent fixture. The final
runtime change remains the one-line nil-safe caller-role check. Details and
original failed runs remain in the initiative logs and durable notes.

## Integration and channel verification

Both integrations used fresh detached worktrees from fetched origin/master and
`git merge --ff-only`, followed by SSH pushes. Remote master and retained feature
branch heads were verified at the exact SHAs above. Comparisons were captured
before integration, and temporary integration worktrees were removed normally.

The channel pin was generated with:

```sh
confctl inputs channel set --commit vpsadmin vpsadmin f7a17d6e512f0b11e2c908813eb2e780261e20ae
```

Only flake.lock changed. A structural comparison verified that only the
vpsadminServices lock node changed; its followed dependencies and original input
specification are unchanged. `confctl inputs channel ls vpsadmin` resolves the
expected fix. The generated commit message was preserved, including its
standard long changelog line.

## CI and boundaries

At handoff, RuboCop and i18n health passed on the final vpsAdmin feature and
master heads. API Specs and integration CI remain queued/running; no completed
failure was reported for the final head. No configuration workflow was listed
for its commit at the status check. Snapshots are in `ci-vpsadmin-final.json`
and `ci-configuration-final.json`.

Per the user's explicit fast-track instruction, passing targeted local specs
was the merge gate. Separate reviewer agents, the full local suite, VM
integration tests and waiting for long CI were omitted. Obsolete runs for the
superseded feature SHA were cancelled; final-head runs were preserved.

The uploaded email remains outside Git. Its token was compared privately
against tracked files, indexes, this session's artifacts and committed changes;
the URL/token is not included in repository artifacts. Tests use synthetic
records and tokens. No live DDNS request was sent.

Feature branches/worktrees and the session remain available. API deployment is
a separate next action; no migration, token regeneration or client change is
required.
