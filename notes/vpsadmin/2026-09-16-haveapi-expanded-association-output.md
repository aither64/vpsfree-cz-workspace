# HaveAPI association expansion can bypass Show execution

During IP release review, a request response expanded with
`_meta[includes]=ip_release_campaign` returned null allocation counts, despite
the same campaign returning integers through its direct Index and Show actions.

HaveAPI can serialize an associated model through `safe_output` without running
its resource Show action. Computed fields initialized only by Show#exec are
therefore not ready on every serialization path. Keep the computed value
available through the model getter too. The campaign uses lazy initialization
of one shared summary, while direct Index/Show explicitly refresh it.

An HTTP regression expands the campaign through the request resource and checks
all declared count fields. A concrete-instance model spy verifies that reading
all three fields invokes the evaluator once. Both checks and lint pass. Avoid
any-instance mocks: the repository's RSpec lint rejects them.

Related initiative: `work/2026-09-09-ip-release-mechanism/`.
