Result: passed (both commands exit 0).

Revision: 574b1166e648d9edb360bb233b87bbd8883be3e7 (worktree dirty with assigned SDK/docs changes).

- `nix build .#checks.x86_64-linux.source-contents --no-link` — exit 0, 4.250 s. Log: `source-contents.log`.
- `nix develop --command npm run audit:design-docs` — exit 0, 5.277 s. Log: `final-docs.log`. Output: 266 routes, 74 API modules; 285 documents checked, 76 unique requirements.

No command or tool session remains running.