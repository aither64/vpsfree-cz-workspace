# Recovery deployment verification

Passed the bounded read-only verification at 2026-10-27T17:38:24.512277+00:00.

- Original switch: exit 0 in 49.362s; source `af6d9c133726c49332e99239b624f7646dab7d68`, runtime `b748e3c3cf5711980cc46608ee27f517b95e5c7d`. The original PID is gone and no owned switch/activation process remains. The raw process scan's sole match was this verifier shell, retained separately and explicitly excluded.
- Selected profile/workspace-host and actual portal/router executable/package root: `/nix/store/7pa7j9pdf5qpk26i4h4n5lmphwqm8f9h-dev-workspace-0.2.0`. Services are active/running with exit status 0; portal/router restarted as expected.
- Native PID `3555077` / start `1241457907` / actual `5rm5…/libexec/codex/bin/codex` unchanged. Tmux `435397` / `842484713` and user manager `4239` / `4036366` unchanged.
- Both system pointers: `/nix/store/k7w9rmdp2aj7i4r1c833v319k3l9zm7c-nixos-system-aitherdev-26.05.20261026.718f670`, matching the accepted clean configuration `05b5c3ae6a307d2acbf1540ff21d12f56214837a` and generation `2026-10-27--18-14-13`.
- Portal Unix health and canonical-Host router Unix health: HTTP 200, `{"ok":true}`. Own session page and served `app.js?v=61`: HTTP 200. Served JS equals accepted **b748** source bytes; SHA256 `2f3e7f46c4f39cf3b65ce969614bee3cb7d79f498961947c40b0f359eb3c7e06`.
- Exact machine claim `2ecc0cfa-f985-4b77-91de-38b36eeab0fc` remains **held**, owner `a846b5e2-83c9-4675-96f7-c5e5af8c1165`, revision 1. No release or integration performed.

Evidence: `switch.meta`, `switch.exit`, `switch.log`, `status-after.txt`, `services-after.txt`, `user-manager-after.txt`, `identities-after.json`, `effects-after.json`, `claim-after.json` and the retained HTTP status/body/hash files in this directory. Verification used synchronous read-only commands; all returned and no asynchronous check was launched.

## Limits

No public exact pending-transition reader is available; no private pending file was read and pending absence is not inferred from an inactive unit. The successful original switch receipt and observed identities are the completion evidence. The root-owned user-manager executable link is unreadable; PID/start/service metadata establish continuity without a privileged workaround. Known HTTPS issuer failure was not retried or bypassed. This HTTP/page/static-asset check ran no JavaScript, message send, Continue, dismiss, CPU workflow, naming/provider inference, tests or probes, and read no foreign session records/transcripts. Separately published naming-high work was not part of this cutover. No source, Git, claim, selection, reconciliation, merge or lifecycle mutation was made.
