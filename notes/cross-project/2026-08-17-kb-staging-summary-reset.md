# Changing a staged DokuWiki summary requires a reset

Initiative: `work/2026-08-14-kb-updates`

`bin/kb-release stage` refuses to reuse existing staged page content when the
latest DokuWiki revision has the same content but a different summary. The
command reports `revision summary differs` and asks for a staging reset because
DokuWiki revision summaries cannot be edited in place.

Confirm that the staging owner and pending content belong to the current
initiative with `bin/kb-stage status`. Then run `bin/kb-stage reset --yes` and
stage the replacement manifest again. The reset mirrors production, so restage
every page and language in the intended bundle afterward.

In this initiative, both schema-5 manifests staged and verified successfully
after the reset, including their per-page summaries and exact managed-source
revision.
