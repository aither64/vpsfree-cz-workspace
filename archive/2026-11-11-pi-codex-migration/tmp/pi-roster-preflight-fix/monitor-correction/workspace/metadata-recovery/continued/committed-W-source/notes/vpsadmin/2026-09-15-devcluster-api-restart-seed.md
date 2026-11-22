# Restore review overrides after the API has started

In the vpsAdmin single/bridge development cluster, `vpsadmin-api.service`
depends on `vpsadmin-devcluster-seed.service`. The seed is a nonpersistent
oneshot, so a later API start runs it again. It can overwrite review-specific
settings and clear ownership of the seed-managed assigned IPs even when those
values were restored immediately before starting API.

Symptom: a post-deployment IP accounting check found the correct usage but one
missing assigned owner per review member. The seed unit journal showed another
successful seed run during API startup. This was seed behavior, not a production
quota adjustment failure.

Order: finish service startup, wait for API readiness, unlock the development
signer, then restore the review overrides under their existing identity checks.
Verify exact public/private IPv4 and IPv6 accounting and VPS state after that;
do not restart the API again between restoration and verification. An immediate
signer command can receive503 until startup finishes.

Verified in `work/2026-09-09-ip-release-mechanism/state.md`: all saved campaign
rows preserved, quotas/PTR matched, both VPSes running. No full cluster reset.
