# 2026-10-17-team-delegation

## Goal

Make leads coordinate and communicate when implementation specialists exist,
and give new Full-team sessions two implementers. Preserve hands-on lead work
in smaller teams without implementers. User accepted the proposed plan and
requested implementation on 2026-10-17.

## Affected repositories

- dev-workspace: repeated-role catalog counts, creation/recovery validation,
  fallback prompts and presets, tests and owning documentation.
- workspace: installed role prompts and roster, workspace instructions and
  policy tests, nested runtime selection.
- vpsfree-cz-configuration: matching dev-workspace channel selection and
  aitherdev deployment.

## Approach

Use end-to-end work packages with owners, acceptance criteria, dependencies,
and checks. Architect owns Full-team investigation/design and implementation
boundaries. Implementers own execution, tests, technical docs, quick checks,
commits and follow-up fixes. Lead retains acceptance, coordination, tracking,
approval-bound actions and user communication. Serialize overlapping edits and
Git operations. Lead-designed retains lead-owned design; Solo and Lead and
reviewer retain hands-on leads. No automatic scheduler is introduced.

Add catalog schema 5 with optional initial_member_counts (default one per
non-lead role), retain schema-4 reads, and create stable numbered members.
Full team has lead, architect0, implementer0, implementer1 and reviewer0.

## Decisions

- Coordinator policy with narrow coordination exceptions when implementers exist.
- New teams only: no saved prompt refresh or existing roster changes. Forks and
  retries retain their exact selections. Shared guidance remains globally visible.
- Existing models, effort, access and default preset remain unchanged.
- Missing specialists allow lead execution; busy or inaccessible retained
  specialists require resolving the condition instead of taking their work.
- Deployment is in scope; default-branch integration has not been authorized.

## Compatibility and deployment

Existing roster and receipt field layouts remain unchanged. New runtime must
read preceding catalog schema 4 and old single-member receipts. Old packages
cannot consume new repeated-role creation snapshots; recover forward using a
compatible package. No database, external service protocol or managed-node
coordination change is intended. Direct threads do not require more native
child capacity. Pair workspace's nested runtime pin with configuration's
dev-workspace channel; preserve extension and unrelated inputs. Build and deploy
feature refs under the aitherdev machine reservation; application selection is
through the user profile. Preserve deployed generations and recovery evidence.

## Documentation

Readers: leads, architects, implementers, package maintainers and operators.
Keep durable behavior in runtime session/portal docs and site team guidance.
Keep exact rollout revisions, commands and evidence in this initiative.

## Testing plan

Focused catalog, runtime, web/CLI creation, receipt/recovery and prompt tests;
validate count failures and digest compatibility. Check interrupted creation,
forks, retained prompts and adding the next numbered member. Commit intended
changes and run mandatory independent review before longer packaged/integration
checks. Run final deployment-pin consistency check and smoke-test both members.
