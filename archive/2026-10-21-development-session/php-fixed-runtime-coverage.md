# Fixed PHP web-runtime coverage and Foto shutdown

Independent evidence: implementer1, 2026-10-21. Exact session/environment
verified as `2026-10-21-development-session`. No CLI checks, builds, live probes,
deployment, source edits or Git mutations by this package.

## Acceptance result

**PASS at source/evaluation level:** ten configured FPM pools use PHP
8.4.27 and the global upload-progress workaround is removed. Foto's unfixed
PHP 5.6 runtime is removed from configuration; its named nginx vhost returns 503
at server level. Foto accounts and data handling are preserved.

Evaluated committed head: `55ed38c1bd5b86e5ab264336d3f285dff4265a57`.
Evaluated Git tree: `8a42d008d0949147945bf7504777c0c368170d81`.
Configuration snapshot: `/nix/store/kd6yz06glpr5l42p5pbb4ck68m50kc09-source`.
Final split head: `38e7c837893695999e588a73f5d2a0088b8257b1`.
Its Git tree is exactly the same `8a42d008d0949147945bf7504777c0c368170d81`. The source
results are reused for that identical final tree; evaluation was not repeated
for the requested history-only split. `php-fixed-final-tree-binding.json` records
the explicit old/new heads and trees.

Final logical commits:

1. `823ffe9cd1bbbf6dd708f756211d4d0d55913bc6`: native stable pin.
2. `01213695503ab85ee273263a17751c2a68389f43`: revert global workaround.
3. `38e7c837893695999e588a73f5d2a0088b8257b1`: standalone Foto shutdown.

## Pin and security provenance

The native pin commit is `823ffe9cd1bbbf6dd708f756211d4d0d55913bc6`.
`nixos-stable` / `nixpkgs` resolves to `nixpkgsStable`:

- Revision: `8c259fc0dd1f3ccc1aaf4f9156ab16b7328b5a4f`.
- Source: `/nix/store/sj5n1vkrcfn7inmm37q6rr0dhwh21n8d-source`.
- NAR hash: `sha256-dEQs/r/DSIvSjw5pQro/BAqsUnFNNZ3I/qmFYzatGvc=`.

Independent GitHub API inspection confirms this is the merge commit of
[PR #576865](https://github.com/NixOS/nixpkgs/pull/576865), merged into
`release-26.05` at 2026-10-21 14:43:05 UTC. The architect selected that branch
head at 14:58:51 UTC, ahead of channel promotion. The lock's original
`nixos-26.05` ref/tracking policy is unchanged. Independent semantic comparison
against follow-up base `37a338b25192d9271ee211110800c2dc6a094a57` found only
`nixpkgsStable` changed; other input nodes are unchanged.

Both first-party vendor advisories were independently read:
[CVE-2026-109618](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)
and
[CVE-2026-109619](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp).
Both list fixed releases 8.2.35, 8.3.36, **8.4.27**, and 8.5.12 within their
respective minor branches. Every remaining web pool meets the 8.4 fixed release.

## Actual consumer versions

These are each pool's effective `phpPackage` and session-extension versions,
not merely the default package's version. In particular, all four DokuWiki
custom `php84.buildEnv` consumers were independently evaluated.

| Machine / nested container | Pool | PHP / session extension | Workaround |
| --- | --- | --- | --- |
| `cz.vpsfree/containers/int.blog` | `wordpress-blog.vpsfree.cz` | 8.4.27 / 8.4.27 | Removed |
| `cz.vpsfree/containers/int.kb` | `dokuwiki-kb.vpsfree.cz` | 8.4.27 / 8.4.27 | Removed |
| `cz.vpsfree/containers/int.kb` | `dokuwiki-kb.vpsfree.org` | 8.4.27 / 8.4.27 | Removed |
| `cz.vpsfree/containers/int.utils` | `adminer` | 8.4.27 / 8.4.27 | Removed |
| `cz.vpsfree/containers/int.web` | `vpsfree` | 8.4.27 / 8.4.27 | Removed |
| `cz.vpsfree/machines/aitherdev / kb-staging` | `dokuwiki-kb-cs.aitherdev.int.vpsfree.cz` | 8.4.27 / 8.4.27 | Removed |
| `cz.vpsfree/machines/aitherdev / kb-staging` | `dokuwiki-kb-en.aitherdev.int.vpsfree.cz` | 8.4.27 / 8.4.27 | Removed |
| `cz.vpsfree/vpsadmin/int.webui-dev` | `vpsadmin-webui` | 8.4.27 / 8.4.27 | Removed |
| `cz.vpsfree/vpsadmin/int.webui1` | `vpsadmin-webui` | 8.4.27 / 8.4.27 | Removed |
| `cz.vpsfree/vpsadmin/int.webui2` | `vpsadmin-webui` | 8.4.27 / 8.4.27 | Removed |

All ten evaluated package sets share unwrapped derivation
`/nix/store/ik5kjfxg09dhb9wsjywa1l1c495b8rb7-php-8.4.27.drv` and session
extension derivation
`/nix/store/09ch89sb574wz6ninf01n7ji9mwjmy7j-php-session-8.4.27.drv`.
The PHP source is the official
`https://www.php.net/distributions/php-8.4.27.tar.bz2`, pinned with
`sha256-slMKh3xyL0sIyeF0owywi6wrfhkD7m6eMV8KqfX4LCQ=`.
Its only evaluated PHP patch is `fix-paths-php84.patch` (gettext/Apache build
paths); session extension patches are empty. The selected source's PHP definition
SHA-256 is `954170c5377a45848e0e76a7afa79de7b0e9896223e2132865285a27161b456a`,
matching the independently fetched immutable source file.

For every pool, assertions verify no upload-progress assignment in pool INI,
no upload-progress administrative setting, and null raw pool configuration.
Apache PHP remains disabled. Nested staging retains `autoStart = false`;
no claim is made about its live state and no container operation was executed.

## Foto result and retained data

The evaluated named `foto.vpsfree.cz` vhost has:

```text
extraConfig = return 503;
root = null
locations = []
enableACME = false
forceSSL = false
```

No Foto FPM pool or `phpfpm-foto` service exists, and Foto is absent from the
session-cleanup pool list. There is no gallery root, file/FastCGI location,
redirect or custom error-page fallback. Source search finds no remaining
`nix-phps`, `php56`, upload-progress workaround module or directive in the active
configuration modules. This establishes removal of the configured legacy web
runtime; no built system-closure or deployment claim is made.

Foto's original external package was PHP 5.6.40 from nix-phps
`1bf10b8c3c378e14d11861a056e885775a2ebc73`, with its own independent nixpkgs
`9e7f26f82acb057498335362905fde6fea4ca50a`. No fixed/backported 5.6 release
was established. Its partial workaround was therefore superseded by shutdown.
Immutable source evidence remains in `php-fixed-foto-source.json`.

The Foto users/groups block is byte-identical to the follow-up base. The
source change adds no data deletion, migration, activation script or ownership
change. Gallery/session data remains in place; re-enabling requires a patched,
reviewed runtime/application path.

## Evidence and limits

`php-fixed-runtime-evaluate.nix` reuses the approved exact confctl composition
seam, exposing only the existing `evalConfigFor` output. Original confctl
source SHA-256 is
`37936e294f8a60fee590f2242f77f1df64f871e8ce44c05f2b9b2f1250925768`.
The final evaluation ran with `allow-import-from-derivation=false`, without
realizing external sources or PHP/system builds.

- `php-fixed-runtime-evidence.json`: exact source snapshot, ten effective
  packages/session versions, settings and Foto vhost/service/account evidence.
- `php-fixed-lock-source.json`: independent lock comparison and source hashes.
- `php-fixed-pr-provenance.json`: independent merged PR metadata.
- `php-fixed-vendor-advisories.json`: independent vendor fixed-version records.

The user owns builds. This package confirms conditional workaround removal
against selected source and effective configuration; it does not establish
realized system outputs, running PHP versions, nginx syntax/build success or
activation success. No additional tests or live probes were added.
