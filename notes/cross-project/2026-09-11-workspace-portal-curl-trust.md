# Workspace portal curl trust during profile validation

Related initiative: `work/2026-09-11-devcluster-packaging-investigation/`.

The existing HTTPS workspace portal certificate is not trusted by ambient curl
or an explicit `/etc/ssl/certs/ca-certificates.crt` bundle on aitherdev; both
return curl error60 before a package switch. A read-only HTTP reachability probe
with `curl --insecure --location --output /dev/null --write-out '%{http_code}'`
works for this internal portal. This verifies application reachability only;
it does not validate the TLS trust chain. Do not treat this pre-existing trust
setup as a candidate-profile regression or use the probe to send credentials.
