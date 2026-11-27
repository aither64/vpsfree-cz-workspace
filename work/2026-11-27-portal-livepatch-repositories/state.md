---
lifecycle: active
---

# Repository tab investigation

Investigation and proposed solution are complete; see [findings.md](findings.md).
The portal selects a 2019 Linux merge base: 88,014 changed paths instead of the
9 paths / 13 commits from linux-core's recorded initial base. Size limits and
four-second Git deadlines explain reproduced 422 responses. Sequential batches
delay healthy repository histories. vpsAdminOS endpoints succeed independently.

## Phase checklist

- [x] Identify installed package and 28 target registrations.
- [x] Reproduce Linux history, summary and comparison failure modes.
- [x] Compare portal-selected and recorded bases with bounded no-fetch Git reads.
- [x] Check vpsAdminOS and replay browser-style batches.
- [x] Record root cause, limits, source paths, proposal and acceptance criteria.
- [ ] Implementation/deployment: outside the requested investigation scope.

## Next action and risks

If implementation is requested, add an explicit review baseline independent of
lifecycle defaults, preserve old durable comparisons, then improve isolation and
errors. Verify intended bases per branch. No complete browser reproduction was
performed; the findings do not claim that every card is broken.

## Ownership and documentation

This separate CLI-created tracking session has no lead Codex thread or roster;
no team was invented or borrowed. No application branch, worktree or deployment
was created. Target-session records, refs and checkouts were not edited. Portal
GET reads may populate normal comparison records. No temporary services or test
artifacts need cleanup. Unrelated shared files/index changes were preserved.

The installed package/source and all evidence are in findings.md. These are
investigation records, so no product documentation change or mandatory change
review is needed. Tracking-only records are the only intended commit.
