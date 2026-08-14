# Guix KB runtime reconfiguration

Initiative: `work/2026-08-14-kb-updates`

## Symptom

Building a Guix image from the current unpinned source made the focused KB test
slow and memory-heavy. A 24 GiB test VM contributed to the coordinating process
being killed by the OOM killer. After switching the test to the published Guix
image, a plain `guix system reconfigure` rejected the image's active channel
generation because the Guix revision packaged in the image was not a descendant
of the revision recorded by that generation.

## Cause

The published image's system generation records its exact channels in
`/run/current-system/channels.scm`. The independently packaged `guix` command
can refer to a different, rewritten channel lineage, so Guix's ancestry safety
check correctly refuses the reconfiguration. Building an unpinned image also
tests moving upstream code rather than the member-facing published template.

## Workaround

Import an explicitly versioned published image, keep the focused VM at 12 GiB,
and run the reconfiguration with the Guix revision that created the active
generation:

```sh
export GUIX_PROFILE=/run/current-system/profile
. "$GUIX_PROFILE/etc/profile"
guix time-machine -C /run/current-system/channels.scm -- \
  system reconfigure -L /etc/config /etc/config/system.scm
```

Set a working container DNS resolver in the runtime fixture before invoking
Guix substitutes. Do not use `--allow-downgrades` to suppress the ancestry
check in member documentation.

## Verification

The focused `kb/guix#reconfigure` test imports the pinned image, changes the
hostname, runs the exact managed-article fixture, restarts the container, and
checks the new generation, hostname, network, and SSH. See the initiative
`state.md` for the recorded test result.
