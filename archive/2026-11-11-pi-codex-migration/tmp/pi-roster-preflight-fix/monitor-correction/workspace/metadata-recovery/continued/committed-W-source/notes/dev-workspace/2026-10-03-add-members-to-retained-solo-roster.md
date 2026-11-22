# Add development members to a retained solo roster

In `work/2026-10-03-infra-monitoring`, the public command
`dev-session team preset 2026-10-03-infra-monitoring delegated --as-is` refused
with `team preset differs from the retained roster`. The retained roster had
the solo preset and no members.

The supported public `dev-session team add <slug> <role> --as-is` commands for
architect, implementer and reviewer succeeded. They selected the installed
catalog's role settings and preserved the lead's retained settings. Verify the
exact session identity first, then inspect saved member purpose, access, state,
model and effort with `dev-session team list <slug> --as-is` before assignment.

Do not rewrite private roster files or substitute the lead for application
edits when adding members through the public interface resolves the setup.
