# Release approval manifest

Prepared on 2026-07-24. No target tag or package version existed when this
manifest was prepared.

## Integrated source

- HaveAPI `master`:
  `efd0314bee237aa3df5f0189eddc7267c05c0fd1`.
- HaveAPI `haveapi-0.29`:
  `2d9edf01cf39963e6fd48282ae6c137c04e692dc`.
- `haveapi-client-php` `master`:
  `03201f582e37abc586a3ac308308808b0b663539`.

The master fix and release-branch backport have identical stable patch IDs.
Both HaveAPI commit sets passed every GitHub Actions component workflow.

## Downstream release heads

- vpsAdmin feature head:
  `fb28d1a708a7268786a818ca54bc4c3da371fa4f`.
- vpsfree-client feature head:
  `936536f59e34ba3be5a7de19d7c0ffc39b3839cc`.

The downstream default branches remain unchanged until their upstream package
dependencies are published and registry-backed checks can pass.

## Artifacts

Artifacts are stored in the ignored `dist/` directory of the HaveAPI 0.29
initiative worktree.

| Artifact | SHA-256 |
| --- | --- |
| `haveapi-0.29.5.gem` | `51f90402050a38f07cc3d13378c5639ee5ee77e98918b053af28ac6333778892` |
| `haveapi-client-0.29.5.gem` | `4d836c7d7d37a5295e3f81e24247a9c398c8888537d94b08d3e4d0168afe3eb6` |
| `haveapi-go-client-0.29.5.gem` | `95973461028a2f73701cbd95b45f2173a901d3bd6f2ad98c585f66d267df1208` |
| `haveapi-client.js` | `548afcc40266d62d4ddb86a434c25bbb2352b9f5a83ce03dbd80ca87f6307dd9` |
| `haveapi-client-0.29.5.tgz` | `d2dcf56b7966d0c6d2f9aeea9dbbef0ad170cc8b96103f4bae2eb22c78c6bd49` |
| `vpsadmin-client-4.2.0.gem` | `d33ca8bcb7b10071762f1236ed854ce1851719b466d9a018671538e354e5816e` |
| `vpsfree-client-0.20.0.gem` | `325751cfc215358d7cc05fcd494356ee4840dc4dd111867217bebd2c036126aa` |

The Nix hash for the exact HaveAPI Ruby-client release artifact is
`1diyzs51dl74sc44pn9phn4ci663m53l5ql17xg2k99pgmynr0sd`.

## Approved release sequence

1. Create and push annotated `v0.29.5` tags for HaveAPI
   `2d9edf01cf39963e6fd48282ae6c137c04e692dc` and the PHP mirror
   `03201f582e37abc586a3ac308308808b0b663539`.
2. From the HaveAPI 0.29 top-level Nix shell, publish the exact coordinated
   artifacts with `make publish`. Verify all three RubyGems packages, the npm
   package, Packagist metadata, and both tags before continuing.
3. Regenerate vpsAdmin's packaged-client metadata with
   `rake vpsadmin:gems:client`. It must retain HaveAPI 0.29.5 and the release
   artifact hash without an unexpected diff.
4. Rerun the vpsAdmin Client Specs workflow and verify the packaged Nix client
   now that HaveAPI 0.29.5 is registry-visible.
5. Fast-forward vpsAdmin `master` from a fresh target worktree, create and push
   lightweight tag `v4.2.0`, publish the exact vpsadmin-client gem, and verify
   its dependency on `haveapi-client ~> 0.29.5`.
6. Resolve vpsfree-client against RubyGems, fast-forward its `master`, create
   and push lightweight tag `v0.20.0`, publish the exact gem, and verify its
   dependency on `vpsadmin-client ~> 4.2`.
7. Perform a clean registry-backed install and, when operational access is
   appropriate, a Czech-account snapshot-download end-to-end check.

Stop the sequence immediately if a tag, checksum, version, dependency, or
registry result differs from this manifest.

## Approval scope

Approval authorizes the release-tag pushes and package publications listed
above. It also explicitly authorizes an exception to vpsAdmin's repository
guideline that normally says not to upload first-party gems to remote
RubyGems, because this initiative specifically requests public
`vpsadmin-client` and `vpsfree-client` releases.
