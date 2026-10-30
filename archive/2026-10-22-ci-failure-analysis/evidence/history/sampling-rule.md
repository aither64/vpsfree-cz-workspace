# Sampling rule declared before classification

Select the latest 15 completed CI workflow runs created before current run 39767770407 (whose per-run remote retrieval is prohibited). Start with the most recent API listing; exclude that run before any per-run retrieval. Retain cancelled, prebuild and unexecuted outcomes. Do not select by failure signature. Report changes in workflow/test availability separately, with execution proven by native results or job logs. All selected family observations are retained even where an older source predates that family. The current preserved run is context only, outside the historical denominator. Reuse seed run 39600028637 archive, do not redownload it.

Retrieval is read-only and bounded to this initial sample. Artifacts are shared once per run/attempt/artifact-ID; metadata and hashes record provenance. Attempts and heads are counted separately.
