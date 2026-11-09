- **Result:** Raw `exit_status` is absent from the status file. It records `command_complete=true` and `private_result.status="passed"`, but that does not provide the exact exit status required to report a terminal command result.
- **Operation identity:** `parent-exec63086 genuineActionsrun42526944434-number11-attempt1-a66 artifact13635427642 copy/read-onlyprivateparity`; run `42526944434`, attempt `1`, artifact `13635427642`, head `a66b7a0102a369a7d9f8fba2ef548319b5508d0f`.
- **Status identity:** The file’s binding matches those run, attempt, artifact, and head values. It records command PID `1677317` and receiver PID `38601`.
- **Duration:** The status reports `10.149218085920438` seconds total and `3.9156595079693943` seconds for the command.
- **Log:** `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/p24-actions-private.log`
- **stillRunning:** `[]` — the atomic status says the command completed. My watcher tool session has also completed.

I can’t report a terminal result with an exact exit status because that field is missing.