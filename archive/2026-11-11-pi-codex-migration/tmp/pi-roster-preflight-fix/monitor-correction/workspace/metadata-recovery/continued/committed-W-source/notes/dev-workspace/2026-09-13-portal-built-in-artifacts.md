# Built-in portal artifacts must not be registered twice

The portal already exposes plan.md and state.md. Adding plan.md to portal.yml's
artifacts list caused manifest validation to fail with "artifact path plan.md
is built in". Session discovery then returned 500 for the index and session page,
although /healthz and standalone upload routes still worked.

Remove the duplicate artifact entry and keep only additional review/results
files in the manifest. The final index, session page and shared upload module
then returned 200. Include real page requests in deployment verification; a
healthy process alone does not prove that session manifests are valid.

Related initiative: work/2026-09-12-portal-file-uploads/.
