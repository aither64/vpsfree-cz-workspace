# API exception from newadmin

## Goal and scope

Find the root cause of the attached API exception in relation to
vpsadmin-webui. This is an investigation; application changes, deployments and
integration are outside the current request. Keep the raw email outside Git
and record only sanitized evidence.

## Affected repositories

- `vpsadmin`: deployed API revision
  `a65a4dfeb92a59df4a80a737a20bcbf8558793ff`, OAuth authentication and SSO
  session/token lifetime management.
- `vpsadmin-webui`: separate newadmin application, canonical bare clone
  `repos/vpsadmin-webui.git`; inspect its default branch's authentication flow.
- `haveapi`: framework reference only if needed to resolve request handling.

## Approach and responsibilities

1. Lead extracts sanitized exception, source location and request context.
2. Retained `architect0` independently traces API token cleanup and records
   root-cause evidence, proposed correction and verification brief in `design.md`.
3. Lead traces the WebUI client behavior and reconciles the evidence with the
   exact deployed API source. Use canonical bare refs; do not use other sessions.
4. Document the proven failure, plausible triggers, remaining uncertainty and
   recommended correction in session records. No application implementation is
   assigned for this investigation.

## Compatibility and deployment

Current work makes no persisted-state, database, API, protocol or deployment
changes. Any proposed correction must preserve OAuth access/refresh-token
semantics and ensure expired or revoked SSO credentials cannot be revived.
Record whether independent SSO and OAuth lifetimes permit a valid access token
to outlive an SSO token. Do not infer production data or a specific user's
actions from the exception alone.

## Documentation and verification

Readers are the user and a future fix implementer. Investigation evidence and
temporary verification belong in this session; an implemented behavior contract
would belong in vpsadmin documentation. Review relevant subsystem docs, follow
the source and its history, and use a bounded isolated probe only if needed.
No integration builds or production mutations are required. Separate source
proof from unverified production-state hypotheses.
