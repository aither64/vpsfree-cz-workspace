"""One guarded operator preparation of the existing private guest only."""
import datetime, hashlib, json, os, pathlib, shlex, stat, subprocess, sys
os.umask(0o077)
T = pathlib.Path(__file__).resolve().parent
prep = json.loads((T/'finish-working-delivery-public-update5-preparation.json').read_text())
packet = json.loads(pathlib.Path(prep['packet_path']).read_text())
root = pathlib.Path(packet['campaign_root']); directory = root/'state/clusters/same-slug'
selection = json.loads((T/'finish-working-delivery-package-realize5-acceptance.json').read_text())['selection']
failure = json.loads((T/'finish-working-delivery-public-update5-failure-disposition.json').read_text())
before = json.loads((root/'accepted-runtime.json').read_text())
baseline = json.loads((root/'continuity.json').read_text())
sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def private_json(path):
    path = pathlib.Path(path); observed = path.lstat()
    assert stat.S_ISREG(observed.st_mode) and observed.st_uid == os.getuid() and stat.S_IMODE(observed.st_mode) == 0o600 and observed.st_size <= 2*1024**2
    fd = os.open(path, os.O_RDONLY|os.O_NOFOLLOW)
    with os.fdopen(fd,'rb') as f:
        opened = os.fstat(f.fileno()); assert (opened.st_dev,opened.st_ino)==(observed.st_dev,observed.st_ino)
        return json.load(f)
journal = private_json(directory/'update.json')
assert journal == failure['journal'] | {'schema':1,'config_input_sha256':journal['config_input_sha256']}
artifact = directory/('artifact-'+journal['artifact_id']+'.json')
assert sha(artifact) == failure['candidate_artifact_sha256']
assert sha(root/'config.json') == prep['configuration_sha256']
assert sha(directory/'credentials/known_hosts') == prep['known_hosts_sha256']
for name, value in baseline['identities']['disks'].items():
    s=(directory/'disks'/name).lstat()
    assert stat.S_ISREG(s.st_mode) and s.st_uid==os.getuid() and {'device':s.st_dev,'inode':s.st_ino,'size':s.st_size}==value
process = private_json(directory/('processes-'+before['run_id']+'.json'))
assert process['complete'] is False and all(process[k]==before[k] for k in ('instance_id','run_id','artifact_id','artifact_sha256'))
runner = process['runner']; base=pathlib.Path('/proc',str(runner['pid']))
ticks=(base/'stat').read_text().rsplit(')',1)[1].split()[19]
assert base.stat().st_uid==runner['owner_uid']==os.getuid() and int(ticks)==runner['start_ticks']
assert pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip()==runner['boot_id']
assert os.readlink(base/'exe')==runner['executable'] and [x.decode() for x in (base/'cmdline').read_bytes().split(b'\0') if x]==runner['argv']
context=root.parent/'update-guest-preparation5'; context.mkdir(mode=0o700)
closure=before['provenance']['machine_toplevels']['services']; identity=pathlib.Path(closure)/'etc/vpsfree-kb-capture.json'
assert json.loads(identity.read_text())==before['provenance']['guest_identity']
guard='set -eu\numask 077\ntest "$(id -u)" = 0\ntest "${HOME-}" = /root\ntest "$(sha256sum /etc/vpsfree-kb-capture.json | cut -d " " -f 1)" = '+sha(identity)+'\ntest "$(readlink -f /run/current-system)" = '+shlex.quote(closure)+'\n'
backup='/root/.vpsfree-kb-update-preparation/'+journal['operation_id']
script=guard+'''test "${NIX_CONFIG+x}" != x
test "${NIX_USER_CONF_FILES+x}" != x
test "${NIX_CONF_DIR+x}" != x
test "${XDG_CONFIG_HOME+x}" != x
test ! -L /root
test ! -L /nix
test ! -L /nix/store
test "$(findmnt --raw -n --target / --output TARGET,FSTYPE,SOURCE,FSROOT)" = '/ ext4 /dev/sda /'
test "$(findmnt --raw -n --target / --output OPTIONS)" = 'rw,relatime'
test "$(findmnt --raw -n --target /nix/store --output TARGET,FSTYPE,SOURCE,FSROOT)" = '/nix/store ext4 /dev/sda[/nix/store] /nix/store'
test "$(findmnt --raw -n --target /nix/store --output OPTIONS)" = 'ro,nosuid,nodev,relatime'
test -w /nix/var/nix/db
for p in /root /root/.config /root/.config/nix /root/.vpsfree-kb-update-preparation; do
  test ! -L "$p"
  if test -e "$p"; then
    test -d "$p"; test "$(stat -c %u "$p")" = 0
    case "$(stat -c %a "$p")" in 700|750|755) ;; *) exit 30;; esac
  fi
done
config=/root/.config/nix/nix.conf
test ! -L "$config"
if test -e "$config"; then
  test -f "$config"; test "$(stat -c %u "$config")" = 0
  case "$(stat -c %a "$config")" in 600|640|644) ;; *) exit 31;; esac
  test "$(stat -c %s "$config")" -le 65536
fi
backup="$1"
test ! -e "$backup"; test ! -L "$backup"
mkdir -p /root/.vpsfree-kb-update-preparation
mkdir -m 700 "$backup"
printf '%s\n' 'ro,nosuid,nodev,relatime' > "$backup/store-options"
sha256sum /etc/nix/nix.conf | cut -d ' ' -f1 > "$backup/system-config.sha256"
if test -e "$config"; then
  cp -p -- "$config" "$backup/nix.conf.original"
  stat -c '%u %a' "$config" > "$backup/config.metadata"
  chmod 600 "$backup/nix.conf.original"
  sha256sum "$config" | cut -d ' ' -f1 > "$backup/config.original.sha256"
  : > "$backup/config.present"
else
  : > "$backup/config.absent"
fi
for p in /root/.config /root/.config/nix; do
  if ! test -d "$p"; then mkdir -m 700 "$p"; printf '%s\n' "$p" >> "$backup/created-directories"; fi
done
mount -o remount,bind,rw,nosuid,nodev,relatime /nix/store
test "$(findmnt --raw -n --target /nix/store --output TARGET,FSTYPE,SOURCE,FSROOT)" = '/nix/store ext4 /dev/sda[/nix/store] /nix/store'
test "$(findmnt --raw -n --target /nix/store --output OPTIONS)" = 'rw,nosuid,nodev,relatime'
test -w /nix/store; test -w /nix/var/nix/db
tmp=$(mktemp /root/.config/nix/nix.conf.kb-update-XXXXXX)
if test -f "$backup/config.present"; then cat "$backup/nix.conf.original" > "$tmp"; fi
printf '\nextra-experimental-features = nix-command\n' >> "$tmp"
chmod 600 "$tmp"; sync -f "$tmp"; mv -T -- "$tmp" "$config"
sha256sum "$config" | cut -d ' ' -f1 > "$backup/config.prepared.sha256"
test "$(sha256sum /etc/nix/nix.conf | cut -d ' ' -f1)" = "$(cat "$backup/system-config.sha256")"
nix path-info --recursive --json "$2" >/dev/null
printf 'prepared=1\nstore_writable=1\nplain_path_info_status=0\n'
printf 'config_original_present=%s\n' "$(test -f "$backup/config.present" && printf 1 || printf 0)"
printf 'config_prepared_sha256=%s\n' "$(cat "$backup/config.prepared.sha256")"
printf 'system_config_sha256=%s\n' "$(cat "$backup/system-config.sha256")"
'''
argv=[selection['runtime']+'/bin/vpsfree-kb-devcluster','--state-root',str(root/'state'),'ssh','same-slug','services','--','sh','-s','--',backup,closure]
with (context/'stdout').open('xb') as out,(context/'stderr').open('xb') as err:
    result=subprocess.run(argv,input=script.encode(),stdout=out,stderr=err,env=packet['environment'],cwd='/home/aither')
values={}
if result.returncode==0:
    values=dict(line.split('=',1) for line in (context/'stdout').read_text().splitlines())
    assert values['prepared']=='1' and values['store_writable']=='1' and values['plain_path_info_status']=='0'
record={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'native_exit_code':result.returncode,'complete':result.returncode==0,'values':values,'operator_preparation':True,'guest_backup_directory':backup,'source_ids':{k:before[k] for k in ('instance_id','run_id','artifact_id','artifact_sha256')},'exact_candidate':journal['artifact_id'],'candidate_artifact_sha256':failure['candidate_artifact_sha256'],'stdout_sha256':sha(context/'stdout'),'stderr_sha256':sha(context/'stderr'),'script_sha256':hashlib.sha256(script.encode()).hexdigest(),'limit':'Only authenticated private guest bind/user-config preparation. Immutable system/identity/trust unchanged. Failed public update remains failed; continuation not yet run. Backup/config values remain private; no imported path cleanup.'}
for p in (context/'proof.json',T/'finish-working-delivery-update-guest-preparation5.json'):
    with p.open('x') as f: json.dump(record,f,indent=2);f.write('\n')
print(json.dumps({'native_exit_code':result.returncode,'complete':record['complete'],'values':values}),flush=True)
sys.exit(result.returncode)
