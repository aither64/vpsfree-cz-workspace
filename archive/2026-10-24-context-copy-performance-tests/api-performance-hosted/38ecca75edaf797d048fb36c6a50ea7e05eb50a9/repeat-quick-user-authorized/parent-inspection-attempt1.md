# Data-inspection correction

The initial parent metadata inspection verified report/header/pair inventory,
source/input/calibration matches and actual compared gate, then required distinct
worker hostnames as fresh-run proof. GitHub reused hostname runnervmtai0g on the
new runner, so that final assertion failed. Exact GitHub runner identities differ:
original1000039711 versus new1000039726, with different CPU descriptions. Hostname
is not a unique runner identity. Corrected the evidence assertion to require the
authoritative distinct hosted runner IDs and retain both host records unchanged.
No benchmark rerun, artifact modification, source/gate change or additional API
request was made for this correction.
