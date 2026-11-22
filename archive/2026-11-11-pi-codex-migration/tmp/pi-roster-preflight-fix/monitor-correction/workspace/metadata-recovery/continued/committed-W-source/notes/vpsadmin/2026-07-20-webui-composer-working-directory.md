# WebUI Composer commands need the WebUI working directory

Initiative: `work/2026-07-20-node-evidence-compat-cleanup`

Running `nix develop .#webui -c composer exec ...` from the vpsAdmin repository
root made Composer use its global directory and reported that `phpunit` was not
installed. The WebUI development shell does not change directories.

Run Composer from `webui/`, for example:

```shell
nix develop .#webui -c bash -lc \
  'composer install && composer exec phpunit -- tests/Regression/Test.php'
```

The project dependencies and PHPUnit test then load normally. This was
verified with `NodeEvidencePagesTest` (11 tests, 57 assertions).
