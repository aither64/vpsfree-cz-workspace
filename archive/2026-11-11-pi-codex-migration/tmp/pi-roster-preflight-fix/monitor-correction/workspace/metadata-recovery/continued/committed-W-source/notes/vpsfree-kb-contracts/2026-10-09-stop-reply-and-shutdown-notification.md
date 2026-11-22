# Stop reply delivery must not govern shutdown notification

Independent final review of K29b17bf4 found a caller-loss path in the runner's
control loop. A valid first stop latched shutdown and withdrew readiness, then
wrote its reply before notifying the main thread. A disconnected caller could
make that write raise EPIPE/IOError. The request rescue consumed the error;
subsequent valid requests acknowledged the existing latch without notification.
The main loop waited for notification rather than polling the latch.

The accepted correction keeps notification in a narrow ensure around the first
valid request's reply write. Invalid requests never notify, and later valid
requests retain the same one-shot drain. Do not move notification to an outer
request ensure where a previous iteration's local latch result could be reused.

Verification must close an actual first peer before its real reply write, prove
the broken reply, and observe the same runner drain through a later public stop.
Retained child/claim evidence and readiness withdrawal still govern the wait;
reply absence cannot establish whether the request was accepted.

At this record boundary the implementation is assigned and source/hosted proof
is pending. The source review established this control-flow defect without a
local reproduction. It does not explain historical incomplete VM campaigns or
provide cleanup authority for them.

Session: [network availability and IPv4-left counter](../../work/2026-10-05-network-ipv4-left-counter/state.md).
