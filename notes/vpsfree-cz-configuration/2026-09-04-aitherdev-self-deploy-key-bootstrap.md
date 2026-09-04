# Bootstrap local aitherdev deployment keys

Initiative: `work/2026-09-03-dev-session-portal/`

## Symptom

A key added to aitherdev root's declarative `authorizedKeys` cannot deploy the
generation that first adds it. A batch SSH probe to the confctl target fails,
and non-interactive local sudo is unavailable.

## Cause and workflow

`confctl` copies and activates the system as root over SSH. The new key is not
accepted until that generation is active, so an existing credential or a
one-time user deployment must bootstrap it.

Keep a self-deployment key out of broad key aggregates and authorize it only on
the intended machine. When deployment originates on that same machine, use
authorized-key source restrictions for its local addresses and disable SSH
forwarding and PTY features while retaining remote command execution.

Rolling back to a generation before the key was added removes access. If the
key is the agent's only credential, `confctl` can activate the old generation
and then fail when it reconnects to update the system profile. Treat that
rollback as user-owned unless another root credential is available, and inspect
the active generation before retrying.

## Verification

Compare the configured public-key fingerprint with both the public-key file and
the public key derived from the private key. Confirm the key is absent from
shared aggregates, has only the intended machine/user consumer, validate the
composed authorized-key line, and use `ip route get` to verify that confctl's
local target route selects an allowed source address.
