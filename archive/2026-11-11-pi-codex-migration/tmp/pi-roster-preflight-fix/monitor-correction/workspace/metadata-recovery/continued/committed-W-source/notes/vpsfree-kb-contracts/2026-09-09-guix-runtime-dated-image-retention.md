# Guix runtime image pins expire under repository retention

The managed Guix runtime suite describes testing the current published image,
but its two `osctl ct new` commands still hard-coded `--version 20260819` when
investigated on September 9, 2026. Commit `89a5012` updated the older
`20260613` pin when the documented platform configuration changed. The exact
date remained unchanged
after newer images were published.

[Run 34276611772](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/34276611772)
fails during fixture creation with image-not-found, before Guix assertions.
Inspect `machine-shell.log` in the uploaded artifact rather than retrying the
workflow blindly.

The [public index](https://images.vpsadminos.org/v1/INDEX.json) on September 9
contains `20260822`, `20260823`, `20260829` and `20260905`. Both `latest` and
`stable` resolve to `20260905`. HTTP HEAD on the Guix `image-archive.tar`
returns 404 for `20260819` and 200 for `20260905` and `latest`.

vpsAdminOS `os/configs/image-repository.nix` retains four numeric Guix versions;
the image builder runs its garbage collector after building. The live index
is consistent with normal collection of the old pin. The individual deletion
event was not verified from builder logs.

For this current-image documentation contract, resolve the published `latest`
tag once per run, log the concrete version, and use that version for the
second fixture. This also prevents a tag update during a run from mixing
generations. A fixed dated image requires an explicit retention mechanism;
merely bumping the date will fail again when it leaves the retention window.

The separate Guix initiative implemented this selection in upstream commit
[`81d6d7d`](https://github.com/vpsfreecz/vpsfree-kb-contracts/commit/81d6d7dfe530884aff3e1d2634e02e4b12fe28e8).
The password-reset initiative inherited it through its next default-branch
rebase. [Run 34354071486](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/34354071486)
passed all four suites / 12 scripts on its first attempt, including Guix
reconfiguration and deployment. No image-repository maintenance was needed.

Related initiative: `work/2026-08-18-vpsadmin-password-reset`.
