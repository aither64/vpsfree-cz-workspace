# Run browser contracts through the Go fixture

The portal's browser_contract_test.cjs is not a standalone unit-test entry point:
it requires a server URL and the provider module supplied by the Go fixture.
Calling node portal/internal/web/browser_contract_test.cjs alone fails with
"browser contract test requires the server URL" after its pure assertions.

Use the repository Nix shell and run from portal/:
`go test ./internal/web -run TestShippedBrowserClientMatchesSessionAPI -count=1`.
The broader `go test ./internal/web` also runs it and passed during the portal
presentation follow-up. `-run TestBrowser` matches static browser checks but
misses this HTTP contract.

Related initiative: work/2026-09-14-portal-review-fixes.
