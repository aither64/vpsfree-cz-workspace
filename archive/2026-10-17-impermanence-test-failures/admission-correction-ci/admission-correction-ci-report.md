# Admission correction CI verification

- Session: `2026-10-17-impermanence-test-failures`
- Repository: `vpsfreecz/vpsadminos`
- Tested head: `e32d5382910501b0c8fe80bc6b9e6044e56ead8e`
- RSpec run `39396698231`: completed, success; `gh run watch` exit 0; 3m56s reported job duration. Raw watch output: `/tmp/admission-correction-ci-39396698231.log`.
- RuboCop run `39396698224`: completed, success; `gh run watch` exit 0. Raw watch output: `/tmp/admission-correction-ci-39396698224.log`.
- Native run `39396698293`: sampled after both hosted checks; status `in_progress`, conclusion empty, head matches. Not awaited per instruction. https://github.com/vpsfreecz/vpsadminos/actions/runs/39396698293
- Failed logs: none; both hosted checks succeeded.
- Elapsed observation time: approximately 4m.
- Failure excerpt: not applicable.

Both hosted runs were observed with `gh run watch --repo vpsfreecz/vpsadminos --interval 60` using the specified run IDs. The initial RSpec invocation without `--repo` addressed the ambient default repository and returned HTTP 404; it was not a check result. The same existing run was then watched in the correct repository.
