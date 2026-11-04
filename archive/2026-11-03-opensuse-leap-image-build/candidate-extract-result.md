# openSUSE Leap 16.1 candidate extraction result

- Result: incomplete; the fixed extraction eval was interrupted after the guest stalled before pool readiness. No candidate archive was produced.
- Source revision: `aa963dce42859ae4251cdfaded91920d67b3a46e` in the clean `vpsadminos` worktree.
- Input: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/candidate-extraction-aa963dce4.rb`; SHA256 `feb4df2ff8c042fac40a7dc729a0296f4dcc59a5fc3932070b30a1775366b6fc` (matched expected).
- Command: `env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-image image-scripts/test@opensuse-leap-16.1`.
- Initial debug reached Pry. The fixed eval printed `Source aa963dce42859ae4251cdfaded91920d67b3a46e; retained builder d5ddc633`, then produced no further output or pool-readiness/export confirmation.
- Escalation evidence: `machine-console.log` recorded watchdog soft lockups for all four guest CPUs: at guest time 425.814–425.828s, each stuck 22s; 453.814–453.828s, 48s; 481.814–481.828s, 74s; 509.814–509.828s, 100s. Latest tasks were `kworker/u16:0:12`, `kworker/u16:1:43`, `pgdatinit0:42`, and `kworker/u16:2:44`. `machine-shell.log` was empty.
- Exact owned run directory: `/tmp/2026-11-03-opensuse-leap-image-build-image/os-test-image-scripts__test__opensuse-leap-16.1-90ada9d4`.
- Cancellation: after lead authorization, Ctrl-C was sent to the owned PTY while the eval was blocked in `IO#wait_readable`; Pry returned at prompt `[2]`. `exit` then closed the debug runner normally with exit status 0. Subsequent process inspection showed no remaining PIDs 1347506 (script), 1347520 (test-runner), or 1352555 (QEMU). Run directory and image/disk evidence were retained.
- No archive at `/tmp/2026-11-03-opensuse-leap-image-build-candidate-repo.tar` exists; archive hash unavailable. Candidate export and builder/RPM identity verification did not complete.
- Full PTY transcript: `candidate-extract.log`, SHA256 `ddfeea38ce57de0a867d53c019619570e4d4246222165e65905433b57ccb8b1c`.
- Guest console: `machine-console.log`, SHA256 `b373a4799f194ed0b751e41f7eb59ac55bbcd11337438fbe583e36d18d437096`. Guest shell: `machine-shell.log`, SHA256 `b75c6663907ff8d42fa525982257b7d537fd8e1bb89aa4720712069fe27deedc`.
- Primary image test had already passed 15/15 before this separate debug export operation.
