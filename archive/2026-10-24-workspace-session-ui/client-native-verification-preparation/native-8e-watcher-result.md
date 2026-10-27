**Result: failed**, exit status 1. The exact runner command ran once and exited after the final state-upgrade stage failed.

- Tested revision: `8e36734a5a5157e21f5719b2e52d6ba4686ec8d5`, tree `459962e198d4ecdab9fd75b299c8850ff3ce2e48`.
- Stages 00–05 passed. Stage 06, `TestNativeStateUpgrade0163To0164`, failed after 3 seconds. Total recorded stage time: 65 seconds.
- Failure excerpt: `native_upgrade_integration_test.go:166: headless bootstrap marker must identify the thread`
- Runner, bindings, and input guards matched their required hashes. The immutable client source was `/nix/store/sgzkqhjrvg80zg2x8m44qkk1ds9lpbs2-source`.
- Receipts and logs are retained under [attempt-8e36734-01](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/client-native-verification-preparation/attempt-8e36734-01). The last completed stage was `05-strict-provider-selection`; stage 06 failed. The runner reports `input_guard_exit=0`. The operation finished; no process remains running.

No diagnosis or retry was performed.