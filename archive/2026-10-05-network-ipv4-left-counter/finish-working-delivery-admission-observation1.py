import datetime
import fcntl
import hashlib
import json
import os
import pathlib
import socket
import stat
import subprocess

T = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
read = lambda n: json.loads((T / n).read_text())
a = read('finish-working-delivery-package-realize1-acceptance.json')
c = read('finish-working-delivery-private-config1.json')
reset = read('finish-working-delivery-g14-reset1.json')
assert reset['native_exit_code'] == 0 and reset['cluster_tree_absent']
assert not pathlib.Path(c['campaign_root']).exists()
assert hashlib.sha256(pathlib.Path(c['configuration']['path']).read_bytes()).hexdigest() == c['configuration']['sha256']
files = []
seen = set()
growth = 0
for old in read('finish-working-delivery-capacity-observation1.json')['files']:
    if old['campaign'] == 'G14':
        assert not os.path.lexists(old['path'])
        continue
    q = pathlib.Path(old['path'])
    s = q.lstat()
    assert stat.S_ISREG(s.st_mode) and [s.st_dev, s.st_ino, s.st_size] == [old['device'], old['inode'], old['apparent_bytes']]
    key = (s.st_dev, s.st_ino)
    assert key not in seen
    seen.add(key)
    remainder = max(0, s.st_size - s.st_blocks * 512) if '/disks/' in str(q) else 0
    growth += remainder
    files.append({'campaign': old['campaign'], 'path': str(q), 'device': s.st_dev, 'inode': s.st_ino,
                  'apparent_bytes': s.st_size, 'allocated_bytes': s.st_blocks * 512, 'remaining_writable_growth_bytes': remainder})

selection = a['selection']
environment = {k: os.environ[k] for k in ['HOME', 'USER', 'LOGNAME'] if k in os.environ}
environment.update(PATH=selection['path'], LANG='C.UTF-8', XDG_RUNTIME_DIR='/run/user/1000')
findmnt = next(str(pathlib.Path(p) / 'findmnt') for p in selection['path'].split(':') if pathlib.Path(p, 'findmnt').is_file())
roles = {}
for role, path in {'state_images': c['private_parent'], 'store': '/nix/store', 'builder_scratch': '/nix/var/nix/builds'}.items():
    s = pathlib.Path(path).stat()
    fs = os.statvfs(path)
    mounted = subprocess.run([findmnt, '--json', '--target', path, '--output', 'TARGET,FSTYPE'], env=environment, check=True, capture_output=True, text=True)
    fields = json.loads(mounted.stdout)['filesystems'][0]
    roles[role] = {'path': path, 'device': s.st_dev, 'mountpoint': fields['target'], 'fstype': fields['fstype'], 'available_bytes': fs.f_bavail * fs.f_frsize}
conf = pathlib.Path('/etc/nix/nix.conf').read_text()
build_fields = [line for line in conf.splitlines() if line.strip().startswith('build-dir')]
assert not build_fields, 'Daemon scratch override needs actual filesystem reconciliation'
systemctl = '/nix/store/khnfirshq5j299s6sfj0laxj0vr7gaa6-systemd-260.2/bin/systemctl'
manager = subprocess.run([systemctl, '--user', 'show', '--property=Version', '--property=ControlGroup'], check=True, capture_output=True, text=True)
user_manager = dict(line.split('=', 1) for line in manager.stdout.splitlines() if '=' in line)
ram = int(next(l for l in pathlib.Path('/proc/meminfo').read_text().splitlines() if l.startswith('MemAvailable:')).split()[1]) * 1024
shm = os.statvfs('/dev/shm')
with open('/dev/kvm', 'rb') as kvm:
    kvm_api = fcntl.ioctl(kvm.fileno(), 0xAE00, 0)

# Reuse the selected SDK's private reader and registry comparison; do not create claims.
ruby = next(str(pathlib.Path(p) / 'ruby') for p in selection['path'].split(':') if pathlib.Path(p, 'ruby').is_file())
script = """require 'json';require 'digest';require 'socket';require File.join(ARGV[0], 'cluster/lib/kb_resources')
s=KbRuntime::State.new(ARGV[1], 'planning'); cfg=s.read(ARGV[2]); local=cfg.fetch('local'); host=local.fetch('bindAddress'); wanted=local.fetch('ports').values.flat_map{|v|v.values.map{|p|{'kind'=>'tcp','host'=>host,'port'=>p}}};wanted<<{'kind'=>'udp','host'=>'0.0.0.0','port'=>local.fetch('multicastPort')};r=KbRuntime::Resources.new(s);s.private_directory(r.root)||raise('registry absent');claims=Dir.glob(File.join(r.root,'*.json')).sort.map{|p|v=s.read(p);raise('requested resource remains claimed') if v.fetch('resource_claims').any?{|x|wanted.any?{|w|r.conflicting?(w,x)}};{'path'=>p,'sha256'=>Digest::SHA256.hexdigest(s.file(p))}};probes=[];begin;wanted.each{|w|if w['kind']=='tcp';probes<<TCPServer.new(w['host'],w['port']);else;x=Socket.new(Socket::AF_INET,Socket::SOCK_DGRAM,0);probes<<x;x.bind(Socket.sockaddr_in(w['port'],w['host']));end};puts JSON.generate({'root'=>r.root,'claims'=>claims,'conflicts'=>false,'bind_probes_held_together'=>wanted.size,'reservation_created'=>false});ensure;probes.each(&:close);end
"""
registry = subprocess.run([ruby, '-e', script, a['source'], c['private_parent'], c['configuration']['path']], env=environment, check=True, capture_output=True, text=True)
record = {'schema': 1, 'generator': a['generator'], 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'scope': 'Fresh post-approved-reset named-file/host/registry/bind observations; no image or guest launch',
          'retained_disks': files, 'retained_growth_bytes': growth, 'roles': roles,
          'ram_available_bytes': ram, 'shm_available_bytes': shm.f_bavail * shm.f_frsize, 'kvm_api': kvm_api,
          'user_manager': user_manager, 'exec_cgroup': pathlib.Path('/proc/self/cgroup').read_text().strip(),
          'daemon_build_directory': '/nix/var/nix/builds', 'system_nix_conf_build_fields': build_fields,
          'registry': json.loads(registry.stdout), 'reset_proof': 'finish-working-delivery-g14-reset1.json',
          'operation_admitted': False}
with (T / 'finish-working-delivery-admission-observation1.json').open('x') as output:
    json.dump(record, output, indent=2); output.write('\n')
print(json.dumps({'free_GiB': min(x['available_bytes'] for x in roles.values()) / 1024**3,
                  'retained_growth_GiB': growth / 1024**3, 'ram_available_GiB': ram / 1024**3,
                  'shm_available_GiB': record['shm_available_bytes'] / 1024**3,
                  'kvm_api': kvm_api, 'port_conflicts': False, 'guest_launched': False}))
