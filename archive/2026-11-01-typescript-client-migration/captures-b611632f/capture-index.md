# Implemented UI captures from existing Browser A artifacts

Source head: `b611632f47d0eec4ad87bbb1566c7cb2a80dbefa` (lead-reported tested head; visible frame footers show `b611632f47d0`). Synthetic local fixtures at `http://127.0.0.1:5187`; these are implemented UI images, not deployed API or production evidence.

All inputs below are beneath `../browser-b611632f-nix1228/core-results/`. Each selected test used project `chromium`, Playwright `1.61.0`, and a context reporting Chrome `149.0.7827.55`, device scale factor `1`, `isMobile: false`, `hasTouch: false`. Actual main-frame DOM snapshots and screencast metadata establish **1280×720 CSS-pixel viewports** for these scenes. Test titles/tags containing “mobile” do not establish mobile viewport or mobile-project coverage. Browser locale `en-US` is not used as evidence of document language.

| Capture | Scene / actual `html.lang` | Viewport | Stored image |
| --- | --- | --- | --- |
| [vps-first-cs.png](vps-first-cs.png) | Czech VPS-first dialog / `cs` | 1280×720 | 576×588 direct dialog-locator PNG crop |
| [vps-first-en.png](vps-first-en.png) | English VPS-first dialog / `en` | 1280×720 | 576×588 direct dialog-locator PNG crop |
| [helpbox-editor-en.jpeg](helpbox-editor-en.jpeg) | English HelpBox editor, including language-clear explanation / `en` | 1280×720 | 800×450 existing sampled viewport JPEG |
| [advisory-node-actions-en.jpeg](advisory-node-actions-en.jpeg) | English advisory Nodes tab, visible Edit / Remove status actions / `en` | 1280×720 | 800×450 existing sampled viewport JPEG |

The images were copied/extracted byte-for-byte; no resizing, annotation, regeneration or browser replay was performed. The two JPEGs were already sampled at 800×450 by the original trace. None is a full-page capture. Original artifacts remain unchanged.

## Czech VPS-first dialog

- Test: `admin/ip_assignment_vps_first.spec.ts:61 › @pr-smoke @pr-smoke-mobile cs assign icon opens VPS first without an ownership write`; project `chromium`.
- Original directory: `admin-ip_assignment_vps_fi-00ea4--without-an-ownership-write-chromium/`.
- Direct source: `vps-first-cs.png`. Image SHA-256: `fd45d3f01a9716dc23dfcf0b5ffa90b8328fdd2fb10bb6bef1fa9a4f8e98fdbe`.
- `test.trace`: screenshot step `pw:api@88`, `21840.768–22143.301 ms`, selector `admin.ip.route.dialog`, originating at spec line 76.
- DOM evidence in `0-trace.trace`: `before@call@245` at `21808.256 ms` explicitly records root `HTML lang="cs"` and viewport `1280×720`; screenshot-associated `before@call@247` at `21849.756 ms` records the same viewport.
- Original `trace.zip` SHA-256: `0370793eedc09dacc60791195cd112044ed6bba3a836282fc0f9c184bb917b8a`.

## English VPS-first dialog

- Test: `admin/ip_assignment_vps_first.spec.ts:61 › @pr-smoke @pr-smoke-mobile en assign icon opens VPS first without an ownership write`; project `chromium`.
- Original directory: `admin-ip_assignment_vps_fi-a6e3d--without-an-ownership-write-chromium/`.
- Direct source: `vps-first-en.png`. Image SHA-256: `91020626ad664fca6949f5ab365a5d55638b5336550a1862cf90cce151ad42b4`.
- `test.trace`: screenshot step `pw:api@88`, `34586.758–34809.562 ms`, selector `admin.ip.route.dialog`, originating at spec line 76.
- DOM evidence in `0-trace.trace`: `before@call@486` at `34556.540 ms` explicitly records root `HTML lang="en"` and viewport `1280×720`; screenshot-associated `before@call@488` at `34594.213 ms` records the same viewport.
- Original `trace.zip` SHA-256: `6a201d89dafaf0dd21d3917b9c3c5f6dc5c362053b1008c7fa7885c3edb5c667`.

## English HelpBox editor

- Test: `admin/help_boxes_responsive_actions.spec.ts:6 › @pr-smoke @pr-smoke-mobile @smoke-mobile admin help-box actions stay reachable on mobile`; project `chromium`.
- Original directory: `admin-help_boxes_responsiv-54f6b-ns-stay-reachable-on-mobile-chromium/`.
- Exact ZIP resource: `resources/page@a8cc7c1e9c2682d7be9d605089dec5f1-1793570041308.jpeg`.
- `0-trace.trace` screencast timestamp: `13905.373 ms`; frame-swap wall time: `1793570041292.6409 ms` since Unix epoch. Resource identifier is the trace's `sha1` field value (a filename, not a content-digest claim).
- Bracketing explicit DOM roots: `after@call@100` at `13889.728 ms` and `before@call@102` at `13906.412 ms`; both `HTML lang="en"`, viewport `1280×720`. The editor visibility expectation completes before the selected frame; Cancel starts at `13924.909 ms`.
- Image SHA-256: `365f56e202d16d80b093ca95d7d8e00dedd063eec4c02b121f37fcdc175a2ca6`.
- Original `trace.zip` SHA-256: `12414e3e95b792b35b0a92db778d2105b39716ac59d552bf0ec93f292ae13a07`.

## English advisory node actions

- Test: `admin/security_advisory_nodes_mobile_actions.spec.ts:28 › @pr-smoke @pr-smoke-mobile security advisory node actions stay directly usable on mobile`; project `chromium`.
- Original directory: `admin-security_advisory_no-a0ccc-y-directly-usable-on-mobile-chromium/`.
- Exact ZIP resource: `resources/page@e9c0b1862fe64e10926aa159fea51d17-1793570076057.jpeg`.
- `0-trace.trace` screencast timestamp: `48654.341 ms`; frame-swap wall time: `1793570076038.656 ms` since Unix epoch. Resource identifier is the trace's `sha1` field value (a filename, not a content-digest claim).
- Bracketing explicit DOM roots: `after@call@641` at `48637.416 ms` and `before@call@719` at `48661.468 ms`; both `HTML lang="en"`, viewport `1280×720`. This frame shows the node row and actions before the later editor opens.
- Image SHA-256: `a64cca8e85dd4667437e0086563804bdf6562fced8fd170eff5c42e93be867de`.
- Original `trace.zip` SHA-256: `f4cc0c59a38c5d4c5f42decfa0c92b7ba85a122bb0ca2ccc9fac5db73a98a773`.

## Coverage limits

These four successful-scene captures are representative evidence only. They do not establish full Czech/English coverage of changed controls, Czech HelpBox/advisory coverage, narrow viewport or mobile-chrome coverage, full-page layout coverage, Browser B completion, or real API compatibility. The broader Browser A attempt stopped at an unrelated standalone-home failure after 17 passes; no new execution was performed for this capture package. Selection and visual inspection used only the existing allowed artifacts. No source, Git, dependencies, old browser plan or session metadata changed.
