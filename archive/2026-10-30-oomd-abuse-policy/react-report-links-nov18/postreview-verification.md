# Nov18 React post-review verification

Reviewed and verified source remains clean `6b14ae5e1702ee8c137605d3512c123c9a24b582`,
tree `727af56aede9132a1e9a77c5726330f31ed61044`, on retained base
`88ac13b89d6421c914cd57e18153de1fee6fc7b7`. Reviewer0 completed all four lanes
without findings before these checks. No source change, new commit, SDK install,
npm/type/unit repeat, push, PR/CI operation, deployment, demo or KB action occurred.
The existing three-purpose history and preservation refs remain unchanged.

## Exact five-target Nix package proof

Ordinary command (React repository cwd):

```sh
nix build --no-link --json --print-build-logs --max-jobs 1 --cores 2 \
  .#frontend .#bff .#checks.x86_64-linux.provenance \
  .#checks.x86_64-linux.source-contents .#checks.x86_64-linux.package-contents
```

Native83916 passed0 in68.558s, with all frozen inputs matched. Preflight showed
six small application/check derivations and923KiB cache restoration; no kernel
or large restoration. One build job and two cores were used. The provenance
target reused its declared cached output; all five actual returned derivations
and outputs match the evaluated declarations. Original stdout, build log, raw v4
derivations, flake metadata, dry run and result are retained under postreview-package-*.

Both installed schema-1 metadata files were read immediately after success:
full6b14, dirty=false, source=environment, equal metadata. The source gate passed
with18 required inputs; installed contents passed with387 public assets. Ordinary
npm fetching/install/build succeeded on x86_64 with the actual immutable Nov18
HTTPS SDK and cache hash. This resolves the documented six optional WASI-cache
warnings for this package build. It does not establish shell/toolchain absence.

| Derivation | Output | NAR hash |
| --- | --- | --- |
| `/nix/store/pkck85qmpik0z8n4ig539mjn6gzsixm1-vpsadmin-webui-frontend-1.0.0.drv` | `/nix/store/q5xhvzy93bc422h2pz2zkix3lsxnprx6-vpsadmin-webui-frontend-1.0.0` | `sha256-f4e4zzn46rLDwThMG//Bebi+sWHuasgWA/uZPdTXQ9o=` |
| `/nix/store/jlai6j41mjhj9z0kcbvnw78ak2x6flzg-vpsadmin-webui-bff-0.1.0.drv` | `/nix/store/399kwx0n6x2y1mfhl13023pszxmyqmpk-vpsadmin-webui-bff-0.1.0` | `sha256-5v+oXrN8pMABueAx/v56dqZafZY8ly8d36TJF12cuUw=` |
| `/nix/store/ny33jynq7m66q5w6q4rxq4q5bqbigvxn-vpsadmin-webui-provenance.drv` | `/nix/store/p3vlsh9drr8mjjvahb4h4sy3r915n6sn-vpsadmin-webui-provenance` | `sha256-d6xi4mKdjkX2JFicDIv5niSzpyI0m/Hnm8GGAIU04kY=` |
| `/nix/store/rsq86n28k2w6kbz90m3m1mas08rz94v1-vpsadmin-webui-source-contents.drv` | `/nix/store/hia5ydg0100x78avny0qv8s31jizhz9n-vpsadmin-webui-source-contents` | `sha256-d6xi4mKdjkX2JFicDIv5niSzpyI0m/Hnm8GGAIU04kY=` |
| `/nix/store/7x73y7qchbb7x5ds96iqbc1ryv7rl10b-vpsadmin-webui-package-contents.drv` | `/nix/store/6155md9br7w60y6dzjri4w5wrwk259ic-vpsadmin-webui-package-contents` | `sha256-d6xi4mKdjkX2JFicDIv5niSzpyI0m/Hnm8GGAIU04kY=` |

Cleaned source: `/nix/store/vcvq4cp02jnfgix8i1pwwdl6vwn4qrv8-source`. Thirteen relevant cleaned-source inputs
matched checkout bytes. Its NAR, full flake lock graph and2080-path derivation
input closure are saved, along with frontend/BFF source and dependency identities.
Manifest/lock/development provenance retain SDK delivery2d251, packed44c651,
actual APIde4/schema7cb28, archive983061/345048bytes and truthful generation
provenance. Runtime peer0.32.0 and separate BFF graph remain unchanged. No private
paths or generated source entered the installed public root; the declared source
and package whitelist checkers passed. See [package evidence](postreview-package-evidence.json)
and [saved NAR/path identities](postreview-package-path-info.json).

**Current residency differs from the successful verification.** A later terminal
check found frontend, BFF, cleaned source and source/package-check outputs absent;
only provenance remains resident. The original successful build and immediate
metadata/NAR inspection remain exact historical evidence. No restore, rebuild or
GC investigation was performed. Future composition/cache/output verification
belongs to a later allocated runtime package. An early report sentence saying all
outputs remained present was corrected immediately in report19f0b637.

## Existing synthetic browser flow

The ordinary repository runner executed only
`e2e/specs/app/vps_incident_summary.spec.ts`, using its unchanged current fixtures:

```sh
nix develop --command env E2E_BASE_URL=http://127.0.0.1:4191 \
  E2E_CHROMIUM_EXECUTABLE_PATH=<existing Nix Chromium headless-shell> \
  PLAYWRIGHT_BROWSERS_PATH=<existing Nix browser root> \
  node scripts/playwright.mjs test e2e/specs/app/vps_incident_summary.spec.ts \
  --project=chromium --project=mobile-chrome --workers=1 --retries=0 \
  --max-failures=1 --reporter=list,json --output=<session artifact directory>
```

The full literal argv, output paths and eleven frozen hashes are in
[browser plan](postreview-browser-plan.json). Native32555 passed0 in138.679s.
Actual browser JSON proves12 expected,0 unexpected/skipped/flaky/global errors,
and exactly one passed attempt per case. Six existing cases ran in each project:
EN/CS owner/admin policy/history/notice flows, combined owner-scoped filters and
old-API absence. No scenario, assertion or fixture changed. Nix-compatible
Chromium149.0.7827.55 was already installed; its executable, resolved store path
and derivations are retained. No browser download or package modernization.

Assertions cover supplied live/saved periods/counts/limits/actions, independent
limit and shared-permission payloads, role controls, zero/reached policies, reports
and policy destinations with owner context, active/retired link targets, three
saved matched sections and separate admin false/null outcomes, and explicit
notice origin independent of trigger/mail state. Links are checked as the existing
spec defines; no extra live authorization or navigation campaign is claimed.
Earlier focused unit evidence retains its stricter matched-error privacy scope.

Browser execution used the ordinary Vite development source bootstrap because
these existing fixtures target that mode. It did not serve the compiled BFF-mode
Nix frontend; no standalone/dev/static/demo equivalence is inferred. A registered
service launched from the exact frozen checkout. Vite runtime env.mjs actually
defines full6b14/dirtyfalse/source=git; its response and parsed proof are saved.
The initial build-info.json probe received the SPA fallback and the direct
buildInfo.ts module probe retained a runtime binding. Those failed probes are
preserved in postreview-readiness-probes.json, and the initial overstatement of
the direct module proof was corrected in report93875d26. No application failure
or browser rerun resulted.

## Implemented captures for root visual acceptance

The unchanged test emitted16 raw PNGs across all eight language/role/viewport
main flows. All are synthetic intercepted data. Root visual acceptance is pending;
Owner2 inspected these four representative images and found no concrete layout
correction. They show clear four-column current/saved tables, distinct limits,
active links and retired history, with a narrow Czech member view.

| View | Raw PNG | Dimensions | SHA256 |
| --- | --- | --- | --- |
| desktop-en-admin-policies | [image](postreview-browser-artifacts/app-vps_incident_summary---12b59-eric-policies-en-admin-true-chromium/generic-policies.png) | 1280×1461 | `d40aab0178b9d92a0c479b6cecf4ab7e4ca42972061907546af8e76a5e19787b` |
| desktop-en-admin-history | [image](postreview-browser-artifacts/app-vps_incident_summary---12b59-eric-policies-en-admin-true-chromium/generic-policy-history.png) | 1280×1433 | `f5a16e31141cfa1e6a19ccffa0b8ca55c8fa3aa5cb1c3dc5bb3e7aacd05a6ae1` |
| mobile-cs-owner-policies | [image](postreview-browser-artifacts/app-vps_incident_summary---f595e-ric-policies-cs-admin-false-mobile-chrome/generic-policies.png) | 393×1577 | `59035078c3b913545b91841456cb327dae2844782e88737cf9951162377b5d06` |
| mobile-cs-owner-history | [image](postreview-browser-artifacts/app-vps_incident_summary---f595e-ric-policies-cs-admin-false-mobile-chrome/generic-policy-history.png) | 393×1804 | `0f5b3f525df287c7756659a8653a9ef6616bed7f97a4feea4d8201da1a3b2513` |

All16 hashes/sizes are in [image manifest](postreview-browser-images.json); the
four-view map is [visual handoff](postreview-visual-handoff.json). Notice-origin
assertions passed, but the existing spec emitted no separate notice PNG. These
are implemented development captures, not canonical KB media, a real API test or
demo/deployment acceptance. No fixture was rerun merely to generate more media.

## Ownership, shutdown and limits

Prior effects were terminal before this package. Session identity and live roster
retained implementer2 Sol/xhigh/workspace_write, full_access. The current installed
utility policy was read: Luna/low/full_access, catalog780db421. Fresh delegation
was not callable; visible monitor-skill active-parent fallback owned each long
command through terminal completion. No competing watcher or heavy build ran.

Public service registration was initially busy and refused before launch. A
subsequent public read admitted the known empty registry. Service
`a162b136-8a52-4eae-ad5e-c9c18ccfb3ba` launched0 (native86333 joined), and only that
owned service was stopped0 (native8084 joined). Independent terminal list has
count0/retired/stopped and loopback4191 returns errno111. Existing demo/runtime
and retired service history were untouched. Preflight25852, build83916 and
browser32555 are joined. No owned handle or uncertain effect remains.

Execution evidence stays in this session packet, as allocated. No source-only
documentation commit was needed; current source prose and prior labels remain
unchanged, avoiding a provenance-only successor. The old94-artifact source review
receipt, b1fb/d26/8ce records and prior media remain literal. All five package
targets bind this same final clean head. Root owns visual acceptance and any
later publication/runtime allocation; Owner2 retains exclusive React source/Git
window and concrete-fix responsibility. Registry SDK publication remains required
before eventual default integration. No merge or session lifecycle action.

[Terminal ownership/residency receipt](postreview-terminal.json).
[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
