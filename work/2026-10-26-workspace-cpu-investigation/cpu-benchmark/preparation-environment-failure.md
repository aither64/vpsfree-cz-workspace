# First preparation failure

No measurement ran. Exported source has no .git; implicit Nix discovery found
parent /tmp and attemptedgit+file:///tmp. build-baseline.log retains error.
Use explicit path:/tmp/... for Nix development shells. Existing exports and
source-identities hashes retained;resume compiles/validates those exact sources.
Firstwatcher reported immediatefailure because nonexistenceguards rejected
alreadycreatedexports;its trailingdotcomment was notcausal. No retries accepted
asvalidation,no productsourcechanges. Freshoperation uses correctedexplicitpath.
