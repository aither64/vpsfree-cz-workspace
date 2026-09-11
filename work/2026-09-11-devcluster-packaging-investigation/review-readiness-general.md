# General review: vpsAdmin SSH readiness follow-up

Reviewed `d2380cbe77f711627ba461ef9359724b6255a5db..3d83a8392cd77fb7e92587ed4ea1a5cc665bd3fb`
in `vpsfree-dev-workspace` using the mandatory general lane at high risk and
`gpt-5.6-sol`/`xhigh`.

## Findings

### Important: the readiness probe can block beyond its documented deadline

`dev-clusters/vpsadmin/bin/devcluster:723` invokes the automated probe with
`-n -o ConnectTimeout=3`, but it leaves OpenSSH's `BatchMode` disabled. `-n`
only redirects standard input; it does not disable password or private-key
passphrase prompts, which OpenSSH can read from the controlling terminal. The
connection timeout covers TCP connection, protocol handshake and key exchange,
not user authentication or execution of the remote command. A rejected key,
an encrypted or mismatched retained key, or a bridge address answered by the
wrong SSH server can therefore leave the first probe waiting for interaction
indefinitely. The `SECONDS` check at lines 729-734 is never reached, the
start/update/refresh lifecycle lock remains held, and the promise at
`dev-clusters/vpsadmin/README.md:127` that refresh waits at most two minutes is
false for this error path.

Make the probe explicitly noninteractive with `-o BatchMode=yes`. If the
two-minute limit is intended as a strict wall-clock bound, also bound each SSH
process after authentication (for example with an outer timeout or suitable
SSH liveness options). Extend the command stub to assert the noninteractive
option and cover an authentication failure or hung probe; the current stub
returns immediately and cannot expose this behavior.

## Commit and coverage assessment

The single commit has one logical purpose and appropriately keeps its focused
test and documentation with the behavior. The probe precedes the services seed
check and each regular-node mutation, retries only probe exit 255, and leaves
the real remote actions single-shot. I found no other Blocking, Important, or
Advisory issues in the reviewed delta.

Residual gaps after resolving the finding:

- The transient regression runs only through local forwarded-port networking;
  live acceptance of this exact head still needs to exercise the original
  bridge-network `No route to host` race.
- The 120-second exhaustion path and immediate propagation of a non-255 probe
  failure are not covered directly.
- The new head has only focused command-test coverage so far; the packet records
  that deployment, branch CI, and repeated live startup acceptance remain.
