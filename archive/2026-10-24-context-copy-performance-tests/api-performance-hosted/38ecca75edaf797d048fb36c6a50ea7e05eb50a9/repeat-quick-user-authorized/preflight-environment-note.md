# Preflight environment correction

The ambient verified /home/aither/bin/dev-session current matched session/env.
The first script ran in Nix GEM_HOME and failed its first session-current call:
workspace Ruby3.4.9 loaded repository json2.21.2 native extension linked to
Ruby3.4.11/GLIBC2.44, incompatible with workspace libc. It made no SSH/API call
or dispatch. Original stderr and failed receipt retained unchanged.

Nix startup substituted two bash-interactive store paths before the script;
no gem/bundle/dependency installation or project change occurred. The corrected
script uses already-present ambient tools and matching identity markers,
without a new shell/dependency install. The one bounded SSH/source/concurrency
preflight is in preflight-ambient/. This is not a benchmark retry.
