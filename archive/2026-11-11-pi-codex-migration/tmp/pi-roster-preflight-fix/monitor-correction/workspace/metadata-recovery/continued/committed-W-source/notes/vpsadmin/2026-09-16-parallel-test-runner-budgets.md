# Separate test-runner instances do not share resource budgets

Starting two `./test-runner.sh test webui#...` processes and a DNS test in
parallel creates independent schedulers. Each WebUI instance reserves 24 GiB
of shared memory; aggregate reservations can exceed the host's /dev/shm even
when each individual runner initially accepts the test. A warning reported
WebUI above its available-memory budget after concurrent evaluation.

The extra storage runner was interrupted with SIGINT before VM startup; run
WebUI scenarios sequentially or group scripts in one scheduler so resource
admission is shared. Check both RAM and /dev/shm headroom alongside any review
cluster. Interrupted execution is not test validation.

Related initiative: work/2026-09-09-ip-release-mechanism.
