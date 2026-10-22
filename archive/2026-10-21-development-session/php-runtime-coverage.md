# Web PHP/FPM coverage and prepared rollout

Owner: implementer1. Session and both environment markers verified as
`2026-10-21-development-session` in `/home/aither/workspace/ai/vpsfree.cz`.
Scope is web-request PHP/FPM only, following the user's explicit removal of CLI
work. No application source edits, shared Git mutation or deployment by this
package. This setting is a precaution; the advisory limitations are in design.md.

## Result

Independent configuration evaluation passes for all **11 FPM pools on eight
machines**, including independently sourced Foto PHP and both nested staging
pools. Evidence is bound to committed head
`38687a8438a6e75b20a1924fb65d060a05217b06`, configuration snapshot
`/nix/store/2q5ar7wpdivcz06vvibqc8bc7k6rvnm2-source`.

For every pool, assertions checked that:

- The effective `php_admin_flag[session.upload_progress.enabled]` is `false`.
- The final INI assignment of `session.upload_progress.enabled` is `Off`.
- Raw pool `extraConfig` is null and no other pool setting targets this directive.
- Apache `enablePHP` is false in the host and nested configurations.

Unrelated session-cleanup INI settings can follow the upload-progress assignment;
these do not change its value. Nested `kb-staging.autoStart` remains false.

## Exact runtime inventory

| Confctl machine | Evaluated FPM pools |
| --- | --- |
| `cz.vpsfree/containers/int.blog` | `wordpress-blog.vpsfree.cz` |
| `cz.vpsfree/containers/int.kb` | `dokuwiki-kb.vpsfree.cz`, `dokuwiki-kb.vpsfree.org` |
| `cz.vpsfree/containers/int.utils` | `adminer` |
| `cz.vpsfree/containers/int.web` | `foto`, `vpsfree` |
| `cz.vpsfree/machines/aitherdev` | Inside `containers.kb-staging`: `dokuwiki-kb-cs.aitherdev.int.vpsfree.cz`, `dokuwiki-kb-en.aitherdev.int.vpsfree.cz` |
| `cz.vpsfree/vpsadmin/int.webui-dev` | `vpsadmin-webui` |
| `cz.vpsfree/vpsadmin/int.webui1` | `vpsadmin-webui` |
| `cz.vpsfree/vpsadmin/int.webui2` | `vpsadmin-webui` |

Aitherdev has no outer-host FPM pool. Its nested container needs the explicit
module import in this patch; host imports do not propagate. Do not start the
intentionally stopped staging container as part of this rollout.

`int.vpsadmin-webui1` runs the new frontend/BFF, not legacy PHP WebUI. Its remote
`qr.php` image is served by int.web; it does not add another local PHP host.
All eight selected machines use `nixpkgsStable` in `confctl.buildPlan`.

## INI precedence and package evidence

The pinned PHP-FPM module creates each pool INI by concatenating
`${pool.phpPackage}/etc/php.ini` and `pool.phpOptions`, then launches that pool's
package with `bin/php-fpm -y <fpm.conf> -c <pool-php.ini>`. The evaluator captured
the executable command and its derivation contexts for all ten nonlegacy pools.

All ten use the same locally present PHP 8.4.26 package:
`/nix/store/x7xv32zhi5cfbbl7kq75rqx6r70dzcbw-php-with-extensions-8.4.26`.
Inspection of its actual `etc/php.ini` and scanned `lib/php.ini` found no explicit
upload-progress assignment. The appended pool INI supplies Off. The forced
administrative pool flag enforces the directive after package/per-directory
configuration; it also covers Foto's independently selected PHP 5.6 package.
No package overlay or PHP version change remains in the final patch.

Repository source search found no `PHP_VALUE`/`PHP_ADMIN_VALUE` injection or
upload-progress setting outside the new mitigation module. Together with the
evaluated pool settings and null raw configuration, there is no identified
configuration path re-enabling upload progress in this patch.

## Reproducible evidence seam

`php-runtime-evaluate.nix` imports the exact pinned confctl evaluator with one
additional output exposing its existing `evalConfigFor` results. It preserves
the original `systemModulesFor`, `specialArgs`, inputs and channels, and uses the
Git flake snapshot as `confDir`. Git reference/snapshot identity was checked
against `nix flake metadata` before evaluating.

- Confctl revision: `7bee58a52372b95c2198ce3f2a719807a3c2c66b`.
- Original source:
  `/nix/store/8mjng71gica53p9jr4085f22xq1zslzg-source/nix/flake/mk-confctl-outputs.nix`.
- Original source SHA-256:
  `37936e294f8a60fee590f2242f77f1df64f871e8ce44c05f2b9b2f1250925768`.
- The helper records the exact replacement text and checks that the replaced
  output occurs exactly once. No configuration repository file is changed.
- Authoritative committed-head result: `php-runtime-fpm-runtime.json`.
- Compact settings projection: `php-runtime-fpm-settings.json`.

The final evaluation ran with `allow-import-from-derivation=false`; Foto's
package/executable fields were omitted from that projection while its effective
pool options remained included. An earlier baseline package inspection was
interrupted when Foto's independent source import triggered source realization.
No PHP or kernel source build was started by this package.

## Exact prepared commands

The pinned live tool returned exactly the eight inventory machines for this
quoted selector:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-21-development-session/vpsfree-cz-configuration

php_hosts='cz.vpsfree/{containers/int.{blog,kb,utils,web},vpsadmin/int.{webui-dev,webui1,webui2},machines/aitherdev}'
nix develop -c confctl ls --hide-header --output name "$php_hosts"

# Lead-selected single-machine build, after review, through its watcher:
nix develop -c confctl build 'cz.vpsfree/containers/int.kb'

# Prepared production rollout; not executed by this task:
nix develop -c confctl deploy --one-by-one "$php_hosts" switch
```

Live pinned `build`, `deploy` and `ls` help passed. Confctl uses Ruby
`File.fnmatch?` with `File::FNM_EXTGLOB` for quoted brace selectors. `deploy`
builds selected hosts by default, then copies and performs the explicit `switch`.
`--one-by-one` copies, activates and health-checks each machine before the next;
normal confirmations and health checks remain enabled. Production activation
requires its own authorization and machine claims. No deployment is requested.

`--max-jobs` controls Nix build jobs rather than rollout concurrency. The special
generation selector is `--generation current` (or numeric offset `0`), not
`latest`; using it requires verifying every selected host's intended local
generation. The prepared default build path avoids stale generation selection.

## Verification limits and follow-up

No live FPM/HTTP request, per-directory `.user.ini` probe, production activation
or service restart was performed. The lead stopped optional disposable probes
under the user's fast-track direction. Foto's actual generated service/package
INI remains uninspected because it requires import-from-derivation realization;
its effective INI options and administrative flag are independently verified.
The other ten generated INI derivations were evaluated through their exact
builder inputs and command references, not built by this package.

The lead owns final review and the single int.kb build result. No full eight-host
build is claimed. Before actual activation, operators must handle running FPM
workers through ordinary switch/restart semantics, preserve stopped staging
ownership, and verify upload/session behavior afterward. Removing the setting
or reverting to an older generation removes this precaution without changing
application state formats.
