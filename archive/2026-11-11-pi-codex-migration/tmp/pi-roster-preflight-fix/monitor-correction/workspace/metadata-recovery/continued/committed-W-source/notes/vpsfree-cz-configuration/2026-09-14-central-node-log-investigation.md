# Central node logs and livepatch attribution

For read-only investigations from aitherdev, use
`ssh root@log.int.prg.vpsfree.cz`. The shorthand `log.int` and
`log.int.vpsfree.cz` did not resolve in this environment.

Kernel/authentication logs are under
`/var/log/remote/cz.vpsfree/nodes/<location>/<node>/log`. Daily rotations are
`log-YYYYMMDD`; the suffix is the rotation date, so September 13 entries occur
in `log-20260914`. Node runit/svlogd output is in
`/var/log/remote/localhost/log`, with the node FQDN embedded in the message.
This layout is declared in
`cluster/cz.vpsfree/containers/prg/int.log/config.nix`.

The logger lacked rg; remote grep worked. Filter out container kernel messages
(`kernel [`) and routine daemon output when correlating host events, otherwise
firewall and filesystem logs can hide the useful lines in output truncation.

Authentication key fingerprints can be matched to data/ssh-keys.nix by hashing
the decoded public-key blob with SHA256. Correlation identifies a key/session;
normal SSH syslog does not prove the command text or the human using the key.

Verified: all three livepatch unloads on September 13–14, 2026 correlated within
102 ms of a matching root SSH session. No host changes were made.
Related initiative: work/2026-09-14-node1-stg-livepatch-unload/.
