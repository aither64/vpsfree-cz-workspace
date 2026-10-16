# Shared login preservation follow-up

Review the new committed authentication correction, general and risk lanes only.
Read the mandatory review skill and those lane references. Reuse earlier review
of unchanged architecture/scope and companion repositories. Inspect the complete
configuration branch series for final history/no-migration conclusions.

Repository worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-update-codex/vpsfree-cz-configuration`.
Base ae98e9dbf05cd3f6b2d0c32255a4cb2d58c3865b; previous reviewed and deployed
9721c331baa47edf3f0c4cbaaa5204889031047e; final head aed7d507 (resolve full SHA).
Read root/repository AGENTS and applicable procedures. This is read-only review;
return the report, do not edit files or launch agents, builds, provider requests,
external messages or deployments. Launcher stores the report separately.

Actual postdeployment strict canary failed before any provider request:
`API key login is required, but ChatGPT is currently being used. Logging out.`
Exact native login/src/auth/manager.rs:1326-1383 enforces forced_login_method
against shared OpenAI auth before custom-provider authentication. Its local
logout removes credentials without token revocation. The local auth file was
restored privately from two identical retained operator backups; local login
status passes. No credential bytes were output or written to this workspace.
Recovery evidence is local-login-recovery.json.

New commit removes forced_login_method from the DeepSeek-only profile. Provider
env_key=DEEPSEEK_API_KEY still supplies authentication; endpoint, model, protocol,
key handling and shared OpenAI login remain otherwise unchanged. Guide and skill
explain this boundary and isolate source/provider probes without copying login
credentials. The earlier profile-schema correction remains independently useful:
it removes rejected keys; this separate commit corrects a valid setting with
undesired authentication effects. Neither repeats dependency pins. No migrations
or state-format changes. Both preceding heads were deployed and retained, but
deployment alone is not the rationale for this independent commit split.

Quick evidence: deepseek-login-preservation.json uses synthetic ChatGPT auth in
private homes and no prompt/model request. Before: forced API guard rejects and
removes synthetic auth. After: strict exec preserves exact synthetic auth bytes
and stops at empty prompt. Nixfmt, diff checks and declared commit hooks pass.
Skill validation runs in the same Nix Python/PyYAML environment as before.

Assess the removed enforcement, credential preservation and continued DeepSeek
authentication. Source/probe isolation is deliberate; do not require a new
production-home framework or change user storage. After accepted review, run
one isolated strict real DeepSeek canary with corrected managed profile and no
copied ChatGPT credentials, then build/deploy the exact final system through the
same reservation and verify deployed-profile loading/auth-file preservation.
No reboot or merge approval exists. All original native/state/naming tests and
workspace application outputs remain unchanged.
