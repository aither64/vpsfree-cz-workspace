# Truncated image ZFS stream during test import

## Symptom

Image workflow run `32094157385` reported Arch as an unexpected failure even
though the image build completed with status 0. Importing the newly exported
stream failed with:

```text
gzip: stdin: unexpected end of file
cannot receive new filesystem stream: incomplete stream
```

The failing pipeline extracted `rootfs/base.dat.gz` from the image tar and fed
it through `gunzip` to `zfs recv`.

## Cause and classification

The gzip member in the generated image archive was truncated. The Arch
bootstrap, both chroot calls, all mount cleanup, and the image build itself
returned success. The same Arch 2026.08.01 bootstrap exported, imported, and
passed all 15 runtime tests in run `32037034898` attempt 4.

This is general exporter/test-runner fragility, not an Arch build-script
regression. Repository commit `24844cae5` already records unexplained
intermittent `Zlib::BufError` failures while writing ZFS image streams.

## Workaround and future fix

An isolated occurrence can be retried only after inspecting the artifact and
confirming that the build completed before the corrupt import. Do not hide a
real image-build failure behind a rerun.

Harden `libosctl`/`osctl-image` separately by writing streams to temporary
members or archives, checking the gzip and ZFS stream before publication, and
atomically exposing only a complete archive. A corrupt export should produce a
specific diagnostic and may then be retried explicitly.

Related initiative: `work/2026-08-17-image-build-failures/`.
