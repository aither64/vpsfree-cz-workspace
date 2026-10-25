# Final review interim finding

Reviewer0, saved Sol/xhigh, exact A96077. Important, general + risk/compatibility.

Valid errors buffer before turn/start reply (ephemeral.go810–825). Binding replays
through consumeLocked (849–853), whose err guard944–945 skips remaining events
once a failed completion sets err. Sequence: valid owned terminal transient error,
exact failed completion with transient info, another valid owned error such as
unauthorized or willRetry=true, then exact start reply and successful cleanup.
The buffered final error is dropped and retry proof remains true, unlike the
same late event after binding. This violates existing terminal-error invalidation
and may authorize another call after permanent/contradictory evidence.

Owner implementer0 prepares narrow replay invalidation and early/late regression
coverage. Current source/refs remain frozen while reviewer completes other lanes.
No long tests/deployment. No new design/API/policy is needed. Final report pending.
