# Current registered-head merge audit

Exact ancestry of every registered local feature head against the configured remote default. Recovery/supersession is not inferred.

| Registered alias | Local feature head | Remote default head | Exact ancestor | Local = remote feature | Tracked dirty |
| --- | --- | --- | --- | --- | --- |
| haveapi | 723037393318 | master 391b0190241c | NO | NO | no |
| vpsadmin | 33d6c7723b39 | master 097226b22edf | NO | yes | no |
| vpsadmin-031 | 9c1b3f773555 | master 097226b22edf | NO | NO | no |
| vpsadmin-default-api-specs | a089b530376c | master 097226b22edf | NO | yes | no |
| vpsadmin-haveapi-032 | aae07e629883 | master 097226b22edf | NO | yes | no |
| vpsadmin-haveapi-dev | 59d762308c87 | master 097226b22edf | NO | yes | no |
| vpsadmin-haveapi-style | 90e2a79092ba | master 097226b22edf | NO | yes | no |
| vpsadmin-live030 | 70a2ed54b98d | master 097226b22edf | NO | yes | no |
| vpsadmin-live0311 | 9697bf28c317 | master 097226b22edf | NO | yes | no |
| vpsadmin-live0312 | 8102179cf7f7 | master 097226b22edf | NO | yes | no |
| vpsadmin-oauth-client-logs | 097226b22edf | master 097226b22edf | yes | yes | no |
| vpsadmin-refresh | 2c6542941fde | master 097226b22edf | NO | yes | no |
| vpsadmin-webui | 2e32c814d3af | main 63d484fc070d | NO | yes | no |
| vpsadmin-webui-031 | f2765d3fd778 | main 63d484fc070d | yes | yes | no |
| vpsadmin-webui-live030 | f10d3d48c4f2 | main 63d484fc070d | NO | yes | no |
| vpsadmin-webui-live0311 | e468ca48406b | main 63d484fc070d | NO | yes | no |
| vpsfree-cz-configuration | 249f2eb5896b | master c040c14cdbac | NO | yes | no |
| vpsfree-cz-configuration-oauth-clients | c040c14cdbac | master c040c14cdbac | yes | yes | no |
| vpsfree-dev-workspace | ab9346b0c4b9 | master e4e7e95ed39b | NO | yes | no |
| vpsfree-dev-workspace-services-os | e4e7e95ed39b | master e4e7e95ed39b | yes | yes | no |
| vpsfree-dev-workspace-writing-policy | d4355518d945 | master e4e7e95ed39b | NO | yes | no |
| workspace | eeec0c40d66a | master 6383e8848c92 | NO | yes | no |
| workspace-services-os | c83620f63200 | master 6383e8848c92 | yes | yes | no |

| Canonical remote | Readback UTC | Configured default(s) |
| --- | --- | --- |
| git@github.com:vpsfreecz/haveapi.git | 2026-11-01T20:07:27.346980+00:00 | refs/heads/master 391b0190241cf195a69b06f7297d3e4eebec5a83 |
| git@github.com:vpsfreecz/vpsadmin.git | 2026-11-01T20:07:28.736775+00:00 | refs/heads/master 097226b22edf8b59f80b5dfaa55265e9d0cac633 |
| git@github.com:vpsfreecz/vpsadmin-webui.git | 2026-11-01T20:07:30.049368+00:00 | refs/heads/main 63d484fc070dbee633d32624de545e834d483701 |
| git@github.com:vpsfreecz/vpsfree-cz-configuration.git | 2026-11-01T20:07:31.406631+00:00 | refs/heads/master c040c14cdbacc07998700b524996a89306188d7f |
| git@github.com:vpsfreecz/dev-workspace.git | 2026-11-01T20:07:32.671502+00:00 | refs/heads/master e4e7e95ed39bf514b33f8f8ae61ba9868de060ae |
| git@github.com:aither64/vpsfree-cz-workspace.git | 2026-11-01T20:07:34.054147+00:00 | refs/heads/master 6383e8848c92c06a9d817f8109853b5b61305c89 |

Tracked dirtiness (paths/status only):

None in the owned worktrees inventoried.

Full IDs, remote feature discrepancies, necessary fetch effects and ancestry results: [JSON](merge-status.json).

Exact ancestry only. No recovery/supersession/canceled-work equivalence inferred; A0 owns reconciliation. E2 observer89033 not inspected or queried. Only own session worktrees have tracked status read; shared workspace checkout status excluded.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/)
