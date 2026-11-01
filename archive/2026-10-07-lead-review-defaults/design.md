# Lead and reviewer defaults

The lead owns this design and application implementation in a tracking-only
initiative without a retained roster. The user authorized the accepted plan.

## Catalog contract

Keep schema 4 and mode development. A team without any implementation-purpose
role is valid when design_owner is team_lead and that lead matches both design
and implementation work policies. If implementation roles exist, keep the current
requirement for a matching implementation role. Require independent fresh-context
read-only reviewers and preserve capacity/routing validation. Apply the same rule
in Nix and Go. Do not add another mode, role purpose, or persisted field.

The site preset lead_reviewed has team_lead and reviewer only. Its lead uses
gpt-6.1-sol/xhigh, workspace-write and high/xhigh allowed efforts; reviewer uses
gpt-6-astra/xhigh, read-only, fresh context and xhigh only. Use session lifetime,
non-priority service policy, existing lifecycle, max_open_agents 1 and existing
simple-effort routing. Keep capacity 4 for other presets. New lead instructions
own investigation, design and edits, use retained final review and do not acquire
specialists automatically. Existing catalog presets retain their settings.

## Portal contract

Render actual selected-team model and effort in new-session HTML. Populate exact
values before dynamic model discovery; keep them if discovery fails. Team changes
replace both selections with catalog defaults. Manual model changes select that
model's advertised default reasoning effort. Dynamic loading must preserve saved
explicit overrides. Restrict sentinel removal to the new-session controls.

Restore unsent legacy blank model/effort pairs as selected-team defaults; preserve
explicit choices and catalog-change acknowledgement. Submitted bodies and request
IDs remain locked and byte-equivalent through recovery, including legacy bodies.
Use existing request fields and backend validation; older API callers may still
omit both settings to resolve defaults. No lifecycle/receipt migration.

## Compatibility, rollout and recovery

Existing retained sessions and forks keep saved lineup, model, effort, access and
instructions. New composition needs the new validator paired with its catalog;
old installed catalogs remain accepted. Update the workspace nested runtime pin
and configuration channel to the same published exact revision. Preserve extension
and sibling inputs. Run the deployment checker before deployment. Deploy only
aitherdev, host configuration first and workspace user profile second. Respect
transition quiescence and ownership refusals; no forced interruption or stale-state
repair. Recovery uses the existing forward-only workflow and a corrected newer
package. No coordinated fleet update, database or generated-client changes.

## Acceptance and verification

Nix and Go accept valid two-member teams and reject missing reviewer, wrong access,
wrong lead policy, and a malformed existing implementer. Projection/creation yields
only lead and reviewer0 with exact settings and independent reviewer instructions.
Portal renders concrete values, resets on team changes, preserves manual choices
through asynchronous loading/reload, handles model discovery failure, resolves
unsent blank drafts, and keeps catalog acknowledgement and locked retries intact.

Quick checks: focused Go packages/browser contracts, node syntax, site Ruby tests
and Nix evaluation. Final committed-deliverable review includes the whole branch
history and an explicit no-migrations conclusion. Longer package/CI checks follow
review and use fresh Luna/low watchers. Live verification reads installed catalog
and the new-session form without creating unrelated persistent test sessions.
