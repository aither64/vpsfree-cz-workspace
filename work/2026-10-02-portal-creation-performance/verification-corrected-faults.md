# Corrected-provider fault verification

Passed on 2026-10-02 at 22:05 UTC, wrapper exit 0. The fresh Luna/low watcher
ran the reviewed, frozen driver once. Parent inspected its completed result
and accepts both real fault cases.

| Case | Acceptance to ready | First assistant after acceptance | Result |
| --- | --- | --- | --- |
| Successful root-helper JSON withheld | 16.796866 seconds | 18.203841 seconds | Same root recovered on attempt 2 |
| Team helper interrupted after a member completed | 18.983364 seconds | 24.262028 seconds | Same root and completed member retained on attempt 2 |

Both retries retained the original receipt, frozen Full preset and goal. Each
finished with three ready members, exactly one initial user message, a completed
assistant turn, no tools, detailed live phases and complete final evidence.
The member interruption produced both a ready and an unfinished member before
retry; it was a genuine partial roster. Full filesystem discovery remained
part of both retries (8.818 and 10.452 seconds).

This verifies the supported old-consumer/new-thread-create-provider combination:
old selected Ruby/services from candidate `0klh7`, corrected public Go provider
from `xl9mvbb5j19anfbx6qj3lrw8k7a9vnz2`, runtime `924c0ec2`. Only the two fixed
fresh fault slugs selected that provider; normal generation and lock checks
remained. Source/provider hashes and independent review are recorded in
[preparation](verification-corrected-fault-preparation.md) and
[review result](review-corrected-faults-result.md).

Original result, stranded receipt/journal, unavailable original root, prior
claims and five timing samples remain unchanged. This run does not prove repair
of the old unavailable root and does not supply new full-package latency data.
The separate production activation and actual-history canary remain required.

Complete noncredential result and events remain in the private fixture under
`/tmp/pcp-oct02-a`; full log/status remain in the initiative's private verification
directory. Credentials and rollout payloads are excluded from this record.
Result SHA256: `6b96c3d5a5c7acf573ef722aa955a5dc6013ae1ac4fc892457662714811f719f`.
