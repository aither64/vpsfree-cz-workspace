# Development preview acceptance — 2026-11-03

The session preview is usable at **https://newadmin.aitherdev.int.vpsfree.cz/**.
The standard initial single/bridge start returned0 after1168.008 seconds.
Exact-session status reports running/ready. The applied selection has no pending
operation and retains full boot proof for services, node1 and both DNS guests.
The cluster and session remain running/open.

Use the development network/DNS and trust the workspace CA at
`.dev-clusters/vpsadmin/certs/default/vpsadmin-ca.crt`. Seeded Administrator and
member credentials are available privately in this session's portal under
React Web UI. No credential values belong in records or messages.

## Actual activation and access

- Services is running the applied system
  `/nix/store/gknys2a4d8csw8ppvwqk225yx5pb1bkr-nixos-system-vpsadmin-services-26.05pre-git`.
  The newadmin container and BFF are active; its system is
  `/nix/store/iknrj6hr91967agkjdplgmnwwl5vgvg5-nixos-system-newadmin-26.05pre-git`.
- CA-validated curl returned200 for `/healthz` (`ok`), build metadata, runtime
  config and `/app/vps`. The config selects this cluster's API7.0. A direct
  session request without same-origin context correctly returned403. A
  same-origin logged-out request returned200 with no token.
- Ordinary seeded-Administrator OAuth login reached the actual auth provider,
  returned to `/app` with200, and produced a BFF session with token, fingerprint
  and expiry present. Their values were neither printed nor recorded. Python's
  strict keyUsage flag was cleared only for this explicitly loaded development
  CA, following the existing workspace note; chain, hostname and expiry checks
  stayed enabled. Curl used ordinary `--cacert` without an insecure option.
- Served deep-route HTML, entry JavaScript and build metadata exactly match
  their active frontend package files. This is a bounded preview check, not a
  browser matrix or certification of every API operation.

## Source and packages

The active frontend is
`/nix/store/p5spjawkxdki3rjzznvrxp6fh9vfry33-vpsadmin-webui-frontend-1.0.0`;
the BFF is
`/nix/store/lwwafhip9lz8jv4b9r6xhm164svchacz-vpsadmin-webui-bff-0.1.0`.
Both derive from `/nix/store/7la9dx6gs44avsf7z0qa597pgc0f5lv1-source`.
All2574 included files, symlinks and executable modes match Git
`4ed519b69c422ea6b4fd0bd7bf490a20fcd6983e`. There are no extra source files;
the path source additionally retains the empty `vendor` directory. The public
frontend has only assets, build-info, favicon and index. All eight BFF own
runtime/package files match committed source and its runtime manifest.

The exact source/lock selects registry `vpsadmin-typescript-client@0.3.0` and
HaveAPI runtime0.32.0. The realized frontend derivation binds the same ordinary
fixed-output npm cache path/hash as the retained final Git package inspection.
That original inspection verified the337128-byte released archive SHA256
`57236647f4065a0ffeaabb0f5f6c64370a5ca4e7e530876b0d562c69651ce610`.
The cache archive is no longer resident, so no new direct cache-byte reading
is claimed. No download or realization was performed by implementer6.

The backend remains the bound clean API610a96 checkout. The actual shared OS
source matches all2367 files and modes at local staging
`5918f94e5e4eef3733b60aca4e03c1a6c0d43748`, without fetching. Node1's running
system matches the applied system
`/nix/store/rabiyg4qkl9gplmszqdq0kxb59vqigxz-vpsadminos-system-dev-node1-26.05pre-git`.

## Explicit preview limits

The standard provider selected Node24.22.1/Python3.13.17; the separate immutable
Git five-package acceptance used Node24.21.0/Python3.13.15. The frontend manifest's
declared Node range accepts24.22.1. The BFF has no separate engines restriction
and uses the provider's Node24 package. Both active package metadata files and
served build-info honestly report unknown/dirty/unavailable for the path input.
Selected-source labels do not replace that package metadata.

The earlier immutable Git output paths were absent. One authorized private
reconstruction changing only provenance values and the BFF wrapper self-path
did not match their retained NAR hashes. No artifact equivalence is claimed.
The later reference watcher refused before native execution because it selected
the wrong tracking path; no reference job remains active. Parent accepts these
recorded preview differences. No provider repin, repair, repeated normalization
or further build campaign followed. The successful independent Git package
acceptance remains evidence for its original inputs.

Sanitized full bindings and evidence: [acceptance JSON](devcluster-preview-acceptance.json).
Private native/log/probe artifacts stay under
`devcluster-preview-start-1d97b28021fc/`. The historical API2 cleanup uncertainty
remains unrelated and untouched. No reset, cleanup, deployment or lifecycle
action was performed.
