# Nov24 retained demo deployment — terminal ROOT ONLY handback

Ordinary services update completed **0 in 239.375s**, after admitted application build **0 in 449.675s**. Pending is null. The existing runner/session remain open and usable. All implementer0 runtime/build/effects windows and capacity return to root; no source, default, profile, host, claim or lifecycle mutation was performed.

## Actual deployed inputs and artifacts

- Backend/PHP `8846c22b20d805ee3d63718d9d23a5be5319b4bf`, tree `24623e460c686325fa88c5a59d5c2dfae1f8302a`.
- React/BFF `ef6c72f4f626822e34934229170195f6d8091764`, tree `f624b9785c77113d05e6f3ca16002a498f9e675a`.
- Site templates `7af51cd6164fd5aad7633f39f6cf4e7ef64c18a7`, tree `e1872cbc645947495160b0b6a13a56cb5b2689d4`.
- Configuration `baf73377af387a8ef1c90e20b17bb559fcd15c45`; config/declaration bytes unchanged, sole trusted OOM policy **3/10** proved in API, supervisor and database contexts.
- OS `52eb4de029f385c3e2d1b614d9b6ff32bbfb29bf`; packaged status f783, historical yz96 recipe/source/released client unchanged. Five worktrees remain clean and frozen.
- Services `/nix/store/rprb7zmgphpmy0hhxikn03cv8vkw34sj-nixos-system-vpsadmin-services-26.05pre-git`.
- API `/nix/store/s3nz3j2l6i5ljvlzww01mkx1m8jy12iy-vpsadmin-api-8846c22b20d805ee3d63718d9d23a5be5319b4bf`; supervisor `y1315xjm47cp609llamam6gb7qkyrlba`; database `0l48bm7w4y5l8jqmi8gk7ik7vlckhw5n` (full paths in private runtime proof).
- Frontend `/nix/store/ywf64vkimrbr70jb122lqbbciksyzcdq-vpsadmin-webui-frontend-1.0.0`; BFF `/nix/store/ba85krm5gl5x763bxcxiqxk5dnabw405-vpsadmin-webui-bff-0.1.0`.
- Captured admitted graph, recipes, projected config and actual package mapping: `private/graph.stdout`, `graph-layout-and-build-names.json`, `actual-package-graph.json`. New result config is `/nix/store/065anfm99dmz934xjhqr25n41yx3r1x3-vpsadmin-devcluster-2026-10-30-oomd-abuse-policy-services.json`.
- Actual frontend source has **2877 included tracked files byte-equal** to frozen ef6; four excluded files match its ordinary `nix/source.nix` filter. **109 unique HTTP-served assets** match the built artifact. Actual nginx selection and BFF process path agree. PHP served symlink/file hashes match frozen 8846. See `served-frontend-result.json`. Packaged frontend `build-info.json` literally reports unknown/dirty/unavailable; provenance above comes from actual source/recipe/served-byte proof, not that label.

## Preservation and templates

`preservation-final.json` proves all original **29 reports / 23 evaluations / 6 actions / 69 MailLogs**, report22/eval20, original membership/counts and saved historical **5/10** unchanged. No new incident/evaluation/escalation action. Users differ only by observed authentication timestamps/IP/count. Preferences, recipients, snapshots and VPS data are unchanged; seed controls and migration lineage match. All three credentials and **16 original BFF session files** match; three legitimate BFF sessions were added.

Both physical VPSes remain **stopped**; native CT records/disks/resources are exact. Node system remains `/nix/store/zv0wss6qmc5s1ip995ycf66nb5b61pr1-vpsadminos-system-dev-node1-26.05.git.ccd51ed`, node kernel **6.12.118**, services kernel **6.12.117**. No node/kernel/root-image/host update.

All **15 protected captures** retain full native rows plus API IDs/received times/flags/tags/headers/plain/HTML/attachment data. Current total **22** includes seven ordinary login captures, paired by exact plain/HTML to MailLogs70–76 (`incidental-login-mail.json`). Nothing was reconstructed, ingested or sent as a test.

Native SQLite online backup integrity and old/snapshot full contents passed; separate private external **147456B** recovery SHA256 `8b820013d47b2202cd9f79bcfe08b6a5a833d94097449da29da55c50def46e23` retained. Mailpit1.33.1 now opens persistent `/var/lib/mailpit/mailpit.db`. Sole local drop-in `/usr/local/lib/systemd/system/mailpit.service.d/50-preserved-database.conf` sets MP_DATABASE, SHA256 `0a826ef127f987fe74d516561f74e96e5bd95dfc0dff8319aa6fa9a53468e12f`. Same-version restart and later services/container update preserved selection and captures; original mail producer resumed healthy. **This is unmanaged per-demo persisted state, not source-reproducible on recreation.** Retain its recovery files/drop-in and verify selection on future retained updates. Root owns consequential recovery; never overwrite a live/newer database or remove selection to fall back to temporary storage.

ONE normal Rake reconcile loaded effective `/nix/store/anvr4fnymyq9ckfadzy0qc969xhagnss-vpsadmin-effective-notification-templates-1` as directory and source_id. All **83 templates**, public metadata, subjects, sender fields and variants match; recipients/preferences preserved. Exactly **10 body changes**: intended daily HTML plus nine previously-nil ordinary backend/plugin plain fallbacks, including daily. Full list and packaged-source proof: `effective-body-comparison.json`. No new template or unexplained drift. Daily producer with normal selected plugin loader and actual stored plain/HTML rendered in a read-only transaction (`daily-render-result.json`); no mail dispatch.

## Usability and direct links

Actual authenticated PHP and React admin Overview/Reports/History, filter/sort/page/refresh, historical report22 and desktop/narrow captures passed; owner allowed, foreign report denied without saved-policy leakage; both new admin APIs return member403 (four checks). See `live-acceptance-result.json`. React narrow cards render; legacy PHP retains its wide table layout on a narrow viewport. External TLS issuer remains qualified; browser capture used the existing ignoreHTTPSErrors setting, without a trust claim.

| Interface | Base | Overview | History |
| --- | --- | --- | --- |
| PHP | https://webui.aitherdev.int.vpsfree.cz/ | https://webui.aitherdev.int.vpsfree.cz/?page=incidents&action=overview | https://webui.aitherdev.int.vpsfree.cz/?page=incidents&action=history |
| React | https://newadmin.aitherdev.int.vpsfree.cz/ | https://newadmin.aitherdev.int.vpsfree.cz/admin/incidents/overview | https://newadmin.aitherdev.int.vpsfree.cz/admin/incidents/history |

Screenshots (actual private demo): `private/php-admin-overview.png`, `private/php-admin-history-narrow.png`, `private/react-admin-overview.png`, `private/react-admin-history-narrow.png`. Full finite set is linked in the acceptance result. Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/

## Effects and literal limits

All native handles joined: build98069/overlay71028; preservation preflight5021, SQLitecopy72424, first guard59597, readonly12082/45005/34174, backup22457, selection21095, settled proof20973, producer88724; update66585; runtime78942; template admission24668/reconcile4400; UI9923/27780/97583 and final denial47316; policy/render93610/51272; final data24590/96987, node17278; served mapping45300/87233/66969/86878. All watchers joined: build39116, first guard93959, preservation84091, update54611, UI11976/4826/83889. No unfinished mutation, pending target or watcher remains.

Preserve literal failed helper evidence: initial default-vhost empty output corrected once to actual configured vhost; immediate Mailpit startup observation settled without second restart; PHP/React selector and loading-wait corrections repeated only unfinished checks with reusable auth state; bare Ruby render lacked ordinary plugin loader; readback helpers initially assumed exact user auth fields/source-filter/system namespace/config paths. These were observation/helper failures, not hidden product passes. Watcher results retain their actual failed/incomplete scopes; final corrected assertions are separate evidence. No extra CI, source, broad browser or build campaign followed. The original build watcher ended incomplete at four minutes; active parent retained and joined the authoritative build0.
