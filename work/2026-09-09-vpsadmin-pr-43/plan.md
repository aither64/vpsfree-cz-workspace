# 2026-09-09-vpsadmin-pr-43

## Goal

review vpsadmin pull request https://github.com/vpsfreecz/vpsadmin/pull/43

## Affected repositories

- `vpsadmin`: review PR #43 at `44cfb4357751d9c925e1a74e7bf6a3842ebd3cd1`
  against `3a64784708faef5e9f4f093255954b14e396904c`.
- No implementation changes, deployment, merge, or GitHub review submission
  requested. Findings will be returned locally to the user.

## Approach

- Inspect all six changed files, surrounding payment resources, pagination
  helpers, existing consumers, and migration/test conventions.
- Run quick verification, then the mandatory general, architecture, scope,
  and risk review lanes with fresh `gpt-5.6-sol` / `xhigh` reviewers.
- Reconcile findings against source and focused reproductions. Report only
  actionable defects with exact locations; document residual test gaps.

## Compatibility and deployment

- New datetime filters are optional API inputs. Check timezone conversion,
  inclusivity, OPTIONS discovery, and existing client behavior.
- Cursor behavior changes within the existing created_at/id ordering. Verify
  normal-user authorization and filtered pagination, including missing cursors.
- One secondary database index is added; check exact predecessor schema and
  reversible removal without changes to payment data. Old API code should
  remain usable with either index state.
- The proposed dependent WebUI Next finance feature must deploy after this API
  contract. No WebUI code or companion revision is included in this PR.
- No daemon protocol, on-disk format, node, or Nix configuration changes.

## Testing plan

- Check committed diff whitespace and Ruby syntax/lint in the API Nix shell.
- Run focused payment API and migration specs in separate RSpec processes
  against isolated disposable databases.
- Inspect CI status at the reviewed head; add temporary focused reproductions
  where needed. Do not run unrelated VM integration suites.
