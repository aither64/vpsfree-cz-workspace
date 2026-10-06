# Scope and proportionality review

## Blocking

No findings.

## Important

### 1. The configuration series permanently retains a superseded and unsafe rollout procedure

**Location:** `vpsfree-cz-configuration`, commits
`aa51729375e9041d263802be16deae6f12375dd9` and
`ad6c41ea295ee6ae45b2fd2f9c806bf74f2a1f9e`,
`docs/operations/vpsadmin-password-recovery-deployment.md:67-84` and
`:102-122` as introduced by `aa517293`.

The first runbook commit says that old and new API processes may overlap while
recovery is disabled and directs the operator to upload templates manually with
an authenticated Rake invocation. The later `ad6c41ea` commit replaces both
instructions: the accepted final design requires a no-overlap writer cutover
even while recovery is disabled, and the authoritative external template
package is reconciled declaratively before the API starts. The final tree is
safe, so this is not a blocking defect in the delivered behavior. However,
fast-forward integration would preserve a release-specific operator guide whose
intermediate version contradicts the final safety decision. A backport,
cherry-pick, bisect checkout, or future history investigation can therefore
surface plausible but unsafe deployment instructions, and reviewers and
operators must reconstruct which of two rollout designs is authoritative.

The smallest remediation is to rebuild these documentation commits so the
runbook is introduced once in its final form: fold the relevant `ad6c41ea`
changes into `aa517293` (or replace both with one final runbook commit). Keep the
generated template and vpsAdmin pin commits separate and verbatim.

### 2. Two vpsAdmin changes remain split from commits that are knowingly incomplete without them

**Locations:**

- `bd32e162892bd04665177731744115bcab6c403e` adds
  `api/spec/api/resources/password_change_log_spec.rb`, but its
  `.github/workflows/api-specs.yml:96-109` topic list omits that spec.
  `1fae19609a819aed3806ae7ffd124dc43087daab` adds the missing entry at line
  108 after the topic-coverage job rejected the branch.
- `44c6144e8d2fe7109a524a7c6405eed941914c1e` adds administrator attribution
  in `webui/forms/users.forms.php:350-379` while resolving
  `user_session.user` for every administrator-visible history row, including
  valid recovery and forced-reset rows with no initiating session.
  `f15d19547ed299339e1809409be5322a154c563e` moves that resolution behind the
  session-presence check at `webui/forms/users.forms.php:350-377` and adds the
  missing sessionless scenario.

These are not speculative features, and their final implementations belong in
scope. The proportionality problem is their permanent separation from the
functional commits they make valid. The branch is intended for fast-forward
integration, so retaining them leaves individual commits unsuitable for the
repository's required checks or valid production data. That makes later
bisects and selective backports unreliable and forces maintainers to remember
which follow-up is inseparable from which feature commit.

The smallest remediation is to autosquash `1fae19609` into `bd32e162` and
`f15d19547` into `44c6144e`, preserving the final code and tests exactly.

## Advisory

No findings.

## Assessment and residual gaps

I reviewed the complete committed ranges from the packet, rather than only the
latest rebase:

- `vpsadmin`: `61d2ef6e712345200daddff3abcb4697c028d176` through
  `a2e6d8037c737c61c15bfd845c1b3c57d894f310`
- `vpsfree-mail-templates`: `9e1ddbd973703cf48a43f0e5afc2bfb392a8b676`
  through `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11`
- `vpsfree-kb-contracts`: `81d6d7dfe530884aff3e1d2634e02e4b12fe28e8`
  through `6d8ab17db3ce8ffc41216feeb90bff8468b4d39d`
- `vpsfree-cz-configuration`:
  `b4e120294696578c3871124259f266205bad4393` through
  `8928b2aba9230202e805aa5489dc9f7369650ac7`

The feature is broad, but the apparent complexity has concrete consumers and
maps to explicit plan decisions: the queue/request/recovery split supports
account-neutral bounded submission and grouped delivery; authentication
generation and factor snapshots serialize credential changes and revoke the
exact verified factor; OAuth client persistence, interactive starts, deletion
cancellation, and session reconciliation implement the accepted client and
rollback contracts; counters and detailed logs serve distinct monitoring and
audit lifecycles; external templates, proxy compatibility, alerts, pins, and
the production runbook implement the chosen deployment model. The mail and KB
series add only the requested user-facing messages and managed documentation
contract. I found no smaller design that preserves the stated behavior,
security, compatibility, and operational requirements.

This was a static scope review. Per the review coordination constraints, I did
not run tests, install dependencies, start services, manipulate refs, or touch
the development cluster. Runtime correctness and integration behavior remain
covered by the packet's existing verification and the other mandatory review
lanes; this report does not independently revalidate them.
