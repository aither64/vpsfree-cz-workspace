# Slow initialization on a large Codex history

A filtered `thread/list` call on Codex 0.154.0 took 61.265 seconds for
`2026-09-13-auth-email`, repeatedly exceeding the old one-minute initialization
deadline. Loaded-thread metadata calls were fast. Keep authoritative discovery
and allow 180 seconds for the thread command, 210 for dev-session and 240 for
receipt reconciliation.

Do not substitute `useStateDbOnly` for authoritative discovery when proving
that a new thread is safe. It is fast, but an unavailable or incomplete index
can omit existing rollouts. An unrelated indexed thread or completed backfill
does not prove that the target directory is absent or unique. This shortcut
was rejected during review.

When changing the provider dependency, `nix develop` can fail before startup
if the Nix input and Go module pins differ. Update the module in an explicit
Nix Go/GCC shell, update the Nix input, and regenerate the vendor hash. Force
the hash calculation with a fake hash; an unchanged fixed-output hash can
return an older cached dependency tree without rebuilding.

Focused organization tests require the fixture configuration paths and runtime
contract environment variables from flake.nix. Its flake has no default shell.

Related initiative: work/2026-09-13-portal-reliability/.
