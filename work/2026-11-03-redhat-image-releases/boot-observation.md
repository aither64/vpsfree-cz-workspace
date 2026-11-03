# Boot and cached-source diagnostic observation

Read-only diagnosis; application head remains
`1a637e9eac4311adba2b08d60dfa7a17d07bcb52`. No source edit, build or retry
was performed by implementer0 during this diagnosis.

The longer logging-only diagnostic reached login and a working shell around
guest 475 seconds, with no watchdog/RIP/Call Trace. It subsequently failed
`osctl-image` status 64 at 20:14:15 CET. The earlier soft-lockups remain an
observation from a separate run; no permanent kernel fault or security-default
correction is established. The 56-second canceled run was incomplete evidence.

The checkout guard is correct: `osctl-image/lib/osctl/image/cli/image.rb:363-368`
requires `os/lib/nixos-container` and `image-scripts` directories, without requiring
Git metadata. The mount command succeeded at 20:14:11; the required exported
layout was no longer available. Exact deletion timing is in the host journal:

```text
Nov 03 20:08:32 aitherdev nix-store-gc-on-pressure-start[1530574]: deleting '/nix/store/91nflgfhifb631q7816j30smqm76afjv-source'
```

Virtiofs connected at 20:04:25, so deletion occurred during this cached run.
The source is now absent. The retained JSON's Nix references include the boot
closures but omit that shared source, whose path came from a raw environment
string. The cached-JSON recommendation preserved the boot inputs but omitted
retention of the exported source after the normal invocation root closed.
There was no guest directory listing; the deletion timeline, mount success and
layout-guard failure establish the diagnostic setup limitation without blaming
checkout recognition or the release RPM.

Normal invocation retains the source through the complete batch:
`Cli::Command.run:8-10` wraps `command.test`; `with_repository_source:138-144`
holds `RepositorySource.open`, whose GC root surrounds its entire yield
(`repository_source.rb:25-31`). `Command#test:59-73` synchronously encloses
prebuild and executor execution; `Executor#run:84-93` joins workers, including
exception cleanup. `TestEvaluator#do_run:770-784` stops/finalizes/cleans the VMs
before those workers finish. The source root is not released before VM cleanup.

Stop cached reuse. The shortest valid next verification is the proper full
four-image local-code invocation, with its source root active throughout and
fresh native resource checks. The lead owns that run and any architect-approved
verification-only memory configuration. No cached-JSON lifetime feature or
checkout guard patch is needed for this task. This receipt does not claim an
image test pass.
