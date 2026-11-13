# F1 reviewed clean-rebase equivalence and check reuse

Original review: reviewer0 Sol/xhigh, all4 lanes, no F1 findings; final-review.md.
Original range 6f71da9777edfc902f6483edcdd84a2ef7d464ab..81d754f47a58e92fddb2a84c67b1aec98b740ae3.
Refreshed range 74e3ab79118fb4a0a013d6c4ace20352e6d62e5f..2d0946c4e699aa61092228d8a7cb275477ee46d0.

Lead independently applied exact reviewed binary patch to new base in disposable Git index. Reconstructed complete tree 553e895ec95ecdc0ed4a90d2e312da674e516c31 equals refreshed head tree. Complete old/new feature diffs are byte-identical. Range-diff:

~~~text
1:  81d754f47 = 1:  2d0946c4e api: correct raw migration default expectations
~~~

One coherent11assertion test commit, no migrations/pin streams/obsolete history. Upstream bases differ only packagedAPI/console dependency metadata and WebUI dependency files. Source/helper/spec/hooks/instructions/Gemfiles/flake graph paths independently confirmed unchanged. Clean patch-equivalent rebase preserves recorded user repository/master approval and source review.

Complete environment comparison:

api: identical bashFunctions/all value-bearing environment fields, output /nix/store/6xasqclpph7jj3vls5zr9a3ffrxdg191-vpsadmin-api-env. Only six value-less type=unknown placeholders omitted by refreshed encoding: ['BASHOPTS', 'BASHPID', 'OPTIND', 'SHELLOPTS', 'SRANDOM', 'noBrokenSymlinksHookInstalled'].

root: identical bashFunctions/all value-bearing environment fields, output /nix/store/5m7xf80v9h6wrscc0r6jiznhnb1b221d-vpsadmin-env. Only six value-less type=unknown placeholders omitted by refreshed encoding: ['BASHOPTS', 'BASHPID', 'OPTIND', 'SHELLOPTS', 'SRANDOM', 'noBrokenSymlinksHookInstalled'].

Effective coreAPI Gemfile.lock independently byte-compared to saved tested lock: SHA256 bb4bccb319f98631d7c7c10a6560c517a475d7ee96c0252fd06923622c755e61.
The already passing full migration run is /tmp/f1-scheduled-workflow-fixes/full-migrations.log:84examples/0failures24.41s, isolatedMariaDB11.4.12/AR8.1.4.1. Exact valued environment/input equality, functions and core lock support reuse for refreshed head; tree equality alone was not used. No duplicate run for rebase. Original hosted18example MariaDB11.8 result retains original provenance; new integrated-master full workflow remains separately required.

Failed first comparison assumed different Bash recording names; inspection established six unknown/no-value placeholder omissions. No meaningful input discrepancy or source repair resulted.
