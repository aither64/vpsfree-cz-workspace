# Ruby native extensions and commit-hook environments

In the container-image pipeline session, ambient Ruby and the test-runner
development shell did not provide a usable combination of RSpec and libosctl's
native extension. An extension built for a different packaged Ruby failed to
load. Reuse the matching Nix wrapper's Ruby/gem/native closure, with current
repository libraries first, rather than rebuilding extensions or changing
project dependencies to repair a local check environment. Exact successful
commands and closure paths are in the session's p3-implementation.md.

For hooks, inspect the repository's actual Overcommit configuration. This
vpsadminos checkout had no gemfile directive; wrapping git commit in the root
bundle unnecessarily selected incompatible RuboCop constraints. The successful
prepared invocation was nix develop .#osctl-repo-server --command git commit -F
with the message-file argument. Required hooks ran normally.

An explicit GEM_PATH can also hide Ruby's default gems, including rexml, even
when Overcommit itself is installed. Preserve normal default gem lookup for
the hook process. Keep the separate native-test environment scoped to its test
command. No hook bypass, dependency edit or broad reinstall was needed.

Evidence: work/2026-11-04-container-image-build-pipeline/{implementation-core,
implementation-http-site,p3-implementation}.md and their linked logs.
