# Release and consumer handoff

HaveAPI master includes the repair at ed88e2a. The supported release branch is
784e113, tagged v0.29.9. All three Ruby packages and npm haveapi-client 0.29.9
are published. PHP mirror v0.29.9 is published through Packagist; its archive
matches all 35 reviewed files. The downloaded server gem matches the verified build and serves
all three repaired documents. The downloaded npm tarball passes registry
integrity checks and its JavaScript matches the reviewed release build.

Completed checks: 20 focused and 365 full server examples, seven exact release
CI workflows, independent whole-branch reviews, 31 packaged service examples,
and successful builds for both API hosts. The configuration pin patch was
cleanly rebased onto updated master and both hosts built again. Current local
generation: 2026-10-12--14-44-02, configuration revision 8e4da52c. No deployment
occurred. All reviewed feature heads are integrated; ready for user-owned deployment.

## Verification disposition

- Exact-head vpsAdmin API specs and four other workflows passed. The user
  explicitly waived waiting for full integration CI; observation ended and
  the server-side run was left untouched, last seen queued.
- User approved the listed master integrations and PHP tag. PHP was released
  first, then vpsAdmin and configuration were fast-forwarded and pushed. All
  registered exact heads are merged. All components of the 0.29.9 release are
  published; see [PHP evidence](php-published-artifact.json) and
  [integration proof](integration-result.json).
- The user handles deployment. Previous configuration service pin:
  b4ef8535a629ee8c9cd753afecdb05e0895d0eea. No migrations or state conversion;
  API instances may roll independently and nodes need no coordinated update.

## Integrated revisions

| Repository | Integrated target | Reviewed feature head | Complete feature series |
| --- | --- | --- | --- |
| vpsadmin | master | 7d911899d0d3d335546f6b3676b2eb46a291764d | 4d53979a, 7d911899 |
| vpsfree-cz-configuration | master | 8e4da52c55f1d4396547630d1d4de518f8255619 | 8e4da52c |
| haveapi-client-php | master, then v0.29.9 tag | 7fa4e35a9d9cb462320a4b2f2786bf84b8e024f2 | 7fa4e35 |

All branches are published, merged and clean. Their full histories and final diffs were
independently reviewed without findings; the configuration rebase preserves the
reviewed patch exactly, proven by range-diff and semantic lock comparison.
No migrations or obsolete update streams. Refreshed host builds passed at the
final configuration head; see [evidence](consumer-hosts-rebase-result.json).
No release/integration gate remains. The user deploys; no deployment or dry
activation was done.

## User-owned deployment and recovery

The built generation is available in the retained configuration feature
worktree. Deploy the two API hosts using confctl's documented generation option:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-diagnose-vpsadmin-api-exception/vpsfree-cz-configuration
nix develop -c confctl deploy --generation 2026-10-12--14-44-02 --one-by-one 'cz.vpsfree/vpsadmin/int.api*' switch
```

This is prepared operator guidance; the command was not executed. Its options
were checked against confctl deploy --help. API instances may update separately.
After deployment, check /doc/json-schema, /doc/protocol.md and
/doc/create-client.md return HTTP 200 with documentation content. Nodes need no
coordinated update for this repair, and there are no database/state conversions.

If rollback is needed, restore the previous vpsadmin service source pin
b4ef8535a629ee8c9cd753afecdb05e0895d0eea using the normal confctl channel operation
on a fresh rollback branch, then build/redeploy only the API hosts. Preserve
other configuration inputs. An existing known-good host generation can also
be selected through the same generation option. Restoring the old API package
restores its prior documentation behavior without data conversion.

## npm publication and automation recommendation

The login refresh resolved the original credential problem. The noninteractive
retry then failed with EOTP; the user completed publication interactively.
Registry artifact verification passed; see [evidence](npm-published-artifact.json).

The user deferred automation to a later task. For future unattended releases,
use npm trusted publishing from a dedicated
GitHub-hosted workflow in vpsfreecz/haveapi. Bind package haveapi-client to the
exact repository/workflow in npm settings, explicitly allow direct npm publish,
give the workflow id-token: write, and build/test/publish the tagged revision.
This needs npm >=11.5.1 and Node >=22.14.0. Self-hosted runners are currently
unsupported. Configure the binding near the next release: its first successful
publish must occur within two days. Correct clients/js/package.json's
repository.url from haveapi-client-js to haveapi, matching the actual workflow
repository. These are recommendations; no workflow or npm settings were changed.
[npm trusted publishing documentation](https://docs.npmjs.com/trusted-publishers/).

A scoped granular read/write token with Bypass 2FA can currently automate local
publication, but npm is removing direct token publication in January 2027.
Prefer trusted publishing for the lasting release path.
[npm access-token policy](https://docs.npmjs.com/about-access-tokens/).

[Release review](release-review.md), [consumer review](consumer-review.md),
[CI checkpoint](consumer-ci-checkpoint.json), [current state](state.md).
Session remains active and open; branches and owned auxiliary worktrees retained.
