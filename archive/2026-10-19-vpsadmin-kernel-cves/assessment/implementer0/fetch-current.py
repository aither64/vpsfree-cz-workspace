import concurrent.futures,datetime,hashlib,json,pathlib,urllib.request
s=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves');o=s/'assessment/implementer0'
linux='1dfea587406b7dd79973831d1677fb2418e5e9aa';jobs=[]
files=['io_uring/io_uring.c','io_uring/sqpoll.c','fs/exec.c','kernel/time/posix-cpu-timers.c','security/landlock/fs.c','security/landlock/syscalls.c','security/landlock/setup.c','net/unix/garbage.c','fs/fuse/dev.c','fs/fuse/inode.c','security/keys/keyctl_pkey.c','security/keys/asymmetric_keys/asymmetric_type.c','security/keys/key.c','security/keys/encrypted-keys/encrypted.c','kernel/events/core.c','arch/x86/events/intel/Makefile','arch/x86/events/intel/pt.c','arch/x86/kvm/ioapic.c','arch/x86/kvm/vmx/nested.c','arch/x86/kvm/vmx/vmx.c','arch/x86/kvm/vmx/evmcs.c','arch/x86/kvm/vmx/hyperv.c','kernel/bpf/syscall.c','kernel/bpf/token.c','kernel/bpf/verifier.c','net/core/filter.c','net/core/xdp.c','net/core/skmsg.c','include/linux/bpf.h','kernel/locking/spinlock_rt.c','kernel/locking/rwbase_rt.c','net/ipv4/inet_connection_sock.c','net/ipv4/ip_output.c','net/packet/af_packet.c','drivers/net/tun.c']
for p in files:jobs.append(('linux',linux,p))
base=json.loads((s/'research/platform-evidence/source-manifest.json').read_text())
for x in base:
 if x['repository'] in ['vpsadminos','vpsadmin','lxc']:jobs.append((x['repository'],x['revision'],x['path']))
for p in ['AGENTS.md','README.md','cluster/all.nix','environments/production.nix']:
 jobs.append(('vpsfree-cz-configuration','a2ad6da408715de811cc6d8ea7b29ac55ea341ec',p))
def one(j):
 repo,rev,p=j;u=f'https://raw.githubusercontent.com/vpsfreecz/{repo}/{rev}/{p}';q=o/'source'/repo/p;q.parent.mkdir(parents=True,exist_ok=True)
 try:
  b=q.read_bytes() if q.exists() else urllib.request.urlopen(u,timeout=20).read();q.write_bytes(b)
  return dict(repository=repo,revision=rev,path=p,url=u,file=str(q.relative_to(s)),sha256=hashlib.sha256(b).hexdigest(),retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
 except Exception as e:return dict(repository=repo,revision=rev,path=p,url=u,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:rows=list(ex.map(one,jobs))
(o/'current-source-manifest.json').write_text(json.dumps(rows,indent=2)+'\n');print('retrieved',sum('error'not in x for x in rows),'/',len(rows));print([x for x in rows if 'error'in x])
