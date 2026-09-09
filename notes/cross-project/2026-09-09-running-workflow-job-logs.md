# Download completed job logs before the workflow finishes

`gh run view --job ID --log` can refuse logs while another job in the workflow
is still running. Use the REST job endpoint instead:

```sh
gh api --allow-escape-sequences repos/OWNER/REPO/actions/jobs/JOB_ID/logs > job.log
```

The escape-sequence flag is needed by newer gh versions for ANSI-containing
logs; redirect to a file for inspection. Retrieve job IDs with
`gh run view RUN --json jobs`. This exposed the actual RSpec failures during
the ongoing IP release workflow, without rerunning or canceling other jobs.
Related initiative: work/2026-09-09-ip-release-mechanism.
