# Leap 16.1 systemd device-unit boundary

Historical preliminary assessment. Its expected-failure recommendation below
was withdrawn. The actual missing-udev cause, controlled resolution and minimal
source fix are recorded in [the final diagnosis](device-unit-result.md).

The expected-failure extension proposed below is **withdrawn** after the user
requested an actual openSUSE root-cause/fix investigation. Milestone 1 leaves
the device-unit test unchanged. Implementer1 owns the separate investigation
under `device-unit-design.md`; lead defines any later source-fix boundaries.
Raw observations, old candidate identity and hashes below remain valid.

Completed evidence is for superseded dedicated-builder source
`aa963dce42859ae4251cdfaded91920d67b3a46e`, candidate image SHA256
`254523b59106db1d27bcf98e43e942c8ea1d7f0c15238542ca17e21612017214`.
The final shared-builder source still needs fresh verification.

The [partial matrix receipt](candidate-matrix-result.md) records device-units
JSON false after 86.294s and start-stop JSON true after 248.382s. Both PTYs and
native shell/console logs are preserved as `aa963dce4-{device-units,start-stop}-*.log`.
Manual debug did not create native `test-runner.log`; the PTYs contain its
script JSON/trace. The tested AA source is retained at
`refs/backup/2026-11-03-opensuse-leap-image-build/tested-dedicated-aa963dce4`.

Exact failure: [device shell](aa963dce4-device-units-shell.log) lines 253–417
repeatedly reports status 3 for
`systemctl status sys-devices-virtual-net-eth0.device`, with `Loaded: loaded`
and `Active: inactive (dead)`. The container start immediately before it
returned 0. The final poll ends in an empty-output protocol timeout only after
those repeated nonzero inactive-unit results. This is not evidence of a missing
image, failed package bootstrap, absent unit or broken container startup.

`tests/suite/systemd/device-units.nix` already documents exactly this inactive
openSUSE behavior for `version == "latest"`, marks it expected failure and
uses one immediate command rather than polling until the shell budget expires.
The supported boundary is that the tested 16.1 candidate boots and passes normal
image/start-stop checks, but its eth0 systemd device unit does not become active.
The dummy0 checks are not reached and remain untested by this result.

Earlier proposal, now withdrawn: match
`distribution == "opensuse"` and version in `[ "latest" "leap-16.1" ]` for the
existing exception. No such source change was applied. Do not treat that
proposal as the current design or call the existing failure a functional pass.

The separate investigation must preserve this exact loaded/inactive eth0
status-3 evidence and distinguish it from an unrelated exception or timeout.
This record makes no final fix recommendation; the later brief defines its
behavioral acceptance criteria.

Preserved device shell SHA256:
`04a2bcd305e622e1fbdd7fba902322bbe84369724bcaca40226d4140ce50fc6a`.
Device PTY SHA256:
`e9fa80f3665190698a550f52716b6c83851d1de93ccecfafd3276c6fc934c420`.
Start-stop shell SHA256:
`7ea647072a8f9c204b7f7c7c2658f384073514981910b4f4b1f801f79a590f9f`.
Start-stop PTY SHA256:
`ae49c23149792fa9fa45691035885ffd8877243a61f9defbfc5aeb96a7fb4975`.
