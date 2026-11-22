# confctl GC roots follow login identity

A host build through rootSSH plus sudo-H-uaither completed Nix output but failed
retention: Permission denied creating /nix/var/nix/gcroots/per-user/root.
ConfCtl::GCRoot.dir uses RubyEtc.getlogin, not effective UID or USER/LOGNAME.
Actual-host diagnostics showed UID/EUID1000 and USER/LOGNAMEaither but
Etc.getloginroot and /proc/self/loginuid0 inherited from SSH. Correct environment
variables do not fix that identity.

The normal workspace tool shell has UID1000/loginuid1000. Run the host build in
that local declared configuration Nix shell, checking Etc.getlogin is aither
before confctl. Do not create root GC directories, modify loginuid or relax their
permissions. Keep original failed log/generation; repeat only the host step,
using normal confctl recovery and a separately named retained candidate root.
The corrected local run built the host generation successfully; its independent private GC root was then confirmed. Application package/checks already passed and its
root/identity exist despite the aggregate batch failure.

Initiative: work/2026-10-02-portal-creation-performance/.
