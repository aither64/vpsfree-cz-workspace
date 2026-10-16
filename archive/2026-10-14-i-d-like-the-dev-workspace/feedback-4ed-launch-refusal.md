# First 4ed browser launch refused before testing

The utility redirected the wrapper's stdout to feedback-4ed-browser.log before
invoking it. The wrapper refuses an existing log; it exited before environment
setup or Go/browser execution. The utility then wrote its exit1 to the status
path. The log is empty and the status is the utility launch result, not a test
result. No browser fixture ran and no operation remains active.

The watcher confirmed its exact shell invocation and file ownership. Both
original outputs remain untouched. A new verified-suffix wrapper preserves the
same reviewed source/check/environment and owns its separate output files.
The fresh watcher is explicitly instructed to invoke the bare command, without
redirection or writing wrapper status. This is correction of a known launch
error, not a retry of a failed test or evidence of product behavior.

Source: 4ed9af55127743b7564cb4dd01d10c9f7fee5120.
