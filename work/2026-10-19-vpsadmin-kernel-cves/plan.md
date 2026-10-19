# 2026-10-19-vpsadmin-kernel-cves

## Goal

I'd like you to gather linux kernel CVEs in vpsadminos kernel since 6.12.95 to 6.12.113 (inclusive). start from the last CVE reported in vpsadmin security advisories at vpsadmin.vpsfree.cz. Make a list of eligible CVEs and after my approval, you will draft them in vpsadmin using the security-advisories repo.

Look at the existing advisories to see what CVEs we're interested in. There's too many in reality, so we choose those that can lead to privilege escalation, etc.  critical severity, I'd say. if  you're unsure about classification, you can ask.

## Affected repositories

- `security-advisories`: read existing assessment conventions and, only after
  approval, prepare unpublished vpsAdmin drafts.
- `vpsadminos` and `linux`: read-only kernel version, configuration, patch and
  stable-fix evidence. vpsAdmin production advisories are read-only in this phase.

## Approach

1. Architect defines the inclusive fixed-version interval, latest published
   advisory baseline, applicability rules and independent research packages.
2. Implementers gather existing-advisory/configuration evidence and enumerate
   upstream CVEs/fix versions, then reconcile reachability and impact.
3. Present a sourced shortlist, explicit exclusions and classification questions.
4. Wait for user selection approval before creating any vpsAdmin drafts.

## Decisions

- Research is authorized; drafting and publication are not yet authorized.
- Assess tenant-to-host privilege escalation, container escape, arbitrary kernel
  execution and similarly serious impact; distinguish platform priority from
  formal CVSS severity. Do not infer exploitability solely from memory corruption.
- Use primary CVE and stable-fix evidence; record uncertainty and deduplicate
  against existing advisories rather than comparing CVE numbers chronologically.

## Compatibility and deployment

This phase changes no application, persisted state, schema, API, protocol,
configuration or deployed kernel. No coordinated machine update is requested.
Later advisory drafts must use the repository's supported schema and guarded
workflow. Publication, deployment and repository integration need separate scope.

## Documentation

Readers: user approving the selection and later advisory authors. Keep research
method in `design.md`, detailed evidence in session artifacts, and current phase,
ownership and unresolved classification decisions in `state.md`.

## Testing plan

Validate range endpoints, CVE identifiers, stable fix inclusion and applicability
against primary records, and confirm prior-report deduplication. No builds or
integration tests are needed for research alone. Routine findings are exempt
from automatic final change review; substantive later advisory changes are not.
