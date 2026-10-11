# Keep Codex mode stable during portal refreshes

Implement the approved plan: retain the current conversation's confirmed mode
and usable explicit mode buttons while background transcript metadata is pending.
Use codex-web's existing refresh notice policy for initial loading and failures.
Fresh server metadata remains required for mode-dependent plan actions.

Affected repositories: dev-workspace (browser behavior, contracts, portal guide),
workspace (nested runtime pin), vpsfree-cz-configuration (matching dev-workspace
channel pin and aitherdev deployment). No codex-web changes are planned.

Keep confirmations scoped to thread identity. Older reads must not overwrite a
successful mode save. Initial loading uses 750 ms; failures use 30 continuous
visible seconds, restarting the grace after hidden-tab return or page restoration.
The user selected keeping explicit mode buttons usable during pending metadata.

No HTTP/protocol, session, persisted-state or schema changes are required. Old
browser assets remain compatible and acquire the fix on reload. Preserve native
Codex launch identity and use a compatible live user-profile switch; never stop
other sessions to deploy. Package recovery is forward-only through a corrected
newer package. Keep branches published and unmerged without explicit integration
direction; deployment is authorized by the accepted plan and implementation request.

Verify first pending metadata, confirmed/pending/recovered modes, actual changes,
visibility/restoration grace, unavailable metadata, explicit mode saves and stale
responses, thread replacement, and plan-action gating. Run quick Nix-environment
checks before committed whole-branch independent review, then packaged/browser
checks and deployment checks through fresh verification watchers.

Publish the runtime revision, select it through the workspace's nested runtime
override and configuration's existing dev-workspace channel, verify the composed
deployment contract, deploy the matching aitherdev host configuration, and switch
the workspace application from its user profile. Verify live assets and native
continuity. The portal guide owns lasting behavior; session artifacts own exact
verification/review and rollout evidence for developers and operators.
