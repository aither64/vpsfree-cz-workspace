> Current integration: product master `0f450b89`, configuration master `64220e28` and React main `f2765d3f` are merged and independently verified. The requested WebUI channel update selects f276; review and the affected Newadmin build passed. All React main workflows passed; configuration exact-head discovery found no workflows. All merge claims are released. Only separate product integration CI remains E2-owned. No new application deployment or lifecycle action. See [current state](state.md) and [channel handoff](integration/configuration/webui-channel/integrated-handoff.md).

The earlier readiness and finish-plan checkpoints below retain their historical scope.

# Finish plan — implementation authorized

**Current correction:** retain Varnish in its original routes and preserve its metrics cache. The user excludes shared-memory-only logs; persistent request logging has not been established for configured Varnish. A0 defines the minimal correction, E2 owns product docs/fixture alignment and E1 the site routes/docs/final pin. Preserve nginx/HAProxy/PHP persistent-log protection and all unrelated behavior.

Current milestone: user approved all three final application merges with “fine, merge it”; all three packages and the React test-only follow-up have now been fast-forwarded, independently verified and their short claims released. Product0f450b89 is reviewed, checked and published with all four exact-head CI workflows passed. Site9927bb70 selects0f and has certified review reuse, four actual builds, precise artifact/input reuse and guarded recovery-first publication accepted. Product/site command effects are reconciled and source writers released. React f2765d3f remains complete; workspace integration/deployment/release is already complete. Varnish routing/caching and persistent-log protections remain. The historicalfbd auth500 is unexplained; no causal-fix claim. The three named application integrations are now approved; production deployment and session lifecycle actions remain unauthorized.

Finish and merge the workspace tooling first, verify the final workspace package
on aitherdev, then release its reservation. Independent product security and React
0.32.0 feature work can proceed alongside verification; workspace integration
remains first.

| Order | Owner / active worktree | Deliverable and target |
| --- | --- | --- |
| 1 | E0, `vpsfree-dev-workspace-services-os` | Finish the already-running checks of combined updater, boot proof and writing policy; integrate into `vpsfreecz/dev-workspace:master`. |
| 2 | E1, `workspace-services-os` | Select that final provider once, retain the current generic runtime and existing instruction repairs, finish review/checks; integrate into `aither64/vpsfree-cz-workspace:master`. |
| 3 | E2, `vpsadmin-oauth-client-logs` | Put reusable API/auth/PHP nginx, FPM and HAProxy protections in vpsAdmin's modules and defaults. Intended target: `vpsfreecz/vpsadmin:master`. |
| 4, after E2 | E1, `vpsfree-cz-configuration-oauth-clients` | Remove duplicated protection, retain site topology/private settings and one final vpsAdmin pin. Intended target: configuration `master`. |
| 3, alongside E2 | E3, `vpsadmin-webui-031` | Use the published `haveapi-client` 0.32.0 package, update lock/provenance/Nix hash, and verify the retained adapter. Intended target: `vpsfreecz/vpsadmin-webui:main`. |

The first two integrations have the user's direction. On 2026-10-31 the user also
approved implementation of the three application corrections. Their eventual
default merges and production deployments remain separate.

After the workspace integrations, deploy and verify the exact final workspace
profile under the existing aitherdev reservation. This is required because the
new consumer changes provider behavior; merging a nonancestor successor is not
proof of equivalence to installed profile 218. Reconcile outstanding operations,
prove complete deployed lineage in fresh remote defaults, check exact claim
`d0061f09-dbfd-4531-b10f-862e7354a78f`, then release it and verify release.
The recorded reservation covers the workspace application; the pending product,
site and React corrections do not block that sequence. No host-system rollout
or guest change is part of this step.

The security correction keeps reusable protection with vpsAdmin. Site configuration
keeps domains, certificates, backend routing, private inputs and operator policy.
Safe access records retain status and timing; PHP keeps native diagnostics.
HTTP redirects must receive the same protection as HTTPS, while preserving ACME,
aliases, maintenance and Basic auth. The product now owns a reviewed private merged-host transform;
its one-sided-listener and raw-snippet limits are explicit in the design and docs. Explicit Varnish/external-proxy routes need their existing
topology treatment and cannot be certified by nginx defaults alone.

React previously retained 0.31.2 because the later 0.32 adoption excluded it and
the consolidation preserved that scope. The corrected branch now uses0.32.0. No technical need to stay on 0.31.2 was
found. The actual npm 0.32.0 release is already verified; use its archive, not
the Ruby release identity or repository-built dist. Keep the adapter unless
checks against that artifact demonstrate a necessary change.

Each changed application candidate gets focused quick checks, committed-source
independent review, then its required final tests/builds. Preserve successful
old checks only for their exact unchanged inputs. Retain one active review
worktree per repository, all recovery refs, live sources and private paths.
No application merge, production deployment, PR rewrite or session cleanup is
authorized by this plan.

[Technical boundaries and evidence](design.md#finish-plan-workspace-first-product-defaults-and-react-032-2026-10-31)
· [Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/)
