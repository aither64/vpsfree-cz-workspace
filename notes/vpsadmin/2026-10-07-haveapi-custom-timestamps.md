# HaveAPI typed and nested Custom timestamp output

At HaveAPI0.29.8, `Parameters::Typed#format_output` formats a direct `Datetime`
`Time` value with `iso8601`. A `Custom` value passes through unchanged, so nested
`Time` values use the ordinary JSON representation. Equal timestamps can
therefore differ as `2026-10-06T21:56:07Z` and `2026-10-06 21:56:07 UTC`.

The storage maintenance API spec compared an entire typed action result with a
nested Custom status summary. Its first owning run executed102 examples with
one failure; only `acquired_at` and `handed_off_at` differed. The installed
parameter formatter and the resource declarations established the cause.

Keep the existing output contracts. In the expected Custom summary, project
only those two typed timestamp strings with `Time.iso8601(value).utc.to_s`, then
retain exact equality for every key. A blanket normalizer or ignored timestamp
fields would weaken the assertion. This does not justify changing API output.

The initial failing result remains in the initiative evidence. Fresh owning
verification passed all102 API/model examples after the correction, including
the complete status-summary assertion. The existing output contracts stayed
unchanged.

Related initiative: `work/2026-09-23-storage-redesign/state.md`.
