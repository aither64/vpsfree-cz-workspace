# Session setup and tracking

Required workspace procedure, selected by the routing table in `AGENTS.md`.
Its rules retain workspace scope and precedence. Paths and commands are relative
to the coordination workspace unless the text specifies another repository.

## Workspace Layout

Use these paths consistently:

- `repos/<project>.git`: canonical bare clone of an upstream repository.
- `worktrees/<yyyy-mm-dd-slug>/<project>`: per-initiative feature worktree.
- `work/<yyyy-mm-dd-slug>/plan.md`: durable plan, affected repositories,
  compatibility notes, and decisions.
- `work/<yyyy-mm-dd-slug>/state.md`: current status, branch names, commands
  run, test results, open questions, and cleanup notes.
- `notes/`: durable development notes, troubleshooting tips, and reusable
  lessons that should survive beyond one initiative. Store each lesson in its
  own file to reduce conflicts between concurrent Codex instances.
- `archive/`: committed plan, state, and curated durable artifacts for
  initiatives that are fully completed or explicitly abandoned.

The initiative slug must be descriptive and dated, for example
`2026-05-27-api-token-rotation`. For affected project repositories, use the
same slug for the tracking directory, feature branch, and worktree group unless
a repository-specific rule requires otherwise.

Use the user-profile `dev-session start <name>` when starting a development
session. It selects the registered workspace from the current directory, fixes
the matching authority, tmux, Codex, and portal endpoints, and creates a dated
slug from the short name. Pass `--workspace <name>` when calling it outside a
registered root or when an explicit selection is clearer. Use `--as-is` when
the full slug has already been chosen. An exact active slug with committed
`plan.md` and `state.md` but no portal manifest can be restarted this way after
its old writers are stopped. The helper preserves both tracking files, creates
a fresh shared conversation, and registers canonical worktrees it finds under
that slug.

When running inside an existing development session, do not choose a new slug
until checking for the active one. Run `dev-session current` from the workspace
root. Treat the printed slug as belonging to the
current process only when the `DEV_SESSION_SLUG` environment variable
is also set to that exact slug. If `current` prints a slug but the environment
variable is missing or different, assume it belongs to another concurrent
session and do not touch that session's `work/<slug>/`, `worktrees/<slug>/`,
branches, or notes. In that case, create a separate initiative unless the user
explicitly tells you to use that existing slug. Reuse `work/<slug>/` and
`worktrees/<slug>/` only for the verified current session, and record progress
in that session's `state.md`.


## Planning And Tracking

Start each requested feature or fix by identifying the affected projects. Some
features span multiple repositories; plan the cross-repository shape before
editing any one component.

For each initiative, maintain:

- `plan.md`: the goal, affected components, approach, compatibility analysis,
  deployment ordering, testing plan, and explicit decisions.
- `state.md`: branch/worktree locations, current progress, commands run,
  results, blockers, and cleanup status.

Treat `work/<slug>/` as active tracking and `archive/<slug>/` as terminal
tracking. New `state.md` files must begin with this exact YAML front matter:

```yaml
---
lifecycle: active
---
```

An initiative remains `active` while any registered feature branch is
unmerged or the session still owns work. Set it to `complete` only after every
registered branch's exact final head is merged into its configured remote
default branch and no review, CI, deployment, approval, or cleanup remains.
Pushing, testing, deploying, or temporarily removing worktrees does not make an
initiative complete. Use `abandoned` only when the work is explicitly
discarded; abandoned work does not have to be merged. Coordination-only
initiatives with no registered branches can still be completed. The anchored
front matter is the only lifecycle authority; lifecycle-looking text in the
Markdown body has no effect.

Completion criteria do not authorize integration. When feature work is ready
but the user has not explicitly approved its repository/target set for merging,
keep `lifecycle: active` and put "ready, awaiting merge approval" near the top
of `state.md`. Record any approval's wording/source, repository and target
branches, whether a later rebase preserved patch equivalence, and the exact
final heads once integrated. Do not mark an initiative complete merely because
review, CI, or deployment succeeded.

Write a substantive plan and initial state, then commit both in the top-level
workspace repository before the first project-code commit or external mutation.
After that initial commit, keep plan and state current in the working tree
without committing every update. A short initiative should normally make no
further tracking-only commit until its final archive commit. If an initiative
remains unfinished at the end of an active working day, it may make at most one
consolidated tracking-only checkpoint for that day when material progress is
worth preserving. This is a ceiling, not a daily requirement. Material progress
includes changed implementation heads, durable decisions, completed phases,
new blockers, and results that change the next step.

An additional same-day tracking checkpoint is allowed only for a genuine
ownership handoff or an explicit user request. A pause until a future working
day can justify that day's consolidated checkpoint, but not a second one.
Individual plan edits, branch-head changes, review findings or remediations,
commands, test or CI results, deployment actions, and status polls do not by
themselves require commits; consolidate them into the next daily, handoff, or
final summary. Functional changes in the workspace repository and normal
commits in project repositories do not count as tracking-only checkpoints.

Keep these files current enough that a future agent can resume the work without
guessing. When plans change because code or tests reveal new facts, update the
tracking notes.

After material changes, review checkpoints, or user-requested status updates,
use `~/.codex/skills/dev-session-handoff/SKILL.md`. Keep the initiative portal manifest
current and include the stable link printed by
`dev-session url <slug> --as-is` in the handoff. If the portal has not been
deployed yet, identify it as the post-deployment URL.

Promote reusable lessons to `notes/`. In particular, write a note when a
command, shell, test, build, deploy, hook, or worktree operation fails in a
non-obvious way; when a workaround saves future time; when a repository has
undocumented setup or ordering requirements; or when an investigation finds a
dead end worth avoiding later.

Keep `state.md` detailed for the current initiative and keep durable notes
concise for future reuse. Store each lesson in a separate file, using
`notes/cross-project/<yyyy-mm-dd-short-topic>.md` for cross-project notes and
`notes/<project>/<yyyy-mm-dd-short-topic>.md` for repository-specific notes.
Record the command or workflow, symptom, cause if known, fix or workaround,
verification result, and related initiative path. Summarize long logs instead
of pasting them. Redact secrets and avoid recording temporary local paths unless
the path itself matters.
