# 2026-09-16-portal-upload-recovery

## Goal

Make rejected and expired prompt attachments removable before and after reload,
and accept punctuation in original filenames without using those names as paths.
The user approved implementation and deployment to aitherdev through
vpsfree-cz-configuration. Do not integrate default branches or archive.

## Affected repositories

- codex-web: shared browser attachment recovery, tests and API documentation.
- dev-workspace: filename validation, store tests and attachment documentation.
- vpsfree-dev-workspace: runtime dependency pin.
- workspace: organization package and transitive pins in a dedicated worktree.
- vpsfree-cz-configuration: aitherdev host-module pin through confctl.

Use branch/worktree group 2026-09-16-portal-upload-recovery.

## Approach

Persist whether creation was never attempted, definitively rejected, uncertain,
or acknowledged, and retain useful error information. Remove local-only drafts
without creating uploads. Preserve same-client-ID recovery for uncertain outcomes
and legacy saved drafts; definitive rejection during recovery permits removal.
Treat deletion of an already absent file as success. Preserve visible retryable
authorization, busy-file and transport failures. Persist removal before showing
success and recompute composer readiness. Only existing incomplete uploads use
the resume label.

Accept Unicode and punctuation, including backslashes and path-looking names,
as metadata. Keep the 255 UTF-8 byte bound and reject empty names, invalid UTF-8
and control characters. Split filename, size and identity errors. Retain random
UUID storage directories, the restricted extension, text-node rendering, JSON
prompt serialization and MIME-formatted download names.

## Decisions

- The user selected punctuation support with control characters still rejected,
  and specifically requested careful escaping.
- No new HTTP endpoint or catalog schema is planned.
- No original emails or SQL payload logs are needed for testing: use synthetic
  filenames and contents.
- Investigation reproduced repeated POST on Remove, persistent failed cards,
  misleading resume labels after reload and stuck expired-file removal.

## Compatibility and deployment

Keep upload storage paths, catalog schema, submission receipts, lifecycle formats,
Codex protocol/version and size quotas unchanged. New browser metadata must load
old drafts and remain ignorable by old assets. Old/new stores can read completed
files, including newly accepted names. Rollback restores old validation/UI bugs,
but must retain completed-file access. No database/client/daemon changes,
coordinated node upgrade, or local kernel build is needed.

Push providers before consumer pins: codex-web -> dev-workspace -> organization
extension -> workspace package. Deploy the application from its user-profile
package; update the matching configuration devWorkspace input with confctl from
the initiative feature worktree. Build, dry-activate, deploy aitherdev and verify
live behavior. Retain previous package/system generations and all feature refs.

## Documentation

Readers are portal users and maintainers of embedding applications. Update the
codex-web README and dev-workspace attachment documentation with current removal,
recovery and filename behavior. Keep rollout revisions/results in this session.
Apply the user-facing writing skill to labels, errors and documentation.

## Testing plan

Focused browser and Go tests: rejected removal before/after reload and legacy
drafts, missing files, repeat removal, storage-write failure, cancellation,
uncertain create/delete responses, readiness and preservation of other files.
Exercise SQL/HTML-like names, quotes, separators, Unicode, length/control bounds,
safe paths, JSON and MIME round trips and old catalog readability.

Commit quick-verified changes before mandatory review. Classify high risk for
persistent browser state, deletion, compatibility and deployment; use all four
required review lanes with gpt-6-astra xhigh. Resolve findings before long package
and real-browser acceptance for both forms. Monitor feature CI and verify live
deployment. Leave the initiative open for follow-up.
