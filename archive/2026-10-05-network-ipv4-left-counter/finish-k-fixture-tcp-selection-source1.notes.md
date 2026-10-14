This source-only fixture correction replaces two sequential TCP allocations
with nested TCPServer.open blocks. Both loopback ephemeral listeners coexist
while their addr ports enter the returned configuration. Block scope closes
both probes on success or exception, including failure to create the inner
listener. No port is reserved after this method returns.

Only RuntimeLifecycleTest#config and its unused free_port helper change.
The entire file prefix before that class and suffix from free_udp_port onward
remain byte-exact. Every original test method, assertion, timeout, UDP helper
and all production bytes are preserved. No redundant test or new CI route is
added; the existing public claim/start/stop cases remain the verification owners.

Native Check38125306206 failed on exact baseline94ea at public-stop start with
duplicate requested host resource, seed13236,99runs/1227assertions,
0failures/1error/0skips. Same-head runtime Check38125302478 passed.
The retained logs bind both outcomes. Separate ephemeral selection can reuse
the first closed TCP port, but the actual native port values were not retained.
This is a source-supported explanation, not a reproduced scheduling event.

No tests, syntax/lint/formatter checks, socket probes, runtime/CI operations,
Git/index/ref/pin mutations or private campaign reads were performed.
The corrected source has no passing verification claim. All source/control
bytes are held for root inspection, normal publication, exact hosted K/E
verification and independent review. Existing private states and preview are
outside this work.

The first metadata inventory stopped before writing controls because it
expected gh-view field names headSha/databaseId. The retained files are REST
metadata with head_sha/id. Correcting that read-only packet preparation did
not change application source or execute verification.

No repository prose change is useful for this narrow test fixture correction.
The native diagnosis and preservation proof remain in this source packet.

Portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/
