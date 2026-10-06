# 2026-07-21-node-evidence-access

## Goal

Review the vpsAdmin Node security-evidence API resources and their WebUI
presentation, then recommend which currently administrator-only data can be
made readable by authenticated vpsFree.cz members without exposing information
that materially helps unauthorized access to Nodes, other VPSes, or operational
control systems.

## Affected repositories

- `vpsadmin`
  - primary review target;
  - trace the Node evidence resources, authorization, serializers, data model,
    collection semantics, API tests, and WebUI rendering;
  - no source changes are planned during this review.
- `security-advisories`
  - read-only reference consumer of the typed evidence API;
  - use its collector and evaluator to identify which fields have concrete
    security-assessment value and which data are deliberately queried only on
    demand;
  - no source changes are planned.

## Approach

1. Inventory every Node evidence resource, action, field, filter, relation,
   and authorization rule exposed by the current vpsAdmin master branch.
2. Trace the WebUI pages and API requests to establish what administrators and
   ordinary logged-in users can see today.
3. Classify each field by member benefit and abuse value. Consider host
   fingerprinting, vulnerable-version discovery, mitigation bypass guidance,
   topology and naming disclosure, source-revision leakage, configuration
   drift, availability information, and whether the same fact is already
   necessarily observable from a member's own VPS.
4. Inspect the security-advisory collector to distinguish broadly useful
   evidence from narrowly requested security-sensitive evidence.
5. Verify important authorization and response-shape conclusions with focused
   existing specs or a non-destructive out-of-tree check if existing coverage
   is insufficient.
6. Record a field-by-field recommendation, including any filtering,
   normalization, freshness, or UI-context requirements. Do not implement the
   recommendations until they are reviewed by the user.

## Compatibility and deployment

- This initiative is an assessment only and changes no API, schema, persisted
  evidence, generated client, WebUI, protocol, or deployment configuration.
- A later implementation should be additive for authenticated users while
  preserving existing administrator responses and evidence collection.
- Authorization must remain enforced by the Ruby API; WebUI visibility is not
  a security boundary.
- Mixed WebUI/API deployments should remain safe: an older WebUI can ignore
  newly readable resources, and a newer WebUI must tolerate older APIs that
  still deny them until the API deployment completes.
- Any future public response should avoid making raw secrets, credentials,
  private addresses, internal service topology, or exploit-enabling mitigation
  detail readable. Rollback should only remove the newly granted read access;
  it must not alter the stored evidence format.

## Testing plan

- Inspect existing API authorization and serialization specs for all Node
  evidence resources.
- Inspect existing WebUI browser coverage for ordinary-user and administrator
  Node detail pages.
- Run focused API specs that establish current ordinary-user behavior and
  field shapes where practical.
- Use only synthetic test data. Do not query production Nodes or production
  evidence for this review.
- Check both worktrees remain clean and run `git diff --check` on the initiative
  documentation before handoff.
