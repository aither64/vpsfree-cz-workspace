# mx2 upgrade: live D-Bus transition and Postgrey log compatibility

The private mx2 candidate moved from NixOS25.05 to the reviewed26.05 system.
A live switch changed the D-Bus unit from notify with explicit ReloadConfig to
notify-reload/dbus-broker while the old dbus-daemon was still running. The reload
waited for acknowledgments that the old daemon could not provide. Restarting the
broker cleared the reload, but disconnected the original activator's system bus.
Confctl's wrapper returned0 despite stopped mail units. The native activator's
retained /run/nixos start/restart/reload lists proved incomplete work; a native
same-generation recovery consumed those lists. A later clean guest reboot restored
fast SSH sessions and correct resolver output. The operator correctly identified
boot plus reboot as the better deployment method for this transition.

Postgrey1.37/Perl BerkeleyDB0.65 also changed underlying library from5.3.28 to4.8.30.
The application reported only "can't create DB environment: No such file or
directory", although directory and file ownership were correct. A complete
protected backup and separate clones exposed unsupported log version19 under4.8;
the matching5.3 library opened the environment and both databases. Neither clone
test changed the live files. The operator confirmed the candidate had never been
used and explicitly authorized resetting its unused greylist state. The old
environment and verified backup were retained; native service startup created a
fresh4.8 environment and became healthy. Postfix queue/spool was never reset.

These are distinct from CentOS queue migration or a production database-reset
procedure. Preserve operator authorization, underlying-library evidence and
rollback state; service health and actual booted/current/profile paths matter
more than wrapper exit status.

Evidence: work/2026-11-01-mx2-nixos-migration, candidate postboot/reset/clone
receipts and mx2-activation-recovery.log. Exact deployed source08448817 and system
4pc5mic0rp9h5qb2lhgmdh2x8z50pqd2 remain in session records.
