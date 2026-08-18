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

## Cause

The gzip member in the generated image archive was truncated. The Arch
bootstrap, both chroot calls, all mount cleanup, and the image build itself
returned success. The same Arch 2026.08.01 bootstrap exported, imported, and
passed all 15 runtime tests in run `32037034898` attempt 4.

`LibOsCtl::Exporter::Zfs` writes `zfs send` through Ruby's
`Zlib::GzipWriter` and closes the writer inside the `IO.popen` block. The
producer child exits at the same time, so Ruby can deliver `SIGCHLD` while
zlib's no-GVL `Z_FINISH` operation is running.

Ruby zlib 3.2.3 retries interrupted work only while input and output both
remain. Deflate finalization must instead continue until `Z_STREAM_END`, even
after all input has been consumed. In the reproduced race, `GzipWriter#close`
returns successfully and writes the correct CRC/ISIZE footer without first
writing the final deflate block. The exporter therefore accepts a corrupt gzip
member and the later import reports unexpected EOF.

The repository's exact producer/writer shape reproduced both silent truncation
and `Zlib::DataError`. The malformed stream had the correct footer for the full
input. With no exiting child, 1,000 iterations passed. Reaping the producer
before finishing gzip also passed 1,000 iterations, while an external gzip
pipeline passed 1,000 producer-exit iterations and 50 iterations under signal
bombardment.

## Fix

Run `zfs send` through an external `gzip -c` process, copy its output into the
tar member, and accept the member only when both child processes exit
successfully. Cover producer exit and Ruby signal delivery in a focused test
that verifies the complete decompressed payload. This avoids Ruby zlib's
interruptible finalization path instead of hiding the failure with a retry.

Resolve `gzip` before starting `zfs send`; otherwise a missing second pipeline
program can leave the producer blocked until Ruby garbage collection closes the
pipe. Supported vpsAdminOS paths already declare the executable: osctld adds
`pkgs.gzip` to its service path, while osctl-image and scheduled image builds
use the core system path that includes GNU gzip. The libosctl gem records the
conditional external requirement for standalone users. The retired OpenVZ
converter is intentionally outside the supported-call-path audit.

Relevant upstream change and discussion:

- <https://github.com/ruby/zlib/commit/c975060f0224e801bb0c12f8357043c3e3065fa3>
- <https://github.com/ruby/zlib/pull/121>

Related initiative: `work/2026-08-17-image-build-failures/`.
