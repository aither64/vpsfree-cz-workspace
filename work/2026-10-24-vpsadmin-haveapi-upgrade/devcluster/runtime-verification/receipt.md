# Package E runtime handoff — 2026-10-26

**Ready for qualified current manual testing; cluster left running.** Both real
`test-user1` OAuth logins passed (2/2), followed by explicit logout (2/2).
Main state, integration decisions and commits remain lead-owned.

| Interface | Live URL | Completed check |
| --- | --- | --- |
| PHP | <https://webui.aitherdev.int.vpsfree.cz/> | Member login/logout; English and Czech controls selected |
| React | <https://newadmin.aitherdev.int.vpsfree.cz/> | Member login/logout; authenticated API 7 reads returned 200 |
| API | <https://api.aitherdev.int.vpsfree.cz/> | `/v7.0/` reads, including React `/users/current`, returned 200 |
| OAuth | <https://auth.aitherdev.int.vpsfree.cz/> | Both login flows returned to the intended interface |

Access requires the internal development network/DNS, cluster CA trust and
credentials from native private access or portal secret fields. No passwords,
tokens, cookies, screenshots or browser traces were recorded in this evidence.
No VPS operations were performed.

Public CA: `/home/aither/workspace/ai/vpsfree.cz/.dev-clusters/vpsadmin/certs/default/vpsadmin-ca.crt`.
SHA-256 fingerprint:
`1C:60:3B:7C:2C:95:48:ED:32:DC:3B:49:33:5A:AF:89:C9:54:F0:7D:EE:04:77:07:03:1B:C6:7C:AD:FB:57:14`.
Curl with `--cacert` and Chromium with an isolated session-local NSS CA database
verified HTTPS; errors were not ignored and host-wide trust was not changed.
Python 3.13 strict SSL rejected the existing CA's missing keyUsage extension;
that limitation does not describe the successful curl/browser checks.
See [TLS evidence](tls-curl.json) and [actual login results](member-login.json).

React `session.json` returned 200 with `accessToken`, `sessionKey`,
`sessionExpiresAt` keys; no values were emitted. The harness's optional
`session.authenticated=false` projection reflects absent `authenticated`/`user`
fields, not failed login. PHP's optional body substring check did not find the
login name; its authenticated logout form and completed flow provided the
recorded authentication evidence. React locale switching was not exercised.
The [executed harness](member-login.cjs) preserves these exact boundaries.

## Running selection and independent guest proof

Parent-owned attempt `../activation/20261026T153200Z/` completed native exit 0
at `1793030138.153` (15:55:38 UTC). Lead accepted strict post-exit canonical
running/ready=true/single/bridge status, runner `2882335` with exact native tuple,
and four QEMU processes (`2891713`, `2896888`, `2898197`, `2898599`) resident in
`vpsadmin-haveapi-upgrade-e-20261026T153200Z.scope`. Limits remained 32 GiB,
zero swap, 12 CPUs, zero OOM. Global Nix daemon load was accounted separately;
two jobs/four cores were requests, not an aggregate daemon limit.
See [native result](../activation/20261026T153200Z/result.json).

Runtime `w6j9bzb…`, provider `q19s1vj…`, native contract
`9c8e9e5c371eda46ccb49eaf275ee4996d2ddce3930c9047da39ccd195f67183`,
schema 1/policy 3. Accepted clean API:
`70a2ed54b98d0c2f359a9cc4484452a257a9807b`; clean React:
`f10d3d48c4f21cc39187c3667ffffd9952404c11`; native OS:
`d9be8c4bada590c0405df85444600d40e6f3caa6`.
The accepted 20-node graph and explained API `cwrqv2…` source remain in
[pre-start evidence](../prestart-20261026T150732Z/verdict.md) and
[source comparison](../refresh-w6j9bzb-20261026T142452Z/source-comparison/conclusion.md); no standalone artifact
reuse/equality is claimed.

Independent guest checks passed **4/4**: dns-primary, dns-secondary, node1 and
services each match their exact selected current-system and booted-system;
every requisite passes `nix-store --check-validity`; each selected system has a
`system-1-link` root. Exact toplevels and root lists are retained in
[guest evidence](guest-residency.json), SHA-256
`dd39f3b135448a46d773447ee2f423d3870eca789e7bcdd4d4b4afe95459c1eb`.

**Provider certificate limitation:** the extra provider-applied root exists only
on dns-primary. The installed SSH-in-while-read loop consumes remaining input,
so its complete applied-envelope claim lacks all-guest proof. This does not
mean the other current closures lack roots. Independent current proof supports
manual testing, not future cold-recovery/pruning or a complete old applied
certificate. The separately reviewed/published fix is **not installed**.
No provider, guest root or preparation-root repair/change was made. Architect's
assessment is in `design.md`; original [diagnostic](guest-residency-diagnostic.json)
is preserved.

The selected services closure contains all four HaveAPI gems (`haveapi`,
`haveapi-client`, `haveapi-go-client`, `haveapi-rust-client`) at **0.30.2**, API
and supervisor at `70a2ed54…`, and the selected frontend/BFF packages. Native
selected WebUI provenance reports clean worktree `f10d3d48…`. Selected PHP
Composer installed metadata and lock both identify `haveapi/client` **0.30.2**.
These are **packaged identities**: no per-process gem introspection or independent
running frontend/BFF file hashing was performed. Exact package paths and
Composer evidence: [closure inventory](selected-packages.json),
[metadata](packaged-identities-kernel-outputs.json).

## Six kernel alerts and retained boundaries

All six original HALT records remain intact: three modules-shrunk builders use
`modules-closure.sh`; three initrd builders use `make-initrd-ng` plus reproducible
cpio/compression. Their actual builders establish module/archive assembly,
not kernel compilation; the broad version-name regex produced false positives.
See [exact derivations](kernel-alert-derivations.json) and
[structured initrd commands](kernel-initrd-classification.json).
Actual kernel outputs `4k5kg…` and `6sn4…` were locally registered at
`1792663862` and `1792878283`, both before attempt 153200; full paths/NARs are
in [kernel output metadata](packaged-identities-kernel-outputs.json).
Alerts arrived at `1793030138.10–.12`, immediately before completion;
buffered stderr/progress prevents precise build-time claims.

No startup retry, signal, teardown, source/provider installation, root repair,
host policy/global trust change, foreign-hold action, KB/staging/production
write or session lifecycle action was performed by these runtime checks.
Existing cluster and roots remain running/retained. No further polls or probes
are assigned for this handoff; merge readiness is a separate lead decision.

Session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/>.
