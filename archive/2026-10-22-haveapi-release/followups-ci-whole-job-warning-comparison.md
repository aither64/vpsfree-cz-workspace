# Full CI build-log warning comparison

Compared all 3,201 lines of original release job `120072628557`, run
`39849807897`, source `b64fb25b`, with all 3,053 lines of follow-up build job
`120546474284`, run `39992191335`, source `090a188c`, attempt 1.
Both exact source hashes appear in their retained full job logs.

| Targeted primary diagnostic | Original | Follow-up |
| --- | ---: | ---: |
| obsolete_npm_rimraf_inflight_glob | 3 | 0 |
| rollup_circular_dependency | 15 | 0 |
| rollup_top_level_this | 72 | 0 |
| fiddle_default_gem | 2 | 0 |
| rust_generated_non_snake_case | 8 | 0 |

All five targeted categories are absent from the new full CI job. Counts refer
to primary diagnostic lines; continuation and aggregate warning lines remain
available in the original full output and machine evidence.

The whole new job still contains eight Nix installation `useradd` warnings
about build-user UIDs exceeding `SYS_UID_MAX`, and four warnings from cloning
empty disposable Git repositories during release-tool tests. It also includes
one Git initial-branch configuration hint containing the word “warning” and
three ordinary Composer lines naming `symfony/deprecation-contracts`.
These residual lines are all retained with original line numbers in the
[machine comparison](followups-ci-whole-job-warning-comparison.json).
The whole CI job is not described as warning-free.

The original file is [the retained full release job](release-followups-build-job120072628557.log).
The [new raw full job](followups-ci-observation-090a188c-20261023T170949Z/release-build-job120546474284-from-archive.log)
is an exact member of the saved GitHub run-log archive, SHA-256
`d0eb197a99d863c9a863e4374aca8b474112d914c5716fb377ce528b1c5d46ea`.
ANSI sequences and all other bytes are preserved. Extraction avoided a GH CLI
terminal-output safety refusal without retrying its direct-log endpoint,
overriding that guard or filtering the build output.
