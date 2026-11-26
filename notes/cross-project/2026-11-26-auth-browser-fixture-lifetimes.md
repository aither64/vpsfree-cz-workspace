# Auth browser fixture lifetime findings

Observed in the OAuth appearance session on vpsAdmin `913806a9` and HaveAPI
`439beea8`, with Playwright 1.61.0 and Chromium 154.0.8037.57.
Details and historical failures: [B evidence](../../work/2026-11-26-oauth-dark-theme/vpsadmin-evidence.md)
and [accepted design](../../work/2026-11-26-oauth-dark-theme/design.md).

- The original TestDb owner registered exit cleanup that stops **and prunes**
  its database. An attaching companion did not inherit that lifetime ownership;
  the original provider remained alive throughout. Restarting it was not a
  state-preserving fixture operation.
- Native WebAuthn needed consistent public hostname, RP and canonical allowed
  origin configuration. This fixture used an accepted localhost companion and
  temporary canonical auth_url change, then exact restoration. This did not
  establish the earlier registration failure's cause or justify origin bypasses.
- Playwright routing sees the first URL of a redirected request. Callback-route
  interception alone therefore did not prove the real provider redirect.
  Accepted proof paired the actual provider response with the matching mainframe
  navigation request and committed/loaded callback document.
- Actual CDP add/get omitted only userName, userDisplayName and userHandle from
  this nonresident credential; key, ID, RP, resident and backup flags stayed
  unchanged. Canonical known-user/ID-bound auth and recovery supported absent
  handle. Only those observed omissions were accepted; a returned handle had to
  match. This supplies no resident/discoverable or general normalization claim.
- Saved counter 1 predated accepted authentication. One exact read-only lookup
  established server-accepted baseline 5, not reconstructed authenticator
  history. A later genuine recovery assertion advanced to 9 and passed normal
  verification. Original key evidence stayed unchanged; later checkpoints were
  actual CDP exports, without server-counter writes or invented assertion state.
- Canonical recovery's invalid-TOTP DOM contained visible validation feedback
  and a hidden passkey `.error`. A global strict locator matched both before
  visibility filtering. The intended visible feedback was uniquely scoped;
  theme selection had already passed and was not the failing operation.
- Waiting for DOM while its mainframe POST was paused stalled the owned route.
  Its async rejection escaped the scenario catch/finally. Forwarding owned-route
  failure into one awaited body failure produced safe terminal results on later
  actual failures. Actual private cookie snapshots and key exports preserved
  legitimate state before fallible assertions and at context close; consumed
  links were not reopened, and expired sessions were not refreshed or reused.

Native acceptance combined separate retained attempts, not one successful batch.
Earlier generic navigation/preference errors remain unproven at their exact
operation boundaries; later passing checks do not retroactively identify them.
