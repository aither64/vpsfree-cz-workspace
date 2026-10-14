Pin network availability backend and WebUI changes

Update the vpsadmin/vpsadmin and vpsadmin-webui/vpsadmin-webui channel roles to
the reviewed feature heads from vpsfreecz/vpsadmin#45 and
vpsfreecz/vpsadmin-webui#19. The two canonical confctl commits retain generated
changelogs. Only the vpsadminServices and vpsadminWebui locked identities change;
the frontend continues following vpsadminServices for its backend input.

Normal hooks passed and the complete generated input diff was inspected.
All 12 affected-host builds passed at the exact configuration head
`dd10d88073da3aed6c4512e938abe4374422aab1`.
Consumers are the internal API, DB, RabbitMQ, Redis, VPS-admin and legacy WebUI
hosts, plus int.vpsadmin-webui1 (12 hosts total). The
[session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/)
records exact revisions, checks and remaining limitations.

Rollout requires the additive schema and every allocation writer upgraded
before any network is disabled. Existing service remains supported. Old API
rollback while disabled pools remain loses enforcement. This pin update does
not deploy services or retire production networks.
