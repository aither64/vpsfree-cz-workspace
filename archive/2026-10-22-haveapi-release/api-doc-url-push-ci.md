# Reviewed URL candidate: feature push and CI handoff

Published only `2026-10-22-haveapi-release` at exact head
`ee150c8515aae399dc14e0fe9daefeb95a8bb17e`, tree `fed8aea303bb91eb488c4c4bbc639356a7488c21`.
Fresh SSH fetch/ls-remote verified target master`a32b15e379f44fc6dae4b15ef4ec17a142e5f465` and prior
feature lease`27b4f8f895a4e5401357a402187c2a4590699aec` before mutation.
Explicit force-with-lease/exact SHA feature refspec succeededexit0, with
--no-follow-tags. Remote after-proof matches final feature SHA and unchanged
master. No default/tag/official release branch/registry mutation.

Top-level HAVEAPI_RELEASE_TOOLS_ONLY=1 Nix; installed executable Overcommit
pre-push entrypoint enabled, no disable variables or bypass. No additional
PrePush checks declared; final source/metadata commit hooks already passed.
Push output in api-doc-url-push.log; exact argv/before+after remote proof and
complete CI snapshots in api-doc-url-push-ci.json and discovery.json.

Source/index clean after push. No build/test/setup/source/history/artifact
mutation, no long checks. Git/source/hooks yielded to lead for fresh watcher;
no process pending after this handoff. Same retained affected4lane review passes
at exact head (api-doc-url-final-review.md); installed/package/full verification
and exact-head CI remain separate gates. Earlier receipts/artifacts preserved.

Read-only gh discovered these exact-head push runs. Status is a discovery
snapshot only; no wait/retry. Cancelled only verified superseded active
same-branch runs if present; count 0.

| Workflow | Run | Status | Conclusion |
| --- | --- | --- | --- |
| clients/rust | [39826642492](https://github.com/vpsfreecz/haveapi/actions/runs/39826642492) | in_progress | pending |
| servers/ruby RSpec | [39826642565](https://github.com/vpsfreecz/haveapi/actions/runs/39826642565) | in_progress | pending |
| clients/go RSpec | [39826642596](https://github.com/vpsfreecz/haveapi/actions/runs/39826642596) | in_progress | pending |
| release | [39826642473](https://github.com/vpsfreecz/haveapi/actions/runs/39826642473) | in_progress | pending |
| i18n health | [39826642540](https://github.com/vpsfreecz/haveapi/actions/runs/39826642540) | completed | success |
| RuboCop | [39826642526](https://github.com/vpsfreecz/haveapi/actions/runs/39826642526) | completed | success |
| clients/js tests | [39826642576](https://github.com/vpsfreecz/haveapi/actions/runs/39826642576) | completed | success |
| clients/ruby RSpec | [39826642609](https://github.com/vpsfreecz/haveapi/actions/runs/39826642609) | in_progress | pending |
| clients/php PHPUnit | [39826642521](https://github.com/vpsfreecz/haveapi/actions/runs/39826642521) | completed | success |
| clients/python | [39826642510](https://github.com/vpsfreecz/haveapi/actions/runs/39826642510) | completed | success |

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
