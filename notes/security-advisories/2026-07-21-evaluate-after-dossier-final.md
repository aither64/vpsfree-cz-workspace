# Evaluate after all dossier files are final

## Symptom

`spec/dossiers_spec.rb` reported that a freshly generated
`evaluation.json` had the wrong dossier digest even though `advisory.yml` had
not changed after evaluation.

## Cause

The dossier digest covers `advisory.yml`, `historical-attestations.yml`, and
`analysis.md`. Refreshing the snapshot time and evidence digest in
`analysis.md` after running `evaluate` therefore invalidates the generated
evaluation.

## Fix and verification

Finalize every dossier file, including analysis provenance, before running
`bin/security-advisory evaluate <CVE>`. Regenerate all evaluations that share
the snapshot, then run the complete dossier spec. In this initiative, the five
evaluations were regenerated after the analysis updates and all four dossier
examples passed.

Related initiative: `work/2026-07-20-security-advisory-review/`.
