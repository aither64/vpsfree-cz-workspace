# osctld repair verification

Final feature head 60f9ed1c153a734880e002b63d6ab7ed5fe87d0e on staging base d531fc90888e3eabf17889b0dff94c648866cea4, published over SSH. One cohesive repair; no migrations or dependency/kernel changes. Reviewed independently with no findings, including narrow VM assertion corrections.

- 30 focused unit examples passed. Exact-old-helper negative control fails premature-limit ordering; corrected helper passes.
- Final focused VM3/3 examples passed in388.46 s on unchanged cached6.12.113.
- Packaged helper loaded source SHA25696ca72b3ee79bbff5627b2939674987725923706ec64669720c2ad5bfc58389f. Preparation1,200 inherited FDs,NOFILE 8192/8192; workload UID 65534,NOFILE 1024/8192,7 open FDs.
- Two containers autostart in parallel; actual init limits, exec, console roundtrip and stopped states pass. Broad unexpected EMFILE/EOF assertion passes, excluding only exact normal console TTY0 closure for these 2 test IDs.
- GitHub RSpec and RuboCop pass. Broader CI39120729965 remains queued; not claimed successful.

Evidence: unit-check-patched-ruby.log, ordering-control.log, final-review.md, final-review-delta.md, vm-retry.log, vm-final-run/*.log, ci-final-status.json. Initial VM test-assertion failures retained vm-first-run; corrected and reviewed before final run. No production deployment/recovery, merge or session lifecycle action.
