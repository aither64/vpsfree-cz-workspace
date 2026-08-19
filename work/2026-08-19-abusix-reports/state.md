# 2026-08-19-abusix-reports

## Repositories

- `vpsfree-cz-configuration`
  - branch: `2026-08-19-abusix-reports`
  - worktree:
    `worktrees/2026-08-19-abusix-reports/vpsfree-cz-configuration`
  - base inspected: `origin/master` at
    `3733ab8c71b8dcfa2ad29a22ca25ed8f3acc4615`

## Status

Implementation and quick local verification are complete. The parser supports
XARF v3 and v4 decoding while the automatic-forwarding policy is restricted to
Abusix spam-trap reports with textual evidence. The supplied messages both pass
the parser in dry-run tests. The mandatory independent review and its follow-up
verification are complete with no remaining findings. Both API configurations
built successfully, and the feature branch is pushed.

## Commands run

- `bin/dev-session current`
- `git status --short --branch`
- `git --git-dir=repos/vpsfree-cz-configuration.git fetch origin master`
- Read-only inspection of parser sources and specifications from
  `origin/master`
- Local MIME/JSON and decoded-evidence inspection of the two supplied messages,
  with identifying data omitted from recorded output
- Review of the official legacy XARF v3 schema and current XARF documentation
- Read-only inspection of authentication-related headers on the supplied RT
  messages
- `bin/dev-session worktree add 2026-08-19-abusix-reports
  vpsfree-cz-configuration --as-is --branch 2026-08-19-abusix-reports --base
  origin/master`
- `nix develop -c bundle check`
- `nix develop -c bundle exec overcommit --install`
- `nix develop -c bundle exec overcommit --sign pre-commit`
- `nix develop -c bundle exec overcommit --sign commit-msg`
- `nix develop -c bundle exec overcommit --list-hooks`
- Focused RSpec for the decoder, parser, and message dispatcher
- Focused RuboCop for all changed Ruby files
- Dry-run parsing of both supplied messages with synthetic assignment records
- `nix develop -c bundle exec rake spec`
- `nix develop -c bundle exec rubocop`
- `nix develop -c git commit -F /tmp/codex-vpsfree-abusix-commit.txt`
- Mandatory independent change review of commit `9d672dab`
- Review of the official XARF v3 shared, v4 core, and v4 messaging/spam schemas
- Focused RSpec and RuboCop after addressing review findings
- Full RSpec and RuboCop after addressing review findings
- Follow-up verification by the same mandatory reviewer on amended commit
  `50e8f420`
- `nix develop -c confctl build cz.vpsfree/vpsadmin/int.api1`
- `nix develop -c confctl build cz.vpsfree/vpsadmin/int.api2`
- `git fetch origin master`
- `nix develop -c git push -u origin 2026-08-19-abusix-reports`
- `nix develop -c gh run list --repo
  vpsfreecz/vpsfree-cz-configuration --branch
  2026-08-19-abusix-reports ...`

## Results

- The two messages are Abusix Global Reporting XARF v3 spam-trap reports sent
  through RT by the same exact originator.
- They report two different IPv4 sources in the vpsFree.cz allocation
  `37.205.8.0/21`, at `2026-08-17T20:59:40Z` and
  `2026-08-19T13:03:45Z`.
- Each JSON report contains a source IP, SMTP envelope sender, UTC event time,
  `Activity` / `Spam` / `Trap` classification, and a base64-encoded
  `message/rfc822` sample.
- The decoded samples contain four `Received` hops, repeat the reported source
  IP, align the visible and envelope sender domains, and show a passing DKIM
  result. Message bodies are explicitly redacted; one subject is present and
  the other is absent.
- Both reports use `Disclosure: false` and anonymized complainant metadata.
- Abusix emits the evidence as singular `Report.Sample`; the archived XARF v3
  schema describes plural `Report.Samples`.
- The current configuration does not match `Abuse Report: Spam`. Its existing
  `XArf` parser handles an older subject-driven text format and therefore cannot
  extract these JSON reports.
- Historical assignment ownership was not queried from production. The parser's
  existing time-aware assignment lookup is the correct final relevance gate.
- XARF is an open, sender-independent reporting format. Current v4 documentation
  explicitly distinguishes the reporter from the sending infrastructure and
  gives examples involving ISPs, brand-protection services, and national CERTs.
- XARF v3 and v4 use the same three-part email transport but incompatible JSON
  field layouts. A normalized decoder with version adapters can support both.
- The supplied RT exports contain passing SPF, DKIM, and DMARC results for the
  RT-generated vpsFree.cz wrapper. They do not provide a DKIM alignment proof
  tying the recorded RT originator to `abusix.com`, so JSON sender metadata must
  not be treated as authentication.
- XARF supports non-IP source identifiers, many abuse categories, and binary or
  sensitive evidence. Generic decoding is safe; unrestricted generic automatic
  forwarding is not.
- Worktree creation returned exit 1 because the ambient shell lacked the
  Bundler-managed Overcommit gems. The branch and worktree were created
  successfully. This is the known setup issue documented in
  `notes/vpsfree-cz-configuration/2026-06-13-overcommit-hooks-need-nix-develop.md`;
  hook commands must run through `nix develop`.
- The generic decoder accepts either XARF v3 or v4 and normalizes their
  incompatible layouts. The forwarding parser independently requires the
  Abusix RT originator, matching JSON sender domain, an allowed spam
  classification, an IP source, textual evidence, and a historical assignment.
- Synthetic fixtures cover Abusix's singular v3 `Report.Sample`, the standard
  plural `Report.Samples`, and a v4 IP-based spam report. No production report
  data was copied into the repository.
- Ruby 3.4 does not provide `base64` as a default gem in this development
  shell. Strict Base64 decoding therefore uses Ruby's built-in
  `String#unpack1('m0')`, avoiding a new dependency and lock-file change.
- Before review, the focused suite passed with 24 examples and the full suite
  passed with 36 examples. After review fixes, the focused suite passed with 27
  examples and the full suite passed with 39 examples. RuboCop inspected all 34
  Ruby files with no offenses in both runs.
- Both supplied messages were recognized as XARF v3 and each generated exactly
  one dry-run incident after registering a synthetic assignment for the
  reported address. No database lookup, incident write, or mail forwarding was
  performed.
- The member-facing incident text was reviewed under the workspace
  user-facing-writing rules. It states the source and evidence plainly and does
  not copy reporter, complainant, or sender contact metadata from the JSON.
- Initial commit `9d672dab7074f586d17fd449d3dde66699c06ebc` was amended after
  review. Commit `50e8f42020ffa2351e4ff14c06d864cf99241fb6` contains the
  complete repository change. Overcommit ran Nixfmt and RuboCop successfully on
  both commits; all pre-commit and commit-message hooks passed.
- The mandatory review found one Blocking issue: timestamps without an offset
  could be interpreted in the API process timezone and query the wrong
  historical assignment. The decoder now requires `Z` or a numeric UTC
  offset, with a regression test running under `Europe/Amsterdam`.
- The review also found one Important issue: the v4 policy accepted all
  `messaging/spam` channels and evidence sources while describing them as
  spam-trap email. The decoder now models protocol, source port, and evidence
  source. Automatic v4 forwarding requires SMTP, a spam-trap source, a valid
  source port, and an envelope sender. A schema-valid synthetic fixture and a
  rejected SMS user-complaint regression test cover the policy.
- The same independent reviewer verified amended commit `50e8f420`. Both
  original findings are resolved, four targeted examples passed, no directly
  related regression was found, and the feature is clear to proceed.
- `cz.vpsfree/vpsadmin/int.api1` built generation
  `2026-08-19--17-13-38` successfully.
- `cz.vpsfree/vpsadmin/int.api2` built generation
  `2026-08-19--17-15-29` successfully.
- A final fetch confirmed that `origin/master` remains at the reviewed base
  `3733ab8c71b8dcfa2ad29a22ca25ed8f3acc4615`.
- Branch `2026-08-19-abusix-reports` is pushed to the SSH origin at
  `50e8f42020ffa2351e4ff14c06d864cf99241fb6`.
- No GitHub Actions run was created for the branch. The repository's only
  workflow is the scheduled or manually dispatched dependency updater, so
  there is no push-triggered CI to monitor for this feature.

## Decisions and follow-up

- `Disclosure: false` is handled conservatively: the incident excludes all
  reporter, complainant, and sender contact metadata. Only the already-redacted
  textual evidence and fields needed by the responsible member are included.
- The initial forwarding allowlist contains only `support@abusix.com`, JSON
  sender domain `abusix.com`, XARF v3 `Activity/Spam/Trap`, and XARF v4
  `messaging/spam` over SMTP from a spam trap.
- Preserving an authenticated original-sender result in a trusted internal
  header remains a possible later hardening measure; it is not required for
  this deliberately narrow policy.

## Cleanup

- The supplied `.eml` files remain only under the ignored/untracked `tmp/`
  evidence directory and must not be committed.
- The feature worktree contains only generated, untracked development artifacts
  under `.bin/`, `.bundle/`, and `.rubocop_cache/`; all tracked files are
  committed and match the pushed branch.
- Keep the feature branch and worktree until the change is reviewed and
  integrated. Remove the worktree after merge; keep branch refs unless the user
  explicitly requests deletion.
