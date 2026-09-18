# Documentation boundaries

## Goal

Separate lasting project documentation from reusable operations, supported
upgrade guidance and individual rollout records across all repositories. Update
the shared authoring and review rules, merge the affected default branches and
deploy the updated skills on aitherdev.

The user authorized implementation, default-branch integration and deployment,
including vpsfree-cz-configuration if a host change is necessary. Do not modify
session 2026-09-09-ip-release-mechanism, its worktrees, branches or cluster.
Prepare a handoff for its owner in this initiative instead.

## Affected repositories

- dev-workspace: generic documentation skill and its human guide.
- vpsfree-dev-workspace: documentation review/handoff guidance and runtime pin.
- workspace: local documentation rules and consuming extension pin, in a
  dedicated workspace feature worktree.
- vpsfree-cz-configuration only if a demonstrated host prerequisite requires
  it. The workspace application is delivered through its user profile.

Use 2026-09-17-documentation-boundaries for branches and worktree grouping.
The shared coordination checkout stays on master. This external conversation
owns the work; the helper-created conversation must remain idle.

## Approach and decisions

1. Establish the generic skill as the authoring authority. Classify material by
   applicability, lifetime and owner, rather than whether it includes dates or
   commit hashes. Apply the rule to mixed passages individually.
2. Keep feature behavior, accepted rationale, invariants and transaction failure
   semantics in owning project docs. Separate repeatable operations, explicitly
   scoped upgrade instructions, specific rollout plans/results and temporary
   development state. Keep site procedures with site configuration.
3. Preserve lasting compatibility constraints with the component; procedures
   link to those constraints. Distinguish application rollback semantics from
   reverting deployed software. Do not hide supported upgrade guidance in a
   private session record.
4. Update the runtime guide, extension review packet/general-review/handoff
   guidance and workspace destinations consistently. Keep generic examples
   independent of organizations and hosts. No new document framework, fixed
   file bundle, mandatory deployment heading or historical backfill.
5. Publish and pin runtime -> extension -> workspace without unrelated input
   updates. Commit quick-verified changes before mandatory review, resolve
   findings before long checks, and check final-head CI.
6. Fetch/rebase when needed, recapture final comparisons and integrate by
   fast-forward. Use fresh temporary target worktrees for independent projects;
   integrate workspace from shared master without staging unrelated changes.
7. Build and deploy through the installed workspace-host switch --source
   command. Verify package/catalog contents, fresh discovery, user services and
   portal access. Retain the predecessor generation for recovery.

## Compatibility and deployment

Instruction/documentation changes and exact dependency pins only. Keep the
skill name, discovery metadata, catalog schema, session templates, runtime APIs,
database formats, lifecycle journals and cluster state unchanged. No migration,
generated client, daemon protocol, NixOS option or coordinated node update is
needed. Old and new packages can read the same session records. Profile rollback
restores earlier skill wording and does not revert committed workspace policy
or authored documentation. Existing conversations may retain instructions loaded
before deployment; verify fresh catalog discovery without claiming they reload.

Record this particular deployment, exact revisions and recovery preparation in
rollout.md here. Do not add host details to generic or organization packages.
Respect package-transition refusals; do not interrupt or reset another session.

## Documentation

Readers: developers, operators and context-owning agents across repositories.
Generic rule and rationale belong in the runtime skill/session guide. Extension
review and handoff instructions consume that rule; workspace AGENTS retains site
destinations. This initiative owns ip-release-handoff.md and rollout.md. The IP
release owner receives relocation instructions without edits or new operational
authorization for that session.

## Verification

- Skill-creator validation for edited skills; Markdown links, metadata,
  whitespace and repository hooks.
- Assess examples covering a small feature fix, transaction rollback, reusable
  recovery, a supported schema upgrade, a site rollout and a disposable branch
  database. Check correct placement and preservation of constraints; no tests
  that merely match wording.
- Mandatory adaptive review of committed changes using gpt-6-astra/xhigh,
  followed by required repository/package/catalog checks and consumer build.
- Final-head GitHub Actions; investigate failures before accepting reruns.
- Verify deployed skill targets/content, fresh catalog discovery, user-service
  health and portal access. Capture exact results and limitations.

## Completion

Merge and push each registered final head to its remote default branch. Retain
feature branches, remove clean owned worktrees after verification, and leave the
session open. No archive, deletion or delayed cleanup is authorized. Final
handoff reports merged revisions, deployed verification, the IP release handoff
and this initiative's stable portal URL.
