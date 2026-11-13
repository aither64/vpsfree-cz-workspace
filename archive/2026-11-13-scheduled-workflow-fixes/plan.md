# Scheduled workflow fixes

## Goal and scope
Diagnose failing daily updates in vpsfree-cz-configuration and
vpsadminos-org-configuration. Inventory scheduled workflows in the workspace
project map, inspect recent run evidence, and fix confirmed relevant causes.
No production machine deployment is authorized. User subsequently approved merging all six repairs to master after completion and running affected workflows; exact wording is in state.md.

## Approach and ownership
Architect0 owns bounded investigation, root-cause design, and design.md.
Implementers own separate repository fixes, quick checks, commits and evidence.
Lead owns tracking, acceptance, independent review dispatch and user reporting.
Prefer minimal conventional workflow changes; avoid unrelated action upgrades.

## Compatibility and recovery
Preserve schedule, permissions, updater intent and generated data contracts.
Assess runner/action/Nix compatibility and token/authentication boundaries.
No schema or persistent runtime changes expected; recover by reverting workflow
commits after integration, without changing deployed machine configurations.

## Documentation
Readers: maintainers diagnosing automation and reviewing fixes. Root cause,
audit scope and run links belong in session evidence; lasting non-obvious
workflow constraints belong beside the owning workflow where useful.

## Validation and delivery
Inspect failed-attempt logs before reruns; verify latest compatible imported
actions from official upstreams. Pass repository hooks and focused workflow
checks, commit all fixes, then independent final review of full branch histories.
Use fresh utility watchers for long/uncertain checks. Publish feature branches;
request explicit repository/target integration approval only once reviewable.

## Confirmed repair repositories
vpsfree-cz-configuration, vpsadminos-org-configuration, vpsfree-irc-bot, haveapi, vpsadmin and vpsfree-kb-contracts. Separate source patches preserve all deployed schemas and product contracts. HaveAPI product performance remains a separately evidenced residual; full audit dispositions are in audit.md.

## Causal scope extension after hosted verification
The org run reached an oversized descendant changelog. confctl GitCommit sends the complete message in one -m argv element; exact-source local proof exposes Linux E2BIG, observed descendant text is1.2MB. Add confctl as seventh implementation repository: scoped standard Tempfile/-F transport and focused real-Git regression, then only org immutable workflow tool pin. Preserve useful changelog, hooks, editor/path/cwd/environment and cleanup/failure semantics. No changelog suppression or consumer sweep. confctl/master integration requires separate explicit approval after concrete reviewed result; original six/master approval remains. Full brief/evidence in design.md and evidence-c2.md.


## Corrected changelog policy
User explicitly says Nixpkgs update commit messages must use --no-changelog because these logs are large and useless. The generic file-backed Git message fix is approved for confctl/master, but preserving all descendant Nixpkgs logs is not an acceptance goal. Inspect direct update flags and component/descendant changelog scope; omit unwanted Nixpkgs logs while retaining useful component messages and full ancestry validation. Supersedes the earlier no-changelog-suppression assumption specifically for Nixpkgs.

Latest user correction further excludes transitive inputs from commit messages
entirely: both title and body must describe selected inputs only. The proposed
C3 selected-log filter with complete descendant summaries is superseded before
commit. Keep the complete graph for validation, callbacks and results; message
selection must not weaken ancestry checks. Architect0 owns the revised minimal
brief and descendant-only message behavior. Exact introduction was confctl
550717765d58e9f28d960ea5bca3459ace86eb9e, authored and committed24October2026;
its guarded callback began forwarding the complete graph diff to the message
builder where the preceding updater used a selected-input diff. This establishes
when behavior changed, without claiming the user requested it.

User explicitly confirmed the dependent adoption: "once that is done, let's
please update confctl in vpsfree-cz-configuration and vpsadminos-org-configuration".
Both one-pin consumers remain assigned to implementer0 and implementer1. Finish
the corrected provider, review and packaged proof, integrate it first, then
integrate both immutable pins and execute fresh daily workflows under the
existing merge/run direction.

## C4: one confctl authority
Latest explicit user correction requires NO revision pin in either workflow.
flake.nix declares the ordinary input; flake.lock selects its immutable revision.
Remove CONFCTL_FLAKE and its nix-shell override, consume the existing locked
confctl executable from each declared tools devShell, and update root confctl
input through normal tooling. Both currently locked providers predate C3, so
removing YAML alone would regress behavior. Architect0 settles exact lock/tool
and Ruby-compatibility checks; owners remain implementer0 vpsFree/implementer1 org.
Keep C3 provider unchanged and preserve merged C1/B1/C2/C3/default history. No new
workflow registry, exported pin, custom flake output or provider source expansion.
Fresh final reviewed workflows must run after this correction. Earlier YAML-only
pin adoption receipts remain historical rather than claiming final architecture.
