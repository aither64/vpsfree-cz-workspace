# Repository browser fixture needs the conversation sync module

`test/repository_browser.cjs` can time out waiting for the first repository
commit because its HTTP fixture serves conversation.js and uploads.js but omits
sync.js, which conversation.js imports. This is a fixture-server failure before
the repository component mounts.

For the portal-reliability verification, a temporary harness copy served
`conversation/assets/sync.js` at `/sync.js`; all 23 browser checks then passed.
Use the browser pageerror/network diagnostics when an otherwise unchanged
component fails to mount. A future fixture maintenance change should serve the
complete conversation module import set.

Related initiative: work/2026-09-13-portal-reliability/.
