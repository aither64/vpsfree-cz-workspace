# Orphaned KB capture process

Related initiative: `work/2026-07-10-kb-czech-fixes`.

## Symptom

A new full screenshot run spent several minutes in fixture preparation while
an older `runner/capture.cjs` process for the same cluster slug was still
present. The older process had no Chromium child and had been waiting since a
checkpoint-only determinism run the previous day.

## Cause and fix

The earlier command lost its browser but left the Node capture process waiting
against the initiative's cluster slug. Before continuing, inspect exact
capture commands and parent/child PIDs with `ps`; terminate only the orphan
belonging to the verified current initiative. Do not kill another initiative's
capture or dev cluster.

## Verification

The orphan had not changed its target PNG during the new run. After terminating
it, one definitive capture process completed all 59 checkpoints and strict
inventory validation passed.
