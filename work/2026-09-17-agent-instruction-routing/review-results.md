# Review findings and reconciliation

All reviews use fresh gpt-6-astra/xhigh and no nested agents. Initial heads are
recorded in review-packet.md. Overall risk: high because routes cover existing
authorization, destructive-operation, deployment and recovery rules.

General, architecture and risk completed independent committed-tree reviews.
All confirmed zero lost original paragraphs (134 across the four changed files).
All Important findings are accepted for narrow trigger/coverage remediation:

- General, architecture, risk: route push-only work to verification.md so CI
  feedback and superseded-run cancellation cannot be missed.
- General/risk Important, architecture Advisory: route downstream configuration
  pin updates to git.md to preserve the upstream fetch/rebase prerequisite.
- General, architecture, risk: route selecting/running existing tests to testing.md
  in vpsAdminOS; apply the equivalent correction in vpsAdmin. This preserves the
  local runner/environment selection even for verification-only work. Architecture
  clarified that current flakes include local tracked sources, so do not claim
  all packaged execution necessarily uses stale code; untracked additions are one
  concrete distinction.
- Risk: include all session mutations and workspace suspension in the lifecycle
  route, preserving unfinished-journal recovery requirements.
- General: include security-advisories at its actual nonstandard remote default
  branch. Confirmed by ls-remote HEAD, audited its full AGENTS.md, and retained its
  cohesive assessment workflow; an ordinary CVE task needs the full procedure.
  Separately record the eleven canonical repositories with no instruction file.

Scope review completed: one Important finding that summaries broadened the
original data-integrity requirement from tests of listed operations to every
operation. Narrowed the vpsAdmin summary; discarded the entire unmerged
vpsAdminOS extraction because its typical development/test context increased
from 5,231 to 6,916 bytes despite an 815-byte core saving. Its original AGENTS.md
remains unchanged. Branch retained at its original base; no published history
was rewritten. Scope reduction needs no review rerun. These fixes broaden trigger coverage without changing
any preserved procedure or the design; focused verification is appropriate under
the review skill, without rerunning unaffected lanes. Behavioral cases will cover
the previously missed actions. No Blocking findings were reported.

Final remediated heads:

- haveapi: `a2fc755452db60dac919205829fda6db362e3fce`.
- vpsadmin: `941451cffe415850e15b29813937fc5e035456c0`.
- workspace: `7f33403e3ca5e002054f02fb442b82763e065b1f`.

## Packaged-check remediation

Final workspace head: `c8889ea85682f5e673ac243e27f533ecc7ef3700`.
Nix evaluation rejected two `checks.${system}.…` definitions of the same dynamic
attribute. Grouped the existing deployment-contract and new instruction checks
in one `checks.${system}` attrset, preserving both derivation bodies. Evaluation
then returned both check names. The builder's C locale exposed Ruby's implicit
US-ASCII reads of Czech procedure text; the guard now reads Markdown explicitly
as UTF-8. `LC_ALL=C ruby test/agent_instructions_test.rb` and both Nix-packaged
checks passed. Focused inspection covered these mechanical test-wiring fixes;
no instruction text, routing policy, contract or scope changed, so no review
lane or behavioral scenario was rerun. Earlier three/four-project review
snapshots remain recorded above rather than relabeled as this final commit.
