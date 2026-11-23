# Keep oomd acting on other containers during a pending restart

Integrate the verified vpsAdminOS change that keeps an outstanding restart or stop
from preventing action against another eligible container. The lean Top sampler
continues reading known containers while its inventory request is outstanding.
Oomd checks each target's current run and scores eligible peers on usable partial
samples. The existing per-container guard and action slots bound dispatch.

The user approved integration into vpsfreecz/vpsadminos staging. The interactive
Top proposal is deferred. This delivery uses the exact locally reviewed and
VM-tested commits. It changes neither persisted state nor the daemon protocol.
The packaged osctl and osctl-oomd should be updated together when deployed.
The operational contract is in docs/os/oomd.md in the OS repository.

Recover the commits from the verified bundle, publish the feature branch, capture
its comparison, and fast-forward staging under the repository claim. Verify the
remote head and report the resulting CI status.
