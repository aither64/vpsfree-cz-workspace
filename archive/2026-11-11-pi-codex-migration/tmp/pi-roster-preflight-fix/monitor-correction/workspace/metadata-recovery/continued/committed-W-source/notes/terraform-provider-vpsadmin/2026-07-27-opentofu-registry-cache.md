# OpenTofu registry versions cache after provider release

## Symptom

After the OpenTofu registry metadata updater and API sync completed
successfully, the provider-specific download endpoint for a new version was
live, but the versions endpoint still returned the preceding release.

## Cause

The observed Cloudflare response for
`/v1/providers/vpsfreecz/vpsadmin/versions` was a cache hit with
`cache-control: max-age=14400`. The generated provider download object had
already been uploaded, while the cached versions object remained stale.

## Verification

- Check the OpenTofu `Bump Provider and Module Versions` run, especially the
  namespace-prefix job.
- Confirm the new version is present in the provider JSON in
  `opentofu/registry`.
- Check the subsequent `Generate and Sync Recent Changes` run.
- Query both:
  - `/v1/providers/NAMESPACE/NAME/versions`
  - `/v1/providers/NAMESPACE/NAME/VERSION/download/OS/ARCH`
- Inspect response cache headers before treating a stale versions list as an
  ingestion failure.

For terraform-provider-vpsadmin `v1.3.0`, the direct Linux AMD64 endpoint
returned HTTP 200 and the correct release checksum while the versions endpoint
still served cached `v1.2.0`.

Related initiative:
`work/2026-07-27-terraform-provider-vpsadmin-issue-11/`.
