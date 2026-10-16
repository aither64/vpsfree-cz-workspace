The first host-overlay binding evaluation passed0 but exact comparison failed1. Only toplevel/squashfs differ; all twelve scripts exactly match current quick inputs. Derivation traversal reaches one source coercion: original gem src i838…-hzbl…-source versus xsfw…-i838…-hzbl…-source. Importing overlays from the already-coerced gem src copied it once more. The actual original flake root hzbl…-source still exists. A tiny derivation-only probe proves that this root coerces to EXACT original i838 source. Correct only the immutable root constant; keep this failed proof and all output. This is the same public-source binding, without any output/path normalization or product change.

The actual flake root and copied gem source both hash to
sha256-VW6GdTjWjngK0UBrP74Uk+aWAKupbFlqyO0eh2TlBrY=.
The runner package is /nix/store/z0mm53z5qj8q20kw603jkp29bmg147bv-test-runner,
derivation3317pnrlw8kg8q26mfkarjj6lb05dq8k. Old-to-current test-runner,
osvm, libosctl, wrapper, flake and lock diffs are empty; runner-inputs.json
records this separately from host config equality.
