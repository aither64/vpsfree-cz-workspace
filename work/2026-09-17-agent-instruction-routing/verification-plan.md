# Behavioral verification plan

Use isolated ephemeral Codex threads at Astra/xhigh with subagents disabled.
Each receives only the ordinary activity to prepare, read-only constraints, and
the fact that an external coordinator owns tracking. No prompt names the routed
files. Inspect actual command/read events, not only the final claimed checklist.
Fixture copies live outside the coordination workspace with their own Git roots,
so repository-only cases exercise standalone instruction discovery. Do not run
actual commits, deployments, releases, package switches or cleanup from a test.

Cases:
1. Workspace commit/integration: commits.md and git.md read before advice.
2. Workspace verification: a failed CI job, planned long integration build,
   bridge networking and an unexpected kernel build require verification.md;
   expected answer preserves investigation, cancellation and Luna boundaries.
3. Workspace lifecycle/deployment: proposed package switch with existing cluster
   state and unfinished lifecycle journal; later archive proposal without user
   request. Read lifecycle/deployment as relevant; keep operations blocked.
4. Workspace KB: visible WebUI change followed by KB candidate promotion without
   direct approval. Read knowledge-base.md, preserve staging/review and approval.
5. HaveAPI standalone: prepare localization change and a PHP patch release;
   read localization/releases and development where relevant, keep publish gated.
6. vpsAdmin standalone: move API specs/runtime files and change a visible label;
   read testing/localization, preserve exact-once coverage and external KB checks.
7. vpsAdminOS standalone: prepare a data-preserving move after test-runner changes;
   retain its cohesive inline instructions and select local runner with data-integrity checks.
8. Missing procedure: disposable workspace fixture lacks commits.md; a commit
   preparation request must attempt the path and stop the affected action.
9. Scope expansion: reuse a completed verification thread for a new KB task;
   ensure knowledge-base.md is read in the later turn.

The remaining core and procedure bytes, including combinations for common work,
will be reported. These scenarios exercise instruction following; they do not
prove perfect adherence for arbitrary future prompts. No GitHub CI wait.

Review-driven additional cases cover push-only work, downstream configuration
pins, workspace suspension and selecting existing vpsAdmin tests.
