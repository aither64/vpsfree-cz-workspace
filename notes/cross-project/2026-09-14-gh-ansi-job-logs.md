# Download GitHub job logs containing terminal escapes

Initiative: `work/2026-09-13-auth-email/`.

`gh api repos/OWNER/REPO/actions/jobs/JOB_ID/logs > /tmp/job.log` can refuse
job output containing ANSI terminal sequences, even with stdout redirected.
The override belongs to the `api` subcommand:

```sh
gh api repos/OWNER/REPO/actions/jobs/JOB_ID/logs \
  --allow-escape-sequences > /tmp/job.raw
```

`gh --allow-escape-sequences api ...` is invalid. Download privately, strip
terminal escapes before displaying selected diagnostic lines, and keep raw
logs out of tracking commits. This retrieved the failed vpsAdmin routes and
engine logs and exposed the root causes before the fix push.
