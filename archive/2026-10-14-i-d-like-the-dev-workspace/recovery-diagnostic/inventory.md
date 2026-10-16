# Frozen recovery diagnostic preparation inventory

Prepared by implementer0 under the architect's accepted fixture-only brief.
Session identity was verified with `dev-session current`; both environment
identity variables were absent and the trusted thread binding matched. Lead owns
tracking registration and the final fixture inspection/watcher assignment.

## Identity and provenance

- Registered application worktree remains clean at
  `b8a6be26a75347dcc9ec0fd1330dff886e47c93f`; no source/pin changes or commits.
- Original product output:
  `/nix/store/54cv3sm4z10nal6hi4p214vds9cmjddd-dev-workspace-0.2.0`.
- Original product derivation:
  `/nix/store/77wgdsbc9ra6b23dd7w8kq3zk480zfyc-dev-workspace-0.2.0.drv`.
- Original check derivation:
  `/nix/store/62lvkrl2f6k82shyb6n4rii4myfmpy5k-vm-test-run-dev-workspace-session-recovery-boot.drv`.
- Final diagnostic derivation:
  `/nix/store/y04aq1qnllbmhs45nv2k8pbr98wqm3yg-vm-test-run-dev-workspace-session-recovery-diagnostic.drv`.
- Final observer:
  `/nix/store/l3x7k7mxv1yldk0v1fhxah50p9b9vnb2-mxnnawm9wgmh7y5ymf8y9d35hfg17r0f-recovery-raise-observer.rb`.
- Original source:
  `/nix/store/fpqzq6vs24m668g5fnddmhc0110vw248-source`.
- Original pinned nixpkgs:
  `a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4`.

The lead acquired the wrapper lock and evaluated both provenance files with the
declared Nix environment. Both evaluations were exit 0, with no build/test.
The final product, product derivation and original check derivation match the
failed original log exactly. The initial evaluation remains preserved. The
final wrapper isolates individual diagnostic file paths from surrounding
evidence files; it still imports the original self/host module/nixpkgs/package.

## Files

| Paths within this directory | Role |
| --- | --- |
| `flake.nix`, `flake.lock` | One named diagnostic check; exact original product assertions and locked input graph |
| `session-recovery-diagnostic.nix` | Original first foreign-cgroup scenario, instance-only probe drop-in, terminal fail-fast and bounded collection |
| `raise-observer.rb` | Guarded, capped, sanitized TracePoint observation; no product methods changed |
| `collect-metadata.py` | Read-only fixed-fixture operation metadata and validated snapshot counts |
| `original-session-recovery-boot.nix`, `original-runtime.lock.json` | Exact original baselines, checked against original product source |
| `check-observer.rb` | Tiny synthetic Ruby subprocess contracts, including canary/caps/propagation |
| `check-static.py`, `quick-checks.sh` | Static input/scenario/compile checks and declared interpreter/shell syntax |
| `summarize-run.py`, `run-diagnostic.sh` | One-attempt identity-guarded watcher command and safe coverage/result summary |
| `fixture.patch` | Complete original-to-copied-fixture diff |
| `preparation.patch` | Complete added executable/flake source and wrapper lock diff from empty |
| `evaluated-provenance.json` | Preserved initial lead evaluation |
| `evaluated-provenance-final.json`, `evaluation-final.log` | Final lead evaluation and its diagnostic identity |
| `quick-checks.log`, `quick-checks.status` | Member preparation checks, exit 0 |
| `INPUTS.sha256` | Frozen execution/test/baseline/final-provenance input manifest |
| `preserved-evidence.sha256` | Hashes of six untouched original failure/passing/browser evidence files outside this bundle |
| `README.md`, `inventory.md` | Accepted scope, execution/interpretation limits and handoff |

## Checked evidence

Final member quick command:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/recovery-diagnostic/quick-checks.sh
```

PASS, approximately 2.53 seconds, using the exact original Ruby 3.4.9 interpreter.
Ruby syntax, shell syntax, Python static compilation, complete original lock
graph, unchanged node/provider/setup, first-scenario assertions, drop-in scope,
terminal return-to-Python and collection bounds all passed. No product code,
VM or metadata collector was executed by these static checks.

Synthetic Ruby results:

| Contract | Evidence |
| --- | --- |
| Forward/nested recovery + errno + original object propagation | 5 records, maximum 196 bytes; two forward and two recovery raises |
| Exact argv/mode/UID rejection | 5 variants; UID rejection uses only an isolated synthetic expected-UID literal |
| Waiting ignored + unrelated Ruby options retained | Only one active marker |
| Signature cap and separate provider callers | 4 raises across two caller signatures, two each; one truncation marker |
| Global process/line/frame caps | 62 total records in stress case, maximum 167 bytes; at most six frames and one truncation marker |
| Unknown exception class | Fixed `OtherError`, no class payload |
| Internal stderr-write failure | Fixed disabled marker; original exception still reached its rescue unchanged |
| Fresh worker process coverage | Distinct active PID markers |
| Secret canaries | No message/argv/token/snapshot/URL/local payload in captured observer output in any case |

Input and original evidence hash verification both passed with:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/recovery-diagnostic
sha256sum --check INPUTS.sha256
sha256sum --check preserved-evidence.sha256
```

Manifest SHA256:
`60ce33f62eb1ffd6756e10e00340284c2c35facba76fb78f7629a57060232d7e`.
Fixture diff SHA256:
`c914cde2d7f1937cb812aaa3af8b463ea976bee7d969a4a7590668a5d27b21f0`.
Preparation source diff SHA256:
`c79cd3e260aca110b0a8c470444bdf868942c5283811b4237ced625fccefed45`.

## Lead execution and interpretation

After direct inspection of the final coverage parser/runner, assign one fresh
Luna/low watcher the exact command:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/recovery-diagnostic/run-diagnostic.sh
```

It verifies the frozen manifest, refuses any existing `run/`, reevaluates and
compares final identities, then builds only
`checks.x86_64-linux.session-recovery-diagnostic`. No full flake, original VM
rerun, automatic retry or product source override is used. Existing failed
original logs are untouched. The watcher records one operation, honors its
normal cancellation/escalation rules and stops an unexpected local kernel build.

Observer coverage is an explicit diagnostic outcome. No active marker means
inconclusive; active with no raises is distinct from active with raises.
Truncated/disabled observation is partial and inconclusive. Coverage collection
has no pre-request fence and cannot turn an already-passed assertion into a
product failure. A diagnostic success is only a non-reproduction; original
flake failure and root cause remain unresolved. No product/private schema or
migration is introduced or consumed. Any remedy requires lead direction.

Prepared only; no diagnostic build/VM run, host operation, lifecycle mutation,
queue/reservation action, deployment, commit or push was performed by the member.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>
