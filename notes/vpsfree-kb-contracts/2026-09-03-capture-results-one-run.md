# Register each screenshot capture before starting the next one

## Symptom

After capturing one scenario in Czech and then English, `bin/validate --update`
accepted the English artifacts but strict validation rejected changed Czech
PNGs. Both capture commands had reported complete checkpoint sets.

## Cause

Each `bin/capture` invocation replaces `tmp/capture-results.json`; it does not
append to the prior language's results. The workflow example that captures both
languages before one update therefore loses the first result whenever its PNGs
actually change.

## Workaround

Run `bin/validate --update` immediately after each language or checkpoint
capture. If the first result has already been replaced, recapture that language
and register it before any subsequent capture. Always finish with strict
`bin/validate` and `bin/check`.

## Verification

The related initiative registered the English result, recaptured and registered
the Czech result, then passed strict validation and the full contract check.

Related initiative: `work/2026-09-03-webui-vps-ipv6/`.
