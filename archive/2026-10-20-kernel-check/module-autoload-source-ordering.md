# Module autoload: exact source and ordering

Implementer1, 2026-10-22. Read-only inspection of merged vpsAdminOS
`846bb469505789ba0b2a405fa5905ba6d8253006`; no evaluation, build, runtime test,
remote CI query, configuration write or source/ref change. Architect owns the
synthesis; implementer0 owns existing executed coverage and its gaps.

The generic sysctl service preserves the ordinary disabled/logged policy in
source. It replays the configured value; it does not choose plain modprobe or
replace the activation snippet. Explicit conflicting overrides and additional
files have the ordering qualifications below. This is source proof, not a
newly executed four-mode integration test.

## Pins and reference notation

`OS` below means the exact OS revision above. Its clean worktree was at that
head. `OS/flake.lock:91–111` maps root `nixpkgs` to `nixpkgs_2`, revision
`da6dc0e7b26060f2f71ce3ef7088fb56ee44fa36`, NAR hash
`sha256-MlvRfa1O5Cqc2/a+gG+l9TSuowEoCKCmrJ1d9oAVm0I=`.
Read-only `nix path-info --json` confirms that hash for
`/nix/store/640irzgl08asrnjly4dspdbx8lz3cvqr-source`, denoted `N` below.
`OS/os/modules/nixos-modules.nix:9–12,49,56` imports the pinned ETC, activation,
modprobe, kernel and sysctl modules.

`N/pkgs/os-specific/linux/procps-ng/default.nix:24–31` pins procps 4.0.6,
source hash `sha256-Z76m+8OkKlNaAjDJ6JHl3ftNnTlCLUZWWimQ0azhUhY=`.
The already retained [procps source provenance](generic-sysctl-failure-injection.md)
and [sysctl.c](procps-4.0.6-src-sysctl.c) supply the parser/write references.

## Four ordinary modes

Assumes no explicit sysctl/file/activation override and the upstream default
`boot.modprobeConfig.enable = true`.

| Autoload enable | Autoload log | Activation writes | Generated sysctl / replay |
| --- | --- | --- | --- |
| false | true (default) | Logging deny wrapper | Same wrapper |
| false | false | Empty string | `kernel.modprobe=` then newline; empty value |
| true | true | Logging load wrapper, which execs kmod | Same wrapper |
| true | false | Upstream `${pkgs.kmod}/bin/modprobe` | No OS declaration for this key; no write absent other input |

`OS/os/modules/config/kernel.nix:12–34,159–177,435–446` derives the wrapper,
normal-priority sysctl declaration and forced activation snippet from the same
policy. Wrapper line 19 logs the action, line 23 execs kmod for enabled mode,
and line 27 exits 1 for disabled mode. With logging off, the selected override
value is the empty string. For enabled/unlogged mode the override condition is
false, leaving upstream activation.

`N/nixos/modules/system/boot/modprobe.nix:25–28,71,92–98` defaults modprobe
configuration on and writes the plain kmod path during activation. It does not
declare `boot.kernel.sysctl."kernel.modprobe"`. Explicitly disabling this
upstream module removes that upstream activation; it is outside the table's
ordinary assumptions.

`N/nixos/modules/config/sysctl.nix:94–98` renders non-null values literally
into `/etc/sysctl.d/60-nixos.conf`. Empty string is distinct from null, so
disabled/unlogged produces `kernel.modprobe=\n`. Procps
`sysctl.c:684–707` accepts the empty RHS, `:166–195` preserves it as an empty
string, and `:623–628` writes the value followed by newline. There is no
substitution of a plain modprobe path. No runtime empty-string write was
performed by this investigation.

Kernel-request logging here is distinct from explicit configured-module loads:
`OS/os/modules/config/kernel-modules.nix:44–54,124–159` calls kmod directly and
logs those operations independently. No coupling to a `logModuleLoading`
symbol was found in the inspected exact OS/pinned upstream modules; this
investigation does not give that name an invented alias to `moduleAutoload.log`.
Denying kernel requests does not prohibit an administrator or the configured
module loader from calling modprobe directly.

## Boot and activation order

1. `OS/os/modules/system/boot/stage-1-init.sh:71–75` installs an initrd modprobe
   path and explicitly loads initrd modules. This is a pre-existing interval
   before stage-2 policy, not a generic-service restoration.
2. `OS/os/modules/system/boot/stage-2-init.sh:65,79,81` runs activation, then
   post-boot commands, then runit. The policy activation depends on `specialfs`.
3. `OS/os/modules/config/runit.nix:19–26` explicitly loads `boot.kernelModules`,
   then synchronously runs `sysctl -w --system` in runit stage 1.
4. `:278–281` starts runsvdir. The new generic service in default/rescue later
   runs the same procps operation (`OS/os/modules/config/sysctl.nix:25–36,52`).

Thus ordinary boot has policy activation before both stage-1 and supervised
replay, and they agree. No general service dependency orders all other
services after the supervised sysctl application. Post-boot commands,
nonstandard runlevels and explicit other writers can alter the result.

## Live switch, unchanged inputs, restart and removal

`OS/os/modules/system/activation/switch-to-configuration.rb:75–120` makes
`switch` install the boot configuration and run `test`; `test` stops changed
services, always invokes activation, then restarts changed existing services.
Service equality is run path plus restart triggers (`:198–203`), and change
selection is `:295–302`. The sysctl service tracks enabled managed
`sysctl.conf` and direct `sysctl.d/*.conf` targets plus normalized source paths
(`OS/os/modules/config/sysctl.nix:8–22,35–36`).

An unchanged switch/test still executes modprobe activation. It rewrites
`kernel.modprobe` even though unchanged sysctl input identity skips the service
restart. Therefore retention of manually changed `kernel.printk` does not
imply retention of manual `kernel.modprobe`. Direct activation alone does not
replay sysctl files. The service's input stamp is not a runtime readback.

Changing to enabled/unlogged mode restores plain kmod through **upstream
activation**, not through a generic-service fallback. Changing to the other
modes immediately writes their target policy during activation. Removing a
key or setting it to null only removes a replay instruction; procps does not
reset omitted values to kernel defaults. For this key, activation remains an
independent writer. Rolling back into an older generation executes that
generation's activation/service code; the target's rules, not the newer
service's existence, govern it.

New services start asynchronously: the real `test` method says runit will
start them (`switch-to-configuration.rb:112`) but does not start/wait its
`start` list. ETC activation exposes their links while activation is still
running; `OS/os/modules/system/boot/runit/default.nix:431–438` generates those
links. The modprobe snippet has only `specialfs` as a dependency, not a
new-service barrier. A newly introduced sysctl service can therefore run before
or after that snippet. Ordinary values agree in either order; conflicting
values do not have an established first-introduction winner. Existing changed
services are explicitly restarted after activation, assuming stopping them
succeeded. Protected services and command failures add limits. Switch success
does not itself establish successful application; its Ruby `system` results
for activation/service operations are not enforced as a transaction.

## Explicit overrides and file precedence

The policy's sysctl declaration has normal priority, whereas its activation
snippet is separately forced. `N/nixos/modules/config/sysctl.nix:9–17` uses
`mergeOneOption` for this key. `N/lib/options.nix:451,470–484` requires one
retained definition; `N/lib/modules.nix:1435–1455,1587–1591` retains the lowest
numeric priority (ordinary 100; `mkForce` 50).

| Input | Effect on activation and later replay |
| --- | --- |
| Stronger explicit sysctl value V | Activation still writes policy; replay writes V if it runs and later inputs do not replace it. V may deliberately be plain modprobe. |
| Competing ordinary sysctl definition | Multiple-definition error, not a silently selected override. |
| Stronger null | Key omitted from generated file; activation still writes policy. Null does not disable that snippet. |
| Remove a former override | Target policy returns during activation; generated target value is replayed where present. Omission alone does not reset a kernel value. |
| Unchanged conflicting override | Unchanged service may skip restart while activation rewrites policy. A manual service restart later replays the override. |
| Additional sysctl files | Their actual procps order decides whether/when they replace the policy value. |

Procps `sysctl.c:831–909` selects each basename from the first directory
containing it, in order `/etc/sysctl.d`, `/run/sysctl.d`,
`/usr/local/lib/sysctl.d`, `/usr/lib/sysctl.d`, `/lib/sysctl.d`; it then sorts
basenames lexically and reads `/etc/sysctl.conf` last. `:201–214,718–738`
retains exact-key entries and writes them in sequence. It is not an atomic or
single-final-value transaction. An earlier file selecting plain modprobe can
temporarily replace a deny wrapper before `60-nixos.conf` restores it; a later
file or `/etc/sysctl.conf` can leave plain modprobe selected. These are
source-supported effects of conflicting inputs, not an observed default bug.

Only managed direct `/etc` inputs affect the service identity. Unmanaged
files, mutable string sources and `/run` or `/usr` inputs can affect an actual
replay without automatically triggering a service restart. Changing managed
inputs restarts the existing service, which reapplies **all** procps inputs,
including any conflicting value for this key.

`N/nixos/modules/system/etc/etc.nix:10,21–67,223–229,360–365` selects enabled
files, normalizes sources and generates ETC activation;
`etc-activation.nix:14–18` orders it after users/groups/specialfs. For the
ordinary symlink renderer, `setup-etc.pl:25–27,57–78,140–147` swaps the static
tree and removes obsolete managed files. Removing a file is not a kernel
sysctl reset. Overlay ETC is an explicit alternative; no runtime overlay
behavior was claimed here.

`OS/os/modules/config/sysctl.nix:38–69` runs once, clears previous stamps,
applies procps and publishes its input identity only after success. Failure
does not roll back already written keys and supplies no plain-modprobe fallback.
Its check validates the input stamp, not the current kernel setting or current
contents of unmanaged inputs. The exact-source table is supported; missing
boot/switch/restart interaction tests remain implementer0's reported coverage
gap, not a demonstrated regression.
