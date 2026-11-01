# PR74 publication plan — final concrete candidate, not executed

PR https://github.com/vpsfreecz/vpsadmin-webui/pull/74 targets main.
Repository git@github.com:vpsfreecz/vpsadmin-webui.git.
Old remote head alias refs/heads/dev/haveapi-async-client.
Own registered branch refs/heads/dev/vpsadmin-haveapi-upgrade.
User permits PR reuse; exact published-commit rewrite authorization is still
required. GitHub cannot change the PR head branch to our new branch.

Old base `7860521f30826c3886c89c35e8ab6f4e082e0a4b`.
Old published head `5dd2333b9af230d4a81c8f772cbbb08d39b14913`.
Exact published range to replace:
`7860521f30826c3886c89c35e8ab6f4e082e0a4b..5dd2333b9af230d4a81c8f772cbbb08d39b14913`.
Its two published commits:

- `0d05a2584bf30ee4acfa1d64bf00325cdda62934`: injectable package pilot.
- `5dd2333b9af230d4a81c8f772cbbb08d39b14913`: prior package proof docs.

Authorized old final local production source also includes
`3b2eed453f385ee37d07c7339edcce8fc28ffd31` archive dependency and
`8772bab21cd8739bf4672cdf4976aea2a6e59de3` production successor.
Full old local content range:
`7860521f30826c3886c89c35e8ab6f4e082e0a4b..8772bab21cd8739bf4672cdf4976aea2a6e59de3`.
These old local branches/worktrees/records and PR63 remain untouched.

Final new base `5a2d2bdc3ad7a827038f877d75959916528db844`.
Final head `757f7fd8c2d5d3a4d1f6ee464acd29a5a2502176`.
Complete new range:
`5a2d2bdc3ad7a827038f877d75959916528db844..757f7fd8c2d5d3a4d1f6ee464acd29a5a2502176`.
Two logical commits:02b45a7d final registry0.30.2 dependency/provenance/Nix hash,
757f7fd8 production adapter/tests/docs with closed R2 uncertainty correction.
All current-main overlap behavior and original authors/dates preserved.
No migrations, released/deployed boundary or external consumption. Source8772bab
is a nonancestor content source; do not call it literally merged.

Prior independently reviewed/R2-closed C range ended014f7b9c9f451d6275af73c4af30a24668b77b7b,
retained at refs/heads/dev/vpsadmin-haveapi-upgrade-reviewed-0301. Exact old/new
range-diff, source map, tree/author proof and0.30.2 checks under0.30.2/.
The final approval candidate is757f7fd8, not the superseded0.30.1 head.

Ordered execution conditions:

1. Complete independent exact-final review and longer required verification.
2. Publish only own branch over SSH; verify exact remote final head.
3. Lead presents this concrete old/new range, source mapping and no-migrations
   conclusion for explicit authorization to rewrite the two published commits.
4. After approval, freshly inspect PR74 and ls-remote exact head alias. If its
   old head changed from approved5dd2333b, stop and refer the new range to lead.
5. Only under that approval, intended exact-lease command is:

   git push origin 757f7fd8c2d5d3a4d1f6ee464acd29a5a2502176:refs/heads/dev/haveapi-async-client --force-with-lease=refs/heads/dev/haveapi-async-client:5dd2333b9af230d4a81c8f772cbbb08d39b14913

6. Verify own branch and PR74 head both equal757f7fd8, PR still targets main;
   cancel only superseded queued/in-progress CI on that exact head branch.
7. Record fresh lease/both remote heads and update PR metadata as lead directs.

Own registration/tracking stays on its own remote branch. PR74 is a second
publication alias, not reassignment of the old session's local registration.
Nothing here authorizes main integration, deployment or session lifecycle action.
