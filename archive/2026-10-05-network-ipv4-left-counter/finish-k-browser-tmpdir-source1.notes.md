Source-only command TMPDIR correction

Only Commands.initialize and three additive owning tests changed. An
explicit ENV TMPDIR must satisfy the existing State private-directory
contract and exact realpath equality. Empty and missing values refuse
without creation; unsafe/noncanonical paths refuse without repair. When
the variable is absent the previous campaign temporary default remains.

The real-child regression goes through Commands.call, preserving native
diagnostics and sole-reaper evidence. It checks the actual child environment,
fixed selected tools and removal of unrelated injected overrides. Every
original verifier test method is byte-identical. All tests/checks are UNRUN.

A lasting short contract paragraph would be useful because TMPDIR is now
a supported caller input with an explicit refusal policy. A technical draft
is in docs.json for root's final wording. Repository prose is untouched.

This is a host command-environment correction, not a new guest artifact,
campaign, phase, timer or qualification. No current/private campaign state
was read. The original Gcd2 failure remains immutable/nonreplayable, and
genuine same-pair direct captures retain their original generator. Root
owns all commits/history/pins, hosted source/strict-media gate and review.
Source/control bytes are held at this freeze; no operation wrapper exists.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/
