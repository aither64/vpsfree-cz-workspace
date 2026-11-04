# Final candidate runtime verification

Result: failed before VM startup; no focused check passed. The owned HTTP server was stopped normally and port 18080 was free afterward. No VM was started by this operation.

Source head: `742eb30cb1a8b6766c85e915d26b0400e38244b1`.

Preflight confirmed all four candidate directories and archive SHA256 values matched the export receipt. The runner SHA256 was `c13929304f04033528bba1b5e98bd24bde862a35b2d6d6d9aa234631790c4e06`; focused input SHA256 was `cab2b7ce716bdf5d82553535424c173d11059d356f0d52e17056668253490221`.

The HTTP server started and stopped normally. Capture: `final-candidate-http-742eb30cb.log`.

First focused command attempted:

```sh
/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/final-runner-742eb30cb-v3.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-final-742eb30cb-focused-device-leap-15.6 image-scripts/test@systemd/device-units#opensuse-latest
```

It exited before VM startup because the test selector included the invalid prefix `image-scripts/test@`. Raw runner output:

```text
error:
       … while calling the 'getAttr' builtin
         at /nix/store/dh4npwsl659j3nivaqfknfkg3h70ag9m-test-runner/nix/evaluate-tests.nix:129:5:
          128|   else
          129|     builtins.getAttr testPath testsMeta
             |     ^
          130| else if mode == "testJson" then

       … in the attribute set under consideration

       error: attribute '"image-scripts/test@systemd/device-units"' missing
error: nix-instantiate --eval --strict --json /nix/store/dh4npwsl659j3nivaqfknfkg3h70ag9m-test-runner/nix/evaluate-tests.nix --arg repoRoot /nix/store/m1n49nc1qdf1f3j298zcmjjb5ni43iag-source --argstr system x86_64-linux --argstr mode testsMetaOne --argstr testPath image-scripts/test@systemd/device-units failed (1)
```

Transcript: `final-focused-device-leap-15.6.log`. The remaining eight rows were not started. No retry was made.

One read-only GitHub metadata snapshot is in `final-candidate-gh-742.json`: runs `41714889091` and `41714888844`, both queued at source head `742eb30cb1a8b6766c85e915d26b0400e38244b1`.
