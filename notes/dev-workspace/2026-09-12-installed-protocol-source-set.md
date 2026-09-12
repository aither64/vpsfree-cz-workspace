# Validate the installed Codex protocol source set

Related initiative: work/2026-09-12-portal-review-experience.

workspace-host check-codex reported source/corpus count mismatches after a
package build passed. codex-web's validator scans production Go files beside
client.go, but packaging installed only client.go. Activity reader calls were
therefore missing only in the installed artifact.

Install the complete production source directory, exclude test files, and point
the host validator at that client.go. Run coverage against those installed
files during packaging. The exact staged layout passed the full experimental
Codex0.154schema validation; retain live installed preflight before switching.
