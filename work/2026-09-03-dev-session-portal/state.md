---
lifecycle: active
---

# 2026-09-03-dev-session-portal

## Current status

The empty-thread correction is deployed and the user successfully created the
new `2026-09-04-testing` session, sent messages, and received Codex responses.
That live use exposed two follow-up defects: an empty Go pending-request slice
is encoded as JSON `null`, which Firefox cannot map, and attachment from a
normal shell derives `nil` from the absent `TMUX` value before calling
`empty?`. The portal also advertises `--as-is` even though exact known slugs are
already resolved without it. The next workspace correction will normalize
empty pending responses to `[]`, retain a browser compatibility fallback,
treat a missing caller socket as empty, and display the concise exact-slug
attach command. The host will install that command as `dev-session`, matching
`./bin/dev-session`; the separate `workspace-dev-session` name will be removed
because the user does not require backward compatibility. The live testing
session belongs to the user and will not be reset or recreated during this fix.
DNS is unchanged. The user also requested a full-width Codex view, so the
session page will use one top-level tab set for Codex, Handoff, Repositories,
Plan, State, and curated artifacts instead of a chat sidebar. The index will
list the newest dated sessions first. The final workspace input pin and
aitherdev configuration are committed and pushed. Quick tests, mandatory
review, full builds, the aitherdev-only switch, and read-only live validation
all pass. The user's `2026-09-04-testing` session and Codex history were not
mutated.

- Portal URL after deployment:
  `https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/`
- Workspace branch: `2026-09-03-dev-session-portal`.
- Configuration branch: `2026-09-03-dev-session-portal`.
- The configuration lock is the authority for the exact workspace revision
  selected through `aitherVpsfreeWorkspace`. Exact heads are reported at
  handoff rather than embedded in this same-repository tracking file.
- The Basic Auth password is prepared at
  `/home/aither/.local/state/vpsfree-workspace-portal/password`, owned by uid
  1000 at mode 0600. Its value has not been printed or recorded.
- Current Codex thread:
  `01a0678c-baae-7600-bcf6-9a0cb6c83232`.

## Repositories and worktrees

### Workspace

- Repository: `aither64/vpsfree-cz-workspace`
- Branch: `2026-09-03-dev-session-portal`
- Initial base: `ac651305d935e3e78768567b4f18b498037f985a`
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/workspace`
- Commit subjects:
  - `pki: add workspace portal certificate tooling`
  - `auth: add workspace portal password derivation`
  - `dev-session: share workspace sessions across clients`
  - `portal: add authenticated development interface`
  - `workspace: develop reusable changes on feature branches`
  - `review: standardize mandatory lanes on xhigh`
  - `docs: explain workspace portal operation`
  - `flake: package the workspace portal at its source`
  - `flake: make wrapped helpers activation-safe`
  - `portal: preserve origin on same-origin forms`
  - `portal: start initial turn before history materializes`
  - `portal: improve live session interaction`

### vpsfree-cz-configuration

- Repository: `vpsfreecz/vpsfree-cz-configuration`
- Branch: `2026-09-03-dev-session-portal`
- Initial base: `248e2fc614bb3bc29c0a9c9f910330ade0b3cb80`
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration`
- Commit subjects:
  - `inputs: add aither workspace source`
  - generated exact `aitherVpsfreeWorkspace` pins through the final workspace
    revision
  - `aitherdev: host authenticated development workspace portal`
  - `internal-dns: publish workspace portal`
  - `aitherdev: authorize local deployment key`
  - `aitherdev: expose one development session command`

The top-level shared checkout remains on `master`. Its unrelated modified
`AGENTS.md` and unrelated untracked files are preserved and are outside this
initiative.

## Supported design

- The workspace repository owns the Go portal, embedded responsive UI,
  `dev-session` integration, PKI/password helpers, handoff skill, documentation,
  and Nix package.
- The host package view excludes only the package's unfixed `dev-session`
  executable so the NixOS-configured wrapper can own that name. The unrelated
  `workspace-portal`, `workspace-pki`, and `workspace-portal-password-hash`
  commands remain installed globally.
- The portal validates active and archived manifests, renders sanitized
  tracking files and curated artifacts, and enriches repository entries with
  GitHub comparisons and workflow status.
- A root-supervised Codex App Server listens only on a local Unix socket. The
  portal and tmux terminal client share the same persisted thread. The App
  Server is never exposed on the network.
- Browser-created sessions use a retry-safe creation journal. Ready sessions
  reopen only their exact recorded thread. A creating, unsent session may
  reconcile the union of loaded and materialized threads for its canonical
  working directory, but a different candidate is accepted only while fresh
  and unmaterialized. Before the initial `turn/start`, a temporary schema-2
  manifest records the durable attempt; retries fail closed until exact history
  appears or an App Server restart permits a replacement. Terminal attach goes
  through `dev-session attach`, which reconciles the tmux client
  after an App Server restart.
- The initial and follow-up message limit is one shared 20,000-byte runtime
  contract. It also publishes worst-case form and JSON transport expansion;
  Ruby, Go, HTML, nginx, and their boundary tests consume that contract.
- The generated schema supplied by the configuration's normal `llm-agents`
  Codex package is checked against every App Server shape consumed by the
  adapter. An incompatible ordinary Codex update fails the aitherdev build;
  there is no initiative-specific Codex pin.
- nginx provides HTTPS and Basic Auth. Application mutations additionally
  require the exact HTTPS origin, responses use `Referrer-Policy: same-origin`
  so ordinary same-origin forms retain a verifiable origin without disclosing
  cross-origin referrer data, and all application responses are `no-store`.
- The custom CA and nginx key material are root-owned and absent from the Nix
  store. Certificate/key pairs are validated and switched atomically, with a
  predecessor retained. The packaged, directly tested reconciler updates its
  applied marker only after successful export and nginx reload, so partial
  failures retry.
- Only the VPN interface can reach the HTTPS listener. Internal DNS maps the
  portal name to aitherdev at `172.16.106.40`.
- The local ED25519 public key is a named configuration entry excluded from the
  broad `aither.all` set and authorized only for root on aitherdev. It enables
  later local confctl deployments after a one-time user bootstrap. The
  authorized-key record accepts only local source addresses and disables SSH
  forwarding and PTY features.
- Portal and Codex processes intentionally share the `aither` account that owns
  the deployment private key. Authenticated portal interaction is therefore
  effectively root command access to aitherdev after bootstrap; VPN reachability
  and Basic Auth are the controlling boundary.

## Compatibility and deployment

- Existing schema-1 manifests remain readable. Completed new sessions are also
  schema 1. Only an unresolved initial-goal delivery uses schema 2; an older
  portal rejects that in-flight state, so the corrected version must be
  redeployed before retrying it. Recorded Codex versions are diagnostic only,
  so compatible ordinary upgrades can resume old completed sessions.
- Portal status and local files remain available when GitHub or Codex is down;
  the unavailable integration is reported without failing the page.
- Active sessions compare live feature branches with repository default
  branches. Finalized sessions retain immutable comparison metadata and become
  read-only at the same URL.
- The CA, password, nginx password hash, portal state, and Codex state persist
  across ordinary NixOS redeployments and generation rollbacks.
- The initial deployment order was aitherdev first, then both DNS containers.
  Both DNS deployments are complete and stayed unchanged during the
  aitherdev-only corrections. Rollback uses ordinary previous NixOS/confctl
  generations. See `deployment.md` for CA trust removal, key-bootstrap rollback
  behavior, and compromise recovery.
- No persisted database, API, protocol between production services, or
  vpsAdminOS node format changes are involved. Mixed versions are safe because
  the portal and DNS entry are additive and a missing portal only makes the
  name unavailable.

## Verification

Completed on the committed interaction and layout follow-up:

- Workspace head: `b484025cf0221a5e26e7ce6e76495f10a535d385`.
- Configuration head: `56b91734e8c10d3417d85d4eea53489543f4bfa6`.
- All Go packages and Go vet passed. The tests cover JSON `[]` for no pending
  prompts, the browser fallback for a legacy `null`, the full-width tab
  structure, and dated newest-first ordering.
- The Ruby suite passed 128 runs and 1,004 assertions with no failures or
  errors; 10 real-tmux cases were intentionally skipped. The new test attaches
  an exact known slug from a shell with no `TMUX` environment value and without
  `--as-is`.
- Configuration Nix formatting and `nix flake check --no-build -L` passed
  after the final exact generated workspace input update. The first
  configuration commit attempt was correctly rejected because the ambient
  shell lacked `nixfmt`; rerunning inside `nix develop` ran the declared hook
  successfully.
- The first two exact pin attempts failed without changing the lock because
  GitHub's commit tarball endpoint had not exposed the just-pushed revision.
  Resolving the pushed feature branch populated the archive, and the required
  `confctl inputs channel set --commit` retry generated the final pin normally.
  The two superseded development pins were consolidated into one generated
  update from the previously deployed revision to the four focused final
  workspace commits.
- The first review pass required truly single-purpose workspace commits,
  retention of the unrelated global PKI/password helper commands, current
  non-mutating deployment instructions, complete rollback effects, and wider
  ordering coverage. The rewritten history and tracking resolve those
  findings. The ordering test now covers active-before-archived grouping,
  equal-time slug ties, and archived finalization metadata.

Completed for the interaction, command, ordering, and layout follow-up:

- `nix build .#workspace-portal --no-link -L` passed. The Codex protocol
  contract, all Go packages, 128 packaged dev-session tests, 14 PKI tests, and
  2 password tests passed. The output is
  `/nix/store/ww6k662i0wk1zjnii2q22g4ndqn4q18k-workspace-portal-0.1.0`.
- `confctl build -y cz.vpsfree/machines/aitherdev` passed and created
  generation `2026-09-04--21-24-39`. It built 18 expected portal and system
  derivations and did not compile a kernel.
- `confctl deploy -y cz.vpsfree/machines/aitherdev switch` completed. Its
  systemd and firewall checks both passed. `/run/current-system` and the system
  profile resolve to
  `/nix/store/1wx5h42ifsw1p2j2v22xpy3n926lk6n8-nixos-system-aitherdev-26.05.20260903.a5cc6f2`.
- nginx, the portal, Codex App Server, dedicated tmux server, and firewall are
  active; certificate renewal is enabled.
- `dev-session`, `workspace-portal`, `workspace-pki`, and
  `workspace-portal-password-hash` are present in the system path.
  `workspace-dev-session` is absent as requested. `dev-session validate`
  accepted all three live manifests, and exact dated slugs work without
  `--as-is` for both URL lookups.
- Authenticated read-only HTTPS checks confirmed the existing testing session's
  pending response is an array, its thread response is an object, the Codex
  panel is the default full-width tab, and its handoff shows
  `dev-session attach 2026-09-04-testing`. The index lists that session before
  this older initiative. The page has one external script and retains CSP,
  HSTS, no-store, and a 401 authentication boundary.
- A non-TTY `dev-session attach 2026-09-04-testing` reached tmux and failed at
  the expected terminal boundary without the former Ruby exception or a hang.
  An interactive terminal remains the appropriate place to attach.
- Final GitHub Actions queries found no runs for either branch, so no
  superseded runs needed cancellation.

Completed on the pushed empty-thread correction:

- Workspace head: `3c8de8bd55615cb594884945239dfa41d9b4782d`.
- Configuration head: `30f7feba2da65e577e5db3f314fc9c5e4dcb46f6`.
- All Go packages passed, including the black-box test against the exact Codex
  0.153 executable supplied by the development shell. That test confirms fresh
  metadata, loaded-thread recovery, first-turn materialization, exact paginated
  history, and exactly one persisted user request.
- Go vet and the generated App Server protocol contract passed. The contract
  includes loaded-thread pagination plus all metadata used for the fresh-thread
  proof.
- The Ruby suite passed 127 runs and 1,001 assertions with no failures or errors;
  10 real-tmux cases were intentionally skipped in the quick pass. It covers
  ready-thread authority, restart replacement, durable attempt state, stable
  schema-1 completion, the temporary schema-2 boundary, and shared schema
  fixtures consumed by both the Ruby and Go validators.
- `nix flake check --no-build -L` passed in the configuration worktree after
  the exact generated input pin was updated.
- The mandatory general-correctness, architecture, scope/compatibility, and
  failure-risk/security lanes all passed at `xhigh` with no remaining findings.
  Earlier passes found and drove fixes for ready-thread replacement, adoption
  of unrelated materialized candidates, duplicate initial delivery after a
  lost response, materialized empty history, rollback compatibility, and the
  duplicated Ruby/Go schema contract.

Completed by the final standalone package build:

- `nix develop -c bash -c 'cd portal && env GOFLAGS=-mod=mod go test
  ./internal/web'` passed. The explicit module mode avoids the development
  shell's vendor-mode default in a checkout without a vendor tree.
- `nix build .#workspace-portal --no-link -L`
  - generated Codex schema contract passed
  - all Go packages passed
  - 127 packaged dev-session tests and 1,000 assertions passed; 10 real-tmux
    cases were intentionally skipped by the package build
  - 14 PKI tests and 92 assertions passed, including failed CA export, failed
    nginx reload, retry, atomic marker publication, and inactive nginx
  - 2 password tests and 18 assertions passed
  - the three installed helpers start with an empty ambient `PATH`, and their
    hidden makeWrapper executables use direct Nix-store Ruby or Bash
    interpreters
  - output:
    `/nix/store/g324kfya7wkxg3rxplby5znmw3icxwqy-workspace-portal-0.1.0`

Completed on the current pushed configuration candidate:

- `nix flake check --no-build -L` passed.
- `named-checkzone vpsfree.cz configs/internal-dns/zone.vpsfree.cz.` loaded
  serial `2026090300` successfully. It reports the repository's existing
  `@fqdn@` template-name warning.
- The configured deployment-key fingerprint matches
  `/home/aither/.ssh/id_ed25519.pub`.
- The restricted authorized-key line parses with the same fingerprint, the
  local route to `172.16.106.40` selects that allowed source address, and the
  built root authorized-keys derivation contains the intended verbatim entry.
- Pre-bootstrap probes confirmed that the previous generation rejected the key
  for root SSH and that local non-interactive sudo needed a password. The user
  then deployed the key-bearing generation; restricted root SSH now succeeds.
- Feature-branch GitHub Actions queries returned no runs.

Completed for the currently deployed predecessor pin:

- `confctl build -y cz.vpsfree/machines/aitherdev` passed and created
  generation `2026-09-04--16-34-31`. It built only the expected portal and
  system derivations; no kernel compilation occurred.
- `confctl deploy -y cz.vpsfree/machines/aitherdev switch` completed, followed
  by two successful confctl health checks for overall systemd state and the
  firewall.
- Both `/nix/var/nix/profiles/system` and `/run/current-system` resolve to
  `/nix/store/rkmbm5s6h13f7xsg199iv9mrqfxp0flv-nixos-system-aitherdev-26.05.20260903.a5cc6f2`.
- nginx, the portal, Codex App Server, dedicated tmux server, renewal timer,
  and firewall are active. The configured package is the configuration-input
  output
  `/nix/store/av59vxr0pabqrpn73rmfjkxaal8sfx6i-workspace-portal-0.1.0`.
- Authentication state is `root:nginx` at modes 0750/0640. PKI authority state
  is `root:root` at mode 0700 with the CA key at 0600. nginx TLS state is
  `root:nginx` at mode 0750, with the leaf certificate at 0644 and key at
  0640. The public CA is `root:root` at mode 0644 beneath a 0755 directory.
- `workspace-pki verify` passed. Starting the certificate-renewal service again
  completed successfully without changing the certificate pair, and nginx
  reloaded successfully.
- Port 443 listens on `172.16.106.40`. The firewall contains only the intended
  portal acceptance rule from `172.16.107.0/24`; the NixOS module does not open
  the port generally.
- DNS resolves the portal hostname to `172.16.106.40`. With the public CA,
  unauthenticated and invalid-password requests both return 401, while valid
  authentication returns 200 for the portal root and this initiative page.
  Plain HTTP redirects with 301. No credential value or generated hash was
  printed.

Completed for the browser-origin fix:

- `confctl build -y cz.vpsfree/machines/aitherdev` passed and created
  generation `2026-09-04--17-48-49`. It built the expected portal and system
  derivations; no kernel compilation occurred.
- `confctl deploy -y cz.vpsfree/machines/aitherdev switch` completed and both
  confctl health checks passed: overall systemd state is running and the
  firewall service is active.
- Both `/nix/var/nix/profiles/system` and `/run/current-system` resolve to
  `/nix/store/xqd4iw8n2sh7y194bdqzvpnsb6j6wkal-nixos-system-aitherdev-26.05.20260903.a5cc6f2`.
  The live portal executable resolves beneath
  `/nix/store/i537whp14xs770627494428c0bnfrim4-workspace-portal-0.1.0`.
- nginx, the portal, Codex App Server, dedicated tmux server, renewal timer,
  and firewall are active. DNS still resolves the portal name to
  `172.16.106.40`.
- An authenticated HTTPS response sends `Referrer-Policy: same-origin` while
  preserving the existing no-store, CSP, and HSTS headers. Deliberately invalid
  session POSTs returned 403 for a missing Origin, literal `Origin: null`, and
  a foreign Origin. The exact portal Origin returned 400 from ordinary form
  validation, proving that it passed the CSRF boundary without creating a
  session. No credential value was printed.
- The then-installed `workspace-dev-session validate` accepted the
  initiative's portal manifest, and its URL command returned the stable
  initiative link.

Completed long configuration builds for the predecessor workspace pin, run
sequentially to avoid shared confctl log collisions:

- `confctl build -y cz.vpsfree/machines/aitherdev` passed and created
  generation `2026-09-04--15-48-25`. Linux was fetched from the binary cache;
  no local kernel compilation occurred.
- `confctl build -y cz.vpsfree/containers/prg/int.ns1` passed and created
  generation `2026-09-04--15-51-07`.
- `confctl build -y cz.vpsfree/containers/brq/int.ns1` passed and created
  generation `2026-09-04--15-52-05`.

Completed for the final empty-thread correction:

- `nix flake check --no-build -L` and
  `confctl build -y cz.vpsfree/machines/aitherdev` passed and created generation
  `2026-09-04--20-07-45`. The build contained 17 expected portal and system
  derivations and did not compile a kernel.
- `confctl deploy -y cz.vpsfree/machines/aitherdev switch` completed. Its
  systemd and firewall health checks both passed.
- Both `/nix/var/nix/profiles/system` and `/run/current-system` resolve to
  `/nix/store/hy7cj91l1m8f0js0nk0jy7ahgjfm5wpl-nixos-system-aitherdev-26.05.20260903.a5cc6f2`.
  The deployed portal executable resolves beneath
  `/nix/store/3py2zznrny0gc7f4952qmdm6xh0yf324-workspace-portal-0.1.0`.
- nginx, the portal, Codex App Server, dedicated tmux server, and firewall are
  active, and certificate renewal is enabled. Restricted root SSH succeeds.
- The then-installed `workspace-dev-session validate` accepted both existing
  portal manifests, and the URL helper returned this initiative's stable URL.
- DNS still resolves the portal name to `172.16.106.40`. With the custom CA,
  unauthenticated and deliberately invalid authentication return 401, while
  valid authentication returns 200 for the root and initiative pages.
- Missing, literal `null`, and foreign origins return 403 for deliberately
  invalid session POSTs. The exact HTTPS portal origin reaches ordinary form
  validation and returns 400, proving the CSRF boundary accepts it without
  creating a session.
- Live responses contain the expected no-store, HSTS, same-origin referrer,
  and strict `script-src 'self'` headers. The initiative page loads the
  reachable `/static/app.js` asset externally and contains no inline script.
- Final GitHub Actions queries found no workflow runs for either feature
  branch, so there were no superseded runs to cancel.

The user subsequently created a working `2026-09-04-testing` session and used
its shared Codex thread from the browser. That live session is user data and
must remain untouched while the pending-response, terminal-attachment, layout,
and ordering corrections are deployed. Installing the public CA on any
remaining client devices remains user-owned.

## Browser CSP diagnosis

Firefox reported a blocked inline-script hash when opening the initiative page.
The live HTML response contains no inline script: its only script element is
`<script src="/static/app.js" defer>`. The page and JavaScript asset both return
the intended `script-src 'self'` policy, the asset is served as JavaScript with
`nosniff`, and the portal's own external script remains allowed. The blocked
inline body was therefore injected on the client side, most commonly by a
browser extension or browser customization. The CSP remains unchanged so the
portal does not authorize unknown injected code. If portal behavior is broken
rather than merely accompanied by a console warning, capture the console
entry's source attribution and reproduce in an extension-free browser profile.

## First deployment diagnosis

- Restricted root SSH with `/home/aither/.ssh/id_ed25519` succeeds after the
  bootstrap deployment.
- `workspace-portal`, `workspace-codex-app-server`, the dedicated tmux server,
  and the renewal timer are active.
- `/run/current-system` stayed on the previous generation because activation
  failed before its final update, while the system profile and systemd units
  point at the new candidate.
- The installed makeWrapper launchers have store-path Bash shebangs, but their
  hidden `.workspace-*-wrapped` executables retain portable `/usr/bin/env`
  shebangs. The password helper is the first such executable and cannot find
  Bash in activation's deliberately minimal path.
- No workspace PKI, nginx TLS, or public CA directories were created. nginx is
  failed with a missing
  `/var/lib/vpsfree-workspace-portal-tls/current/server.pem` error.

## Current-session runtime handoff

This initiative began before the supervised portal runtime was deployed. Its
manifest has a historical thread ID but no endpoint provenance or managed tmux
authority. The status page, comparisons, workflows, and files are available,
but the portal correctly keeps this thread non-interactive.

After deployment, `dev-session start
2026-09-03-dev-session-portal --as-is --no-attach --json` attempted to import
the historical thread. The supervised App Server refused because this running
Codex process already owns the thread's active writer. The command did not
change the manifest or create a tmux session. Once the original writer is no
longer active, the same command can resume the thread and add trusted runtime
provenance. New sessions created in the portal or through `dev-session start`
use the shared App Server and tmux runtime from the outset and do not have this
legacy handoff condition.

## Mandatory change review

The interaction, command, ordering, and layout follow-up was reviewed at
`xhigh`, never max or ultra. Architecture passed on the first run. General,
Scope/Compatibility, and Failure-Risk/Security found issues that were resolved
before their clean reruns:

- the four workspace commits are independently reviewable and revertible;
- the ordering test covers active and archived grouping plus deterministic
  ties;
- the global package view preserves the PKI and password-hash helpers while
  replacing only the session command;
- deployment instructions describe the pending aitherdev-only switch and
  non-mutating validation of the user's existing live session;
- rollback documentation includes the defects, command rename, ordering, and
  layout effects.

All four final lanes report no Blocking, Important, or Advisory findings for
workspace `b484025c` and configuration `56b91734`.

The final full review used fresh `gpt-5.6-sol` reviewers at xhigh, never max or
ultra. Its General, Architecture, Scope, and Risk lanes reviewed workspace
`ed58a077` and configuration `4022ff8d`.

Resolved Blocking and Important findings:

- split the password helper from the PKI commit;
- changed all displayed attach commands to the reconciliation wrapper;
- published the 20,000-byte request boundary as one cross-layer contract;
- replaced permanent nginx restart behavior with a one-time restart trigger;
- persisted the last successfully applied TLS target so failed exports or
  reloads retry;
- corrected and condensed operator tracking to the supported implementation.

Resolved low-cost advisory work adds permanent CA decommission and compromise
recovery instructions. The in-memory GitHub/session caches remain intentionally
unbounded because this is a single-user, VPN-only service with a small set of
workspace initiatives. The native ChatGPT section remains because the user
explicitly asked about desktop and mobile access; it clearly describes a
separate SSH-based workflow rather than claiming access to the portal thread.

The first remediation rerun reviewed workspace `0ae37664` and configuration
`5d4e9eaf` with fresh General, Architecture, and Risk xhigh lanes. It found:

- the workspace branch needed rebasing after tracking advanced `master`;
- the review-effort policy needed its own commit;
- percent-encoded form and escaped JSON requests could hit independent
  transport caps below the semantic message limit;
- `thread/start` had to verify its returned working directory before sending
  the initial turn;
- the TLS applied-marker retry state machine needed direct regression tests.

The branch is rebased, the policy commit is split, transport ceilings and all
numeric messages derive from the runtime contract, `thread/start` validates
the returned cwd, and the tested PKI reconciler now owns the export/reload
state machine.

The next General rerun reviewed workspace `71e04754` and configuration
`f04ea365`. It confirmed the durable current-path, Git-index, and Git-history
slug tombstone behavior with no Blocking or Important findings. Its two
Advisories were fixed in the owning `dev-session` commit: invalid
`--json --attach` input is rejected before any creation side effect, and the
index-only tombstone path has direct regression coverage.

The final General and first Risk reruns reviewed workspace `7e626dd4` and
configuration `69d60c27`, including the dedicated aitherdev deployment key.
The General bootstrap finding is resolved by the explicit one-time user
deployment and this updated tracking. Risk review additionally required the
pre-key rollback reconnect failure and authorization-removal behavior to be
documented; `deployment.md` now records both. A final security-only Risk rerun
reviewed configuration `6f5ce257` after the key was restricted to local source
addresses and cleared with no Blocking, Important, or Advisory findings. All
review work used fresh `gpt-5.6-sol` reviewers at xhigh, never max or ultra.

The activation-shebang remediation review classified the change as High risk
because it affects root host activation, deployment retry behavior, and
persistent authentication and PKI state. Fresh General, Architecture, Scope,
and Risk reviewers used `gpt-5.6-sol` at xhigh to review workspace `ba54a9a`
and configuration `27059095`.

- No lane found a Blocking implementation issue.
- Scope and Risk found the active deployment runbook's pre-bootstrap and DNS
  instructions Important because following them would assign already-complete
  work to the user and expand the current recovery beyond aitherdev. The
  runbook and plan now record the completed bootstrap and DNS deployments and
  limit remediation deployment to aitherdev. This tracking-only correction did
  not require a reviewer rerun.
- General, Architecture, and Scope noted stale predecessor package evidence in
  this state file. It now records the corrected standalone package output and
  distinguishes the earlier long configuration builds from the pending
  current-pin build.
- Architecture advised consolidating the finite three-helper catalog. Scope
  recommended keeping the explicit helper-specific interpreter and expected
  CLI checks because a registry would add indirection without reducing current
  risk; that proportionality decision is accepted.
- Risk additionally built the workspace package with the configuration's
  followed inputs at
  `/nix/store/av59vxr0pabqrpn73rmfjkxaal8sfx6i-workspace-portal-0.1.0`.
  Build-time checks passed. Temporary live aitherdev probes ran the installed
  password and PKI helpers with `PATH=/empty` without displaying credentials,
  reloading services, or changing persistent portal state.
- At review completion, the remaining gaps were the current-pin aitherdev build
  and switch, generation convergence, protected credential and PKI state,
  service health, HTTPS and Basic Auth, VPN reachability, and the
  browser/terminal shared-thread smoke test. All are now verified as recorded
  above except client CA installation and the shared-thread client smoke test.

The browser-origin remediation review also classified the change as High risk
because it affects the CSRF mutation boundary and the deployed host service.
Fresh General, Architecture, Scope, and Risk reviewers used `gpt-5.6-sol` at
xhigh. No lane found a Blocking implementation issue. General, Architecture,
and Risk found no Important issue. Scope found that the runbook and current
status still described the predecessor generation as fully current; those
files now explicitly keep the aitherdev origin-fix build, switch, and live
validation pending while leaving DNS unchanged. Risk advised direct coverage
of the incident's literal `Origin: null`; that regression assertion was added,
the focused and full package tests passed, and a fresh Risk rerun cleared with
no Blocking, Important, or Advisory findings. The real-browser form submission
remains part of the post-deployment smoke test because the repository's browser
contract test supplies Origin explicitly.

## Handoff and cleanup

- User deployment instructions: `deployment.md`.
- Reusable first-input bootstrap lesson:
  `notes/vpsfree-cz-configuration/2026-09-04-confctl-add-new-input.md`.
- Reusable local deployment-key bootstrap and rollback lesson:
  `notes/vpsfree-cz-configuration/2026-09-04-aitherdev-self-deploy-key-bootstrap.md`.
- Keep both feature branches after integration unless the user explicitly asks
  for deletion.
- Do not finalize or archive this initiative until deployment, CA installation,
  live smoke tests, and worktree cleanup are complete.
