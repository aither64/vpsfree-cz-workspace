# Read-only postactivation acceptance

Prepared by implementer2 for final candidate
`d0e4318cb1872feb69f3109f032870c310f14bdf`; **EXECUTED / PASS, exit 0**.
Lead owns claims, activation, expected target paths and final acceptance.
User authorized deployment only; no merge or lifecycle action is authorized.

On the lead's activation trigger (host switch session `91112`, chunk `f0d6aa`;
profile session `84251`, chunk `515a96`, both reported exit 0), implementer2 ran
the prepared read-only package **once**. Execution session `25034` completed
exit 0, final chunk `4fd9ed`. Compact result:
`/tmp/files-tab-browser-smoke-2026-10-28-implementer2/live-read-only-result.json`;
stderr log alongside, `live-read-only.log`, is empty. No operation remains.

| Verified after activation | Result |
| --- | --- |
| Exact selected profile | `/nix/store/7wqvb8wdy58x94nh24k0kqnagqldfhvi-dev-workspace-0.2.0` |
| Exact current system | `/nix/store/vkn22mr0xjf72kxkjcgfmclpflz6l9md-nixos-system-aitherdev-26.05.20261026.718f670` |
| Profile deriver/source | `/nix/store/3pi8b0a50cifi96jspadpxsix0n974m4-dev-workspace-0.2.0.drv`; `/nix/store/4f7a480bkrrq6nkw0rpihzh9gr6645ln-source` |
| Active/running services | Portal PID `3445193`, router PID `3444721`, both executing the selected package's `/bin/workspace-portal`; native App Server PID `156049` and executable unchanged |
| Native socket continuity | Device/inode `64769`/`18745722`, unchanged |
| Direct portal and router `/healthz` | HTTP 200, `{"ok":true}` |
| Own directory root | 20 direct children, 994 bytes, no continuation |
| Authorized large session root | `2026-10-24-vpsadmin-haveapi-upgrade`: 43 direct children, 2,021 bytes, no continuation |
| Listing contracts | Root path, entry path/kind, directories-first byte ordering, uniqueness, 200-entry/256-KiB bounds, continuation shape and `Cache-Control: no-store` passed |
| Own page asset URL | `/static/app.js?v=65` present |
| Served/build-source identity | Both assets byte-equal to exact Git source `d0e4318c` and selected derivation source |

Served SHA-256:

- `app.js`: `8905d18ca7fb6d5f6d694a92e2eb02d3e4d0032edbbb8856df7af6c0b7c8e673`.
- `source-file.js`: `7ef5c7cdee39eca1f2919b35a9f1c82c4ad26f591bd8cd06a42c6fd944ff3b9b`.

No prompts, conversation reads, lifecycle actions, source/runtime mutations,
duplicate run, claim release or integration were performed. The lead retains
machine ownership and final acceptance under the user's unmerged deployment
restriction. Public TLS/auth/full-browser and native-turn limits below remain.

Initially prepared for `dd445cb0627f93375f1378af6b59d30ef8b34875`.
After final review passed for `d0e4318c`, the lead reported its 14 Files assets
and full JavaScript byte-identical to `dd445cb0`; no duplicate Chromium smoke is
required absent a gap. Only the live script's expected source SHA was updated;
all immutable served/build-source checks and native continuity guards remain.
Earlier Chromium evidence and diagnosis remain in `browser-smoke-preparation.md`.

Lead-reported **predicted**, not activated/verified, target paths while builds
continue:

- Profile: `/nix/store/7wqvb8wdy58x94nh24k0kqnagqldfhvi-dev-workspace-0.2.0`.
- System: `/nix/store/vkn22mr0xjf72kxkjcgfmclpflz6l9md-nixos-system-aitherdev-26.05.20261026.718f670`.

These predictions were subsequently confirmed by the activation trigger and
the exact-path acceptance assertions above.

Baseline observed before activation:

| Item | Exact identity |
| --- | --- |
| Selected profile | `/home/aither/.local/state/dev-workspaces/profile` → `/nix/store/kdqm98kwk1mly4i1rfx58lnz6cscn6z6-dev-workspace-0.2.0` |
| Profile deriver/source | `/nix/store/pi16yflzhggq1dzf6fs4vds11av0cbyi-dev-workspace-0.2.0.drv`; `/nix/store/f8ww1pcp5v9jb4icybcz5j26w9k19fbp-source` |
| System | `/nix/store/l18arwf42sxzwf864yjwsvnjma5m5cav-nixos-system-aitherdev-26.05.20261026.718f670` |
| Portal | `workspace-portal@vpsfree-cz.service`, active/running, PID `1075392`, executable selected profile package `/bin/workspace-portal` |
| Router | `workspace-router.service`, active/running, PID `1075328` |
| Native App Server | `workspace-codex@vpsfree-cz.service`, active/running, PID `156049`; `/nix/store/5rm5bizqzrc1sjlpbdnwps2cf16dxys0-codex-package-0.164.0/libexec/codex/bin/codex` |
| Native socket | `/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock`; target device/inode `64769`/`18745722` |

Own registry entry confirms workspace root `/home/aither/workspace/ai/vpsfree.cz`
and hostname `vpsfree-cz.workspace.aitherdev.int.vpsfree.cz`. Portal service uses
the stable user profile's `workspace-host run-portal vpsfree-cz`. Direct trusted
user HTTP socket: `/run/user/1000/dev-workspaces/vpsfree-cz/portal.sock`.
Router socket: `/run/dev-workspaces/router.sock`, with that Host header.
Both `/healthz` requests returned 200, `{"ok":true}`. Own directory route returned
404 on the old runtime, as expected. This was a preactivation baseline; the new
route is now verified as recorded above.

Exact command executed once after the activation trigger:

```sh
/nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15/bin/python3 \
  /tmp/files-tab-browser-smoke-2026-10-28-implementer2/live-read-only.py \
  --expected-profile /nix/store/7wqvb8wdy58x94nh24k0kqnagqldfhvi-dev-workspace-0.2.0 \
  --expected-system /nix/store/vkn22mr0xjf72kxkjcgfmclpflz6l9md-nixos-system-aitherdev-26.05.20261026.718f670
```

The standard-library script uses GET only and prints compact metadata/hashes:
selected system/profile, profile deriver/source, active services, native
PID/executable/socket continuity, direct portal/router health, own root directory
and already-authorized large `2026-10-24-vpsadmin-haveapi-upgrade` root page.
It validates direct-child path/kind shape, alphabetical directories-first order,
uniqueness, page/byte bounds, continuation shape and no-store header without
printing entry names or opening their content. It reads only page one; no
recursive legacy endpoint or optional child expansion is needed.

It reads this session's page only to verify `app.js?v=65`, compares served
`app.js` and `source-file.js` byte-for-byte with Git source `d0e4318c` and the
selected derivation's source, and reports SHA-256 hashes. Nix 2.34's
`derivation show` wraps results in `derivations`; the script handles that shape
and the older direct mapping. No build, Codex request, prompt, transcript,
credential, state mutation or deployment is performed. Temporary code stays
outside tracking; no new dependency installation or proxy framework.

Limits: public HTTPS health probing failed local CA verification (curl 60), so
direct Unix HTTP verifies portal/router health, not public TLS, Basic auth or a
full public browser. The separate real Chromium fixture smoke and served-asset
identity support native Files behavior; this live package does not reenact it.
Native PID/socket continuity is evidence of process continuity, not a new model
turn or conversation-content check. Exact full source/input graph and rollout
selection evidence remain lead-owned.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-files-tab-limit-diagnosis/>.
