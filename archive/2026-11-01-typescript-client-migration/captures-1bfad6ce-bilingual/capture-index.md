# Existing bilingual request and template-editor captures

Source head: `1bfad6ce1846aef2d21bb6a58d4529a962e7aa97`. Every selected trace renders that full revision in its source commit link. Inputs are only existing `../browser-1bfad6ce-nix1228-observed/capture-results/` and `../browser-1bfad6ce-nix1228-observed/captures/` artifacts. These scenes use synthetic local fixtures at `http://127.0.0.1:5187`.

| Image | Actual project / DOM `html.lang` | Actual CSS viewport | Stored pixels / kind |
| --- | --- | --- | --- |
| [request-risk-cs-desktop.png](request-risk-cs-desktop.png) | `chromium` / `cs` | 1024×900 | 1024×1986 / direct full-page PNG |
| [request-risk-en-desktop.png](request-risk-en-desktop.png) | `chromium` / `en` | 1280×720 | 1280×1950 / direct full-page PNG |
| [request-risk-cs-mobile.png](request-risk-cs-mobile.png) | `mobile-chrome` / `cs` | 393×727 | 1081×11336 / direct full-page PNG |
| [request-risk-en-mobile.png](request-risk-en-mobile.png) | `mobile-chrome` / `en` | 393×727 | 1081×11446 / direct full-page PNG |
| [user-data-editor-cs-desktop.png](user-data-editor-cs-desktop.png) | `chromium` / `cs` | 1280×720 | 1280×720 / direct full-viewport PNG, scale:css |
| [user-data-editor-en-mobile.jpeg](user-data-editor-en-mobile.jpeg) | `mobile-chrome` / `en` | 393×727 | 392×725 / existing sampled viewport JPEG |

The four request images are original **full-page** screenshots after the risk details were expanded, not crops or single viewport screenshots. They show applicant details, technical metadata, risk checks and decision controls. Czech desktop explicitly used 1024×900; English desktop retained 1280×720. Both mobile request captures used 393×727. Their tall stored images include the scrollable page and use device scale factor 2.75; stored pixel sizes are not CSS viewport dimensions.

The Czech user-data image is the existing CSS-scale full-viewport PNG of the centered editor with populated label/content. The English mobile image is an actual sampled trace frame with label entered and the content area still empty at that recorded instant; it is not a reconstructed equivalent of the Czech PNG. It was selected before the later short-height viewport override. No direct English editor PNG was created by this package.

Contexts report Playwright 1.61.0, Chromium/Chrome 149.0.7827.55. Desktop project `chromium` uses desktop user agent, isMobile:false, hasTouch:false, device scale factor 1. Mobile project `mobile-chrome` uses Android Pixel 5 user agent, isMobile:true, hasTouch:true, device scale factor 2.75. Actual viewport and language claims come from the scene's main-frame snapshots and frame metadata, rather than project defaults, browser locale or test title. Browser locale is en-US in all contexts.

## request-risk-cs-desktop.png
- Test: `admin/requests_operations_smoke.spec.ts:210 › @workflow-matrix @pr-smoke @pr-smoke-mobile admin requests: address copy and risk emphasis work across breakpoints in cs`; project `chromium`.
- Input directory under `capture-results/`: `admin-requests_operations_-521d8-rk-across-breakpoints-in-cs-chromium/`. Direct original `request-risk-below-details.png` under input directory.
- `test.trace` screenshot `pw:api@108`, `21976.075–22350.942 ms`, spec line 286; `fullPage:true`.
- Bracketing explicit main-frame roots: `after@call@377` at `21972.619 ms` and `after@call@381` at `22391.467 ms`; both `HTML lang="cs"`, CSS viewport 1024×900.
- Full source revision rendered in DOM snapshot `after@call@229` at `20517.883 ms`.
- Image SHA-256: `0c32336da154c17b177368a0fb3c1a46ce689ba70d4347c704b4dbf478551693`.
- Original `trace.zip` SHA-256: `89a770cddb9bef7b8267a0032efc90f4333551d63d8e2da1061f6995059a45ed`.

## request-risk-en-desktop.png
- Test: `admin/requests_operations_smoke.spec.ts:210 › @workflow-matrix @pr-smoke @pr-smoke-mobile admin requests: address copy and risk emphasis work across breakpoints in en`; project `chromium`.
- Input directory under `capture-results/`: `admin-requests_operations_-e63a5-rk-across-breakpoints-in-en-chromium/`. Direct original `request-risk-below-details.png` under input directory.
- `test.trace` screenshot `pw:api@116`, `14546.144–14951.193 ms`, spec line 286; `fullPage:true`.
- Bracketing explicit main-frame roots: `after@call@170` at `14541.608 ms` and `after@call@174` at `14983.580 ms`; both `HTML lang="en"`, CSS viewport 1280×720.
- Full source revision rendered in DOM snapshot `after@call@22` at `13059.356 ms`.
- Image SHA-256: `7f2ceb2723a0f191c04b6c5ce5b2a03c1fea00510f0344df9a9eb5c13c899a7b`.
- Original `trace.zip` SHA-256: `4fdf1315a98ebde7395e2ecc0d1078ec2b9581e38f1d49f3b6ce0f03c740e2de`.

## request-risk-cs-mobile.png
- Test: `admin/requests_operations_smoke.spec.ts:210 › @workflow-matrix @pr-smoke @pr-smoke-mobile admin requests: address copy and risk emphasis work across breakpoints in cs`; project `mobile-chrome`.
- Input directory under `capture-results/`: `admin-requests_operations_-521d8-rk-across-breakpoints-in-cs-mobile-chrome/`. Direct original `request-risk-below-details.png` under input directory.
- `test.trace` screenshot `pw:api@99`, `37032.682–37976.837 ms`, spec line 286; `fullPage:true`.
- Bracketing explicit main-frame roots: `after@call@343` at `37027.720 ms` and `after@call@347` at `38009.991 ms`; both `HTML lang="cs"`, CSS viewport 393×727.
- Full source revision rendered in DOM snapshot `after@call@211` at `35156.326 ms`.
- Image SHA-256: `e53a86e2b4f147d27cb2e7fa1e8723c973e04cad0fdf0cb98c10f06051a627b3`.
- Original `trace.zip` SHA-256: `2fc7bd062578c9ca95d5c2973335ba5e2b8e68eb372db21ccf03aba478f6245a`.

## request-risk-en-mobile.png
- Test: `admin/requests_operations_smoke.spec.ts:210 › @workflow-matrix @pr-smoke @pr-smoke-mobile admin requests: address copy and risk emphasis work across breakpoints in en`; project `mobile-chrome`.
- Input directory under `capture-results/`: `admin-requests_operations_-e63a5-rk-across-breakpoints-in-en-mobile-chrome/`. Direct original `request-risk-below-details.png` under input directory.
- `test.trace` screenshot `pw:api@108`, `28805.243–29618.941 ms`, spec line 286; `fullPage:true`.
- Bracketing explicit main-frame roots: `after@call@154` at `28801.351 ms` and `after@call@158` at `29651.263 ms`; both `HTML lang="en"`, CSS viewport 393×727.
- Full source revision rendered in DOM snapshot `after@call@22` at `26752.493 ms`.
- Image SHA-256: `47ed94c980d37f04e45de9fde3a02da52070ae79c9d46cca6c2217fc2d565312`.
- Original `trace.zip` SHA-256: `08d10c933a14e3cdc7b06aeb66d2008680d7c34a78079623259c1262ec187bd3`.

## user-data-editor-cs-desktop.png
- Test: `app/profile_user_data.spec.ts:298 › @pr-smoke @pr-smoke-mobile centered template editor and supported filters remain usable (cs)`; project `chromium`.
- Input directory under `capture-results/`: `app-profile_user_data--pr--34cc8-d-filters-remain-usable-cs--chromium/`. Direct original `captures/chromium-user-data.png` under run root.
- `test.trace` screenshot `pw:api@84`, `13573.887–13772.239 ms`, spec line 311; `scale:css`; no full-page option.
- Bracketing explicit main-frame roots: `after@call@92` at `13568.214 ms` and `before@call@94` at `13579.773 ms`; both `HTML lang="cs"`, CSS viewport 1280×720.
- Full source revision rendered in DOM snapshot `input@call@16` at `13048.226 ms`.
- Image SHA-256: `fc310cb9c880b1b21a9c14c048726988e5984933e59a588998a2f5f552061d84`.
- Original `trace.zip` SHA-256: `b69f51f8df6b7a19bf2dc0d0e72a9b94e14ab07e257a40a16fc505e58476106f`.

## user-data-editor-en-mobile.jpeg
- Test: `app/profile_user_data.spec.ts:298 › @pr-smoke @pr-smoke-mobile centered template editor and supported filters remain usable (en)`; project `mobile-chrome`.
- Input directory under `capture-results/`: `app-profile_user_data--pr--f0548-d-filters-remain-usable-en--mobile-chrome/`. ZIP resource `resources/page@8bf594d0519387eec7be3832e78a1465-1793576930102.jpeg`.
- Screencast timestamp `35370.738 ms`, frame-swap wall time `1793576930089.335 ms` since Unix epoch; resource is the exact filename in the trace `sha1` field (not a content-digest claim).
- Bracketing explicit main-frame roots: `input@call@225` at `35339.756 ms` and `after@call@225` at `35374.054 ms`; both `HTML lang="en"`, CSS viewport 393×727.
- Full source revision rendered in DOM snapshot `input@call@151` at `34963.575 ms`.
- Image SHA-256: `f36893c85f38c0e63c79ab3ba9dba2c4cd30aa9818e8232476f0644fcf32ff2a`.
- Original `trace.zip` SHA-256: `ca26ccea75a1760e4da3883f3d45a895ec4085593e2698abd5bfc4232ab2a7f2`.

## Scope and preservation

All six selected images were visually inspected and copied/extracted byte-for-byte. No resizing, annotation, mockup, browser replay or persistent extractor was used. Original image bytes and ZIP hashes were rechecked unchanged. Only this new capture directory/index was written; source, Git, tests, dependencies, old records and earlier captures were untouched.

These are representative existing implemented scenes from the lead-reported passing B8 run. They add no new execution or scene coverage, and do not prove other controls, bilingual HelpBox behavior, date/reset/filter completeness, another engine or physical device, real API compatibility, deployment, or all product states. The user-data images intentionally represent only Czech desktop and English mobile. Existing b611 desktop and 536 mobile evidence remains separate and retained.
