# 2026-07-17-mandatory-review-updates

## Goal

Strengthen the mandatory standalone review so it catches compatibility code
for abandoned feature-branch iterations, raw vpsAdmin API identifiers where
HaveAPI associations fit, misplaced top-level API resources, and unnecessarily
duplicated ActiveRecord migration directions.

## Affected repositories

- Top-level vpsFree.cz development workspace repository only.
- `skills/mandatory-change-review/SKILL.md` contains the functional change.
- Initiative tracking and a validator-invocation note document the work.

## Approach

- Require new features developed iteratively on an unmerged branch to converge
  on their final protocol, version, and schema instead of retaining superseded
  intermediate forms.
- Require vpsAdmin API relationships to use HaveAPI `resource` declarations
  when the referenced resource exists and can be resolved safely.
- Require each top-level vpsAdmin API resource to have its own source file while
  allowing nested resources to stay with their parent.
- Prefer ActiveRecord `change` migrations and `reversible` blocks for
  direction-specific data changes, with justified exceptions for clearer or
  otherwise unsuitable operations.
- Apply the checks to newly introduced or changed code and require concrete
  rationale for exceptions rather than flagging unrelated legacy code.

## Decisions

- Compatibility remains required for behavior and state that was merged,
  released, deployed, or externally consumed. Compatibility solely with an
  abandoned, never-merged branch iteration is not required.
- Raw IDs remain valid for historical records, deleted resources, and other
  cases where a live HaveAPI association cannot represent the data safely.
- The migration rule is a strong default, not an absolute ban on `up`/`down`.
- The skill's trigger and UI metadata remain unchanged.

## Compatibility and deployment

This initiative changes review policy only. It changes no runtime code, public
API, persisted state, database schema, generated client, configuration, or
deployment ordering. Existing reviews gain additional checks without changing
the standalone-review workflow or output severity levels.

## Testing plan

- Validate the skill directory with the skill-creator validator in a Nix Python
  environment containing PyYAML.
- Run `git diff --check` and inspect representative compliant and non-compliant
  cases for all four rules.
- Commit the intended changes after quick verification, then run the mandatory
  review with exactly one fresh standalone agent using the updated skill.
- Record the review outcome and address or explicitly discuss significant
  findings.
