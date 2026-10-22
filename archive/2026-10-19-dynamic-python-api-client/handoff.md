# Python HaveAPI client — merge blocked by coordinator

HaveAPI/master is merged at exact reviewedc1823f3, and all five postmerge CI
workflows pass. The release build passed with package publication skipped. The
repository claim is released; no operation remains active. User-directed merge
is complete, no release/tag/version/package publication made. Session stays open,
feature/recovery refs and retained stash preserved. See
[native-merge-evidence.md](native-merge-evidence.md) and
[merge-completion.json](merge-completion.json).

Feature: https://github.com/vpsfreecz/haveapi/tree/2026-10-19-dynamic-python-api-client

Final head `326c05b78cec149b81e2c516c5cdcb7d1810d678`,
tree `0882b639badb5c917dd20918f63a803058001785`,
base/fetched origin/master `c58704a08451a231fdf6c6123437133422af46dc`.
Seven coherent owning commits, clean checkout, normal hooks and exact fold tree
receipts. No migrations, obsolete fixes or repeated dependency streams. Original
and affected independent reviews plus directly checked narrow reductions are
recorded in review.md, review-followup.md and token-review.md.

Client: `clients/python`, distribution `haveapi-client`, import `haveapi_client`,
Python3.11+. Sync Client and AsyncClient share immutable discovery, protocol and
authentication policy; HTTPX/AnyIO, typed inputs/errors, explicit pagination and
operation waiting, advertised resumable authentication. uv tooling, Ruff/mypy,
hooks/CI, vpsAdmin examples and trusted PyPI release workflow are included.
Project README/CONTRIBUTING own lasting usage/compatibility contracts.

Verification:

- 261 unit tests, strict mypy18, Ruff38 and46 actual Rack cases pass.
- 59 generic server/Rack integration cases, standalone wheel/sdist rebuild/install,
  34release specs and6artifact tests pass.
- Real core vpsAdmin fb2f512 with released HaveAPI0.29.12: eight scenarios passed
  initially; corrected sync/async revoked/expired-token proof passed2examples at
  final326c05b. No runtime change was needed for the invalid OPTIONS expectation.
- All five final-head workflows succeed: Python39337780111 (3.11–3.15, package
  installs and real generic server), release39337779915 (build/artifact checks,
  publication skipped), RubyRSpec39337779942, RuboCop39337779958,
  i18n39337779914. Evidence in verification-summary.md and verification/.

GET follows documented lossless Rack subset; unsupported structures fail locally.
POST/PUT/DELETE use server-authoritative JSON object roots/namespaces. Async waits
have an overall deadline; sync in-flight HTTP retains documented per-phase limits.
API-only vpsAdmin proof does not cover actual node/VPS lifecycle or browser auth.

Maintainer actions remaining:

- Explicit integration direction for HaveAPI/master; no merge has occurred.
- Confirm PyPI name ownership and configure trusted publisher for vpsfreecz/haveapi,
  release.yml and protected release environment before an authorized version
  release. Shared HaveAPI VERSION/tags apply; no registry publication occurred.

No deployment, tag, registry write or session closure was performed. Retain all
feature/recovery refs and the original recovery stash. No owned verification
process remains. Further tracking changes are uncommitted under daily cadence;
initial and daily implementation/review checkpoints remain preserved.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-dynamic-python-api-client/

## Newcomer README clarification

User-requested Python README introduction added atc1823f3. Defines vpsAdmin as
vpsFree.cz VPS control panel, main HaveAPI user, and explains examples choice.
Four added lines only, normalhooks/link/Markdown checks and independent
retainedreviewer general-only review pass. No runtime change or additional
local integration needed. Original verified326c05b remains unchanged parent.
Feature publication/CI inventory follows normal documentation update policy.

README follow-upc1823f3 published normally; general-only independent review and
all3newheadCI checks pass. Currentheadc1823f3, runtime-parent326c05b unchanged.
No blocker remains; ready awaiting explicit HaveAPI/master integration approval.

## Authorized integration

User reports PyPI account and pending publisher created and explicitly directs
HaveAPI client merge into master, with no release. Lead prepares merge_only
coordinator request binding exact reviewedc1823f3, basec58704a and accepted
independent review/history/migration receipts. impl1 owns premerge SSH fetch and
clean fullseries check; coordinator alone will FF/pushmaster. No tag/version/
release/registry/deploy/lifecycle operation is included. Session remains open.

Merge-only background integration admittedrun a9c23f6e-036d-4680-b06b-4b27701c0393
for exactc1823f3, targetmaster, originalbasec58704a. Matching retained lead owns
native notifications, source frozen. Phaseprepare at initial/status receipt;
master not yet claimed integrated. NO RELEASE/version/tag/registry operation.

Coordinator merge prep blocked before submission by Overcommit trust signature;
no master change. Hand-off acknowledged, impl1 owns inspected ordinary signing,
then lead resumes same run. This is hook environment recovery, no source/public
behavior delta and no authorization expansion. NO RELEASE remains enforced.

Current merge remains blocked/unsubmitted by diagnosed coordinator+Overcommit
single-signature conflict. Ordinary integration run paused atprepare; session is
stillopen. Architect/owner found no supported sign-only env/config solution.
User needs decide separate runtime-fix scope; HaveAPI merge approval remains
recorded, NO RELEASE. See merge-blocker.md and separate recovery evidence.

## Updated coordinator claim flow

User reports coordinator reworked and asks finishmerge. Selectedruntime
/nix/store/i2q0yyjkyvd0x3qa3cy9jafr1jmgxc70-dev-workspace-0.2.0 now grants
resourceclaims; session owns ordinary Git/hooks instead of automaticcheckout.
Oldunsubmittedruna9c23f6e canceled via officialinterface (no jobs/effects), retained
history. HaveAPI repositoryclaimfa9aac60-c9e4-45fb-b21e-6433a2e609b6 held; impl1
owns native preflight, then approvedFFmerge under claim, no releases. This
supersedes earlier instruction to resume olddriver; no ledger/payload edits.
