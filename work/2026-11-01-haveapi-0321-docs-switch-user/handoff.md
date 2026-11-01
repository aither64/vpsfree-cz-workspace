# HaveAPI patch-release handoff

HaveAPI 0.32.1 is published and verified at all maintained destinations. The
originating lead has received exact release provenance and install evidence.

The provider-neutral documentation OAuth extension accepts:

    switch_user: true,
    switch_user_revoke_params: { 'close_sso' => '1' }

Only validated Switch user requests add these parameters to revoke POST. Ordinary
Sign out is unchanged. HaveAPI protects credentials, token and token_type_hint;
the provider owns SSO semantics. Upgrade every worker before enabling the option
and remove it before reverting to an older library. Initial fixed docs-cookie
expiry remains unchanged.

## Integrated source and published release

- master: 391b0190241cf195a69b06f7297d3e4eebec5a83; shared VERSION 0.32.0.
- haveapi-0.32: 9efeadf91d894e01d1d4f4a3e3fc64c6309785c7; VERSION 0.32.1.
- v0.32.1 annotated object: ceebc179cd4266ac4353360acf248f8d7493d5bf;
  source is the exact stable head above.
- https://github.com/vpsfreecz/haveapi/releases/tag/v0.32.1
- Release run: https://github.com/vpsfreecz/haveapi/actions/runs/41333460242
- Original artifact: 13094149459, release-41333460242.
- Manifest SHA256:
  37d48672acfbef768f10bb1b86787880a215056b5dc092e48ee8b6db348abe0d.

The patch includes the OAuth source/test/guide fix, the sole existing master-only
CI baseline correction 209a7ac0, and a seven-line release-fixture correction found
by stable CI. All backports retain -x provenance. Patch version metadata stays on
stable; published history was preserved. Recovery refs retain original targets
and previously reviewed feature heads.

## Verification

Focused OAuth/CI baseline: 152 examples, zero failures; lint, mandatory hooks and
release metadata checks pass. Fresh independent Astra/xhigh review passed all
four lanes; affected fixture/history review also had no findings. Complete final
histories, backport equivalence and no-migration conclusions are in review.md and
review-fixtures.md. No external dependency update, database/schema/persisted-format
change, production deployment or consumer runtime campaign.

Original branch CI exposed two pre-existing patch-incompatible release fixtures.
The real master patch-zero guard correctly rejected their setup. The minimal
fixture fix preserved that guard; affected branch builds and all subsequent tag
checks passed. Original failure evidence is retained. Tagged candidate artifacts
were downloaded and verified before protected publication approval.

## Published package and registry/install evidence

All five RubyGems packages are published at 0.32.1: haveapi, haveapi-client,
haveapi-go-client, haveapi-rust-client and haveapi-typescript-client. Actual
registry bytes match the approved manifest; conventional isolated installation,
explicit activation and loading passed for all five. All 154 loaded HaveAPI files
came from those isolated registry packages. Ruby client and configured
DocumentationOAuth constructors passed. The finite check took 19 seconds and
reused prepared external dependencies.

npm tarball and both PyPI artifacts match the approved hashes. PHP mirror/master/
tag and Packagist 0.32.1 point to 4b3260d36a070ad9590ff6c3ee8a91eb873b4e84,
with exact HaveAPI source provenance. Public GitHub assets match the retained
candidate; public manifest is byte-identical. See [artifact-verification.md](artifact-verification.md)
for complete hashes, commands and proof limits, and [release.md](release.md) for
integration/tag/approval receipts. No package version split.

## Ownership and next action

The originating session 2026-10-24-vpsadmin-haveapi-upgrade owns vpsAdmin adoption,
consumer wiring, site setup docs and vpsfree-cz-configuration channels, using quick
verification only. This session owns HaveAPI source/publication evidence and
lead-to-lead readiness notice. No machine ownership or deployment. Repository
claim was released and verified released after integration. Keep session open;
no archive/delete/stop/cleanup is authorized.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-haveapi-0321-docs-switch-user/
