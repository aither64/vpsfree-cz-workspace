# Treat API output whitelists as consumer contracts

## Symptom

A security hardening change removed `Location#has_ipv6` from non-admin API
responses because it was absent from an older output whitelist. The direct
Location endpoint still appeared internally consistent, but the WebUI consumes
the field through a nested `VPS -> Node -> Location` include and silently hid
IPv6 controls when the property was absent.

## Cause

The whitelist was treated as a sensitivity classification without inventorying
downstream consumers or classifying each omitted field. An API spec then
asserted that the capability was absent, cementing the accidental behavior.

## Workflow

Before reducing an output whitelist, search direct and nested consumers and
classify every removed field independently. Cover both the resource endpoint
and the exact include path used by important clients. For capability booleans,
also test both values at the UI boundary so a missing property cannot be
mistaken for a legitimate `false` value.

## Verification

The related fix covers authenticated and anonymous direct Location responses,
the WebUI's nested VPS include, and IPv6-enabled and IPv6-disabled browser
fixtures while keeping the unrelated Location domain restricted.

Related initiative: `work/2026-09-03-webui-vps-ipv6/`.
