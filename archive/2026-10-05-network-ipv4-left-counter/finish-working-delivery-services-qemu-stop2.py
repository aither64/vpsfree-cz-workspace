#!/usr/bin/env python3
"""One proposed operator action; requires explicit user approval before signalling."""
import json
import os
from pathlib import Path
import signal
import subprocess
import sys

if sys.argv[1:] not in (["--prepare-only"], ["--approved-by-user"]):
    raise SystemExit("Select prepare-only; signalling requires the user's explicit approval")
tracking = Path(__file__).resolve().parent
proof_path = tracking / "finish-working-delivery-services-qemu-disposition2.json"
proof = json.loads(proof_path.read_text())
if proof["source"] != "f467934d3f678abc8b552f89805636d4d910438a":
    raise SystemExit("Unexpected source")
pid = proof["qemu_tuple"]["pid"]
guard = r'''
require 'json'; require 'digest'
require '/nix/store/xllyhnv9ba1d49f9fvdwbpgxaf04phdf-source/cluster/lib/kb_state.rb'
require '/nix/store/xllyhnv9ba1d49f9fvdwbpgxaf04phdf-source/cluster/lib/kb_process.rb'
expected = JSON.parse(File.read(ARGV.fetch(0)))
s = KbRuntime::State.new('/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-working3/campaign/state', 'same-slug')
ids = expected.fetch('source_ids')
run = ids.fetch('run_id')
p = s.read(s.path("processes-#{run}.json")); l = s.read(s.path("launch-#{run}.json"))
raise 'phase changed' unless s.read(s.path('phase.json')) == { 'schema' => 1, 'phase' => 'stopping', 'run_id' => run }
raise 'foreign retained root' unless l['state_root'] == s.root && l['state_dir'] == s.path('disks') && l['owner_uid'] == Process.uid && l['slug'] == s.slug && s.identity['instance_id'] == ids['instance_id']
raise 'receipt changed' unless p['schema'] == 1 && p['complete'] == false &&
  ids.all? { |k,v| p[k] == v && l[k] == v }
raise 'runner changed' unless KbRuntime::ProcessIdentity.runner_matches?(p.fetch('runner'), l)
t = p.fetch('children').find { |c| c['pid'] == expected.fetch('qemu_tuple').fetch('pid') }
raise 'target changed' unless t && KbRuntime::ProcessIdentity.matches?(t) &&
  Digest::SHA256.hexdigest(JSON.generate(t)) == expected.fetch('qemu_tuple_sha256') &&
  t.slice(*expected.fetch('qemu_tuple').keys) == expected.fetch('qemu_tuple') &&
  t['owner_uid'] == Process.uid && t['argv'].each_cons(2).include?(['-name', 'os-vm-services']) &&
  t['argv'].any? { |a| a.include?(File.join(s.path('disks'), 'services-root.img')) }
puts 'confirmed'
'''
process_fd = os.pidfd_open(pid, 0)
try:
    checked = subprocess.run(
        ["/nix/store/k5zrvznvg3h4b7spivvflxsb1xxw1i0k-ruby-3.4.9/bin/ruby",
         "-e", guard, str(proof_path)],
        capture_output=True, text=True, close_fds=True, check=True,
    )
    if checked.stdout.strip() != "confirmed":
        raise SystemExit("Ownership guard did not confirm the selected target")
    sent = sys.argv[1] == "--approved-by-user"
    if sent:
        signal.pidfd_send_signal(process_fd, signal.SIGTERM)
    print(json.dumps({"pid": pid, "ownership_confirmed": True,
                      "pidfd_used": True, "signal_sent": "SIGTERM" if sent else None,
                      "limits": "No other signal, reap, reset, deletion or guest launch performed"}))
finally:
    os.close(process_fd)
