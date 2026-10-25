# Current outcome: vpsAdmin Rust client0.1.0 published and verified

The requested regeneration and publication are complete. HaveAPI0.30.1 drives
savedAPI7.0; all686generatedRustfiles remainedbyteidentical. Final SDKsource
b6f84679d33ff041388535dcf4dc060aeb0d1b9d, annotatedv0.1.0
77b40d42f1f4a882f1454d6f39c977f66d67ad1f, successfulnativepublish run40133192469/1.
[Public crate](https://crates.io/crates/vpsadmin-client/0.1.0) and
[docs.rs](https://docs.rs/vpsadmin-client/0.1.0/vpsadmin_client/) independently
confirmed; publicoriginalarchive matches actualnativepublish andcandidate.
[Lead acceptance](vpsadmin-client-0.1.0-release-lead-acceptance.json) binds allproof.

Architect0 designed, implementer3 ownedsource/Git/nativechecks/releases, reviewer0
independentlyreviewedcommittedwholehistory/affectedrepair, implementer1 performed
independentpublicverification, implementer2 configuredreviewedprotectedenvironment;
leadownedprose/acceptance/coordination. LibraryCargo.lock ignored; actualnative
runlocks retained. User explicitlyapproved movingunpublishedv0.1.0 toreviewedfix
and retryafteremailverification. Oldtag/source/failures/approvals remainpreserved.
No SDKmainintegration granted; that feature remainsunmerged. Sessionactive/open,
no lifecycle/deployment/cleanupaction. HaveAPI0.30.1 also fullyreleased/verified.

The remaining text records historical scope and decisions rather than pending
release work. Currentstatus/ownership is at topofstate.md.

# 2026-10-22-haveapi-release

## Current direction: remove library locks, backport and release0.30.1

The user explicitly authorized actual lockfile removal, master integration,
backport to haveapi-0.30 and publication of0.30.1. This supersedes previous
release/removal holds. Use accepted architect brief library-lockfile-policy.md
(authority-only revision1405e27b), parallel disjoint implementation owners0/1/2/3,
focused quick checks, independent committed final review and one authoritative
affected release build per changed candidate. Preserve old91 and original
artifacts. No additional user permission gate for these authorized actions.
No deployment, cleanup or lifecycle action.


## Current authorized work: instruction update, then lockfile policy follow-up

The explicit HaveAPI instruction update is complete: master7ac977a2 contains
the no-library-lockfiles/application-locks-permitted rule after normal hooks,
independent general review and verified FF integration/claim release. Existing
locks/workflows remain unchanged; broader removal is still a prepared design.

New user steering: library components should not track dependency lockfiles;
applications may. Architect0 prepares the exact removal and build/version/release
plan, including retaining the private Rust runtime test harness lock when
classified as an application. Owner0 implements only after accepted design.
Supported integration of the existing candidate is held; new affected checks,
review and candidate evidence follow source changes. Existing91 evidence stays
immutable. No unrelated dependency update or publication is authorized.


The latest user direction authorizes the completed HaveAPI master integration,
backporting all fixes and dependency updates to `haveapi-0.30`, and preparing
0.30.1 with the refreshed changelog date. Candidate `91d4293e` has passed quick
checks, independent whole-release review, actual Go/Rust version checks and all
ten CI workflows. Lead accepted the retained build artifacts and all 3,211 final
dossier entries. Implementer0 prepares the supported target and ordinary hooks
outside any claim, then performs the approved fast-forward and SSH push under a
short claim after concrete preparation acceptance. No tag, registry publication,
deployment or lifecycle action is included. Earlier holds below are history.


## Current authorized work: dependency refresh; 0.30.1 held

Latest steering: the user held the release, requested dependency updates authored
by us instead of accepting a new Dependabot PR, and questioned old selected
versions. Keep 0.30.1 tagging/publication held. Architect0's accepted
[dependency brief](dependency-refresh-addendum.md) selects current Markdown15/
anchor10/linkify6 and Rollup4.65.0, with TypeScript6.0.3 retaining required ES5.
Owner1 implements in haveapi-dependency-refresh; owner3 independently crosschecks
the frozen candidate; owner0 owns Git; reviewer0 reviews the committed full range
before affected longer checks. Lead owns final prose, acceptance and coordination;
owner2 prepares the post-review verification package. Publish our development
branch and inspect exact-head automatic CI after review and affected checks.
New default integration and release resumption remain separate held decisions.
Preserve completed integrations and all evidence; leave the bot PR untouched.

## Additional request: vpsAdmin SDK and client-example configuration

The final [simplification design](client-example-profile-simplification-design.md)
is accepted for implementation in a separate HaveAPI feature worktree from4dc0:
owner0 server/profiles/templates/docs/shared tests and Git, owner2 Go adapter,
owner3 Rust factories/model and specs, owner1 exact setup/verification preparation.
Optional versions and automatic current-schema descriptions are the default;
legacy file forms are preserved. Quick-tested complete source and lead prose
precede commits, whole-range independent final review and longer acceptance.
This changes HaveAPI support first; no vpsAdmin deployment or release resumption.

Follow-up user steering asks for a simpler contract: optional generator_version
defaulting to the API's HaveAPI version, reconsidering external saved-schema
paths and explaining/removing unnecessary Rust generator-config requirements.
Architect0 investigates a proposed simplified interface from actual loader/
adapter/render lifecycles, with current-user authorization and generator-owned
names preserved. Lead explains the concrete tradeoff and recommendation; no
application implementation or release resumption is inferred from the questions.

Additional user request: show how vpsAdmin API would enable Go and Rust client
examples and how its SDKs are configured. Architect0 investigates current
canonical HaveAPI/vpsAdmin/SDK source and writes a concrete configuration design
with actual names, revisions, required API changes and checks. Lead owns the
explanation. This read-only design package adds vpsAdmin/SDK source inspection;
it does not authorize live API/schema refresh, production deployment or default
integration. Dependency verification continues while 0.30.1 stays held.

## Held release authorization and completed default integrations

The user requested “let's release haveapi 0.30.1 with the fixes, to see if the
release issues are solved”, then explicitly approved merging the HaveAPI fixes
into master first and merging vpsadmin-rust-client as well. This authorizes the
reviewed HaveAPI090a integration into master, reviewed downstreamff876abe into
main, and normal HaveAPI0.30.1 patch release on supported haveapi-0.30, including
tagging and publication through the protected release workflow. It does not
authorize Rust crate publication, credential/configuration changes or session
lifecycle actions. Preserve published0.30.0 and all prior artifacts/refs.

Architect0 owns the release/input/verification brief before new metadata edits.
Implementer0 owns serialized Git, short separate repository merge claims,
release-worktree cherry-picks, version metadata and later tag/branch operations.
Lead owns CHANGELOG/release prose and acceptance. Implementer2 owns publication
prerequisite/recovery preparation; implementer1 owns independent final public
destination verification against the original0.30.1 artifacts. All intended
release changes must be committed and quick-checked, then independently reviewed
before long release verification. Never repeat an uncertain accepted upload or
replace original artifacts. Successful clean publication validates this actual
release; bounded delayed-visibility/recovery behavior also retains its fake-test
evidence rather than requiring manufactured production failures.

## Current authorized work: regenerate vpsadmin-client

After the HaveAPI follow-up branch passed review, local verification and CI,
the user explicitly said “okay, regenerate the client”. Regenerate the downstream
`vpsfreecz/vpsadmin-rust-client` repository (Cargo package `vpsadmin-client`)
with fixed HaveAPI commit `090a188cb4ef3477324718627f4ae3415d1c0975`, preserving
the saved API schema and current crate version. Use a new registered worktree
and development branch from freshly verified `origin/main`; no other session's
worktree or private evidence. The generated runtime is embedded, so another
HaveAPI registry release is not required.

Architect0 owns the exact design/input/surface compatibility brief before
implementation. Implementer0 owns worktree preparation and serialized Git;
implementer3 is the intended regeneration owner. Delegate an independent bounded
surface comparison if useful. Separate generator configuration/provenance and
mechanically generated output purposes as owning rules require. Commit and
quick-check all intended changes, independently review the complete new branch,
then run longer Cargo/MSRV/regeneration/package verification with a fresh pinned
watcher and push/check development CI. No live API refresh, version bump,
default integration, release tag, token/configuration change or crates.io upload
is authorized. HaveAPI follow-up and official0.30.0 bytes/refs stay untouched.

## Goal

Prepare HaveAPI 0.30, the first release containing rewritten JavaScript
clients, the Rust client generator and Python client. Audit release processes,
prepare version metadata and release documentation, verify package artifacts,
and identify exact pending trusted-publisher registrations.

## Affected repositories

- `haveapi`: release metadata, packaging, workflows and release documentation.
- `vpsadmin-rust-client`: user clarified the crates.io token is intended for
  this generated client; audit its owning repository, preparation and release
  dependency graph alongside HaveAPI. Owner is `vpsfreecz/vpsadmin-rust-client`,
  default branch `main`; actual Cargo package is `vpsadmin-client` 0.1.0.
  Preserve that package name; the repository name is not the crate name.
- Workspace: this session's coordination records only. Downstream generator pin
  and generated source refresh are now authorized by the current regeneration
  request; historical release-preparation scope below is retained as context.

## Approach

1. Architect audits current release paths, compatibility, package names and
   registry bootstrap constraints, then records the design and execution packages.
2. Implementers prepare independent release packages with serialized Git work.
3. Commit intended changes, pass quick checks, inventory the complete branch,
   and run independent final review before longer verification.
4. Publish the development branch and provide an actionable release checklist,
   trusted-publisher reminder, verification results and remaining operator steps.

## Decisions

- User explicitly requested the final commit message to be exactly
  `Version 0.30.0`; keep the coherent version commit last after new feature
  commits/history consolidation, retaining prior verification receipts.
- User explicitly requested removing the inactive File system example format
  from generated server API documentation to save space. Implement this bounded
  removal after exact-head verification ends; retain the filesystem client itself.
  User subsequently approved implementation with "Implement the plan"; the
  plan-first hold is revoked for the approved four-package scope.

- This request authorizes release preparation. Default-branch integration needs
  explicit direction for the repository and target under workspace rules.
- No registry publication, release tags or GitHub release publication during
  preparation. Describe the concrete ready result before asking for any final
  release/integration direction that is required.
- A crates.io credential is available locally. Never include its value in
  output, notes, prompts or commits; use only if an authorized registry action
  actually requires it.
- HaveAPI's Rust generator is the Ruby gem `haveapi-rust-client`; its runtime
  is embedded in generated crates and is not separately published. The supplied
  crates.io credential concerns `vpsadmin-rust-client`, per the user's correction.
- Carry forward three already-released 0.29.12 fixes absent from development
  master: structured API example validation, generated-example syntax checks,
  and nested PHP example values. Preserve provenance and prevent a 0.30
  regression rather than treating them as new features.
- Retain the current session and saved team settings; leave the session open.

## Compatibility and deployment

Assess package version alignment, generated clients and runtime dependencies,
JavaScript upgrade behavior, Python/Rust minimum versions and first publication
ordering. Preserve old-client/server compatibility and document intentional
breaks. No production deployment or database change is planned.

## Documentation

- User additionally requested a plan for generated server API examples covering
  Go, Rust async/blocking, Python sync/async, JavaScript callback/async and
  TypeScript callback/async. Architect owns
  `api-doc-client-examples-plan.md`. User approved the final plan. Four implementers own shared infrastructure,
  dynamic variants, Go and Rust respectively; architect records the final
  interfaces before substantive work.

- Readers: release operator, SDK consumers and future maintainers.
- Repeatable release instructions belong in HaveAPI; exact release evidence and
  pending registry registrations belong in this session.
- Lead owns final user-facing release prose after technical facts are settled.

## Testing plan

Use HaveAPI's declared Nix environment, hooks and release checks. Quick checks
must precede committed-deliverable review; longer builds/tests use a fresh
utility watcher. Validate package contents and dry-run paths without publishing.

## 2026-10-24 integration and patch-release direction

After the completed profile deliverable passes committed final review and affected
verification, integrate the HaveAPI fixes and dependency updates into master.
Then backport the accepted final changes to haveapi-0.30 with cherry-pick -x,
prepare shared version0.30.1 and refresh its changelog date to the actual
preparation date. Architect0 owns the ordering/compatibility brief;0 retains sole
Git ownership. Required review, exact-head checks and short merge claims remain.
This is preparation and integration authorization, without tag or registry
publication. Preserve already merged downstream lineage and all original release
artifacts. Session stays open.

## Accepted metadata recovery, 2026-10-24

The maintained version target stopped after twelve intended version fields at
an empty-cache uv metadata miss. Accepted [native recovery design](release-0-30-1-uv-recovery-design.md)
preserves that partial state. Owner1 prepares one fresh native online dry-run /
offline shadow proof with all26 external records unchanged; owner0 alone resumes
the maintained target under a new attempt after lead accepts the proof. No source
reset, constraint change, manual lock/cache edit or online live-patch fallback.
Current preparation/integration authority excludes tags and publication.

Metadata recovery is complete: native offline shadow proof accepted, one maintained
target retry succeeded, and exact18 version paths plus datedCHANGELOG19th yielded.
Owner1 now prepares only required Python/Gooptional/combined environments while
owner0 holds source. Quicks/normal commit precede final whole-range review and
actual-version acceptance/build. Original failures and metadata recovery history
remain in session records; no product or dependency-constraint repair was needed.

Independent whole-release review at91d4293e/tree61152a51 completed/all4lanes/no
findings; supported090a boundary and no-migrations/consolidation independently
confirmed. ActualGo/Rustsubset77c1cfa1 now follows; candidatepublication/build
preparation staysdisabled until itsacceptance. No duplicatefullsource/MSRV/model
campaign, tag/publication or sessionlifecycle action is authorized.
