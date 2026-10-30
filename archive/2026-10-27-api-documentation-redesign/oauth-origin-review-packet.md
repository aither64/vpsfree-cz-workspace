# Final affected review: native documentation form Origin

The user explicitly requested deployment to the development cluster. Deployment
of reviewed consumer59d/HaveAPI511 succeeded, and real HTTPS sign-in works.
Normal Chromium Switch user then returned403 with a valid documentation cookie,
matching CSRF nonce and parsed scalar switch field, but `Origin: null`. The
source's uniform `no-referrer` document policy conflicts with Fetch's Origin
generation for native form navigation. This packet covers the bounded owning
correction, not another full product campaign or permission to merge/release.

Session: `2026-10-27-api-documentation-redesign`.
Repository: HaveAPI, canonical `git@github.com:vpsfreecz/haveapi.git`.
Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi`.
Plan/state/design are in this packet's directory. Read the final design section
“Final devtrial OAuth correction — native form Origin and referrer policy”.

## Committed correction and final history

Checked sidecar: `6f7aa4449759260e6095870ffccb2fd0870284d6`, on original
`fb07c1378e4267bdfd54fa8fbfcfc57b6ec53413`, final tree
`e526e62753d6c18218074995761a944e6e61bdd5`.
Three paths, +105/-7:

- `servers/ruby/lib/haveapi/documentation_oauth.rb`: documentation authenticate
  explicitly selects strict-origin; existing private helper defaults to
  no-referrer for OAuth responses. Production delta is three changed lines.
- `servers/ruby/spec/documentation/oauth_spec.rb`: owning regression coverage,
  using existing Rack/provider/session helpers.
- `doc/documentation-oauth.md`: one precise policy/privacy paragraph, authored
  by main after applying the required writing skill.

Final folded head: `2f6c18a80f3a5f8ce46449ff81183b100b60f34c`, tree
`e526e62753d6c18218074995761a944e6e61bdd5`, exact checked sidecar tree.
Final three groups are Core51073383 (unchanged), Optional
`78ab264add97495aa38ffb33800f16cc9870838d` (tree
`6329fa36a7e730bb785d1cc64bcde1ffb2c7da04`), Performance2f6c18a8.
Owner2 explicitly released Source/Git/hooks before receipt prose; no active or
uncertain effect. Ordinary two rewritten-commit hook sets passed, no Core
recommit. History evidence:
`history-m8-oauth-fold-20261029t101802z/{before-move.json,completion.json,committed-Optional.json,committed-Performance.json}`.
Old-to-new Optional and Performance each differ by identical accepted three-path
patch SHA256 `9ddbb27e0d6c4be48d24de239834e194eb96d863f5be1b5c4a7d420c1e9b5a82`.
Final base aggregate SHA256
`9f9231d0dbdb3066d44f87f61e9a3ee6a9634b07c6acfbb2adcf4a8bd258eeb7` is byte-exact
to checked sidecar; all148 changed paths remain the old inventory, no additions.
Base is `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`.
Original accepted groups:

1. Core `51073383f063abbc24bf19ca669b9b6e46bb9555`, which must remain exact.
2. Optional `2462dfbac4921e15619ce17736bde9931f6d3fac`, owner of all three paths.
3. Performance `fb07c1378e4267bdfd54fa8fbfcfc57b6ec53413`.

The correction is folded into Optional with exact Performance patch replay and
verbatim original messages. Sidecar tree/aggregate equality and full base-to-head
path-set correspondence must be proven. Original148 paths gain no unrelated
path: these three paths were already in the complete branch inventory. No
migrations, dependency/channel/input update streams, versions or locks change.
Independently verify whole-history correspondence and migration/stream
conclusions, reusing earlier whole-branch findings only within their proven
unchanged scope. Original deployed511/oldfb07 and accepted sidecar references
remain recoverable. A nonancestor511 is not described as literally merged.

## Acceptance and compatibility

Documentation responses use `strict-origin`. Login/callback/logout, redirects,
errors and failures retain `no-referrer`; cache headers/search-index exception
retain existing behavior. Strict-origin sends at most scheme/host/port and
suppresses HTTPS downgrade referrers. It deliberately permits origin disclosure
to eligible HTTPS destinations, with no document path/query disclosure.

Preserve exact configured HTTPS Origin, valid encrypted documentation session,
constant-time CSRF, strict scalar switch parsing, cookie flags/mount/host-only
scope, R1 callback preservation, revoke/clear/login ordering and honest502.
Absent/null/foreign/wrong-scheme/wrong-port Origins remain403 without logout
effects. No Referer/Sec-Fetch fallback or forged Origin. Ordinary API/OPTIONS
authentication and documentation-cookie isolation stay intact. No provider,
parser, cookie format, config or JavaScript change.

Existing sessions/private config/client credentials remain compatible; an old
tab needs navigation/reload to receive the new document policy. Rollback restores
the previous browser defect without a data migration. The substantive header
change requires fresh consumer pin/package/deployment, rather than relabelling
the existing511 output. Peer owns that deployment and real Chromium acceptance;
no peer-private worktree/team/transcript access is granted by this packet.

## Verification and documentation

Owner4 receipt: `verification/oauth-origin-correction-fb07/receipt.md` and its
`commit-receipt.json`, `doc-copy.json`, `oauth-spec.log` and `commit.log`.
Focused existing `bundle exec rspec spec/documentation/oauth_spec.rb`:80/0,
seed16029,7.06s plus1.23s load. Changed Ruby lint2 files clean; whitespace and
ordinary mandatory pre-commit/commit-message hooks pass. Existing rooted Ruby
and frozen server bundle reused without dependency installation/graph change.

Regressions cover signed-in/out documentation root/version/resource/authdoc
GET/HEAD policy, sensitive OAuth redirects/refusals/failures, both ordinary
logout encodings, native URL-encoded switch, and absent/null/foreign/wrong-scheme/
wrong-port Origin refusal with valid session+CSRF, no revoke/cookieclear and
preserved session. Existing parser/wrong-CSRF/API/OPTIONS/R1/revoke502 coverage
remains. Rack supplies test headers; it does not establish browser-generated
Origin. Final actual Chromium proof of policy, native POST Origin, revoke,
sign-out/switch/expiry/relogin and logging remains after reviewed deployment.

One ordinary `make doc` ran before specs; only ignored packaged OAuth guide
changed, equal to source guide, SHA256
`cd890eb49bcb371d3e484d95ecc1341ecbfccbecbe70e1b6088edbcf1971768d`.
Other905 source entries, protected2148 inputs,23roots and prior docs preserved.
The intentional guide copy delta is accounted explicitly rather than hidden
behind an all-inputs-unchanged assertion.

Earlier fb07 all11CI/package payloads, actual511 native/MSRV, e5ea/a06b installed/
browser checks and direct-f6 timing remain at their actual revisions/scopes.
Direct-f6 remains8PASS/6INCONCLUSIVE timing, all14 deterministic/allocation PASS;
this correction does not trigger another measurement campaign. No blanket final
head pass, release publication, default integration or production acceptance.

## Reviewer selection and lanes

Overall HIGH risk: authentication response/browser security boundary and
cross-project deployment. Retain independent reviewer0, review/read_only,
saved `gpt-6.1-sol`/xhigh, without overrides. Apply mandatory-change-review skill
and all four full references: general; architecture and repetition; scope and
proportionality; risk and compatibility. Perform review directly without nested
reviewers. Start with scope, concrete failure and proportionality, then inspect
committed delta, owning context, tests, guide, exact final history and evidence.
Earlier product review does not prejudge this correction. Report findings by
severity and give explicit history/migration/update-stream conclusions and
residual browser/deployment limits. Remain read-only; no tests/browser/HTTP,
source/Git/service/lifecycle or peer actions.
