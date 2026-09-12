# Focused browser contracts and in-progress asset builds

Use the Go wrapper TestShippedBrowserClientMatchesSessionAPI to run the full
browser contract: it supplies the server URL and shared conversation module.
For units only, the CJS script takes --unit, an origin and the absolute path to
codex-web/conversation/assets/conversation.js. node --test without these arguments
fails before running assertions. The repository navigation contract has its own
Go wrapper TestRepositoryBrowserNavigationContracts.

While Nix assets or pins are being edited, a narrow nix shell --inputs-from .
with Go/GCC/Git/Node/Ruby/tmux/OpenSSL avoids building the unfinished application
merely to enter a shell. Git-backed Nix filesets omit new files until staged.
Final full Go tests and the correctly invoked Node units passed.
Related initiative: work/2026-09-12-portal-review-experience/.
