# Exact-head hosted verification

All results here bind edb90d2fe2190d88d8b9d2d21bd0def79eedc898.
Source/tree and complete history are in ../effective-mounts-review/i1-disposition.md.

- Images38735726560: SUCCESS, all six actual image cases. Original completed
  job/status/full workflow log/artifact inventory are in
  ../effective-mounts-ci-observation/38735726560/.
- nixos25.11:1156.55s; nixos25.11-impermanence:1101.61s;
  nixos26.05:1121.48s; nixos26.05-impermanence:1096.85s;
  nixosunstable:1122.73s; nixosunstable-impermanence:1112.72s.
- The nominal25.11 image uses the shared stable builder; this does not establish
  historical25.11 guest software. Actual25.11 adoption is a separate local row.
- RSpec38735727114:SUCCESS. RuboCop38735726534:SUCCESS.
- CoreCI38735726547 build/cache job116424410403:SUCCESS. Exact job JSON verifies
  head and all step conclusions. Normal compatibility/template evaluation,
  native persistence flake check, both disk-reuse checks, host closure/cache
  build all pass. Full native/livepatch jobs remain queued/running; no
  whole-workflow green claim.

The native persistence step ran12:40:33Z–12:48:35Z and built derivation
/nix/store/6218pz068gff57gp72fjhw2b0ylh5msd-nixos-container-persistence.drv.
Raw job log/JSON are retained here. Initial raw-log request refused terminal
escapes; the corrected request allowed them only into a file, with no test retry.

Prior20bCI38645848469 was cancelled after same-branch/head verification and final
publication. Its original failures and completed AMD/Intel results remain in
../final-core-ci-observation/38645848469/ and prior-20b-ci-failures/diagnosis.md.
No foreign or current-head run was cancelled. This evidence does not authorize
integration, production deployment/KB publication or session closure.
