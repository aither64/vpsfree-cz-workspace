# Final branch inventory: numbered paste follow-up

No migrations. The previously deployed 14-commit deliverable is retained as consumed provenance. Four focused follow-up commits implement naming and consumer/deployment adoption. Workspace was rebased onto current shared master 21624498; range-diff proves its three consumed pin patches unchanged (c89e35ae/76bc6985/97ab907c ->73efd334/99a4152c/6112aee4). No superseded unconsumed implementation or compatibility path remains.

## codex-web

Base: 3d07cf60cfde5d117a181a9bdb6d90a5860f6f0c; head: 7dab76305dc0084735095d6dbdaef607585d9bca.

dd13156b051c1ae32bc9bc409b622b5eb5d58e18 codex: expose account credits and idempotent limit resets
8263ccd44587a50148242d4e94d2e582d6bda759 conversation: attach binary clipboard files from the composer
860d515d0aa5d2f7ad68893db41f0969c78e00a7 conversation: keep refresh quiet and edit settings in a dialog
7dab76305dc0084735095d6dbdaef607585d9bca conversation: number pasted attachment filenames

codex/client.go                             |  53 ++++++-
 codex/client_test.go                        |   4 +-
 codex/reset_credit_test.go                  |  78 ++++++++++
 conversation/assets/conversation.css        |   4 +
 conversation/assets/conversation.js         | 216 +++++++++++++++++++---------
 conversation/assets/refresh.js              |  75 ++++++++++
 conversation/assets/sync.js                 |  33 +++--
 conversation/assets/uploads.js              |  92 +++++++++++-
 conversation/handler.go                     |   2 +-
 docs/reference.md                           |  49 ++++++-
 flake.nix                                   |   2 +-
 test/codex_protocol_contract.py             |   7 +
 test/conversation_browser_contract_test.cjs | 100 +++++++++++++
 test/refresh_browser_contract_test.cjs      |  66 +++++++++
 test/sync_browser_contract_test.cjs         |   5 +-
 test/uploads_browser_contract_test.cjs      | 172 +++++++++++++++++++++-
 16 files changed, 859 insertions(+), 99 deletions(-)

## dev-workspace

Base: c51ba3c0ca0d41d237ef71c56accd564beb70a33; head: 66262519d497073d9bb0dccc2252cdec4528f389.

f824e6900298d0a3f149db1e7abb366aa7eda2f2 portal: keep refresh values visible and compact model controls
c93cb06c1894764ebb670e2a0e563673c7d74bab portal: show credits and confirm banked reset use
675504f638d21578e87a94f460cc9cbf9e0df395 inputs: select the updated Codex web integration
577d5b72b9bdcd68e37cd74f6304b2ca80b8bf97 portal: make account and composer controls compact
c650a4c7ee38ebd546ce91cbbe2f0713abe6bae4 portal: attach pasted files to new-session requests
66262519d497073d9bb0dccc2252cdec4528f389 portal: adopt numbered clipboard attachments

README.md                                          |  38 +-
 docs/workspace-portal.md                           |  50 ++-
 flake.lock                                         |   8 +-
 flake.nix                                          |   2 +-
 nix/workspace-portal.nix                           |   2 +-
 portal/go.mod                                      |   2 +-
 portal/go.sum                                      |   4 +-
 portal/internal/web/auto_archive_test.go           |   2 +-
 portal/internal/web/browser_contract_test.cjs      |   8 +-
 portal/internal/web/codex_limits.go                | 108 ++++-
 portal/internal/web/paging_browser_live_test.cjs   |  17 +-
 portal/internal/web/presentation_browser_test.cjs  |  22 +-
 portal/internal/web/question_browser_test.cjs      |   5 +-
 portal/internal/web/question_browser_test.go       |   3 +-
 portal/internal/web/reset_credits_browser_test.cjs | 115 +++++
 portal/internal/web/reset_credits_browser_test.go  |  16 +
 portal/internal/web/reset_credits_test.go          | 126 ++++++
 portal/internal/web/server.go                      |   4 +
 portal/internal/web/server_test.go                 |  10 +-
 portal/internal/web/static/app.js                  | 462 ++++++++++++++-------
 portal/internal/web/static/reset-credits.js        |  55 +++
 portal/internal/web/static/style.css               |  20 +-
 portal/internal/web/team_settings_browser_test.cjs | 220 +++-------
 .../internal/web/templates/automatic-archival.html |   4 +-
 portal/internal/web/templates/creation.html        |   2 +-
 portal/internal/web/templates/index.html           |   9 +-
 portal/internal/web/templates/session.html         |  18 +-
 portal/internal/web/templates/source-file.html     |   2 +-
 portal/internal/web/usability_browser_test.cjs     | 239 +++++++++++
 29 files changed, 1199 insertions(+), 374 deletions(-)

## workspace

Base: 21624498189f12fec0424d547c6e21c78145e84b; head: 07b393609417e921d5b1c2cfec7b3d89abc473ab.

73efd33418eba29aa1f4d7e7acdf0292d84077df inputs: select the portal usability runtime
99a4152ca6a981cb29cc115a9ca4931277441e1e inputs: select the compact portal controls
6112aee4b5055e824a6590d80f4bfff5720fa06b inputs: select new-session clipboard uploads
07b393609417e921d5b1c2cfec7b3d89abc473ab inputs: select numbered clipboard attachments

flake.lock | 16 ++++++++--------
 flake.nix  |  2 +-
 2 files changed, 9 insertions(+), 9 deletions(-)

## vpsfree-cz-configuration

Base: ae670dc0d4a5d43adf9560da1a6a0a35925cd2e5; head: 1f3569902a4a6b02633019cd172eade5afe90005.

081ac7cc6098f79b004f7ff349e71c85257b518f inputs: set devWorkspace to 675504f6
04ee1fe64e40e9b2c40f073556210196cc37cf88 inputs: set devWorkspace to 577d5b72
557c97a730a0517de1b9db9bc9eafeecd5a79785 inputs: set devWorkspace to c650a4c7
1f3569902a4a6b02633019cd172eade5afe90005 inputs: set devWorkspace to 66262519

flake.lock | 14 +++++++-------
 1 file changed, 7 insertions(+), 7 deletions(-)
