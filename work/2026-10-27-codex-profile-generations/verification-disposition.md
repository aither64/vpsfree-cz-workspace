# Verification disposition

Packaged steps 1/2 passed. Local step 3 was intentionally interrupted by lead with SIGINT to verified Nix pid/group 2067499 after accepted exact CI equivalence. Raw controller labels it failed/exit 1; final log says `error: interrupted by the user`, no test assertion failure. This is canceled duplicate verification, NOT a successful local run or a failed-test rerun.

Successful VM evidence is creation-ci-reuse.json + ci-creation.log: same `2sma25j1bh8862lwrij0zpcwhk44sj7p` check and `08zdpg38y1mwaj11008z0xzqw7qrvhfq` driver, exact c2182254 source and complete input graph. CI conclusion success; script 915.58s. Parent accepted reuse under existing exact-derivation policy.

Verified Nix command and batch controller 1564411 exited after cancellation; no matching owned VM derivation process remains. No source/profile/deployment mutation. Original watcher receives cancellation disposition and stops. Fresh gpt-6-luna/low utility will run configuration build only; parent alone copies/deploys.
