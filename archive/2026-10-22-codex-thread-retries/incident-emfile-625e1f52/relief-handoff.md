Targeted native NOFILE relief completed at 2026-10-24 10:52:39 UTC.

The held machine claim was verified. Only native MainPID 3387667 soft NOFILE
changed from 1024 to its existing hard limit 524288. The command exited zero.
Immediate and independent readback preserved PID, InvocationID, process start
ticks, UID, executable and hard limit; the unit remained active/running with
no restart. Portal health returned HTTP 200 and {"ok":true} at 10:57:51 UTC.
No child limits, service settings, source, session records or submission state
were changed. The claim remains held.

The corrected journal projection found nine native ERROR records containing
Too many open files (os error 24), from 10:31:47.993762 to 10:33:34.383697 UTC.
Journal MESSAGE byte arrays must be decoded; the earlier zero/empty-marker
collector evidence is superseded by journal-network-correlation-decoded.json.
The selected-unit query found no network-permission-revoked or exact creation
ID marker. Temporal overlap does not prove the original reviewer start outcome
or link the separate network error. No native history or prompts were read.

Detailed receipts and checksums are in relief-final.json and
live-nofile-relief-20261024T105239Z/. Persistent service correction and exact
creation recovery remain assigned to their owners. This relief adds headroom;
it does not establish a leak fix or successful creation recovery.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
