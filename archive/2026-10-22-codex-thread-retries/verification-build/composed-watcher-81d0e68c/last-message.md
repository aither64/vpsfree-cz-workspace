**Result: incomplete.** The W/C no-build checks, all 12 selected packaged checks, the composed workspace package build, and the scoped confctl generation build succeeded. The final-source deployment-contract check was reused from its exact successful receipt.

The confctl build selected generation `2026-10-22--22-16-53`. The required Ruby receipt command then failed with exit 1: `mkConfigDevShell mode 'tools' requires ./Gemfile`. I stopped without retrying. No process remains running; no copy or activation occurred. The final C source comparison was not reached.

Full command evidence, logs, build roots, and the result are retained under [composed-81d0e68c](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/verification-build/composed-81d0e68c/result.md).