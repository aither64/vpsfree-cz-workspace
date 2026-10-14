READY: diagnosis and proposal appended at [design.md:6107](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/design.md:6107).

- OSVM removes virtiofs sockets but leaves daemon-created pidfiles; K correctly refuses the leftovers.
- Recommend a shared K machine adapter using virtiofsd’s existing [`--fd` API](https://gitlab.com/virtio-fs/virtiofsd/-/blob/v1.13.3/src/main.rs#L670-705), avoiding new pidfile cleanup authority.
- G13 processes are completely gone and its claim is absent; stop cleanup remains failed. Explicit retention of that state is a proposed alternative requiring root disposition.
- Focused hosted tests and affected review must precede new qualification.

Fresh empty-unit observations are recorded without overriding either native failure. Only design.md changed; launch and captures remain held.
