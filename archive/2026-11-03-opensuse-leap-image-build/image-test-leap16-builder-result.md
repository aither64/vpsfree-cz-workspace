# Leap 16 builder verification result

- Result: passed (outer command exit status 0).
- Elapsed: approximately 22 minutes 30 seconds from command start (19:13:33 to 19:36:03 +0100).
- Source: vpsadminos HEAD `aa963dce42859ae4251cdfaded91920d67b3a46e`, tree `d4a264295678a50eac25732074dc942e637850e4`; worktree was clean at preflight.
- Config: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix`, pinned to the exact source head.
- Command: `env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh test --no-destructive --state-dir /tmp/2026-11-03-opensuse-leap-image-build-image image-scripts/test@opensuse-leap-16.1`
- Outer log: `image-test-leap16-builder.log`.
- Guest evidence: `/tmp/2026-11-03-opensuse-leap-image-build-image/os-test-image-scripts__test__opensuse-leap-16.1-90ada9d4/`; guest test runner reported `15 tests run, 15 succeeded, 0 failed`, then `poweroff -f`. The test state and disk are retained for candidate extraction.
- The guest reported the image builder HTTP endpoint as `server: nginx`, `HTTP/2 200`, `etag: "r824bmpcqfmdqn3yq2lgy2j9r1ssza0m-7"`; a separate builder image/download identity was not printed in the observed logs.
- No Lua `exec`/`execute` nil, scriptlet error, or libgio cpio failure signature was observed in the captured outer and guest logs.
- No operation remains running. No cancellation or cleanup was performed.
