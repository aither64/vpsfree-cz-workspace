#!/usr/bin/env bash
# Parent must clear final committed review before selecting any mode.
set -euo pipefail
set -o noclobber
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
mode=${1:?Missing legacy mode}
head=${2:?Missing reviewed V head}
[[ $# == 2 && $head =~ ^[0-9a-f]{40}$ ]]
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter ]]
[[ ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
case "$mode" in
  legacy) selector=webui#admin-cluster ;;
  *) exit 2 ;;
esac
cd "$v_root"
[[ $(git rev-parse HEAD) == "$head" && -z $(git status --porcelain) ]]
state_root=/tmp/vna-${head:0:12}-$mode
[[ ! -e "$state_root" ]]
for artifact in log exit inventory.log inventory.exit capacity.json state.path; do
  [[ ! -e "$tracking/legacy-network-client-vm-$mode.$artifact" ]]
done
# Keep default runner reserves and VM sizes. Refuse insufficient real capacity
# rather than allowing the runner's oversize-alone warning to start the test.
python3 - "$tracking/legacy-network-client-vm-$mode.capacity.json" <<'PYCAPACITY'
import json
from pathlib import Path
import subprocess
import sys
memory = dict(line.split(':', 1) for line in Path('/proc/meminfo').read_text().splitlines())
available_memory = int(memory['MemAvailable'].split()[0]) * 1024
available_shm = int(subprocess.check_output(['df', '-B1', '--output=avail', '/dev/shm'], text=True).splitlines()[-1])
minimum = 32 * 1024**3
Path(sys.argv[1]).write_text(json.dumps({
    'memory_available_bytes': available_memory,
    'shm_available_bytes': available_shm,
    'required_available_bytes': minimum,
    'scenario_bytes': 24 * 1024**3,
    'default_reserve_bytes': 8 * 1024**3,
}, indent=2) + '\n')
assert min(available_memory, available_shm) >= minimum, 'Insufficient real capacity; no VM launch'
PYCAPACITY
run_step() {
  local suffix=$1 result=0
  shift
  "$@" >"$tracking/legacy-network-client-vm-$mode.$suffix.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/legacy-network-client-vm-$mode.$suffix.exit"
  return "$result"
}
run_step inventory ./test-runner.sh ls "$selector"
printf '%s\n' "$state_root" >"$tracking/legacy-network-client-vm-$mode.state.path"
result=0
./test-runner.sh test --jobs 1 --stop-on-failure --state-dir "$state_root" "$selector" \
  >"$tracking/legacy-network-client-vm-$mode.log" 2>&1 || result=$?
printf '%s\n' "$result" >"$tracking/legacy-network-client-vm-$mode.exit"
[[ $(git rev-parse HEAD) == "$head" && -z $(git status --porcelain) ]]
exit "$result"
