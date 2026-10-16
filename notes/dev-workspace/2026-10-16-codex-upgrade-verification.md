# Codex upgrade verification prerequisites

When refreshing codex-web's Go pseudo-version, regenerate the runtime's final
vendorHash after go mod tidy. A cached fixed-output result passed with a stale
hash locally, while clean CI correctly rejected it. The runtime update skill
now records this requirement. Preserve the clean dependency-build evidence.

For a disposable NixOS naming VM, a manifest's diagnostic package.drvPath must
not retain Nix string context when the guest never opens that derivation.
builtins.unsafeDiscardStringContext keeps the provenance name without adding
all build inputs and sources to the guest closure. Keep strong references for
the actual application, fixture, source and resources. The accidental derivation
reference requested 4109 paths and 38.5 GiB; the corrected runner needed only ten
derivations and no downloads. Do not garbage-collect retained Codex generations
to compensate for a test-runner closure mistake.

The fixture invokes /run/current-system/sw/bin/managed-naming-smoke-counter.
Whitelist that exact path in the disposable VM's narrowly scoped sudo rule.
A rule naming only its Nix-store path required a password. Keep a read-only
counter preflight before the fixture so authorization failures remain visible;
the fixture intentionally suppresses subprocess stderr.

Native session cwd can be its tracking directory. Read its retained metadata
before asserting continuity, rather than assuming the coordination root. The
session's required ownership binding remains a separate prerequisite.

confctl build prompts even for a build-only operation. For an already authorized
noninteractive build, use confctl build --yes with the exact machine selector.
This flag does not authorize deployment or default-branch integration.

Evidence and final VM recipe: work/2026-10-16-update-codex/state.md and
work/2026-10-16-update-codex/final-managed-naming-vm.nix.

Codex --help exits before configuration loading. A successful strict help
command did not validate the DeepSeek profile: a real strict exec rejected
preferred_auth_method and the 0.163.0 schema also omitted
model_supports_reasoning_summaries. Remove obsolete fields in the managed
configuration. Keep custom-provider authentication in its own env_key.
forced_login_method=api enforces the shared OpenAI login before custom-provider
startup and can delete a ChatGPT credential. A synthetic-auth empty-prompt check
reproduced this; removing the unrelated restriction preserves authentication.
Source/provider probes need an isolated home without copied production logins. For a no-authentication source check, render the managed
profile as the base config in an isolated home and run strict App Server startup
with stdin EOF; do not pass -p to app-server. For deployed profile/provider
acceptance, run one small strict ephemeral request. debug prompt-input does not
support strict-config. The configuration skill and operations guide now record
the real provider check. Home Manager installs codex-ds under ~/.nix-profile/bin;
verify its selected package instead of assuming /run/current-system/sw/bin.
