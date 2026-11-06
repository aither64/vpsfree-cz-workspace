# Candidate deployment preparation

2026-11-04: strict read-only refresh passed. Scope is only configured machine
`cz.vpsfree/containers/mx2`, VPS27627, root@172.19.9.22:22. Session/environment
identity matches. Feature is clean at reviewed/built
`0844881779d62d9a6a86d2bacd61d21565b33932`. Selected runtime
`/nix/store/myjy32qh6bd4avgym1awx180y29nvwz9-dev-workspace-0.2.0` supports
schema2 exact registered-repository Machine.name claims; no catalog edit is
needed. Lead owns claim13ba611e-2f87-4036-b958-b0e056e13da7 acquisition/verification,
copy and activation. No claim/copy/activation/mail was performed by this owner.

Local generation`2026-11-03--15-47-12` remains available. Toplevel
`/nix/store/4pc5mic0rp9h5qb2lhgmdh2x8z50pqd2-nixos-system-mx2-26.05.20261026.718f670`,
deriver`/nix/store/bpyiq4bfdmd9anf96zqyg8kqmyd3d9b0-nixos-system-mx2-26.05.20261026.718f670.drv`,
NAR`sha256-dGOqT6fHxNlWSfrfMGRzPem0RqpuLSzHLoWJ/CG5cjg=` match prior receipt.
Installed-in-output configuration-info binds clean084488; generation/output
inputs-info agree, rolepaths are unchanged and final lockSHA256 remains507e781c…
(full proof in staging-built-systems.json/staging-input-graph.json).

## Current guest

Single pinned-key strict SSH completed in0.65s, exit0, no stderr. Full selected
facts are in candidate-deployment-preflight.json. Host mx2, LXC,
NixOS25.05.git.7c43f080a; stateVersion25.05. Current/profile/booted all remain
`/nix/store/98n9xjgm42pjmzi9vy430qilp2hqbzvb-nixos-system-mx2-25.05.git.7c43f080a`.
System profile generation3 is current; old switch-to-configuration executable
exists. Root/var/nix remain ZFS tank/ct/27627[/private], rw.

venet0 has172.19.9.22/32 and link-localIPv6 only; IPv4 default gateway
255.255.255.254. Neither37.205.11.114 nor2a03:3b40:100::1:95 is configured.
Queue count0; Postfix/Postgrey/firewall/sshd active. Old node-exporter is active
and will be disabled by the reviewed candidate. rsyslog absent. Old resolvers
remain172.16.9.90/172.19.9.90/1.1.1.1; no confctl metadata is installed yet.
Canonical-primary DNS must be checked through actual candidate resolver after
activation before mail. No current primary-path or publicIPv6 claim is made.

## Exact lead command set

Run in the owned configuration worktree; these commands are prepared, unexecuted.
The0600 candidate-ssh.conf is local session data; it selects the existing
id_ed25519, IdentitiesOnly/BatchMode/StrictHostKeyChecking yes, exact known_hosts,
no forwarding/controlsharing/host-key updates,5s connect/one attempt. Local ssh-G
validated it. Trusted ED25519 host fingerprint remains
`SHA256:8gUL5bD+9+wpn1P6jfhUaKOtdoUhoFroLW8KcFcem6o`.

```sh
export CONFCTL_SSH_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-mx2-nixos-migration/candidate-ssh.conf
export NIX_SSHOPTS='-F /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-mx2-nixos-migration/candidate-ssh.conf'

nix develop --no-write-lock-file -c confctl deploy --yes --no-interactive --generation 2026-11-03--15-47-12 --enable-auto-rollback --copy-only cz.vpsfree/containers/mx2 switch
```

Lead then acquires and verifies the exact schema2 machine claim. Dry activation:

```sh
nix develop --no-write-lock-file -c confctl deploy --yes --no-interactive --generation 2026-11-03--15-47-12 --enable-auto-rollback cz.vpsfree/containers/mx2 dry-activate
```

Inspect the dry result/effects before the real switch under that same claim:

```sh
nix develop --no-write-lock-file -c confctl deploy --yes --no-interactive --generation 2026-11-03--15-47-12 --enable-auto-rollback --health-checks --no-keep-going cz.vpsfree/containers/mx2 switch
```

Generation pin selects existing native generation without building. Copy-only
copies toplevel+auto-rollback helper, returns before activation/profile/health.
Dry-activate invokes the ordinary system dry action and does not set profile.
There is no skip-copy flag: later commands can check/copy the same store paths.
MachineControl uses CONFCTL_SSH_CONFIG; nix-copy-closure inherits NIX_SSHOPTS.
No reboot is requested. Booted-system may remain98n9 until a subsequent reboot;
current-system and system profile must become4pc5 after successful switch.

## Native checks and recovery

Pinned confctl7bee58a5 sources inspected: cli/cluster.rb deploy/copy/activation,
nix_legacy.rb activation+profile, machine_control.rb SSH, nix_copy.rb transport,
and exact built auto-rollback helper. Native help confirms all options above.
Auto-rollback is enabled with60s timeout and snapshots /run/current-system.
It waits for confctl SSH confirmation, rolling back old runtime on timeout.
Profile is set after activation returns; health checks run afterward. Declared
checks require SystemState=running and firewall ActiveState=active; explicit
Postfix/Postgrey/DNS/access/persistence acceptance remains lead-owned.

The helper confirms reachability before application health checks and does not
undo a later health-check failure. Its Process.wait also does not inspect the
child switch exit status. Therefore inspect actual activation log, runtime and
profile paths and service health; an exit0 alone is insufficient. On interruption
reconcile the original command/helper first; preserve the claim and accepted
queues. Do not blindly replay switch or clear messages.

If recovery is necessary and state compatibility is confirmed, observed native
profile generation3 and its exact old activation provide this recovery command
under the same held claim (prepared, unexecuted):

```sh
ssh -F "$CONFCTL_SSH_CONFIG" root@172.19.9.22 'nix-env -p /nix/var/nix/profiles/system --switch-generation 3 && /nix/store/98n9xjgm42pjmzi9vy430qilp2hqbzvb-nixos-system-mx2-25.05.git.7c43f080a/bin/switch-to-configuration switch'
```

After recovery verify current/profile paths, strict SSH and services/queue; retain
all state. Automatic rollback handles runtime activation only; manual native
profile restoration reconciles profile if needed. No configuration integration
or old CentOS/public routing action is authorized here.

## Deployed-state correction checkpoint (2026-11-04)

Actual system/profile084488/4pc5 is deployed but unhealthy (Postgrey DB environment
startup and dynamic DNS priority); it is preserved in explicit local ref
`2026-11-01-mx2-nixos-migration-deployed-staging`. Original/import/runtime/mail
refs and existing full source/input/closure receipts remain intact.
Local DNS draft adds only host resolvconf.extraConfig public-server prepend.
Nixfmt/parse/whitespace and native generated resolver text pass; raw draft proof
is mx2-dns-draft-root.json. This is dirty-draft evaluation, not a new committed
head or realized/deployed output. No input update, commit/fold or remote action.
DB decision and user console access recovery remain pending; one combined
correction follows the architect brief.

## User reboot and actual booted state (2026-11-04)

User reported rebooting the candidate; no reboot was issued by this owner.
Strict streamed postboot read completed0.60s (first marker0.35s). Actual
current/profile/booted all4pc5 with clean084488 configuration-info, bootID
507276a8-af4c-4ff0-8769-d12f82669058, uptime39.88s. DBus/logind/SSH/Postfix/
firewall/resolvconf healthy, nojobs, queue0. Rawfacts: candidate-postboot.json.
Actual resolver is now solely1.1.1.1; primary A37.205.15.53 and
AAAA2a03:3b40:fe:1c3::1 resolve. The unnecessary uncommitted DNS draft was
removed, leaving feature clean at084488; its earlier draft evaluation is
historical, not a required source correction. Postgrey still fails Env startup
exit2 with existing258-owned DBfiles retained. No DB mutation or SMTP has run.

## Postgrey library compatibility proof and preserved state

Held claim13ba was authoritatively confirmed before the released backup work.
Postgrey is intentionally stopped/inactive, MainPID0, no job. Whole original
/var/postgrey remains unchanged; no live recovery/conversion/reset was attempted.
Protected backup root /root/mx2-postgrey-recovery-20261104-57422c4b is root:root0700;
backup/ preserves every original file and metadata, independently copied and
verified. original-metadata.txt SHA256
26b73c236d3cf37246dfb595f4fa481ce81fea98f4ac141c6c99220b9add841c;
original-sha256.txt SHA256
65054cc5a2da3827d84b1980c69182c0a2b2af4a888a3daa0bea023195b89e33.
Both manifests are protected root-only data; no database records were printed.

Old Postgrey1.37/BerkeleyDB0.65 Perl5.40 links DB5.3.28; deployed new1.37/0.65
Perl5.42 links DB4.8.30. Separate clone-db48 fails native Env recovery with
unsupported log version19 and DB_RUNRECOVERY; ENOENT was a misleading$! from
Postgrey. Separate clone-db53 opens the environment AND both existing Btree
databases successfully, exit0, without printing records. After tests, whole
live and untouched-backup hashes still matched original manifests. Total0.56s,
exit0; raw proof postgrey-backup-clone.json. Matching5.3 package is the bounded
proposed remedy, pending architect brief/lead source release. No live DB
conversion, source edit, package deployment, test mail or backup cleanup.

## Authorized unused greylist reset and initial SMTP (2026-11-04)

User explicitly authorized resetting the unused Postgrey DB. Protected complete
backup was verified again; old /var/postgrey was renamed atomically to
/root/mx2-postgrey-recovery-20261104-57422c4b/reset-original. Native preStart
created a fresh4.8 environment; no original files deleted/converted, no Postfix
spool reset. Postgrey active/no restart/socket+freshfiles healthy; systemrunning,
all3systempaths4pc5, clean084488, DNSprimary works, queue0. Raw:postgrey-reset.json.
This preserves original state as backup, not as continued active greylist history.

EHLO/greeting passed from actual172.16.106.40, SIZE104857600. Unrelated reserved
postmaster@example.org rejected RCPT5545.7.1 Relay access denied, noDATA. First
normal fixed475byte podpora->podpora payload got explicit preDATA450 native
300s greylist. Same payload/Message-ID retained for one retry after305s; no mail
accepted yet at this checkpoint. mx2-normal-smtp.json records timing/byteshash.
Banner mx2.localdomain and absent STARTTLS remain scoped private-stage residuals,
not authorization for a source expansion. No source/package/build was changed.

Persistent laterfault nativepath is listed/usr/local/lib/systemd/system, with
writable persistent/usr parent; standard dirs currently absent. Local rendered
unit+PostfixRequires drop-in hashes/addresses are in mx2-outage-plan.json. Both
chains and unit are absent; no remote fault files/rules were installed. Lead
acceptance is required before that verification mutation.
