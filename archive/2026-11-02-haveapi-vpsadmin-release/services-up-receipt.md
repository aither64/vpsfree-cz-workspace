# Required packaged-content test

Exact source:5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5.
Original command: `./test-runner.sh test --jobs 1 --state-dir /tmp/hvrel-services-up-5586ea8ab services-up`.
Fresh pinned Luna/low utility services_up; original run, no retry/cancellation.
Passed exit0,~11m24s total,496.74s native script, all34examples passed.
Native test-result.txt: expected_success. Covers five shared doc routes and
generated Go/Rust/TypeScript examples through packaged API. No kernel build
escalation. Original wrapper/runner terminal, no owned running operation.

Config store output: /nix/store/4b7gsxfsdkazwsqyp1xb6g8kb0c3kbbj-os-test-vpsadmin-services-up.json.
Test state: /tmp/hvrel-services-up-5586ea8ab/os-test-services-up-3cba672b.
Full source graph: exact vpsAdmin head+flake.lock, pinned OS input
8e44a5124439b1f3048ffc56b1717614a5360358, package locks/gemset sources from A;
exact five gem bytes in vpsadmin-gem-hashes.json and A package receipt.
All fixture/export inputs separately bound in vpsadmin-schema-export-receipt.json.

Exact realized machine paths:

- toplevel: `/nix/store/swcpl7sk923b43yf9zzdgpw3lvy2i3ql-nixos-system-vpsadmin-services-26.05pre-git`.
- diskImage: `/nix/store/awskpqm2d668phf2b8kwpqkh6kamyym2-nixos-test-disk-image/nixos-test.img`.
- kernel: `/nix/store/c9ahm2mgq3fwz3f3g8xk78rs8gljmbwy-linux-6.12.104/bzImage`.
- initrd: `/nix/store/33858d8z8m5a7ydg9yzdpjycg2chw16b-initrd-linux-6.12.104/initrd`.
- qemu: `/nix/store/w4i3scdab4y1vp6wlkymx19gjgm80pka-qemu-host-cpu-only-for-vm-tests-10.2.4`.
- virtiofsd: `/nix/store/5k8lzdmn4xybrsw876ijv7mnrbmah4rq-virtiofsd-1.13.3`.

Full log services-up.log, native test-runner.log/test-result.txt retained during
active work. Brief parent monitoring interruption was reconciled against original
PID/log, same operation resumed. A later process snapshot proved VM running;
initial stdout only showed source derivation because native progress is per-test.
This is local VM verification, not machine deployment or broad CI completion.
