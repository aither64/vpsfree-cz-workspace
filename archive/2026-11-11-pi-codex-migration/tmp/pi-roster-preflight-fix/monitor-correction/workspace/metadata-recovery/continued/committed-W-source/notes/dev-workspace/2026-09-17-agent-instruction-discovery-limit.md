# Keep required instructions within automatic discovery limits

During `work/2026-09-17-agent-instruction-routing/`, the workspace AGENTS.md
was 45,697 bytes. Inspecting the installed Codex 0.154.0 smoke-thread rollout
showed only its first 32,768 bytes in automatically loaded instructions. Later
KB publication, commit and project-map rules were absent from that load.
A link or a longer source file does not prove those rules reached the model.

The accepted fix keeps critical boundaries and explicit mandatory activity
routes in an 11,056-byte entry file, with complete procedures in owning project
documentation. Every original paragraph is mapped to its verbatim destination.
A repository check protects the entry size and all procedure links; harmless
fresh-thread probes check actual complete file reads, scope changes and stopping
when a required file is missing. Existing sessions must reread changed guidance.

Measure both the entry file and the applicable procedures. Moving sections adds
routing and retrieval overhead; vpsAdminOS remained inline because normal
verification became more expensive after splitting. Byte reductions do not
measure weekly allowance savings or prove universal instruction compliance.

When inventorying repositories, inspect the actual remote default (origin/HEAD,
verified with ls-remote --symref origin HEAD for unusual cases), not a stale bare
HEAD. Security-advisories used a dated default branch, so inspecting bare master
initially omitted its instruction file. See the earlier bare-clone default-ref
inspection note for this failure pattern.
