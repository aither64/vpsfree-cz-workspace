# Registry bootstrap and GitHub Actions publishing

The user selected GitHub Actions publication instead of local Cargo publication.
No registry upload or settings change has occurred. Architect-owned design
Clarification 6 specifies a workflow_dispatch release against a version tag,
explicit oidc/bootstrap selection, protected release environment and reuse of
the existing exact-revision CI workflow. Implementer3 is preparing that bounded
client change; HaveAPI release integration remains a recommendation only. The earlier local Cargo
login request is withdrawn. Default-branch integration remains unauthorized.

## vpsadmin-client on crates.io

Current [crates.io documentation](https://crates.io/docs/trusted-publishing)
requires an existing published crate before its owner can configure a trusted
publisher. The live documentation source was independently inspected in
[rust-lang/crates.io](https://github.com/rust-lang/crates.io/blob/main/svelte/src/routes/docs/trusted-publishing/+page.svelte).
The first publication needs an API token, but it may run in GitHub Actions;
it need not run on a local workstation. After the first successful upload,
register repository owner vpsfreecz, repository vpsadmin-rust-client, the chosen
workflow filename and matching release environment on the crate settings page.
Remove and revoke any one-time bootstrap token after configuring OIDC.

Subsequent publishing uses the official
[rust-lang/crates-io-auth-action](https://github.com/rust-lang/crates-io-auth-action)
to exchange GitHub OIDC identity for a short-lived Cargo token. Grant
id-token: write only to the publishing job, and bind it to the configured
workflow and release environment. A bootstrap mode must be an explicit operator
choice, never an automatic fallback when OIDC fails.

At inspection, crates.io returned 404 for vpsadmin-client and version 0.1.0.
Read-only GitHub API inspection also found no repository environments yet;
the protected release environment has not been configured. No Cargo credentials
are configured locally; this is no longer a local
credential request. Account-owner setup is needed for any protected Actions
bootstrap secret and later crates.io trusted-publisher registration.

## haveapi-rust-client on RubyGems

The generator is a Ruby gem, not a Rust crate. RubyGems supports
[pending trusted publishers for new gems](https://guides.rubygems.org/trusted-publishing/#pushing-a-new-gem-with-a-trusted-publisher).
A RubyGems account owner can register haveapi-rust-client with repository owner
vpsfreecz, repository haveapi, workflow release.yml, environment release before
the gem exists. The first OIDC-authenticated push creates the gem and establishes
ownership; no bootstrap API token is necessary.

HaveAPI's committed release.yml already grants id-token: write to its protected
release job and configures RubyGems OIDC. Its artifact inventory and build loop
currently include haveapi-client, haveapi and haveapi-go-client, not the Rust
generator. Add the generator to that existing release contract rather than
creating an unrelated publisher. Its source gem version is 0.29.0 and it depends
on haveapi-client ~> 0.29.0. Exact shared release preparation is a separate action:
the existing pipeline publishes other gems, npm and the PHP mirror too. The user
has asked about the generator mechanism, not authorized a full HaveAPI release.

## README readiness

Committed user-facing rewrite: c4a0f597cd3602e28ae11846962e2d1e07a0c1ff.
Independent review found no Blocking/Important issues; its one Advisory about
relative packaged links was fixed with absolute retained feature URLs and
accepted by direct diff inspection. Fresh cargo publish --dry-run passed exit
zero in 34 seconds at this exact clean head. See final-review-readme-release.md
and artifacts/readme-cargo-dry-run/result.json. No archive upload occurred.

## Prepared client workflow

The draft adds .github/workflows/release.yml and reuses ci.yml via workflow_call.
Run it explicitly against a version tag with authentication=bootstrap for the
first crate upload, or authentication=oidc for later releases. The latter is
the default; OIDC errors do not select bootstrap automatically. The workflow
checks repository/package/tag/version and commit binding, and gives publishing
credentials only to the protected release job after CI. The main-agent writing
pass is complete on docs/development.md. Committed as 091bd70954d270f3e575a71a8a5a1884eed2eccd. Quick static and
26 gate checks passed. Independent four-lane review completed with no findings;
feature publication completed normally at 091bd70, with exact-head CI run
39318944837 passed all four jobs, confirmed by a fresh utility. Direct Git comparison confirms README, source, schema, manifests,
locks, toolchain, examples and tests unchanged from the clean Cargo dry-run head.
No workflow dispatch, tag creation or release
upload has occurred. The final reviewed client branch has four logical commits:
handwritten package, generated source, user-focused README and Actions release.
No migrations or repeated update streams remain; the prior source reviews are
preserved. GitHub must have the dispatch workflow installed on main
and at its release tag; installing feature content on main still requires
explicit integration direction under workspace Git rules.
