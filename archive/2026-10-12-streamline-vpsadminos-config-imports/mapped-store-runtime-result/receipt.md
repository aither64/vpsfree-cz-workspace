# Corrected native-store focused runtime

Reviewed/published6abc650f/tree9393, runtime-attempt.dymifpby, /tmp/ni.ljm4450b,
upgrade26.05 only, terminal1/unexpected_failure. Fresh Luna/low watcher ran once;
runner1002.14s, example291.25s; exact elapsed differs by wrapper/image overhead.
No local kernel compile observed. Original state/logs remain retained/hashes bound.

Actual stopped per-variant closure-copy and registration succeed86.81s; boot0.
Old initial systemd stays degraded before old live switch/baseline. Actual failed
units are dbus-broker,dhcpcd,nscd,dbus.socket. Earlier logrotate wrong-owner failure
is absent from failed set; native store provisioning resolves that concrete
consumer symptom. Nonroot EXEC EACCES remains and no upgrade pass is established.

Lead source traced the new/nix dataset private root creation at0750 in libosctl
create_private!, retained when mounted directly as/nix. Nonroot nscd/dhcpcd and
broker credentials cannot traverse it while root init/exec works. Implementer0
is verifying the source/image relation and preparing only fresh/nix mode0755
setup if confirmed. This concerns a newly created empty fixture before accounts,
not existing persistent source/payload metadata. No provider/service/readiness
or assertion change. Next runtime follows focused check/fold/review gates.
