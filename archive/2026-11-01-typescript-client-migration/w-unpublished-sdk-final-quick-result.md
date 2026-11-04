exit=2
elapsed_seconds=93

log=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/w-unpublished-sdk-final-quick.log

--- output tail ---

[audit-active-docs] ok (1505 files scanned)

> vpsadmin-webui@1.0.0 audit:overlays
> node scripts/audit-overlay-contracts.mjs

Overlay contract audit OK

> vpsadmin-webui@1.0.0 audit:lookup-primitives
> node scripts/audit-lookup-primitives.mjs

Lookup primitives OK

> vpsadmin-webui@1.0.0 audit:api-barrel-imports
> node scripts/audit-api-barrel-imports.mjs

audit-api-barrel-imports: OK

> vpsadmin-webui@1.0.0 audit:ui-strings:check
> node scripts/audit-ui-strings.mjs --fail --write work/audits/ui_strings.md


> vpsadmin-webui@1.0.0 audit:mutations:check
> node scripts/audit-mutations.mjs --fail-on-warn

# Mutation surface audit report

Generated: 2026-11-01T19:48:14.029Z

Scanned root: `src`

Parser: `typescript`

Found `224` useMutation(...) calls.

✅ No warnings found.


> vpsadmin-webui@1.0.0 typecheck
> tsc --noEmit

src/pages/app/admin/ipAddresses/useProgressiveSuggestedIpPagination.test.tsx(62,62): error TS2345: Argument of type '{ data: { input: { parameters: { network_enabled: {}; }; }; }; envelope: { status: true; response: { input: { parameters: { network_enabled: {}; }; }; }; }; }' is not assignable to parameter of type 'Omit<RequestResult<{ input?: { parameters?: Record<string, unknown> | null | undefined; } | null | undefined; }>, "meta"> & { meta: Record<string, unknown>; }'.
  Property 'httpStatus' is missing in type '{ data: { input: { parameters: { network_enabled: {}; }; }; }; envelope: { status: true; response: { input: { parameters: { network_enabled: {}; }; }; }; }; }' but required in type 'Omit<RequestResult<{ input?: { parameters?: Record<string, unknown> | null | undefined; } | null | undefined; }>, "meta">'.
src/pages/app/admin/ipAddresses/useProgressiveSuggestedIpPagination.test.tsx(72,52): error TS2345: Argument of type '(opts: { limit?: number | undefined; fromId?: number | undefined; includes?: string | undefined; location?: number | undefined; network?: number | undefined; version?: number | undefined; ... 12 more ...; signal?: AbortSignal | undefined; } | undefined) => Promise<...>' is not assignable to parameter of type '(opts?: { limit?: number | undefined; fromId?: number | undefined; includes?: string | undefined; location?: number | undefined; network?: number | undefined; version?: number | undefined; ... 12 more ...; signal?: AbortSignal | undefined; } | undefined) => Promise<...>'.
  Type 'Promise<{ data: IpAddress[]; envelope: { status: boolean; }; }>' is not assignable to type 'Promise<ActionResult<IpAddress[], IpAddress__IndexGlobalOutput>>'.
    Type '{ data: IpAddress[]; envelope: { status: boolean; }; }' is not assignable to type 'ActionResult<IpAddress[], IpAddress__IndexGlobalOutput>'.
      Property 'httpStatus' is missing in type '{ data: IpAddress[]; envelope: { status: boolean; }; }' but required in type 'Omit<RequestResult<IpAddress[]>, "meta">'.
src/pages/app/admin/ipAddresses/useProgressiveSuggestedIpPagination.test.tsx(96,52): error TS2345: Argument of type '(opts: { limit?: number | undefined; fromId?: number | undefined; includes?: string | undefined; location?: number | undefined; network?: number | undefined; version?: number | undefined; ... 12 more ...; signal?: AbortSignal | undefined; } | undefined) => Promise<...>' is not assignable to parameter of type '(opts?: { limit?: number | undefined; fromId?: number | undefined; includes?: string | undefined; location?: number | undefined; network?: number | undefined; version?: number | undefined; ... 12 more ...; signal?: AbortSignal | undefined; } | undefined) => Promise<...>'.
  Type 'Promise<{ data: IpAddress[]; envelope: { status: boolean; }; }>' is not assignable to type 'Promise<ActionResult<IpAddress[], IpAddress__IndexGlobalOutput>>'.
    Type '{ data: IpAddress[]; envelope: { status: boolean; }; }' is not assignable to type 'ActionResult<IpAddress[], IpAddress__IndexGlobalOutput>'.
      Property 'httpStatus' is missing in type '{ data: IpAddress[]; envelope: { status: boolean; }; }' but required in type 'Omit<RequestResult<IpAddress[]>, "meta">'.
src/pages/app/admin/ipAddresses/useProgressiveSuggestedIpPagination.test.tsx(110,68): error TS2322: Type 'Promise<{ data: IpAddress[]; envelope: { status: boolean; }; }>' is not assignable to type 'Promise<ActionResult<IpAddress[], IpAddress__IndexGlobalOutput>>'.
  Type '{ data: IpAddress[]; envelope: { status: boolean; }; }' is not assignable to type 'ActionResult<IpAddress[], IpAddress__IndexGlobalOutput>'.
    Property 'httpStatus' is missing in type '{ data: IpAddress[]; envelope: { status: boolean; }; }' but required in type 'Omit<RequestResult<IpAddress[]>, "meta">'.
src/pages/app/admin/ipAddresses/useProgressiveSuggestedIpPagination.test.tsx(122,68): error TS2322: Type 'Promise<{ data: IpAddress[]; envelope: { status: boolean; }; }>' is not assignable to type 'Promise<ActionResult<IpAddress[], IpAddress__IndexGlobalOutput>>'.
  Type '{ data: IpAddress[]; envelope: { status: boolean; }; }' is not assignable to type 'ActionResult<IpAddress[], IpAddress__IndexGlobalOutput>'.
    Property 'httpStatus' is missing in type '{ data: IpAddress[]; envelope: { status: boolean; }; }' but required in type 'Omit<RequestResult<IpAddress[]>, "meta">'.
src/pages/app/admin/ipAddresses/useProgressiveSuggestedIpPagination.test.tsx(132,68): error TS2322: Type 'Promise<{ data: IpAddress[]; envelope: { status: boolean; }; }>' is not assignable to type 'Promise<ActionResult<IpAddress[], IpAddress__IndexGlobalOutput>>'.
  Type '{ data: IpAddress[]; envelope: { status: boolean; }; }' is not assignable to type 'ActionResult<IpAddress[], IpAddress__IndexGlobalOutput>'.
    Property 'httpStatus' is missing in type '{ data: IpAddress[]; envelope: { status: boolean; }; }' but required in type 'Omit<RequestResult<IpAddress[]>, "meta">'.
