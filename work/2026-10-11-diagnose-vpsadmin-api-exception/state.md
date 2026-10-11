---
lifecycle: active
---

# 2026-10-11-diagnose-vpsadmin-api-exception

## Status

- Requested diagnosis complete: HaveAPI 0.29.8 was published without generated
  documentation. A crawler requested the advertised JSON schema page; its
  unguarded file read raised `Errno::ENOENT` and triggered ExceptionMailer.
- The matching local Nix package and published gem independently confirm the
  missing files. See [findings](findings.md).
- No application code was edited, independently reviewed, released or deployed.
- Session remains open with `lifecycle: active` for follow-up.

## Phase checklist

- [x] Verify exact session identity and retained roster.
- [x] Extract sanitized request and exception evidence.
- [x] Trace the route and release packaging at `v0.29.8`.
- [x] Inspect the matching installed package and published gem.
- [x] Recommend the packaging fix, defensive behavior and regression checks.
- [x] Reconcile investigation records and portal artifact.
- Independent final review and long integration tests: not applicable to
  routine investigation and evidence; no substantive implementation deliverable.

## Next actions

If implementation is requested, make documentation generation mandatory before
gem packaging, add packaged-artifact checks and a narrow missing-file response,
then follow the normal independent review and release process. No investigation
blocker remains.

## Documentation

- [Plan and scope](plan.md)
- [Findings and proposed solution](findings.md)
- Portal: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-11-diagnose-vpsadmin-api-exception/>
- No project documentation changed because only diagnosis was requested.

## Repositories

Read-only references: canonical `repos/haveapi.git`, tag `v0.29.8` (commit
`22fae15`), and `repos/vpsadmin.git`, local `origin/master` API gemset. No feature
branches or worktrees were created or registered.

## Commands run

- `dev-session current`: matches both environment markers and the trusted
  thread binding for this exact workspace and slug.
- `dev-session team list 2026-10-11-diagnose-vpsadmin-api-exception --as-is`:
  retained Lead and reviewer preset; `reviewer0` is ready, read-only, Astra/xhigh.
  No review assignment was made for routine findings.
- Read the email with Python's MIME/HTML parsers, outputting only the exception,
  first relevant stack frames and whitelisted request fields.
- Read tagged release and route source using Git's bare-repository commands.
- List documentation in the exact Nix package named in the email.
- Download the published `haveapi-0.29.8.gem` into memory and inspect its nested
  tar members without extracting or retaining the artifact.
- Inspect shared workspace status/index and declared hook configuration before
  the owned tracking commit. No hook framework is declared in this workspace.
- `dev-session url ... --as-is`: stable portal link recorded above.

## Results

- Email date: 2026-10-11 21:12:14 +0200; request is `GET /doc/json-schema`.
- User agent identifies itself as PetalBot; identity is not independently proven.
- Exact installed `server.rb:536` reads absent `doc/json-schema.html`.
- Both installed and published package documentation contain only `hooks.erb`
  and `index.md`; protocol/client pages are also absent.
- Published gem SHA256:
  `8e362aef9e6b1c77233ee53bb1237056b2e15abcba9b2ef5b3d188a1dd9ec1e7`.
- The release target has no documentation prerequisite. The doc task generates
  the missing HTML and copies shared docs; the gemspec includes those files only
  if already present when packaging.
- Existing documentation specs do not exercise the missing JSON schema page.

## Open questions

The specific release operator's command history was not inspected. The package
omission and clean-source release weakness are established independently of
that history. No live production response, repair or rollout was checked.

## Cleanup

The input email stays in its original upload location outside version control.
Downloaded package bytes were inspected in memory only. No infrastructure or
session lifecycle operation was performed.
