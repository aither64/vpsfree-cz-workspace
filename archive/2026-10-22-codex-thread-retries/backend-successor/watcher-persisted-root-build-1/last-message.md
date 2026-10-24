Both released verification drivers completed successfully with exit 0.

- `run-affected-packaged-verification.py`: passed; driver reported build checks in 239.8 seconds, with all recorded checks and source-after checks exiting 0.
- `run-composed-verification.py`: passed; driver reported system build in 98.5 seconds, with all recorded checks, output closures, rollback checks, and final source checks exiting 0.

Both ran concurrently from the initiative directory. No command remains running. The drivers’ complete raw output was retained in the execution logs; they did not print result artifact paths.