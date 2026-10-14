# Hosted adapter CI failure

[Run 37678050938](https://github.com/vpsfreecz/dev-workspace/actions/runs/37678050938)
completed failure at exact f6d2c080469b224ac77765aecd76a6d531358363. The flake
job failed building organization-source; its output identifies the new
`test/fixtures/kb-config.json`. Owning flake.nix:429-440 rejects deployment-specific
names in tracked files. The copied fixture violates that retained boundary.
This is a concrete source packaging issue, not the earlier push server error.
Metadata and failed logs are retained in kb-runtime-e-ci37678050938.json and
kb-runtime-e-ci37678050938-failed.log. No rerun/local CI was launched. Implementer0
owns a narrow portable-placeholder fixture correction; root will inspect and
publish it with normal hooks. Original source review remains tied to f6.

The narrow correction changes only17 hostname suffixes to example.test. Root
verified exact replacement equality, valid JSON, source SHA/manifests, empty
index/one owned path, source content/path scan and unchanged consumers. This is
mandatory-review step9 direct remediation: rejected test naming is removed;
product behavior, pins and source guard are unchanged. No local CI/tests ran.

Normal hooks folded the correction into provider06eefd98d09d756a8791c494cd855ffcfa625548,
retaining input5b987 and exactly two logical commits/no merges. Expected staged/
final tree equality, histories/diffs and proof are saved under fixture-name-
consolidated receipts. Normal hooks enabled; no framework/path override/custom
hook. Feature publication with verified oldf6 lease succeeded, remote equals06,
default0ff unchanged and tree clean (fixture-name-publish1 exit0).

One hosted snapshot found [CI37679475899](https://github.com/vpsfreecz/dev-workspace/actions/runs/37679475899)
in_progress at exact06. No pass/wait/rerun claimed. Superseded inventory had no
candidates/no cancellation. Package/live-guest/two-PNG gaps remain unchanged.
