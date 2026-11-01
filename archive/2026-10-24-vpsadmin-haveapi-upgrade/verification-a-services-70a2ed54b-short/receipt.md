# A post-review services and packaged API verification: passed

Owner implementer0; exact tested head `70a2ed54b98d0c2f359a9cc4484452a257a9807b`,
tree `f1cb0699d91ab11b461d94b1174bc43cf28f14ef`. Lead explicitly released this
retry after the prior socket-path setup failure was diagnosed and reconciled.
Both earlier failure receipts remain immutable; `prior-evidence-sha256.json`
inventories their bytes, checked unchanged after this run.

The ordinary `services-up` runner passed all **32 examples**. These include API
startup, all three shared documentation URLs, real Go/Rust example tabs and
registry installation hints, PHP public entrypoints/private-file rejection and
console-router direct/proxied assets. It ran with jobs1, caps16GiB memory/shm and
8CPUs, uniquely owned `/tmp/ha3.szlt_8sr/s`. The initial shell socket
budget was54 bytes<108; a later audit included the built-in vmSharedDir socket
and corrected the full maximum to63 bytes<108. This missing preflight category
is recorded explicitly; the completed run passed. see `socket-budget.json` and `ownership.json`.

`status.json` is authoritative: 2026-10-26 09:17:09–09:26:04 UTC, total535.207s;
services command513.703s including preparation; native test339.9s. All nine batch
stages returned0. Native logs and test-result are retained alongside outer logs.
The fresh pinned Luna/low watcher used full access/approval never; its exact
launch, brief and runtime header are retained. Its command acknowledgement is
in `RECEIPT/command-received.json` (it misread the receipt variable as a literal
subdirectory). Its elapsed estimate is inaccurate; use the script status above.
No duplicate execution or automatic retry occurred within this operation.

The API package was selected from the actual services VM closure, then its exact
derivation output was built/reused and its own wrapped Ruby executed:

- Test config `/nix/store/yg5zy73il8xbk13v67x8ljm5icza7dpz-os-test-vpsadmin-services-up.json`;
  derivation `/nix/store/vc12ywkckmlw352bkzkklrppbq5blc70-os-test-vpsadmin-services-up.json.drv`.
- System/profile `/nix/store/2war0njnsnki8srg4v3bwj9kpcl25v1z-nixos-system-vpsadmin-services-26.05pre-git`;
  derivation `/nix/store/340dsj1shc5h6q7qpwgqqra3s6havbzr-nixos-system-vpsadmin-services-26.05pre-git.drv`.
- API `/nix/store/jvjm1ixawf3zj3y1lylriznan3618dhg-vpsadmin-api-unknown`;
  derivation `/nix/store/h3ypi5yplww2pj52zbkhxy5xr61ixkmr-vpsadmin-api-unknown.drv`.
- Ruby environment `/nix/store/y54fk2516grll0jiq1qm9ll0rzipmr6k-vpsadmin-api-env-unknown`;
  wrapper `/nix/store/z23748wfzxc5izkzlspq32xdfa8nqybd-wrapped-ruby-vpsadmin-api-env-unknown`.

`paths.json`, `selected-test-packages.json`, `test-config.json`, full recursive
`{test,system,api}-recursive-derivations.json`, system closure and immutable
`flake-source-graph.json` capture the exact package/input/source graph. The
package's `unknown` revision label is preserved truthfully; its source identity
is bound by the captured graph and exact tested checkout, not inferred from
that label. Effective API, packaged API and flake locks are copied here.

Ruby3.4.9 loaded HaveAPI, Ruby client and both Go/Rust documentation adapters at
**0.30.2**, plus Fiddle1.1.8. `packaged-api-load.json` retains loaded gem/native
paths and six shared documentation/template/highlighting asset hashes.
`packaged-source-and-assets.json` proves context, Rust documentation and version
files match the verified release archives. Both actual packaged legacy bundles
match release SHA256 `96450c40a55ec7b7af4fca903d045bd0fc7ba1216efe12c3fee9b3e6a09e9198`.
`fiddle-linkage.log` proves its native extension links
`/nix/store/br4ikmi388vrj4bf8kd9nb3k2kiqprc0-libffi-3.8.0/lib/libffi.so.8`;
its complete closure is also retained.

Native machine logs record normal stop, QEMU exit0, kill with no signal and
destroy. `reconciliation.json` proves all recorded command PIDs absent and no
process argv/cwd/readable FD references the owned state. Source-before equals
source-after/final; fresh source/lock checks retain the clean exact head and all
initial hashes. No unexpected local kernel build, source/Git/pin/provider change,
live infrastructure operation, session lifecycle action or evidence deletion.
The exclusive watcher slot was released to lead in report
`55539820-109b-4c07-b12f-a4bb83c0bccc` before the next fresh watcher.

This passes the required packaged services/native dependency gate. API topics,
legacy console/browser scenarios and separate other-package verification remain
independent gates; no all-topic CI or deployment claim is made. Evidence-only
work requires no application documentation edit.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/)
