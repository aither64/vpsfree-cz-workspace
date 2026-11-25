# SysRq through a remote console

Read-only clarification by implementer4, 2026-10-20. Session/environment verified.
No key sequence, shell SysRq command, BMC connection, crash, setting change,
package installation, build/test or repository fetch was performed.
Dell-specific UI documentation is owned separately by implementer0.

## Exact Linux behavior

At incident Linux `1dfea587406b7dd79973831d1677fb2418e5e9aa`,
`Documentation/admin-guide/sysrq.rst` distinguishes these input paths:

- **Graphical/virtual keyboard on x86:** `Alt+SysRq+<command>`, where SysRq is
  normally the Print Screen key. Delivery through a particular iDRAC UI depends
  on that UI's virtual-keyboard/key-macro support, not a serial BREAK command.
- **Actual PC-style serial console:** send one serial **BREAK**, then the
  command character **within five seconds**. There is **no mandatory two-second
  wait**. A second BREAK cancels the armed SysRq sequence and is interpreted as
  a normal BREAK.

This reaches a kernel input handler and does not require logging in at the
displayed login prompt. It still requires delivery and processing of keyboard
or UART input; it is not an NMI mechanism and need not work when that path or
interrupt handling is stuck. An alive BMC/video/login screen does not prove the
host input path is alive.

The UART implementation is `include/linux/serial_core.h:1161-1277`:
`SYSRQ_TIMEOUT = HZ * 5`; `uart_handle_break()` arms the timer only with
`port->has_sysrq && uart_console(port)`; the next command consumes the arm.
8250 receive code routes BREAK and characters through these functions
(`drivers/tty/serial/8250/8250_port.c:1718,1740`). Its SysRq capability is
initialized from `CONFIG_SERIAL_8250_CONSOLE` (`:3253`). Merely having a serial
getty or BMC SOL channel does not establish that this UART is a Linux console.

## Relevant commands and permission

| Lowercase command | Meaning | Permission nuance |
| --- | --- | --- |
| `h` | Display SysRq help; no intentional crash | Help follows the no-operation entry and does not test an operation mask. It requires globally enabled SysRq on the normal input route. Seeing `crash(c)` in help does not prove `c` is permitted. |
| `w` | Dump tasks in uninterruptible/blocked state | Requires dump bit `0x8`, or value `1` enabling everything. |
| `l` | Request backtraces for active CPUs | Requires dump bit `0x8`, or value `1`; collection can depend on other CPUs and printing progress. |
| `c` | **Deliberately panic the running kernel and attempt configured crash handling** | Requires dump bit `0x8`, or value `1`. This is not a harmless probe or a guarantee that the crash kernel/capture/upload succeeds. |

`drivers/tty/sysrq.c:149-160` implements `c` with
`panic("sysrq triggered crash\n")` and `SYSRQ_ENABLE_DUMP`.
`include/linux/sysrq.h:22-31` defines dump bit `0x8` and reserves `1` for all
operations. `handle_sysrq()` calls `__handle_sysrq(..., true)`
(`drivers/tty/sysrq.c:642-645`); UART handling uses that same checked path.
**Serial input is subject to the sysctl mask too**, although the documentation
describes the mask as influencing keyboard invocation.
Only the privileged `/proc/sysrq-trigger` write path calls with `check_mask=false`
(`:1167-1199`); that bypass must not be applied to remote keyboard/SOL input.
Help's distinct no-operation branch is `:604-635`.

For node24, no `kernel.sysrq` override was found in incident vpsAdminOS
`2abbe3cc` OS modules, applicable configuration `177a9305` sources, or the pinned
Nixpkgs `26f4107e` NixOS modules. The ordinary x86 recipe enables
`CONFIG_MAGIC_SYSRQ` (`arch/x86/configs/x86_64_defconfig:270`), with Kconfig
defaults `MAGIC_SYSRQ_DEFAULT_ENABLE=0x1` and `MAGIC_SYSRQ_SERIAL=y`
(`lib/Kconfig.debug:624-646`). These match the retained initial `.113` config;
configuration-generation inputs are unchanged at the incident repin, as recorded
in [packaging-audit.md](packaging-audit.md). Thus the **source-derived configured
state is `kernel.sysrq=1`, permitting `c`, `w` and `l`**, using the user's
confirmation that no runtime sysctl changes occurred. This does not pretend the
initial local `.113` file is the final node24 `.config`.

The observed generation-144 command line contains no explicit `console=ttyS*`;
the configuration's `system.serial-console` option defaults false and no node
override was found. Therefore **active serial-console UART selection is not
established** by this evidence. Do not promise that SOL BREAK works on node24
merely because serial SysRq was compiled in. The graphical-keyboard route is a
separate option and does not require that serial-console condition.

## ipmitool SOL and nested SSH escaping

The local ipmitool executable/manual/source were unavailable. Read-only checks
used the official upstream source at the exact Nixpkgs-pinned revision
`3c91e6d91ec6090fe548c55ef301c33ff20c8ed8`:

- [ipmitool manual](https://codeberg.org/IPMITool/ipmitool/src/commit/3c91e6d91ec6090fe548c55ef301c33ff20c8ed8/doc/ipmitool.1.in),
  lines 3327-3334: interactive SOL `~B` means **send BREAK**, and escapes are
  recognized only immediately after a newline.
- [SOL implementation](https://codeberg.org/IPMITool/ipmitool/src/commit/3c91e6d91ec6090fe548c55ef301c33ff20c8ed8/lib/ipmi_sol.c),
  lines 1398-1402: uppercase `B` in escape mode invokes `sendBreak()`;
  lines 1418-1430 implement the preceding-newline condition.

Consequently the sequence to describe is: reach the start of an input line
**before** BREAK, enter `~B` (uppercase B), then the chosen lowercase SysRq
command within five seconds. `~B` is interpreted immediately: do not insert
an extra Enter between BREAK and the command, since that byte can consume the
armed SysRq sequence. Typing the word `BREAK`, a graphical Break key, or an
arbitrary terminal keyboard shortcut is not proof that SOL sent a serial break.

If ipmitool runs through **one interactive OpenSSH hop with the default `~`
escape**, type `~~B` at line beginning so SSH forwards literal `~B` to ipmitool.
The local OpenSSH 10.5p1 manual confirms `~~` sends literal `~`, `~B` is itself
an SSH BREAK escape, and escape recognition follows a newline (lines
1009-1013,1037-1039 of its retained `ssh.1`). Additional nesting or changed
escape characters require interpreting those layers separately.

The lowercase `c` crash action is intentionally destructive to the running
instance. These notes establish an available mechanism and its prerequisites;
they neither execute it nor establish that it would have succeeded during the
node24 incident.

## Follow-up: an apparently consumed `h` with no visible help

The user identified the tested machine as **node2.stg**. Its kernel version and
SysRq mask are not established here; do not apply node24's inferred settings.
At the checked 6.12 source,
`drivers/tty/sysrq.c:833-927` keeps keyboard SysRq active until the matching Alt
release. `h` itself does not disarm it; subsequent keys while Alt stays held
are also suppressed. If Alt was released after the first `h`, a later ordinary
typed `h` is expected and does not indicate a modifier problem. The missing
first character alone does not prove the kernel handled it. With normal
`sysrq=0` and no always-enabled override,
the SysRq input handler is not registered, or is unregistered when disabled
(`:1107-1118,1211-1216`); that disabled handler cannot explain consuming `h`.

Help explicitly clears `suppress_printk` and temporarily raises
`console_loglevel` to `CONFIG_CONSOLE_LOGLEVEL_DEFAULT` (recipe 7) until the help
line is emitted (`:583-639`). Thus ordinary low console verbosity alone is not
a sufficient explanation for invisible help. Console output may still be
deferred/unavailable; actual console filtering uses the log level at flush time
(`kernel/printk/printk.c:1279-1282,3080-3082`). The expected kernel-record prefix
is `sysrq: HELP :`. A read of `/proc/sys/kernel/sysrq` and observation of the
actual target host's privileged `dmesg` while repeating **help only** distinguish
the possibilities. Restricted nonzero masks can show help while forbidding `c`.
No crash test or setting change is needed to establish this input evidence.
