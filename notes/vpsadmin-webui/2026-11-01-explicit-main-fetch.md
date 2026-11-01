# Verify remote main when a bare clone lacks a fetch refspec

The published-advisory correction branch began at a verified current main. A
later ordinary fetch left origin/main unchanged while ls-remote showed a newer
main: the canonical bare clone had no ordinary heads-to-tracking fetch refspec,
so fetching origin only refreshed HEAD/FETCH_HEAD.

Before readiness, compare the exact remote default ref with ls-remote. Fetch
that ref explicitly into its tracking ref when needed, then reconcile only the
owned feature branch. Preserve old/new base/head ranges and range-diff evidence;
shared documentation conflicts must retain both changes. Do not change shared
Git configuration or a colleague's checkout to repair this.

New dependency/toolchain/shared-inventory inputs require their affected checks
even when advisory source and browser specs are byte-equivalent. A local
tracking ref alone is not fresh remote evidence.

Evidence: work/2026-11-01-published-advisory-corrections/implementer1.md.
