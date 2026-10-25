# HaveAPI 0.30 source backports complete

The held patch feature now ends at `8591394e13144431b27ecb366aae2b7b77a94e2c`. Five normal `cherry-pick -x` commits were appended to `8270b519`; the existing six genuine backports are unchanged. Each new intermediate tree and stable patch ID equals its master source. Required Overcommit diff and commit-message checks passed for all five; no hook was bypassed.

The complete preversion tree is `80804b1c0c3ed33fc4b086673dbc3618a789cd4f`, exactly equal to integrated master `67fcd34b`. All 775 tracked file modes, blobs and SHA-256 hashes match the accepted source export. Full b64-to-final diffs are byte-identical (SHA256 `bf284357888973d98a9eb81bd8b39dd167c88d52406b7abbc8d6e344237ade38`). All11 commits retain ordered genuine provenance; no migration or source deviation was introduced.

VERSION remains `0.30.0`; the old CHANGELOG section is unchanged. The held ignored root lock remains `7c48d2c2…`. Known ignored files, current source166 inputs/5 locks/47 outputs, original artifacts, native tool closure/configuration/signatures and all other refs remain exact. Fresh SSH maps before/after are identical: master67, supported0.30 b64, original tags and feature refs preserved. Only the owned local patch branch head moved.

The registered patch comparison was captured at b64→8591394e before versioning. No tests/compiler campaign, install, package rebuild, push, default mutation, version/changelog change, tag/publication, claim or lifecycle action ran. The source package is yielded command-free, with no utility/process/claim owned by implementer0. Owner1 may now use its separate setup grant; versioning still requires the lead’s next package.

| Master source | Patch backport |
| --- | --- |
| `4dc0f7e11c494d1a0dc852dabcc312411699fcab` | `682a9869f7b3cfb90e25b330dc6d138d36e27b46` |
| `6cb3c3e80b827b665e00da3de588d97eb9d00ec3` | `a252adbc94bce918c2605e503c3582853ec0a483` |
| `f08d3f63cd1d4e4dc6731bad81ec6f34d6228921` | `d7bfed7778aac9d34384d82669b45d39a9330cb7` |
| `dc52a7a52d0991b597f44cd5bd8901eec92259f9` | `9c5de16776a964dadf1b886b5d22f3b7183a3414` |
| `67fcd34ba506264a5c7ee2e8e18a88d221c6f469` | `8591394e13144431b27ecb366aae2b7b77a94e2c` |

No product documentation edit was needed for a byte-equivalent source backport. The accepted implementation docs remain unchanged. The lead owns shared state reconciliation from this receipt.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
