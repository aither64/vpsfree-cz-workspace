# Fixed PHP follow-up

**Current scope change:** the user subsequently requested temporary Foto
shutdown. The [current design](design.md#current-follow-up-fixed-php-and-temporary-foto-shutdown)
supersedes this document's Foto-only precaution and any assumption that its pool
remains configured. Keep the pin/fixed-version evidence below; the final
functional commit removes Foto's PHP runtime and returns HTTP 503 at nginx while
preserving accounts and data.

Design owner: architect0 (saved Astra/xhigh). Session and both environment
markers verified. Source worktree is the registered same-session
`vpsfree-cz-configuration`; current preparation base is
`37a338b25192d9271ee211110800c2dc6a094a57`. Earlier precaution commit
`38687a84` is already merged. Preserve that history and its deployment evidence.

## Selected source and authoritative fix criteria

The user explicitly selected the latest `release-26.05` source without waiting
for channel promotion. At 2026-10-21 14:58:51 UTC, the GitHub
[release branch ref](https://api.github.com/repos/NixOS/nixpkgs/git/ref/heads/release-26.05)
was `8c259fc0dd1f3ccc1aaf4f9156ab16b7328b5a4f`. This is exactly the merge
commit of [PR #576865](https://github.com/NixOS/nixpkgs/pull/576865), merged
into `release-26.05` at 14:43:05 UTC. The independently observed
`nixos-26.05` ref was `cd4ea8d57de16f4810bc5f14207bac45fbf19f67`.
[GitHub comparison](https://github.com/NixOS/nixpkgs/compare/8c259fc0dd1f3ccc1aaf4f9156ab16b7328b5a4f...cd4ea8d57de16f4810bc5f14207bac45fbf19f67)
reported it 75 commits behind, with zero commits ahead and merge base equal
to `cd4ea8d...`; that channel ref does not contain the PHP fix.

PHP's [vendor release advisory](https://www.php.net/archive/2026.php#2026-10-21-5)
and first-party advisories for
[CVE-2026-109618](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)
and [CVE-2026-109619](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp)
confirm fixed releases 8.2.35, 8.3.36, 8.4.27 and 8.5.12. PR #576865 updates
all four package branches to those releases and adjusts filter-extension tests.
Judge versions within their own supported minor branch, with the selected
source as provenance; a lexicographic or single global minimum is insufficient.

The disclosed vendor guidance confirms disabling upload progress blocks known
session paths for CVE-2026-109619 but is incomplete protection. It does not fix
CVE-2026-109618 or all stale-state variants. Keep the Foto residual exposure
explicit; this follow-up does not claim that PHP 5.6 is patched or safe.

## Scope, interfaces and file boundaries

Implementer0 owns all application edits and Git. Make two coherent commits:

1. Generated pin update only, using the existing mapping
   `nixos-stable` channel / `nixpkgs` role -> `nixpkgsStable` input:

   ```sh
   nix develop -c confctl inputs channel set --commit --no-changelog --no-editor nixos-stable nixpkgs 8c259fc0dd1f3ccc1aaf4f9156ab16b7328b5a4f
   ```

   Preserve the native generated commit message. Do not hand-edit `flake.lock`.
   Inspect its semantic diff and preserve unrelated inputs. This selects the
   exact released-source commit; leave the input's original ref/tracking policy
   unchanged. The request does not change future automation to track release
   branches permanently.
2. Localize the precaution to Foto in a separate functional commit:
   - Delete `modules/system/php-upload-progress.nix`.
   - Remove its NixOS import from `modules/module-list.nix`.
   - Remove its nested-container import from
     `cluster/cz.vpsfree/machines/aitherdev/kb-staging.nix`.
   - In `configs/webs/foto.vpsfree.cz.nix`, retain the exact previous behavior
     directly on `services.phpfpm.pools.foto`: append
     `session.upload_progress.enabled = Off` using `lib.mkAfter`, and set
     `settings."php_admin_flag[session.upload_progress.enabled]" = lib.mkForce false`.
     Add the `lib` argument and a short comment explaining the independent,
     unfixed PHP 5.6 runtime and the partial mitigation. Preserve its package pin,
     session-cleanup module, pool sizing, users and nginx configuration.

No PHP package overrides, CLI work, generalized version-detection framework,
extra mitigation changes, system builds, live probing, deployment, or merge.
Implementer0 may execute the pin now that this brief is present. The functional
removal must be accepted only with implementer1's fixed-runtime evidence.

## Web-runtime coverage and independent evidence

All eight affected machine metadata entries select `nixos-stable`. Expected
fixed runtime is PHP 8.4.27 for these ten pools after the pin:

| Machine | Pools |
| --- | --- |
| `cz.vpsfree/containers/int.blog` | `wordpress-blog.vpsfree.cz` |
| `cz.vpsfree/containers/int.kb` | `dokuwiki-kb.vpsfree.cz`, `dokuwiki-kb.vpsfree.org` |
| `cz.vpsfree/containers/int.utils` | `adminer` |
| `cz.vpsfree/containers/int.web` | `vpsfree` |
| `cz.vpsfree/vpsadmin/int.webui1` | `vpsadmin-webui` |
| `cz.vpsfree/vpsadmin/int.webui2` | `vpsadmin-webui` |
| `cz.vpsfree/vpsadmin/int.webui-dev` | `vpsadmin-webui` |
| `cz.vpsfree/machines/aitherdev`, nested `kb-staging` | `dokuwiki-kb-cs.aitherdev.int.vpsfree.cz`, `dokuwiki-kb-en.aitherdev.int.vpsfree.cz` |

DokuWiki explicitly selects `php84` and then builds its per-site PHP environment;
verify its effective package version instead of assuming the default `pkgs.php`
proves coverage. Aitherdev remains in scope for its nested web container only.

The eleventh pool is `foto` on int.web. Its source is
[fossar/nix-phps at 1bf10b8c3c378e14d11861a056e885775a2ebc73](https://github.com/fossar/nix-phps/tree/1bf10b8c3c378e14d11861a056e885775a2ebc73),
which supplies PHP 5.6.40 and an independent nixpkgs input. Updating this
repository's stable input cannot update it. Implementer1 independently inspected
its source and found no established fix provenance. Retain both Foto settings.

Implementer1 owns session-only `php-fixed-runtime-coverage.md` and evidence,
independent of application files. Reuse the existing actual confctl-composition
evaluator with `allow-import-from-derivation = false`. Record selected input
identity, all ten fixed effective package versions, and absence of the removed
precaution in those pools. Verify Foto from source or cached evaluation without
triggering IFD builds. Record any remaining evaluation limitation explicitly.

## Acceptance and checks

- Exact locked stable source equals the selected SHA and contains PR #576865;
  no unrelated input changes or channel-policy edits.
- Each of the ten non-Foto effective PHP packages meets its documented fixed
  minor-branch floor; independently confirm `pkgs.php` and custom DokuWiki `php84`
  source/versions. Any unexpected or unfixed runtime blocks removal for that pool.
- The deleted module has no remaining imports. Non-Foto pools have neither its
  appended Off line nor its forced admin flag. Foto retains both, with raw INI
  and administrative precedence unchanged.
- Nix parse/format checks, `git diff --check`, and bounded no-build evaluation.
  No CLI, HTTP, or FPM process probe is required for this source update.
- Review the final committed pin and functional change together using mandatory
  independent review. No new migrations; do not rewrite earlier merged commits.
  Preserve two logical commits rather than merging generated lock and functional
  changes. Record user-owned build verification as pending, not passing.

## Compatibility, deployment and recovery implications

PHP stays within its 8.4 minor branch for the ten fixed pools. This follow-up adds
no database migration, schema/state-format change, API contract or daemon protocol.
Removing the precaution allows the normal package/application upload-progress
setting on fixed PHP; Foto continues Off. New pool configurations and patched
PHP enter the same NixOS generation, so each machine can be updated independently.
Running workers remain on their old binaries until the user's later activation.
The intentionally stopped KB staging container must remain stopped unless the
user separately chooses to start it.

This is a whole `nixos-stable` input update: other stable consumers can receive
package changes between the old channel commit and selected release head.
It is not a PHP-only overlay. Source evaluation cannot establish system-build or
activation success; the user explicitly owns builds. Retain this limitation in
the handoff. The old deployed generation remains a rollback target, but reverting
reintroduces vulnerable PHP with only the former partial precaution. Do not roll
back the PHP pin independently of the conditional-removal commit. No operation
here changes persistent application data or executes a deployment.
