# Modern post-review verification

Target: `1c8478bceb3943645ec06ccde895ee4b0985873f`, tree
`7d3169bc4f80af199631e73cc4442b7985d8cf6d`, over
`63d484fc070dbee633d32624de545e834d483701`. Independent original range/report and
prescribed successor acceptance: [review reconciliation](review-reconciliation.md).
Draft PR: https://github.com/vpsfreecz/vpsadmin-webui/pull/122.

All released local checks passed, exit0, 2026-11-01T19:11:10Z–19:14:58Z
(3m48s). Fresh Luna/low watcher owned one related operation; no source edit or
retry occurred. Node24.21.0/npm11.19.0 from locked Nix shell.

- `nix develop -c npm test`:314files,1976tests passed,37.06seconds.
- `nix develop -c npm run build`:passed,21.36seconds; existing chunk-size notice.
- Selected advisory admin/update-mutation desktop wrapper run:10passed,1.1minutes.
- Selected node/outage mobile wrapper run:2passed,20.8seconds.
- `nix build --no-link --json .#frontend .#bff .#checks.x86_64-linux.provenance .#checks.x86_64-linux.source-contents .#checks.x86_64-linux.package-contents`:allpassed.

Browsers used locked Nix Chromium, own loopback port5189, one worker,
max-failures1, no retries/capture-only shortcut/live credentials. Data is synthetic;
fixture success does not prove backend locking/cascade/mail. Primary API and
legacy real integration remain separately owned. No deployment/default integration
or lifecycle action occurred. No operation remains; utility slot released.

Both package build-info records bind full1c8478bc and dirty:false. Flake Git
source:`/nix/store/wvqxim6nqra2wbhjqdkcn64sgvyp9iym-source`; cleaned package source:
`/nix/store/rf9zg89hf0ksirxgaqfcpli1qbkqg7zq-source` (BFF uses its bff/ subtree).
Frontend npmDepsHash:`sha256-TlJjsHvAx/4mNyWUfOa6OguUg4kgwK7aHw6KjhUIkRo=`;
BFF:`sha256-pifjCWQ5ShvtQw1V3bAlmutW43nPi93hDVW8Q4HuVMw=`.
Recursive receipt contains1799derivation nodes. Combined runtime closure has60paths
and includes full Node/npm/shell references; no minimal-runtime-closure claim or
unrequested packaging redesign. Declared source/provenance/installed-content checks
passed. Exact source/content acceptance concerns this immutable head only.

| Output | Derivation | Store path |
| --- | --- | --- |
| -webui-frontend-1.0.0.drv | `/nix/store/x2jx6r6kf7c615h6qi6p82m1kjizh8j2-vpsadmin-webui-frontend-1.0.0.drv` | `/nix/store/cl3vai81y77i88jp5ym10ch4qskl6zb4-vpsadmin-webui-frontend-1.0.0` |
| -webui-bff-0.1.0.drv | `/nix/store/saq5ghjjswzqcrdxbfkdzkgz3kflapnc-vpsadmin-webui-bff-0.1.0.drv` | `/nix/store/yn1vbayj8kvx9xjim3x9iy9s3nsrb885-vpsadmin-webui-bff-0.1.0` |
| -webui-provenance.drv | `/nix/store/ny33jynq7m66q5w6q4rxq4q5bqbigvxn-vpsadmin-webui-provenance.drv` | `/nix/store/p3vlsh9drr8mjjvahb4h4sy3r915n6sn-vpsadmin-webui-provenance` |
| -webui-source-contents.drv | `/nix/store/sickcp04xh980qxz095v3glqycn8sr96-vpsadmin-webui-source-contents.drv` | `/nix/store/b482rw29c2d6m05g7w2vg9lkpy9q2gia-vpsadmin-webui-source-contents` |
| -webui-package-contents.drv | `/nix/store/yj589rr2f9wyk7mirqkhh228l1rvip2d-vpsadmin-webui-package-contents.drv` | `/nix/store/2z296gmzic5x63nr6d2g20djlchq3sib-vpsadmin-webui-package-contents` |

## Complete locked input graph

| Node | Revision | Content hash | Inputs/follows |
| --- | --- | --- | --- |
| home-manager | c47b2cc64a629f8e075de52e4742de688f930dc6 | sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg= | `{"nixpkgs": ["vpsadmin", "vpsadminos", "impermanence", "nixpkgs"]}` |
| impermanence | 7b1d382faf603b6d264f58627330f9faa5cba149 | sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y= | `{"home-manager": "home-manager", "nixpkgs": "nixpkgs_2"}` |
| netlinkrb | d9de53d843d2586ffa5b7b404887fa801c697ddf | sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg= | `{}` |
| nixpkgs | 5e2305d577ca00acbba631b05cb1094d172b29f3 | sha256-/eLCD/X9kaWJqPR47+fDozEC87Hjmm3i8gJbYmDAD7g= | `{}` |
| nixpkgsUnstable | e158d9ed9b51c98974c5e66e1ba1c9e0255fecaa | sha256-hKlVl12B1dF0Q5vd9dY3lIJM5mFGWYSlXwSLAqHZ1+s= | `{}` |
| nixpkgs_2 | e4bae1bd10c9c57b2cf517953ab70060a828ee6f | sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc= | `{}` |
| nixpkgs_3 | 5e2305d577ca00acbba631b05cb1094d172b29f3 | sha256-/eLCD/X9kaWJqPR47+fDozEC87Hjmm3i8gJbYmDAD7g= | `{}` |
| root | root | — | `{"nixpkgs": "nixpkgs", "vpsadmin": "vpsadmin"}` |
| ruby-lxc | 004bf35eb90d41ba60b347b5b1e73d868a4f95d9 | sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE= | `{}` |
| vpsadmin | a65a4dfeb92a59df4a80a737a20bcbf8558793ff | sha256-mT3f1aRybGtZIQYRrHHEjdTp5foxhmAWu4KJogZ48Rk= | `{"nixpkgs": ["nixpkgs"], "vpsadminos": "vpsadminos"}` |
| vpsadminos | 97045e5a5ff6671c65e6d7515bef0cdb43e708cb | sha256-jxK97bRNtEpmk5wKqeUeN1LzNZFlVq1hGJkrQV8fddE= | `{"impermanence": "impermanence", "netlinkrb": "netlinkrb", "nixpkgs": "nixpkgs_3", "nixpkgsUnstable": "nixpkgsUnstable", "ruby-lxc": "ruby-lxc"}` |

Lock SHA256s:
flake:`6ea5fc4d9d7b43a6c4d6b18a70dc7206f3ba760053513215093b58e24721fa99`;
rootnpm:`87c94a4fb28d57b633b0142a441fa398153b472e129afd354e784ee90509ee28`;
BFFnpm:`50ffa053cd8b22d78505d10117fa2a42db62f73f6aa0b6de18138cbca9277d5a`.

Logs/raw receipts are retained under [modern-verification/](modern-verification/)
and `/tmp/2026-11-01-advisory-modern-*`. Browser report/results paths use that same
/tmp prefix with desktop/mobile-report/results suffixes. Raw artifacts remain
untracked/disposable under workspace retention policy; this Markdown preserves
compact source/input/output/result evidence.

Fresh single snapshot at2026-11-01T19:42:38Z confirms both exact1c8478bc runs
completed success: [CI41339759463](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41339759463)
and [browser41339759427](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41339759427).
CI jobs Required nonbrowser checks124947074795, Production build124947074887 and
Chromium script regression124947074918 all succeeded. PR smoke jobs mobile-chrome
124947429117, mobile-webkit124947429262 and chromium124947429452 all succeeded.
No failed completed job needs diagnosis. Raw exact-head job snapshots are retained
as modern-verification/{ci,browser}-final.json. No wait/rerun/cancellation/local
check/utility occurred for this bookkeeping. No current-head run cancelled;
superseded b02c922a smoke41338075464 completed cancelled after the final push.
Modern released local and CI package is complete; fixtures still do not establish
real API correctness, which remains the separate API/legacy package. The selected
local advisory cases do not imply advisory WebKit coverage where that project's
selection excludes them. Draft PR/source remain unchanged; integration/deployment
still require separate direction.
