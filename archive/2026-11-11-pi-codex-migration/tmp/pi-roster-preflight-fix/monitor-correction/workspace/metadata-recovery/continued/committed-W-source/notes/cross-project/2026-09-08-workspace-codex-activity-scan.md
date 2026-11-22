# Workspace index activity lookup

## Symptom

After portal activation, the index waited for its five-second Codex deadline
and logged `load Codex session activity: context deadline exceeded`. Session
pages remained responsive and the App Server continued serving exact-thread
requests.

## Cause

The index used an unscoped `thread/list` request to find activity for every
portal session. On the long-lived aitherdev rollout store, Codex 0.153.4 did not
complete that global scan within the deadline.

## Fix

Pass the exact thread ID and working directory from each active portal manifest
to the Codex client. Read only those recorded threads with `thread/read`, verify
both identity fields and the portal source, and use their `updatedAt` values for
sorting. Filesystem timestamps remain the fallback if an exact lookup fails.

## Verification

Race-enabled cluster, Codex, and Web tests passed, as did the complete
development-cluster suite and sandboxed package build. A temporary candidate
portal queried the live Codex 0.153.4 App Server and rendered the complete index
through its Unix socket in under two seconds while another thread was active.

Related initiative:
`work/2026-09-06-portal-config-deployment-policy`.
