# GitHub job logs can be refused for ANSI escapes

Related initiative: `work/2026-09-11-devcluster-packaging-investigation/`.

`gh api repos/OWNER/REPO/actions/jobs/JOB/logs > FILE` can return1 with
`the response contains terminal escape sequences`, even with file redirection.
A completed job's full test artifact was still downloadable while another job
in the workflow ran, so artifact inspection supplied the actual failure evidence.
For raw logs, gh suggests --allow-escape-sequences; use it only with a private
file destination and sanitize escapes before displaying contents. Do not mistake
this client-side refusal for a missing job log or a successful empty capture.
