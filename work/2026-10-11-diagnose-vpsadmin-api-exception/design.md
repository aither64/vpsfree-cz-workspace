# HaveAPI generated documentation repair

## Scope, ownership and boundaries

Lead owns substantive design and implementation (Sol/xhigh). First deliverable
is the HaveAPI development-branch fix, tests, CI and developer guidance. Stop
after independent review and verification for the user's review. Backport,
release, vpsAdmin dependencies and configuration updates are later phases.
Deployment belongs to the user. No automatic design/implementation specialists.

## Interfaces and files

- Root Makefile: `release: doc` generates documents before any release recipe.
- Ruby server Rakefile: `build` depends on a documentation check that rejects
  missing/empty copied or generated docs with guidance to run root `make doc`.
  Do not enforce this in gemspec evaluation: clean Bundler setup must work.
- Ruby server `server.rb`: catch only `Errno::ENOENT` from the JSON-schema
  `File.read`, returning 404. Keep template and other request failures visible.
- Documentation/ExceptionMailer specs: populated routes return HTML 200;
  missing JSON schema returns 404 and never triggers exception mail.
- Packaging specs: build a real gem, extract it into an owned temporary dir,
  assert required doc content, then launch a subprocess using extracted HaveAPI
  rather than source. Verify its load location and the three repaired routes.
- Server RSpec workflow/shared job: generate docs before server specs and run
  packaging checks; trigger on Makefile, shared source docs, copy script and the
  shared workflow. Preserve current action versions unless an edit requires
  verification and updating them under workspace rules.
- Developer development/release procedures: explain canonical build ordering,
  direct-build failure and artifact-based verification. Generated docs remain
  untracked; include the copied typed-input guide in component ignore rules.

## Invariants and failure behavior

Shipping generated documentation is the primary fix. A defensive 404 does not
replace the package check. Required docs include JSON schema HTML, protocol and
client-creation Markdown, the typed-input guide and copied protocol image.
Generation errors stop the release. The direct Rake build check runs before
packaging, while existing gemspec document inclusion remains valid. Missing
docs must not break bundle install or unrelated development tasks.

Build tests must not accidentally validate a source checkout, stale gem or
untracked-only code. Packaging fixtures use explicitly owned temporary dirs;
never delete actual worktree documents to simulate omissions. Child dependency
resolution may reuse installed development dependencies, but the HaveAPI load
path must resolve exclusively to the extracted artifact. Mail tests intercept
delivery locally, preserve hook listeners and do not contact SMTP.

## Compatibility, deployment and recovery

Only a missing documentation resource changes from exception/500 to 404.
Existing document routes and content retain their public shape. No database,
schema, migrations, persisted state, API action, generated client, daemon
protocol, CLI, Terraform or NixOS option changes. Mixed API/node versions work
normally; no coordinated node updates or data conversion are needed.

After user review, cherry-pick functional changes to the latest 0.29 branch,
version and publish through the normal approved workflow, then update vpsAdmin
and the `vpsadminServices` configuration input. The user deploys. Rolling back
the service/configuration revision restores previous doc behavior without state
conversion. Retain previous channel revisions in session handoff evidence.

## Acceptance and checks

Quick checks before committed final review: Ruby syntax, changed-file RuboCop,
workflow validation, focused docs and mail specs, direct-build guard cases and
gem content/extracted-route checks when known quick. Required Overcommit hooks
must pass; inspect/sign changed hook config instead of bypassing it.

Longer checks after final review: full server RSpec suite, clean generated-doc
packaging verification, exact-head server CI across supported Ruby versions.
Use a fresh Luna/low utility watcher for each long/uncertain operation. No full
client matrix or production requests are needed for this server-only fix unless
the changed shared workflow or resulting CI selects those existing checks.

Before readiness, inventory complete base-to-head commits/diff and state there
are no migrations, superseded approaches or repeated dependency-pin streams.
Retained reviewer independently assesses those conclusions. Record all actual
results and unresolved gaps in state, then stop for the user's review.
