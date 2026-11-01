# Probe API readiness through version metadata

HaveAPI 0.32.1 changed the root documentation heading to `API versions`. The
legacy runner's healthy API returned HTTP 200, but its `API description` text
match kept waiting until timeout. No browser scenario had started.

The existing root `OPTIONS ?describe=versions` request returns the protocol's
successful `status`/`response` envelope with `versions` and `default`. The
services-up scenario already uses it. The services machine readiness helper
now checks that contract while retaining its deadline, curl error propagation
and caller interface. HTML documentation assertions remain with services-up.

Evidence and independent review:
work/2026-11-01-published-advisory-corrections/readiness-final-review.md.
