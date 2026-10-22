# Current follow-up: fixed PHP and temporary Foto shutdown

The user explicitly requested disabling `foto.vpsfree.cz`; retaining a partial
PHP 5.6 workaround is superseded. Keep the fixed stable pin and removal of the
global precaution, and apply this bounded change in
`configs/webs/foto.vpsfree.cz.nix`:

- Preserve `services.nginx.virtualHosts."foto.vpsfree.cz"`, `enableACME = false`
  and `forceSSL = false`. Set its server-level `extraConfig = "return 503;"`.
  Nginx processes this server rewrite directive before selecting a location,
  covering every URI/method, including PHP and static paths. Use nginx's normal
  503 response; no new frontend, maintenance text or feature flag is needed.
- Remove the site's `root` and both existing locations. Do not add a redirect,
  alias, FastCGI target or custom error-page fallback. The disabled virtual host
  must not serve gallery files or expose PHP source.
- Remove the `foto` FPM pool, the independently sourced `nix-phps` fetch/import,
  its PHP 5.6 package reference and Foto's session-cleanup pool registration.
  Remove now-unused module arguments/let bindings. Preserve all `users` content.
- Preserve `/var/www/foto.vpsfree.cz`, Foto's existing session/data directories,
  ownership, users/groups, DNS and proxy routing. No activation script, deletion,
  migration or permission change is needed. Removing the cleanup registration
  stops that configuration's scheduled cleanup; it does not delete stored data.

Implementer0 owns source/Git and amends the local-only obsolete workaround
commit `6cf8c9e2a67908874e343682c088ed190749529a` into the final disablement
commit. Keep generated pin commit `823ffe9cd1bbbf6dd708f756211d4d0d55913bc6`
separate, and preserve all earlier merged history. Implementer1 independently
evaluates: no Foto pool/service or imported PHP 5.6 runtime, same named nginx
virtual host with server-level 503 and no file/FastCGI locations, unchanged
users/data handling, ten remaining fixed PHP pools, and no global workaround.
Quick checks are formatting, parsing, diff checks and no-build evaluation.

Expected behavior after the user's later build/activation: Foto returns HTTP
503 for all paths; the other PHP web applications use their fixed packages.
No deployment, merge, build, live probe or data mutation is authorized here.
Reverting this disablement alone restores a vulnerable PHP runtime; do not
recommend that recovery. Reopening requires a separately reviewed patched
runtime/application path. The source change preserves data for that follow-up.

## Accepted pin and superseded Foto-only precaution

Current brief: [fixed-version implementation and evidence](php-fixed-version-design.md).
User explicitly selected `release-26.05` without waiting for channel promotion;
pin `nixos-stable` / `nixpkgs` to
`8c259fc0dd1f3ccc1aaf4f9156ab16b7328b5a4f` through native confctl. Remove the
global FPM precaution only after confirming the ten non-Foto pools use fixed
PHP. The prior Foto-only precaution is superseded by shutdown above.
Implementer0 owns pin/source/Git; implementer1 owns independent version
and option evidence. No builds, deployment, or merge are authorized for this
follow-up. The user will build.

The [original precaution design below](#historical-php-upload-progress-precaution)
records the earlier evidence and implementation at the time; its pre-disclosure
uncertainty and all-pool scope are superseded by the current follow-up. The earlier
commit `38687a84` was merged and must not be rewritten.

# Historical PHP upload-progress precaution

Design owner: architect0 (retained Astra/xhigh). Configuration base inspected:
`86e19685313270d88e4db30038c056ce4b807abd`. Scope is a configuration patch and
an operator command; no deployment, merge, lifecycle action, or PHP version bump.
The user's later instruction, "let's not waste time with CLI", narrows this
brief to PHP web requests. CLI packages, wrappers and CLI verification are out
of scope; the default-PHP overlay has been removed from the implementation.

## Evidence and limits

- [PHP vendor announcement](https://www.php.net/archive/2026.php#2026-10-20-1)
  confirms two critical vulnerabilities and a release scheduled for 21 October
  2026, 14:00 UTC. It withholds technical details and affected/fixed versions.
- [CERT-EU advisory 2026-018](https://cert.europa.eu/publications/security-advisories/2026-018)
  names CVE-2026-109618 and CVE-2026-109619. It does not confirm this workaround.
- [watchTowr's first-party FAQ](https://watchtowr.com/intelligence/php-cve-2026-109618-faq/)
  also names the identifiers, but expressly describes technical scope and a
  workaround as unconfirmed. Its release-date claim differs from PHP's; use PHP's.
- [PHP session configuration](https://www.php.net/manual/en/session.configuration.php#ini.session.upload-progress.enabled)
  documents `session.upload_progress.enabled`, its enabled default and per-directory
  changeability. Disabling it disables session-based upload progress. It is a
  precaution, not evidence of remediation of either CVE; revisit vendor fixes.
- [PHP FPM configuration](https://www.php.net/manual/en/install.fpm.configuration.php)
  documents administrative pool settings and warns that trusted FastCGI clients
  can send PHP configuration. Do not claim protection against a privileged
  operator deliberately replacing PHP configuration or using arbitrary PHP builds.

## Inventory and interfaces

| Confctl machine | Runtime paths to cover |
| --- | --- |
| `cz.vpsfree/containers/int.blog` | `wordpress-blog.vpsfree.cz` FPM |
| `cz.vpsfree/containers/int.kb` | `dokuwiki-kb.vpsfree.cz` and `dokuwiki-kb.vpsfree.org` FPM; DokuWiki builds PHP 8.4 with per-site INI through `buildEnv` |
| `cz.vpsfree/containers/int.utils` | `adminer` FPM |
| `cz.vpsfree/containers/int.web` | `vpsfree` FPM; `foto` FPM from independently imported fossar/nix-phps PHP 5.6 |
| `cz.vpsfree/vpsadmin/int.webui1` | inherited `vpsadmin-webui` FPM |
| `cz.vpsfree/vpsadmin/int.webui2` | inherited `vpsadmin-webui` FPM |
| `cz.vpsfree/vpsadmin/int.webui-dev` | inherited `vpsadmin-webui` FPM |
| `cz.vpsfree/machines/aitherdev` | nested `containers.kb-staging` with two DokuWiki FPM pools |

The staging pools are `dokuwiki-kb-cs.aitherdev.int.vpsfree.cz` and
`dokuwiki-kb-en.aitherdev.int.vpsfree.cz`. The container is configured with
`autoStart = false`; do not start it or change its staging ownership.

No Apache PHP service is declared by this inventory; active web paths use nginx
and FPM. Munin CGI is Perl, Bepasty is Python, Discourse is Ruby. The new
`int.vpsadmin-webui1` deploys a JS BFF/frontend and is excluded. Its reference
to a PHP QR endpoint is a remote URL served by int.web. PHP packages fetched by
ad hoc user development shells and unmanaged container contents are outside the
configuration's control; do not expand this patch to them.

## Smallest robust implementation

Implementer0 owns all application edits and Git, in the registered configuration
worktree. Keep this to the following three source boundaries unless evidence shows
a real gap; refer any expansion to the lead:

1. Add `modules/system/php-upload-progress.nix`, a small NixOS module that extends
   the existing `services.phpfpm.pools` submodule type. For every actual pool,
   append `session.upload_progress.enabled = Off` to pool `phpOptions` with
   `lib.mkAfter` and force `settings."php_admin_flag[session.upload_progress.enabled]"`
   to `false`. Extend the pool submodule using `types.attrsOf (types.submodule ...)`;
   avoid constructing pools by recursively mapping over their final definition.
   The administrative flag is the decisive runtime enforcement, after INI loading.
   Preserve all unrelated pool options, extensions, session paths and cleanup.
2. Import this module in the NixOS list in `modules/module-list.nix`.
3. Import this same module explicitly inside the nested container's `config` in
   `cluster/cz.vpsfree/machines/aitherdev/kb-staging.nix`. Host module imports do
   not propagate into this container.

FPM's `-c` INI and package `PHP_INI_SCAN_DIR` are distinct: a service-specific
scanned INI can override pool INI settings. The administrative pool flag applies
after INI loading and covers independently sourced foto PHP 5.6 and DokuWiki
PHP 8.4 without replacing either package. No PHP package overlay or source
override is needed for this web-request scope.

No existing source sets upload-progress On, FPM raw extraConfig or FastCGI
PHP_VALUE/PHP_ADMIN_VALUE. Acceptance must check final configuration and refuse
to call the workaround effective if a later raw/administrative override re-enables
it. Do not add a generalized security framework for hypothetical future services.

## Independent packages and dependencies

- Implementer0: three source paths above, concise rationale comments, formatting,
  quick syntax checks and one coherent commit; serialize all Git operations.
  Must wait for this brief, now present, before substantive edits.
- Implementer1: session-only `php-runtime-coverage.md` and a session-local
  evaluation helper/evidence. No application source edits. May inspect the pinned
  confctl `mk-confctl-outputs.nix` by a local copy with only an additional output
  exposing `evalConfigFor` results; preserve exact confDir, inputs, channels,
  relative imports, systemModulesFor and specialArgs. Record the source revision
  and one-output delta. This uses actual composition instead of recreating it.
  Initial inventory/evaluator work is independent; effective-value checks depend
  on implementer0's patch. Check all eight machines and nested staging config.
- Architect0: authoritative-source evidence, design revisions and acceptance
  interpretation. Lead accepts scope/results, registers artifacts and handles
  tracking/review/watcher assignment. No extra implementers or reviewers.

## Acceptance and verification

Quick checks before final review:

1. Nix formatting and parse checks on changed files; `git diff --check`.
2. Evaluate actual configurations and show the exact FPM pool names. Every pool
   must have final administrative upload-progress flag false, final pool INI Off,
   and no later raw extraConfig or FastCGI administrative override enabling it.
3. Inspect generated service ExecStart and the available `-c` and scanned INI
   configuration. Include foto and DokuWiki in the pool-policy checks, but do not
   force third-party fetches or import-from-derivation builds for uncached legacy
   PHP before review. Defer those package/runtime checks to watcher-owned builds.
   Executable checks must use the actual FPM package/configuration; a default
   shell PHP value is insufficient evidence for a web service. Do not dump full
   configuration environments or secrets.
4. Check Apache `enablePHP` remains false and no extra PHP-bearing declared
   service was missed; verify the eight-host selector against `confctl ls`.
5. Use a harmless disposable FPM request probe with a per-directory `.user.ini`
   attempting to enable upload progress if existing packages/tooling permit it.
   It should report Off under the enforced administrative pool flag. Report any
   unexecuted runtime assertion as a verification limit, not as passing. Keep
   these checks proportional; do not add CLI probes or a new test framework.

Longer checks after completed committed change and mandatory independent review:
build affected system configurations with the pinned `nix develop` environment
and fresh verification watcher as required by workspace policy. This may fetch
or realize the legacy PHP package; the patch itself changes no PHP package
derivation. Stop any unexpected kernel build. No deployment, including dry-activate,
is part of the authorized work. Actual HTTP smoke checks/service restarts await
an operator deployment. Keep uploads and authentication as post-deploy smoke
checks; the intended user-visible difference is session-based progress reporting.

## Compatibility, deployment and recovery

No database migration, persisted-state format, API/client/CLI command interface,
daemon protocol, or application package version changes. Ordinary uploads and
existing session storage remain enabled; applications using PHP session progress
lose those progress values. Machines can be updated independently with no fleet
coordination. PHP/FPM configuration reload/restart is needed for running workers;
ordinary confctl switch activates changed units. Nested staging activation must
be inspected without starting an intentionally stopped container.

Rollback to the previous system generation can read all existing application
state, but removes the precaution. Prefer repairing service configuration while
retaining Off where possible. No schema rollback or data repair is expected.
Applying this workaround does not remove the need to update PHP once vendor fixes
are available. PHP 5.6 is independently sourced and will need separate follow-up.

## Prepared operator commands (not executed)

Run in the configuration feature worktree's `nix develop` shell:

```sh
php_hosts='cz.vpsfree/{containers/{int.blog,int.kb,int.utils,int.web},vpsadmin/{int.webui1,int.webui2,int.webui-dev},machines/aitherdev}'
confctl ls "$php_hosts"
confctl deploy --one-by-one "$php_hosts" switch
```

Pinned confctl revision `7bee58a52372b95c2198ce3f2a719807a3c2c66b` uses
`File.fnmatch?(pattern, name, File::FNM_EXTGLOB)` (`lib/confctl/pattern.rb`), so the
quoted braces are interpreted by confctl. Unquoted shell brace expansion is
incorrect here. `deploy` builds a new generation unless `--generation` is given,
then copies and activates; `switch` is also its default action. `--one-by-one`
serializes copying/activation per machine. `--generation current` instead reuses
the latest locally recorded build and must only be used after verifying it is
the intended candidate. `dry-activate` contacts machines and is not a local-only
check. Sources: pinned `man/man8/confctl.8.md`, `lib/confctl/cli/app.rb`, and
`lib/confctl/cli/cluster.rb`. The independent coverage report verifies the live
pinned help and exact selector membership before these commands are handed off.
