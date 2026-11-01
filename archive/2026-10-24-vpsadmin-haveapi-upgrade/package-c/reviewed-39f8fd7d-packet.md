# Package C final review input

Status: complete committed Package C, ready for lead-coordinated final review.
Lead owns reviewer assignment and final review acceptance; do not treat this
file as an early review request.

## Outcome and boundary

React WebUI adopts the actual published npm `haveapi-client@0.30.1` AsyncClient
for all ordinary authenticated, public and fallback-description requests. The
library owns wire encoding/decoding and XHR; WebUI preserves live credentials,
locale, BFF renewal/session identity, one bounded read retry, mutation
non-replay, domain results/metadata and uncertain-operation safeguards.
Actual installed declarations, controlled-XHR API fixtures and ordinary browser
entry tests verify the boundary. No alternate transport, pilot/toggle,
local tarball override, BFF product edits, merge or deployment.

Session: `work/2026-10-24-vpsadmin-haveapi-upgrade/{plan,state,design}.md`.
Worktree:
`worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui`.
Repository: `git@github.com:vpsfreecz/vpsadmin-webui.git`; target `main`.
Branch: `dev/vpsadmin-haveapi-upgrade`.
Base: `5a2d2bdc3ad7a827038f877d75959916528db844`; head `39f8fd7d2bee0c4754f0f9921d97855da7fbdddf`.

## History and migration review

Read `receipt.md`, `source-paths.json` and `content-mapping.json`. The old local
`7860521f..8772bab2` series is read-only source, including obsolete pilot and
vendored pin. Its final production content is reconstructed on fresh main,
preserving original author Jakub Skokan. Current main's seven overlapping
paths are reconciled; current member/node features and E2E type scope survive.
Old pilot, pilot proof and vendor commits are not replayed. One final dependency
stream selects registry 0.30.1 directly, with one separate production adaptation
commit. No intermediate pin, superseded implementation, migration or supported
consumer boundary requires retention.

No migrations: neither database schema nor persisted formats change. The old
source branch was not merged/released/deployed according to the accepted source
records/design. New source has no deployment or external consumer. The old local
head is nonancestor carried source, not a literally merged ancestor. PR74 remains
at `5dd2333b9af230d4a81c8f772cbbb08d39b14913`; PR63 remains untouched.
Require explicit independent whole-branch history/consolidation and no-migrations
conclusions, not only final-tree code review.

## Review risk and lanes

Overall risk: high, due to authenticated transport, public isolation, renewal
and mutation ambiguity. Applicable lanes: General, Architecture and repetition,
Scope and proportionality, Risk and compatibility. Lead selects retained
reviewer0 from fresh roster (saved `gpt-6.1-sol` / `xhigh`, read-only) without
model/effort overrides and supplies mandatory-change-review plus all four lane
references. This package's owner read the skill and every applicable lane.

Inspect real AsyncError classification and original response/meta receipts,
per-base/scope lazy instances, original retry inputs/language, no write retry,
logout/identity/impersonation guards, 401 protocol ambiguity, malformed envelope
handling, abort/timeout settlement, and domain action-state receipts. Preserve
current node overview/capability test and current typed E2E adoption. Do not
infer that controlled HTTP fixtures certify live OAuth or backend capability.

Provider/consumer: HaveAPI owns low-level RequestSpec, AsyncClient, AsyncError;
WebUI's `haveapiRequestClient.ts` owns translation into its existing policy and
`haveapi.ts` owns admission/renewal/result projection. All domain API wrappers
consume the latter. BFF config/session/OAuth remain separate protocols; legacy
callback JS in vpsadmin is Package A, not a reason for frontend callback use.
Registry source commit/tag/integrity are in the project provenance record;
all 53 packed files match the attested HaveAPI source.

## Documentation and verification

Current project contracts: docs/design/{API_CONTRACTS,ARCHITECTURE,DOMAIN_COVERAGE,
HAVEAPI_CLIENT,PACKAGING,README,REQUIREMENTS,VERIFICATION}.md and regenerated
IMPLEMENTATION_INVENTORY.md. One dated docs/work-log/2026-10-24 record links from
WORK_LOG.md. These are developer-facing English; no catalog/UI/BFF prose edits.
No separate operations procedure is needed: existing matching-release rollback,
session store/credentials and independent frontend/BFF packaging remain valid.
Exact temporary review/publication steps stay in this session directory.

Quick receipt and logs: `receipt.md`, `npm-setup.log`, `quick-batch.log`,
`scoped-quick-final.log`, `final-adapter-quick.log` and remaining-checks.log.
Final results will be appended. Initial 324 API cases plus 62 follow-up cases
and six source-check cases passed; scopes overlap and must not be summed.

After final committed-deliverable independent review only: full unit suite,
normal production build, Nix frontend/provenance/source/package checks and
ordinary desktop/mobile fixture workflows for public overview, authenticated
home, renewal/expiry, failure and relevant VPS action state. No deployment is
authorized. The live API/OAuth proof gap remains explicit.

## Final committed series and quick conclusion

Exact final range:
`5a2d2bdc3ad7a827038f877d75959916528db844..39f8fd7d2bee0c4754f0f9921d97855da7fbdddf`.

1. `cd3577a6365685273c1b39a724814f7d67931508`
   deps: adopt the released HaveAPI 0.30.1 client.
   Root manifest/lock, ordinary Nix hash, registry provenance and source-security
   guards/tests form one final update stream.
2. `39f8fd7d2bee0c4754f0f9921d97855da7fbdddf`
   api: use the released HaveAPI AsyncClient in production.
   Carried adapter/policy, API fixtures, ordinary browser assertions, typed
   coverage, current design contracts and dated work log belong to this behavior.

Complete series: `commit-series.txt`; full final diff: `final.diff`;
stat: `final-stat.txt`; mapping: `content-mapping.json`. Clean worktree after
both commits. Both commit authors retain Jakub Skokan's configured/carried
identity. No hook framework declared; actual canonical hooks are samples only.
No obsolete history, repeated dependency streams or migrations remain in the new
series. Reviewer must independently assess that conclusion.

Final quick acceptance: full `ci:quick` passed. Domain API 324 cases passed;
after cause/timeout follow-up, installed declarations typecheck and 62 focused
cases plus six source guard cases passed. The gate's included typecheck/audits
also passed on the final source. Audit: zero production vulnerabilities.
409 registry signatures/101 attestations verified. New root hash:
`sha256-yz+FSmc+aZDCwoNF6PiI9VUAbAXlMwzRqyi6Mjdt+e0=`.
Only Nix hash/docs/work-log evidence was updated after the broad quick run;
final design audit and diff whitespace check were repeated after commits.
The install's seven development-toolchain audit findings were preexisting;
no unrelated forced dependency refresh. Nix prefetch's six bundled optional
missing-URL warnings remain for post-review build verification.

No branch push, PR update, integration or deployment performed. Own branch may
publish after final review per lead direction. PR74 reuse plan is separate in
`pr74-publication-plan.md`, requiring exact published-commit rewrite approval.
