# Final revision-label cleanup

This bounded required wording update supersedes the final heads in
`package-a-expanded.md`. Its implementation, CI diagnosis, migration conclusion
and broader evidence remain applicable; no acceptance test result is added here.

## Exact final source and pin ranges

| Repository | Base | Before wording fix | Final head |
| --- | --- | --- | --- |
| vpsadmin | `610a96f8ce523afbcd3e4374a70047dbe3264b0d` | `fb53edcb2326cd6c7d7bc638b3a0d86f4323deb4` | `218e3180896debd3006b9a0583e557286702761d` |
| vpsfree-kb-contracts | `ce2c8cd9358c3636e5d39343e595df813a0b197f` | `938942f5235098faa0fa39a61fd4be42c488a969` | `21c5213256c28f4a65fd582485e07234a02f5f55` |

Fresh SSH fetch/ls-remote proves both final feature heads and unchanged master
bases. Both worktrees/indexes are clean and comparison captures refreshed.
Earlier expanded heads remain reachable through each repository's local
`2026-11-01-published-advisory-corrections-pre-labels` branch. No default branch
was rewritten, merged or deployed.

Final vpsAdmin A is `866bccf1a8e1d7f758012cb4d6490c0f3af2cb34`; B is the final
head above. History still has exactly two logical commits. KB history has exactly
one five-pin commit. No migrations or supported-history boundary changed.

## Metadata-only equivalence

The final source difference from the pre-wording expanded head is three paths,
five insertions and one deletion:

- Explicit `label: 'Expected content revision'` in root, node and CVE shared
  precondition declarations, plus Publish's standalone revision declaration.
- Generated English `expected_content_revision.label` changes from
  `Expected_content_revision` to `Expected content revision`.

Czech locale bytes are unchanged, retaining `Očekávaná revize obsahu`. The lead
directly approved these exact labels. No parameter, type, enum, validator,
description, behavior, test or documentation content changed. Giving Publish the
same explicit label prevents the generator splitting one common translation
into scoped keys with missing Czech defaults.

The saved exact patch is checked against those source-line additions and that
single English replacement. A was amended at the first rebase edit stop; B was
replayed without edits and its full binary diff is byte-identical to the prior
B commit. `range-diff.txt` records old/new complete ranges. Final tree
`27b1d1327541f2137a347c9b240d965263c66f88` equals the intended captured tree.
This limited wording equivalence does not reuse the earlier narrower review or
certify final expanded readiness; the new final review uses the new full range.

## Checks and KB refresh

Final locale normalization/health, two-file RuboCop and Ruby syntax passed exit 0
in about 127 seconds. Fresh watcher `01a19862-4ab7-7071-b234-3c04ea220ba9` used
the retained Luna/low utility and verified full-access/never policy. The first
normalization exposed scoped Czech TODOs while Publish retained a default label;
uniform source labels resolved the actual cause, with no generated-key churn in
the final diff.

The A amendment passed every mandatory pre-commit hook, including root RuboCop and
both locale health hooks. Commit-message hooks passed with the existing advisory
width warnings. Fresh observer `01a19865-8274-7161-9070-55e2ae112cd8` reported
the parent-owned fold complete in 66.19 seconds, clean and with exact B equality.

D regenerated only the selected `vpsadmin` lock node and refreshed the same four
source pins to final vpsAdmin. The explicit vpsAdminOS revision
`6bdf458fd9105379860234ff33d352e55844f08f`, every other node/root follows,
capture provenance, pages and assets are unchanged. Pinned-shell JSON/YAML/Nix
parse, exact five-pin/graph/provenance checks and diff checks passed. D remains
five files, eight insertions/deletions over its original base. No strict full
`bin/check`, browser acceptance or application suite was started.

Raw exact patch, range diff, intended-tree/fold status and logs are in
`/tmp/2026-11-01-published-advisory-corrections-labels/`; D old inputs, lock graph
and quick checks are under its `kb/` directory. All owned operations completed;
the utility slot was released to E.

Current source CI identities: CI `41337574315`, i18n `41337574263`, RuboCop
`41337574264`, API Specs `41337574258`, Webui PHPUnit `41337574308`. KB:
Managed page runtime `41337657793`, Check `41337657622`. Runs were listed only,
not awaited for acceptance. Cancellation was requested only for superseded
same-branch runs: vpsAdmin `41335692937`/`41335693055` and KB `41336064109`.
All three are confirmed completed/cancelled at their superseded heads; no
current-head run was canceled.

Next: expanded independent final review of the new exact complete ranges, then
the assigned bounded full/core/plugin/concurrency, legacy browser and strict KB
checks. No integration, deployment, production or lifecycle action is authorized.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/>
