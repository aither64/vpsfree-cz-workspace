# Aitherdev communication authorization rollout

Status: prepared design; activation, integration and release have not been
performed by architect0. The lead owns execution and updates this receipt.
See [design.md](design.md#aitherdev-rollout-addendum-2026-10-30) for packages and
invariants, [plan.md](plan.md) for the user brief, and [state.md](state.md) for
current progress.

## Authorization and ownership

User direction relayed in this conversation: “aitherdev can be deployed using
vpsfree-cz-configuration”, followed by “when deployed and verified, you can merge
it and release aitherdev”. Integration is conditional on successful deployed
verification and covers the feature in these exact repositories/targets:

| Registration | Canonical SSH repository | Target |
| --- | --- | --- |
| dev-workspace | `git@github.com:aither64/dev-workspace.git` | `refs/heads/master` |
| vpsfree-cz-configuration | `git@github.com:vpsfreecz/vpsfree-cz-configuration.git` | `refs/heads/master` |
| workspace | `git@github.com:aither64/vpsfree-cz-workspace.git` | `refs/heads/master` |

Physical machine ID and `profileMachine`: `vpsfree:aitherdev`; catalog key
`aitherdev`; aliases `aitherdev.int.vpsfree.cz` and
`cz.vpsfree/machines/aitherdev`. The latter is the configuration selector;
host target is `172.16.106.40`. Reserve this physical machine separately from
short repository merge claims. No actual-session grants, incident-private access,
forced idle, archive, delete or stop are authorized.

Architect identity was verified from own native context: thread
`01a189c3-501d-79a0-825b-1d9ddbb8c227`, `codex-lb`, `gpt-6-astra`, `xhigh`.
On resume, `dev-session current`, both environment identity values and roster
revision 27 matched. No settings were changed. Preserve provider and saved
model/effort/access for every retained member during activation.

## Recorded baseline and intended graph

| Item | Inspected identity |
| --- | --- |
| Selected profile output | `/nix/store/g650vgjpzvyifjmb1j44pc5bby3522z4-dev-workspace-0.2.0` |
| Selected derivation | `/nix/store/wxxdwf6ibjnhrfdvv3dx7gf2flhqp3x9-dev-workspace-0.2.0.drv` |
| Selected runtime source (`env.src`) | `/nix/store/wdh3nqarvakn0aqs3q4zw479v3lgjr2s-source` |
| Selected composed workspace source | `/nix/store/3ccam87ljbh4m00yjpz5d0zfm1r8l5x7-source` |
| Selected extension source | `/nix/store/lfmiclfqmpw7bs99lil6x5f83ba1j070-source` |
| Selected codex-web source | `/nix/store/4zsm43x32dilp195ai3yg9vcbsk1adbc-source` |
| Active assembled Codex | `/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0` |
| `/run/current-system` and `/nix/var/nix/profiles/system` | `/nix/store/r4rd3qyn52z1bipbln8kdh43mjd2wb1k-nixos-system-aitherdev-26.05.20261026.718f670` |
| Old generic runtime | `5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3` |
| Intended published runtime | `4155d0099d03028b43d5f08d225a88156cb4155a` |
| Configuration registered base | `b3b933bf6f9fc9f7f533b3f4e06775defd8879da` |
| Workspace registered base | `398dc7bab89ee51bcc77d23a5acc52c7e02878c1` |

All worktrees are under `worktrees/2026-10-29-cross-session-communication-authorization/`.
The lead reports both pin worktrees registered and clean. Configuration's earlier
post-checkout hook lacked pinned gems outside `nix develop`; D owns normal Nix
environment/hook preparation before commits, without bypass.

The selected runtime source NAR is
`sha256-+7fKx6VYAWRW2mzg8cQ1/+Kjz+Ye3p5xnEk6J1uptY4=`, equal to its old lock
identity. Full old graphs remain available in the selected composed source's
`flake.lock` (35 nodes, SHA256
`d716d6e88369ad456b825e350e40f6171da7852783b26cde2a7c1ed86ccdbd32`) and
configuration `b3b933bf6f9fc9f7f533b3f4e06775defd8879da:flake.lock` (64 nodes,
SHA256 `1bd193ffcf0041f45df62acb306a588be0398863692e2b1118c1b206f9d1c2f4`).
The inspected shared workspace lock at
`55a26f27e06d855176a8ae016a2f6bf23ece5f14` equals the selected composed lock;
that inspected tracking head is not the registered feature base.

Preserve extension `767dfd587e346168e1443e65ccdb67ce748f3fe3` / NAR
`sha256-om/+qNfQw6y74gjdzXfVG5AbHOQGysMefFZiqR92KP4=`, codex-web
`9d337b70987fdf1dd42a5d8efff31f755a122550`, and llm-agents
`91ff550fe42d4dd51dcf8b6bad87a0134fe7f314`. The separate configuration
llm-agents input has that same revision and remains unchanged. Workspace
`nixpkgs` follows `vpsfree-dev-workspace/nixpkgs`; runtime selection remains the
direct nested override. Compare complete semantic graphs, including follows,
locked hashes and sibling nodes, rather than only these prominent revisions.

Old-to-target runtime `nix/`, `libexec/`, both flake files and runtime contract
are unchanged. The selected contract also byte-equals target, SHA256
`f06f639a247b584a652777543c27284b1939bc8179ecfbbc1fe3299f4090b8a2`:
live-switch policy 1, reporting policy 2, communication policy 1, cluster
transition policy 3. Installed/current workspace `flake.nix`, `flake.lock`,
`.dev-workspace.json`, and agent-teams/coordination/integration configuration
match. This proves the present profile-only choice; final heads must retain it.

## Prepared sequence and evidence to fill

1. **Pins and quick checks.** D sets configuration channel
   `dev-workspace/devWorkspace` to target through `confctl ... set --commit` in
   its Nix shell. E changes workspace nested runtime URL and regenerates its lock
   with `nix flake update vpsfree-dev-workspace/dev-workspace`. Record each final
   base/head, generated diff and hooks. Run the matching deployment checker
   against both worktrees plus full graph comparison and relevant quick checks.
   Keep one logical update per pin stream; no host/provider/native edits.
2. **Review then build.** Apply final-review rules, including mechanical-pin
   disposition and whole-branch history/migration conclusion. Utility-build the
   committed composed workspace package and applicable checks after review.
   Record exact output, derivation, complete source/input graph, native executable
   and hash. Prepare any copies before a machine claim. Existing runtime
   review/native/CI evidence covers `4155d009`; distinguish that from new composed
   artifact evidence. No system build or activation is required on equality.
3. **Reserve and activate.** Inspect fresh baseline and acquire this session's
   exact `vpsfree:aitherdev` claim. Record claim ID and held status. Run ordinary
   `workspace-host switch --source WORKSPACE_FEATURE_PATH` with
   `DEV_WORKSPACE_CLAIM_ID`, the exact session slug, and
   `DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz`. Retain the
   same-native live path; do not stop sessions or bypass a refusal. If actual
   host/native requirements differ, stop and reassess rather than adding a
   system switch. When both ever need changes, site policy requires verified
   system activation before application selection.
4. **Deployed verification.** Prove selected profile equals prepared output and
   both system targets remain unchanged. Record live executable/native launch
   continuity separately from assembled package identity, portal/router health,
   own conversation continuity, naming availability, tool registration and
   unchanged codex-lb/member settings. Read only this session's live identity;
   do not probe incident conversations. Smoke the shipped tool/policy and retain
   the completed source-native exact-pair idle/steer/immediate-reply evidence.
   Existing tagged test is an in-process production worker, not the installed
   portal executable; state which installed artifacts each check executes.
   Lead accepts combined artifact/source/native proof on the unchanged graph.
   No new worker harness or provider/DeepSeek requests are required. If a concrete
   mismatch makes an installed-binary fixture materially necessary, use only
   owned unregistered roots/sockets/native/mock provider and refer the bounded
   addition through the lead. Preserve ordinary holds/revocation and avoid
   UI-cache freshness assertions. Never infer a grant between actual sessions.
   Retain teardown evidence for any owned fixture; no actual-session lifecycle
   cleanup.
5. **Conditional integration.** Only after step 4 succeeds, prepare fresh target
   refs and reviewed histories outside claims. Integrate runtime first, then
   matching configuration/workspace, each with one short repository claim,
   fresh target check, ordinary fast-forward/hooks, SSH push and remote proof.
   Shared workspace also requires the nonblocking tracking lock; if busy,
   release the repository claim. Release repository ownership before CI or
   records. Capture comparison after each final head change.
6. **Machine release.** Record fresh remote ancestry for the complete deployed
   lineage in all three defaults and reconcile command effects. For a pin-only
   clean refresh retain exact old/new base/head ranges, range-diff, package/input
   equivalence, migration evidence and independent conclusion. Do not call a
   nonancestor deployed SHA literally merged. A substantive successor needs a
   new verified deployment; ordinary completion still needs exact final heads.
   Inspect this session's exact machine claim, release when prerequisites hold,
   and confirm released status. No separate UI acceptance is needed; leave the
   session open and keep feature refs.

Execution fields pending: D/E final heads; review receipt; composed output/DRV
and full graph; build/check results; machine claim; activation result; postdeploy
fixture/live checks; final default heads and lineage; release result. These are
requirements for the lead's receipt, not claims that the operations occurred.

Recovery is forward-only. Preserve profile/native roots, journals, grants,
queued state and original saved delivery tuples. Establish effects after a
failed/uncertain switch and retry its supported forward path; do not erase
state, change stable message IDs, reset clusters or invoke an older package.
Keep the machine held while effects, verification or integrated lineage remain
unsettled. Releasing it grants no lifecycle permission.

Owning guides: workspace deployment/coordination procedures; selected
`workspace-host coordination guide`; configuration
`docs/operations/codex-providers-aitherdev.md`; runtime
`docs/session-communication-upgrade.md`, `docs/codex-package.md` and
`docs/workspace-portal.md` live-switch/recovery sections.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-29-cross-session-communication-authorization/

## Prepared final sources and review

D configuration b3b933bf..fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627 and E
workspace55a26f27..8302996e0f7e0ad0ce0e62fa02f7cc1afec2bf9a are committed,
published and clean. Complete semantic graph and normal hooks/check evidence is
in [D](rollout/config-pin-evidence.md) and [E](rollout/workspace-pin-evidence.md).
Both locks select4155d009 with unchanged siblings/follows/native inputs.
E's earlier398dc7b..bedbf9cd pin patch equals final55a..830; the baseline note
changes filtered source refs/DRV, so only final830 will be built and selected.

[Independent final rollout review](review-report-rollout.md), retained reviewer0
Sol/xhigh/codex-lb, found no findings. Mechanical-content exemption accepted;
whole-history/consolidation/no-migration and High-risk deployment contract
independently checked. Runtime source/reviews/native/CI are unchanged. Inherited
AGENTS-size check failure is byte-identical baseline behavior and excluded,
without claiming a pass or changing instructions. Exact-final package plus four
composition checks assigned fresh Luna/low composed_build, bounded20minutes.

Preactivation baseline is verification/predeploy-baseline.json. Native PID467324
and tmux wrapper PID435397 were active, selected profileg650, both system targets
r4rd3qyn. Own exact session remains codex-lb even though current workspace default
is openai; preserve both existing selections, do not switch provider. No machine
claim/activation/integration yet. Runtime detached merge target is
worktrees/2026-10-29-cross-session-communication-authorization/runtime-integration-target
at08f3dbb9; configuration prepared target/environment is in D receipt.

## Build and original activation

Exact830 composed package and four checks passed exit0,09:26:09Z–09:37:29Z
(11m20s). Actual DRVgia18wgbmc0ssxr81qykk076rmh0kl6d and output
/nix/store/d97nazmvhm2a2m3jn8ichid4ksannliq-dev-workspace-0.2.0 match final
evaluation. Outputs/root links and complete local Nix package/check logs are
retained under verification/. Main source is1jliyjqz4abknq16kwp8afw6m5k3yqqi;
native inputg69/output2rqw and executable SHA647b0157 remain exact.

Machine claim7bb60f85-6258-478f-b436-0af467b4144a acquired held09:38:06Z,
owner51dd7ad4-89e9-4ab3-ae9a-181dcec7266c; exact status rechecked before action.
Host is local aitherdev; package already local, no remote copy needed.
Lead launched ordinary guarded source switch09:38:57.109567Z with exact claim
and session environment. Original launcher880054/command880072 tracked in
rollout/activation-status.json and activation.log. Fresh standalone Luna/low
watcher01a18c2e-0cc0-76b2-b01d-484fb38472fa observes original status/log only;
no cancellation/retry/deploy authority. Activation acceptance is pending.

## Deployed acceptance

Original activation exited0 at09:40:03.170376Z (66.061s). Selected profile is
exact prepared d97. Native daemon467324 and tmux435397 retain original start/exe;
portal883089 and router883059 execute d97. Both system targets remain r4rd3qyn.
Direct and routed healthz pass. Naming child883327 uses unchanged native2rqw;
private cwd/listen socket and fixed catalog present with no new unavailable/exit
log. No naming/provider inference requested. Own exact six native settings rows
and roster match preactivation; own codex-lb and default openai both preserved.
Installed team-mcp initialize/tools-list passes corrected policy/schema assertions
in owned unregistered temp state; no host call/grant/provider request; fixture
exited and its owned data removed. Full evidence is verification/postdeploy-verification.json
and installed-tool-smoke.json. Retained source-native worker proof remains separate.

Lead accepts deployed usability within reviewed boundary. Conditional integration
approval is satisfied; integrate exact4155d009/fcc7fc97/8302996e defaults next,
under three separate short repository claims. Machine7bb60f85 remains held until
complete fresh remote lineage proof and settled effects, then release promptly.
Selected d97 coordination guide body equals previously fully read g650 guidance.

## Integration and mechanical refresh

Runtime4155d009 remote master verified; repository claim906b4760-2049-4b6b-8afb-560ffa71d11e
released09:45:17Z. Configurationfcc7fc97 remote master verified after normal
Nix/Overcommit environment FF and separately inspected push; claim
b9ca1918-f71a-4e7a-afb1-b0c8e8d90db4 released09:48:01Z. No CI/records under
repository ownership.

Workspace shared baseline advanced by automatic archive coordination commit
55a26f27->58989d3db45048560f3305bfac4470a579e1722e during build. No source
outside work/archive changed. E rebased original deployed55a..8302996e onto
589..4beddf77a8f9af1d926c5b48bd6ee4c84f439e85, preserving pin patch, full lock,
filtered source and native inputs. Final published head4bed is clean, one pin;
explicit final comparison captured. Lead independently reconstructed exact final
tree by applying original binary patch to new base using disposable GIT_INDEX_FILE.
Reconstruction tree6bcd7257a816e0ed7e72f7dd0eaf6f864ea8a7d4 equals final.
Fresh independent final Nix eval returns exact built/deployed gia18 DRV/d97 output;
matching checker pass, no new build or deployment needed for equal artifact.
See rollout/workspace-refresh-reconstruction.json and E receipt. Reviewer0 asked
for narrow independent final history/equivalence/no-migration mapping conclusion.
Original deployed830 is not literally merged; accepted equivalent successor
lineage will be recorded only after review and final remote proof.

## Final integration and release

[Independent refreshed-history conclusion](review-followup-rollout.md) accepted
589..4bed as an equivalent successor to deployed55a..830 with identical complete
patch, reconstructed tree and exact built/deployed artifact/input identity. No
new build/deployment/native check is required. Deployed830 remains nonancestor
and is not described as literally merged.

Workspace exact4beddf77a8f9af1d926c5b48bd6ee4c84f439e85 fast-forwarded under
claim9b8a0a78-8364-467f-87cb-286bad089660 and nonblocking tracking lock. Fresh
remote master/ancestry proved; repository ownership released09:54:40Z before
records. Fresh complete remote proof for runtime4155d009/configfcc7fc97/workspace4bed
and their full immutable input graphs is in rollout/final-lineage.json. All
registered exact final heads are integrated; no source successor needs deployment.

Machine claim7bb60f85-6258-478f-b436-0af467b4144a was inspected with exact
owner51dd7ad4-89e9-4ab3-ae9a-181dcec7266c, held solely for vpsfree:aitherdev.
Settled activation exit0, selected profile/native/system identity and healthy
portal were reconfirmed. Normal release completed; authoritative released status
verified at 2026-10-30T09:55:35Z. See rollout/machine-release.json. No claims remain owned
for this rollout; no further machine mutation was performed. The two temporary
merge targets were removed normally, while feature refs/registered worktrees and
this open session remain. No lifecycle cleanup was requested or invoked.
