Technical draft for root final writing; source docs are not yet changed. No verification or activation claim.

README additions:
- Link the KB managed integration guide at dev-clusters/kb/README.md alongside the existing vpsAdmin guide.
- Optional clusterDefaults.kb = ./config/kb-devcluster.json enables the kb provider; omission keeps only existing vpsadmin/vpsadminos providers.
- Keep full portable lifecycle/source/capture behavior in K, linked from the E guide rather than copied.

Proposed dev-clusters/kb/README.md:

# Managed KB clusters

Set `siteConfig.clusterDefaults.kb` to an immutable JSON file to include the `kb` provider in the workspace package. Omit it to retain the existing provider set. A registered workspace can then select `kb` in `.dev-workspace.json`. The package uses one exact published K revision for its launcher, source receipt and imported read-only validators, retaining K's own input graph.

The [portable runtime contract](https://github.com/vpsfreecz/vpsfree-kb-contracts/blob/master/cluster/runtime-contract.md) owns lifecycle, prepared-artifact, source, resource and capture behavior. This adapter supplies workspace/session binding and the public provider route; it delegates lifecycle and live checks to K's fixed packaged executable. It does not start a second launcher.

Use `kb-devcluster --workspace NAME COMMAND SLUG`. The public dispatcher holds the selected package generation for the command. Mutations and captures require the active session and exclude its lifecycle journals. A busy session, adapter or portable gate returns the existing busy exit code 75.

Managed bindings are stored separately under `.dev-clusters/kb/bindings/SLUG`; K owns `.dev-clusters/kb/clusters/SLUG`. The binding records the engine revision at creation and keeps it across compatible package transitions. Transition adoption validates management compatibility without making a stopped or old-source artifact ready for capture. Resume and update retain K's supported prerequisites. Existing unbound or legacy state is refused.

`connection SLUG` exports a private managed descriptor that changes only K's controller route to the public `kb-devcluster` command. It preserves the original source, artifact, endpoints and credential references. Capture uses that descriptor with K's shared capture engine, for example `vpsfree-kb-capture --connection /private/connection.json ...`. The adapter validates the current descriptor and translates only its digest in lease readiness. It does not overwrite K's canonical descriptor.

The full capture lease retains generation, session, adapter and portable guards. Protocol stdout loss ends the lease; diagnostic stderr EOF alone does not. Peer or dispatcher loss closes child input, and normal cleanup reaps the exact spawned child. No peer or outer authority descriptor is inherited by the portable child.

`cleanup-paths SLUG` reports only the positively owned instance, binding and recorded socket paths. It can inspect running, stopped or pending state without recreating locks or claiming that processes exited. The generic removal workflow already holds the session lock, so this inventory does not reacquire it. Reset is a separate guarded K-owned stop/reset operation and retains ordinary exit and capture-exclusion proof.

Focused local tests separate synthetic CLI/pipe fixtures from actual selected K snapshot readers. They do not certify guests, package activation or installed managed capture. Package and real runtime verification follow committed independent review.

Root should review all English CLI usage/error text in dev-clusters/kb/lib/{cli,portable,provider,guards,managed,connection,lease}.rb before commits; no EN/CS product locale/catalog changes.
