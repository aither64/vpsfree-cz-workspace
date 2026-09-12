# Organization CI timing failure

Run 34713657833 on organization 2a3f442 failed in nix flake check. Downloaded and
read the failed step logs before any rerun. Both normal/compatibility packages
were building concurrently on the GitHub runner. Runtime run 34713615190 on the
same UI head e35cf0b passed.

The failing assertion was creation_test.go:131 in
TestCreationNavigationPrecedesSlowValidationAndManifestDiscovery. It returned
HTTP 303 with an empty body, the expected redirect, but exceeded the test's 500 ms
threshold; the reported test duration was 0.88s. The fixture blocks ListModels on
an unreleased channel, so successful acceptance already proves it does not wait
for validation. No creation implementation changed in this UI follow-up. The
logs do not isolate scheduler versus filesystem overhead, so no narrower cause
is claimed.

Separate runtime test commit dc8d6cf replaces elapsed-time benchmarking with a
buffered response channel while validation remains blocked. Five seconds is a
deadlock guard, not a latency contract. Failure now reports whether no response
arrived or its status was wrong. Worker entry uses the same generous guard.
Twenty focused runs passed (0.546s); five race-enabled runs passed (1.430s).
New downstream pins select the fix; the failed run is retained rather than blindly
rerun. Final exact-head CI and package acceptance remain required.
