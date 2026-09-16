# Scope and proportionality review

## Findings

No Blocking, Important, or Advisory findings. The final committed series is
proportionate to the approved recovery and filename requirements. This includes
the four remediations recorded in `review-reconciliation.md`.

Reviewer: gpt-6-astra, xhigh; performed directly without delegation or
project-code changes. Read the mandatory review skill and scope reference,
final packet, plan/state, reconciliation, local AGENTS files, commit series,
changed implementation/tests/docs, and adjacent consumers and host configuration.

## Scope assessment

- `codex-web` commit `f2e44242411358d1651811e37e8ed6f9325b6bfb`,
  `conversation/assets/uploads.js:245`: creation outcomes, persisted errors,
  persistence failure tracking and save-before-removal each address an observed
  failure. These remain local to the existing composer. There is no new
  cancellation protocol, storage format migration, or general recovery framework.
- The same commit at `conversation/assets/uploads.js:315` uses the existing
  authorized listing only after DELETE 404. The runtime's current
  `portal/internal/web/uploads.go:54` does use 404 for scope-resolution failures,
  so this is necessary handling of an actual consumer, not speculative support
  for arbitrary servers. Remembering successful deletion at line 324 and
  restoring the prior creation outcome at line 264 correct existing transitions
  without expanding the supported operation set.
- `dev-workspace` commit `8da4eebed517a2f76a64dc8d9eb602511107d6f1`,
  `portal/internal/uploads/store.go:469`: relaxed punctuation validation and
  separate errors implement the selected policy. Moving admission checks after
  scoped identity recovery preserves files admitted by the previous validator;
  it does not introduce a second legacy validator or compatibility registry.
  Existing UUID paths, restricted extensions and catalog structure remain.
- `codex-web` commit `7429ff29d3ae35c43b155a99b1bd34c6a33ae187`,
  `conversation/uploads.go:199`: checking the already bounded request bytes for
  UTF-8 is a small addition needed before JSON decoding can replace invalid
  input. JSON decoding and MIME encoding remain delegated to the standard
  library. The representative filename tests check application boundaries
  without attempting exhaustive JSON, MIME, filesystem or Unicode conformance.
- The browser test fixture invokes the shipped component through events and
  observes requests, persisted selection and readiness. Its failure cases cover
  distinct owned behavior: lost acknowledgements, rejected/legacy drafts,
  cancellation, transient versus persistent writes, scope-level 404 and denied
  reads. The tests are proportional to persistent selection and removal behavior.
- Functional browser recovery and transport encoding are separate provider
  commits; runtime validation and provider consumption are separate runtime
  commits. Cache identities, module sums, vendor hash and matching source pin
  belong together in the consumer commit. The remaining three commits update
  only the existing dependency chain. Configuration still consumes
  `nixosModules.host`; its host module/path sources are unchanged from its older
  runtime pin. No unrelated host or application deployment behavior was added.
- Both owning READMEs document the changed behavior and embedding contract.
  Operational evidence stays in the initiative. No obsolete implementation
  branch or speculative defensive layer remains in the committed changes.

## Verification and residual gaps

- Reviewed the exact ranges below and the focused verification evidence;
  no tests were rerun and no long integration or deployment action was started.
- Real Firefox acceptance for both portal forms, warmed-cache upgrade/rollback,
  package acceptance, host dry activation and live deployment verification still
  need their planned evidence. DOM test doubles cannot establish those results.
- The catalog reopen test uses the new reader. Actual previous-package access
  to files with newly accepted names remains part of rollback acceptance.
- Recovery depends on the documented store contract: HTTP 400/413 cannot conceal
  an accepted creation, and the authorized listing must faithfully report the
  scope's files. The current consumer supports this contract; this review does
  not establish compatibility with arbitrary third-party stores.

## Exact reviewed revisions

| Repository | Base | Head |
| --- | --- | --- |
| codex-web | `882c88ccfbebfb646fb2cafbe9bc6790141b2d13` | `7429ff29d3ae35c43b155a99b1bd34c6a33ae187` |
| dev-workspace | `5d853b6b0c2608549a1f0e940c680ccb40a14bec` | `eb658d49e6b8182d5fc07ab98bc897c58490baa9` |
| vpsfree-dev-workspace | `b75cc8a6270219ca2fc25c1e292ce030fc33e45d` | `17da396e7fea5d4e31d4af1382da00fe4d140e17` |
| workspace | `94f8add7ca745ae9b35e2ee700e923663a2c5a02` | `7a1c0f53448ddb32af2044f33f529a748e25d16a` |
| vpsfree-cz-configuration | `b6e650ad902482b4c4e66b5a89a4275bed92419e` | `47e1ce3de7c326c9f8931cfa02e4ecfe4b0229cc` |
