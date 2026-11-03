# Candidate staging preflight

Current result, 2026-11-03 14:14 UTC: after the user installed the existing public
key, a single strict pinned-key attempt succeeded. Candidate NixOS, private-only
addressing, current system and bounded state/storage/mail facts are recorded under
[Successful authorized preflight](#successful-authorized-preflight). No remote or
source mutation occurred. Earlier trust/authentication refusals below are retained
as historical evidence.

2026-11-03, 13:51:58 UTC. Result: strict SSH host trust is not established;
remote preflight did not run. No host, source or Git state was changed.

## Identity and supplied facts

`dev-session current`, both `DEV_SESSION_*` variables and trusted thread binding
agree on `2026-11-01-mx2-nixos-migration` at
`/home/aither/workspace/ai/vpsfree.cz`. Retained implementer0 is ready with
workspace_write, `gpt-6.1-sol` / xhigh; settings unchanged. Workspace and repository
instructions, applicable session/documentation/verification/deployment procedures,
staging plan, current state and verification results were read before probing.

User-supplied candidate address `172.19.9.22` and container/VPS ID `27627` match
the inherited source declaration. This match neither proves a collision with
CentOS nor justifies changing those identifiers. Container identity/placement
has not been remotely verified.

## Exact access result

Local effective SSH metadata resolves `root@172.19.9.22`, port 22, with no proxy,
host-key alias or canonicalization. Existing trust paths are
`/home/aither/.ssh/known_hosts`, `/home/aither/.ssh/known_hosts2` and
`/etc/ssh/ssh_known_hosts`. Normal credential selection was retained; no keys,
credentials or trust-file contents were read or printed.

Exactly one noninteractive connection used `BatchMode=yes`,
`StrictHostKeyChecking=yes`, `ConnectTimeout=5`, `ConnectionAttempts=1`, no PTY,
host-key updates disabled, no control sharing or forwarding, and no local
commands. No algorithm or trust relaxation was supplied. It returned exit 255:

```text
No ED25519 host key is known for 172.19.9.22 and you have requested strict checking.
Host key verification failed.
```

Stdout was empty; the bounded read-only remote allowlist never executed.
Authentication was not reached. No retry, scan, alternate host/credentials,
host-key acceptance, SMTP command, package operation, service change, build,
deployment or reboot occurred. Disposable structured probe evidence is
`candidate-preflight-probe.json`.

## Readiness and unknowns

| Item | Evidence/status |
| --- | --- |
| Intended candidate private address and ID | User supplied; matches source |
| Trusted SSH identity | Missing; ED25519 host key is not known for exact endpoint |
| Root authentication | Not tested because host trust failed first |
| Installed NixOS/version, hostname and virtualization | Unknown; no remote command ran |
| Installed system/profile paths and confctl source/input metadata | Unknown |
| Interface addresses, routes and resolver | Unknown |
| Absence of `37.205.11.114` and `2a03:3b40:100::1:95` | Unverified; must be established before staging |
| Mail service and queue existence/count | Unknown; no mail/queue content inspected |
| Persistent storage and first-installed stateVersion | Unknown; not inferred from the planned source setting |

No application change is established by this probe. Preserve the matching private
target/container ID. Staging source adaptations in the prepared plan still need
architect reconciliation against actual host facts; the historical public
addresses, automatic update selection and production monitoring identity must not
be assumed safe for the candidate merely because private endpoint/ID match.

Next prerequisite: obtain this candidate's ED25519 host-key identity/fingerprint
through the trusted console/control-panel/operator channel, verify it, and
establish the intended local SSH trust through the approved workflow. Do not use
an unauthenticated scan as identity proof or silently accept a new key. After
that prerequisite and a new authorized strict attempt, inspect the already
bounded host/network/storage/mail metadata before deciding minimal source changes.
No further remote access is attempted by this package.

Lead owns plan/state and architect reconciliation. The session remains active;
no machine/repository claim or lifecycle action was needed for this read-only
preflight. [Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-mx2-nixos-migration/).

## Verified trust and resumed attempt

The user supplied this candidate ED25519 fingerprint in the current chat after
the request for trusted console/existing-SSH identity:

```text
SHA256:8gUL5bD+9+wpn1P6jfhUaKOtdoUhoFroLW8KcFcem6o
```

Session identity, saved ready/workspace_write and Sol/xhigh settings were
reverified unchanged. At 14:06:58 UTC, one bounded `ssh-keyscan -T 5 -p 22 -t
ed25519 172.19.9.22` obtained only ED25519 key material for that exact endpoint.
The scan was not treated as identity proof; local `ssh-keygen -lf - -E sha256`
computed a fingerprint byte-for-byte equal to the user-supplied trusted value.

Before trust mutation, effective target remained root, port 22, no proxy/alias.
No exact-host entry existed in ordinary user/global known-host files; the second
user file was absent. The existing ordinary user file was a regular nonsymlink,
owned by this user with mode 0600, inside a user-owned 0700 `.ssh` directory.
Appended only one exact `172.19.9.22` verified ED25519 entry with an advisory file
lock, append-only write, conflict recheck and inode/owner/permission checks.
Unrelated content and concurrent append changes were preserved. No key was
replaced, no global trust changed and no permissions relaxed. Public key material
was not copied into this report; structured verification is in disposable
`candidate-trust-verification.json`.

At 14:07:21 UTC, exactly one resumed strict noninteractive attempt used normal
credential selection, BatchMode/StrictHostKeyChecking enabled, five-second
connect timeout, one connection attempt, no PTY/forwarding/control sharing/local
commands and host-key updates disabled. Host identity verification succeeded,
but authentication returned exit 255:

```text
root@172.19.9.22: Permission denied (publickey,password,keyboard-interactive).
```

Stdout was empty and the remote allowlist never executed. No retry, alternate
credential, password/authentication prompt, key installation on the candidate or
further remote discovery followed. See disposable
`candidate-preflight-probe-verified.json` for the exact result/time.

The current access prerequisite is **root authentication**, not host identity.
The operator must authorize/install the agreed existing deployment public key or
otherwise restore the intended normal root SSH access through their trusted
console workflow. This package does not inspect private keys, add candidate user
keys or change SSH policy. After that access prerequisite is satisfied, lead can
authorize the same bounded strict preflight without repeating trust setup.

All remote facts in the original unknowns table remain unknown: installed OS and
system/profile/source metadata, addresses/routes/resolver, actual absence of the
old public IPv4/IPv6, persistent storage/stateVersion and mail queue/service state.
The supplied private IP and ID still match source and should be preserved. No
source delta is justified from this authentication refusal; architect retains
the staging boundary decision after actual host evidence becomes available.

Only the explicitly authorized local exact-host trust entry changed. No remote,
application, repository/Git, deployment, mail, resource-claim or lifecycle change
occurred. The session remains open and active; no command remains running.

## Concrete existing public-key access prerequisite

Local-only follow-up found one unambiguous existing file identity among the
effective defaults for `root@172.19.9.22`: `/home/aither/.ssh/id_ed25519` and
its adjacent existing `.pub`. The other effective RSA/ECDSA/security-key/MLDSA
file paths are absent. Public-key authentication is enabled; `IdentitiesOnly`
is currently `no`, with no explicit IdentityAgent override. The identity file
is a readable user-owned regular nonsymlink at mode 0600. Only path metadata
was inspected for that file; no private contents or signing operation were read
or used. No unrelated agent keys were requested or printed.

The operator can add this single existing public key as one line to the
candidate root account's `authorized_keys` through its trusted console:

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJlvsbOljzxEs7PHmiZHPo4Vcr9QfmWwlqvVZpGVAL6h aither@aitherdev
```

Its locally computed public fingerprint is
`SHA256:38gX47C2LkQgccktDtHa27hPk8wXo3kXLMGUQSnswK0` (ED25519, 256 bits).
This is the client authentication key, distinct from the already verified
candidate host-key fingerprint above.

No `IdentityFile` or `IdentitiesOnly` change is required to select it: it is
already an effective default and the only existing file identity. A later bounded
probe may explicitly pin `-i /home/aither/.ssh/id_ed25519 -o IdentitiesOnly=yes`
for deterministic selection if lead directs; that uses the existing credential.
Existence/readability and `.pub` metadata establish the available normal identity,
not a successful signature or authentication result. No retry, signing test,
private-key read, new key generation, agent forwarding or remote action occurred
during this local-only follow-up. Root access remains unverified until the
operator completes the authorized console step and lead resumes strict preflight.

## Successful authorized preflight

The user reported the public key installed and authorized agent deployment to the
exact candidate: “done. well, with this access, you can deploy mx2 yourself.” Lead
released only the bounded read-only preflight at this step; source/design, review,
machine reservation and deployment remain subsequent lead-owned work. No merge,
public-address transfer, primary change or real-mail authorization was inferred.

Reverified current session/environment, retained workspace_write/Sol/xhigh and
architect identity. One strict attempt at 14:14:51 UTC used
`-i /home/aither/.ssh/id_ed25519 -o IdentitiesOnly=yes`, BatchMode and strict
host-key checking, five-second connect timeout, one connection attempt, no PTY,
forwarding/control sharing/local command/host-key update. It completed exit 0,
empty stderr and the full bounded allowlist end marker. No retry was needed.
Disposable exact output is `candidate-preflight-probe-authorized.json`.

| Observation | Actual candidate evidence |
| --- | --- |
| Hostname / OS | `mx2`; NixOS `25.05.git.7c43f080a` (Warbler) |
| Virtualization | `lxc` |
| Current system, system profile, booted system | All `/nix/store/98n9xjgm42pjmzi9vy430qilp2hqbzvb-nixos-system-mx2-25.05.git.7c43f080a` |
| Confctl source/input receipt | Both `/etc/confctl/configuration-info.json` and `inputs-info.json` absent |
| Nonloopback IPv4 | `venet0`: `172.19.9.22/32` |
| Nonloopback IPv6 | Link-local only: `fe80::780b:8aff:fe2c:b7d0/64`; no global address |
| Old public IPs | Neither `37.205.11.114` nor `2a03:3b40:100::1:95` configured |
| IPv4 routes | Default via `255.255.255.254` on `venet0`; gateway link route |
| IPv6 routes | Link-local `fe80::/64` only; no IPv6 default route |
| Resolver order | `172.16.9.90`, `172.19.9.90`, `1.1.1.1`; resolvconf-generated |
| Root, `/var`, `/nix` mount | Same read-write ZFS root `tank/ct/27627[/private]` |
| State-version evidence | Known bootstrap file `/etc/nixos/configuration.nix` explicitly has `system.stateVersion = "25.05";` |
| Mail services | Postfix and Postgrey loaded/active/running; rspamd not found |
| Existing mail paths | `/var/lib/postfix`, `/var/lib/postfix/queue`, `/var/postgrey` present |
| Queue count | `postqueue -j` record count 0; no queue content printed |

The guest's ZFS path corroborates supplied ID 27627. It does not establish the
physical node or provisioning ownership outside this guest. The persistent root
mount and existing paths are positive storage evidence, but no restart or
rollback has yet tested durability on this actual candidate. StateVersion 25.05
is a directly observed configuration line, not inferred from the OS release.

Selected current Postfix evidence:

- `myhostname = mx2.localdomain`; local `mydestination`; relay_domains and
  relay-restriction output are legacy compatibility expressions. No modern
  explicit three-domain relay configuration is claimed installed.
- Existing transport map reference is `hash:/etc/postfix/transport`. The map's
  contents were not read. Recipient restrictions retain Postgrey at
  `/run/postgrey.sock`, original DNSBLs and legacy `reject_unauth_destination`.
- `mynetworks` includes only loopback, the candidate private IPv4 and its
  link-local IPv6 host addresses; no arbitrary client network was inferred.
- Milter `inet:localhost:11332`, failure action `accept`; rspamd absent.
- Empty inbound TLS level/chain output; outbound `smtp_tls_security_level = may`.
- Message limit `10240000`; queue `/var/lib/postfix/queue`, data
  `/var/lib/postfix/data`.

This installed system is an older candidate configuration, not the final built
1e3afc47 closure. Existing active mail services and the zero queue are facts from
this probe; no SMTP listener, firewall ACL, actual resolver answers, outbound
TCP25/NAT identity or real-primary acceptance was tested. No MAIL/RCPT/DATA,
mail body, recipient-map content, secret or arbitrary configuration dump was read.

Minimal source implications for architect reconciliation: retain the matching
private management target, ID and observed 25.05 stateVersion. Replace historical
public address declarations with actual private-only candidate metadata, keep
automatic bulk updates and production monitoring/logging identity out of staging,
and define the temporary identity, resolver view and restricted ingress boundary.
No new public allocation or assumed CentOS/IP collision is justified. Physical
placement remains unverified; do not rewrite it from a guess. Keep tested shared
mail behavior unchanged unless the architect's concrete staging boundary requires
an explicit documented constraint.

Lead received the facts promptly; architect0 was directly notified through the
same-session native team channel. Application/Git/source edits remain frozen
until architect's final execution package is released. No remote changes, build,
deployment, reboot, primary operation, real mail, claim or lifecycle action was
performed. No command remains running after reporting.

## Required staging source/DNS follow-up

Architect explicitly requested the single additional combined read-only call to
select the narrow candidate ACL and resolver boundary. It ran at 14:21:08 UTC
with the same strict pinned-key settings, exit 0 and no mutation:

```text
SSH_CONNECTION=172.16.106.40 55958 172.19.9.22 22
```

The observed workspace SSH source is therefore `172.16.106.40`; it is distinct
from the candidate's private endpoint. This gives concrete input for the
staging-only source allowlist, without assuming an externally observed NAT address.

The guest has no `dig` executable. The planned canonical-primary A/AAAA queries
through current resolver and separately `1.1.1.1` did not run. No package was
installed and no fallback/extra remote probe or SMTP operation was attempted.
Actual candidate DNS answers remain unknown. Exact output is in disposable
`candidate-source-dns-probe.json`; architect and lead received results directly.
Source/Git remain unchanged pending the executable architect package and lead
release. The objective is deployment of the prepared new branch to this candidate,
not treating its old installed closure as the new configuration.
