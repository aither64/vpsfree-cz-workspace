"""Restore only the recorded private guest operator settings after acceptance."""
import datetime,hashlib,json,os,pathlib,shlex,subprocess,sys
os.umask(0o077)
T=pathlib.Path(__file__).resolve().parent
prep=json.loads((T/'finish-working-delivery-public-update5-preparation.json').read_text())
packet=json.loads(pathlib.Path(prep['packet_path']).read_text());root=pathlib.Path(packet['campaign_root'])
selection=json.loads((T/'finish-working-delivery-package-realize5-acceptance.json').read_text())['selection']
operator=json.loads((T/'finish-working-delivery-update-guest-preparation5.json').read_text())
post=json.loads((T/'finish-working-delivery-public-update5-proof.json').read_text())
assert post['complete'] and post['old_complete_process_receipt'] and post['public_member_api_php_and_lease']
connection=json.loads(pathlib.Path(post['connection_path']).read_text())
assert connection['provenance']['source']['revision']==prep['generator']
assert connection['artifact_id']==operator['exact_candidate'] and connection['artifact_sha256']==operator['candidate_artifact_sha256']
context=root.parent/'update-guest-restoration5';context.mkdir(mode=0o700)
closure=connection['provenance']['machine_toplevels']['services']; identity=pathlib.Path(closure)/'etc/vpsfree-kb-capture.json'
assert json.loads(identity.read_text())==connection['provenance']['guest_identity']
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
guard='set -eu\numask 077\ntest "$(id -u)" = 0\ntest "${HOME-}" = /root\ntest "$(sha256sum /etc/vpsfree-kb-capture.json | cut -d " " -f1)" = '+sha(identity)+'\ntest "$(readlink -f /run/current-system)" = '+shlex.quote(closure)+'\n'
script=guard+'''backup="$1"
expected="$2"
test ! -L "$backup"; test -d "$backup"
test "$(stat -c %u "$backup")" = 0; test "$(stat -c %a "$backup")" = 700
for p in /root /root/.config /root/.config/nix; do test ! -L "$p"; test -d "$p"; test "$(stat -c %u "$p")" = 0; done
config=/root/.config/nix/nix.conf
test ! -L "$config"; test -f "$config"; test "$(stat -c %u "$config")" = 0; test "$(stat -c %a "$config")" = 600
test "$(sha256sum "$config" | cut -d ' ' -f1)" = "$expected"
test "$(cat "$backup/config.prepared.sha256")" = "$expected"
test "$(findmnt --raw -n --target / --output TARGET,FSTYPE,SOURCE,FSROOT)" = '/ ext4 /dev/sda /'
test "$(findmnt --raw -n --target /nix/store --output TARGET,FSTYPE,SOURCE,FSROOT)" = '/nix/store ext4 /dev/sda[/nix/store] /nix/store'
options=$(findmnt --raw -n --target /nix/store --output OPTIONS)
case "$options" in 'ro,nosuid,nodev,relatime') ;; 'rw,nosuid,nodev,relatime') mount -o remount,bind,ro,nosuid,nodev,relatime /nix/store;; *) exit 32;; esac
test "$(findmnt --raw -n --target /nix/store --output OPTIONS)" = "$(cat "$backup/store-options")"
if test -f "$backup/config.present"; then
  test ! -L "$backup/nix.conf.original"; test -f "$backup/nix.conf.original"
  test "$(sha256sum "$backup/nix.conf.original" | cut -d ' ' -f1)" = "$(cat "$backup/config.original.sha256")"
  tmp=$(mktemp /root/.config/nix/nix.conf.kb-restore-XXXXXX)
  cat "$backup/nix.conf.original" > "$tmp"
  read owner mode < "$backup/config.metadata"; test "$owner" = 0
  case "$mode" in 600|640|644) ;; *) exit 33;; esac
  chmod "$mode" "$tmp"; sync -f "$tmp"; mv -T -- "$tmp" "$config"
  test "$(sha256sum "$config" | cut -d ' ' -f1)" = "$(cat "$backup/config.original.sha256")"
  printf 'config_original_restored=1\nconfig_original_absence_restored=0\n'
else
  test -f "$backup/config.absent"
  rm -- "$config"
  if test -f "$backup/created-directories"; then
    # Remove only the recorded directories, in reverse nesting order and only empty.
    for p in /root/.config/nix /root/.config; do
      if grep -Fxq "$p" "$backup/created-directories"; then rmdir -- "$p"; fi
    done
  fi
  printf 'config_original_restored=0\nconfig_original_absence_restored=1\n'
fi
printf 'store_original_options_restored=1\n'
'''
argv=[selection['runtime']+'/bin/vpsfree-kb-devcluster','--state-root',str(root/'state'),'ssh','same-slug','services','--','sh','-s','--',operator['guest_backup_directory'],operator['values']['config_prepared_sha256']]
with (context/'stdout').open('xb') as out,(context/'stderr').open('xb') as err:
    result=subprocess.run(argv,input=script.encode(),stdout=out,stderr=err,env=packet['environment'],cwd='/home/aither')
values=dict(line.split('=',1) for line in (context/'stdout').read_text().splitlines()) if result.returncode==0 else {}
record={'schema':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'native_exit_code':result.returncode,'complete':result.returncode==0,'generator':prep['generator'],'source_ids':{k:connection[k] for k in ('instance_id','run_id','artifact_id','artifact_sha256')},'values':values,'stdout_sha256':sha(context/'stdout'),'stderr_sha256':sha(context/'stderr'),'script_sha256':hashlib.sha256(script.encode()).hexdigest(),'limit':'Recorded private user-config bytes/absence and private-bind options only restored after new-source proof. No imported closures/roots removed, no immutable source/config/trust change, backup retained privately.'}
for p in (context/'proof.json',T/'finish-working-delivery-update-guest-restoration5.json'):
    with p.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
print(json.dumps({'native_exit_code':result.returncode,'complete':record['complete'],'values':values}),flush=True)
sys.exit(result.returncode)
