# Milestones and acceptance

1. Generator: generated root/action descriptions, pre-dispatch validation errors,
   typed metadata, metadata namespace compatibility and HaveAPI0.32 support.
   Quick source checks and committed independent review precede real HTTP tests.
2. SDK: two exact full-schema exports match existing519-action/151-resource schema;
   refresh source/tooling provenance and regenerate from committed generator.
   Prepare0.3.0 immutable candidate with strict TS5.9/TS6 consumers.
3. Shared WebUI: one full RequestSpec policy executor; zero API calls at client
   construction, public isolation, no write replay, raw receipt preservation and
   precise local input versus uncertain transport classification.
4. Pilot: VPS read/start plus a live network capability. Validate metadata,
   optional fields, async receipts and denied capability behavior before batches.
5. Parallel domains: five nonoverlapping API groups, direct consumer fixes and
   focused tests. Source-backed unsupported inputs receive honest UI handling,
   not loose SDK types. New upstream call sites are included after each rebase.
6. Retirement/readiness: remove generic call/descriptor/unwrap layer and duplicate
   wire DTOs, update package guards/docs, quick checks, committed whole-series
   review, then long browser/API/package checks. Integration/publication/deployment
   remain separately authorized actions.

User priorities: clean separation of concerns; improvements to generated client
must originate in its HaveAPI generator. Eight implementers retain owned packages
through follow-up fixes. Lead coordinates scope, Git serialization and acceptance.
