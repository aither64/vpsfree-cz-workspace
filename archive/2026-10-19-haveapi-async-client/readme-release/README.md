# README and release preparation audit

User requested project documentation for JavaScript and TypeScript consumers and
an up-to-date release process. One npm package ships JavaScript UMD and emitted
types, exposing callback and async APIs. No version release is requested.

| Owner | Result | Acceptance and checks |
| --- | --- | --- |
| architect0 | Bounded design recorded before implementation | Existing build retained; only demonstrated release gaps fixed |
| implementer0 | Release checks committed as 3a79c8ec | 49 release specs, scoped lint, syntax, metadata and hooks pass |
| implementer1 | Three docs committed as 40365b47 | Main fact/prose pass, 18 local links, whitespace and hooks pass |
| reviewer0 | Independent final review accepted | All four lanes; complete history, update streams and migrations |
| lead | Scope, acceptance and user contact | No release or WebUI history mutation inferred |

Final HaveAPI head: 40365b47a1a0c946367bc4596db6060853b52c0a.
Tree: 3fe6010640cf64a063731fe8c49eb5819ca94b59. Working tree/index clean.
The eight-commit complete range starts at c58704a08451a231fdf6c6123437133422af46dc
(see full review and Git inventory).

The version target now updates both lock root versions, release JS dependencies
use npm ci, and package checks cover required files plus isolated installed CJS
and TypeScript consumers. Actual install/pack proof passed once after independent review: normal npm
installation, both runtime constructors and strict installed types passed. All51
packed files equal final source; runtime+44 declarations equal f94 and only the
packaged README differs. Final source stayed clean.

The root README updates only the client-list entry, per user direction. The
component README explains the package, callback/async APIs, shipped declarations
and setup-free low-level async requests. The release guide
matches implemented checks and retains the existing protected publication and
retained-artifact workflow.

[Review packet](final-review-packet.md), [code inventory](owner0/inventory.md),
[corrected documentation](owner1-overview-correction/receipt.json),
[installed-package proof](owner0/post-review/result.json).
WebUI's existing exact f94 archive is unchanged. Its separate history approval
and subsequent verification remain pending; no WebUI operation occurs here.

Current phase: reviewed, corrected, locally verified and published on the
HaveAPI development branch at40365b47. Remote exact head verified; masterc587
unchanged. One-shot CI: i18n, RuboCop and JS pass; release and RubyRSpec in progress.
No CI wait/dispatch/rerun. No package version released, deployment or lifecycle
action. [Publication receipt](owner0/publication/receipt.json).
