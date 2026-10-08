# Executed file-link rollout

Status: host and matching application deployed; live acceptance passed.
All three exact feature heads are merged and pushed; master CI passed both jobs.
No work or deployment blocker remains.

## Exact published, reviewed and deployed heads

- Runtime: 9e8e6e87a5a4844d4639ddf4008de483d1897f4c.
- Workspace composition: 70035dfe565058054e30efe2562c655c80dd183c.
- Host configuration: 5447020fccf99705e65a907cfe6e80684a5a1577.

Both downstream pins select the identical runtime. The final deployment contract
passed. Extension0ff827df, Codex, Nixpkgs and siblings retain their exact prior
identities. No migrations, state conversions or coordinated node updates exist.
The user directed implementation and continuation of deployment in this thread,
then approved the three master integrations with "merge". No archive, deletion
or forced interruption was requested.

## Deployment and selected generations

Host configuration was built and deployed from its feature worktree using
confctl deploy --yes --no-interactive --dry-activate-first
cz.vpsfree/machines/aitherdev switch. Named unit
file-links-host-deploy-20261007-retry.service, invocation
442d8d65749443fe9fdd2ad8ce0de6f6, passed in 92s. Both confctl health checks
passed; host-deploy.log/.exit record completion.

The application was activated separately from the workspace feature worktree
through the stable workspace-host switch --source command. Successful unit
file-links-application-deploy-20261007-retry2.service, invocation
9f10480eab0947c9a06c1fbf6e0e3e18, finished with ExecMainStatus 0 and atomic
application-deploy.exit 0. ExecMainCode 1 is normal CLD_EXITED. Normal generation,
cluster, session, team, protocol and semantic registration checks remained in
effect. The launcher restored terminal clients normally.

Selected host:
/nix/store/gknwlgf8v3lhva6yr1ky8c367fi3sqn2-nixos-system-aitherdev-26.05.20261006.b253099.
Selected application:
/nix/store/y0j44svpcdpqzvjj43n5kg06iqfnxvzv-dev-workspace-0.2.0.
The portal, compatible Codex App Server and router are active/running. No pending
Codex transition or deployment process remains; deployment-status.json records
current observations. Completed transient units remain for evidence.

Previous host:
/nix/store/r3c1kcrjmqgq48vjsvkmz3nwkzj6hggy-nixos-system-aitherdev-26.05.20261006.b253099.
Previous application:
/nix/store/b2q12p1725bqrb4nrd6yfjg28hgsggcf-dev-workspace-0.2.0.
These paths are recovery evidence. Profile transitions remain forward-only:
repeat an interrupted supported switch to the same candidate or select a reviewed
newer package. Do not relink profiles, rewrite private transition records, force
idle or select an older application package.

The prepared deployment wrapper required the exact previous application profile;
a rerun after this successful activation correctly refuses at that guard. It is
an execution record, not the procedure for a future transition. No retry remains.

## Verification and live acceptance

Final runtime flake check passed in 675s, including local VM smoke 257s. Composed
check passed in 634s; exact aitherdev build passed in 119s. CI 37586905151 succeeded
at runtime 9e8e6e8; fast passed and feature host job skipped. Local VM checks
passed independently. All final *-9e8e6e8.exit are 0. Independent final review
found no findings and explicitly verified complete histories and no migrations.
Portal validation passed 239 manifests before activation and handoff.

The guarded run-live-acceptance.sh passed in 4s after verifying literal session,
exact selected profile, host and final product heads. Fresh operation utility
file_link_live_verified_watch executed the exact prepared command; the lead
interpreted its evidence and visually checked shared-file-viewer.png.

- CA-verified authenticated API: all 15 checks passed. Original absolute
  lifecycle.md:93 URL 302 to canonical viewer 200, current file text equal to
  the shared document, authentication and excluded/untracked rejection, existing
  session redirects and source API. live-verification.json.
- Real Chromium browser: line 93 selected in the real read-only editor, copy link,
  actual gutter click and hash to 94, missing-line notice and selection clearing,
  restored line 93, AGENTS and existing session viewer, size/binary notices,
  no page errors. live-browser-verification.json and shared-file-viewer.png.
- Browser development-certificate exception is recorded explicitly and backed
  by the separate CA-verified API check. Credentials stayed in script memory,
  without argv, logs or artifacts containing them.

live-acceptance.log/.exit preserve full final results, exit 0. Product heads did
not change during deployment or live fixture correction; final worktrees are
clean and match published feature tracking refs.

## Resolved intermediate failures and evidence

The first host wrapper omitted Git from its service PATH and stopped before any
deployment. Verified store paths fixed the wrapper. host-deploy.*.first retains
that attempt. No source change or skipped hook was used.

Initial application attempts refused before profile selection while the unrelated
2026-10-05-network-ipv4-left-counter root and later implementer were active.
The helper restored quiesced terminals; none was interrupted or forced idle.
application-deploy.*.first and *.retry1 retain those attempts. Root-only idle
proof does not establish full-team readiness.

A standalone readiness watcher later lacked DEV_WORKSPACE_CODEX_HOME and could
not prove an archived member. That read-only loop was explicitly cancelled,
with no other process touched. The normal launcher supplies the correct state
context and completed the subsequent deployment. Readiness logs/JSON retain
this incomplete observation rather than classifying it as a deployment failure.

Initial browser fixture used a role selector that excluded CodeMirror's visible
aria-hidden gutter. DOM diagnosis found exactly one visible link 94, with the
expected URL and bounds. Adding includeHidden to the fixture selector preserved
all actual click/navigation assertions. Final acceptance passed. Failure and
cause remain in live-acceptance.*.first and live-browser-diagnostic.json/PNG.
This changed no product code or reviewed branch head.

Two earlier packaged-check baseline failures were reproduced and fixed before
final review/checks: lifecycle receipt contention and a timestamp-changing
archived observation fixture. Historical checkpoints and logs preserve the
source/fixture evidence; no production protection or assertion was suppressed.

## Remaining verification

All three master integrations are approved and complete at the exact reviewed
heads. Master CI 37607262893 passed fast and host at exact runtime 9e8e6e8 in
11m 1s, with watch exit 0 and no running operation. master-ci.json/.log/.exit
record the result. The deployed fix passed live acceptance. No verification
remains; feature branches and worktrees remain retained.

## Approved exact-head integration

The user subsequently said "merge" for the three named master targets. All
were fast-forwarded and pushed over SSH at their exact reviewed/deployed heads,
without rebase or source changes. Integration browser and deployment contracts
passed. Both clean temporary target checkouts were removed; feature refs and
checkouts retained. integration-proof.json records remote heads and preservation
of 86 unrelated shared-root modified files/index entries. Master CI 37607262893
passed; deployed profile and prior live acceptance remain unchanged. Lifecycle
is complete, with no archive or deletion requested.
