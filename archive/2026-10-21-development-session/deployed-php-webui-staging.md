# Built PHP/FPM artifact inspection: WebUI and KB staging

Read-only inspection on 2026-10-21 by implementer1. Session/environment exactly
match `2026-10-21-development-session` and `/home/aither/workspace/ai/vpsfree.cz`.
No build, source/Git change, deployment, restart, container start, PHP CLI check
or request probe was performed.

## Result

**The currently selected aitherdev staging build does not contain the mitigation.**
Both actual built staging FPM configs lack the upload-progress administrative
flag, and their referenced actual PHP INI lacks an active Off assignment. The
package-scanned INI supplies no override. This is a check of file contents and
service references, not a runtime directive query.

**The three WebUI machines remain a verification gap.** Their expected
merged-snapshot generated files are absent in the local store. Remote system
identity and files were not verified because SSH host-key validation failed;
the lead directed stopping SSH investigation and checking local built output.
This does not establish what those remote machines are running.

## Inventory and identity

Pinned `nix develop -c confctl ls --hide-header --output name,host.fqdn,host.target`
resolved the assigned targets:

| Machine | SSH target | Inspection result |
| --- | --- | --- |
| `cz.vpsfree/vpsadmin/int.webui-dev` | `webui-dev.int.vpsfree.cz` | Local expected outputs absent; remote identity unverified |
| `cz.vpsfree/vpsadmin/int.webui1` | `webui1.int.vpsfree.cz` | Local expected outputs absent; remote identity unverified |
| `cz.vpsfree/vpsadmin/int.webui2` | `webui2.int.vpsfree.cz` | Local expected outputs absent; remote identity unverified |
| `cz.vpsfree/machines/aitherdev` | `172.16.106.40` | Actual current host and selected nested built artifacts inspected |

Bounded SSH used BatchMode, ConnectTimeout=5, ServerAliveInterval=5,
ServerAliveCountMax=1 and a 20-second command timeout. No host-key data was
written or bypassed. Aitherdev's successful root SSH result matches the local
hostname `aitherdev` and local `/run/current-system` target:

```text
/nix/store/vq63sg427gay6wb9w41ixnv6hza88izk-nixos-system-aitherdev-26.05.20261019.f3a73bc
```

The host's actual built `etc/nixos-containers/kb-staging.conf` resolves to:

```text
/nix/store/i4p2zwk4zs3sjx50a1l8rjz7aqr2mdba-etc-nixos-containers-kb-staging.conf
```

Its actual line selects this nested built system:

```text
SYSTEM_PATH=/nix/store/7psqfgnz602qlhg935fy5rbc6il8jqkw-nixos-system-kb-staging-26.05pre-git
```

`container@kb-staging.service` was already `ActiveState=active`,
`SubState=running`, MainPID `3507687` when inspected. Its state was left untouched.
The selected built system above is not independently proven to match the
container's live mount namespace/current generation or every running FPM worker.

## Actual selected staging units and files

Both built units are under the nested system's `etc/systemd/system/` and resolve
to existing store artifacts:

| Pool | Resolved built unit file |
| --- | --- |
| `dokuwiki-kb-cs.aitherdev.int.vpsfree.cz` | `/nix/store/13amxj4r0mkmdbmp60la6dw7l4aawyxb-unit-phpfpm-dokuwiki-kb-cs.aitherdev.int.vpsfree.cz.service/phpfpm-dokuwiki-kb-cs.aitherdev.int.vpsfree.cz.service` |
| `dokuwiki-kb-en.aitherdev.int.vpsfree.cz` | `/nix/store/v566464xljpnpbx12aiwq43ryr6jsf0n-unit-phpfpm-dokuwiki-kb-en.aitherdev.int.vpsfree.cz.service/phpfpm-dokuwiki-kb-en.aitherdev.int.vpsfree.cz.service` |

Their actual ExecStart fields use the same executable:

```text
/nix/store/x7xv32zhi5cfbbl7kq75rqx6r70dzcbw-php-with-extensions-8.4.26/bin/php-fpm
```

and these actual, present configuration files:

| Pool | `-y` FPM config | `-c` PHP INI |
| --- | --- | --- |
| Czech | `/nix/store/1jhgzhkpaiydgj8fmhvyy87cvdy22ffy-phpfpm-dokuwiki-kb-cs.aitherdev.int.vpsfree.cz.conf` | `/nix/store/6a856s7i2cgn3wkaaylm6l8nl9rasn7q-php.ini` |
| English | `/nix/store/glgh3bypn8hv7v2lrp9jwr97b796gcgd-phpfpm-dokuwiki-kb-en.aitherdev.int.vpsfree.cz.conf` | `/nix/store/6a856s7i2cgn3wkaaylm6l8nl9rasn7q-php.ini` |

Neither actual FPM config has an `include` directive or any `upload_progress`
setting. In the actual shared PHP INI, line 1443 is only the commented default:

```ini
;session.upload_progress.enabled = On
```

There is no active `session.upload_progress.enabled` assignment anywhere in that
file. There is no final `Off` setting or `php_admin_flag[...] = no/off/0` in
these selected built artifacts.

### Wrapper/scanned configuration chain

Inspection of the actual FPM executable wrapper found its generated setting:

```text
setenv("PHP_INI_SCAN_DIR", "/nix/store/x7xv32zhi5cfbbl7kq75rqx6r70dzcbw-php-with-extensions-8.4.26/lib", 0)
```

This is a default scan directory, preserving an already defined environment
value. Its only `.ini` file, `lib/php.ini`, resolves to the actual built file:

```text
/nix/store/7lhk3p4nnrszmp5k47693gmjyg8b5m7r-php-extra-init-8.4.26.ini
```

That file contains no active upload-progress setting. The two actual built
service units contain no PHP scan-directory/PHPRC/PHP_VALUE/PHP_ADMIN_VALUE
configuration, no EnvironmentFile, and no built service drop-ins. No FPM includes
supply further administrative settings. Live manager/process environment was
not queried; no runtime directive value is claimed.

## Exact merged-snapshot local availability check

The earlier committed evaluator snapshot binds head
`38687a8438a6e75b20a1924fb65d060a05217b06` and configuration source
`/nix/store/2q5ar7wpdivcz06vvibqc8bc7k6rvnm2-source`. Its expected output paths
were checked for actual local existence; **all six distinct files below are
absent** (WebUI1/WebUI2 share paths):

| Consumer | Expected FPM config | Expected PHP INI |
| --- | --- | --- |
| WebUI dev | `/nix/store/sg1s3jas4a0bp0jc8a63zggk675zsgz5-phpfpm-vpsadmin-webui.conf` | `/nix/store/v4vxml4z87wb74rnm9ywpigiyb6a350a-php.ini` |
| WebUI1 and WebUI2 | `/nix/store/sg1s3jas4a0bp0jc8a63zggk675zsgz5-phpfpm-vpsadmin-webui.conf` | `/nix/store/6h9mimshzc2hvbr2rgly3v6dw7ldzf26-php.ini` |
| Staging Czech | `/nix/store/phgmmcrgy3azx1q5z8znixkaf9pknbkh-phpfpm-dokuwiki-kb-cs.aitherdev.int.vpsfree.cz.conf` | `/nix/store/2a3mdrhn3ddxs8gwv5g34xzrx3lk8spf-php.ini` |
| Staging English | `/nix/store/8zwzw9a4frz9z1mzv3xhm0in8nfb88sq-phpfpm-dokuwiki-kb-en.aitherdev.int.vpsfree.cz.conf` | `/nix/store/2a3mdrhn3ddxs8gwv5g34xzrx3lk8spf-php.ini` |

The PHP executable itself is present. Evaluated builder inputs are not used as
proof that these absent files were built. Other locally realized WebUI/staging
FPM config variants were also inspected for the directive and contained no
upload-progress setting; they were not attributed to remote deployed systems.

The lead has the material current-staging mismatch and WebUI verification gaps.
Further activation or fetching/building outputs was outside this read-only
assignment. Operator build/deployment provenance must be reconciled before
claiming these selected artifacts contain the mitigation.
