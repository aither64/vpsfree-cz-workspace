# Registry readiness audit

Read-only investigation by implementer1 on 2026-10-22. Public registry requests
were made without authentication at 14:36:57–14:37:51 UTC, with the actual Cargo
package rechecked at 14:55:09 UTC. The session command
and both environment markers matched `2026-10-22-haveapi-release` and
`/home/aither/workspace/ai/vpsfree.cz`. No application files, Git refs, registry
settings or publications were changed; no publishing credential was read.

## Package inventory and observed state

Architect0 confirmed the HaveAPI destinations against `origin/master`
`a32b15e`. The Rust generator is a Ruby gem; its embedded runtime is not an
independent crates.io dependency. The user's clarified repository,
`vpsadmin-rust-client`, is a separate generated-client release scope. Architect0
subsequently verified its live `main` (`945af6a`): its actual Cargo package is
**`vpsadmin-client` 0.1.0**, imported as `vpsadmin_client`. Preserve this name;
the repository basename is not the registry package name.

| Registry | Package | Public API observation | Evidence |
| --- | --- | --- | --- |
| RubyGems | `haveapi` | HTTP 200; latest `0.29.12`, created 2026-10-19 19:49:02 UTC | [Gem JSON](https://rubygems.org/api/v1/gems/haveapi.json) |
| RubyGems | `haveapi-client` | HTTP 200; latest `0.29.12`, created 2026-10-19 19:48:55 UTC | [Gem JSON](https://rubygems.org/api/v1/gems/haveapi-client.json) |
| RubyGems | `haveapi-go-client` | HTTP 200; latest `0.29.12`, created 2026-10-19 19:49:08 UTC | [Gem JSON](https://rubygems.org/api/v1/gems/haveapi-go-client.json) |
| RubyGems | `haveapi-rust-client` | HTTP 404; body says gem could not be found | [Gem JSON](https://rubygems.org/api/v1/gems/haveapi-rust-client.json) |
| npm | `haveapi-client` | HTTP 200; `latest=0.29.12`, published 2026-10-19 19:50:12 UTC; 78 versions, no `0.30.0` | [Package JSON](https://registry.npmjs.org/haveapi-client) |
| PyPI | `haveapi-client` | HTTP 404; `{"message":"Not Found"}` | [Project JSON](https://pypi.org/pypi/haveapi-client/json) |
| crates.io | `vpsadmin-client` | HTTP 404 at 14:55:09 UTC; actual Cargo target; error says crate does not exist | [Crate JSON](https://crates.io/api/v1/crates/vpsadmin-client) |
| crates.io | `vpsadmin-rust-client` | HTTP 404 at 14:37:51 UTC; original requested/repository-name lookup, not the Cargo target | [Crate JSON](https://crates.io/api/v1/crates/vpsadmin-rust-client) |
| crates.io | `haveapi-runtime-tests` | HTTP 404; error says crate does not exist; not a publication target | [Crate JSON](https://crates.io/api/v1/crates/haveapi-runtime-tests) |

The npm metadata identifies `git+https://github.com/vpsfreecz/haveapi.git`,
directory `clients/js`, and public maintainer username `aither64`. This supports
the package/repository identity; it does not prove present account access or
publisher configuration. A 404 establishes the observed absence of a public
package response, not account ownership, name reservation or permission to
register that name. Recheck all release destinations immediately before an
authorized publication.

## HaveAPI trusted-publisher registrations

These are required identities to confirm with the registry account owner.
Actual account-side registration status is unobserved, so these are a readiness
checklist rather than a claim that each entry is missing.

| Registry / project | Registration route | GitHub owner | Repository | Workflow filename | Environment |
| --- | --- | --- | --- | --- | --- |
| RubyGems `haveapi` | Existing gem → Trusted publishers | `vpsfreecz` | `haveapi` | `release.yml` | `release` |
| RubyGems `haveapi-client` | Existing gem → Trusted publishers | `vpsfreecz` | `haveapi` | `release.yml` | `release` |
| RubyGems `haveapi-go-client` | Existing gem → Trusted publishers | `vpsfreecz` | `haveapi` | `release.yml` | `release` |
| RubyGems `haveapi-rust-client` | Account pending trusted publisher; gem name `haveapi-rust-client` | `vpsfreecz` | `haveapi` | `release.yml` | `release` |
| npm `haveapi-client` | Existing package Settings → Trusted publishing; provider GitHub Actions | `vpsfreecz` | `haveapi` | `release.yml` | `release` |
| PyPI `haveapi-client` | Account Publishing → pending publisher; project name `haveapi-client` | `vpsfreecz` | `haveapi` | `release.yml` | `release` |

Use the filename `release.yml`, not `.github/workflows/release.yml`, in registry
forms. It identifies that path in the repository. The publishing job must use
the matching `release` environment and `id-token: write`. Repository-local
instructions additionally require approval through a protected GitHub `release`
environment. The workflow must include the Rust gem before a registration can
lead to its publication; architect0 owns that integration design.

### RubyGems first release

RubyGems supports publishing a brand-new gem through a pending trusted publisher:
no manually published seed version or long-lived RubyGems token is required.
Use the [account pending-publisher page](https://rubygems.org/profile/oidc/pending_trusted_publishers)
and enter gem name `haveapi-rust-client` plus the tuple above. Leave optional
Workflow Repository Owner/Name fields blank for a workflow in the same
repository. First successful push converts the pending entry to a regular
publisher and makes the configuring account an owner. Existing gems require
their owner to register the publisher separately for each gem. The pending
page redirected unauthenticated browsing to sign-in; no account entries were
observed. [Authoritative guide](https://guides.rubygems.org/trusted-publishing/).

### PyPI first release

Use the account's Publishing page to add a pending publisher, supplying project
name `haveapi-client` and the HaveAPI tuple above. First upload creates the
project and converts the entry to a normal publisher; no manual seed upload is
needed. A pending publisher does not reserve the project name and is invalidated
if another user registers it first. The account registering this pending
publisher needs to be the intended initial project owner. Existing-project
configuration uses the project's Manage → Publishing page. TestPyPI needs its
own setup. [Pending-project guide](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/),
[GitHub publisher fields](https://docs.pypi.org/trusted-publishers/adding-a-publisher/).

### npm readiness constraints

The npm package already exists, so no first-package bootstrap is needed.
Configure or confirm the HaveAPI tuple in its package settings. Permit direct
`npm publish`, which the current HaveAPI release procedure uses; a new entry's
default staged-publishing permission alone is insufficient. Newly created
publisher entries must complete their first successful publish within **2 days**
or expire; expired entries must be recreated. Do not create a new entry too far
ahead of the authorized release. Field values are case-sensitive and the
workflow file must exist. Current minimums are npm 11.5.1 and Node 22.14.0.
GitHub-hosted runners are supported; self-hosted runners are not. The package's
`repository.url` must identify the publishing GitHub repository. Public metadata
currently points to HaveAPI. Account-side configuration is not validated merely
by saving its form. [Authoritative npm guide](https://docs.npmjs.com/trusted-publishers/).

## Separate crates.io bootstrap: vpsadmin-client

The current crates.io documentation requires an already published crate and
crate ownership before adding a trusted publisher. **Its first publication
requires an API token.** Pending publishers cannot bootstrap this name through
the documented process. The Cargo guide also requires a crates.io account with
a verified email address; new names are allocated on first publication.
The supplied local token's account, scopes, expiry and ability to create this
crate were not inspected. [Cargo first-publication guide](https://doc.rust-lang.org/cargo/reference/publishing.html).

After an explicitly authorized, verified first release, the owner can configure
Settings → Trusted Publishing with GitHub repository owner, repository name,
workflow filename and optional environment. Architect0 subsequently confirmed
the existing downstream source tuple: owner `vpsfreecz`, repository
`vpsadmin-rust-client`, workflow filename `release.yml`, environment `release`.
The source workflow's explicit `authentication=bootstrap` mode uses protected
environment secret `CARGO_PUBLISH_BOOTSTRAP_TOKEN`; subsequent `oidc` mode has no
token fallback. These are source requirements, not proof that the account-side
publisher or secret exists or works. No token was read. OIDC publication needs
`id-token: write` and an identity
exchange such as the official crates.io authentication action. Current registry
policy also supports trusted-publishing-only mode and blocks
`pull_request_target` and `workflow_run` triggers.

The [live trusted-publishing page](https://crates.io/docs/trusted-publishing)
rendered only a JavaScript-required message to the public text browser. Its
current authoritative [website source](https://github.com/rust-lang/crates.io/blob/b92b83f173d5ff02183d45ed0623c1bf34d39cf9/svelte/src/routes/docs/trusted-publishing/+page.svelte)
was read directly and contains the first-publication prerequisite and exact
GitHub fields. The file's latest commit was `b92b83f173d5ff02183d45ed0623c1bf34d39cf9`
(2026-10-02). The [2026-01 crates.io update](https://blog.rust-lang.org/2026/01/21/crates-io-development-update/)
supports the trigger restrictions and trusted-publishing-only setting.

See the architect-owned
[downstream source readiness audit](vpsadmin-rust-client-readiness.md) for exact
source and dependency graphs, current CI and GitHub environment observations.

HaveAPI's `clients/rust/runtime/Cargo.toml` declares `haveapi-runtime-tests`
`0.1.0` with `publish = false`. Its maintained runtime source is copied into
generated clients. Publishing `haveapi-rust-client` to RubyGems therefore does
not require any crates.io bootstrap or token. See HaveAPI's
`clients/rust/docs/releasing.md` and `clients/rust/runtime/README.md`.

## Remaining account/operator evidence

- Registry account ownership and permission to manage the existing packages;
  actual existing/pending publisher entries, their exact tuple and npm expiry.
- PyPI/RubyGems acceptance of the new names under the intended owner account.
- crates.io bootstrap token readiness and account-side publisher/secret setup
  for generated package `vpsadmin-client` from repository `vpsadmin-rust-client`;
  architect/lead own final source provenance and release dependency evidence.
- GitHub required reviewers, allowed tag rules, publication enablement and PHP
  mirror deploy-key/webhook readiness. These are outside this registry account
  audit; the lead/architect's release-process evidence owns them.

No account configuration, first upload, release tag or publication has been
attempted. No application test was necessary for this read-only evidence
package. The lead owns the state/manifest summary and any later implementation
assignment. This investigation alone does not trigger final deliverable review.
