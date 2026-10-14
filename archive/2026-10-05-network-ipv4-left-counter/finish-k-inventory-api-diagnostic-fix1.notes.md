Source-only direct remediation of reviewer0's Important inventory diagnostic
finding at exact K8de1776588e374e39e3ba6c7595158c6b7d25225.

Non-200 responses now refuse before JSON parsing with the existing bounded
method/pathname/status error. HTTP200 parsing has one local catch which creates
a fixed Error and retains no parser cause or response excerpt. The envelope
must be a non-null object, status must be exactly true and response must be a
non-null object; arrays and primitive values refuse at the same fixed boundary.
Lease assertion and transport errors retain their existing paths.

The existing transport seam can emit supplied raw bytes. Eleven new cases
cover malformed HTTP404/200 and invalid success envelopes. Each requires bounded
secret-free message/stack, absent cause, exactly one member identity GET, no
browser or further requests and no fixture metadata. The existing valid JSON404,
all old test declarations/assertions, producers, deadlines and cleanup remain.

No repository prose change is useful. The fixed technical error text was checked
directly with the configured writing skill and English Humanizer. Root prose,
other tracked source and earlier frozen controls remain unchanged. There were
no local tests/checks, syntax/formatting, evaluations/builds, process probes,
guest/private campaign reads, lifecycle actions, Git/index/ref/pin changes or
hosted operations. All new tests are UNRUN; no passing repair is claimed.

The direct canonical remediation brief binds the finding and original reviewed
head. Root owns original review acceptance, normal consolidation/publication,
focused hosted verification, exact downstream selection and step9 disposition.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/

report_to_lead is unavailable. Native final is the accepted reporting fallback
and uses the fresh message_id in this packet.
