# Final deployment evidence after configuration baseline advance

Exact heads: staging-refresh-heads.json. Runtime 9b50f357 and workspace 399202fa unchanged from independently reviewed and fully verified reservation-refresh-* records; seven checks all passed, including native idle delivery, package/systemd, composed app and exact CI39018599934.

Configuration final range 17be0d34..fbe190dc is independently accepted in staging-refresh-review-report.md by same actual Astra/xhigh/read-only reviewer. It retains one patch-equivalent generated devWorkspace pin and includes upstream's unrelated staging vpsAdminOS input update. Aitherdev uses neither staging channel. Only devWorkspace differs from new base (staging-refresh-pin-proof.json); no new DB migrations/state/protocol/approval contract. Runtime sidecar and manual predecessor compatibility unchanged.

Exact new configuration build passed, receipt staging-refresh-system-build.json; generation 2026-10-17--11-07-18, with only host metadata/activation and standard wrapper derivations, no local kernel compilation. Rebuild was necessary because configuration revision is embedded. Earlier prepared system was safely refused on remote-baseline mismatch and never activated; failure logs retained. Application profile preparation succeeded at unchanged source, snapshot sha256:2efb80938e466ab45bab9e1b916d386b173762ea79212b79b0324548f36fcb71.

Prepare/approve exact current system, refresh original jobs/reservation with system-before-profile dependency. Live candidate acceptance is still required before user-approved master integration. No forced release, foreign edit, archive/delete or direct activation. Evidence files are frozen once snapshot referenced.
