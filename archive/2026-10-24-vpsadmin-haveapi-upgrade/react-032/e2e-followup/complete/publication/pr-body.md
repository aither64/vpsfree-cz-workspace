Align four browser fixtures with the existing HaveAPI transport: require `{ vps: {} }` for member deletion, compare decoded session filters, and capture the page URL immediately before XHR send. The ordering check continues to require removal of an invalid session filter before request dispatch. Both profile specs now participate in strict E2E type checking.

Validation: `npm run ci:quick` passed, independent review found no issues, and 20 focused Chromium/mobile Chrome tests passed with retries disabled. These tests use mocked API responses.

Original failures: [broad smoke](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41291251937) and [PR smoke](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41291251986).
