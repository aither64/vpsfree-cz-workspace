# Authoritative old-run conclusion reconciliation

Past run41740116653 attempt1, exact tested48f2983e3cf6b5b72a21c254f744ad8e7d62a123,
was superseded by published5235. After its watch exited1, parent made one
bounded authoritative REST run+attemptjobs read (no continuing duplicate poll).
GitHub reports statuscompleted/conclusioncancelled, updated2026-11-04T04:31:01Z.

| Job | Authoritative conclusion |
| --- | --- |
| Build126279219707 | success |
| Native126293359151 | cancelled |
| amd-low-memory-v6 126293359207 | success |
| amd126293359224 | cancelled |
| amd-low-memory-v5 126293359241 | success |
| Intel-representative-v5 126293359266 | success |
| Intel-representative-v6 126293359279 | success |
| amd-fresh126293359286 | cancelled |
| aged-v5 126293359292 | cancelled |
| aged-v6 126293359298 | cancelled |
| Intel126293359412 | failure (independent earlier fragment lookup) |

The watch's X labels/exit1 do not make all those rows failed products. The aged
log stayedpassing through04:26:49Z, thenexplicitoperationcancel04:30:32Z; no aged
assertionfailure inferred. Nativejob was cancelled but has partialpre-cancel
OpenSUSE16.1 example failures in its rawlog. D owns boundedread-only classification
and lineage; do not erase those actualresults or infercompletednativepass/failure
from cancellation alone. No rerun/skip/mergewaiver or unrelatedsourcefix is authorized.

Originalwatch17219 is terminal, no ownedprocessremains. FreshLuna operation
/root/ci_41773470432 owns exactnewrun5235 observation, nottheoldtoolhandle.
