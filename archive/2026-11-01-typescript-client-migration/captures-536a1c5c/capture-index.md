# Existing mobile UI capture evidence

Source head: `536a1c5cbc49bb27a50e26af733e9b605e506f1c`, recorded in each trace's rendered GitHub commit link. Synthetic local fixtures at `http://127.0.0.1:5187`. Only existing inputs from `../browser-536a1c5c-nix1228/core-results/` were used; no browser, test, server or Git command was run for this capture package.

| Image | Actual DOM `html.lang` | Actual CSS viewport | Stored pixels / capture kind |
| --- | --- | --- | --- |
| [vps-first-cs-mobile.png](vps-first-cs-mobile.png) | `cs` | 393×727 | 993×1741 direct dialog-locator PNG crop |
| [vps-first-en-mobile.png](vps-first-en-mobile.png) | `en` | 393×727 | 993×1785 direct dialog-locator PNG crop |
| [helpbox-editor-en-mobile.jpeg](helpbox-editor-en-mobile.jpeg) | `en` | **320×900 explicit override** | 258×726 existing sampled viewport JPEG |

All three selected cases belong to **`mobile-chrome`**, not the desktop `chromium` project. Trace contexts independently report Chromium, Playwright `1.61.0`, Chrome `149.0.7827.55` Android Pixel 5 user agent, `isMobile: true`, `hasTouch: true`, device scale factor `2.75`, and initial viewport `393×727`. The HelpBox scenario overrides that viewport; its actual frame/snapshots are 320×900. Language claims use the main-frame HTML attribute, not browser locale (`en-US`) or test titles. Image pixel dimensions are not CSS viewport dimensions. The direct PNGs contain the dialog only; the JPEG was already downsampled by the trace. No image is a full-page capture.

## Czech VPS-first dialog

- Test: `admin/ip_assignment_vps_first.spec.ts:61 › @pr-smoke @pr-smoke-mobile cs assign icon opens VPS first without an ownership write`; project `mobile-chrome`.
- Input directory: `admin-ip_assignment_vps_fi-00ea4--without-an-ownership-write-mobile-chrome/`; direct original `vps-first-cs.png`.
- `test.trace` screenshot step `pw:api@97`, `240782.170–241263.768 ms`, selector `admin.ip.route.dialog`, spec line 76.
- `0-trace.trace` explicit root in `before@call@130` at `240745.017 ms`: `HTML lang="cs"`, viewport 393×727. Screenshot-associated `before@call@132` at `240790.925 ms` retains viewport 393×727.
- Exact revision link appears in `input@call@16` at `239317.247 ms`.
- Image SHA-256: `bd15ea3bdb72a1ad586353eb2416d0c2826586bbc63aca262499034dbd52bd27`.
- Original `trace.zip` SHA-256: `f27853ca6040bce3964441d958c5aac503e450957cb36cab983a896ec4f0597e`.

## English VPS-first dialog

- Test: `admin/ip_assignment_vps_first.spec.ts:61 › @pr-smoke @pr-smoke-mobile en assign icon opens VPS first without an ownership write`; project `mobile-chrome`.
- Input directory: `admin-ip_assignment_vps_fi-a6e3d--without-an-ownership-write-mobile-chrome/`; direct original `vps-first-en.png`.
- `test.trace` screenshot step `pw:api@88`, `253902.659–254293.864 ms`, selector `admin.ip.route.dialog`, spec line 76.
- `0-trace.trace` explicit root in `before@call@371` at `253852.500 ms`: `HTML lang="en"`, viewport 393×727. Screenshot-associated `before@call@373` at `253909.323 ms` retains viewport 393×727.
- Exact revision link appears in `input@call@257` at `252477.774 ms`.
- Image SHA-256: `01c004e39237ffc011789f39ab7df432aebb9fac94982beaef88c1343715131b`.
- Original `trace.zip` SHA-256: `b8f38af1314dae0f3a8f81ea677af2adc65bfafd1d8f5318c99953644d370a28`.

## English HelpBox editor

- Test: `admin/help_boxes_responsive_actions.spec.ts:6 › @pr-smoke @pr-smoke-mobile @smoke-mobile admin help-box actions stay reachable on mobile`; project `mobile-chrome`.
- Input directory: `admin-help_boxes_responsiv-54f6b-ns-stay-reachable-on-mobile-mobile-chrome/`; exact ZIP resource `resources/page@d6dab73d9743a439cd11b93204bbc43b-1793575347461.jpeg`.
- `0-trace.trace` screencast timestamp `231292.277 ms`, frame-swap wall time `1793575347450.1008 ms` since Unix epoch. Resource filename is the trace's `sha1` field identifier, not a content-hash claim.
- `call@8` at `226647.667 ms` explicitly sets viewport 320×900. Bracketing snapshots `before@call@138` at `231280.123 ms` and `after@call@138` at `231299.674 ms` both record `HTML lang="en"` and viewport 320×900. Editor is visible; Cancel begins later at `231304.223 ms`.
- Exact revision link appears in `after@call@16` at `229909.754 ms`.
- Image SHA-256: `6dffcdb295c78471a6831112dc795c8c8fa7beeb2278c6bdc0848b5882f43bd6`.
- Original `trace.zip` SHA-256: `d1de1273205ed34aae205aee384343f38fe504829b0fd7170e283d57c987adf7`.

These are existing lead-reported passed scenes. The selected images were visually inspected after byte-for-byte copy/extraction, without resizing or annotations. Original archives and direct images remain unchanged. The VPS pair shows the existing Czech/English mobile dialog scene; the HelpBox image shows the existing English editor with its language-clear explanation and footer controls. This package adds no scene execution or coverage, and makes no claim of complete mobile-suite success, Czech HelpBox coverage, other changed controls, another browser engine, physical-device behavior, live API compatibility, or deployment. The campaign's later mobile profile failure remains separate.
