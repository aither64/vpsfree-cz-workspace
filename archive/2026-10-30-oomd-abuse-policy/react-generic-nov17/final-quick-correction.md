# Final quick first failure

The original 14-command batch stopped at full typecheck: exit2,76.425s,
0passed/1failed/13notrun. All59input hashes matched. Logs/receipts remain unchanged.

TS7053 came from isPolicy narrowing unknown to generated IncidentPolicy, which
dropped the Record<string,unknown> index shape before checking VPS-only fields.
The predicate now retains that actually checked record intersection. No runtime
expression, assertion, generated model, SDK input or transport changed. A fresh
batch repeats the failed typecheck and executes the13previously unrun checks.

## E2E coverage correction

The resumed batch passed real types0/58.311s and12files/98tests0/10.314s,
then failed E2E coverage1/4.801s: the preparer placed a disposable config under
e2e/test-results, whose ignored TypeScript files are still scanned. The config
was moved to verified ignored/untracked work/g2-preview, with relative test/output
paths corrected. Product, assertion, E2E coverage policy and all59source hashes
remain unchanged. Resume only failed E2E types and11previously unrun commands;
do not repeat successful app types/unit checks.
