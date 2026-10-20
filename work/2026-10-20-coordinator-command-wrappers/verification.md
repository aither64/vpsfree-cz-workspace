# Verification evidence

Runtime final candidate: f7ebc3e151cd52d1e45c22adb8da7b9fc1940e18 on
74ff349efc9238922a63a47af815504c305c9838. Workspace instructions:
5e6c5aa411af16e2d81a5e3440c09c35b1884b10 on
9439f4c5569997f465e51be2fb9459e4afd3e304. Both branches contain one coherent
functional commit and no migrations or dependency-update streams. See the final
inventory artifacts and independent review/remediation record.

| Check | Result |
| --- | --- |
| Command unit suite | 22 tests, 89 assertions passed |
| Browser coordination suite | 14 tests passed |
| Selected original host/coordination checks | 8/60 and 19/142 passed |
| Affected Go policy packages | Passed |
| Disposable forward profile recovery under a command lock | 1/14 passed |
| Retained profile recovery regression | 1/12 passed |
| Retained background CLI admission regression | 1/13 passed |
| Actual systemd worker survival and interruption, plus latency | 3/22 passed |
| Signed Overcommit 0.73.0 fixture | 1/33 passed |
| Packaged Ruby aggregate, package, host contract/module and source filter | Passed |

The packaged aggregate proves complete unique coverage of 851 Ruby cases across
13 shards, with 9,630 assertions, no failures/errors and 16 declared environment
skips. The package's Go and browser checks passed. Selected Nix checks finished
in 432.3 seconds. Built candidate:
/nix/store/ay9ac0azmkhn4jgjzharafk8nvxcf6n6-dev-workspace-0.2.0.
It has not been selected or deployed.

Both exact feature heads are published over SSH. Runtime CI run 39452948198 is
in progress; the workspace-instruction repository has no configured CI runs.

The systemd fixture uses independent transient user services and private fixture
state. It proves survival after dispatcher exit, exact request retry, interruption
exclusion and explicit resolution. Its production code matches the final candidate;
subsequent edits only improved signed-hook and legacy test fixtures. Full evidence:
attempt3-systemd-latency-integration.log and latency-results.json.

Five no-op commands took 0.467, 0.488, 0.490, 0.513 and 0.554 seconds, median
0.490 seconds. Their regular records/log files totalled 14,079 bytes, with no
source payload directory. This is a small disposable overhead measurement, not a
production merge-speed comparison. Project hooks, builds and network operations
remain session work.

The signed fixture installs Overcommit into disposable GEM_HOME and uses generated
configuration and plugin bytes. Explicit session-supplied signing establishes
feature checkout trust, historical checkout trust and final feature trust before
ordinary merge/push hooks. A deliberately failing pre-push hook prevents the remote
default ref from changing, while the local fast-forward remains observable. An
explicit later push succeeds. The generic coordinator performs no signing or
checkout. The unit suite separately proves Git can return zero after post-merge
hook failure, so command success is never presented as verified integration.

Failed attempts were investigated before rerun. The first systemd fixture loaded
the real CLI too early because of its basename; it now controls the entrypoint
and captures journals on timeout. Signed-hook setup now signs individual plugins.
The isolated gem runner preserves Nix's Minitest path. Two old module/allocated-host
fixtures now provide their environment/package identity. These were fixture setup
failures; their original logs/results remain under attempt1 through attempt4.

Long checks initially used fresh Luna/low utilities from installed policy. When
fresh utility launch became unavailable, the lead reported the monitoring-skill
fallback and took bounded parent monitoring. No tests touched another session,
existing trust state, shared runtime selection or a production/default ref.
